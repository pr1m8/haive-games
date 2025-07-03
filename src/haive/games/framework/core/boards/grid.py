# game_framework/boards/grid.py
from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

from pydantic import field_validator

from haive.games.framework.core.board import Board
from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.grid import GridPosition
from haive.games.framework.core.spaces.grid import GridSpace

# Type variable for game pieces
T = TypeVar("T", bound=GamePiece)


class GridBoard(Board[GridSpace[T], GridPosition, T]):
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

    def get_space_at_position(self, position: GridPosition) -> GridSpace[T] | None:
        """Get the space at the specified grid coordinates.

        Args:
            position: Grid position to look up

        Returns:
            The space at the position, or None if no space exists there
        """
        for space in self.spaces.values():
            if (
                space.position.row == position.row
                and space.position.col == position.col
            ):
                return space
        return None

    def get_space_at(self, row: int, col: int) -> GridSpace[T] | None:
        """Get the space at the specified grid coordinates.

        Args:
            row: Row index
            col: Column index

        Returns:
            The space at the position, or None if no space exists there
        """
        return self.get_space_at_position(GridPosition(row=row, col=col))

    def initialize_grid(
        self, space_factory: Callable[[int, int], GridSpace[T]] | None = None
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
                    space = GridSpace[T](position=position)

                self.add_space(space)

                # Connect to adjacent spaces
                for dr, dc in [(0, 1), (1, 0)]:  # right and down
                    adj_row, adj_col = row + dr, col + dc
                    if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                        # Find adjacent space
                        adj_space = self.get_space_at(adj_row, adj_col)
                        if adj_space:
                            self.connect_spaces(space.id, adj_space.id)
