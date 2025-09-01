# game_framework/positions/path.py
from __future__ import annotations
from typing import Any, Optional
from pydantic import Field

from haive.games.framework.core.position import Position

class PathPosition(Position):
    """
    Position on a path-based board.
    
    This represents a position along a linear path, like in Monopoly
    or Snakes & Ladders.
    """
    index: int
    
    def get_coordinates(self) -> int:
        """Get the path index as coordinates."""
        return self.index
    
    def distance_to(self, other: PathPosition) -> int:
        """
        Calculate the distance along the path.
        
        Args:
            other: Another path position
            
        Returns:
            Number of steps between positions
        """
        if not isinstance(other, PathPosition):
            return super().distance_to(other)
            
        return abs(self.index - other.index)
    
    def __eq__(self, other: object) -> bool:
        """Path positions are equal if they have the same index."""
        if not isinstance(other, PathPosition):
            return False
        return self.index == other.index
    
    def __hash__(self) -> int:
        """Hash based on index."""
        return hash(self.index)