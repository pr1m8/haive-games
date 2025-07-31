# haive/packages/haive-games/src/haive/games/card/poker/actions.py

from enum import Enum

from pydantic import model_validator

from haive.games.cards.card.components.actions import ActionResult, CardAction
from haive.games.cards.card.components.standard import StandardCard
from haive.games.cards.standard.poker.state import PokerGameState


class PokerActionType(str, Enum):
    """Types of poker actions."""

    CHECK = "check"
    CALL = "call"
    BET = "bet"
    RAISE = "raise"
    FOLD = "fold"
    ALL_IN = "all_in"


class PokerAction(CardAction[StandardCard, PokerGameState]):
    """Base class for poker actions."""

    action_type: str = "poker_action"
    poker_action_type: PokerActionType

    def can_execute(self, state: PokerGameState) -> bool:
        """Check if this action can be executed."""
        # Basic checks
        if state.game_status != "in_progress":
            return False

        if self.player_id != state.current_player_id:
            return False

        if self.player_id in state.folded_players:
            return False

        return self.player_id not in state.all_in_players


class CheckAction(PokerAction):
    """Action to check (pass without betting)."""

    poker_action_type: PokerActionType = PokerActionType.CHECK

    def can_execute(self, state: PokerGameState) -> bool:
        """Check if player can check."""
        if not super().can_execute(state):
            return False

        # Can only check if no one has bet yet or player has matched the
        # current bet
        current_player_bet = state.current_bets.get(self.player_id, 0)
        return state.current_bet in (0, current_player_bet)

    def execute(self, state: PokerGameState) -> ActionResult:
        """Execute check action."""
        if not self.can_execute(state):
            return ActionResult(
                success=False,
                message="Cannot check: either not your turn or there is an existing bet",
            )

        # Check if this was the last player in the round
        positions = state._get_position_order()
        current_pos = state.players.index(self.player_id)
        current_idx = positions.index(current_pos) if current_pos in positions else -1

        # Check if all players have acted
        if current_idx == len(positions) - 1 or state.last_raiser == self.player_id:
            # End of betting round, move to next phase
            state.advance_phase()
        else:
            # Move to next player
            next_pos = positions[current_idx + 1]
            state.current_player_id = state.players[next_pos]

        return ActionResult(
            success=True,
            message=f"Player {self.player_id} checks",
            state_updates={
                "current_player_id": state.current_player_id,
                "phase": state.phase,
            },
        )


class CallAction(PokerAction):
    """Action to call a bet."""

    poker_action_type: PokerActionType = PokerActionType.CALL

    def can_execute(self, state: PokerGameState) -> bool:
        """Check if player can call."""
        if not super().can_execute(state):
            return False

        # Can only call if there is a bet to call
        return state.current_bet > 0

    def execute(self, state: PokerGameState) -> ActionResult:
        """Execute call action."""
        if not self.can_execute(state):
            return ActionResult(
                success=False,
                message="Cannot call: either not your turn or no bet to call",
            )

        # Calculate call amount
        current_player_bet = state.current_bets.get(self.player_id, 0)
        call_amount = state.current_bet - current_player_bet
        player_chips = state.player_chips.get(self.player_id, 0)

        # Check if player has enough chips
        if player_chips < call_amount:
            # Player has to go all-in
            call_amount = player_chips
            state.all_in_players.append(self.player_id)

        # Place the call
        state.player_chips[self.player_id] -= call_amount
        state.current_bets[self.player_id] = current_player_bet + call_amount

        # Check if this was the last player in the round
        positions = state._get_position_order()
        current_pos = state.players.index(self.player_id)
        current_idx = positions.index(current_pos) if current_pos in positions else -1

        # Check if all players have acted
        if current_idx == len(positions) - 1 or state.last_raiser == self.player_id:
            # End of betting round, move to next phase
            state.advance_phase()
        else:
            # Move to next player
            next_pos = positions[current_idx + 1]
            state.current_player_id = state.players[next_pos]

        return ActionResult(
            success=True,
            message=f"Player {self.player_id} calls {call_amount}",
            state_updates={
                "player_chips": state.player_chips,
                "current_bets": state.current_bets,
                "current_player_id": state.current_player_id,
                "all_in_players": state.all_in_players,
                "phase": state.phase,
            },
        )


