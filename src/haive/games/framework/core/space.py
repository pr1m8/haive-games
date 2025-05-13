# game_framework/core/space.py
from __future__ import annotations
from typing import Generic, Optional, TypeVar, Dict, Any, Set
from pydantic import BaseModel, Field
import uuid

from haive.games.framework.core.position import Position
from haive.games.framework.core.piece import GamePiece

# Type variables
P = TypeVar('P', bound=Position)
T = TypeVar('T', bound=GamePiece)

class Space(BaseModel, Generic[P, T]):
    """
    A single space on a game board that can hold a piece.
    
    Spaces are the fundamental units that make up a board. Each space has
    a position and can optionally contain a game piece.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    position: P
    piece: Optional[T] = None
    name: Optional[str] = None
    properties: Dict[str, Any] = Field(default_factory=dict)
    connections: Set[str] = Field(default_factory=set)  # IDs of connected spaces
    
    class Config:
        arbitrary_types_allowed = True
    
    def place_piece(self, piece: T) -> bool:
        """
        Place a piece on this space.
        
        Args:
            piece: The piece to place
            
        Returns:
            True if the piece was placed successfully, False otherwise
        """
        if self.is_occupied():
            return False
        
        self.piece = piece
        piece.place_at(self.position)
        return True
    
    def remove_piece(self) -> Optional[T]:
        """
        Remove the piece from this space.
        
        Returns:
            The removed piece, or None if there was no piece
        """
        piece = self.piece
        self.piece = None
        return piece
    
    def is_occupied(self) -> bool:
        """Check if this space contains a piece."""
        return self.piece is not None