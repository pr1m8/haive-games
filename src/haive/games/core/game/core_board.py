from __future__ import annotations

"""Board models for the game framework.

This module defines the base Board class and specific implementations
for different types of game boards.
"""


import uuid
from abc import abstractmethod
from collections.abc import Callable
from typing import Any, Generic, TypeVar

from game.core.piece import GamePiece
from game.core.position import GridPosition, Position
from game.core.space import GridSpace, Space
from pydantic import BaseModel, Field, computed_field

# Type variables for generics
S = TypeVar("S", bound=Space)
P = TypeVar("P", bound=Position)
T = TypeVar("T", bound=GamePiece)


class Board(BaseModel, Generic[S, P, T]):
    """Base class for all game boards.

    A Board represents the playing surface in a game, containing spaces
    where pieces can be placed. It manages the spatial relationships
    between spaces.
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

    def get_connected_spaces(self, space_id: str) -> list[S]:
        """Get all spaces connected to the given space.

        Args:
            space_id: ID of the space to get connections for

        Returns:
            List of connected spaces

        Raises:
            ValueError: If the space doesn't exist on the board
        """
        if space_id not in self.spaces:
            raise ValueError(f"Space {space_id} not found")

        space = self.spaces[space_id]
        return [
            self.spaces[conn_id]
            for conn_id in space.connections
            if conn_id in self.spaces
        ]

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

        if hasattr(piece, "can_move_to") and callable(piece.can_move_to):
            if not piece.can_move_to(position, self):
                return False

        return space.place_piece(piece)

    def remove_piece(self, position: P) -> T | None:
        """Remove a piece from the specified position.

        Args:
            position: Position to remove the piece from

        Returns:
            The removed piece, or None if no piece was at the position
        """
        space = self.get_space_at_position(position)
        if not space:
            return None

        return space.remove_piece()

    def is_position_valid(self, position: P) -> bool:
        """Check if a position is valid on this board.

        Args:
            position: Position to check

        Returns:
            True if the position is valid, False otherwise
        """
        return self.get_space_at_position(position) is not None

    def get_all_pieces(self) -> dict[str, T]:
        """Get all pieces currently on the board.

        Returns:
            Dictionary mapping piece IDs to pieces
        """
        pieces: dict[str, T] = {}
        for space in self.spaces.values():
            if space.piece is not None and hasattr(space.piece, "id"):
                pieces[space.piece.id] = space.piece
        return pieces

    def get_player_pieces(self, player_id: str) -> list[T]:
        """Get all pieces belonging to a specific player.

        Args:
            player_id: ID of the player

        Returns:
            List of pieces owned by the player
        """
        return [
            space.piece
            for space in self.spaces.values()
            if space.piece is not None
            and hasattr(space.piece, "owner_id")
            and space.piece.owner_id == player_id
        ]

    def set_property(self, key: str, value: Any) -> None:
        """Set a board property.

        Args:
            key: Property name
            value: Property value
        """
        self.properties[key] = value

    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a board property.

        Args:
            key: Property name
            default: Default value if property doesn't exist

        Returns:
            Property value or default
        """
        return self.properties.get(key, default)


class GridBoard(Board[GridSpace[P, T], P, T]):
    """A grid-based board (Chess, Checkers, Scrabble).

    This represents a rectangular grid of spaces.
    """

    rows: int
    cols: int

    @field_validator("rows", "cols")
    @classmethod
    def validate_dimensions(cls, v: int) -> int:
        """Ensure board dimensions are positive."""
        if v <= 0:
            raise ValueError("Board dimensions must be positive")
        return v

    def get_space_at_position(self, position: P) -> GridSpace[P, T] | None:
        """Get the space at the specified grid coordinates.

        Args:
            position: Grid position to look up

        Returns:
            The space at the position, or None if no space exists there
        """
        # Simple linear search - could be optimized with a position-based index
        for space in self.spaces.values():
            if (
                hasattr(space.position, "row")
                and hasattr(space.position, "col")
                and hasattr(position, "row")
                and hasattr(position, "col")
                and space.position.row == position.row
                and space.position.col == position.col
            ):
                return space
        return None

    def get_space_at(self, row: int, col: int) -> GridSpace[P, T] | None:
        """Get the space at the specified grid coordinates.

        Args:
            row: Row index
            col: Column index

        Returns:
            The space at the position, or None if no space exists there
        """
        # Create a temporary position object for lookup
        # This assumes P is compatible with GridPosition
        position = GridPosition(row=row, col=col)
        return self.get_space_at_position(position)

    def initialize_grid(
        self, space_factory: Callable[[int, int], GridSpace[P, T]] | None = None
    ) -> None:
        """Initialize a standard grid with the specified dimensions.

        Args:
            space_factory: Optional factory function to create spaces
        """
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)

                # Create space using factory if provided, otherwise default
                if space_factory:
                    space = space_factory(row, col)
                else:
                    # Create a basic GridSpace
                    # This assumes P is compatible with GridPosition
                    space = GridSpace[P, T](position=position)

                self.add_space(space)

                # Connect to adjacent spaces
                for dr, dc in [(0, 1), (1, 0)]:  # right and down
                    adj_row, adj_col = row + dr, col + dc
                    if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                        # Find adjacent space
                        adj_space = self.get_space_at(adj_row, adj_col)
                        if adj_space:
                            self.connect_spaces(space.id, adj_space.id)

    def is_position_valid(self, position: P) -> bool:
        """Check if a position is within the grid bounds.

        Args:
            position: Position to check

        Returns:
            True if the position is valid, False otherwise
        """
        return (
            hasattr(position, "row")
            and hasattr(position, "col")
            and 0 <= position.row < self.rows
            and 0 <= position.col < self.cols
        )

    @computed_field
    @property
    def size(self) -> int:
        """Get the total number of spaces on the board.

        Returns:
            Total number of spaces
        """
        return self.rows * self.cols

    def get_row(self, row: int) -> list[GridSpace[P, T]]:
        """Get all spaces in a row.

        Args:
            row: Row index

        Returns:
            List of spaces in the row, ordered by column
        """
        if not 0 <= row < self.rows:
            return []

        row_spaces = []
        for col in range(self.cols):
            space = self.get_space_at(row, col)
            if space:
                row_spaces.append(space)
        return row_spaces

    def get_column(self, col: int) -> list[GridSpace[P, T]]:
        """Get all spaces in a column.

        Args:
            col: Column index

        Returns:
            List of spaces in the column, ordered by row
        """
        if not 0 <= col < self.cols:
            return []

        col_spaces = []
        for row in range(self.rows):
            space = self.get_space_at(row, col)
            if space:
                col_spaces.append(space)
        return col_spaces
