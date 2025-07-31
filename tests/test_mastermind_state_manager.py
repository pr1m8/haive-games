"""Test cases for Mastermind game state manager.

This module tests the MastermindStateManager class and its methods for
managing game initialization, moves, feedback, and state transitions.
"""

import pytest

from haive.games.mastermind.models import (
    ColorCode,
    MastermindAnalysis,
    MastermindFeedback,
    MastermindGuess,
)
from haive.games.mastermind.state import MastermindState
from haive.games.mastermind.state_manager import MastermindStateManager


class TestMastermindStateManagerInitialization:
    """Test cases for MastermindStateManager initialization methods."""

    def test_initialize_default(self) -> None:
        """Test initializing game with default settings."""
        state = MastermindStateManager.initialize()

        assert state.codemaker == "player1"
        assert state.turn == "player2"  # Codebreaker starts
        assert state.game_status == "ongoing"
        assert len(state.secret_code) == 4
        assert state.max_turns == 10
        assert state.guesses == []
        assert state.feedback == []
        assert all(
            color in MastermindStateManager.VALID_COLORS for color in state.secret_code
        )

    def test_initialize_player2_codemaker(self) -> None:
        """Test initializing game with player2 as codemaker."""
        state = MastermindStateManager.initialize(codemaker="player2")

        assert state.codemaker == "player2"
        assert state.turn == "player1"  # Other player is codebreaker

    def test_initialize_custom_max_turns(self) -> None:
        """Test initializing game with custom max turns."""
        state = MastermindStateManager.initialize(max_turns=15)

        assert state.max_turns == 15

    def test_initialize_with_predetermined_code_list(self) -> None:
        """Test initializing game with predetermined secret code as list."""
        secret = ["red", "blue", "green", "yellow"]
        state = MastermindStateManager.initialize(secret_code=secret)

        assert state.secret_code == secret

    def test_initialize_with_predetermined_code_colorcode(self) -> None:
        """Test initializing game with predetermined secret code as ColorCode."""
        secret = ColorCode(code=["purple", "orange", "red", "blue"])
        state = MastermindStateManager.initialize(secret_code=secret)

        assert state.secret_code == secret.code

    def test_initialize_custom_colors(self) -> None:
        """Test initializing game with custom color set."""
        custom_colors = ["red", "blue", "green", "yellow"]
        state = MastermindStateManager.initialize(colors=custom_colors)

        # All secret code colors should be from custom set
        assert all(color in custom_colors for color in state.secret_code)

    def test_initialize_custom_code_length(self) -> None:
        """Test initializing game with custom code length."""
        # Note: Current implementation doesn't support custom code length
        # This test documents current behavior
        state = MastermindStateManager.initialize(code_length=6)

        # Currently always returns 4-length codes
        assert len(state.secret_code) == 4

    def test_initialize_randomness(self) -> None:
        """Test that initialization produces random codes."""
        # Generate multiple states
        states = [MastermindStateManager.initialize() for _ in range(10)]

        # Extract secret codes
        codes = [tuple(state.secret_code) for state in states]

        # Should have some variety (not all the same)
        unique_codes = set(codes)
        assert len(unique_codes) > 1


