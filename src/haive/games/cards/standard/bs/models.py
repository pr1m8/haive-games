import random
from enum import Enum

from pydantic import BaseModel, Field


class CardSuit(str, Enum):
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"


class Card(BaseModel):
    """Represents a playing card."""

    value: str  # 2-10, J, Q, K, A
    suit: CardSuit

    def __str__(self) -> str:
        return f"{self.value} of {self.suit.value}"

    @classmethod
    def create_deck(cls) -> list["Card"]:
        """Create a full deck of 52 cards."""
        suits = list(CardSuit)
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        deck = [cls(value=value, suit=suit) for suit in suits for value in values]
        random.shuffle(deck)
        return deck


class PlayerClaimAction(BaseModel):
    """Represents a player's claim during their turn."""

    claimed_value: str = Field(..., description="The value of cards being claimed")
    number_of_cards: int = Field(..., description="Number of cards being played")
    is_truth: bool = Field(..., description="Whether the player is telling the truth")
    reasoning: str | None = Field(
        default=None, description="Reasoning behind the claim"
    )


class ChallengeAction(BaseModel):
    """Represents a player challenging another player's claim."""

    challenge_type: str = Field(..., description="Type of challenge")
    target_player_index: int = Field(
        ..., description="Index of the player being challenged"
    )
    reasoning: str | None = Field(
        default=None, description="Reasoning behind the challenge"
    )


class PlayerState(BaseModel):
    """Represents a player's state in the Bullshit game."""

    name: str
    hand: list[Card] = Field(default_factory=list)
    cards_played: list[Card] = Field(default_factory=list)

    def play_cards(self, cards: list[Card]) -> None:
        """Remove played cards from hand."""
        for card in cards:
            self.hand.remove(card)
            self.cards_played.append(card)
