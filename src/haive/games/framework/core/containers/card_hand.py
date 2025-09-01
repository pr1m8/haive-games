# haive/games/framework/core/containers/card_hand.py
from typing import List, Optional, TypeVar
from pydantic import computed_field

from haive.games.framework.core.container import GamePieceContainer
from haive.games.framework.core.containers.hand import Hand
from haive.games.framework.core.pieces.card import Card
from haive.games.framework.core.pieces.uno_card import UnoCard

# Type variable for cards
C = TypeVar('C', bound=Card)

class CardHand(Hand[C]):
    """
    A hand of playing cards.
    
    This represents a player's hand in a card game, with card-specific
    functionality like sorting by suit/rank.
    """
    
    def sort_by_suit_rank(self) -> None:
        """Sort cards by suit then rank."""
        self.sort(key=lambda card: (
            getattr(card, 'suit', ''),
            getattr(card, 'value', 0)
        ))
    
    def sort_by_rank_suit(self) -> None:
        """Sort cards by rank then suit."""
        self.sort(key=lambda card: (
            getattr(card, 'value', 0),
            getattr(card, 'suit', '')
        ))
    
    def get_cards_of_suit(self, suit) -> List[C]:
        """
        Get all cards of a specific suit.
        
        Args:
            suit: The suit to filter by
            
        Returns:
            List of cards with the specified suit
        """
        return [card for card in self.pieces if hasattr(card, 'suit') and card.suit == suit]
    
    def get_cards_of_rank(self, rank) -> List[C]:
        """
        Get all cards of a specific rank.
        
        Args:
            rank: The rank to filter by
            
        Returns:
            List of cards with the specified rank
        """
        return [card for card in self.pieces if hasattr(card, 'value') and card.value == rank]
    
    @computed_field
    @property
    def visible_to_others(self) -> bool:
        """Check if all cards are face up (visible)."""
        return all(getattr(card, 'face_up', False) for card in self.pieces)

class UnoHand(CardHand[UnoCard]):
    """
    A hand of UNO cards.
    
    This extends the card hand with UNO-specific functionality.
    """
    
    def get_playable_cards(self, top_card: UnoCard) -> List[UnoCard]:
        """
        Get all cards that can be played on the given top card.
        
        Args:
            top_card: The top card on the discard pile
            
        Returns:
            List of cards that can be legally played
        """
        return [card for card in self.pieces if card.matches(top_card)]
    
    def has_playable_card(self, top_card: UnoCard) -> bool:
        """
        Check if the hand has any card that can be played.
        
        Args:
            top_card: The top card on the discard pile
            
        Returns:
            True if at least one card can be played, False otherwise
        """
        return any(card.matches(top_card) for card in self.pieces)
    
    @computed_field
    @property
    def points(self) -> int:
        """Get the total point value of cards in the hand."""
        return sum(card.points for card in self.pieces)