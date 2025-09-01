# game_framework/positions/graph.py
from __future__ import annotations
from typing import Any, Dict, Optional
from pydantic import Field

from haive.games.framework.core.position import Position

class GraphPosition(Position):
    """
    Position on a graph-based board.
    
    This represents a node in a graph, like a territory in Risk.
    """
    node_id: str
    coordinates: Optional[Dict[str, float]] = None  # Optional real-world coordinates
    
    def get_coordinates(self) -> str:
        """Get the node ID as coordinates."""
        return self.node_id
    
    def distance_to(self, other: GraphPosition) -> float:
        """
        Calculate the distance between positions.
        
        Since graph distances depend on the board topology, this just
        checks for equality.
        
        Args:
            other: Another graph position
            
        Returns:
            0 if equal, 1 if different nodes
        """
        if not isinstance(other, GraphPosition):
            return super().distance_to(other)
            
        return 0 if self.node_id == other.node_id else 1
    
    def __eq__(self, other: object) -> bool:
        """Graph positions are equal if they have the same node ID."""
        if not isinstance(other, GraphPosition):
            return False
        return self.node_id == other.node_id
    
    def __hash__(self) -> int:
        """Hash based on node ID."""
        return hash(self.node_id)