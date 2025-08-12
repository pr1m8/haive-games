import uuid
from enum import Enum
from typing import Any, Literal

from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field, ValidationInfo, computed_field, field_validator

from haive.games.monopoly.engines import build_monopoly_player_aug_llms
from haive.games.monopoly.player_agent import MonopolyPlayerAgent, PlayerDecisionState
from haive.games.monopoly.state import MonopolyState
from haive.games.monopoly.utils import create_board, create_players, shuffle_cards

r"""Comprehensive configuration system for strategic Monopoly gameplay and real.
estate management.

This module provides sophisticated configuration management for Monopoly agents with
support for advanced gameplay features, strategic AI customization, and flexible
game rule variations. The configuration system enables complex economic simulations
from casual family games to competitive tournament play.

The configuration system supports:
- Complete game rule customization with house rules and variants
- Advanced AI strategy parameters for realistic economic decision-making
- Multi-player configurations with different AI personalities
- Economic simulation parameters for property development
- Trading and negotiation system configuration
- Performance optimization for different gameplay scenarios
- Comprehensive validation and error handling

Examples:
    Standard family game configuration::\n

        config = MonopolyGameAgentConfig.family_game()
        agent = MonopolyGameAgent(config)

    Tournament-level competitive play::\n

        config = MonopolyGameAgentConfig.tournament()
        # Advanced AI with trading and strategic analysis

    Economic simulation for research::\n

        config = MonopolyGameAgentConfig.economic_simulation()
        # Complex market dynamics and property development

    Custom house rules variant::\n

        config = MonopolyGameAgentConfig(
            player_names=["Alice", "Bob", "Charlie"],
            enable_trading=True,
            enable_building=True,
            enable_auctions=True,
            starting_money=2000,
            free_parking_bonus=True,
            double_go_salary=True
        )

Note:
    All configurations use Pydantic for validation and support both JSON serialization
    and integration with distributed game systems for multiplayer online play.
"""


class GameDifficulty(str, Enum):
    """Enumeration of game difficulty levels for AI strategy.

    Defines different difficulty levels that affect AI decision-making,
    strategic depth, and negotiation complexity.

    Values:
        EASY: Simple decision-making, basic property management
        MEDIUM: Balanced strategy with moderate complexity
        HARD: Advanced strategic analysis and complex negotiations
        EXPERT: Maximum strategic depth with economic optimization

    """

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


class GameVariant(str, Enum):
    """Enumeration of popular Monopoly game variants.

    Defines different rule sets and game configurations based on
    popular Monopoly variants and house rules.

    Values:
        CLASSIC: Traditional Monopoly rules
        SPEED: Fast-paced variant with reduced game time
        CITY: Modern urban-focused property themes
        ELECTRONIC: Digital banking and modern features
        CUSTOM: User-defined rule combinations

    """

    CLASSIC = "classic"
    SPEED = "speed"
    CITY = "city"
    ELECTRONIC = "electronic"
    CUSTOM = "custom"


