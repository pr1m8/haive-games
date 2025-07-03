"""Checkers agent configuration module.

This module provides configuration classes for checkers agents, including:
    - Board size and game rules
    - Engine configurations for LLM-powered players
    - Maximum turn limits
    - State schema definition
    - Runnable configuration for the agent

The configuration system uses Pydantic for validation and default values,
making it easy to create and customize checkers agent instances.
"""

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import BaseModel, Field

from haive.games.checkers.engines import build_checkers_aug_llms
from haive.games.checkers.state import CheckersState


class CheckersAgentConfig(AgentConfig):
    """Configuration for checkers game agent.

    This class defines all configuration parameters for a checkers agent,
    including board size, rule variations, LLM engines, and other game settings.

    Attributes:
        board_size (int): Size of the checkers board (typically 8x8)
        max_turns (int): Maximum number of turns before the game is declared a draw
        allow_flying_kings (bool): Whether kings can move any distance along diagonals
        mandatory_jumps (bool): Whether jumps are mandatory when available
        state_schema (type[BaseModel]): State schema for the checkers game
        engines (dict[str, AugLLMConfig]): LLM configurations for players and analyzers
        runnable_config (RunnableConfig): Runtime configuration for the agent

    Examples:
        >>> # Create a default configuration
        >>> config = CheckersAgentConfig()
        >>> config.board_size
        8
        >>> config.mandatory_jumps
        True

        >>> # Create a configuration with custom settings
        >>> config = CheckersAgentConfig(
        ...     board_size=10,
        ...     max_turns=150,
        ...     allow_flying_kings=True
        ... )
    """

    board_size: int = Field(default=8, description="Size of the checkers board")
    max_turns: int = Field(
        default=100, description="Maximum number of turns before declaring a draw"
    )
    allow_flying_kings: bool = Field(
        default=False, description="Whether kings can move any distance along diagonals"
    )
    mandatory_jumps: bool = Field(
        default=True, description="Whether jumps are mandatory when available"
    )
    state_schema: type[BaseModel] = Field(
        default=CheckersState, description="State schema for the checkers game"
    )
    engines: dict[str, AugLLMConfig] = Field(
        default_factory=build_checkers_aug_llms,
        description="Engines for the checkers game",
    )
    runnable_config: RunnableConfig = Field(
        default={"configurable": {"recursion_limit": 2000}},
        # ),
        description="Runnable configuration for the checkers game",
    )

    @classmethod
    def default(cls):
        """Create a default configuration for checkers.

        Creates a configuration with standard checkers rules:
        - 8x8 board
        - 100 max turns
        - Mandatory jumps
        - Standard kings (no flying kings)

        Returns:
            CheckersAgentConfig: Default configuration for checkers

        Examples:
            >>> config = CheckersAgentConfig.default()
            >>> config.board_size
            8
            >>> config.mandatory_jumps
            True
        """
        return cls(
            name="checkers_agent",
            max_turns=100,
            board_size=8,
            mandatory_jumps=True,
            allow_flying_kings=False,
        )

    class Config:
        """Pydantic configuration.

        Allows arbitrary types to be used in the model.
        """

        arbitrary_types_allowed = True
