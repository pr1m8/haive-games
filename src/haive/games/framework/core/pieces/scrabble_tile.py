# game_framework/pieces/scrabble_tile.py
from typing import Optional
from pydantic import field_validator

from haive.games.framework.core.position import Position
from haive.games.framework.core.pieces.tile import Tile

class ScrabbleTile(Tile):
    """
    A Scrabble letter tile.
    
    This represents a tile in the Scrabble game with a letter and point value.
    """
    letter: str
    points: int
    blank: bool = False
    
    @field_validator('letter')
    @classmethod
    def validate_letter(cls, v: str) -> str:
        """Ensure letter is a single uppercase character or empty for blanks."""
        if cls.blank:
            return v.upper() if v else ""
        
        if not v or len(v) != 1 or not v.isalpha():
            raise ValueError("Letter must be a single alphabetic character")
        
        return v.upper()
    
    def set_blank_letter(self, letter: str) -> None:
        """
        Set the letter for a blank tile.
        
        Args:
            letter: The letter to assign to the blank
            
        Raises:
            ValueError: If this is not a blank tile
        """
        if not self.blank:
            raise ValueError("Can only set letter on blank tiles")
            
        self.letter = letter.upper() if letter else ""
    
    def clear_blank(self) -> None:
        """Clear the letter from a blank tile."""
        if self.blank:
            self.letter = ""
    
    @property
    def value(self) -> int:
        """Get the tile's point value (0 for blanks)."""
        return 0 if self.blank else self.points
    
    def __str__(self) -> str:
        """String representation of the tile."""
        if self.blank and not self.letter:
            return "[ ]"  # Empty blank
        if self.blank:
            return f"[{self.letter.lower()}]"  # Lowercase to indicate blank
        return self.letter