"""Texas Hold'em game state management module.

This module provides a dedicated state manager for Texas Hold'em poker games,
offering static methods for state manipulation, including:
    - Creating and initializing game states
    - Advancing game phases
    - Applying player actions
    - Handling betting rounds
    - Managing pot and chip distribution
    - Tracking hand history

The state manager serves as a central interface for manipulating the game state
in a consistent manner, separating state manipulation logic from the game agent.

Example:
    >>> from haive.games.hold_em.state_manager import HoldemGameStateManager
    >>> from haive.games.hold_em.state import HoldemState, PlayerState
    >>>
    >>> # Create player states
    >>> players = [
    >>>     PlayerState(player_id="p1", name="Alice", chips=1000, position=0),
    >>>     PlayerState(player_id="p2", name="Bob", chips=1000, position=1),
    >>> ]
    >>>
    >>> # Initialize a new game state
    >>> state = HoldemGameStateManager.create_initial_state(
    >>>     players=players,
    >>>     small_blind=10,
    >>>     big_blind=20
    >>> )
    >>>
    >>> # Advance the game to the next phase
    >>> updated_state = HoldemGameStateManager.advance_phase(state)
"""

import random
import uuid
from typing import Dict, List, Optional, Tuple

from haive.games.hold_em.state import GamePhase, HoldemState, PlayerState, PlayerStatus
from haive.games.hold_em.utils import (
    create_standard_deck,
    evaluate_hand_simple,
    shuffle_deck,
)


