# game_framework/boards/path.py
from typing import List, Optional, Dict, Any, TypeVar
from pydantic import Field

from haive.games.framework.core.board import Board, BoardTopology
from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.path import PathPosition
from haive.games.framework.core.spaces.path import PathSpace, PathSpaceAction

# Type variable for pieces
T = TypeVar('T', bound=GamePiece)

class PathBoard(Board[PathSpace[T], PathPosition, T]):
    """
    A path-based board for games like Monopoly or Snakes & Ladders.
    
    This represents a linear path of spaces with special connections.
    """
    topology: BoardTopology = BoardTopology.PATH
    space_count: int
    is_circular: bool = True  # Whether the path loops (like in Monopoly)
    
    def initialize_path(self, 
                        space_names: Optional[List[str]] = None, 
                        space_props: Optional[List[Dict[str, Any]]] = None) -> None:
        """
        Initialize a standard linear path with the specified number of spaces.
        
        Args:
            space_names: Optional list of names for each space
            space_props: Optional list of properties for each space
        """
        for i in range(self.space_count):
            # Create position
            position = PathPosition(index=i)
            
            # Create space
            name = space_names[i] if space_names and i < len(space_names) else f"Space {i}"
            props = space_props[i] if space_props and i < len(space_props) else {}
            
            # Determine if corner (e.g., for Monopoly)
            is_corner = (i % (self.space_count // 4) == 0) if self.space_count >= 4 else False
            
            space = PathSpace[T](
                position=position,
                name=name,
                properties=props,
                is_corner=is_corner
            )
            
            # Add to board
            space_id = self.add_space(space)
            
            # Connect to previous space
            if i > 0:
                prev_space_id = next(s.id for s in self.spaces.values() 
                                    if s.position.index == i-1)
                space.set_prev(prev_space_id)
                self.spaces[prev_space_id].set_next(space_id)
            
            # If circular, connect last space to first
            if i == self.space_count - 1 and self.is_circular:
                first_space_id = next(s.id for s in self.spaces.values() 
                                     if s.position.index == 0)
                space.set_next(first_space_id)
                self.spaces[first_space_id].set_prev(space_id)
    
    def add_shortcut(self, from_index: int, to_index: int, 
                    action: PathSpaceAction = PathSpaceAction.TELEPORT) -> None:
        """
        Add a shortcut connection between spaces (like snakes and ladders).
        
        Args:
            from_index: Starting space index
            to_index: Destination space index
            action: Action type for the shortcut
        """
        # Find spaces
        from_space = next((s for s in self.spaces.values() 
                          if s.position.index == from_index), None)
        to_space = next((s for s in self.spaces.values() 
                        if s.position.index == to_index), None)
        
        if not from_space or not to_space:
            raise ValueError(f"Spaces at indices {from_index} and {to_index} must exist")
        
        # Add connection and action
        from_space.connections.add(to_space.id)
        from_space.set_action(action, to_index)
    
    def get_space_at_index(self, index: int) -> Optional[PathSpace[T]]:
        """
        Get the space at the specified index.
        
        Args:
            index: Path index to look up
            
        Returns:
            The space at the index, or None if no space exists there
        """
        # Handle circular paths
        if self.is_circular:
            index = index % self.space_count
            
        return self.get_space_at_position(PathPosition(index=index))
    
    def move_piece(self, piece_id: str, steps: int) -> Optional[PathSpace[T]]:
        """
        Move a piece along the path by a number of steps.
        
        Args:
            piece_id: ID of the piece to move
            steps: Number of steps to move (can be negative)
            
        Returns:
            The destination space, or None if the piece was not found
        """
        # Find the piece
        for space in self.spaces.values():
            for piece in space.pieces:
                if piece.id == piece_id:
                    # Found the piece, calculate new position
                    current_index = space.position.index
                    new_index = current_index + steps
                    
                    # Handle circular paths
                    if self.is_circular:
                        new_index = new_index % self.space_count
                    elif new_index < 0 or new_index >= self.space_count:
                        # Out of bounds
                        return None
                    
                    # Get the destination space
                    dest_space = self.get_space_at_index(new_index)
                    if not dest_space:
                        return None
                        
                    # Remove from current space and place on new space
                    removed_piece = space.remove_piece(piece_id)
                    if removed_piece:
                        dest_space.place_piece(removed_piece)
                        return dest_space
                        
        return None  # Piece not found