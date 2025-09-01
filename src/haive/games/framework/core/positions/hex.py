# game_framework/positions/hex.py
from __future__ import annotations
from typing import Tuple, List
from pydantic import field_validator, computed_field

from haive.games.framework.core.position import Position

class HexPosition(Position):
    """
    Position on a hex-based board using cube coordinates.
    
    Uses the cube coordinate system (q, r, s) where q + r + s = 0
    This creates a hexagonal grid with well-defined neighborhoods.
    """
    q: int  # x-axis
    r: int  # y-axis
    s: int  # z-axis (computed as -q-r)
    
    @field_validator('q', 'r')
    @classmethod
    def validate_coordinates(cls, v: int) -> int:
        return v
    
    @field_validator('s')
    @classmethod
    def validate_s(cls, v: int, values) -> int:
        """Ensure s = -q-r to maintain cube coordinates."""
        q = values.data.get('q')
        r = values.data.get('r')
        
        if q is not None and r is not None:
            computed_s = -q - r
            return computed_s
        return v
    
    def __init__(self, **data):
        """Initialize with auto-computed s if not provided."""
        if 'q' in data and 'r' in data and 's' not in data:
            data['s'] = -data['q'] - data['r']
        super().__init__(**data)
    
    def __eq__(self, other: object) -> bool:
        """Hex positions are equal if they have the same q, r, s coordinates."""
        if not isinstance(other, HexPosition):
            return False
        return self.q == other.q and self.r == other.r and self.s == other.s
    
    def __hash__(self) -> int:
        """Hash based on q, r, s coordinates."""
        return hash((self.q, self.r, self.s))
    
    @computed_field
    @property
    def coordinates(self) -> Tuple[int, int, int]:
        """Get the q, r, s coordinates as a tuple."""
        return (self.q, self.r, self.s)
    
    def distance(self, other: HexPosition) -> int:
        """
        Calculate the distance between two hex positions.
        
        Args:
            other: Another hex position
            
        Returns:
            The number of steps from this position to the other
        """
        return max(
            abs(self.q - other.q),
            abs(self.r - other.r),
            abs(self.s - other.s)
        )
    
    def neighbors(self) -> List[HexPosition]:
        """
        Get all adjacent hex positions.
        
        Returns:
            List of the six neighboring positions
        """
        directions = [
            (1, -1, 0), (1, 0, -1), (0, 1, -1),
            (-1, 1, 0), (-1, 0, 1), (0, -1, 1)
        ]
        return [
            HexPosition(q=self.q+dq, r=self.r+dr, s=self.s+ds)
            for dq, dr, ds in directions
        ]