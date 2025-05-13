# game_framework/positions/grid.py
from __future__ import annotations
from typing import Dict, Tuple
from pydantic import field_validator, computed_field

from haive.games.framework.core.position import Position

class GridPosition(Position):
    """
    Position on a grid-based board with row and column coordinates.
    
    Used in games like Chess, Checkers, Scrabble, etc. where the board
    is organized as a rectangular grid of cells.
    """
    row: int
    col: int
    
    @field_validator('row', 'col')
    @classmethod
    def validate_coordinates(cls, v: int) -> int:
        """Ensure coordinates are valid."""
        if v < 0:
            raise ValueError("Coordinates must be non-negative")
        return v
    
    def __eq__(self, other: object) -> bool:
        """Grid positions are equal if they have the same row and column."""
        if not isinstance(other, GridPosition):
            return False
        return self.row == other.row and self.col == other.col
    
    def __hash__(self) -> int:
        """Hash based on row and column."""
        return hash((self.row, self.col))
    
    @computed_field
    @property
    def coordinates(self) -> Tuple[int, int]:
        """Get the row and column as a tuple."""
        return (self.row, self.col)
    
    @computed_field
    @property
    def display_coords(self) -> str:
        """
        Return human-readable coordinates.
        
        For chess-style notation, this returns coordinates like 'A1', 'B2', etc.
        where the column is a letter (A-Z) and the row is a number (1-based).
        """
        col_letter = chr(ord('A') + self.col)
        return f"{col_letter}{self.row + 1}"