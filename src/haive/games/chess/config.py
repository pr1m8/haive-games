"""Chess agent configuration module.

This module provides configuration classes for chess agents, including:
    - Core game parameters
    - LLM engine settings
    - Analysis options
    - Visualization settings
    - State schema definition

The configuration system uses Pydantic for validation and default values,
making it easy to create and customize chess agent instances.
"""

import uuid
from typing import Any, Dict, Type

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

from haive.games.chess.engines import build_chess_aug_llms
from haive.games.chess.state import ChessState


class ChessAgentConfig(AgentConfig):
    """Configuration class for chess game agents.

    This class defines all configuration parameters for a chess agent,
    including state schema, LLM engines, game settings, and visualization
    options.

    Attributes:
        state_schema (Type[ChessState]): The state schema for the game.
        enable_analysis (bool): Whether to enable position analysis during gameplay.
        should_visualize_graph (bool): Whether to visualize the game workflow graph.
        max_moves (int): Maximum number of moves before forcing a draw.
        engines (Dict[str, AugLLMConfig]): LLM configurations for players and analyzers.
        runnable_config (Dict[str, Any]): Runtime configuration for the agent.

    Examples:
        >>> # Create a basic configuration
        >>> config = ChessAgentConfig()
        >>>
        >>> # Create a configuration with analysis disabled
        >>> config = ChessAgentConfig(enable_analysis=False)
        >>>
        >>> # Create a configuration with custom LLM engines
        >>> from haive.core.engine.aug_llm import build_aug_llm
        >>> engines = {
        ...     "white_player": build_aug_llm("openai", "gpt-4"),
        ...     "black_player": build_aug_llm("anthropic", "claude-3-opus-20240229"),
        ... }
        >>> config = ChessAgentConfig(engines=engines)
    """

    # State schema
    state_schema: Type[ChessState] = Field(
        default=ChessState, description="The state schema for the game"
    )

    # Analysis settings
    enable_analysis: bool = Field(
        default=True, description="Whether to enable position analysis during gameplay"
    )

    # Visualization settings
    should_visualize_graph: bool = Field(
        default=True, description="Whether to visualize the game workflow graph"
    )

    # Game settings
    max_moves: int = Field(
        default=200, description="Maximum number of moves before forcing a draw"
    )

    # LLM engines
    engines: Dict[str, AugLLMConfig] = Field(
        default_factory=build_chess_aug_llms,
        description="LLM configurations for players and analyzers",
    )

    # Runnable config with proper defaults
    runnable_config: Dict[str, Any] = Field(
        default_factory=lambda: {
            "configurable": {
                "thread_id": str(uuid.uuid4()),
                "recursion_limit": 200,
                "engine_configs": {},
            }
        },
        description="Runtime configuration for the agent",
    )

    class Config:
        """Pydantic configuration.

        This inner class configures Pydantic behavior for the ChessAgentConfig.

        Attributes:
            arbitrary_types_allowed (bool): Whether to allow arbitrary types in the model.
        """

        arbitrary_types_allowed = True
