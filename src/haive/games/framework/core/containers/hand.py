# game_framework/containers/hand.py
from typing import List, Optional, TypeVar, Generic, Dict, Any
from pydantic import Field

from haive.games.framework.core.container import GamePieceContainer
from haive.games.framework.core.piece import GamePiece

# Type variable for game pieces
T = TypeVar('T', bound=GamePiece)

class Hand(GamePieceContainer[T], Generic[T]):
    """
    A generic player's hand of game pieces.
    
    This represents a collection of pieces held by a player,
    such as cards in a card game or tiles in a tile game.
    """
    player_id: str
    max_size: Optional[int] = None
    
    def add(self, piece: T, position: str = "bottom") -> None:
        """
        Add a piece to the hand and assign ownership.
        
        Args:
            piece: The piece to add
            position: Where to add the piece
            
        Raises:
            ValueError: If the hand is already at maximum size
        """
        if self.max_size is not None and len(self.pieces) >= self.max_size:
            raise ValueError(f"Hand is at maximum size ({self.max_size})")
            
        # Assign ownership
        piece.assign_to_player(self.player_id)
        
        # Add to hand
        super().add(piece, position)
    
    def play(self, piece_id: str) -> Optional[T]:
        """
        Play a piece from the hand (remove it).
        
        Args:
            piece_id: ID of the piece to play
            
        Returns:
            The played piece, or None if not found
        """
        return self.remove(piece_id)
    
    def play_all(self, piece_ids: List[str]) -> List[T]:
        """
        Play multiple pieces from the hand.
        
        Args:
            piece_ids: List of piece IDs to play
            
        Returns:
            List of played pieces
        """
        played = []
        for piece_id in piece_ids:
            piece = self.play(piece_id)
            if piece:
                played.append(piece)
        return played
    
    def sort(self, key_function=None) -> None:
        """
        Sort the pieces in the hand.
        
        Args:
            key_function: Optional sorting key function
        """
        self.pieces.sort(key=key_function)
    
    def has_piece(self, piece_id: str) -> bool:
        """
        Check if the hand contains a specific piece.
        
        Args:
            piece_id: ID of the piece to check
            
        Returns:
            True if the piece is in the hand, False otherwise
        """
        return any(piece.id == piece_id for piece in self.pieces)