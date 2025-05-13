# game_framework/core/piece.py
from __future__ import annotations
from typing import Generic, Optional, TypeVar, Dict, Any
from pydantic import BaseModel, Field
import uuid

from haive.games.framework.core.position import Position

# Type variable for position types
P = TypeVar('P', bound=Position)

class GamePiece(BaseModel, Generic[P]):
    """
    Base class for any game piece that can be placed on a board.
    
    GamePiece serves as the foundation for all movable objects in games,
    such as chess pieces, playing cards, tiles, etc.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    owner_id: Optional[str] = None
    position: Optional[P] = None
    name: Optional[str] = None
    properties: Dict[str, Any] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed = True
    
    def can_move_to(self, position: P, board: Any) -> bool:
        """
        Check if this piece can move to the specified position.
        
        Args:
            position: Target position to check
            board: The game board
            
        Returns:
            True if the piece can be moved to the position, False otherwise
        """
        # Base implementation - subclasses should override
        return True
    
    def assign_to_player(self, player_id: str) -> None:
        """
        Assign this piece to a player.
        
        Args:
            player_id: ID of the player to assign this piece to
        """
        self.owner_id = player_id
    
    def place_at(self, position: P) -> None:
        """
        Place this piece at the specified position.
        
        Args:
            position: Position to place the piece at
        """
        self.position = position
    
    def get_property(self, key: str, default: Any = None) -> Any:
        """Get a property value with default if not found."""
        return self.properties.get(key, default)
    
    def set_property(self, key: str, value: Any) -> None:
        """Set a property value."""
        self.properties[key] = value