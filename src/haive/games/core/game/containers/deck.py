"""
Deck classes for card games in the game framework.

This module defines the Deck container type and related classes for card games.
"""

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Type, TypeVar

from game_framework.containers.base import GamePieceContainer
from game_framework.pieces.base import GamePiece
from pydantic import Field

# We would normally import from card.py, but since we haven't fully implemented it yet
# we'll create a simple Card type for illustration


class Card(GamePiece):
    """Simple Card class for illustration."""

    face_up: bool = False

    def flip(self) -> None:
        """Flip the card face up/down."""
        self.face_up = not self.face_up


# Type variable for cards
C = TypeVar("C", bound=Card)


class Deck(GamePieceContainer[C]):
    """
    A deck of cards.

    This represents a collection of cards that can be drawn, shuffled, and dealt.
    """

    face_down: bool = True  # Whether cards are hidden by default
    discard_pile: List[C] = Field(default_factory=list)

    def draw(self) -> Optional[C]:
        """
        Draw the top card and set its face up/down based on deck configuration.

        Returns:
            The drawn card, or None if deck is empty
        """
        if not self.pieces:
            return None
        card = self.pieces.pop(0)
        card.face_up = not self.face_down
        return card

    def deal(self, num_players: int, cards_per_player: int) -> List[List[C]]:
        """
        Deal cards to multiple players.

        Args:
            num_players: Number of players to deal to
            cards_per_player: Number of cards per player

        Returns:
            List of lists, where each inner list contains a player's cards
        """
        hands = [[] for _ in range(num_players)]
        for i in range(cards_per_player):
            for player in range(num_players):
                if self.pieces:
                    card = self.draw()
                    if card:
                        hands[player].append(card)
        return hands

    def discard(self, card: C) -> None:
        """
        Add a card to the discard pile.

        Args:
            card: Card to discard
        """
        self.discard_pile.append(card)

    def recycle_discards(self, shuffle: bool = True) -> None:
        """
        Move all cards from discard pile back into the deck.

        Args:
            shuffle: Whether to shuffle the deck after recycling
        """
        self.pieces.extend(self.discard_pile)
        self.discard_pile.clear()
        if shuffle:
            self.shuffle()

    def peek_top(self, count: int = 1) -> List[C]:
        """
        Look at top cards without drawing.

        Args:
            count: Number of cards to peek at

        Returns:
            List of cards from the top
        """
        return self.peek(count)

    def peek_bottom(self, count: int = 1) -> List[C]:
        """
        Look at bottom cards without drawing.

        Args:
            count: Number of cards to peek at

        Returns:
            List of cards from the bottom
        """
        return self.pieces[-count:] if count <= len(self.pieces) else self.pieces.copy()

    def draw_bottom(self) -> Optional[C]:
        """
        Draw the bottom card.

        Returns:
            The bottom card, or None if deck is empty
        """
        if not self.pieces:
            return None
        card = self.pieces.pop()
        card.face_up = not self.face_down
        return card

    def insert(self, card: C, position: int) -> None:
        """
        Insert a card at a specific position.

        Args:
            card: Card to insert
            position: Position to insert at (0 for top, len(self.pieces) for bottom)

        Raises:
            ValueError: If position is out of bounds
        """
        if position < 0 or position > len(self.pieces):
            raise ValueError(f"Position {position} is out of bounds")
        self.pieces.insert(position, card)

    def place_on_bottom(self, card: C) -> None:
        """
        Place a card on the bottom of the deck.

        Args:
            card: Card to place
        """
        self.pieces.append(card)


class StandardPlayingCardDeck(Deck):
    """A standard 52-card playing card deck."""

    class Suit(str, Enum):
        """Standard card suits."""

        HEARTS = "hearts"
        DIAMONDS = "diamonds"
        CLUBS = "clubs"
        SPADES = "spades"

    class Rank(str, Enum):
        """Standard card ranks."""

        ACE = "ace"
        TWO = "2"
        THREE = "3"
        FOUR = "4"
        FIVE = "5"
        SIX = "6"
        SEVEN = "7"
        EIGHT = "8"
        NINE = "9"
        TEN = "10"
        JACK = "jack"
        QUEEN = "queen"
        KING = "king"

    @classmethod
    def create_standard_deck(
        cls, include_jokers: bool = False
    ) -> "StandardPlayingCardDeck":
        """
        Create a standard 52-card deck.

        Args:
            include_jokers: Whether to include jokers in the deck

        Returns:
            A new StandardPlayingCardDeck instance
        """
        # Since we don't have the full PlayingCard implementation,
        # we'll just illustrate the structure here
        deck = cls(name="Standard Deck")

        # Add cards for each suit and rank
        for suit in cls.Suit:
            for rank in cls.Rank:
                # In a real implementation, we would use PlayingCard here
                card = Card(name=f"{rank.value} of {suit.value}")
                card.set_property("suit", suit)
                card.set_property("rank", rank)
                deck.add(card, "bottom")

        # Add jokers if requested
        if include_jokers:
            deck.add(Card(name="Red Joker"), "bottom")
            deck.add(Card(name="Black Joker"), "bottom")

        # Shuffle the deck
        deck.shuffle()

        return deck
