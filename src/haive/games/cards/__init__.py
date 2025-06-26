"""
Card game utilities and implementations.

This package provides comprehensive utilities for implementing card games
within the Haive framework. It includes card, deck, and hand representations,
along with evaluation logic for various card game combinations.

The package is designed to be both:
1. A standalone utility for card manipulation
2. A building block for more complex card game implementations

Key components:
    - Card: Representation of a playing card with rank and suit
    - Deck: Collection of cards with operations like shuffling and drawing
    - Hand: Collection of cards held by a player with evaluation logic
    - SpecializedDeck: Custom deck implementations for specific games

Example:
    >>> from haive.games.cards import Deck, Hand
    >>> # Create a standard deck and shuffle it
    >>> deck = Deck.standard_deck()
    >>> deck.shuffle()
    >>> # Deal a poker hand
    >>> hand = Hand([deck.draw() for _ in range(5)])
    >>> # Check if it's a flush
    >>> if hand.is_flush():
    ...     print("You have a flush!")
"""

from haive.games.cards.models.card import Card, Rank, Suit

# Note: The following imports are commented out because the modules don't exist yet
# They should be uncommented when the modules are implemented
# from haive.games.cards.deck import Deck, SpecializedDeck
# from haive.games.cards.hand import Hand, PokerHandType

__all__ = [
    "Card",
    "Rank",
    "Suit",
    # "Deck",
    # "SpecializedDeck",
    # "Hand",
    # "PokerHandType",
]

__version__ = "1.0.0"
