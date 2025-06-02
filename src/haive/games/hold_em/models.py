"""Texas Hold'em game models module.

This module provides data models for the Texas Hold'em game, including:
    - Player decisions
    - Hand evaluation
    - Betting actions
    - Structured output models for LLMs
"""

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, field_validator


class HandRank(str, Enum):
    """Hand rankings in poker."""

    HIGH_CARD = "high_card"
    PAIR = "pair"
    TWO_PAIR = "two_pair"
    THREE_OF_A_KIND = "three_of_a_kind"
    STRAIGHT = "straight"
    FLUSH = "flush"
    FULL_HOUSE = "full_house"
    FOUR_OF_A_KIND = "four_of_a_kind"
    STRAIGHT_FLUSH = "straight_flush"
    ROYAL_FLUSH = "royal_flush"


class PokerAction(str, Enum):
    """Possible poker actions."""

    FOLD = "fold"
    CHECK = "check"
    CALL = "call"
    BET = "bet"
    RAISE = "raise"
    ALL_IN = "all_in"


class Position(str, Enum):
    """Player positions."""

    SMALL_BLIND = "small_blind"
    BIG_BLIND = "big_blind"
    UNDER_THE_GUN = "under_the_gun"
    MIDDLE_POSITION = "middle_position"
    LATE_POSITION = "late_position"
    CUTOFF = "cutoff"
    BUTTON = "button"


class PokerCard(BaseModel):
    """Model for a poker card."""

    rank: str = Field(description="Card rank (2-A)")
    suit: str = Field(description="Card suit (hearts, diamonds, clubs, spades)")

    @field_validator("rank")
    def validate_rank(cls, v: str) -> str:
        """Validate card rank."""
        valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        if v not in valid_ranks:
            raise ValueError(f"Invalid rank: {v}")
        return v

    @field_validator("suit")
    def validate_suit(cls, v: str) -> str:
        """Validate card suit."""
        valid_suits = ["hearts", "diamonds", "clubs", "spades", "h", "d", "c", "s"]
        if v not in valid_suits:
            raise ValueError(f"Invalid suit: {v}")
        return v

    def __str__(self) -> str:
        """String representation of card."""
        suit_symbols = {
            "hearts": "♥",
            "diamonds": "♦",
            "clubs": "♣",
            "spades": "♠",
            "h": "♥",
            "d": "♦",
            "c": "♣",
            "s": "♠",
        }
        return f"{self.rank}{suit_symbols.get(self.suit, self.suit)}"


class HandEvaluation(BaseModel):
    """Model for hand evaluation."""

    hand_rank: HandRank = Field(description="Rank of the hand")
    strength: float = Field(description="Hand strength (0-1)")
    description: str = Field(description="Human-readable description")
    kickers: List[str] = Field(default_factory=list, description="Kicker cards")
    made_hand: List[str] = Field(
        default_factory=list, description="Cards that make the hand"
    )


class PlayerDecisionModel(BaseModel):
    """Model for player decision-making."""

    action: PokerAction = Field(description="Chosen action")
    amount: int = Field(default=0, description="Amount for bet/raise")
    reasoning: str = Field(description="Reasoning for the decision")
    confidence: float = Field(default=0.5, description="Confidence in decision (0-1)")
    hand_strength_estimate: Optional[str] = Field(
        default=None, description="Estimated hand strength"
    )

    @field_validator("amount")
    def validate_amount(cls, v: int) -> int:
        """Validate bet amount."""
        if v < 0:
            raise ValueError("Amount cannot be negative")
        return v

    @field_validator("confidence")
    def validate_confidence(cls, v: float) -> float:
        """Validate confidence score."""
        if not 0 <= v <= 1:
            raise ValueError("Confidence must be between 0 and 1")
        return v


class PokerAnalysis(BaseModel):
    """Model for poker position analysis."""

    hand_strength: float = Field(description="Estimated hand strength (0-1)")
    pot_odds: float = Field(description="Current pot odds")
    position_advantage: str = Field(description="Position assessment")
    opponent_analysis: List[str] = Field(
        default_factory=list, description="Analysis of opponents"
    )
    recommended_actions: List[str] = Field(
        default_factory=list, description="Recommended actions in order of preference"
    )
    bluff_potential: float = Field(default=0.0, description="Bluff potential (0-1)")
    fold_equity: float = Field(default=0.0, description="Fold equity estimate (0-1)")


class GameSituationAnalysis(BaseModel):
    """Analysis of the current game situation."""

    stack_sizes: Dict[str, int] = Field(
        default_factory=dict, description="Stack sizes of all players"
    )
    pot_size: int = Field(description="Current pot size")
    players_in_hand: int = Field(description="Number of players in hand")
    betting_action: str = Field(description="Description of betting action so far")
    position_description: str = Field(description="Player's position description")
    game_stage: str = Field(description="Current stage of the hand")


class BettingDecision(BaseModel):
    """Structured betting decision."""

    primary_action: PokerAction = Field(description="Primary action to take")
    bet_size: int = Field(default=0, description="Bet/raise size if applicable")
    alternative_action: Optional[PokerAction] = Field(
        default=None, description="Alternative action if primary fails"
    )
    reasoning: str = Field(description="Detailed reasoning for the decision")
    aggression_level: str = Field(
        default="moderate",
        description="Level of aggression (passive, moderate, aggressive)",
    )
    expected_outcome: str = Field(description="Expected outcome of this action")


class OpponentModel(BaseModel):
    """Model of an opponent's playing style."""

    player_id: str = Field(description="Opponent's ID")
    aggression_factor: float = Field(
        default=0.5, description="How aggressive they are (0-1)"
    )
    tightness_factor: float = Field(
        default=0.5, description="How tight they play (0-1)"
    )
    bluff_frequency: float = Field(
        default=0.2, description="Estimated bluff frequency (0-1)"
    )
    fold_to_aggression: float = Field(
        default=0.5, description="Likelihood to fold to aggression (0-1)"
    )
    notes: List[str] = Field(default_factory=list, description="Observational notes")


class PokerHandHistory(BaseModel):
    """History of a completed poker hand."""

    hand_id: str = Field(description="Unique hand identifier")
    winner: str = Field(description="Winner of the hand")
    winning_hand: HandEvaluation = Field(description="Winning hand details")
    final_pot: int = Field(description="Final pot size")
    actions: List[Dict[str, Any]] = Field(
        default_factory=list, description="All actions taken during the hand"
    )
    showdown_cards: Dict[str, List[str]] = Field(
        default_factory=dict, description="Cards shown at showdown"
    )


class TableDynamics(BaseModel):
    """Analysis of table dynamics."""

    table_image: str = Field(
        description="Overall table image (tight, loose, aggressive, passive)"
    )
    stack_distribution: str = Field(
        description="Description of stack size distribution"
    )
    recent_action: str = Field(description="Summary of recent action/trends")
    player_types: Dict[str, str] = Field(
        default_factory=dict, description="Categorization of each player type"
    )
    opportunities: List[str] = Field(
        default_factory=list, description="Identified opportunities for exploitation"
    )