class HoldemGameStateManager:
    """State manager for Texas Hold'em poker games.

    This class provides static methods for manipulating the game state,
    separating state logic from the game agent. It handles state transitions,
    player actions, and game flow management in a functional manner.

    All methods are static and take a state object as input, returning a new
    state object with the requested changes applied, following an immutable
    approach to state management.
    """

    @staticmethod
    def create_initial_state(
        players: List[PlayerState],
        small_blind: int = 10,
        big_blind: int = 20,
        starting_chips: int = 1000,
        game_id: Optional[str] = None,
    ) -> HoldemState:
        """Create an initial game state for a new poker game.

        Args:
            players: List of player states
            small_blind: Small blind amount
            big_blind: Big blind amount
            starting_chips: Starting chips for each player
            game_id: Optional game identifier (generated if not provided)

        Returns:
            A new HoldemState instance ready for the first hand
        """
        if not game_id:
            game_id = f"game_{uuid.uuid4().hex[:8]}"

        # Set initial positions
        for i, player in enumerate(players):
            player.position = i
            player.is_dealer = i == 0
            player.is_small_blind = (i == 1) if len(players) > 2 else (i == 0)
            player.is_big_blind = (i == 2) if len(players) > 2 else (i == 1)

            # Initialize player chips if not set
            if player.chips <= 0:
                player.chips = starting_chips

        # Create the game state
        state = HoldemState(
            game_id=game_id,
            players=players,
            max_players=len(players),
            small_blind=small_blind,
            big_blind=big_blind,
            deck=shuffle_deck(create_standard_deck()),
            current_phase=GamePhase.PREFLOP,
            hand_number=1,
        )

        return state

    @staticmethod
    def setup_new_hand(state: HoldemState) -> HoldemState:
        """Set up a new poker hand with shuffled deck and reset player states.

        Args:
            state: Current game state

        Returns:
            Updated state with new hand setup
        """
        # Create a copy of the state to modify
        updated_state = state.model_copy(deep=True)

        # Create and shuffle a new deck
        updated_state.deck = shuffle_deck(create_standard_deck())

        # Reset player states for the new hand
        for player in updated_state.players:
            player.hole_cards = []
            player.current_bet = 0
            player.total_bet = 0
            player.actions_this_hand = []
            if player.status != PlayerStatus.OUT:
                player.status = PlayerStatus.ACTIVE

        # Advance dealer position (rotate button)
        new_dealer_position = (updated_state.dealer_position + 1) % len(
            updated_state.players
        )

        # Update player positions
        HoldemGameStateManager._set_player_positions(updated_state, new_dealer_position)

        # Reset game state for new hand
        updated_state.community_cards = []
        updated_state.burned_cards = []
        updated_state.pot = 0
        updated_state.side_pots = []
        updated_state.current_bet = 0
        updated_state.min_raise = updated_state.big_blind
        updated_state.current_phase = GamePhase.PREFLOP
        updated_state.actions_this_round = []
        updated_state.betting_round_complete = False
        updated_state.winner = None
        updated_state.error_message = None
        updated_state.dealer_position = new_dealer_position

        return updated_state

    @staticmethod
    def post_blinds(state: HoldemState) -> HoldemState:
        """Post small and big blinds to start the betting.

        Args:
            state: Current game state

        Returns:
            Updated state with blinds posted
        """
        updated_state = state.model_copy(deep=True)

        # Find blind positions
        small_blind_player = None
        big_blind_player = None

        for player in updated_state.players:
            if player.is_small_blind:
                small_blind_player = player
            elif player.is_big_blind:
                big_blind_player = player

        if not small_blind_player or not big_blind_player:
            raise ValueError("Could not find blind players")

        # Post blinds
        small_blind_amount = min(updated_state.small_blind, small_blind_player.chips)
        big_blind_amount = min(updated_state.big_blind, big_blind_player.chips)

        small_blind_player.chips -= small_blind_amount
        small_blind_player.current_bet = small_blind_amount
        small_blind_player.total_bet = small_blind_amount

        big_blind_player.chips -= big_blind_amount
        big_blind_player.current_bet = big_blind_amount
        big_blind_player.total_bet = big_blind_amount

        # Set all-in if necessary
        if small_blind_player.chips == 0:
            small_blind_player.status = PlayerStatus.ALL_IN
        if big_blind_player.chips == 0:
            big_blind_player.status = PlayerStatus.ALL_IN

        # Update pot and current bet
        updated_state.pot = small_blind_amount + big_blind_amount
        updated_state.current_bet = big_blind_amount

        # Record actions
        actions = [
            {
                "player_id": small_blind_player.player_id,
                "action": "post_small_blind",
                "amount": small_blind_amount,
                "phase": "preflop",
            },
            {
                "player_id": big_blind_player.player_id,
                "action": "post_big_blind",
                "amount": big_blind_amount,
                "phase": "preflop",
            },
        ]
        updated_state.actions_this_round = actions

        return updated_state

    @staticmethod
    def deal_hole_cards(state: HoldemState) -> HoldemState:
        """Deal two hole cards to each active player.

        Args:
            state: Current game state

        Returns:
            Updated state with hole cards dealt
        """
        updated_state = state.model_copy(deep=True)
        deck = updated_state.deck.copy()

        # Deal 2 cards to each active player
        for player in updated_state.players:
            if player.status in [PlayerStatus.ACTIVE, PlayerStatus.ALL_IN]:
                if len(deck) >= 2:
                    player.hole_cards = [deck.pop(), deck.pop()]
                else:
                    raise ValueError(f"Not enough cards to deal to {player.name}")

        # Set first player to act (after big blind)
        big_blind_pos = next(
            (i for i, p in enumerate(updated_state.players) if p.is_big_blind), 0
        )
        first_to_act = (big_blind_pos + 1) % len(updated_state.players)

        # Find next active player
        attempts = 0
        while (
            attempts < len(updated_state.players)
            and updated_state.players[first_to_act].status != PlayerStatus.ACTIVE
        ):
            first_to_act = (first_to_act + 1) % len(updated_state.players)
            attempts += 1

        updated_state.deck = deck
        updated_state.current_player_index = first_to_act

        return updated_state

    @staticmethod
    def deal_community_cards(
        state: HoldemState, num_cards: int, phase: GamePhase
    ) -> HoldemState:
        """Deal community cards (flop, turn, or river).

        Args:
            state: Current game state
            num_cards: Number of cards to deal
            phase: New game phase

        Returns:
            Updated state with community cards dealt
        """
        updated_state = state.model_copy(deep=True)
        deck = updated_state.deck.copy()
        community_cards = updated_state.community_cards.copy()
        burned_cards = updated_state.burned_cards.copy()

        # Burn a card
        if deck:
            burned_cards.append(deck.pop())

        # Deal community cards
        for _ in range(num_cards):
            if deck:
                card = deck.pop()
                community_cards.append(card)
            else:
                raise ValueError("Not enough cards in deck")

        # Reset betting for new round
        for player in updated_state.players:
            player.current_bet = 0

        # First to act is first active player after dealer
        dealer_pos = updated_state.dealer_position
        first_to_act = (dealer_pos + 1) % len(updated_state.players)

        # Find next active player
        attempts = 0
        while (
            attempts < len(updated_state.players)
            and updated_state.players[first_to_act].status != PlayerStatus.ACTIVE
        ):
            first_to_act = (first_to_act + 1) % len(updated_state.players)
            attempts += 1

        # Update state
        updated_state.deck = deck
        updated_state.community_cards = community_cards
        updated_state.burned_cards = burned_cards
        updated_state.current_phase = phase
        updated_state.current_bet = 0
        updated_state.current_player_index = first_to_act
        updated_state.actions_this_round = []
        updated_state.betting_round_complete = False

        return updated_state

    @staticmethod
    def apply_player_action(
        state: HoldemState, player_index: int, action: str, amount: int = 0
    ) -> HoldemState:
        """Apply a player's action to the game state.

        Args:
            state: Current game state
            player_index: Index of the player taking the action
            action: Action to take (fold, check, call, bet, raise, all_in)
            amount: Amount for bet/raise (if applicable)

        Returns:
            Updated state with the action applied
        """
        updated_state = state.model_copy(deep=True)
        player = updated_state.players[player_index]

        # Record the action
        action_record = {
            "player_id": player.player_id,
            "action": action,
            "amount": amount,
            "phase": updated_state.current_phase.value,
        }

        # Apply the action logic
        if action == "fold":
            player.status = PlayerStatus.FOLDED

        elif action == "check":
            if updated_state.current_bet > player.current_bet:
                # Can't check if there's a bet to call
                call_amount = updated_state.current_bet - player.current_bet
                if call_amount <= player.chips:
                    # Force call
                    action = "call"
                    amount = call_amount
                    action_record["action"] = "call"
                    action_record["amount"] = amount
                    HoldemGameStateManager._apply_call(
                        player, updated_state, call_amount
                    )
                else:
                    # Force fold
                    player.status = PlayerStatus.FOLDED
                    action_record["action"] = "fold"
                    action_record["amount"] = 0

        elif action == "call":
            call_amount = min(
                amount, updated_state.current_bet - player.current_bet, player.chips
            )
            HoldemGameStateManager._apply_call(player, updated_state, call_amount)
            action_record["amount"] = call_amount
            if player.chips == 0:
                player.status = PlayerStatus.ALL_IN

        elif action == "bet":
            if updated_state.current_bet > 0:
                # Already a bet, this should be a raise
                action = "raise"
                action_record["action"] = "raise"

            bet_amount = min(amount, player.chips)
            HoldemGameStateManager._apply_bet_raise(player, updated_state, bet_amount)
            action_record["amount"] = bet_amount

            if player.chips == 0:
                player.status = PlayerStatus.ALL_IN

        elif action == "raise":
            # Calculate total amount needed
            call_amount = updated_state.current_bet - player.current_bet
            raise_amount = max(0, amount - call_amount)
            total_amount = call_amount + raise_amount

            if total_amount > player.chips:
                total_amount = player.chips
                action = "all_in"
                action_record["action"] = "all_in"

            HoldemGameStateManager._apply_bet_raise(player, updated_state, total_amount)
            action_record["amount"] = total_amount

            if player.chips == 0:
                player.status = PlayerStatus.ALL_IN

        elif action == "all_in":
            all_in_amount = player.chips
            HoldemGameStateManager._apply_bet_raise(
                player, updated_state, all_in_amount
            )
            player.status = PlayerStatus.ALL_IN
            action_record["amount"] = all_in_amount

        else:
            # Unknown action, treat as fold
            player.status = PlayerStatus.FOLDED
            action_record["action"] = "fold"
            action_record["amount"] = 0

        # Add action to player's hand history
        player.actions_this_hand.append(action_record)

        # Record action in game state
        if not updated_state.actions_this_round:
            updated_state.actions_this_round = [action_record]
        else:
            updated_state.actions_this_round.append(action_record)

        updated_state.last_action = action_record

        # Advance to next player or complete betting
        if updated_state.is_betting_complete():
            updated_state.betting_round_complete = True
        else:
            next_player_index = HoldemGameStateManager._get_next_player_index(
                updated_state
            )
            if next_player_index is not None:
                updated_state.current_player_index = next_player_index

        return updated_state

    @staticmethod
    def evaluate_showdown(state: HoldemState) -> HoldemState:
        """Evaluate player hands at showdown and determine winner.

        Args:
            state: Current game state

        Returns:
            Updated state with winner determined
        """
        updated_state = state.model_copy(deep=True)

        players_in_showdown = [
            p
            for p in updated_state.players_in_hand
            if p.status in [PlayerStatus.ACTIVE, PlayerStatus.ALL_IN]
        ]

        if len(players_in_showdown) <= 1:
            # Only one player left, they win automatically
            winner = players_in_showdown[0] if players_in_showdown else None
            winner_id = winner.player_id if winner else None
            updated_state.winner = winner_id
            return updated_state

        # Evaluate hands and find winner
        hand_rankings = []
        for player in players_in_showdown:
            hand_strength = evaluate_hand_simple(
                player.hole_cards, updated_state.community_cards
            )
            hand_rankings.append((player, hand_strength))

        # Sort by hand strength (higher is better)
        hand_rankings.sort(key=lambda x: x[1], reverse=True)
        winner = hand_rankings[0][0]

        updated_state.winner = winner.player_id
        return updated_state

    @staticmethod
    def award_pot(state: HoldemState) -> HoldemState:
        """Award the pot to the winner and record hand history.

        Args:
            state: Current game state

        Returns:
            Updated state with pot awarded and hand recorded
        """
        updated_state = state.model_copy(deep=True)

        winner_id = updated_state.winner
        if not winner_id:
            # Find last remaining player
            players_in_hand = updated_state.players_in_hand
            if players_in_hand:
                winner_id = players_in_hand[0].player_id

        if winner_id:
            winner = updated_state.get_player_by_id(winner_id)
            if winner:
                winner.chips += updated_state.total_pot

        # Record hand in history
        hand_record = {
            "hand_number": updated_state.hand_number,
            "winner": winner_id,
            "pot_size": updated_state.total_pot,
            "community_cards": updated_state.community_cards,
            "actions": updated_state.actions_this_round,
        }

        # Add to hand history
        if not updated_state.hand_history:
            updated_state.hand_history = [hand_record]
        else:
            updated_state.hand_history.append(hand_record)

        updated_state.hand_number += 1

        return updated_state

    @staticmethod
    def check_game_end(state: HoldemState) -> Tuple[HoldemState, bool]:
        """Check if the game should end.

        Args:
            state: Current game state

        Returns:
            Tuple of (updated state, game_over flag)
        """
        updated_state = state.model_copy(deep=True)

        # Check win conditions
        players_with_chips = [p for p in updated_state.players if p.chips > 0]

        if len(players_with_chips) <= 1:
            # Only one player with chips, game over
            updated_state.game_over = True
            return updated_state, True

        if updated_state.hand_number > updated_state.max_players * 50:
            # Maximum hands reached
            updated_state.game_over = True
            return updated_state, True

        # Continue to next hand
        return updated_state, False

    @staticmethod
    def advance_phase(state: HoldemState) -> HoldemState:
        """Advance the game to the next phase based on current phase.

        Args:
            state: Current game state

        Returns:
            Updated state in the next game phase
        """
        # Check if only one player remains
        players_in_hand = [
            p for p in state.players_in_hand if p.status != PlayerStatus.FOLDED
        ]
        if len(players_in_hand) <= 1:
            # Skip to showdown/award pot if only one player remains
            updated_state = state.model_copy(deep=True)
            updated_state.current_phase = GamePhase.SHOWDOWN
            return updated_state

        # Advance based on current phase
        if state.current_phase == GamePhase.PREFLOP:
            return HoldemGameStateManager.deal_community_cards(state, 3, GamePhase.FLOP)
        elif state.current_phase == GamePhase.FLOP:
            return HoldemGameStateManager.deal_community_cards(state, 1, GamePhase.TURN)
        elif state.current_phase == GamePhase.TURN:
            return HoldemGameStateManager.deal_community_cards(
                state, 1, GamePhase.RIVER
            )
        elif state.current_phase == GamePhase.RIVER:
            updated_state = state.model_copy(deep=True)
            updated_state.current_phase = GamePhase.SHOWDOWN
            return updated_state
        else:
            # Already at showdown or game over, no advancement
            return state

    # Helper methods

    @staticmethod
    def _set_player_positions(state: HoldemState, dealer_pos: int) -> None:
        """Set player positions for the hand."""
        num_players = len(state.players)

        # Reset position flags
        for player in state.players:
            player.is_dealer = False
            player.is_small_blind = False
            player.is_big_blind = False

        # Set dealer
        state.players[dealer_pos].is_dealer = True

        # Set blinds
        if num_players == 2:
            # Heads up: dealer is small blind
            state.players[dealer_pos].is_small_blind = True
            state.players[(dealer_pos + 1) % num_players].is_big_blind = True
        else:
            # Normal: small blind after dealer, big blind after small
            state.players[(dealer_pos + 1) % num_players].is_small_blind = True
            state.players[(dealer_pos + 2) % num_players].is_big_blind = True

    @staticmethod
    def _apply_call(player: PlayerState, state: HoldemState, call_amount: int) -> None:
        """Apply a call action."""
        player.chips -= call_amount
        player.current_bet += call_amount
        player.total_bet += call_amount
        state.pot += call_amount

    @staticmethod
    def _apply_bet_raise(
        player: PlayerState, state: HoldemState, bet_amount: int
    ) -> None:
        """Apply a bet or raise action."""
        player.chips -= bet_amount
        player.current_bet += bet_amount
        player.total_bet += bet_amount
        state.pot += bet_amount
        state.current_bet = player.current_bet
        state.min_raise = bet_amount

    @staticmethod
    def _get_next_player_index(state: HoldemState) -> Optional[int]:
        """Get the index of the next player to act."""
        start_index = state.current_player_index

        for i in range(1, len(state.players) + 1):
            next_index = (start_index + i) % len(state.players)
            next_player = state.players[next_index]

            if next_player.status == PlayerStatus.ACTIVE:
                return next_index

        return None
