"""Comprehensive configuration system for strategic Tic Tac Toe gameplay.

This module provides sophisticated configuration management for Tic Tac Toe agents,
supporting various gameplay modes, AI difficulty levels, and analysis features.
The configuration system enables flexible game setups from educational tutorials
to competitive AI matches with perfect play algorithms.

The configuration system supports:
- Multiple AI engine configurations for different skill levels
- Strategic analysis toggle for educational gameplay
- Visualization options for interactive experiences
- Player assignment and turn order customization
- Integration with LLM-based decision engines
- Tournament-ready configuration presets

Examples:
    Basic game configuration::

        config = TicTacToeConfig(
            name="educational_game",
            enable_analysis=True,
            visualize=True
        )

    Tournament configuration::

        config = TicTacToeConfig(
            name="tournament_match",
            enable_analysis=False,
            visualize=False,
            first_player="X"
        )

    Custom player setup::

        config = TicTacToeConfig(
            player_X="player2",
            player_O="player1",
            first_player="O"
        )

    Using default configuration::

        config = TicTacToeConfig.default_config()
        # Ready for standard gameplay

Note:
    All configurations use Pydantic for validation and support both JSON
    serialization and integration with the game agent framework.
"""

from typing import Any, Literal

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field, computed_field, field_validator

from haive.games.framework.base.config import GameConfig
from haive.games.tic_tac_toe.engines import tictactoe_engines
from haive.games.tic_tac_toe.state import TicTacToeState


