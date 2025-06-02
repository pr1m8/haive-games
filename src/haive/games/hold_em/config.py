"""Texas Hold'em configuration module.

This module provides configuration classes for the Hold'em game, including:
    - Game agent configuration
    - Player agent configurations
    - Engine configurations
"""

import uuid
from typing import Dict, List, Optional, Tuple

from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field

from haive.games.hold_em.engines import build_holdem_game_engines, build_player_engines
from haive.games.hold_em.game_agent import HoldemGameAgentConfig
from haive.games.hold_em.player_agent import HoldemPlayerAgentConfig
from haive.games.hold_em.state import HoldemState


def create_default_holdem_config(
    num_players: int = 4,
    starting_chips: int = 1000,
    small_blind: int = 10,
    big_blind: int = 20,
) -> HoldemGameAgentConfig:
    """Create a default Hold'em game configuration."""

    print(f"🎮 Creating default Hold'em configuration...")
    print(f"   Players: {num_players}")
    print(f"   Starting chips: {starting_chips}")
    print(f"   Blinds: {small_blind}/{big_blind}")

    # Validate inputs
    if num_players < 2 or num_players > 8:
        raise ValueError("Number of players must be between 2 and 8")
    if starting_chips <= 0:
        raise ValueError("Starting chips must be positive")
    if big_blind <= small_blind:
        raise ValueError("Big blind must be greater than small blind")

    # Create player configurations
    player_configs = []
    player_names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Eve",
        "Frank",
        "Grace",
        "Henry",
    ][:num_players]
    player_styles = [
        "tight",
        "loose",
        "aggressive",
        "passive",
        "balanced",
        "tricky",
    ] * 2
    player_styles = player_styles[:num_players]

    print(f"🎭 Creating {num_players} player configurations...")

    for i, (name, style) in enumerate(zip(player_names, player_styles)):
        print(f"   Setting up {name} ({style} style)")

        # Build engines for this player with error handling
        try:
            player_engines = build_player_engines(name, style)
            engine_count = len(player_engines)
            print(f"     ✅ Built {engine_count} engines for {name}")

            # Validate engines
            if not validate_player_engines(player_engines):
                print(f"     ⚠️ Engine validation failed for {name}")

        except Exception as e:
            print(f"     ❌ Error building engines for {name}: {e}")
            player_engines = create_fallback_engines(name, style)
            print(f"     🔄 Using fallback engines for {name}")

        # Create player config
        try:
            player_config = HoldemPlayerAgentConfig(
                name=f"player_{name.lower()}",
                player_name=name,
                player_style=style,
                risk_tolerance=0.3 + (i * 0.1),  # Vary risk tolerance
                engines=player_engines,
                state_schema=HoldemState,
                runnable_config=RunnableConfigManager.create(
                    thread_id=str(uuid.uuid4()), recursion_limit=50
                ),
            )
            player_configs.append(player_config)
            print(f"     ✅ Created config for {name}")

        except Exception as e:
            print(f"     ❌ Error creating config for {name}: {e}")
            raise ValueError(f"Failed to create player config for {name}: {e}")

    print(f"🎯 Building game engines...")

    # Build game engines with error handling
    try:
        game_engines = build_holdem_game_engines()
        print(f"   ✅ Built {len(game_engines)} game engines")
    except Exception as e:
        print(f"   ❌ Error building game engines: {e}")
        game_engines = create_fallback_game_engines()
        print(f"   🔄 Using fallback game engines")

    # Create main game configuration
    try:
        game_config = HoldemGameAgentConfig(
            name="holdem_game",
            state_schema=HoldemState,
            max_players=num_players,
            small_blind=small_blind,
            big_blind=big_blind,
            starting_chips=starting_chips,
            max_hands=100,
            player_configs=player_configs,
            engines=game_engines,
            runnable_config=RunnableConfigManager.create(
                thread_id=str(uuid.uuid4()), recursion_limit=200
            ),
        )

        print(f"✅ Created game configuration successfully")
        print(f"   {len(player_configs)} players configured")
        print(f"   {len(game_engines)} game engines")

        return game_config

    except Exception as e:
        print(f"❌ Error creating game configuration: {e}")
        raise ValueError(f"Failed to create game configuration: {e}")


