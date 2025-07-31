"""Base configuration module for game agents.

This module provides the foundational configuration class for game agents,
defining common settings and parameters that all game agents need.

Example:
    >>> config = GameConfig(
    ...     state_schema=ChessState,
    ...     engines={"player1": player1_engine},
    ...     enable_analysis=True
    ... )

Typical usage:
    - Inherit from GameConfig to create game-specific configurations
    - Override default values to customize game behavior
    - Use as configuration for game agents

"""

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import Field

from haive.games.framework.base.state import GameState


class GameConfig(AgentConfig):
    """Base configuration for game agents.

    This class defines the core configuration parameters that all game agents
    need, including state schema, LLM engines, and analysis settings.

    Attributes:
        state_schema (Type[GameState]): The state schema class for the game.
        engines (Dict[str, AugLLMConfig]): Configurations for game LLMs.
        enable_analysis (bool): Whether to enable move analysis.
        visualize (bool): Whether to visualize the game.

    Example:
        >>> class ChessConfig(GameConfig):
        ...     state_schema: Type[GameState] = ChessState
        ...     engines: Dict[str, AugLLMConfig] = {
        ...         "player1": player1_engine,
        ...         "player2": player2_engine
        ...     }
        ...     enable_analysis: bool = True

    """

    state_schema: type[GameState] = Field(
        default=GameState, description="State schema for the game"
    )

    engines: dict[str, AugLLMConfig] = Field(
        default_factory=dict, description="Configurations for game LLMs"
    )

    enable_analysis: bool = Field(
        default=False, description="Whether to enable move analysis"
    )

    visualize: bool = Field(default=True, description="Whether to visualize the game")
    runnable_config: RunnableConfig = Field(
        default={"configurable": {"recursion_limit": 10000}}
    )

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True
