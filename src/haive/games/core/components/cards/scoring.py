"""Scoring core module.

This module provides scoring functionality for the Haive framework.

Classes:
    HandRank: HandRank implementation.
    HandEvaluator: HandEvaluator implementation.
    Config: Config implementation.

Functions:
    evaluate: Evaluate functionality.
"""

# haive/games/core/components/cards/scoring.py


from pydantic import BaseModel, Field

from haive.games.core.components.models import TCard


class HandRank(BaseModel, Generic[TCard]):
    """Representation of a hand's rank in a card game."""

    rank_name: str
    rank_value: int
    primary_cards: list[TCard] = Field(default_factory=list)
    secondary_cards: list[TCard] = Field(default_factory=list)

    def __lt__(self, other: "HandRank") -> bool:
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.rank_value < other.rank_value

    def __eq__(self, other: "HandRank") -> bool:
        if not isinstance(other, HandRank):
            return NotImplemented
        return self.rank_value == other.rank_value


class HandEvaluator(BaseModel, Generic[TCard]):
    """Base model for hand evaluation strategies."""

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def evaluate(cls, cards: list[TCard], context: dict = None) -> HandRank[TCard]:
        """Evaluate a hand of cards."""
        raise NotImplementedError("Subclasses must implement evaluate method")

    @classmethod
    def compare_hands(
        cls, hand1: list[TCard], hand2: list[TCard], context: dict = None
    ) -> int:
        """Compare two hands.

        Returns: -1 if hand1 < hand2, 0 if equal, 1 if hand1 > hand2.
        """
        rank1 = cls.evaluate(hand1, context)
        rank2 = cls.evaluate(hand2, context)

        if rank1 < rank2:
            return -1
        if rank1 > rank2:
            return 1
        return 0
