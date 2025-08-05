from enum import Enum
from typing import Any

from pydantic import Field, model_validator

from haive.games.cards.card.components.actions import CardAction
from haive.games.cards.card.components.betting import WagerableGameState
from haive.games.cards.card.components.standard import StandardCard
from haive.games.cards.card.components.state import CardGameState
from haive.games.cards.standard.poker.scoring import PokerHandEvaluator, PokerHandRank


class PokerPhase(str, Enum):
    """Phases in a poker game."""

    DEAL = "deal"
    PRE_FLOP = "pre_flop"
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"
    SHOWDOWN = "showdown"


class PokerBettingRound(str, Enum):
    """Betting rounds in poker."""

    PRE_FLOP = "pre_flop"
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"


class PokerVariant(str, Enum):
    """Types of poker games."""

    TEXAS_HOLDEM = "texas_holdem"
    OMAHA = "omaha"
    SEVEN_CARD_STUD = "seven_card_stud"
    FIVE_CARD_DRAW = "five_card_draw"


class PokerGameState(CardGameState[StandardCard, CardAction], WagerableGameState):
    """State for poker games."""

    variant: PokerVariant = PokerVariant.TEXAS_HOLDEM
    community_cards: list[StandardCard] = Field(default_factory=list)
    phase: PokerPhase = PokerPhase.DEAL
    betting_round: PokerBettingRound | None = None
    active_players: list[str] = Field(default_factory=list)
    folded_players: list[str] = Field(default_factory=list)
    all_in_players: list[str] = Field(default_factory=list)
    dealer_position: int = 0
    small_blind_position: int | None = None
    big_blind_position: int | None = None
    small_blind: int = 1
    big_blind: int = 2
    current_bet: int = 0
    last_raiser: str | None = None
    hand_rankings: dict[str, PokerHandRank] = Field(default_factory=dict)

    @model_validator(mode="after")
    def setup_active_players(self) -> "PokerGameState":
        """Ensure active_players is populated."""
        if not self.active_players and self.players:
            self.active_players = self.players.copy()
        return self

    def start_game(self) -> None:
        """Start the poker game."""
        if self.game_status != "not_started":
            return
        self._setup_positions()
        self._post_blinds()
        self.deal_hole_cards()
        self.phase = PokerPhase.PRE_FLOP
        self.betting_round = PokerBettingRound.PRE_FLOP
        positions = self._get_position_order()
        if positions:
            self.current_player_id = self.players[positions[0]]
        super().start_game()

    def _setup_positions(self) -> None:
        """Set up dealer and blind positions."""
        num_players = len(self.players)
        if num_players == 2:
            self.small_blind_position = self.dealer_position
            self.big_blind_position = (self.dealer_position + 1) % num_players
        else:
            self.small_blind_position = (self.dealer_position + 1) % num_players
            self.big_blind_position = (self.dealer_position + 2) % num_players

    def _post_blinds(self) -> None:
        """Post small and big blinds."""
        if self.small_blind_position is not None:
            small_blind_player = self.players[self.small_blind_position]
            self.player_chips[small_blind_player] -= self.small_blind
            self.current_bets[small_blind_player] = self.small_blind
        if self.big_blind_position is not None:
            big_blind_player = self.players[self.big_blind_position]
            self.player_chips[big_blind_player] -= self.big_blind
            self.current_bets[big_blind_player] = self.big_blind
            self.current_bet = self.big_blind

    def _get_position_order(self) -> list[int]:
        """Get the order of positions for the current betting round."""
        num_players = len(self.players)
        if self.phase == PokerPhase.PRE_FLOP:
            if self.big_blind_position is not None:
                start_pos = (self.big_blind_position + 1) % num_players
            else:
                start_pos = (self.dealer_position + 1) % num_players
        else:
            start_pos = (self.dealer_position + 1) % num_players
        positions = [(start_pos + i) % num_players for i in range(num_players)]
        active_positions = []
        for pos in positions:
            player_id = self.players[pos]
            if (
                player_id not in self.folded_players
                and player_id not in self.all_in_players
            ):
                active_positions.append(pos)
        return active_positions

    def deal_hole_cards(self) -> None:
        """Deal hole cards to all players."""
        cards_per_player = 2
        if self.variant == PokerVariant.OMAHA:
            cards_per_player = 4
        elif self.variant == PokerVariant.SEVEN_CARD_STUD:
            cards_per_player = 3
        elif self.variant == PokerVariant.FIVE_CARD_DRAW:
            cards_per_player = 5
        positions = []
        for i in range(len(self.players)):
            pos = (self.small_blind_position + i) % len(self.players)
            positions.append(pos)
        for _ in range(cards_per_player):
            for pos in positions:
                player_id = self.players[pos]
                card = self.deck.draw()
                if card:
                    self.hands[player_id].add_card(card)

    def deal_community_cards(self, count: int = 1) -> list[StandardCard]:
        """Deal community cards."""
        cards = []
        for _ in range(count):
            card = self.deck.draw()
            if card:
                card.face_up = True
                self.community_cards.append(card)
                cards.append(card)
        return cards

    def advance_phase(self) -> None:
        """Advance to the next phase of the poker game."""
        self.collect_bets()
        self.current_bet = 0
        self.last_raiser = None
        phase_order = [
            PokerPhase.DEAL,
            PokerPhase.PRE_FLOP,
            PokerPhase.FLOP,
            PokerPhase.TURN,
            PokerPhase.RIVER,
            PokerPhase.SHOWDOWN,
        ]
        current_idx = phase_order.index(self.phase)
        if current_idx < len(phase_order) - 1:
            self.phase = phase_order[current_idx + 1]
            if self.phase == PokerPhase.FLOP:
                self.deal_community_cards(3)
                self.betting_round = PokerBettingRound.FLOP
            elif self.phase == PokerPhase.TURN:
                self.deal_community_cards(1)
                self.betting_round = PokerBettingRound.TURN
            elif self.phase == PokerPhase.RIVER:
                self.deal_community_cards(1)
                self.betting_round = PokerBettingRound.RIVER
            elif self.phase == PokerPhase.SHOWDOWN:
                self._evaluate_hands()
                self._distribute_winnings()
        positions = self._get_position_order()
        if positions and self.phase != PokerPhase.SHOWDOWN:
            self.current_player_id = self.players[positions[0]]

    def _evaluate_hands(self) -> None:
        """Evaluate all active hands to determine winner(s)."""
        self.hand_rankings = {}
        for player_id in self.active_players:
            if player_id in self.folded_players:
                continue
            all_cards = self.hands[player_id].cards + self.community_cards
            if self.variant == PokerVariant.TEXAS_HOLDEM:
                self.hand_rankings[player_id] = PokerHandEvaluator.evaluate(all_cards)
            elif self.variant == PokerVariant.OMAHA:
                pass
            else:
                self.hand_rankings[player_id] = PokerHandEvaluator.evaluate(all_cards)

    def _distribute_winnings(self) -> None:
        """Distribute pot to winners based on hand rankings."""
        if not self.hand_rankings:
            return
        best_rank = max(self.hand_rankings.values())
        winners = [
            player_id
            for player_id, rank in self.hand_rankings.items()
            if rank == best_rank
        ]
        self.distribute_pot(winners)
        self.game_status = "completed"
        if len(winners) == 1:
            self.winner_id = winners[0]

    def get_player_view(self, player_id: str) -> dict[str, Any]:
        """Get the game state from a specific player's perspective."""
        view = {
            "my_hand": (
                [card.dict() for card in self.hands[player_id].cards]
                if player_id in self.hands
                else []
            ),
            "community_cards": [card.dict() for card in self.community_cards],
            "pot": self.pot,
            "current_bet": self.current_bet,
            "current_bets": self.current_bets,
            "my_chips": self.player_chips.get(player_id, 0),
            "player_chips": self.player_chips,
            "active_players": self.active_players,
            "folded_players": self.folded_players,
            "all_in_players": self.all_in_players,
            "dealer": (
                self.players[self.dealer_position]
                if self.dealer_position < len(self.players)
                else None
            ),
            "current_player": self.current_player_id,
            "phase": self.phase,
            "hand_rankings": (
                {pid: str(rank) for pid, rank in self.hand_rankings.items()}
                if self.phase == PokerPhase.SHOWDOWN
                else {}
            ),
            "winner": self.winner_id,
        }
        return view
