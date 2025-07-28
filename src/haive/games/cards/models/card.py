"""Card representation and operations for card games.

This module provides classes for representing playing cards, including ranks,
suits, and card values. It's designed to be used in various card game implementations
with consistent handling of card comparisons and representations.

Example:
    >>> from haive.games.cards.models.card import Card, Rank, Suit
    >>> card = Card(Rank.ACE, Suit.SPADES)
    >>> print(card)
    A`
    >>> card.value
    14
"""

from enum import Enum, auto


class Suit(Enum):
    """Playing card suits.

    Standard card suits for a 52-card deck, with optional support for
    additional special suits in non-standard decks.
    """

    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()
    JOKER = auto()  # Special suit for joker cards

    def __str__(self) -> str:
        """Return the Unicode symbol for the suit.

        Returns:
            The Unicode character representing the suit.
        """
        return {
            Suit.CLUBS: "c",
            Suit.DIAMONDS: "f",
            Suit.HEARTS: "e",
            Suit.SPADES: "`",
            Suit.JOKER: "",
        }[self]

    @property
    def color(self) -> str:
        """Get the color of the suit (red or black).

        Returns:
            The color as a string: "red" or "black".
        """
        if self in [Suit.HEARTS, Suit.DIAMONDS]:
            return "red"
        return "black"


class Rank(Enum):
    """Playing card ranks.

    Standard card ranks for a 52-card deck, with values that facilitate
    numeric comparisons between cards.
    """

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14  # High ace by default
    JOKER = 15  # Higher than all standard cards

    def __str__(self) -> str:
        """Return a string representation of the rank.

        Returns:
            A string representation suitable for display.
        """
        rank_str = {
            Rank.ACE: "A",
            Rank.TWO: "2",
            Rank.THREE: "3",
            Rank.FOUR: "4",
            Rank.FIVE: "5",
            Rank.SIX: "6",
            Rank.SEVEN: "7",
            Rank.EIGHT: "8",
            Rank.NINE: "9",
            Rank.TEN: "10",
            Rank.JACK: "J",
            Rank.QUEEN: "Q",
            Rank.KING: "K",
            Rank.JOKER: "Joker",
        }
        return rank_str[self]


class Card:
    """A playing card with rank and suit.

    Represents a standard playing card with rank and suit, providing methods
    for comparison, display, and game-specific value calculations.

    Attributes:
        rank: The rank of the card (2-10, J, Q, K, A, Joker).
        suit: The suit of the card (clubs, diamonds, hearts, spades, joker).
        value: The numeric value of the card for comparisons.

    Examples:
        >>> card = Card(Rank.ACE, Suit.SPADES)
        >>> print(card)
        A`
        >>> card.value
        14
        >>> card.long_name
        'Ace of Spades'
    """

    def __init__(self, rank: Rank, suit: Suit):
        """Initialize a card with rank and suit.

        Args:
            rank: The rank of the card.
            suit: The suit of the card.

        Raises:
            ValueError: If a standard card is created with Joker suit but not Joker rank.
        """
        if suit == Suit.JOKER and rank != Rank.JOKER:
            raise ValueError("Cards with Joker suit must have Joker rank")

        self.rank = rank
        self.suit = suit
        self.value = rank.value

    def __str__(self) -> str:
        """Return a string representation of the card.

        Returns:
            A string with rank and suit symbols.
        """
        return f"{self.rank}{self.suit}"

    def __repr__(self) -> str:
        """Return a detailed representation of the card.

        Returns:
            A string representation for debugging.
        """
        return f"Card({self.rank}, {self.suit})"

    def __eq__(self, other: object) -> bool:
        """Check if two cards are equal.

        Args:
            other: Another card to compare with.

        Returns:
            True if the cards have the same rank and suit, False otherwise.
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: "Card") -> bool:
        """Check if this card has a lower value than another.

        Args:
            other: Another card to compare with.

        Returns:
            True if this card's value is less than the other card's value.
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.value < other.value

    def __gt__(self, other: "Card") -> bool:
        """Check if this card has a higher value than another.

        Args:
            other: Another card to compare with.

        Returns:
            True if this card's value is greater than the other card's value.
        """
        if not isinstance(other, Card):
            return NotImplemented
        return self.value > other.value

    @property
    def long_name(self) -> str:
        """Get the full name of the card.

        Returns:
            A string with the full name (e.g., "Ace of Spades").
        """
        if self.rank == Rank.JOKER:
            return "Jokef"

        rank_names = {
            Rank.ACE: "Ace",
            Rank.TWO: "Two",
            Rank.THREE: "Three",
            Rank.FOUR: "Four",
            Rank.FIVE: "Five",
            Rank.SIX: "Six",
            Rank.SEVEN: "Seven",
            Rank.EIGHT: "Eight",
            Rank.NINE: "Nine",
            Rank.TEN: "Ten",
            Rank.JACK: "Jack",
            Rank.QUEEN: "Queen",
            Rank.KING: "King",
        }

        suit_names = {
            Suit.CLUBS: "Clubs",
            Suit.DIAMONDS: "Diamonds",
            Suit.HEARTS: "Hearts",
            Suit.SPADES: "Spades",
        }

        return f"{rank_names[self.rank]} of {suit_names[self.suit]}"

    def blackjack_value(self) -> int:
        """Calculate the value of the card in Blackjack.

        Aces are worth 11 by default (caller should handle alternate values).
        Face cards (J, Q, K) are worth 10.

        Returns:
            The card's value in Blackjack.
        """
        if self.rank == Rank.ACE:
            return 11
        if self.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]:
            return 10
        return self.rank.value

    def is_face_card(self) -> bool:
        """Check if the card is a face card (Jack, Queen, or King).

        Returns:
            True if the card is a face card, False otherwise.
        """
        return self.rank in [Rank.JACK, Rank.QUEEN, Rank.KING]

    @classmethod
    def from_string(cls, card_str: str) -> "Card":
        """Create a card from a string representation.

        Args:
            card_str: A string like "AH" (Ace of Hearts) or "10S" (Ten of Spades).

        Returns:
            A new Card instance.

        Raises:
            ValueError: If the string format is invalid.
        """
        if len(card_str) < 2:
            raise ValueError(f"Invalid card string: {card_str}")

        # Handle 10 as a special case
        if card_str.startswith("10"):
            rank_str = "10"
            suit_str = card_str[2:]
        else:
            rank_str = card_str[0]
            suit_str = card_str[1:]

        # Map rank string to Rank enum
        rank_map = {
            "2": Rank.TWO,
            "3": Rank.THREE,
            "4": Rank.FOUR,
            "5": Rank.FIVE,
            "6": Rank.SIX,
            "7": Rank.SEVEN,
            "8": Rank.EIGHT,
            "9": Rank.NINE,
            "10": Rank.TEN,
            "J": Rank.JACK,
            "Q": Rank.QUEEN,
            "K": Rank.KING,
            "A": Rank.ACE,
        }

        # Map suit string to Suit enum
        suit_map = {
            "C": Suit.CLUBS,
            "D": Suit.DIAMONDS,
            "H": Suit.HEARTS,
            "S": Suit.SPADES,
        }

        if rank_str not in rank_map:
            raise ValueError(f"Invalid rank: {rank_str}")

        if suit_str not in suit_map:
            raise ValueError(f"Invalid suit: {suit_str}")

        return cls(rank_map[rank_str], suit_map[suit_str])
