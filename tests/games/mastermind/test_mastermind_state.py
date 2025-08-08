"""Test cases for Mastermind game state.

This module tests the MastermindState class and its properties and methods
for managing the game state and board representation.
"""

import pytest

from haive.games.mastermind.models import (
    MastermindAnalysis,
    MastermindFeedback,
    MastermindGuess,
)
from haive.games.mastermind.state import MastermindState


class TestMastermindState:
    """Test cases for MastermindState class."""

    def test_mastermind_state_default_creation(self) -> None:
        """Test creating MastermindState with minimal required fields."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        assert state.secret_code == ["red", "blue", "green", "yellow"]
        assert state.codemaker == "player1"
        assert state.turn == "player2"
        assert state.game_status == "ongoing"
        assert state.guesses == []
        assert state.feedback == []
        assert state.max_turns == 10
        assert state.winner is None

    def test_mastermind_state_full_creation(self) -> None:
        """Test creating MastermindState with all fields."""
        guess1 = MastermindGuess(
            colors=["red", "red", "blue", "blue"], player="player2"
        )
        feedback1 = MastermindFeedback(correct_position=1, correct_color=1)
        analysis1 = MastermindAnalysis(
            possible_combinations=100,
            high_probability_colors=["red", "blue"],
            strategy="Test strategy",
            reasoning="Test reasoning",
            confidence=5,
        )

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[guess1],
            feedback=[feedback1],
            player1_analysis=[],
            player2_analysis=[analysis1],
            max_turns=12,
            winner=None,
        )

        assert len(state.guesses) == 1
        assert len(state.feedback) == 1
        assert len(state.player2_analysis) == 1
        assert state.max_turns == 12

    def test_mastermind_state_game_won(self) -> None:
        """Test state when game is won."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="player2_win",
            winner="player2",
        )

        assert state.game_status == "player2_win"
        assert state.winner == "player2"

    def test_mastermind_state_invalid_secret_code_length(self) -> None:
        """Test that invalid secret code length raises error."""
        with pytest.raises(ValueError):
            MastermindState(
                secret_code=["red", "blue", "green"],  # Only 3 colors
                codemaker="player1",
                turn="player2",
                game_status="ongoing",
            )

    def test_mastermind_state_invalid_color_in_secret(self) -> None:
        """Test that invalid color in secret code raises error."""
        with pytest.raises(ValueError):
            MastermindState(
                secret_code=["red", "blue", "green", "pink"],  # Invalid color
                codemaker="player1",
                turn="player2",
                game_status="ongoing",
            )

    def test_current_turn_number_empty(self) -> None:
        """Test current_turn_number with no guesses."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        assert state.current_turn_number == 1

    def test_current_turn_number_with_guesses(self) -> None:
        """Test current_turn_number with guesses."""
        guesses = [
            MastermindGuess(colors=["red"] * 4, player="player2"),
            MastermindGuess(colors=["blue"] * 4, player="player2"),
            MastermindGuess(colors=["green"] * 4, player="player2"),
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=guesses,
            feedback=[MastermindFeedback(correct_position=1, correct_color=0)] * 3,
        )

        assert state.current_turn_number == 4

    def test_turns_remaining_full(self) -> None:
        """Test turns_remaining with no guesses."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            max_turns=10,
        )

        assert state.turns_remaining == 10

    def test_turns_remaining_partial(self) -> None:
        """Test turns_remaining with some guesses."""
        guesses = [
            MastermindGuess(colors=["red"] * 4, player="player2") for _ in range(3)
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=guesses,
            feedback=[MastermindFeedback(correct_position=1, correct_color=0)] * 3,
            max_turns=10,
        )

        assert state.turns_remaining == 7

    def test_turns_remaining_none(self) -> None:
        """Test turns_remaining when all turns used."""
        guesses = [
            MastermindGuess(colors=["red"] * 4, player="player2") for _ in range(10)
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=guesses,
            feedback=[MastermindFeedback(correct_position=1, correct_color=0)] * 10,
            max_turns=10,
        )

        assert state.turns_remaining == 0

    def test_is_game_over_ongoing(self) -> None:
        """Test is_game_over when game is ongoing."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        assert state.is_game_over is False

    def test_is_game_over_player_win(self) -> None:
        """Test is_game_over when a player wins."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="player2_win",
        )

        assert state.is_game_over is True

    def test_is_game_over_codemaker_win(self) -> None:
        """Test is_game_over when codemaker wins."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="player1_win",
        )

        assert state.is_game_over is True

    def test_last_guess_empty(self) -> None:
        """Test last_guess when no guesses made."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        assert state.last_guess is None

    def test_last_guess_single(self) -> None:
        """Test last_guess with one guess."""
        guess = MastermindGuess(colors=["red", "red", "red", "red"], player="player2")

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[guess],
        )

        assert state.last_guess == guess

    def test_last_guess_multiple(self) -> None:
        """Test last_guess with multiple guesses."""
        guesses = [
            MastermindGuess(colors=["red"] * 4, player="player2"),
            MastermindGuess(colors=["blue"] * 4, player="player2"),
            MastermindGuess(colors=["green"] * 4, player="player2"),
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=guesses,
        )

        assert state.last_guess == guesses[-1]
        assert state.last_guess.colors == ["green"] * 4

    def test_last_feedback_empty(self) -> None:
        """Test last_feedback when no feedback given."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        assert state.last_feedback is None

    def test_last_feedback_single(self) -> None:
        """Test last_feedback with one feedback."""
        feedback = MastermindFeedback(correct_position=2, correct_color=1)

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            feedback=[feedback],
        )

        assert state.last_feedback == feedback

    def test_last_feedback_multiple(self) -> None:
        """Test last_feedback with multiple feedbacks."""
        feedbacks = [
            MastermindFeedback(correct_position=1, correct_color=0),
            MastermindFeedback(correct_position=2, correct_color=0),
            MastermindFeedback(correct_position=3, correct_color=0),
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            feedback=feedbacks,
        )

        assert state.last_feedback == feedbacks[-1]
        assert state.last_feedback.correct_position == 3

    def test_board_string_empty(self) -> None:
        """Test board_string with no guesses."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        board = state.board_string
        assert "Turn 1:" in board
        assert "No guesses yet" in board

    def test_board_string_single_guess(self) -> None:
        """Test board_string with one guess."""
        guess = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )
        feedback = MastermindFeedback(correct_position=4, correct_color=0)

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="player2_win",
            guesses=[guess],
            feedback=[feedback],
        )

        board = state.board_string
        assert "Turn 1:" in board
        assert "red, blue, green, yellow" in board
        assert "🌟 4" in board
        assert "🔄 0" in board

    def test_board_string_multiple_guesses(self) -> None:
        """Test board_string with multiple guesses."""
        guesses = [
            MastermindGuess(colors=["red"] * 4, player="player2"),
            MastermindGuess(colors=["blue"] * 4, player="player2"),
            MastermindGuess(colors=["green"] * 4, player="player2"),
        ]
        feedbacks = [
            MastermindFeedback(correct_position=1, correct_color=0),
            MastermindFeedback(correct_position=1, correct_color=0),
            MastermindFeedback(correct_position=1, correct_color=0),
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=guesses,
            feedback=feedbacks,
        )

        board = state.board_string
        assert "Turn 1:" in board
        assert "Turn 2:" in board
        assert "Turn 3:" in board
        assert "red, red, red, red" in board
        assert "blue, blue, blue, blue" in board
        assert "green, green, green, green" in board

    def test_board_string_no_feedback(self) -> None:
        """Test board_string with guess but no feedback."""
        guess = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[guess],
            feedback=[],
        )

        board = state.board_string
        assert "Turn 1:" in board
        assert "red, blue, green, yellow" in board
        assert "🌟" not in board  # No feedback shown

    def test_state_serialization(self) -> None:
        """Test serialization and deserialization of MastermindState."""
        guess = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )
        feedback = MastermindFeedback(correct_position=2, correct_color=1)
        analysis = MastermindAnalysis(
            possible_combinations=50,
            high_probability_colors=["red", "blue"],
            strategy="Test",
            reasoning="Test",
            confidence=5,
        )

        original_state = MastermindState(
            secret_code=["purple", "orange", "red", "blue"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[guess],
            feedback=[feedback],
            player2_analysis=[analysis],
            max_turns=8,
        )

        # Serialize to dict
        state_dict = original_state.model_dump()

        # Deserialize from dict
        restored_state = MastermindState(**state_dict)

        assert restored_state.secret_code == original_state.secret_code
        assert restored_state.codemaker == original_state.codemaker
        assert len(restored_state.guesses) == 1
        assert len(restored_state.feedback) == 1
        assert len(restored_state.player2_analysis) == 1
        assert restored_state.max_turns == 8

    def test_state_game_progression(self) -> None:
        """Test state through a game progression."""
        # Initial state
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        assert state.current_turn_number == 1
        assert state.turns_remaining == 10
        assert state.is_game_over is False

        # Add first guess
        state.guesses.append(
            MastermindGuess(
                colors=["purple", "purple", "purple", "purple"], player="player2"
            )
        )
        state.feedback.append(MastermindFeedback(correct_position=0, correct_color=0))

        assert state.current_turn_number == 2
        assert state.turns_remaining == 9

        # Add winning guess
        state.guesses.append(
            MastermindGuess(colors=["red", "blue", "green", "yellow"], player="player2")
        )
        state.feedback.append(MastermindFeedback(correct_position=4, correct_color=0))
        state.game_status = "player2_win"
        state.winner = "player2"

        assert state.is_game_over is True
        assert state.last_feedback.is_winning() is True

    def test_state_max_turns_game_over(self) -> None:
        """Test state when max turns reached."""
        guesses = [
            MastermindGuess(colors=["purple"] * 4, player="player2") for _ in range(10)
        ]
        feedbacks = [
            MastermindFeedback(correct_position=0, correct_color=0) for _ in range(10)
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="player1_win",  # Codemaker wins
            guesses=guesses,
            feedback=feedbacks,
            max_turns=10,
            winner="player1",
        )

        assert state.current_turn_number == 11  # Would be 11 if game continued
        assert state.turns_remaining == 0
        assert state.is_game_over is True
        assert state.winner == "player1"
