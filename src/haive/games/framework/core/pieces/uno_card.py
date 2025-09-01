# game_framework/pieces/uno_card.py
from __future__ import annotations
from typing import Optional, ClassVar, Dict, TypeVar
from enum import Enum
from pydantic import computed_field

from haive.games.framework.core.position import Position
from haive.games.framework.core.piece import GamePiece

# Type variable for position types
P = TypeVar('P', bound=Position)

class UnoColor(str, Enum):
    """UNO card colors."""
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    WILD = "wild"  # For wild cards

class UnoValue(str, Enum):
    """UNO card values."""
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    SKIP = "skip"
    REVERSE = "reverse"
    DRAW_TWO = "draw_two"
    WILD = "wild"
    WILD_DRAW_FOUR = "wild_draw_four"

class UnoCard(GamePiece[P]):
    """
    An UNO card.
    
    This represents a single card in the UNO game with a color and value.
    """
    color: UnoColor
    value: UnoValue
    face_up: bool = False
    
    # Point values for scoring
    _point_values: ClassVar[Dict[UnoValue, int]] = {
        UnoValue.ZERO: 0,
        UnoValue.ONE: 1,
        UnoValue.TWO: 2,
        UnoValue.THREE: 3,
        UnoValue.FOUR: 4,
        UnoValue.FIVE: 5,
        UnoValue.SIX: 6,
        UnoValue.SEVEN: 7,
        UnoValue.EIGHT: 8,
        UnoValue.NINE: 9,
        UnoValue.SKIP: 20,
        UnoValue.REVERSE: 20,
        UnoValue.DRAW_TWO: 20,
        UnoValue.WILD: 50,
        UnoValue.WILD_DRAW_FOUR: 50
    }
    
    @computed_field
    @property
    def points(self) -> int:
        """Get the card's point value."""
        return self._point_values.get(self.value, 0)
    
    def flip(self) -> None:
        """Flip the card face up/down."""
        self.face_up = not self.face_up
    
    def matches(self, other: UnoCard) -> bool:
        """
        Check if this card can be played on top of another card.
        
        Args:
            other: The card to match against
            
        Returns:
            True if this card can be played on the other card, False otherwise
        """
        # Wild cards can always be played
        if self.color == UnoColor.WILD:
            return True
            
        # Match by color
        if self.color == other.color:
            return True
            
        # Match by value
        if self.value == other.value:
            return True
            
        return False
    
    def __str__(self) -> str:
        """String representation of the card."""
        if self.color == UnoColor.WILD:
            return f"WILD {self.value.upper()}"
        return f"{self.color.upper()} {self.value.upper()}"