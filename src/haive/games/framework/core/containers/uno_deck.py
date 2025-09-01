# haive/games/framework/core/containers/uno_deck.py
from typing import List, Optional, TypeVar
from pydantic import Field

from haive.games.framework.core.container import GamePieceContainer
from haive.games.framework.core.pieces.uno_card import UnoCard, UnoColor, UnoValue

# Type variable for cards
C = TypeVar('C', bound=UnoCard)

class UnoDeck(GamePieceContainer[C]):
    """
    A deck of UNO cards.
    
    This represents the complete set of UNO cards that can be drawn and played.
    """
    discard_pile: List[C] = Field(default_factory=list)
    
    def draw(self) -> Optional[C]:
        """
        Draw the top card.
        
        Returns:
            The top card, or None if the deck is empty
        """
        if not self.pieces:
            # If main deck is empty, shuffle discard pile and use it
            if self.discard_pile:
                self.recycle_discards()
            else:
                return None
        
        return self.pieces.pop(0)
    
    def discard(self, card: C) -> None:
        """
        Add a card to the discard pile.
        
        Args:
            card: Card to discard
        """
        card.face_up = True  # Ensure card is face up for discard pile
        self.discard_pile.append(card)
    
    def recycle_discards(self) -> None:
        """Shuffle the discard pile and add it to the bottom of the deck."""
        if not self.discard_pile:
            return
            
        # Keep the top card of the discard pile visible
        top_card = self.discard_pile.pop() if self.discard_pile else None
        
        # Shuffle the rest and add to the deck
        import random
        random.shuffle(self.discard_pile)
        self.pieces.extend(self.discard_pile)
        self.discard_pile.clear()
        
        # Put the top card back on the discard pile
        if top_card:
            self.discard_pile.append(top_card)
    
    def get_top_discard(self) -> Optional[C]:
        """
        Get the top card of the discard pile without removing it.
        
        Returns:
            The top discard card, or None if the discard pile is empty
        """
        if not self.discard_pile:
            return None
        return self.discard_pile[-1]
    
    @classmethod
    def create_standard_deck(cls) -> 'UnoDeck[UnoCard]':
        """
        Create a standard 108-card UNO deck.
        
        Returns:
            A new UnoDeck with standard UNO cards
        """
        deck = cls(name="UNO Deck")
        
        # Add number cards (0-9)
        # One 0 card and two 1-9 cards for each color
        for color in [UnoColor.RED, UnoColor.YELLOW, UnoColor.GREEN, UnoColor.BLUE]:
            # Add one 0 card
            deck.add(UnoCard(color=color, value=UnoValue.ZERO))
            
            # Add two of each 1-9 card
            for value in [
                UnoValue.ONE, UnoValue.TWO, UnoValue.THREE, UnoValue.FOUR,
                UnoValue.FIVE, UnoValue.SIX, UnoValue.SEVEN, UnoValue.EIGHT,
                UnoValue.NINE
            ]:
                deck.add(UnoCard(color=color, value=value))
                deck.add(UnoCard(color=color, value=value))
        
        # Add action cards (Skip, Reverse, Draw Two)
        # Two of each action card for each color
        for color in [UnoColor.RED, UnoColor.YELLOW, UnoColor.GREEN, UnoColor.BLUE]:
            for value in [UnoValue.SKIP, UnoValue.REVERSE, UnoValue.DRAW_TWO]:
                deck.add(UnoCard(color=color, value=value))
                deck.add(UnoCard(color=color, value=value))
        
        # Add wild cards
        # Four of each wild card type
        for _ in range(4):
            deck.add(UnoCard(color=UnoColor.WILD, value=UnoValue.WILD))
            deck.add(UnoCard(color=UnoColor.WILD, value=UnoValue.WILD_DRAW_FOUR))
        
        # Shuffle the deck
        deck.shuffle()
        
        return deck