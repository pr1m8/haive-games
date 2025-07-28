"""Standard core module.

This module provides standard functionality for the Haive framework.

Classes:
    StandardSuit: StandardSuit implementation.
    StandardRank: StandardRank implementation.
    StandardCard: StandardCard implementation.

Functions:
    set_value: Set Value functionality.
    set_face_card: Set Face Card functionality.
    set_color: Set Color functionality.
"""

# haive/games/core/components/cards/standard.py

from enum import Enum
from typing import ClassVar

from pydantic import validator

from haive.games.core.components.models import Card, Deck


class StandardSuit(str, Enum):
    """Standard card suits."""

    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"


class StandardRank(str, Enum):
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


class StandardCard(Card):
    """Standard playing card."""

    suit: StandardSuit
    rank: StandardRank

    # Computed properties with validators
    value: int = 0
    is_face_card: bool = False
    color: str = "black"

    _rank_values: ClassVar[dict[StandardRank, int]] = {
        StandardRank.ACE: 1,  # Default low ace
        StandardRank.TWO: 2,
        StandardRank.THREE: 3,
        StandardRank.FOUR: 4,
        StandardRank.FIVE: 5,
        StandardRank.SIX: 6,
        StandardRank.SEVEN: 7,
        StandardRank.EIGHT: 8,
        StandardRank.NINE: 9,
        StandardRank.TEN: 10,
        StandardRank.JACK: 11,
        StandardRank.QUEEN: 12,
        StandardRank.KING: 13,
    }

    @validator("value", pre=True, always=True)
    def set_value(cls, v, values):
        """Auto-set value based on rank."""
        if v != 0:
            return v

        rank = values.get("rank")
        if not rank:
            return 0

        return cls._rank_values.get(rank, 0)

    @validator("is_face_card", pre=True, always=True)
    def set_face_card(cls, v, values):
        """Determine if this is a face card."""
        if "rank" not in values:
            return False

        rank = values["rank"]
        return rank in [StandardRank.JACK, StandardRank.QUEEN, StandardRank.KING]

    @validator("color", pre=True, always=True)
    def set_color(cls, v, values):
        """Set card color based on suit."""
        if v != "black":
            return v

        if "suit" not in values:
            return "black"

        suit = values["suit"]
        if suit in [StandardSuit.HEARTS, StandardSuit.DIAMONDS]:
            return "red"
        return "black"

    @validator("name", pre=True, always=True)
    def set_name(cls, v, values):
        """Set default name based on rank and suit."""
        if v:
            return v

        if "rank" in values and "suit" in values:
            return f"{values['rank'].value} of {values['suit'].value}"
        return "Unknown Card"

    def __str__(self) -> str:
        """String representation of card."""
        return self.format()

    def format(self) -> str:
        """Format the card for display."""
        rank_display = {
            StandardRank.ACE: "A",
            StandardRank.KING: "K",
            StandardRank.QUEEN: "Q",
            StandardRank.JACK: "J",
            StandardRank.TEN: "10",
            StandardRank.NINE: "9",
            StandardRank.EIGHT: "8",
            StandardRank.SEVEN: "7",
            StandardRank.SIX: "6",
            StandardRank.FIVE: "5",
            StandardRank.FOUR: "4",
            StandardRank.THREE: "3",
            StandardRank.TWO: "2",
        }

        suit_display = {
            StandardSuit.HEARTS: "♥",
            StandardSuit.DIAMONDS: "♦",
            StandardSuit.CLUBS: "♣",
            StandardSuit.SPADES: "♠",
        }

        return f"{rank_display.get(self.rank, self.rank.value)}{suit_display.get(self.suit, '')}"


class StandardDeckFactory:
    """Factory for creating standard card decks."""

    @staticmethod
    def create_standard_deck(include_jokers: bool = False) -> Deck[StandardCard]:
        """Create a standard 52-card deck."""
        cards = []

        # Create all suit/rank combinations
        for suit in StandardSuit:
            for rank in StandardRank:
                cards.append(StandardCard(suit=suit, rank=rank))

        # Add jokers if requested
        if include_jokers:
            cards.append(
                Card(name="Red Jokef", properties={"is_joker": True, "color": "red"})
            )
            cards.append(
                Card(
                    name="Black Jokef", properties={"is_joker": True, "color": "black"}
                )
            )

        # Create and return the deck
        deck = Deck[StandardCard](name="Standard Deck", cards=cards)
        deck.shuffle()
        return deck

    @staticmethod
    def create_pinochle_deck() -> Deck[StandardCard]:
        """Create a pinochle deck (2 copies of 9-A)."""
        cards = []
        for _ in range(2):  # Two copies
            for suit in StandardSuit:
                for rank in [
                    StandardRank.NINE,
                    StandardRank.TEN,
                    StandardRank.JACK,
                    StandardRank.QUEEN,
                    StandardRank.KING,
                    StandardRank.ACE,
                ]:
                    cards.append(StandardCard(suit=suit, rank=rank))

        deck = Deck[StandardCard](name="Pinochle Deck", cards=cards)
        deck.shuffle()
        return deck


class StandardCardComparator:
    """Comparator for standard playing cards."""

    @classmethod
    def compare(
        cls, card1: StandardCard, card2: StandardCard, context: dict = None
    ) -> int:
        """Compare two standard cards."""
        context = context or {}
        aces_high = context.get("aces_high", False)

        # Adjust values for aces high
        value1 = card1.value
        value2 = card2.value

        if aces_high:
            if card1.rank == StandardRank.ACE:
                value1 = 14
            if card2.rank == StandardRank.ACE:
                value2 = 14

        # Compare by rank first
        if value1 < value2:
            return -1
        if value1 > value2:
            return 1

        # If ranks match, compare by suit if needed
        if context.get("compare_suits", False):
            suit_order = {
                StandardSuit.CLUBS: 1,
                StandardSuit.DIAMONDS: 2,
                StandardSuit.HEARTS: 3,
                StandardSuit.SPADES: 4,
            }

            suit1 = suit_order.get(card1.suit, 0)
            suit2 = suit_order.get(card2.suit, 0)

            if suit1 < suit2:
                return -1
            if suit1 > suit2:
                return 1

        # Cards are equal
        return 0

    @classmethod
    def sort_cards(
        cls, cards: list[StandardCard], context: dict = None
    ) -> list[StandardCard]:
        """Sort standard cards by rank and optionally suit."""
        return sorted(
            cards, key=functools.cmp_to_key(lambda a, b: cls.compare(a, b, context))
        )