class MonopolyPlayerAgentConfig(AgentConfig):
    r"""Advanced configuration for individual Monopoly player AI agents.

    This class provides comprehensive configuration for AI players, including
    strategic parameters, personality traits, and decision-making preferences.
    The configuration enables realistic player behavior simulation with varying
    skill levels and strategic approaches.

    The configuration supports:
    - Strategic personality profiles for realistic gameplay
    - Risk tolerance and investment preferences
    - Negotiation styles and trading behavior
    - Property development strategies
    - Economic analysis depth and decision speed

    Attributes:
        name (str): Unique identifier for the player agent.
        strategic_personality (Literal): AI personality type affecting decisions.
        risk_tolerance (float): Risk preference for investments (0.0-1.0).
        negotiation_aggressiveness (float): Trading aggressiveness (0.0-1.0).
        property_development_focus (bool): Whether to prioritize building development.
        cash_reserve_preference (float): Preferred cash reserve ratio (0.0-1.0).
        trading_willingness (float): Likelihood to engage in trades (0.0-1.0).
        state_schema (type[BaseModel]): State schema for decision-making.
        input_schema (type[BaseModel]): Input schema for processing.
        output_schema (type[BaseModel]): Output schema for responses.
        engines (Dict[str, AugLLMConfig]): LLM engines for different decision types.

    Examples:
        Conservative player configuration::\n

            config = MonopolyPlayerAgentConfig(
                name="conservative_player",
                strategic_personality="conservative",
                risk_tolerance=0.3,
                cash_reserve_preference=0.4,
                trading_willingness=0.2
            )

        Aggressive trader configuration::\n

            config = MonopolyPlayerAgentConfig(
                name="aggressive_trader",
                strategic_personality="aggressive",
                risk_tolerance=0.8,
                negotiation_aggressiveness=0.9,
                trading_willingness=0.9
            )

    """

    # Override base fields with enhanced descriptions
    name: str = Field(
        default="monopoly_player", description="Unique identifier for the player agent"
    )

    strategic_personality: Literal[
        "conservative", "aggressive", "balanced", "opportunistic"
    ] = Field(
        default="balanced",
        description="AI personality type affecting strategic decisions and risk assessment",
    )

    risk_tolerance: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Risk preference for investments and property purchases (0.0=risk-averse, 1.0=risk-seeking)",
    )

    negotiation_aggressiveness: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Trading aggressiveness and negotiation intensity (0.0=passive, 1.0=very aggressive)",
    )

    property_development_focus: bool = Field(
        default=True,
        description="Whether to prioritize building houses and hotels over cash accumulation",
    )

    cash_reserve_preference: float = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        description="Preferred cash reserve ratio relative to total assets (0.0=spend all, 1.0=hoard cash)",
    )

    trading_willingness: float = Field(
        default=0.6,
        ge=0.0,
        le=1.0,
        description="Likelihood to engage in property trades and negotiations (0.0=never trade, 1.0=always trade)",
    )

    state_schema: type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="State schema for player decision-making processes",
    )

    input_schema: type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="Input schema for processing game state information",
    )

    output_schema: type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="Output schema for player decision responses",
    )

    engines: dict[str, AugLLMConfig] = Field(
        default_factory=dict,
        description="LLM engines for different decision types (property, trading, building, jail)",
    )

    @computed_field
    @property
    def player_profile(self) -> dict[str, str | float | bool]:
        """Generate comprehensive player profile summary.

        Returns:
            Dict[str, Union[str, float, bool]]: Player characteristics and preferences.

        """
        return {
            "personality": self.strategic_personality,
            "risk_tolerance": self.risk_tolerance,
            "negotiation_style": self.negotiation_aggressiveness,
            "development_focus": self.property_development_focus,
            "cash_preference": self.cash_reserve_preference,
            "trading_willingness": self.trading_willingness,
            "player_type": self._classify_player_type(),
        }

    def _classify_player_type(self) -> str:
        """Classify player type based on configuration parameters.

        Returns:
            str: Player type classification.

        """
        if self.risk_tolerance < 0.3 and self.cash_reserve_preference > 0.6:
            return "Conservative Saver"
        if self.risk_tolerance > 0.7 and self.trading_willingness > 0.7:
            return "Aggressive Trader"
        if self.property_development_focus and self.risk_tolerance > 0.5:
            return "Property Developer"
        if self.negotiation_aggressiveness > 0.6 and self.trading_willingness > 0.6:
            return "Deal Maker"
        return "Balanced Player"

    model_config = {"arbitrary_types_allowed": True}


