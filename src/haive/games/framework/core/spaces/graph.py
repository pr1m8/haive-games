# game_framework/spaces/graph.py
from typing import Generic, TypeVar, Optional, Dict, Any, List
from pydantic import Field

from haive.games.framework.core.space import Space, SpaceType
from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.graph import GraphPosition

# Type variable for pieces
T = TypeVar('T', bound=GamePiece)

class GraphSpace(Space[GraphPosition, T]):
    """
    A space on a graph-based board.
    
    This represents a node in a graph-based game like Risk or Ticket to Ride.
    """
    position: GraphPosition
    max_pieces: Optional[int] = None  # Maximum number of pieces allowed
    groups: List[str] = Field(default_factory=list)  # Groups this space belongs to (e.g., continents)
    
    def add_connection(self, space_id: str) -> None:
        """Add a connection to another space."""
        self.connections.add(space_id)
    
    def add_group(self, group: str) -> None:
        """
        Add this space to a group.
        
        Args:
            group: Group name (e.g., continent in Risk)
        """
        if group not in self.groups:
            self.groups.append(group)
    
    def is_in_group(self, group: str) -> bool:
        """
        Check if this space belongs to a specific group.
        
        Args:
            group: Group name to check
            
        Returns:
            True if the space is in the group, False otherwise
        """
        return group in self.groups
    
    def place_piece(self, piece: T) -> bool:
        """
        Place a piece on this space.
        
        Args:
            piece: The piece to place
            
        Returns:
            True if the piece was placed successfully, False otherwise
        """
        # Check max pieces limit
        if self.max_pieces is not None and len(self.pieces) >= self.max_pieces:
            return False
            
        return super().place_piece(piece)