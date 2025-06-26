"""
Chess game configuration.

This module provides configuration classes for chess games, including
settings for time controls, skill levels, and display options. These
configurations are used to customize game behavior and agent decision-making.

Example:
    >>> from haive.games.chess.config import ChessConfig
    >>> config = ChessConfig(
    ...     player_names=["Magnus", "Hikaru"],
    ...     time_control="rapid",
    ...     skill_level=8
    ... )
    >>> agent = ChessAgent(config)
"""

from enum import Enum
from typing import List, Optional

from haive.core.engine.aug_llm import AugLLMConfig
from pydantic import Field, field_validator

from haive.games.framework import GameConfig


class TimeControl(str, Enum):
    """Chess time control options.

    Standard time controls used in chess games, affecting how much time
    players have to make their moves.
    """

    BULLET = "bullet"  # 1-2 minutes per player
    BLITZ = "blitz"  # 3-5 minutes per player
    RAPID = "rapid"  # 10-30 minutes per player
    CLASSICAL = "classical"  # 60+ minutes per player
    CORRESPONDENCE = "correspondence"  # Days per move


class ChessConfig(GameConfig):
    """Configuration for chess games.

    This class defines the configuration parameters for chess games,
    including player names, time controls, and various gameplay options.

    Attributes:
        player_names: Names for the players (white and black).
        time_control: Time control setting for the game.
        time_per_player: Time in seconds per player (overrides time_control if set).
        increment: Time increment in seconds after each move.
        skill_level: Skill level for AI players (1-10 scale).
        use_opening_book: Whether to use opening theory.
        use_endgame_tablebase: Whether to use endgame tablebases.
        visualization_style: Style for board visualization.
        enable_analysis: Whether to enable position analysis.
        llm_config: Configuration for the LLM used for decision making.

    Examples:
        >>> # Standard configuration
        >>> config = ChessConfig(
        ...     player_names=["Player 1", "Player 2"],
        ...     time_control=TimeControl.RAPID
        ... )
        >>>
        >>> # Advanced configuration
        >>> config = ChessConfig(
        ...     player_names=["Human", "AI"],
        ...     time_per_player=600,  # 10 minutes
        ...     increment=5,  # 5 second increment
        ...     skill_level=8,
        ...     use_opening_book=True,
        ...     llm_config=AugLLMConfig(
        ...         system_message="You are a chess master. Play strategically.",
        ...         temperature=0.2
        ...     )
        ... )
    """

    player_names: List[str] = Field(
        default=["White", "Black"], description="Names for the white and black players"
    )

    time_control: TimeControl = Field(
        default=TimeControl.RAPID, description="Time control setting for the game"
    )

    time_per_player: Optional[int] = Field(
        default=None,
        description="Time in seconds per player (overrides time_control if set)",
    )

    increment: int = Field(
        default=0, description="Time increment in seconds after each move", ge=0
    )

    skill_level: int = Field(
        default=5, description="Skill level for AI players (1-10 scale)", ge=1, le=10
    )

    use_opening_book: bool = Field(
        default=True, description="Whether to use opening theory"
    )

    use_endgame_tablebase: bool = Field(
        default=False, description="Whether to use endgame tablebases"
    )

    visualization_style: str = Field(
        default="unicode", description="Style for board visualization"
    )

    enable_analysis: bool = Field(
        default=True, description="Whether to enable position analysis"
    )

    llm_config: Optional[AugLLMConfig] = Field(
        default=None, description="Configuration for the LLM used for decision making"
    )

    @field_validator("player_names")
    def validate_player_names(cls, v: List[str]) -> List[str]:
        """Validate player names.

        Ensures there are exactly two players for a chess game.

        Args:
            v: List of player names.

        Returns:
            The validated list of player names.

        Raises:
            ValueError: If there aren't exactly two player names.
        """
        if len(v) != 2:
            raise ValueError("Chess requires exactly 2 players")
        return v

    def get_time_seconds(self) -> int:
        """Get the time per player in seconds.

        Returns:
            The time per player in seconds, based on time_per_player or time_control.
        """
        if self.time_per_player is not None:
            return self.time_per_player

        # Default times for each time control
        time_control_seconds = {
            TimeControl.BULLET: 120,  # 2 minutes
            TimeControl.BLITZ: 300,  # 5 minutes
            TimeControl.RAPID: 900,  # 15 minutes
            TimeControl.CLASSICAL: 3600,  # 1 hour
            TimeControl.CORRESPONDENCE: 86400,  # 1 day
        }

        return time_control_seconds[self.time_control]

    def create_default_llm_config(self) -> AugLLMConfig:
        """Create a default LLM configuration if none is provided.

        Returns:
            A default LLM configuration for chess decision making.
        """
        return AugLLMConfig(
            system_message="You are playing chess. Analyze the position carefully and make the best move.",
            temperature=0.3
            - (0.02 * self.skill_level),  # Lower temperature for higher skill
        )

    def get_llm_config(self) -> AugLLMConfig:
        """Get the LLM configuration to use.

        Returns:
            The LLM configuration, either user-provided or a default.
        """
        return self.llm_config or self.create_default_llm_config()