class MonopolyGameAgentConfig(AgentConfig):
    r"""Advanced configuration system for Monopoly game agents with comprehensive rule.
    support.

    This class provides complete configuration management for Monopoly gameplay,
    supporting multiple rule variants, economic simulation parameters, and strategic
    AI customization. The configuration system enables flexible game setups from
    casual family games to competitive tournaments and economic research.

    The configuration supports:
    - International rule variants and house rules
    - Advanced economic simulation parameters
    - Multi-player AI configurations with different personalities
    - Trading and negotiation system customization
    - Property development and auction mechanics
    - Performance optimization for different scenarios
    - Comprehensive validation and error handling

    Attributes:
        name (str): Unique identifier for the game agent.
        game_variant (GameVariant): Selected game variant (classic, speed, city, etc.).
        difficulty (GameDifficulty): AI difficulty level affecting strategic depth.
        player_names (List[str]): Names of players participating in the game.
        max_turns (int): Maximum number of turns before forcing game end.
        max_rounds (int): Maximum number of complete rounds before game end.
        starting_money (int): Initial money for each player ($1500 in classic).
        go_salary (int): Money collected for passing GO ($200 in classic).
        enable_trading (bool): Whether to enable property trading between players.
        enable_building (bool): Whether to enable house and hotel construction.
        enable_auctions (bool): Whether to enable property auctions.
        enable_jail_bail (bool): Whether players can pay bail to leave jail.
        free_parking_bonus (bool): Whether Free Parking collects tax money.
        double_go_salary (bool): Whether landing on GO gives double salary.
        income_tax_rate (float): Income tax rate as percentage of net worth.
        luxury_tax_amount (int): Fixed luxury tax amount.
        jail_bail_amount (int): Amount to pay for jail bail.
        house_shortage_rules (bool): Whether to enforce building shortages.
        mortgage_interest_rate (float): Interest rate for mortgage redemption.
        state_schema (type[BaseModel]): State schema for the game.
        player_agent_config (MonopolyPlayerAgentConfig): Configuration for player agents.
        runnable_config (RunnableConfig): Runtime configuration.

    Examples:
        Standard family game configuration::\n

            config = MonopolyGameAgentConfig.family_game()
            assert config.difficulty == GameDifficulty.MEDIUM
            assert config.enable_trading == True
            assert config.starting_money == 1500

        Tournament-level competitive play::\n

            config = MonopolyGameAgentConfig.tournament()
            assert config.difficulty == GameDifficulty.EXPERT
            assert config.enable_auctions == True
            assert config.max_turns == 2000

        Economic simulation for research::\n

            config = MonopolyGameAgentConfig.economic_simulation()
            assert config.house_shortage_rules == True
            assert config.mortgage_interest_rate == 0.1
            assert len(config.player_names) == 6

        Custom house rules variant::\n

            config = MonopolyGameAgentConfig(
                game_variant=GameVariant.CUSTOM,
                starting_money=2000,
                free_parking_bonus=True,
                double_go_salary=True,
                enable_trading=True
            )

        Speed game configuration::\n

            config = MonopolyGameAgentConfig.speed_game()
            assert config.max_turns == 200
            assert config.starting_money == 1000
            assert config.go_salary == 400

    Note:
        All configurations use Pydantic for validation and support both JSON
        serialization and integration with distributed tournament systems.

    """

    # Override base agent config fields
    name: str = Field(
        default="monopoly_game", description="Unique identifier for the game agent"
    )

    game_variant: GameVariant = Field(
        default=GameVariant.CLASSIC,
        description="Selected game variant determining rule set and mechanics",
    )

    difficulty: GameDifficulty = Field(
        default=GameDifficulty.MEDIUM,
        description="AI difficulty level affecting strategic depth and decision complexity",
    )

    state_schema: type[BaseModel] = Field(
        default=MonopolyState,
        description="State schema for the game defining data structure",
    )

    # Player configuration
    player_names: list[str] = Field(
        default=["Alice", "Bob", "Charlie", "Diana"],
        min_length=2,
        max_length=8,
        description="Names of players participating in the game (2-8 players)",
    )

    # Game duration limits
    max_turns: int = Field(
        default=1000,
        ge=50,
        le=5000,
        description="Maximum number of turns before forcing game end (50-5000)",
    )

    max_rounds: int = Field(
        default=100,
        ge=10,
        le=500,
        description="Maximum number of complete rounds before game end (10-500)",
    )

    # Economic parameters
    starting_money: int = Field(
        default=1500,
        ge=500,
        le=10000,
        description="Initial money for each player in dollars (500-10000)",
    )

    go_salary: int = Field(
        default=200,
        ge=100,
        le=1000,
        description="Money collected for passing GO in dollars (100-1000)",
    )

    income_tax_rate: float = Field(
        default=0.1,
        ge=0.0,
        le=0.5,
        description="Income tax rate as percentage of net worth (0.0-0.5)",
    )

    luxury_tax_amount: int = Field(
        default=100,
        ge=50,
        le=500,
        description="Fixed luxury tax amount in dollars (50-500)",
    )

    jail_bail_amount: int = Field(
        default=50,
        ge=10,
        le=200,
        description="Amount to pay for jail bail in dollars (10-200)",
    )

    mortgage_interest_rate: float = Field(
        default=0.1,
        ge=0.0,
        le=0.3,
        description="Interest rate for mortgage redemption (0.0-0.3)",
    )

    # Feature toggles
    enable_trading: bool = Field(
        default=True, description="Whether to enable property trading between players"
    )

    enable_building: bool = Field(
        default=True, description="Whether to enable house and hotel construction"
    )

    enable_auctions: bool = Field(
        default=True, description="Whether to enable property auctions when declined"
    )

    enable_jail_bail: bool = Field(
        default=True,
        description="Whether players can pay bail to leave jail immediately",
    )

    house_shortage_rules: bool = Field(
        default=True,
        description="Whether to enforce building shortage rules (32 houses, 12 hotels)",
    )

    # House rules
    free_parking_bonus: bool = Field(
        default=False, description="Whether Free Parking collects tax money as bonus"
    )

    double_go_salary: bool = Field(
        default=False, description="Whether landing exactly on GO gives double salary"
    )

    snake_eyes_bonus: bool = Field(
        default=False,
        description="Whether rolling snake eyes (double 1s) gives bonus money",
    )

    bankruptcy_elimination: bool = Field(
        default=True,
        description="Whether bankrupt players are eliminated from the game",
    )

    # Visualization and debugging
    should_visualize_graph: bool = Field(
        default=True, description="Whether to visualize the game workflow graph"
    )

    enable_detailed_logging: bool = Field(
        default=False, description="Whether to enable detailed game event logging"
    )

    # Player agent configuration
    player_agent_config: MonopolyPlayerAgentConfig = Field(
        default_factory=lambda: MonopolyPlayerAgentConfig(name="monopoly_player_agent"),
        description="Configuration for player decision agents",
    )

    # Runtime configuration
    runnable_config: RunnableConfig = Field(
        default_factory=lambda: RunnableConfigManager.create(
            thread_id=str(uuid.uuid4()), recursion_limit=500
        ),
        description="Runtime configuration for the game execution",
    )

    @field_validator("player_names")
    @classmethod
    def validate_player_names(cls, v: list[str]) -> list[str]:
        """Validate player names are unique and reasonable.

        Args:
            v (List[str]): List of player names to validate.

        Returns:
            List[str]: Validated list of player names.

        Raises:
            ValueError: If player names are not unique or invalid.

        """
        if len(v) != len(set(v)):
            raise ValueError("All player names must be unique")

        for name in v:
            if not name.strip():
                raise ValueError("Player names cannot be empty")
            if len(name) > 20:
                raise ValueError("Player names must be 20 characters or less")

        return v

    @field_validator("max_turns")
    @classmethod
    def validate_max_turns(cls, v: int, info: ValidationInfo) -> int:
        """Validate max turns is reasonable for the number of players.

        Args:
            v (int): Maximum turns to validate.
            info (ValidationInfo): Validation context containing other field values.

        Returns:
            int: Validated max turns value.

        """
        player_count = len(info.data.get("player_names", []))
        if player_count > 0:
            min_turns = player_count * 10  # Minimum 10 turns per player
            if v < min_turns:
                raise ValueError(
                    f"Max turns ({v}) should be at least {min_turns} for {player_count} players"
                )
        return v

    @computed_field
    @property
    def game_profile(self) -> dict[str, str | int | float | bool]:
        """Generate comprehensive game profile summary.

        Returns:
            Dict[str, Union[str, int, float, bool]]: Game characteristics and settings.

        """
        return {
            "variant": self.game_variant.value,
            "difficulty": self.difficulty.value,
            "player_count": len(self.player_names),
            "starting_money": self.starting_money,
            "go_salary": self.go_salary,
            "trading_enabled": self.enable_trading,
            "building_enabled": self.enable_building,
            "auctions_enabled": self.enable_auctions,
            "house_rules_count": sum(
                [
                    self.free_parking_bonus,
                    self.double_go_salary,
                    self.snake_eyes_bonus,
                    not self.bankruptcy_elimination,
                ]
            ),
            "estimated_duration": self._estimate_game_duration(),
        }

    @computed_field
    @property
    def economic_parameters(self) -> dict[str, int | float]:
        """Calculate economic parameters for the game.

        Returns:
            Dict[str, Union[int, float]]: Economic settings and derived values.

        """
        total_starting_money = self.starting_money * len(self.player_names)

        return {
            "total_starting_money": total_starting_money,
            "money_per_player": self.starting_money,
            "go_salary_ratio": self.go_salary / self.starting_money,
            "income_tax_rate": self.income_tax_rate,
            "luxury_tax_ratio": self.luxury_tax_amount / self.starting_money,
            "jail_bail_ratio": self.jail_bail_amount / self.starting_money,
            "mortgage_interest_rate": self.mortgage_interest_rate,
            "economic_velocity": self._calculate_economic_velocity(),
        }

    def _estimate_game_duration(self) -> str:
        """Estimate game duration based on configuration.

        Returns:
            str: Estimated game duration category.

        """
        base_duration = self.max_turns / len(self.player_names)

        if base_duration < 50:
            return "Short (30-60 minutes)"
        if base_duration < 100:
            return "Medium (60-120 minutes)"
        if base_duration < 200:
            return "Long (2-3 hours)"
        return "Extended (3+ hours)"

    def _calculate_economic_velocity(self) -> float:
        """Calculate economic velocity factor.

        Returns:
            float: Economic velocity multiplier.

        """
        velocity = 1.0

        # Higher GO salary increases velocity
        velocity *= self.go_salary / 200

        # More players increase velocity
        velocity *= len(self.player_names) / 4

        # Trading increases velocity
        if self.enable_trading:
            velocity *= 1.2

        # Building increases velocity
        if self.enable_building:
            velocity *= 1.1

        return round(velocity, 2)

    def create_initial_state(self) -> MonopolyState:
        r"""Create the initial game state with all required fields and proper validation.

        Returns:
            MonopolyState: Fully initialized game state ready for gameplay.

        Raises:
            ValueError: If state creation or validation fails.

        Examples:
            Creating initial state::\n

                config = MonopolyGameAgentConfig.family_game()
                state = config.create_initial_state()
                assert len(state.players) == 4
                assert state.current_player_index == 0
                assert state.turn_number == 1

            Validating state consistency::\n

                state = config.create_initial_state()
                issues = state.validate_state_consistency()
                assert len(issues) == 0  # No validation issues

        """
        # Create board and players
        properties = create_board()
        players = create_players(self.player_names)

        # Apply starting money from configuration
        for player in players:
            player.money = self.starting_money

        # Shuffle cards
        chance_cards, community_chest_cards = shuffle_cards()

        # Validate we have players
        if not players:
            raise ValueError(
                "No players were created - check player_names configuration"
            )

        # Create initial state with ALL required fields
        initial_state = MonopolyState(
            players=players,
            properties=properties,
            current_player_index=0,  # Always start with first player
            turn_number=1,
            round_number=1,
            game_status="waiting",
            chance_cards=chance_cards,
            community_chest_cards=community_chest_cards,
            game_events=[],
            messages=[],  # Include empty messages list for schema compatibility
        )

        # Validate the initial state
        issues = initial_state.validate_state_consistency()
        if issues:
            raise ValueError(f"Initial state validation failed: {issues}")

        return initial_state

    def create_player_agent(self) -> Any:
        r"""Create the player decision agent with configured engines.

        Returns:
            MonopolyPlayerAgent: Configured player agent for decision-making.

        Examples:
            Creating player agent::\n

                config = MonopolyGameAgentConfig.tournament()
                agent = config.create_player_agent()
                # Agent has advanced AI capabilities

        """
        # Import here to avoid circular dependency

        # Set up the engines for the player agent
        if not self.player_agent_config.engines:
            self.player_agent_config.engines = build_monopoly_player_aug_llms()

        # Create and return the player agent
        return MonopolyPlayerAgent(self.player_agent_config)

    def setup_player_agent_engines(self) -> None:
        """Set up the engines for the player agent if not already configured.

        This method ensures that the player agent has the necessary LLM engines
        configured for different types of decisions (property, trading, building, etc.).

        """
        if not self.player_agent_config.engines:
            self.player_agent_config.engines = build_monopoly_player_aug_llms()

    @classmethod
    def family_game(cls) -> "MonopolyGameAgentConfig":
        r"""Create configuration for family-friendly Monopoly game.

        Family game features:
        - Balanced difficulty for all skill levels
        - Standard rules with optional house rules
        - Moderate game duration
        - All major features enabled

        Returns:
            MonopolyGameAgentConfig: Configuration for family gameplay.

        Examples:
            Creating family game::\n

                config = MonopolyGameAgentConfig.family_game()
                agent = MonopolyGameAgent(config)
                result = agent.run_game()

        """
        return cls(
            name="family_monopoly",
            game_variant=GameVariant.CLASSIC,
            difficulty=GameDifficulty.MEDIUM,
            player_names=["Alice", "Bob", "Charlie", "Diana"],
            max_turns=600,
            max_rounds=60,
            starting_money=1500,
            go_salary=200,
            enable_trading=True,
            enable_building=True,
            enable_auctions=True,
            free_parking_bonus=True,
            double_go_salary=False,
        )

    @classmethod
    def tournament(cls) -> "MonopolyGameAgentConfig":
        """Create configuration for tournament-level competitive play.

        Tournament features:
        - Expert AI difficulty
        - Strict official rules
        - Extended game duration
        - All advanced features enabled
        - No house rules

        Returns:
            MonopolyGameAgentConfig: Configuration for competitive tournament play.

        """
        return cls(
            name="tournament_monopoly",
            game_variant=GameVariant.CLASSIC,
            difficulty=GameDifficulty.EXPERT,
            player_names=["Player1", "Player2", "Player3", "Player4"],
            max_turns=2000,
            max_rounds=200,
            starting_money=1500,
            go_salary=200,
            enable_trading=True,
            enable_building=True,
            enable_auctions=True,
            house_shortage_rules=True,
            free_parking_bonus=False,
            double_go_salary=False,
            enable_detailed_logging=True,
        )

    @classmethod
    def speed_game(cls) -> "MonopolyGameAgentConfig":
        """Create configuration for fast-paced Monopoly game.

        Speed game features:
        - Reduced game duration
        - Increased starting money and GO salary
        - Simplified decision-making
        - Limited turns and rounds

        Returns:
            MonopolyGameAgentConfig: Configuration for speed gameplay.

        """
        return cls(
            name="speed_monopoly",
            game_variant=GameVariant.SPEED,
            difficulty=GameDifficulty.MEDIUM,
            player_names=["Speed1", "Speed2", "Speed3"],
            max_turns=300,
            max_rounds=30,
            starting_money=1000,
            go_salary=400,
            enable_trading=True,
            enable_building=False,
            enable_auctions=False,
            free_parking_bonus=True,
            double_go_salary=True,
        )

    @classmethod
    def economic_simulation(cls) -> "MonopolyGameAgentConfig":
        """Create configuration for economic research simulation.

        Economic simulation features:
        - Multiple players for market dynamics
        - Realistic economic parameters
        - All advanced features enabled
        - Detailed logging for analysis
        - Extended duration for pattern analysis

        Returns:
            MonopolyGameAgentConfig: Configuration for economic simulation.

        """
        return cls(
            name="economic_monopoly",
            game_variant=GameVariant.CUSTOM,
            difficulty=GameDifficulty.EXPERT,
            player_names=[
                "Conservative",
                "Aggressive",
                "Balanced",
                "Opportunistic",
                "Developer",
                "Trader",
            ],
            max_turns=3000,
            max_rounds=300,
            starting_money=1500,
            go_salary=200,
            income_tax_rate=0.1,
            luxury_tax_amount=100,
            mortgage_interest_rate=0.1,
            enable_trading=True,
            enable_building=True,
            enable_auctions=True,
            house_shortage_rules=True,
            enable_detailed_logging=True,
        )

    @classmethod
    def casual_game(cls) -> "MonopolyGameAgentConfig":
        """Create configuration for casual, relaxed gameplay.

        Casual game features:
        - Easy AI difficulty
        - Generous house rules
        - Shorter game duration
        - Simplified mechanics

        Returns:
            MonopolyGameAgentConfig: Configuration for casual gameplay.

        """
        return cls(
            name="casual_monopoly",
            game_variant=GameVariant.CLASSIC,
            difficulty=GameDifficulty.EASY,
            player_names=["Alice", "Bob", "Charlie"],
            max_turns=400,
            max_rounds=40,
            starting_money=2000,
            go_salary=300,
            enable_trading=True,
            enable_building=True,
            enable_auctions=False,
            free_parking_bonus=True,
            double_go_salary=True,
            snake_eyes_bonus=True,
            jail_bail_amount=25,
        )

    @classmethod
    def default(cls) -> "MonopolyGameAgentConfig":
        """Create a default configuration for Monopoly.

        Returns:
            MonopolyGameAgentConfig: Default configuration for standard gameplay.

        """
        return cls.family_game()

    model_config = {"arbitrary_types_allowed": True}
