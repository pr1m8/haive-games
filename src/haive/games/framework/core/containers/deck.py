# game_framework/containers/deck.py
from __future__ import annotations

from typing import TypeVar

from pydantic import Field

from haive.games.framework.core.container import GamePieceContainer
from haive.games.framework.pieces.card import Card, CardRank, CardSuit, PlayingCard

# Type variable for cards
C = TypeVar("C", bound=Card)


class Deck(GamePieceContainer[C]):
    """A deck of cards.

    This represents a collection of cards that can be drawn, shuffled, and dealt.
    """

    face_down: bool = True  # Whether cards are hidden by default
    discard_pile: list[C] = Field(default_factory=list)

    def draw(self) -> C | None:
        """Draw the top card and set its face up/down based on deck configuration.

        Returns:
            The drawn card, or None if deck is empty
        """
        if not self.pieces:
            return None
        card = self.pieces.pop(0)
        card.face_up = not self.face_down
        return card

    def draw_many(self, count: int) -> list[C]:
        """Draw multiple cards from the top.

        Args:
            count: Number of cards to draw

        Returns:
            List of drawn cards
        """
        result = []
        for _ in range(min(count, len(self.pieces))):
            card = self.draw()
            if card:
                result.append(card)
        return result

    def discard(self, card: C) -> None:
        """Add a card to the discard pile.

        Args:
            card: Card to discard
        """
        self.discard_pile.append(card)

    @classmethod
    def create_standard_deck(cls) -> Deck[PlayingCard]:
        """Create a standard 52-card deck.

        Returns:
            A new deck with standard playing cards
        """
        deck = cls(name="Standard Deck")

        # Create a card for each suit and rank
        for suit in CardSuit:
            for rank in CardRank:
                card = PlayingCard(suit=suit, rank=rank)
                deck.add(card)

        # Shuffle the new deck
        deck.shuffle()

        return deck
