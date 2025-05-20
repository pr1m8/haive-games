from __future__ import annotations

import uuid
from typing import List, Optional

from pydantic import BaseModel, Field, computed_field, field_validator

# ======================================================
# POSITION TYPES - How locations are represented in games
# ======================================================


class Position(BaseModel):
    """Base class for all position types in games."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    class Config:
        frozen = True  # Make position immutable


class GridPosition(Position):
    """Position on a grid-based board (Chess, Checkers, Scrabble)."""

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
        if not isinstance(other, GridPosition):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    @computed_field
    @property
    def display_coords(self) -> str:
        """Return human-readable coordinates (e.g. 'A1' for chess)."""
        col_letter = chr(ord("A") + self.col)
        return f"{col_letter}{self.row + 1}"


class HexPosition(Position):
    """Position on a hexagonal grid (e.g., Settlers of Catan)."""

    q: int  # Axial coordinates - q is column-like
    r: int  # Axial coordinates - r is row-like

    @field_validator("q", "r")
    @classmethod
    def validate_hex_coords(cls, v: int) -> int:
        """Hex coordinates can be negative."""
        return v

    @computed_field
    @property
    def s(self) -> int:
        """Compute third coordinate for cube representation."""
        return -self.q - self.r

    def neighbors(self) -> List["HexPosition"]:
        """Get all adjacent hex positions."""
        # Six directions in hexagonal grid
        directions = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
        return [HexPosition(q=self.q + dq, r=self.r + dr) for dq, dr in directions]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HexPosition):
            return False
        return self.q == other.q and self.r == other.r

    def __hash__(self) -> int:
        return hash((self.q, self.r))


class PointPosition(Position):
    """Position using floating point coordinates (e.g., Go, graph-based games)."""

    x: float
    y: float
    z: Optional[float] = None  # For 3D games

    def distance_to(self, other: "PointPosition") -> float:
        """Calculate Euclidean distance to another point."""
        if self.z is None and other.z is None:
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        elif self.z is not None and other.z is not None:
            return (
                (self.x - other.x) ** 2
                + (self.y - other.y) ** 2
                + (self.z - other.z) ** 2
            ) ** 0.5
        else:
            raise ValueError("Cannot calculate distance between 2D and 3D points")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PointPosition):
            return False
        if self.z is None and other.z is None:
            return self.x == other.x and self.y == other.y
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


class NodePosition(Position):
    """Position in a graph-based board (e.g., Ticket to Ride)."""

    node_id: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NodePosition):
            return False
        return self.node_id == other.node_id

    def __hash__(self) -> int:
        return hash(self.node_id)
