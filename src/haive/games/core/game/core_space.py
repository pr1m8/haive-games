from __future__ import annotations

"""Space models for the game framework.

This module defines the base Space class and specific implementations
for different types of board spaces.
"""


import uuid
from typing import Any, Generic, Protocol, TypeVar

from game.core.piece import GamePiece
from game.core.position import Position
from pydantic import BaseModel, Field

# Type variables for generics
P = TypeVar("P", bound=Position)
T = TypeVar("T", bound=GamePiece)


class SpaceProtocol(Protocol, Generic[P, T]):
    """Protocol defining the required interface for board spaces."""

    id: str
    position: P

    def is_occupied(self) -> bool: ...
    def place_piece(self, piece: T) -> bool: ...
    def remove_piece(self) -> T | None: ...


class Space(BaseModel, Generic[P, T]):
    """A space on a game board where pieces can be placed.

    A Space represents a location on a board that can hold a game piece.
    It has a position and can be connected to other spaces.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    position: P
    piece: T | None = None
    name: str | None = None
    properties: dict[str, Any] = Field(default_factory=dict)
    connections: set[str] = Field(default_factory=set)  # IDs of connected spaces

    class Config:
        arbitrary_types_allowed = True

    def is_occupied(self) -> bool:
        """Check if this space is occupied by a piece.

        Returns:
            True if the space has a piece, False otherwise
        """
        return self.piece is not None

    def place_piece(self, piece: T) -> bool:
        """Place a piece on this space.

        Args:
            piece: The piece to place

        Returns:
            True if placement was successful, False otherwise
        """
        if self.is_occupied():
            return False

        self.piece = piece
        if piece and hasattr(piece, "place_at"):
            piece.place_at(self.position)

        return True

    def remove_piece(self) -> T | None:
        """Remove and return the piece on this space.

        Returns:
            The removed piece, or None if no piece was on the space
        """
        piece = self.piece
        self.piece = None
        return piece

    def add_connection(self, space_id: str) -> None:
        """Add a connection to another space.

        Args:
            space_id: ID of the space to connect to
        """
        self.connections.add(space_id)

    def remove_connection(self, space_id: str) -> None:
        """Remove a connection to another space.

        Args:
            space_id: ID of the space to disconnect from
        """
        if space_id in self.connections:
            self.connections.remove(space_id)

    def is_connected_to(self, space_id: str) -> bool:
        """Check if this space is connected to another space.

        Args:
            space_id: ID of the space to check

        Returns:
            True if connected, False otherwise
        """
        return space_id in self.connections

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a property value.

        Args:
            key: Property name
            default: Default value if property doesn't exist

        Returns:
            Property value or default
        """
        return self.properties.get(key, default)

    def set_property(self, key: str, value: Any) -> None:
        """Set a property value.

        Args:
            key: Property name
            value: Property value
        """
        self.properties[key] = value


class GridSpace(Space[P, T]):
    """A space on a grid-based board.

    Used for games like Chess, Checkers, Scrabble, etc.
    """

    def get_grid_position(self) -> tuple[int, int]:
        """Get the grid coordinates of this space.

        Returns:
            Tuple of (row, col)
        """
        if hasattr(self.position, "row") and hasattr(self.position, "col"):
            return (self.position.row, self.position.col)
        return (-1, -1)  # Invalid position

    @computed_field
    @property
    def coordinates(self) -> str:
        """Get human-readable coordinates for this space.

        Returns:
            String like "A1", "B2", etc.
        """
        if hasattr(self.position, "display_coords"):
            return self.position.display_coords
        return str(self.position)


class HexSpace(Space[P, T]):
    """A space on a hexagonal board.

    Used for games like Catan, hex-based war games, etc.
    """

    @computed_field
    @property
    def coordinates(self) -> tuple[int, int, int]:
        """Get the hex coordinates of this space.

        Returns:
            Tuple of (q, r, s) in cube coordinates
        """
        if (
            hasattr(self.position, "q")
            and hasattr(self.position, "r")
            and hasattr(self.position, "s")
        ):
            return (self.position.q, self.position.r, self.position.s)
        return (0, 0, 0)  # Invalid position