def create_tournament_config(
    num_players: int = 6,
    starting_chips: int = 1500,
    blind_levels: Optional[List[Tuple[int, int]]] = None,
) -> HoldemGameAgentConfig:
    """Create a tournament-style configuration with escalating blinds."""

    print(f"🏆 Creating tournament configuration...")

    if blind_levels is None:
        blind_levels = [
            (10, 20),
            (15, 30),
            (25, 50),
            (50, 100),
            (75, 150),
            (100, 200),
            (150, 300),
            (200, 400),
        ]

    # Start with the first blind level
    config = create_default_holdem_config(
        num_players=num_players,
        starting_chips=starting_chips,
        small_blind=blind_levels[0][0],
        big_blind=blind_levels[0][1],
    )

    # Add tournament-specific metadata
    config.metadata = {
        "tournament_mode": True,
        "blind_levels": blind_levels,
        "current_level": 0,
        "hands_per_level": 10,
        "level_duration_minutes": 20,
    }

    print(f"   Tournament with {len(blind_levels)} blind levels")
    print(f"   Starting level: {blind_levels[0][0]}/{blind_levels[0][1]}")

    return config


def create_cash_game_config(
    num_players: int = 6,
    big_blind: int = 20,
    max_buy_in: int = 2000,
    min_buy_in: int = 400,
) -> HoldemGameAgentConfig:
    """Create a cash game configuration."""

    print(f"💰 Creating cash game configuration...")

    small_blind = big_blind // 2
    starting_chips = max_buy_in

    # Validate buy-in amounts
    if min_buy_in >= max_buy_in:
        raise ValueError("Min buy-in must be less than max buy-in")
    if min_buy_in < big_blind * 20:
        print(f"⚠️ Warning: Min buy-in ({min_buy_in}) is less than 20 big blinds")

    config = create_default_holdem_config(
        num_players=num_players,
        starting_chips=starting_chips,
        small_blind=small_blind,
        big_blind=big_blind,
    )

    # Add cash game specific settings
    config.max_hands = 200  # Longer sessions
    config.metadata = {
        "cash_game_mode": True,
        "max_buy_in": max_buy_in,
        "min_buy_in": min_buy_in,
        "rebuy_allowed": True,
        "stack_to_bb_ratio": starting_chips // big_blind,
    }

    print(f"   Buy-in range: {min_buy_in} - {max_buy_in}")
    print(f"   Starting stacks: {starting_chips // big_blind} BB")

    return config


def create_heads_up_config(
    player1_name: str = "Alice",
    player2_name: str = "Bob",
    starting_chips: int = 1000,
    big_blind: int = 20,
) -> HoldemGameAgentConfig:
    """Create a heads-up (2 player) configuration."""

    print(f"🥊 Creating heads-up configuration: {player1_name} vs {player2_name}")

    # Create specialized player configs for heads-up
    player_configs = []

    for i, name in enumerate([player1_name, player2_name]):
        # Adjust styles for heads-up play
        style = "aggressive" if i == 0 else "balanced"  # First player more aggressive

        print(f"   Setting up {name} ({style} style for heads-up)")

        # Build engines for this player with heads-up flag
        try:
            player_engines = build_player_engines(name, style, heads_up=True)
            print(f"     ✅ Built {len(player_engines)} engines for {name}")

            if not validate_player_engines(player_engines):
                print(f"     ⚠️ Engine validation failed for {name}")

        except Exception as e:
            print(f"     ❌ Error building engines for {name}: {e}")
            player_engines = create_fallback_engines(name, style)
            print(f"     🔄 Using fallback engines for {name}")

        # Create player config with higher risk tolerance for heads-up
        try:
            player_config = HoldemPlayerAgentConfig(
                name=f"player_{name.lower()}",
                player_name=name,
                player_style=style,
                risk_tolerance=0.6 + (i * 0.2),  # Higher risk tolerance for heads-up
                engines=player_engines,
                state_schema=HoldemState,
                runnable_config=RunnableConfigManager.create(
                    thread_id=str(uuid.uuid4()), recursion_limit=50
                ),
            )
            player_configs.append(player_config)
            print(f"     ✅ Created heads-up config for {name}")

        except Exception as e:
            print(f"     ❌ Error creating config for {name}: {e}")
            raise ValueError(f"Failed to create heads-up config for {name}: {e}")

    # Build game engines
    try:
        game_engines = build_holdem_game_engines()
        print(f"   ✅ Built {len(game_engines)} game engines")
    except Exception as e:
        print(f"   ❌ Error building game engines: {e}")
        game_engines = create_fallback_game_engines()
        print(f"   🔄 Using fallback game engines")

    # Create heads-up specific configuration
    try:
        config = HoldemGameAgentConfig(
            name="holdem_heads_up",
            state_schema=HoldemState,
            max_players=2,
            small_blind=big_blind // 2,
            big_blind=big_blind,
            starting_chips=starting_chips,
            max_hands=50,
            player_configs=player_configs,
            engines=game_engines,
            runnable_config=RunnableConfigManager.create(
                thread_id=str(uuid.uuid4()), recursion_limit=200
            ),
        )

        config.metadata = {
            "heads_up_mode": True,
            "fast_fold": True,  # Faster decision making
            "aggressive_play": True,
        }

        print(f"✅ Created heads-up configuration")
        return config

    except Exception as e:
        print(f"❌ Error creating heads-up configuration: {e}")
        raise ValueError(f"Failed to create heads-up configuration: {e}")


