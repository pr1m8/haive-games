# game_framework/core/board.py
from __future__ import annotations

import uuid
from abc import abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.position import Position
from haive.games.framework.core.space import Space

# Type variables
S = TypeVar("S", bound=Space)
P = TypeVar("P", bound=Position)
T = TypeVar("T", bound=GamePiece)


class Board(BaseModel, Generic[S, P, T]):
    """Base class for all game boards.

    A Board represents the playing surface in a game, containing spaces
    where pieces can be placed. It manages the spatial relationships between
    spaces.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    spaces: dict[str, S] = Field(default_factory=dict)  # space_id -> Space
    properties: dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    def add_space(self, space: S) -> str:
        """Add a space to the board.

        Args:
            space: The space to add

        Returns:
            ID of the added space
        """
        self.spaces[space.id] = space
        return space.id

    def connect_spaces(self, space1_id: str, space2_id: str) -> None:
        """Connect two spaces bidirectionally.

        Args:
            space1_id: ID of the first space
            space2_id: ID of the second space

        Raises:
            ValueError: If either space doesn't exist on the board
        """
        if space1_id not in self.spaces or space2_id not in self.spaces:
            raise ValueError("Both spaces must exist on the board")

        self.spaces[space1_id].connections.add(space2_id)
        self.spaces[space2_id].connections.add(space1_id)

    @abstractmethod
    def get_space_at_position(self, position: P) -> S | None:
        """Get the space at the specified position.

        This is an abstract method that must be implemented by subclasses
        to provide position-based lookup.

        Args:
            position: The position to look up

        Returns:
            The space at the position, or None if no space exists there
        """

    def place_piece(self, piece: T, position: P) -> bool:
        """Place a piece at the specified position.

        Args:
            piece: The piece to place
            position: Position to place the piece at

        Returns:
            True if placement was successful, False otherwise
        """
        space = self.get_space_at_position(position)
        if not space:
            return False

        return space.place_piece(piece)
