# game_framework/spaces/hex.py
from typing import Generic, TypeVar, Optional, Tuple

from haive.games.framework.core.space import Space
from haive.games.framework.core.piece import GamePiece
from haive.games.framework.core.positions.hex import HexPosition

# Type variable for pieces
T = TypeVar('T', bound=GamePiece)

class HexSpace(Space[HexPosition, T]):
    """
    A space on a hex-based board.
    
    This represents a single hex cell in games like Catan, hex-based
    war games, etc.
    """
    position: HexPosition
    
    def get_coordinates(self) -> Tuple[int, int, int]:
        """Get the q, r, s coordinates of this space."""
        return self.position.coordinates
    
    def get_q(self) -> int:
        """Get the q coordinate (roughly corresponds to x)."""
        return self.position.q
    
    def get_r(self) -> int:
        """Get the r coordinate (roughly corresponds to y)."""
        return self.position.r
    
    def get_s(self) -> int:
        """Get the s coordinate (roughly corresponds to z)."""
        return self.position.s