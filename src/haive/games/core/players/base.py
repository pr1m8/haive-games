"""Base core module.

This module provides base functionality for the Haive framework.

Classes:
    PlayerTypes: PlayerTypes implementation.
    Player: Player implementation.
    for: for implementation.
"""

from enum import Enum

from pydantic import BaseModel


class PlayerTypes(str, Enum):
    """Types of players in a game."""

    HUMAN = "human"
    AI = "ai"
    # NETWORK = "network"


class Player(BaseModel):
    """Base class for all players."""

    id: str
    name: str
    player_type: PlayerTypes


class HumanPlayer(Player):
    """A human player."""

    player_type: PlayerTypes = PlayerTypes.HUMAN


class AIPlayer(Player):
    """An AI player."""
