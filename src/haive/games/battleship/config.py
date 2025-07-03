"""Battleship agent configuration module.

This module provides configuration classes for the Battleship game agent, including:
    - Base configuration
    - Game settings
    - Visualization options
"""

import uuid

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import Field, model_validator

from haive.games.battleship.engines import build_battleship_engines
from haive.games.battleship.state import BattleshipState


class BattleshipAgentConfig(AgentConfig):
    """Configuration class for Battleship game agents.

    This class defines the configuration parameters for Battleship agents, including:
        - Game settings
        - Analysis options
        - Visualization settings
        - Engine configurations

    Attributes:
        state_schema (type): The state schema for the game
        player1_name (str): Name of player 1
        player2_name (str): Name of player 2
        enable_analysis (bool): Whether to enable strategic analysis
        visualize_board (bool): Whether to visualize the game boards
        engines (Dict[str, AugLLMConfig]): Engine configurations
    """

    name: str = Field(default="battleship_agent", description="Name of the agent")

    state_schema: type = Field(
        default=BattleshipState, description="State schema for the game"
    )

    player1_name: str = Field(default="Player 1", description="Name of player 1")

    player2_name: str = Field(default="Player 2", description="Name of player 2")

    enable_analysis: bool = Field(
        default=True, description="Whether to enable strategic analysis"
    )

    visualize_board: bool = Field(
        default=True, description="Whether to visualize the game boards"
    )

    runnable_config: RunnableConfig = Field(
        default={
            "configurable": {
                "recursion_limit": 10000,
                "thread_id": None,  # Will be set to UUID in model_validator
            }
        },
        description="Runnable configuration with recursion limit and thread_id",
    )

    engines: dict[str, AugLLMConfig] = Field(
        default_factory=build_battleship_engines,
        description="Engine configurations for players and analyzers",
    )

    @model_validator(mode="after")
    def update_player_names_from_engines(self):
        """Update player names based on LLM provider and model from engines."""
        # Set thread_id if not already set
        if (
            not self.runnable_config.get("configurable", {}).get("thread_id")
            or self.runnable_config["configurable"]["thread_id"] is None
        ):
            self.runnable_config["configurable"]["thread_id"] = str(uuid.uuid4())

        if self.engines:
            # Generate names based on LLM provider and model
            player1_engine = self.engines.get("player1_move")
            player2_engine = self.engines.get("player2_move")

            if player1_engine and hasattr(player1_engine, "llm_config"):
                llm_config = player1_engine.llm_config
                provider = getattr(llm_config, "provider", "unknown")
                model = getattr(llm_config, "model", "unknown")
                self.player1_name = f"{provider.value if hasattr(provider, 'value') else provider}-{model}"

            if player2_engine and hasattr(player2_engine, "llm_config"):
                llm_config = player2_engine.llm_config
                provider = getattr(llm_config, "provider", "unknown")
                model = getattr(llm_config, "model", "unknown")
                self.player2_name = f"{provider.value if hasattr(provider, 'value') else provider}-{model}"

        return self

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True
