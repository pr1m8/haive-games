"""Card game models and data structures.

This package provides fundamental models for card game components including
cards, decks, and hands. These models form the foundation for implementing
various card games while maintaining consistent behavior and interfaces.

Modules:
    card: Card representation with rank and suit enumerations
    deck: Deck management with operations like shuffling and drawing
    hand: Hand representation with game-specific evaluation logic

Example:
    >>> from haive.games.cards.models import Card, Deck, Hand, Rank, Suit
    >>> # Create a standard deck
    >>> deck = Deck.standard_deck()
    >>> # Shuffle and draw cards
    >>> deck.shuffle()
    >>> hand = Hand([deck.draw() for _ in range(5)])
    >>> # Evaluate the hand
    >>> is_flush = hand.is_flush()
"""

from haive.games.cards.models.card import Card, Rank, Suit

__all__ = [
    "Card",
    "Rank",
    "Suit",
]
