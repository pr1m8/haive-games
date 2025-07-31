# game_framework/core/container.py

from __future__ import annotations

import random
import uuid
from typing import Any, Generic, TypeVar

from game_framework.core.piece import GamePiece
from pydantic import BaseModel, Field

# Type variable for game pieces
T = TypeVar("T", bound=GamePiece)


class GamePieceContainer(BaseModel, Generic[T]):
    """Base container for game pieces.

    This represents a collection of game pieces like a deck of cards, a bag of tiles, or
    a player's hand.

    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    pieces: list[T] = Field(default_factory=list)
    properties: dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    def add(self, piece: T, position: str = "top") -> None:
        """Add a piece to this container.

        Args:
            piece: The piece to add
            position: Where to add the piece ("top", "bottom", or "random")

        """
        if position == "top":
            self.pieces.insert(0, piece)
        elif position == "bottom":
            self.pieces.append(piece)
        elif position == "random":
            idx = random.randint(0, len(self.pieces))
            self.pieces.insert(idx, piece)
        else:
            raise ValueError(f"Unknown position: {position}")

    def remove(self, piece_id: str) -> T | None:
        """Remove a piece by ID.

        Args:
            piece_id: ID of the piece to remove

        Returns:
            The removed piece, or None if not found

        """
        for i, piece in enumerate(self.pieces):
            if piece.id == piece_id:
                return self.pieces.pop(i)
        return None

    def count(self) -> int:
        """Count pieces in the container."""
        return len(self.pieces)

    def is_empty(self) -> bool:
        """Check if container is empty."""
        return len(self.pieces) == 0

    def shuffle(self) -> None:
        """Shuffle the pieces in the container."""
        random.shuffle(self.pieces)
