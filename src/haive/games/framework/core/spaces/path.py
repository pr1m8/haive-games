# game_framework/spaces/path.py
from typing import Generic, TypeVar, Optional, Dict, Any
from pydantic import Field
from enum import Enum
from haive.games.framework.core.space import Space, SpaceType
from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.path import PathPosition

# Type variable for pieces
T = TypeVar('T', bound=GamePiece)

class PathSpaceAction(str, Enum):
    """Special actions for path spaces."""
    NONE = "none"
    MOVE = "move"       # Move a specified number of spaces
    TELEPORT = "teleport"  # Teleport to a specific space
    COLLECT = "collect"    # Collect money/resources
    PAY = "pay"           # Pay money/resources
    DRAW = "draw"         # Draw a card

class PathSpace(Space[PathPosition, T]):
    """
    A space on a path-based board.
    
    This represents a single space in games like Monopoly or Snakes & Ladders.
    """
    position: PathPosition
    action: PathSpaceAction = PathSpaceAction.NONE
    action_value: Optional[Any] = None
    next_space_id: Optional[str] = None
    prev_space_id: Optional[str] = None
    is_corner: bool = False
    
    def set_next(self, space_id: str) -> None:
        """Set the next space in the path."""
        self.next_space_id = space_id
        self.connections.add(space_id)
    
    def set_prev(self, space_id: str) -> None:
        """Set the previous space in the path."""
        self.prev_space_id = space_id
        self.connections.add(space_id)
    
    def set_action(self, action: PathSpaceAction, value: Any = None) -> None:
        """
        Set a special action for this space.
        
        Args:
            action: The action type
            value: Associated value (e.g., amount to pay, spaces to move)
        """
        self.action = action
        self.action_value = value