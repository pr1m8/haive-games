"""Configuration for the Fox and Geese game agent.

This module defines the configuration for the Fox and Geese game agent,
which includes the game name, state schema, AugLLM configurations,
enable_analysis, visualize, and max_turns.
"""

from typing import Type

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

from haive.games.fox_and_geese.engines import fox_and_geese_engines
from haive.games.fox_and_geese.state import FoxAndGeeseState
from haive.games.framework.base.config import GameConfig


class FoxAndGeeseConfig(GameConfig):
    """Configuration for the Fox and Geese game agent.

    This class defines the configuration for the Fox and Geese game agent,
    which includes the game name, state schema, AugLLM configurations,
    enable_analysis, visualize, and max_turns.
    """

    name: str = Field(default="fox_and_geese", description="Name of the game")
    input_schema: Type[FoxAndGeeseState] = Field(default=FoxAndGeeseState)
    state_schema: Type[FoxAndGeeseState] = Field(default=FoxAndGeeseState)
    engines: dict[str, AugLLMConfig] = Field(
        default=fox_and_geese_engines,
        description="Configs for the Fox and Geese engines",
    )
    enable_analysis: bool = Field(
        default=True, description="Whether to enable position analysis"
    )
    visualize: bool = Field(default=True, description="Whether to visualize the game")
    max_turns: int = Field(
        default=100, description="Maximum number of turns before declaring a draw"
    )

    @classmethod
    def default_config(cls):
        """Create a default configuration."""
        return cls(
            name="fox_and_geese",
            state_schema=FoxAndGeeseState,
            engines=fox_and_geese_engines,
            enable_analysis=True,
            visualize=True,
            max_turns=100,
        )