class BetAction(PokerAction):
    """Action to place a new bet."""

    poker_action_type: PokerActionType = PokerActionType.BET
    amount: int

    @model_validator(mode="after")
    @classmethod
    def validate_bet(cls) -> "BetAction":
        """Validate bet amount."""
        if self.amount <= 0:
            raise ValueError("Bet amount must be greater than 0")
        return self

    def can_execute(self, state: PokerGameState) -> bool:
        """Check if player can bet."""
        if not super().can_execute(state):
            return False

        # Can only bet if no one has bet yet
        if state.current_bet > 0:
            return False

        # Check if player has enough chips
        return state.player_chips.get(self.player_id, 0) >= self.amount

    def execute(self, state: PokerGameState) -> ActionResult:
        """Execute bet action."""
        if not self.can_execute(state):
            return ActionResult(
                success=False,
                message="Cannot bet: either not your turn, there is an existing bet, or insufficient chips",
            )

        # Place the bet
        state.player_chips[self.player_id] -= self.amount
        state.current_bets[self.player_id] = self.amount
        state.current_bet = self.amount
        state.last_raiser = self.player_id

        # Check if the amount is all-in
        if state.player_chips[self.player_id] == 0:
            state.all_in_players.append(self.player_id)

        # Move to next player
        positions = state._get_position_order()
        current_pos = state.players.index(self.player_id)
        current_idx = positions.index(current_pos) if current_pos in positions else -1

        if current_idx < len(positions) - 1:
            next_pos = positions[current_idx + 1]
            state.current_player_id = state.players[next_pos]
        else:
            # If last player bets, loop back to first active player
            state.current_player_id = state.players[positions[0]]

        return ActionResult(
            success=True,
            message=f"Player {self.player_id} bets {self.amount}",
            state_updates={
                "player_chips": state.player_chips,
                "current_bets": state.current_bets,
                "current_bet": state.current_bet,
                "last_raiser": state.last_raiser,
                "current_player_id": state.current_player_id,
                "all_in_players": state.all_in_players,
            },
        )


class RaiseAction(PokerAction):
    """Action to raise an existing bet."""

    poker_action_type: PokerActionType = PokerActionType.RAISE
    amount: int  # Total amount, including the call amount

    @model_validator(mode="after")
    @classmethod
    def validate_raise(cls) -> "RaiseAction":
        """Validate raise amount."""
        if self.amount <= 0:
            raise ValueError("Raise amount must be greater than 0")
        return self

    def can_execute(self, state: PokerGameState) -> bool:
        """Check if player can raise."""
        if not super().can_execute(state):
            return False

        # Can only raise if there is a bet to raise
        if state.current_bet <= 0:
            return False

        # Raise must be at least double the current bet
        current_player_bet = state.current_bets.get(self.player_id, 0)
        min_raise = state.current_bet * 2 - current_player_bet

        # Check if player has enough chips
        return self.amount >= min_raise and state.player_chips.get(
            self.player_id, 0
        ) >= (self.amount - current_player_bet)

    def execute(self, state: PokerGameState) -> ActionResult:
        """Execute raise action."""
        if not self.can_execute(state):
            return ActionResult(
                success=False,
                message="Cannot raise: either not your turn, no bet to raise, raise too small, or insufficient chips",
            )

        # Calculate actual amount to add
        current_player_bet = state.current_bets.get(self.player_id, 0)
        to_add = self.amount - current_player_bet

        # Place the raise
        state.player_chips[self.player_id] -= to_add
        state.current_bets[self.player_id] = self.amount
        state.current_bet = self.amount
        state.last_raiser = self.player_id

        # Check if the amount is all-in
        if state.player_chips[self.player_id] == 0:
            state.all_in_players.append(self.player_id)

        # Move to next player
        positions = state._get_position_order()
        current_pos = state.players.index(self.player_id)
        current_idx = positions.index(current_pos) if current_pos in positions else -1

        if current_idx < len(positions) - 1:
            next_pos = positions[current_idx + 1]
            state.current_player_id = state.players[next_pos]
        else:
            # If last player raises, loop back to first active player
            state.current_player_id = state.players[positions[0]]

        return ActionResult(
            success=True,
            message=f"Player {self.player_id} raises to {self.amount}",
            state_updates={
                "player_chips": state.player_chips,
                "current_bets": state.current_bets,
                "current_bet": state.current_bet,
                "last_raiser": state.last_raiser,
                "current_player_id": state.current_player_id,
                "all_in_players": state.all_in_players,
            },
        )


