"""Fixed Texas Hold'em game state models.

Key fixes:
1. Added Annotated type for current_player_index to handle concurrent updates
2. Fixed reducer setup for fields that might be updated concurrently
3. Added proper field annotations for LangGraph compatibility

"""

import operator
from enum import Enum
from typing import Annotated, Any

from pydantic import BaseModel, Field, computed_field


class PokerAction(str, Enum):
    """Possible poker actions."""

    FOLD = "fold"
    CHECK = "check"
    CALL = "call"
    BET = "bet"
    RAISE = "raise"
    ALL_IN = "all_in"


class GamePhase(str, Enum):
    """Game phases in Texas Hold'em."""

    PREFLOP = "preflop"
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"
    SHOWDOWN = "showdown"
    GAME_OVER = "game_over"


class PlayerStatus(str, Enum):
    """Player status in the game."""

    ACTIVE = "active"
    FOLDED = "folded"
    ALL_IN = "all_in"
    OUT = "out"  # No more chips


def last_value_reducer(a: Any, b: Any) -> Any:
    """Reducer that takes the last value - for fields that should be overwritten."""
    return b


class PlayerState(BaseModel):
    """State for an individual player."""

    player_id: str = Field(description="Unique player identifier")
    name: str = Field(description="Player name")
    chips: int = Field(description="Current chip count")
    hole_cards: list[str] = Field(
        default_factory=list, description="Player's hole cards"
    )
    status: PlayerStatus = Field(
        default=PlayerStatus.ACTIVE, description="Player status"
    )
    current_bet: int = Field(default=0, description="Current bet this round")
    total_bet: int = Field(default=0, description="Total bet this hand")
    position: int = Field(description="Position at table (0-based)")
    is_dealer: bool = Field(default=False, description="Is dealer this hand")
    is_small_blind: bool = Field(default=False, description="Is small blind this hand")
    is_big_blind: bool = Field(default=False, description="Is big blind this hand")

    # Action history for this hand - using Annotated for multiple updates
    actions_this_hand: Annotated[list[dict[str, Any]], operator.add] = Field(
        default_factory=list, description="Actions taken this hand"
    )