class HoldemGameSettings(BaseModel):
    """Settings for customizing Hold'em games."""

    # Basic game settings
    num_players: int = Field(default=6, ge=2, le=8, description="Number of players")
    starting_chips: int = Field(
        default=1000, gt=0, description="Starting chips per player"
    )
    small_blind: int = Field(default=10, gt=0, description="Small blind amount")
    big_blind: int = Field(default=20, gt=0, description="Big blind amount")
    max_hands: int = Field(default=100, gt=0, description="Maximum hands to play")

    # Game variant settings
    tournament_mode: bool = Field(default=False, description="Tournament vs cash game")
    heads_up: bool = Field(default=False, description="Heads-up mode")
    fast_fold: bool = Field(default=False, description="Allow fast folding")

    # AI behavior settings
    ai_aggression: float = Field(
        default=0.5, ge=0, le=1, description="Overall AI aggression level"
    )
    ai_variance: float = Field(
        default=0.3, ge=0, le=1, description="Variance in AI play styles"
    )
    decision_time: float = Field(
        default=2.0, gt=0, description="Time for AI decisions (seconds)"
    )

    # Analysis settings
    enable_hand_analysis: bool = Field(
        default=True, description="Enable detailed hand analysis"
    )
    enable_opponent_modeling: bool = Field(
        default=True, description="Enable opponent modeling"
    )
    enable_position_analysis: bool = Field(
        default=True, description="Enable position analysis"
    )

    def to_game_config(self) -> HoldemGameAgentConfig:
        """Convert settings to a game configuration."""

        if self.heads_up:
            return create_heads_up_config(
                starting_chips=self.starting_chips, big_blind=self.big_blind
            )
        elif self.tournament_mode:
            return create_tournament_config(
                num_players=self.num_players, starting_chips=self.starting_chips
            )
        else:
            return create_cash_game_config(
                num_players=self.num_players,
                big_blind=self.big_blind,
                max_buy_in=self.starting_chips * 2,
            )


def validate_player_engines(engines: Dict[str, AugLLMConfig]) -> bool:
    """Validate that player engines are properly configured."""
    required_engines = [
        "decision_maker",
        "situation_analyzer",
        "hand_analyzer",
        "opponent_analyzer",
    ]

    missing_engines = []
    for engine_name in required_engines:
        if engine_name not in engines:
            missing_engines.append(engine_name)

    if missing_engines:
        print(f"❌ Missing required engines: {missing_engines}")
        return False

    # Validate engine configuration
    for engine_name, engine in engines.items():
        try:
            if not hasattr(engine, "structured_output_model"):
                print(f"⚠️ Engine {engine_name} missing structured_output_model")
            if not hasattr(engine, "prompt_template"):
                print(f"⚠️ Engine {engine_name} missing prompt_template")
        except Exception as e:
            print(f"❌ Error validating engine {engine_name}: {e}")
            return False

    return True


