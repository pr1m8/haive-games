# haive/games/core/components/cards/models.py

from __future__ import annotations

import random
import uuid
from collections.abc import Sequence
from typing import Generic, Protocol, TypeVar

from pydantic import BaseModel, Field

from haive.games.core.components.cards.actions import CardAction

# Type variables for generic relationships
TCard = TypeVar("TCard", bound="Card")
TAction = TypeVar("TAction", bound="CardAction")
TState = TypeVar("TState", bound="CardGameState")


class Card(BaseModel):
    """Base model for all cards."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    face_up: bool = False
    owner_id: str | None = None

    class Config:
        arbitrary_types_allowed = True

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        if not isinstance(other, Card):
            return False
        return self.id == other.id

    def flip(self) -> None:
        """Flip the card's visibility."""
        self.face_up = not self.face_up


class CardContainer(BaseModel, Generic[TCard]):
    """Base model for any collection of cards."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    cards: list[TCard] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def add(self, card: TCard, position: str = "top") -> None:
        """Add a card to this container."""
        if position == "top":
            self.cards.insert(0, card)
        elif position == "bottom":
            self.cards.append(card)
        elif position == "random":
            idx = random.randint(0, len(self.cards))
            self.cards.insert(idx, card)
        else:
            raise ValueError(f"Unknown position: {position}")

    def remove(self, card_id: str) -> TCard | None:
        """Remove a card by ID."""
        for i, card in enumerate(self.cards):
            if card.id == card_id:
                return self.cards.pop(i)
        return None

    def count(self) -> int:
        """Count cards in the container."""
        return len(self.cards)

    def is_empty(self) -> bool:
        """Check if container is empty."""
        return len(self.cards) == 0

    def shuffle(self) -> None:
        """Shuffle the cards."""
        random.shuffle(self.cards)

    @classmethod
    def of_type(cls, card_type: type[TCard]) -> type[CardContainer[TCard]]:
        """Create a type-specific card container."""
        return cls[card_type]  # Leverage Generic type specialization


class Deck(CardContainer[TCard]):
    """A deck of cards that can be drawn from."""

    face_down: bool = True  # Whether cards are hidden by default

    def draw(self) -> TCard | None:
        """Draw the top card."""
        if not self.cards:
            return None
        card = self.cards.pop(0)
        card.face_up = not self.face_down
        return card

    def draw_many(self, count: int) -> list[TCard]:
        """Draw multiple cards."""
        return [self.draw() for _ in range(min(count, len(self.cards)))]

    def peek_top(self, count: int = 1) -> list[TCard]:
        """Look at top cards without drawing."""
        return self.cards[: min(count, len(self.cards))]


class Hand(CardContainer[TCard]):
    """A player's hand of cards."""

    player_id: str

    def add_card(self, card: TCard) -> None:
        """Add a card to the hand."""
        card.owner_id = self.player_id
        self.cards.append(card)

    def play_card(self, card_id: str) -> TCard | None:
        """Play a card (remove and mark as face up)."""
        card = self.remove(card_id)
        if card:
            card.face_up = True
        return card


class CardComparator(Protocol, Generic[TCard]):
    """Protocol for card comparison strategies."""

    @classmethod
    def compare(cls, card1: TCard, card2: TCard, context: dict = None) -> int:
        """Compare two cards."""
        ...

    @classmethod
    def sort_cards(cls, cards: Sequence[TCard], context: dict = None) -> list[TCard]:
        """Sort a list of cards."""
        ...
