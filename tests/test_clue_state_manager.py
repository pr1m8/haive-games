"""Comprehensive tests for Clue game state manager.

This module tests the ClueStateManager class and its methods
for managing game state transitions and game logic.
"""

import pytest

from haive.games.clue.models import (
    ClueGuess,
    ClueSolution,
    ValidRoom,
    ValidSuspect,
    ValidWeapon,
)
from haive.games.clue.state import ClueState
from haive.games.clue.state_manager import ClueStateManager


class TestClueStateManagerInitialization:
    """Test ClueStateManager initialization methods."""

    def test_initialize_default_game(self):
        """Test initializing a default game."""
        state = ClueStateManager.initialize()

        assert isinstance(state, ClueState)
        assert isinstance(state.solution, ClueSolution)
        assert state.current_player == "player1"
        assert state.max_turns == 20
        assert state.game_status == "ongoing"
        assert len(state.player1_cards) > 0
        assert len(state.player2_cards) > 0

    def test_initialize_with_custom_solution(self):
        """Test initializing with a specific solution."""
        custom_solution = ClueSolution(
            suspect=ValidSuspect.PROFESSOR_PLUM,
            weapon=ValidWeapon.LEAD_PIPE,
            room=ValidRoom.CONSERVATORY,
        )

        state = ClueStateManager.initialize(solution=custom_solution)

        assert state.solution == custom_solution
        assert state.solution.suspect == ValidSuspect.PROFESSOR_PLUM
        assert state.solution.weapon == ValidWeapon.LEAD_PIPE
        assert state.solution.room == ValidRoom.CONSERVATORY

    def test_initialize_with_custom_parameters(self):
        """Test initializing with various custom parameters."""
        state = ClueStateManager.initialize(
            first_player="player2",
            max_turns=30,
        )

        assert state.current_player == "player2"
        assert state.max_turns == 30

    def test_initialize_returns_proper_state_type(self):
        """Test that initialize returns ClueState instance."""
        state = ClueStateManager.initialize()
        assert isinstance(state, ClueState)
        assert hasattr(state, "solution")
        assert hasattr(state, "guesses")
        assert hasattr(state, "responses")


class TestClueStateManagerLegalMoves:
    """Test legal move generation."""

    def test_get_legal_moves_returns_empty_list(self):
        """Test get_legal_moves returns empty list (as implemented)."""
        state = ClueStateManager.initialize()
        moves = ClueStateManager.get_legal_moves(state)

        assert isinstance(moves, list)
        assert len(moves) == 0

    def test_get_legal_moves_with_various_states(self):
        """Test get_legal_moves with different game states."""
        # Ongoing game
        state = ClueStateManager.initialize()
        moves = ClueStateManager.get_legal_moves(state)
        assert moves == []

        # Game over
        state.game_status = "player1_win"
        moves = ClueStateManager.get_legal_moves(state)
        assert moves == []


class TestClueStateManagerApplyMove:
    """Test applying moves to game state."""

    def test_apply_move_basic(self):
        """Test applying a basic move."""
        state = ClueStateManager.initialize()
        initial_guess_count = len(state.guesses)

        # Create a guess
        guess = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )

        # Apply the move
        new_state = ClueStateManager.apply_move(state, guess)

        # Verify state changes
        assert len(new_state.guesses) == initial_guess_count + 1
        assert new_state.guesses[-1] == guess
        assert new_state != state  # Should be a new state object

    def test_apply_move_switches_players(self):
        """Test that applying a move switches players."""
        state = ClueStateManager.initialize()
        state.current_player = "player1"

        # Non-winning guess
        guess = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.KITCHEN,
        )

        # Ensure it's not the solution
        while (
            guess.suspect == state.solution.suspect
            and guess.weapon == state.solution.weapon
            and guess.room == state.solution.room
        ):
            guess = ClueGuess(
                suspect=ValidSuspect.MRS_WHITE,
                weapon=ValidWeapon.WRENCH,
                room=ValidRoom.HALL,
            )

        new_state = ClueStateManager.apply_move(state, guess)

        # Player should switch
        assert new_state.current_player == "player2"

    def test_apply_winning_move(self):
        """Test applying a winning move."""
        # Create state with known solution
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        state = ClueStateManager.initialize(solution=solution)

        # Create winning guess
        winning_guess = ClueGuess(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )

        # Set player attribute on guess for win condition
        winning_guess.player = "player1"

        new_state = ClueStateManager.apply_move(state, winning_guess)

        # Game should be won
        assert new_state.game_status == "player1_win"
        assert new_state.winner == "player1"

    def test_apply_move_at_max_turns(self):
        """Test applying move when max turns is reached."""
        state = ClueStateManager.initialize(max_turns=2)

        # Add first guess
        guess1 = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )
        state = ClueStateManager.apply_move(state, guess1)

        # Add second guess (reaching max)
        guess2 = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.KITCHEN,
        )
        new_state = ClueStateManager.apply_move(state, guess2)

        # Game should end with solution suspect as winner
        assert len(new_state.guesses) == 2
        assert new_state.game_status == f"{new_state.solution.suspect}_win"
        assert new_state.winner == new_state.solution.suspect

    def test_apply_move_beyond_max_turns_raises_error(self):
        """Test that applying move beyond max turns raises error."""
        state = ClueStateManager.initialize(max_turns=1)

        # Add first guess
        guess1 = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )
        state = ClueStateManager.apply_move(state, guess1)

        # Try to add another guess beyond max
        guess2 = ClueGuess(
            suspect=ValidSuspect.MR_GREEN,
            weapon=ValidWeapon.KNIFE,
            room=ValidRoom.KITCHEN,
        )

        with pytest.raises(ValueError, match="Maximum number of turns reached"):
            ClueStateManager.apply_move(state, guess2)

    def test_apply_move_creates_new_state(self):
        """Test that apply_move creates a new state object."""
        state = ClueStateManager.initialize()
        original_id = id(state)

        guess = ClueGuess(
            suspect=ValidSuspect.MRS_PEACOCK,
            weapon=ValidWeapon.REVOLVER,
            room=ValidRoom.BALLROOM,
        )

        new_state = ClueStateManager.apply_move(state, guess)

        # Should be different objects
        assert id(new_state) != original_id
        assert len(state.guesses) == 0  # Original unchanged
        assert len(new_state.guesses) == 1  # New state has guess


