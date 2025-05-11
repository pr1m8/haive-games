"""Go game configuration module."""

from haive.core.engine.agent.agent import AgentConfig
from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field

from .aug_llms import aug_llm_configs
from .models import GoGameState


class GoAgentConfig(AgentConfig):
    """Configuration for the Go game agent.

    This class defines the configuration settings for a Go game agent,
    including state management, LLM configurations, visualization options,
    and analysis settings.

    Attributes:
        state_schema (type): Schema class for game state (default: GoGameState).
        aug_llm_configs (Dict[str, AugLLMConfig]): LLM configurations for
            players and analysis.
        should_visualize_graph (bool): Whether to generate a visualization
            of the game graph (default: True).
        graph_name (str): Filename for the graph visualization
            (default: "go_game.png").
        include_analysis (bool): Whether to include position analysis
            during the game (default: True).

    Example:
        >>> config = GoAgentConfig(
        ...     include_analysis=True,
        ...     aug_llm_configs={
        ...         "black_player": AugLLMConfig(...),
        ...         "white_player": AugLLMConfig(...),
        ...         "analyzer": AugLLMConfig(...)
        ...     }
        ... )
    """

    state_schema: type = Field(
        default=GoGameState, description="Schema class for the Go game state."
    )

    aug_llm_configs: dict[str, AugLLMConfig] = Field(
        default=aug_llm_configs,
        description="LLM configurations for players and analysis.",
    )

    should_visualize_graph: bool = Field(
        default=True,
        description="Whether to generate a visualization of the game graph.",
    )

    graph_name: str = Field(
        default="go_game.png",
        description="Filename for the graph visualization output.",
    )

    include_analysis: bool = Field(
        default=True,
        description="Whether to include position analysis during the game.",
    )
