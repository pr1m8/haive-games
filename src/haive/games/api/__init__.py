"""Game API integration module.

This module provides utilities for integrating games with the
standardized GameAPI system from haive-dataflow.
"""

from haive.games.api.general_api import (
    GameInfo,
    GameSelectionRequest,
    GeneralGameAPI,
    create_general_game_api,
)
from haive.games.api.setup import (
    GameAPIConfig,
    create_chess_api,
    create_connect4_api,
    create_game_api,
    create_tic_tac_toe_api,
)

__all__ = [
    # Specific game APIs
    "create_game_api",
    "create_chess_api",
    "create_connect4_api",
    "create_tic_tac_toe_api",
    "GameAPIConfig",
    # General API
    "create_general_game_api",
    "GeneralGameAPI",
    "GameInfo",
    "GameSelectionRequest",
]