class TestClueStateManagerGameStatus:
    """Test game status checking methods."""

    def test_check_game_status_returns_unchanged(self):
        """Test check_game_status returns state unchanged."""
        state = ClueStateManager.initialize()
        original_status = state.game_status

        new_state = ClueStateManager.check_game_status(state)

        assert new_state == state
        assert new_state.game_status == original_status

    def test_get_winner_ongoing_game(self):
        """Test get_winner returns None for ongoing game."""
        state = ClueStateManager.initialize()
        state.game_status = "ongoing"
        state.winner = None

        winner = ClueStateManager.get_winner(state)
        assert winner is None

    def test_get_winner_completed_game(self):
        """Test get_winner returns winner for completed game."""
        state = ClueStateManager.initialize()
        state.game_status = "player1_win"
        state.winner = "player1"

        winner = ClueStateManager.get_winner(state)
        assert winner == "player1"

        # Test player 2 win
        state.game_status = "player2_win"
        state.winner = "player2"

        winner = ClueStateManager.get_winner(state)
        assert winner == "player2"


class TestClueStateManagerAnalysis:
    """Test analysis and hypothesis methods."""

    def test_add_analysis_for_player1(self):
        """Test adding analysis for player 1."""
        state = ClueStateManager.initialize()
        initial_count = len(state.player1_hypotheses)

        hypothesis = {
            "suspect": "Colonel Mustard",
            "weapon": "Candlestick",
            "room": "Library",
            "confidence": 0.8,
        }

        new_state = ClueStateManager.add_analysis(state, "player1", hypothesis)

        assert len(new_state.player1_hypotheses) == initial_count + 1
        assert new_state.player1_hypotheses[-1] == hypothesis
        assert len(new_state.player2_hypotheses) == len(state.player2_hypotheses)

    def test_add_analysis_for_player2(self):
        """Test adding analysis for player 2."""
        state = ClueStateManager.initialize()
        initial_count = len(state.player2_hypotheses)

        hypothesis = {
            "suspect": "Miss Scarlet",
            "weapon": "Rope",
            "room": "Study",
            "confidence": 0.9,
        }

        new_state = ClueStateManager.add_analysis(state, "player2", hypothesis)

        assert len(new_state.player2_hypotheses) == initial_count + 1
        assert new_state.player2_hypotheses[-1] == hypothesis
        assert len(new_state.player1_hypotheses) == len(state.player1_hypotheses)

    def test_add_multiple_analyses(self):
        """Test adding multiple analyses."""
        state = ClueStateManager.initialize()

        # Add multiple hypotheses for player 1
        hyp1 = {"suspect": "Mr. Green", "confidence": 0.5}
        hyp2 = {"suspect": "Mrs. White", "confidence": 0.7}

        state = ClueStateManager.add_analysis(state, "player1", hyp1)
        state = ClueStateManager.add_analysis(state, "player1", hyp2)

        assert len(state.player1_hypotheses) == 2
        assert state.player1_hypotheses[0] == hyp1
        assert state.player1_hypotheses[1] == hyp2


