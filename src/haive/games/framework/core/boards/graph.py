# haive/games/framework/core/boards/graph.py
from typing import List, Optional, Dict, Any, TypeVar, Set, Callable
from pydantic import Field

from haive.games.framework.core.board import Board, BoardTopology
from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.graph import GraphPosition
from haive.games.framework.core.spaces.graph import GraphSpace

# Type variable for pieces
T = TypeVar('T', bound=GamePiece)

class GraphBoard(Board[GraphSpace[T], GraphPosition, T]):
    """
    A graph-based board for games like Risk or Ticket to Ride.
    
    This represents a collection of spaces with arbitrary connections.
    """
    topology: BoardTopology = BoardTopology.GRAPH
    groups: Dict[str, Set[str]] = Field(default_factory=dict)  # group -> space_ids
    
    def add_space(self, space: GraphSpace[T]) -> str:
        """
        Add a space to the board.
        
        Args:
            space: The space to add
            
        Returns:
            ID of the added space
        """
        space_id = super().add_space(space)
        
        # Update groups
        for group in space.groups:
            if group not in self.groups:
                self.groups[group] = set()
            self.groups[group].add(space_id)
            
        return space_id
    
    def connect_spaces(self, space1_id: str, space2_id: str, bidirectional: bool = True) -> None:
        """
        Connect two spaces.
        
        Args:
            space1_id: ID of the first space
            space2_id: ID of the second space
            bidirectional: Whether to connect in both directions
        """
        super().connect_spaces(space1_id, space2_id, bidirectional)
    
    def get_spaces_in_group(self, group: str) -> List[GraphSpace[T]]:
        """
        Get all spaces in a specific group.
        
        Args:
            group: Group name (e.g., continent in Risk)
            
        Returns:
            List of spaces in the group
        """
        if group not in self.groups:
            return []
            
        return [self.spaces[space_id] for space_id in self.groups[group]
                if space_id in self.spaces]
    
    def add_group(self, group: str, space_ids: List[str]) -> None:
        """
        Define a new group of spaces.
        
        Args:
            group: Group name
            space_ids: IDs of spaces in the group
        """
        # Create group if it doesn't exist
        if group not in self.groups:
            self.groups[group] = set()
            
        # Add spaces to group
        for space_id in space_ids:
            if space_id in self.spaces:
                self.groups[group].add(space_id)
                
                # Update space's groups
                space = self.spaces[space_id]
                if group not in space.groups:
                    space.groups.append(group)
    
    def are_connected(self, space1_id: str, space2_id: str) -> bool:
        """
        Check if two spaces are directly connected.
        
        Args:
            space1_id: ID of the first space
            space2_id: ID of the second space
            
        Returns:
            True if the spaces are connected, False otherwise
        """
        if space1_id not in self.spaces or space2_id not in self.spaces:
            return False
            
        return space2_id in self.spaces[space1_id].connections
    
    def find_path(self, start_id: str, end_id: str, 
                 filter_fn: Optional[Callable[[GraphSpace[T]], bool]] = None) -> Optional[List[str]]:
        """
        Find a path between two spaces.
        
        Args:
            start_id: ID of the starting space
            end_id: ID of the destination space
            filter_fn: Optional function to filter valid spaces
            
        Returns:
            List of space IDs forming a path, or None if no path exists
        """
        return super().find_path(start_id, end_id, filter_fn)