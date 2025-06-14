"""Chess agent configuration module."""

import uuid
from typing import Any, Dict, Type

from haive.core.config.runnable import RunnableConfigManager
from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

from haive.games.chess.engines import build_chess_aug_llms
from haive.games.chess.state import ChessState


class ChessAgentConfig(AgentConfig):
    """Configuration class for chess game agents."""

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
        """Pydantic configuration."""

        arbitrary_types_allowed = True