class TicTacToeConfig(GameConfig):
    """Advanced configuration system for Tic Tac Toe game agents.

    This class provides comprehensive configuration management for Tic Tac Toe
    gameplay, supporting multiple AI personalities, strategic analysis features,
    and flexible game setups. The configuration enables various gameplay modes
    from casual games to perfect-play AI competitions.

    The configuration supports:
    - AI engine selection for different skill levels
    - Strategic analysis for educational purposes
    - Board visualization for interactive gameplay
    - Flexible player assignment and turn order
    - Integration with LLM-based decision systems
    - Tournament and casual play modes

    Attributes:
        name (str): Unique identifier for the game configuration.
            Used for logging and game session management.
        state_schema (Type[TicTacToeState]): State management class.
            Defines the game state structure and validation rules.
        engines (Dict[str, AugLLMConfig]): AI engine configurations.
            Maps engine roles to their LLM configurations.
        enable_analysis (bool): Toggle for strategic analysis features.
            When True, provides detailed move explanations.
        visualize (bool): Toggle for board visualization.
            When True, displays board state after each move.
        first_player (Literal['X', 'O']): Starting player symbol.
            Determines which player makes the first move.
        player_X (Literal['player1', 'player2']): Player using X.
            Maps X symbol to player identifier.
        player_O (Literal['player1', 'player2']): Player using O.
            Maps O symbol to player identifier.

    Examples:
        Educational game with analysis::

            config = TicTacToeConfig(
                name="learning_game",
                enable_analysis=True,
                visualize=True,
                first_player="X"
            )
            # Provides move explanations and board visualization

        Competitive AI match::

            config = TicTacToeConfig(
                name="ai_competition",
                enable_analysis=False,
                visualize=False,
                engines=advanced_engines
            )
            # Fast gameplay without analysis overhead

        Custom player assignment::

            config = TicTacToeConfig(
                player_X="player2",
                player_O="player1",
                first_player="O"
            )
            # Player 2 uses X, Player 1 uses O and goes first

        Tournament configuration::

            config = TicTacToeConfig(
                name="tournament_round_1",
                enable_analysis=False,
                visualize=True,
                engines=tournament_engines
            )
            # Optimized for competitive play with spectator view

    Note:
        The configuration integrates with the game agent framework and
        supports runtime modification through the agent's lifecycle.
    """

    name: str = Field(
        default="tictactoe",
        min_length=1,
        max_length=50,
        description="Unique identifier for the game configuration",
        examples=["tictactoe", "educational_game", "tournament_match", "ai_battle"],
    )

    state_schema: type[TicTacToeState] = Field(
        default=TicTacToeState,
        description="State management class defining game structure and rules",
        exclude=True,  # Exclude from serialization
    )

    engines: dict[str, AugLLMConfig] = Field(
        default_factory=lambda: tictactoe_engines,
        description="AI engine configurations for move generation and analysis",
        exclude=True,  # Exclude from serialization since it contains model classes
    )

    enable_analysis: bool = Field(
        default=True,
        description="Enable strategic position analysis after each move for educational insights",
        examples=[True, False],
    )

    visualize: bool = Field(
        default=True,
        description="Display board state and moves in human-readable format during gameplay",
        examples=[True, False],
    )

    first_player: Literal["X", "O"] = Field(
        default="X",
        description="Symbol of the player who makes the first move (X traditionally goes first)",
        examples=["X", "O"],
    )

    player_X: Literal["player1", "player2"] = Field(
        default="player1",
        description="Player identifier assigned to use the X symbol",
        examples=["player1", "player2"],
    )

    player_O: Literal["player1", "player2"] = Field(
        default="player2",
        description="Player identifier assigned to use the O symbol",
        examples=["player1", "player2"],
    )

    @field_validator("first_player")
    @classmethod
    def validate_first_player(cls, v: str) -> str:
        """Validate first player is either X or O.

        Args:
            v (str): First player symbol to validate.

        Returns:
            str: Validated first player symbol.

        Raises:
            ValueError: If first player is not X or O.
        """
        if v not in ["X", "O"]:
            raise ValueError(f"first_player must be 'X' or 'O', got '{v}'")
        return v

    @computed_field
    @property
    def game_mode(self) -> str:
        """Determine the game mode based on configuration.

        Returns:
            str: Game mode classification.
        """
        if self.enable_analysis and self.visualize:
            return "educational"
        elif not self.enable_analysis and not self.visualize:
            return "competitive"
        elif self.visualize and not self.enable_analysis:
            return "spectator"
        else:
            return "analysis"

    @computed_field
    @property
    def performance_profile(self) -> dict[str, Any]:
        """Generate performance profile based on settings.

        Returns:
            Dict[str, Any]: Performance characteristics.
        """
        return {
            "analysis_overhead": self.enable_analysis,
            "visualization_cost": self.visualize,
            "optimal_for_ai": not self.enable_analysis and not self.visualize,
            "optimal_for_learning": self.enable_analysis and self.visualize,
        }

    @classmethod
    def default_config(cls) -> "TicTacToeConfig":
        """Create a default configuration for standard Tic Tac Toe gameplay.

        The default configuration is optimized for educational gameplay with
        both analysis and visualization enabled, suitable for learning and
        casual play.

        Returns:
            TicTacToeConfig: Default game configuration instance.

        Examples:
            Creating default game::

                config = TicTacToeConfig.default_config()
                assert config.enable_analysis == True
                assert config.visualize == True
                assert config.first_player == "X"

            Using with agent::

                config = TicTacToeConfig.default_config()
                agent = TicTacToeAgent(config)
                agent.run_game()
        """
        return cls(
            name="tictactoe",
            state_schema=TicTacToeState,
            engines=tictactoe_engines,
            enable_analysis=True,
            visualize=True,
            first_player="X",
            player_X="player1",
            player_O="player2",
        )

    @classmethod
    def educational_config(cls) -> "TicTacToeConfig":
        """Create configuration optimized for learning.

        Features:
        - Full analysis of every position
        - Board visualization after each move
        - Detailed move explanations
        - Perfect for teaching optimal strategy

        Returns:
            TicTacToeConfig: Educational configuration.
        """
        return cls(name="educational_tictactoe", enable_analysis=True, visualize=True)

    @classmethod
    def competitive_config(cls) -> "TicTacToeConfig":
        """Create configuration for competitive AI play.

        Features:
        - No analysis overhead
        - No visualization delays
        - Optimized for speed
        - Perfect for AI tournaments

        Returns:
            TicTacToeConfig: Competitive configuration.
        """
        return cls(name="competitive_tictactoe", enable_analysis=False, visualize=False)

    @classmethod
    def spectator_config(cls) -> "TicTacToeConfig":
        """Create configuration for watching games.

        Features:
        - Board visualization enabled
        - Analysis disabled for speed
        - Good balance for spectating
        - Suitable for demonstrations

        Returns:
            TicTacToeConfig: Spectator configuration.
        """
        return cls(name="spectator_tictactoe", enable_analysis=False, visualize=True)

    model_config = {"arbitrary_types_allowed": True}