class FoldAction(PokerAction):
    """Action to fold (forfeit hand)."""

    poker_action_type: PokerActionType = PokerActionType.FOLD

    def execute(self, state: PokerGameState) -> ActionResult:
        """Execute fold action."""
        if not self.can_execute(state):
            return ActionResult(success=False, message="Cannot fold: not your turn")

        # Add player to folded list
        state.folded_players.append(self.player_id)

        # Remove from active players
        if self.player_id in state.active_players:
            state.active_players.remove(self.player_id)

        # Check if only one active player remains
        if len(state.active_players) == 1:
            # Game is over, remaining player wins
            state.winner_id = state.active_players[0]
            state.distribute_pot([state.winner_id])
            state.game_status = "completed"
            return ActionResult(
                success=True,
                message=f"Player {self.player_id} folds, {state.winner_id} wins",
                state_updates={
                    "folded_players": state.folded_players,
                    "active_players": state.active_players,
                    "winner_id": state.winner_id,
                    "game_status": state.game_status,
                    "player_chips": state.player_chips,
                },
            )

        # Move to next player
        positions = state._get_position_order()
        current_pos = state.players.index(self.player_id)
        current_idx = positions.index(current_pos) if current_pos in positions else -1

        # Check if all remaining players have acted
        if current_idx == len(positions) - 1 or state.last_raiser == self.player_id:
            # End of betting round, move to next phase
            state.advance_phase()
        else:
            # Move to next player
            next_pos = positions[current_idx + 1]
            state.current_player_id = state.players[next_pos]

        return ActionResult(
            success=True,
            message=f"Player {self.player_id} folds",
            state_updates={
                "folded_players": state.folded_players,
                "active_players": state.active_players,
                "current_player_id": state.current_player_id,
                "phase": state.phase,
            },
        )


class AllInAction(PokerAction):
    """Action to go all-in."""

    poker_action_type: PokerActionType = PokerActionType.ALL_IN

    def execute(self, state: PokerGameState) -> ActionResult:
        """Execute all-in action."""
        if not self.can_execute(state):
            return ActionResult(
                success=False, message="Cannot go all-in: not your turn"
            )

        # Get current chips and bet
        player_chips = state.player_chips.get(self.player_id, 0)
        current_player_bet = state.current_bets.get(self.player_id, 0)

        # Place all-in bet
        total_bet = current_player_bet + player_chips
        state.player_chips[self.player_id] = 0
        state.current_bets[self.player_id] = total_bet

        # Add to all-in players
        state.all_in_players.append(self.player_id)

        # Update current bet if this is a raise
        if total_bet > state.current_bet:
            state.current_bet = total_bet
            state.last_raiser = self.player_id

        # Move to next player
        positions = state._get_position_order()
        current_pos = state.players.index(self.player_id)
        current_idx = positions.index(current_pos) if current_pos in positions else -1

        # Check if all remaining players have acted
        if current_idx == len(positions) - 1 or state.last_raiser == self.player_id:
            # End of betting round, move to next phase
            state.advance_phase()
        else:
            # Move to next player
            next_pos = positions[current_idx + 1]
            state.current_player_id = state.players[next_pos]

        return ActionResult(
            success=True,
            message=f"Player {self.player_id} goes all-in with {player_chips}",
            state_updates={
                "player_chips": state.player_chips,
                "current_bets": state.current_bets,
                "current_bet": state.current_bet,
                "last_raiser": state.last_raiser,
                "current_player_id": state.current_player_id,
                "all_in_players": state.all_in_players,
                "phase": state.phase,
            },
        )