class TestMastermindStateManagerMakeGuess:
    """Test cases for MastermindStateManager make_guess method."""

    def test_make_guess_valid(self) -> None:
        """Test making a valid guess."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )
        guess = MastermindGuess(colors=["red", "red", "red", "red"], player="player2")

        new_state = MastermindStateManager.make_guess(state, guess)

        assert len(new_state.guesses) == 1
        assert new_state.guesses[0] == guess
        assert new_state.turn == "player2"  # Turn doesn't change on guess

    def test_make_guess_wrong_player(self) -> None:
        """Test making guess as wrong player raises error."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )
        guess = MastermindGuess(
            colors=["red", "red", "red", "red"],
            player="player1",  # Wrong player
        )

        with pytest.raises(ValueError, match="Codemaker cannot make guesses"):
            MastermindStateManager.make_guess(state, guess)

    def test_make_guess_game_over(self) -> None:
        """Test making guess when game is over raises error."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="player2_win",
            winner="player2",
        )
        guess = MastermindGuess(colors=["red", "red", "red", "red"], player="player2")

        with pytest.raises(ValueError, match="Game is already over"):
            MastermindStateManager.make_guess(state, guess)

    def test_make_guess_preserves_state(self) -> None:
        """Test that making guess doesn't modify original state."""
        original_state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )
        guess = MastermindGuess(colors=["red", "red", "red", "red"], player="player2")

        new_state = MastermindStateManager.make_guess(original_state, guess)

        # Original state unchanged
        assert len(original_state.guesses) == 0
        # New state has guess
        assert len(new_state.guesses) == 1

    def test_make_multiple_guesses(self) -> None:
        """Test making multiple guesses in sequence."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        # First guess
        guess1 = MastermindGuess(colors=["red"] * 4, player="player2")
        state = MastermindStateManager.make_guess(state, guess1)
        assert len(state.guesses) == 1

        # Second guess
        guess2 = MastermindGuess(colors=["blue"] * 4, player="player2")
        state = MastermindStateManager.make_guess(state, guess2)
        assert len(state.guesses) == 2

        # Guesses in order
        assert state.guesses[0] == guess1
        assert state.guesses[1] == guess2


class TestMastermindStateManagerProvideFeedback:
    """Test cases for MastermindStateManager provide_feedback method."""

    def test_provide_feedback_all_correct(self) -> None:
        """Test providing feedback when guess is completely correct."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["red", "blue", "green", "yellow"], player="player2"
                )
            ],
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert len(new_state.feedback) == 1
        assert new_state.feedback[0].correct_position == 4
        assert new_state.feedback[0].correct_color == 0
        assert new_state.game_status == "player2_win"
        assert new_state.winner == "player2"

    def test_provide_feedback_no_correct(self) -> None:
        """Test providing feedback when no colors are correct."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["purple", "purple", "orange", "orange"], player="player2"
                )
            ],
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert len(new_state.feedback) == 1
        assert new_state.feedback[0].correct_position == 0
        assert new_state.feedback[0].correct_color == 0
        assert new_state.game_status == "ongoing"

    def test_provide_feedback_some_correct_position(self) -> None:
        """Test providing feedback with some correct positions."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["red", "blue", "yellow", "green"], player="player2"
                )
            ],
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert new_state.feedback[0].correct_position == 2  # red and blue
        assert new_state.feedback[0].correct_color == 2  # green and yellow

    def test_provide_feedback_all_correct_color_wrong_position(self) -> None:
        """Test feedback when all colors correct but wrong positions."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["yellow", "green", "blue", "red"], player="player2"
                )
            ],
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert new_state.feedback[0].correct_position == 0
        assert new_state.feedback[0].correct_color == 4

    def test_provide_feedback_duplicate_colors_in_guess(self) -> None:
        """Test feedback with duplicate colors in guess."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(colors=["red", "red", "red", "red"], player="player2")
            ],
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert new_state.feedback[0].correct_position == 1  # Only first red
        assert new_state.feedback[0].correct_color == 0

    def test_provide_feedback_duplicate_colors_in_secret(self) -> None:
        """Test feedback with duplicate colors in secret code."""
        state = MastermindState(
            secret_code=["red", "red", "blue", "blue"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(colors=["red", "blue", "red", "blue"], player="player2")
            ],
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert new_state.feedback[0].correct_position == 2  # First red and last blue
        assert new_state.feedback[0].correct_color == 2  # Second red and first blue

    def test_provide_feedback_no_guess(self) -> None:
        """Test providing feedback with no guesses raises error."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[],
        )

        with pytest.raises(ValueError, match="No guess to provide feedback for"):
            MastermindStateManager.provide_feedback(state)

    def test_provide_feedback_already_provided(self) -> None:
        """Test providing feedback when already provided raises error."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[MastermindGuess(colors=["red"] * 4, player="player2")],
            feedback=[MastermindFeedback(correct_position=1, correct_color=0)],
        )

        with pytest.raises(ValueError, match="Feedback already provided"):
            MastermindStateManager.provide_feedback(state)

    def test_provide_feedback_max_turns_reached(self) -> None:
        """Test providing feedback when max turns reached."""
        guesses = [
            MastermindGuess(colors=["purple"] * 4, player="player2") for _ in range(10)
        ]
        feedbacks = [
            MastermindFeedback(correct_position=0, correct_color=0) for _ in range(9)
        ]

        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=guesses,
            feedback=feedbacks,
            max_turns=10,
        )

        new_state = MastermindStateManager.provide_feedback(state)

        assert len(new_state.feedback) == 10
        assert new_state.game_status == "player1_win"  # Codemaker wins
        assert new_state.winner == "player1"


