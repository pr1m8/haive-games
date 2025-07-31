"""Configuration for Flow Free game agent.

This module defines the configuration for the Flow Free game agent, including player
type, game mode, and difficulty settings.

"""

from pydantic import Field

from haive.games.single_player.base import (
    GameDifficulty,
    GameMode,
    PlayerType,
    SinglePlayerGameConfig,
)
from haive.games.single_player.flow_free.engines import flow_free_engines
from haive.games.single_player.flow_free.state import FlowFreeState


class FlowFreeConfig(SinglePlayerGameConfig):
    """Configuration for the Flow Free game agent.

    Attributes:
        name: Name of the game agent.
        state_schema: State schema for the game.
        player_type: Type of player.
        game_mode: Mode of operation.
        difficulty: Difficulty level of the game.
        max_hints: Maximum number of hints allowed.
        auto_analyze: Whether to automatically analyze after each move.
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.
        num_flows: Number of flows to include. If None, determined by difficulty.
        engines: Configurations for game LLMs.

    """

    name: str = Field(default="flow_free", description="Name of the game agent")
    state_schema: type[FlowFreeState] = Field(
        default=FlowFreeState, description="State schema for Flow Free"
    )
    player_type: PlayerType = Field(
        default=PlayerType.LLM, description="Type of player"
    )
    game_mode: GameMode = Field(default=GameMode.AUTO, description="Mode of operation")
    difficulty: GameDifficulty = Field(
        default=GameDifficulty.MEDIUM, description="Difficulty level of the game"
    )
    max_hints: int = Field(default=3, description="Maximum number of hints allowed")
    auto_analyze: bool = Field(
        default=True, description="Whether to automatically analyze after each move"
    )
    rows: int = Field(default=5, description="Number of rows in the grid")
    cols: int = Field(default=5, description="Number of columns in the grid")
    num_flows: int | None = Field(
        default=None, description="Number of flows to include"
    )
    engines: dict = Field(
        default_factory=lambda: flow_free_engines,
        description="Configurations for game LLMs",
    )

    @classmethod
    def default_config(cls):
        """Create a default configuration for a new Flow Free game.

        Returns:
            FlowFreeConfig: An instance of the default game configuration.

        """
        return cls(
            name="flow_free",
            state_schema=FlowFreeState,
            player_type=PlayerType.LLM,
            game_mode=GameMode.AUTO,
            difficulty=GameDifficulty.MEDIUM,
            max_hints=3,
            auto_analyze=True,
            rows=5,
            cols=5,
            num_flows=None,
            engines=flow_free_engines,
        )

    @classmethod
    def easy_config(cls):
        """Create an easy configuration for a new Flow Free game.

        Returns:
            FlowFreeConfig: An instance of the easy game configuration.

        """
        return cls(
            name="flow_free_easy",
            state_schema=FlowFreeState,
            player_type=PlayerType.LLM,
            game_mode=GameMode.AUTO,
            difficulty=GameDifficulty.EASY,
            max_hints=5,
            auto_analyze=True,
            rows=5,
            cols=5,
            num_flows=4,
            engines=flow_free_engines,
        )

    @classmethod
    def interactive_config(cls):
        """Create an interactive configuration for a new Flow Free game.

        Returns:
            FlowFreeConfig: An instance of the interactive game configuration.

        """
        return cls(
            name="flow_free_interactive",
            state_schema=FlowFreeState,
            player_type=PlayerType.HUMAN,
            game_mode=GameMode.INTERACTIVE,
            difficulty=GameDifficulty.MEDIUM,
            max_hints=3,
            auto_analyze=False,
            rows=5,
            cols=5,
            num_flows=None,
            engines=flow_free_engines,
        )
