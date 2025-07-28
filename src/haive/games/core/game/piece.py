"""Piece core module.

This module provides piece functionality for the Haive framework.

Classes:
    GamePiece: GamePiece implementation.
    for: for implementation.
    GamePieceProtocol: GamePieceProtocol implementation.

Functions:
    can_move_to: Can Move To functionality.
    assign_to_player: Assign To Player functionality.
    place_at: Place At functionality.
"""

import uuid
from abc import abstractmethod
from typing import Generic, Protocol

from pydantic import BaseModel, Field

# ======================================================
# GAME PIECES - Movable objects used in games
# ======================================================


class GamePiece(BaseModel, Generic[P]):
    """Base class for any game piece that can be placed on a board."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    owner_id: str | None = None
    position: P | None = None

    @abstractmethod
    def can_move_to(self, position: P, board: "Board") -> bool:
        """Check if this piece can move to the specified position."""

    def assign_to_player(self, player_id: str) -> None:
        """Assign this piece to a player."""
        self.owner_id = player_id

    def place_at(self, position: P) -> None:
        """Place this piece at the specified position."""
        self.position = position


class GamePieceProtocol(Protocol):
    """Protocol defining the required interface for game pieces."""

    id: str
    owner_id: str | None
    position: Position | None

    def can_move_to(self, position: Position, board: "Board") -> bool: ...
    def assign_to_player(self, player_id: str) -> None: ...
    def place_at(self, position: Position) -> None: ...
