"""Chess agent configuration module.

This module provides configuration classes for the chess game agent, including:
    - Base configuration
    - LLM configuration for players and analyzers
    - Game settings and visualization options
"""

import uuid

from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from langchain_core.runnables import RunnableConfig
from pydantic import Field

from haive.games.chess.engines import build_chess_aug_llms
from haive.games.chess.state import ChessState


class ChessAgentConfig(AgentConfig):
    """Configuration class for chess game agents.

    This class defines the configuration parameters for chess agents, including:
        - Game settings (max moves, analysis options)
        - LLM configurations for players and analyzers
        - Visualization settings

    Attributes:
        state_schema (BaseModel): The state schema for the game
        enable_analysis (bool): Whether to enable position analysis
        should_visualize_graph (bool): Whether to visualize the workflow graph
        max_moves (int): Maximum number of moves before forcing a draw
        engines (Dict[str, AugLLMConfig]): LLM configurations for players and analyzers
    """

    # State schema
    state_schema: type = Field(
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
    engines: dict[str, AugLLMConfig] = Field(
        default_factory=build_chess_aug_llms,
        description="LLM configurations for players and analyzers",
    )
    runnable_config: RunnableConfig = Field(
        default_factory=lambda: RunnableConfigManager.create(
            thread_id=str(uuid.uuid4()), recursion_limit=200
        )
    )

    # runnable_config: Dict['configurable]
    class Config:
        """Pydantic configuration class."""

        arbitrary_types_allowed = True
