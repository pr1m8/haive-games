"""Grid core module.

This module provides grid functionality for the Haive framework.

Classes:
    GridSpace: GridSpace implementation.

Functions:
    get_row: Get Row functionality.
    get_col: Get Col functionality.
    is_dark_square: Is Dark Square functionality.
"""

# game_framework/spaces/grid.py
from typing import TypeVar

from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.grid import GridPosition
from haive.games.framework.core.space import Space

# Type variable for pieces
T = TypeVar("T", bound=GamePiece)


class GridSpace(Space[GridPosition, T]):
    """A space on a grid-based board.

    This represents a single cell in a grid-based board, like a square
    on a chess board.
    """

    position: GridPosition

    def get_row(self) -> int:
        """Get the row index of this space."""
        return self.position.row

    def get_col(self) -> int:
        """Get the column index of this space."""
        return self.position.col

    def is_dark_square(self) -> bool:
        """Determine if this is a dark square (for checkered boards).

        Returns:
            True if the square should be dark, False if light
        """
        return (self.position.row + self.position.col) % 2 == 1

    def get_chess_notation(self) -> str:
        """Get the space's position in chess notation (e.g., 'a1', 'h8').

        Returns:
            Chess notation for this space
        """
        col_letter = chr(ord("a") + self.position.col)
        return f"{col_letter}{self.position.row + 1}"