class TestMastermindStateManagerAddAnalysis:
    """Test cases for MastermindStateManager add_analysis method."""

    def test_add_analysis_player1(self) -> None:
        """Test adding analysis for player1."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player2",
            turn="player1",
            game_status="ongoing",
        )
        analysis = MastermindAnalysis(
            possible_combinations=100,
            high_probability_colors=["red", "blue"],
            strategy="Initial exploration",
            reasoning="No information yet",
            confidence=3,
        )

        new_state = MastermindStateManager.add_analysis(state, "player1", analysis)

        assert len(new_state.player1_analysis) == 1
        assert new_state.player1_analysis[0] == analysis
        assert len(new_state.player2_analysis) == 0

    def test_add_analysis_player2(self) -> None:
        """Test adding analysis for player2."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )
        analysis = MastermindAnalysis(
            possible_combinations=50,
            high_probability_colors=["green", "yellow"],
            strategy="Narrow down colors",
            reasoning="Based on feedback",
            confidence=6,
        )

        new_state = MastermindStateManager.add_analysis(state, "player2", analysis)

        assert len(new_state.player2_analysis) == 1
        assert new_state.player2_analysis[0] == analysis

    def test_add_multiple_analyses(self) -> None:
        """Test adding multiple analyses."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        analysis1 = MastermindAnalysis(
            possible_combinations=100,
            high_probability_colors=["red"],
            strategy="Test 1",
            reasoning="Test 1",
            confidence=5,
        )
        analysis2 = MastermindAnalysis(
            possible_combinations=50,
            high_probability_colors=["blue"],
            strategy="Test 2",
            reasoning="Test 2",
            confidence=7,
        )

        state = MastermindStateManager.add_analysis(state, "player2", analysis1)
        state = MastermindStateManager.add_analysis(state, "player2", analysis2)

        assert len(state.player2_analysis) == 2
        assert state.player2_analysis[0] == analysis1
        assert state.player2_analysis[1] == analysis2


class TestMastermindStateManagerGetPossibleCodes:
    """Test cases for MastermindStateManager get_possible_codes method."""

    def test_get_possible_codes_no_guesses(self) -> None:
        """Test getting possible codes with no guesses."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        possible = MastermindStateManager.get_possible_codes(state)

        # Should be 6^4 = 1296 possible codes
        assert len(possible) == 1296

    def test_get_possible_codes_with_feedback(self) -> None:
        """Test getting possible codes after feedback."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(colors=["red", "red", "red", "red"], player="player2")
            ],
            feedback=[MastermindFeedback(correct_position=1, correct_color=0)],
        )

        possible = MastermindStateManager.get_possible_codes(state)

        # Should be significantly fewer than 1296
        assert len(possible) < 1296

        # All possible codes should have exactly one red in one position
        for code in possible:
            red_count = sum(1 for c in code if c == "red")
            assert red_count == 1

    def test_get_possible_codes_no_matches(self) -> None:
        """Test getting possible codes when colors don't match."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["purple", "purple", "orange", "orange"], player="player2"
                )
            ],
            feedback=[MastermindFeedback(correct_position=0, correct_color=0)],
        )

        possible = MastermindStateManager.get_possible_codes(state)

        # No possible codes should contain purple or orange
        for code in possible:
            assert "purple" not in code
            assert "orange" not in code

    def test_get_possible_codes_exact_match(self) -> None:
        """Test getting possible codes with exact match."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["red", "blue", "green", "yellow"], player="player2"
                )
            ],
            feedback=[MastermindFeedback(correct_position=4, correct_color=0)],
        )

        possible = MastermindStateManager.get_possible_codes(state)

        # Only one possible code
        assert len(possible) == 1
        assert list(possible)[0] == ("red", "blue", "green", "yellow")


class TestMastermindStateManagerIsConsistentWithFeedback:
    """Test cases for _is_consistent_with_feedback helper method."""

    def test_is_consistent_exact_match(self) -> None:
        """Test consistency check with exact match."""
        code = ("red", "blue", "green", "yellow")
        guess = ("red", "blue", "green", "yellow")
        feedback = MastermindFeedback(correct_position=4, correct_color=0)

        result = MastermindStateManager._is_consistent_with_feedback(
            code, guess, feedback
        )

        assert result is True

    def test_is_consistent_no_match(self) -> None:
        """Test consistency check with no matches."""
        code = ("red", "blue", "green", "yellow")
        guess = ("purple", "purple", "orange", "orange")
        feedback = MastermindFeedback(correct_position=0, correct_color=0)

        result = MastermindStateManager._is_consistent_with_feedback(
            code, guess, feedback
        )

        assert result is True

    def test_is_consistent_partial_match(self) -> None:
        """Test consistency check with partial matches."""
        code = ("red", "blue", "green", "yellow")
        guess = ("red", "green", "blue", "yellow")
        feedback = MastermindFeedback(correct_position=2, correct_color=2)

        result = MastermindStateManager._is_consistent_with_feedback(
            code, guess, feedback
        )

        assert result is True

    def test_is_not_consistent_wrong_feedback(self) -> None:
        """Test consistency check with incorrect feedback."""
        code = ("red", "blue", "green", "yellow")
        guess = ("red", "blue", "green", "yellow")
        feedback = MastermindFeedback(correct_position=3, correct_color=0)  # Wrong

        result = MastermindStateManager._is_consistent_with_feedback(
            code, guess, feedback
        )

        assert result is False

    def test_is_consistent_duplicates(self) -> None:
        """Test consistency check with duplicate colors."""
        code = ("red", "red", "blue", "blue")
        guess = ("red", "blue", "red", "blue")
        feedback = MastermindFeedback(correct_position=2, correct_color=2)

        result = MastermindStateManager._is_consistent_with_feedback(
            code, guess, feedback
        )

        assert result is True


class TestMastermindStateManagerEndToEnd:
    """Test cases for end-to-end MastermindStateManager workflows."""

    def test_complete_game_win(self) -> None:
        """Test complete game workflow ending in codebreaker win."""
        # Initialize
        state = MastermindStateManager.initialize(
            secret_code=["red", "blue", "green", "yellow"]
        )

        # First guess - all wrong
        guess1 = MastermindGuess(
            colors=["purple", "purple", "orange", "orange"], player="player2"
        )
        state = MastermindStateManager.make_guess(state, guess1)
        state = MastermindStateManager.provide_feedback(state)
        assert state.feedback[0].correct_position == 0
        assert state.feedback[0].correct_color == 0

        # Second guess - some correct colors
        guess2 = MastermindGuess(
            colors=["red", "red", "blue", "blue"], player="player2"
        )
        state = MastermindStateManager.make_guess(state, guess2)
        state = MastermindStateManager.provide_feedback(state)
        assert state.feedback[1].correct_position == 1  # First red
        assert state.feedback[1].correct_color == 1  # Blue in wrong spot

        # Third guess - winning
        guess3 = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )
        state = MastermindStateManager.make_guess(state, guess3)
        state = MastermindStateManager.provide_feedback(state)

        assert state.feedback[2].correct_position == 4
        assert state.feedback[2].correct_color == 0
        assert state.game_status == "player2_win"
        assert state.winner == "player2"

    def test_complete_game_lose(self) -> None:
        """Test complete game workflow ending in codemaker win."""
        # Initialize with simple code
        state = MastermindStateManager.initialize(
            secret_code=["red", "red", "red", "red"], max_turns=3
        )

        # Make 3 wrong guesses
        wrong_colors = [
            ["blue", "blue", "blue", "blue"],
            ["green", "green", "green", "green"],
            ["yellow", "yellow", "yellow", "yellow"],
        ]

        for colors in wrong_colors:
            guess = MastermindGuess(colors=colors, player="player2")
            state = MastermindStateManager.make_guess(state, guess)
            state = MastermindStateManager.provide_feedback(state)

        # Game should be over with codemaker win
        assert len(state.guesses) == 3
        assert len(state.feedback) == 3
        assert all(f.correct_position == 0 for f in state.feedback)
        assert state.game_status == "player1_win"
        assert state.winner == "player1"