class TestClueStateManagerPossibleSolutions:
    """Test possible solutions calculation."""

    def test_get_possible_solutions_initial_state(self):
        """Test getting possible solutions from initial state."""
        state = ClueStateManager.initialize()

        possible = ClueStateManager.get_possible_solutions(state)

        assert isinstance(possible, set)
        assert len(possible) > 0

        # Each solution should be a 3-tuple
        for solution in possible:
            assert isinstance(solution, tuple)
            assert len(solution) == 3
            suspect, weapon, room = solution
            assert isinstance(suspect, str)
            assert isinstance(weapon, str)
            assert isinstance(room, str)

    def test_possible_solutions_excludes_player_cards(self):
        """Test that possible solutions exclude cards in player hands."""
        state = ClueStateManager.initialize()

        # Manually set some player cards
        state.player1_cards = [ValidSuspect.COLONEL_MUSTARD, ValidWeapon.KNIFE]
        state.player2_cards = [ValidRoom.KITCHEN, ValidSuspect.MISS_SCARLET]

        possible = ClueStateManager.get_possible_solutions(state)

        # These cards should not appear in any solution
        for suspect, weapon, room in possible:
            assert suspect not in ["Colonel Mustard", "Miss Scarlet"]
            assert weapon != "Knife"
            assert room != "Kitchen"

    def test_possible_solutions_with_all_cards_known(self):
        """Test possible solutions when many cards are known."""
        state = ClueStateManager.initialize()

        # Set up a scenario where most cards are known
        state.player1_cards = [
            ValidSuspect.COLONEL_MUSTARD,
            ValidSuspect.PROFESSOR_PLUM,
            ValidWeapon.KNIFE,
            ValidWeapon.CANDLESTICK,
            ValidRoom.KITCHEN,
            ValidRoom.BALLROOM,
        ]
        state.player2_cards = [
            ValidSuspect.MR_GREEN,
            ValidSuspect.MRS_PEACOCK,
            ValidWeapon.REVOLVER,
            ValidWeapon.ROPE,
            ValidRoom.CONSERVATORY,
            ValidRoom.LIBRARY,
        ]

        possible = ClueStateManager.get_possible_solutions(state)

        # Should have fewer possible solutions
        assert len(possible) < 100  # Much less than 6*6*9 = 324

    def test_possible_solutions_uses_string_literals(self):
        """Test that get_possible_solutions uses string literals not enums."""
        state = ClueStateManager.initialize()

        # Clear player cards to get all possibilities
        state.player1_cards = []
        state.player2_cards = []

        possible = ClueStateManager.get_possible_solutions(state)

        # Check that we get expected string values
        expected_suspects = {
            "Miss Scarlet",
            "Colonel Mustard",
            "Mrs. White",
            "Mr. Green",
            "Mrs. Peacock",
            "Professor Plum",
        }
        expected_weapons = {
            "Candlestick",
            "Knife",
            "Lead Pipe",
            "Revolver",
            "Rope",
            "Wrench",
        }
        expected_rooms = {
            "Hall",
            "Lounge",
            "Dining Room",
            "Kitchen",
            "Ballroom",
            "Conservatory",
            "Billiard Room",
            "Library",
            "Study",
        }

        # Collect all unique values from solutions
        all_suspects = {s for s, _, _ in possible}
        all_weapons = {w for _, w, _ in possible}
        all_rooms = {r for _, _, r in possible}

        assert all_suspects == expected_suspects
        assert all_weapons == expected_weapons
        assert all_rooms == expected_rooms


class TestClueStateManagerEdgeCases:
    """Test edge cases and error handling."""

    def test_apply_move_with_guess_player_attribute(self):
        """Test apply_move handling when guess has player attribute."""
        state = ClueStateManager.initialize()

        # Create guess with player attribute
        guess = ClueGuess(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )
        # Manually add player attribute (not part of model)
        guess.player = "player1"

        # Should handle gracefully
        new_state = ClueStateManager.apply_move(state, guess)
        assert len(new_state.guesses) == 1

    def test_state_manager_with_empty_state(self):
        """Test state manager methods with minimal state."""
        # Create minimal state
        solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )
        state = ClueState(solution=solution)

        # Test methods work with minimal state
        moves = ClueStateManager.get_legal_moves(state)
        assert moves == []

        winner = ClueStateManager.get_winner(state)
        assert winner is None

        checked = ClueStateManager.check_game_status(state)
        assert checked == state

    def test_hypothesis_with_invalid_player(self):
        """Test add_analysis with invalid player name."""
        state = ClueStateManager.initialize()
        hypothesis = {"test": "data"}

        # Should handle any player name
        new_state = ClueStateManager.add_analysis(state, "player3", hypothesis)

        # Hypothesis goes to player2 list (else clause)
        assert len(new_state.player2_hypotheses) == 1
        assert new_state.player2_hypotheses[0] == hypothesis
