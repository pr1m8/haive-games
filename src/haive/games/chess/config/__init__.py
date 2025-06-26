"""
Chess game configuration module.

This module provides configuration classes and options for chess games,
including time controls, skill levels, and other gameplay settings.

Classes:
    ChessConfig: Main configuration class for chess games
    TimeControl: Enumeration of standard chess time controls

Example:
    >>> from haive.games.chess.config import ChessConfig, TimeControl
    >>> config = ChessConfig(
    ...     player_names=["Magnus", "Hikaru"],
    ...     time_control=TimeControl.RAPID,
    ...     skill_level=8
    ... )
"""

from haive.games.chess.config.config import ChessConfig, TimeControl

__all__ = ["ChessConfig", "TimeControl"]