def create_fallback_engines(
    player_name: str, player_style: str
) -> Dict[str, AugLLMConfig]:
    """Create minimal fallback engines if the main engine creation fails."""
    from haive.core.models.llm.base import AzureLLMConfig
    from langchain_core.prompts import ChatPromptTemplate

    from haive.games.hold_em.models import (
        BettingDecision,
        GameSituationAnalysis,
        OpponentModel,
        PokerAnalysis,
    )

    print(f"🔄 Creating fallback engines for {player_name}")

    # Use a simple model for fallback
    fallback_model = AzureLLMConfig(model="gpt-4o-mini", temperature=0.7)

    # Create minimal prompts
    simple_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"You are {player_name}, a {player_style} poker player. Make decisions based on the situation.",
            ),
            ("human", "Situation: {situation}. Make your decision."),
        ]
    )

    try:
        return {
            "decision_maker": AugLLMConfig(
                name=f"{player_name}_fallback_decision_maker",
                llm_config=fallback_model,
                prompt_template=simple_prompt,
                structured_output_model=BettingDecision,
                force_tool_choice=True,
                description=f"Fallback decision maker for {player_name}",
                structured_output_version="v1",
            ),
            "situation_analyzer": AugLLMConfig(
                name=f"{player_name}_fallback_situation_analyzer",
                llm_config=fallback_model,
                prompt_template=simple_prompt,
                structured_output_model=GameSituationAnalysis,
                force_tool_choice=True,
                description=f"Fallback situation analyzer for {player_name}",
                structured_output_version="v1",
            ),
            "hand_analyzer": AugLLMConfig(
                name=f"{player_name}_fallback_hand_analyzer",
                llm_config=fallback_model,
                prompt_template=simple_prompt,
                structured_output_model=PokerAnalysis,
                force_tool_choice=True,
                description=f"Fallback hand analyzer for {player_name}",
                structured_output_version="v1",
            ),
            "opponent_analyzer": AugLLMConfig(
                name=f"{player_name}_fallback_opponent_analyzer",
                llm_config=fallback_model,
                prompt_template=simple_prompt,
                structured_output_model=OpponentModel,
                force_tool_choice=True,
                description=f"Fallback opponent analyzer for {player_name}",
                structured_output_version="v1",
            ),
        }
    except Exception as e:
        print(f"❌ Failed to create fallback engines: {e}")
        return {}


def create_fallback_game_engines() -> Dict[str, AugLLMConfig]:
    """Create minimal fallback game engines."""
    from haive.core.models.llm.base import AzureLLMConfig
    from langchain_core.prompts import ChatPromptTemplate

    print(f"🔄 Creating fallback game engines")

    fallback_model = AzureLLMConfig(model="gpt-4o-mini", temperature=0.3)

    simple_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a poker game narrator."),
            ("human", "Describe: {situation}"),
        ]
    )

    try:
        return {
            "game_narrator": AugLLMConfig(
                name="fallback_game_narrator",
                llm_config=fallback_model,
                prompt_template=simple_prompt,
                description="Fallback game narration",
                structured_output_version="v1",
            )
        }
    except Exception as e:
        print(f"❌ Failed to create fallback game engines: {e}")
        return {}


def create_custom_holdem_config(settings: HoldemGameSettings) -> HoldemGameAgentConfig:
    """Create a custom Hold'em configuration from settings."""
    return settings.to_game_config()


def validate_config(config: HoldemGameAgentConfig) -> Tuple[bool, List[str]]:
    """Validate a game configuration and return issues found."""
    issues = []

    # Validate basic settings
    if config.max_players < 2 or config.max_players > 8:
        issues.append("max_players must be between 2 and 8")

    if config.starting_chips <= 0:
        issues.append("starting_chips must be positive")

    if config.big_blind <= config.small_blind:
        issues.append("big_blind must be greater than small_blind")

    if config.max_hands <= 0:
        issues.append("max_hands must be positive")

    # Validate player configs
    if len(config.player_configs) != config.max_players:
        issues.append(
            f"Expected {config.max_players} player configs, got {len(config.player_configs)}"
        )

    # Check for duplicate player names
    player_names = [pc.player_name for pc in config.player_configs]
    if len(set(player_names)) != len(player_names):
        issues.append("Duplicate player names found")

    # Validate engines
    for i, player_config in enumerate(config.player_configs):
        if not validate_player_engines(player_config.engines):
            issues.append(
                f"Player {i} ({player_config.player_name}) has invalid engines"
            )

    return len(issues) == 0, issues
