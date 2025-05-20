"""
Position models for the game framework.

This module defines the base Position class and its specific implementations
for different coordinate systems used in games.
"""

from __future__ import annotations

import uuid
from typing import Any, Dict, Optional, Tuple

from pydantic import BaseModel, Field, computed_field, field_validator


class Position(BaseModel):
    """
    Base class for all position types in games.

    A Position represents a location in a game. Different games use different
    coordinate systems, so this base class is extended for specific needs.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    class Config:
        frozen = True  # Positions should be immutable

    def __eq__(self, other: object) -> bool:
        """
        Check if positions are equal.
        Base implementation compares IDs; subclasses should override.
        """
        if not isinstance(other, Position):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        """Hash implementation for dictionary keys and sets."""
        return hash(self.id)

    def serialize(self) -> Dict[str, Any]:
        """Convert the position to a serializable dictionary."""
        return self.model_dump()


class GridPosition(Position):
    """
    Position on a grid-based board with row and column coordinates.

    Used in games like Chess, Checkers, Scrabble, etc. where the board
    is organized as a rectangular grid of cells.
    """

    row: int
    col: int

    @field_validator("row", "col")
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
        col_letter = chr(ord("A") + self.col)
        return f"{col_letter}{self.row + 1}"

    def offset(self, row_offset: int, col_offset: int) -> GridPosition:
        """Create a new position that is offset from this one."""
        return GridPosition(row=self.row + row_offset, col=self.col + col_offset)

    def neighbors(self) -> Dict[str, GridPosition]:
        """
        Get all adjacent grid positions (orthogonal).

        Returns:
            Dictionary mapping direction names to positions.
        """
        return {
            "north": self.offset(-1, 0),
            "east": self.offset(0, 1),
            "south": self.offset(1, 0),
            "west": self.offset(0, -1),
        }

    def neighbors_with_diagonals(self) -> Dict[str, GridPosition]:
        """
        Get all adjacent grid positions including diagonals.

        Returns:
            Dictionary mapping direction names to positions.
        """
        neighbors = self.neighbors()
        neighbors.update(
            {
                "northeast": self.offset(-1, 1),
                "southeast": self.offset(1, 1),
                "southwest": self.offset(1, -1),
                "northwest": self.offset(-1, -1),
            }
        )
        return neighbors

    def manhattan_distance(self, other: GridPosition) -> int:
        """Calculate the Manhattan distance to another grid position."""
        return abs(self.row - other.row) + abs(self.col - other.col)

    def chebyshev_distance(self, other: GridPosition) -> int:
        """
        Calculate the Chebyshev distance to another grid position.

        This is the maximum of the horizontal and vertical distances,
        which corresponds to the number of moves a king in chess would need.
        """
        return max(abs(self.row - other.row), abs(self.col - other.col))


class PointPosition(Position):
    """
    Position using floating point coordinates in a 2D space.

    Used in games with continuous coordinates like territory maps or
    physics-based games.
    """

    x: float
    y: float

    def __eq__(self, other: object) -> bool:
        """Point positions are equal if they have the same x and y."""
        if not isinstance(other, PointPosition):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        """Hash based on x and y coordinates."""
        return hash((self.x, self.y))

    @computed_field
    @property
    def coordinates(self) -> Tuple[float, float]:
        """Get the x and y as a tuple."""
        return (self.x, self.y)

    def distance_to(self, other: PointPosition) -> float:
        """Calculate the Euclidean distance to another point position."""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def offset(self, x_offset: float, y_offset: float) -> PointPosition:
        """Create a new position that is offset from this one."""
        return PointPosition(x=self.x + x_offset, y=self.y + y_offset)


class HexPosition(Position):
    """
    Position on a hexagonal grid using cube coordinates.

    Used in games like Catan, hex-based war games, etc.

    This uses cube coordinates (q, r, s) where q + r + s = 0.
    """

    q: int  # x-axis
    r: int  # y-axis
    s: int  # z-axis (computed as -q-r)

    @field_validator("s")
    @classmethod
    def validate_cube_coords(cls, v: int, values: Dict) -> int:
        """Ensure cube coordinates are valid (q + r + s = 0)."""
        q = values.data.get("q")
        r = values.data.get("r")
        if q is not None and r is not None:
            expected_s = -q - r
            if v != expected_s:
                return expected_s
        return v

    def __eq__(self, other: object) -> bool:
        """Hex positions are equal if they have the same q, r, and s."""
        if not isinstance(other, HexPosition):
            return False
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __hash__(self) -> int:
        """Hash based on q, r, and s coordinates."""
        return hash((self.q, self.r, self.s))

    @classmethod
    def from_axial(cls, q: int, r: int) -> HexPosition:
        """Create a hex position from axial coordinates (q, r)."""
        return cls(q=q, r=r, s=-q - r)

    @computed_field
    @property
    def axial_coords(self) -> Tuple[int, int]:
        """Get the axial coordinates (q, r) as a tuple."""
        return (self.q, self.r)

    def neighbors(self) -> Dict[str, HexPosition]:
        """
        Get all adjacent hex positions.

        Returns:
            Dictionary mapping direction names to positions.
        """
        directions = [
            (1, -1, 0),
            (1, 0, -1),
            (0, 1, -1),
            (-1, 1, 0),
            (-1, 0, 1),
            (0, -1, 1),
        ]

        result = {}
        for i, (dq, dr, ds) in enumerate(directions):
            direction_name = [
                "northeast",
                "east",
                "southeast",
                "southwest",
                "west",
                "northwest",
            ][i]
            result[direction_name] = HexPosition(
                q=self.q + dq, r=self.r + dr, s=self.s + ds
            )

        return result

    def distance(self, other: HexPosition) -> int:
        """Calculate the distance to another hex position."""
        return max(abs(self.q - other.q), abs(self.r - other.r), abs(self.s - other.s))