class HoldemState(BaseModel):
    """State for the Texas Hold'em game.

    This class represents the complete game state including:
        - Players and their states
        - Community cards
        - Betting rounds
        - Pot information
        - Game phase tracking

    """

    # Game setup
    game_id: str = Field(description="Unique game identifier")
    players: list[PlayerState] = Field(description="All players in the game")
    max_players: int = Field(default=6, description="Maximum players at table")

    # Current hand state
    dealer_position: int = Field(default=0, description="Current dealer position")
    small_blind: int = Field(default=10, description="Small blind amount")
    big_blind: int = Field(default=20, description="Big blind amount")

    # Cards
    community_cards: list[str] = Field(
        default_factory=list, description="Community cards"
    )
    deck: list[str] = Field(default_factory=list, description="Remaining deck")
    burned_cards: list[str] = Field(default_factory=list, description="Burned cards")

    # Game flow - FIXED: Use Annotated with reducer for concurrent updates
    current_phase: GamePhase = Field(
        default=GamePhase.PREFLOP, description="Current game phase"
    )
    current_player_index: Annotated[int, last_value_reducer] = Field(
        default=0, description="Index of current player to act"
    )
    betting_round_complete: Annotated[bool, last_value_reducer] = Field(
        default=False, description="Is current betting round done"
    )

    # Betting state
    pot: int = Field(default=0, description="Main pot amount")
    side_pots: list[dict[str, Any]] = Field(
        default_factory=list, description="Side pots"
    )
    current_bet: Annotated[int, last_value_reducer] = Field(
        default=0, description="Current bet to call"
    )
    min_raise: int = Field(default=0, description="Minimum raise amount")

    # Action tracking - using Annotated for multiple updates
    actions_this_round: Annotated[list[dict[str, Any]], operator.add] = Field(
        default_factory=list, description="Actions taken this betting round"
    )
    last_action: Annotated[dict[str, Any] | None, last_value_reducer] = Field(
        default=None, description="Last action taken"
    )

    # Hand history - using Annotated for multiple updates
    hand_number: int = Field(default=1, description="Current hand number")
    hand_history: Annotated[list[dict[str, Any]], operator.add] = Field(
        default_factory=list, description="History of completed hands"
    )

    # Game status
    winner: str | None = Field(default=None, description="Winner of current hand")
    game_over: bool = Field(default=False, description="Is game finished")
    error_message: str | None = Field(default=None, description="Error message if any")

    @computed_field
    @property
    def active_players(self) -> list[PlayerState]:
        """Get list of active players."""
        return [p for p in self.players if p.status == PlayerStatus.ACTIVE]

    @computed_field
    @property
    def players_in_hand(self) -> list[PlayerState]:
        """Get players still in the current hand (not folded)."""
        return [
            p
            for p in self.players
            if p.status in [PlayerStatus.ACTIVE, PlayerStatus.ALL_IN]
        ]

    @computed_field
    @property
    def total_pot(self) -> int:
        """Calculate total pot including side pots."""
        side_pot_total = sum(pot["amount"] for pot in self.side_pots)
        return self.pot + side_pot_total

    @computed_field
    @property
    def players_to_act(self) -> list[PlayerState]:
        """Get players who still need to act this round."""
        players_in_hand = self.players_in_hand
        if not players_in_hand:
            return []

        # Players who can still act (not all-in and not folded)
        return [p for p in players_in_hand if p.status == PlayerStatus.ACTIVE]

    @computed_field
    @property
    def current_player(self) -> PlayerState | None:
        """Get the current player to act."""
        if self.current_player_index >= len(self.players):
            return None

        player = self.players[self.current_player_index]
        # Only return if they can actually act
        if player.status == PlayerStatus.ACTIVE:
            return player
        return None

    def get_player_by_id(self, player_id: str) -> PlayerState | None:
        """Get player by ID."""
        return next((p for p in self.players if p.player_id == player_id), None)

    def get_player_by_index(self, index: int) -> PlayerState | None:
        """Get player by index."""
        if 0 <= index < len(self.players):
            return self.players[index]
        return None

    def is_betting_complete(self) -> bool:
        """Check if betting round is complete."""
        players_to_act = self.players_to_act

        # No one left to act
        if len(players_to_act) <= 1:
            return True

        # Everyone has matched the current bet
        current_bet = self.current_bet
        for player in players_to_act:
            if player.current_bet < current_bet:
                return False

        return True

    def advance_to_next_player(self) -> int | None:
        """Advance to the next player who can act."""
        players_to_act = self.players_to_act
        if not players_to_act:
            return None

        # Find next active player
        start_index = self.current_player_index
        for i in range(len(self.players)):
            next_index = (start_index + i + 1) % len(self.players)
            next_player = self.players[next_index]
            if next_player.status == PlayerStatus.ACTIVE:
                return next_index

        # No active players found
        return None

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True


class PlayerAction(BaseModel):
    """Represents a player action."""

    player_id: str = Field(description="Player making the action")
    action: PokerAction = Field(description="Type of action")
    amount: int = Field(default=0, description="Amount for bet/raise")
    timestamp: str | None = Field(default=None, description="When action was taken")
    phase: GamePhase = Field(description="Game phase when action was taken")


class PlayerDecision(BaseModel):
    """Model for player decision-making."""

    action: PokerAction = Field(description="Chosen action")
    amount: int = Field(default=0, description="Amount for bet/raise")
    reasoning: str = Field(description="Reasoning for the decision")
    confidence: float = Field(default=0.5, description="Confidence in decision (0-1)")
    hand_strength_estimate: str | None = Field(
        default=None, description="Estimated hand strength"
    )
