# game_framework/core/move.py
from __future__ import annotations
from typing import Generic, Optional, TypeVar, Dict, Any
from pydantic import BaseModel, Field
from abc import abstractmethod

# Type variable for game state
S = TypeVar('S', bound=BaseModel)

class Move(BaseModel, Generic[S]):
    """
    Base class for game moves.
    
    Moves represent changes to the game state initiated by players.
    """
    player_id: str
    move_type: str
    
    class Config:
        arbitrary_types_allowed = True
    
    @abstractmethod
    def is_valid(self, game_state: S) -> bool:
        """
        Check if this move is valid in the current game state.
        
        Args:
            game_state: The current game state
            
        Returns:
            True if the move is valid, False otherwise
        """
        pass
    
    @abstractmethod
    def apply(self, game_state: S) -> S:
        """
        Apply this move to the game state.
        
        Args:
            game_state: The current game state
            
        Returns:
            Updated game state after applying the move
        """
        pass