"""Fixed Monopoly agent configuration module.

This module provides corrected configuration classes for the monopoly game agent, including:
    - Proper initial state creation with all required fields
    - Clean BaseModel usage
    - Fixed field validation
"""

import uuid
from typing import Any, Dict, List, Optional, Type

from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.agent.config import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field

from haive.games.monopoly.player_agent import PlayerDecisionState
from haive.games.monopoly.state import MonopolyState
from haive.games.monopoly.utils import create_board, create_players, shuffle_cards


class MonopolyPlayerAgentConfig(AgentConfig):
    """Configuration for monopoly player decision agent."""

    # Override base fields
    name: str = Field(default="monopoly_player", description="Agent name")
    state_schema: Type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="State schema (will be set dynamically)",
    )
    input_schema: Type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="Input schema (will be set dynamically)",
    )
    output_schema: Type[BaseModel] = Field(
        default=PlayerDecisionState,
        description="Output schema (will be set dynamically)",
    )
    # Player agent specific engines
    engines: Dict[str, AugLLMConfig] = Field(
        default_factory=dict, description="LLM engines for different decision types"
    )

    class Config:
        arbitrary_types_allowed = True


class MonopolyGameAgentConfig(AgentConfig):
    """Configuration class for monopoly game agents.

    This class defines the configuration parameters for monopoly agents, including:
        - Game settings (players, turn limits)
        - Player decision configurations
        - Board and game state initialization

    Attributes:
        state_schema (type): The state schema for the game
        player_names (List[str]): Names of players in the game
        max_turns (int): Maximum turns before ending game
        enable_trading (bool): Whether to enable trade negotiations
        enable_building (bool): Whether to enable house/hotel building
    """

    # Override base agent config fields
    name: str = Field(default="monopoly_game", description="Agent name")
    state_schema: type = Field(
        default=MonopolyState, description="The state schema for the game"
    )

    # Game settings
    player_names: List[str] = Field(
        default=["Alice", "Bob", "Charlie", "Diana"],
        description="Names of players in the game",
    )

    max_turns: int = Field(
        default=1000, description="Maximum number of turns before forcing game end"
    )

    enable_trading: bool = Field(
        default=False,
        description="Whether to enable trade negotiations between players",
    )

    enable_building: bool = Field(
        default=False, description="Whether to enable house/hotel building"
    )

    enable_auctions: bool = Field(
        default=False, description="Whether to enable property auctions"
    )

    # Visualization settings
    should_visualize_graph: bool = Field(
        default=True, description="Whether to visualize the game workflow graph"
    )

    state_schema: Type[BaseModel] = Field(
        default=MonopolyState, description="The state schema for the game"
    )

    # Player agent configuration - using composition instead of direct reference
    player_agent_config: MonopolyPlayerAgentConfig = Field(
        default_factory=lambda: MonopolyPlayerAgentConfig(name="monopoly_player_agent"),
        description="Configuration for player decision agent",
    )

    # Runtime configuration
    runnable_config: RunnableConfig = Field(
        default_factory=lambda: RunnableConfigManager.create(
            thread_id=str(uuid.uuid4()), recursion_limit=500
        ),
        description="Runtime configuration for the game",
    )

    def create_initial_state(self) -> MonopolyState:
        """Create the initial game state with all required fields and proper validation."""
        # Create board and players
        properties = create_board()
        players = create_players(self.player_names)

        # Shuffle cards
        chance_cards, community_chest_cards = shuffle_cards()

        # Validate we have players
        if not players:
            raise ValueError(
                "No players were created - check player_names configuration"
            )

        print(f"DEBUG: Creating initial state with {len(players)} players")
        print(f"DEBUG: Player names: {[p.name for p in players]}")

        # Create initial state with ALL required fields including messages
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
            messages=[],  # CRITICAL FIX: Include empty messages list for schema compatibility
        )

        # Validate the initial state
        issues = initial_state.validate_state_consistency()
        if issues:
            print(f"WARNING: Initial state has issues: {issues}")
            raise ValueError(f"Initial state validation failed: {issues}")

        print(f"DEBUG: Initial state created successfully")
        print(f"DEBUG: Current player: {initial_state.current_player.name}")

        return initial_state

    def create_player_agent(self):
        """Create the player decision agent."""
        # Import here to avoid circular dependency
        from haive.games.monopoly.engines import build_monopoly_player_aug_llms
        from haive.games.monopoly.player_agent import MonopolyPlayerAgent

        # Set up the engines for the player agent
        if not self.player_agent_config.engines:
            self.player_agent_config.engines = build_monopoly_player_aug_llms()

        # Create and return the player agent
        return MonopolyPlayerAgent(self.player_agent_config)

    def setup_player_agent_engines(self) -> None:
        """Set up the engines for the player agent if not already configured."""
        if not self.player_agent_config.engines:
            from haive.games.monopoly.engines import build_monopoly_player_aug_llms

            self.player_agent_config.engines = build_monopoly_player_aug_llms()

    class Config:
        """Pydantic configuration class."""

        arbitrary_types_allowed = True
