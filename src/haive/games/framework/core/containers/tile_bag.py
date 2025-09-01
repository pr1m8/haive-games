# game_framework/containers/scrabble_bag.py
from typing import Dict, List, Optional
from pydantic import Field

from haive.games.framework.core.container import GamePieceContainer
from haive.games.framework.core.pieces.scrabble_tile import ScrabbleTile

class ScrabbleTileBag(GamePieceContainer[ScrabbleTile]):
    """
    A bag of Scrabble tiles.
    
    This represents the collection of letter tiles in a Scrabble game.
    """
    # Track distributions of remaining tiles
    letter_counts: Dict[str, int] = Field(default_factory=dict)
    
    def add(self, piece: ScrabbleTile, position: str = "random") -> None:
        """
        Add a tile to the bag.
        
        Args:
            piece: The tile to add
            position: Where to add the tile
        """
        super().add(piece, position)
        
        # Update letter count
        letter = piece.letter
        self.letter_counts[letter] = self.letter_counts.get(letter, 0) + 1
    
    def remove(self, piece_id: str) -> Optional[ScrabbleTile]:
        """
        Remove a tile by ID.
        
        Args:
            piece_id: ID of the tile to remove
            
        Returns:
            The removed tile, or None if not found
        """
        for i, piece in enumerate(self.pieces):
            if piece.id == piece_id:
                tile = self.pieces.pop(i)
                
                # Update letter count
                letter = tile.letter
                if letter in self.letter_counts:
                    self.letter_counts[letter] -= 1
                    if self.letter_counts[letter] <= 0:
                        del self.letter_counts[letter]
                
                return tile
        return None
    
    def draw_random(self) -> Optional[ScrabbleTile]:
        """
        Draw a random tile from the bag.
        
        Returns:
            A random tile, or None if the bag is empty
        """
        if not self.pieces:
            return None
            
        import random
        idx = random.randint(0, len(self.pieces) - 1)
        tile = self.pieces.pop(idx)
        
        # Update letter count
        letter = tile.letter
        if letter in self.letter_counts:
            self.letter_counts[letter] -= 1
            if self.letter_counts[letter] <= 0:
                del self.letter_counts[letter]
        
        return tile
    
    def draw_many_random(self, count: int) -> List[ScrabbleTile]:
        """
        Draw multiple random tiles from the bag.
        
        Args:
            count: Number of tiles to draw
            
        Returns:
            List of randomly drawn tiles
        """
        tiles = []
        for _ in range(min(count, len(self.pieces))):
            tile = self.draw_random()
            if tile:
                tiles.append(tile)
        return tiles
    
    def get_remaining_count(self, letter: str = None) -> int:
        """
        Get the number of remaining tiles.
        
        Args:
            letter: Optional specific letter to count
            
        Returns:
            Number of tiles remaining (total or for specific letter)
        """
        if letter:
            return self.letter_counts.get(letter.upper(), 0)
        return len(self.pieces)
    
    @classmethod
    def create_english_bag(cls) -> 'ScrabbleTileBag':
        """
        Create a standard English Scrabble tile bag.
        
        Returns:
            A new ScrabbleTileBag with standard English Scrabble distribution
        """
        bag = cls(name="Scrabble Tile Bag")
        
        # English Scrabble distribution
        distribution = {
            'A': (9, 1), 'B': (2, 3), 'C': (2, 3), 'D': (4, 2),
            'E': (12, 1), 'F': (2, 4), 'G': (3, 2), 'H': (2, 4),
            'I': (9, 1), 'J': (1, 8), 'K': (1, 5), 'L': (4, 1),
            'M': (2, 3), 'N': (6, 1), 'O': (8, 1), 'P': (2, 3),
            'Q': (1, 10), 'R': (6, 1), 'S': (4, 1), 'T': (6, 1),
            'U': (4, 1), 'V': (2, 4), 'W': (2, 4), 'X': (1, 8),
            'Y': (2, 4), 'Z': (1, 10), ' ': (2, 0)  # Blanks
        }
        
        # Add tiles according to distribution
        for letter, (count, points) in distribution.items():
            for _ in range(count):
                if letter == ' ':
                    # Blank tile
                    bag.add(ScrabbleTile(letter="", points=0, blank=True))
                else:
                    bag.add(ScrabbleTile(letter=letter, points=points))
        
        # Initialize letter counts
        bag.letter_counts = {
            letter: count for letter, (count, _) in distribution.items()
        }
        
        # Shuffle the bag
        bag.shuffle()
        
        return bag