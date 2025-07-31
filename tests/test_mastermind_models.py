"""Test cases for Mastermind game models.

This module tests all the data models and classes used in the Mastermind game,
ensuring they behave correctly and validate input properly.
"""

from pydantic import ValidationError
import pytest

from haive.games.mastermind.models import (
    ColorCode,
    MastermindAnalysis,
    MastermindFeedback,
    MastermindGuess,
)


class TestColorCode:
    """Test cases for ColorCode model."""

    def test_valid_color_code_creation(self) -> None:
        """Test creating a valid color code."""
        code = ColorCode(code=["red", "blue", "green", "yellow"])

        assert code.code == ["red", "blue", "green", "yellow"]
        assert len(code.code) == 4

    def test_color_code_all_same_color(self) -> None:
        """Test creating a color code with all same colors."""
        code = ColorCode(code=["red", "red", "red", "red"])

        assert code.code == ["red", "red", "red", "red"]
        assert all(c == "red" for c in code.code)

    def test_color_code_all_valid_colors(self) -> None:
        """Test creating color codes with all valid colors."""
        valid_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

        for color in valid_colors:
            code = ColorCode(code=[color, "red", "blue", "green"])
            assert code.code[0] == color

    def test_color_code_invalid_length_too_short(self) -> None:
        """Test that color code with less than 4 colors raises error."""
        with pytest.raises(ValidationError) as exc_info:
            ColorCode(code=["red", "blue", "green"])

        errors = exc_info.value.errors()
        assert any(
            "List should have at least 4 items" in str(error) for error in errors
        )

    def test_color_code_invalid_length_too_long(self) -> None:
        """Test that color code with more than 4 colors raises error."""
        with pytest.raises(ValidationError) as exc_info:
            ColorCode(code=["red", "blue", "green", "yellow", "purple"])

        errors = exc_info.value.errors()
        assert any("List should have at most 4 items" in str(error) for error in errors)

    def test_color_code_invalid_color(self) -> None:
        """Test that invalid color raises error."""
        with pytest.raises(ValidationError) as exc_info:
            ColorCode(code=["red", "blue", "green", "pink"])

        errors = exc_info.value.errors()
        assert any("pink" in str(error) for error in errors)

    def test_color_code_empty_list(self) -> None:
        """Test that empty list raises error."""
        with pytest.raises(ValidationError):
            ColorCode(code=[])

    def test_color_code_serialization(self) -> None:
        """Test serialization and deserialization of ColorCode."""
        original_code = ColorCode(code=["purple", "orange", "blue", "red"])

        # Serialize to dict
        code_dict = original_code.model_dump()
        assert code_dict == {"code": ["purple", "orange", "blue", "red"]}

        # Deserialize from dict
        restored_code = ColorCode(**code_dict)
        assert restored_code == original_code


class TestMastermindGuess:
    """Test cases for MastermindGuess model."""

    def test_valid_guess_creation_player1(self) -> None:
        """Test creating a valid guess for player1."""
        guess = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player1"
        )

        assert guess.colors == ["red", "blue", "green", "yellow"]
        assert guess.player == "player1"

    def test_valid_guess_creation_player2(self) -> None:
        """Test creating a valid guess for player2."""
        guess = MastermindGuess(
            colors=["purple", "orange", "red", "blue"], player="player2"
        )

        assert guess.colors == ["purple", "orange", "red", "blue"]
        assert guess.player == "player2"

    def test_guess_string_representation(self) -> None:
        """Test string representation of guess."""
        guess = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player1"
        )

        expected = "player1 guesses: red, blue, green, yellow"
        assert str(guess) == expected

    def test_guess_invalid_player(self) -> None:
        """Test that invalid player raises error."""
        with pytest.raises(ValidationError) as exc_info:
            MastermindGuess(colors=["red", "blue", "green", "yellow"], player="player3")

        errors = exc_info.value.errors()
        assert any("player3" in str(error) for error in errors)

    def test_guess_invalid_color(self) -> None:
        """Test that invalid color in guess raises error."""
        with pytest.raises(ValidationError):
            MastermindGuess(colors=["red", "blue", "green", "black"], player="player1")

    def test_guess_wrong_length(self) -> None:
        """Test that wrong number of colors raises error."""
        with pytest.raises(ValidationError):
            MastermindGuess(colors=["red", "blue", "green"], player="player1")

    def test_guess_duplicate_colors(self) -> None:
        """Test that duplicate colors are allowed."""
        guess = MastermindGuess(colors=["red", "red", "red", "red"], player="player2")

        assert all(c == "red" for c in guess.colors)

    def test_guess_equality(self) -> None:
        """Test equality comparison of MastermindGuess objects."""
        guess1 = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player1"
        )
        guess2 = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player1"
        )
        guess3 = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )

        assert guess1 == guess2
        assert guess1 != guess3

    def test_guess_serialization(self) -> None:
        """Test serialization and deserialization of MastermindGuess."""
        original_guess = MastermindGuess(
            colors=["purple", "orange", "blue", "red"], player="player2"
        )

        # Serialize to dict
        guess_dict = original_guess.model_dump()
        assert guess_dict == {
            "colors": ["purple", "orange", "blue", "red"],
            "player": "player2",
        }

        # Deserialize from dict
        restored_guess = MastermindGuess(**guess_dict)
        assert restored_guess == original_guess


class TestMastermindFeedback:
    """Test cases for MastermindFeedback model."""

    def test_valid_feedback_creation(self) -> None:
        """Test creating valid feedback."""
        feedback = MastermindFeedback(correct_position=2, correct_color=1)

        assert feedback.correct_position == 2
        assert feedback.correct_color == 1

    def test_feedback_string_representation(self) -> None:
        """Test string representation of feedback."""
        feedback = MastermindFeedback(correct_position=3, correct_color=0)

        expected = "🌟 Correct position: 3, 🔄 Correct color: 0"
        assert str(feedback) == expected

    def test_feedback_is_winning_true(self) -> None:
        """Test is_winning method when all positions are correct."""
        feedback = MastermindFeedback(correct_position=4, correct_color=0)

        assert feedback.is_winning() is True

    def test_feedback_is_winning_false(self) -> None:
        """Test is_winning method when not all positions are correct."""
        feedback = MastermindFeedback(correct_position=3, correct_color=1)

        assert feedback.is_winning() is False

    def test_feedback_zero_values(self) -> None:
        """Test feedback with zero correct positions and colors."""
        feedback = MastermindFeedback(correct_position=0, correct_color=0)

        assert feedback.correct_position == 0
        assert feedback.correct_color == 0
        assert feedback.is_winning() is False

    def test_feedback_max_values(self) -> None:
        """Test feedback with maximum values."""
        feedback = MastermindFeedback(correct_position=4, correct_color=0)

        assert feedback.correct_position == 4
        assert feedback.correct_color == 0

    def test_feedback_invalid_position_negative(self) -> None:
        """Test that negative correct_position raises error."""
        with pytest.raises(ValidationError):
            MastermindFeedback(correct_position=-1, correct_color=0)

    def test_feedback_invalid_position_too_high(self) -> None:
        """Test that correct_position > 4 raises error."""
        with pytest.raises(ValidationError):
            MastermindFeedback(correct_position=5, correct_color=0)

    def test_feedback_invalid_color_negative(self) -> None:
        """Test that negative correct_color raises error."""
        with pytest.raises(ValidationError):
            MastermindFeedback(correct_position=0, correct_color=-1)

    def test_feedback_invalid_color_too_high(self) -> None:
        """Test that correct_color > 4 raises error."""
        with pytest.raises(ValidationError):
            MastermindFeedback(correct_position=0, correct_color=5)

    def test_feedback_invalid_total(self) -> None:
        """Test that total > 4 is allowed (though illogical in game)."""
        # Note: The model doesn't validate total <= 4, which could be added
        feedback = MastermindFeedback(correct_position=3, correct_color=3)

        assert feedback.correct_position == 3
        assert feedback.correct_color == 3

    def test_feedback_equality(self) -> None:
        """Test equality comparison of MastermindFeedback objects."""
        feedback1 = MastermindFeedback(correct_position=2, correct_color=1)
        feedback2 = MastermindFeedback(correct_position=2, correct_color=1)
        feedback3 = MastermindFeedback(correct_position=2, correct_color=2)

        assert feedback1 == feedback2
        assert feedback1 != feedback3

    def test_feedback_serialization(self) -> None:
        """Test serialization and deserialization of MastermindFeedback."""
        original_feedback = MastermindFeedback(correct_position=1, correct_color=2)

        # Serialize to dict
        feedback_dict = original_feedback.model_dump()
        assert feedback_dict == {"correct_position": 1, "correct_color": 2}

        # Deserialize from dict
        restored_feedback = MastermindFeedback(**feedback_dict)
        assert restored_feedback == original_feedback


class TestMastermindAnalysis:
    """Test cases for MastermindAnalysis model."""

    def test_valid_analysis_creation(self) -> None:
        """Test creating a valid analysis."""
        analysis = MastermindAnalysis(
            possible_combinations=100,
            high_probability_colors=["red", "blue"],
            eliminated_colors=["green"],
            fixed_positions=[{"index": "0", "color": "red"}],
            strategy="Focus on high probability colors",
            reasoning="Based on previous feedback, red and blue appear frequently",
            confidence=7,
        )

        assert analysis.possible_combinations == 100
        assert analysis.high_probability_colors == ["red", "blue"]
        assert analysis.eliminated_colors == ["green"]
        assert len(analysis.fixed_positions) == 1
        assert analysis.confidence == 7

    def test_analysis_minimal_creation(self) -> None:
        """Test creating analysis with minimal required fields."""
        analysis = MastermindAnalysis(
            possible_combinations=50,
            high_probability_colors=["purple"],
            strategy="Random guess",
            reasoning="Not enough information yet",
            confidence=3,
        )

        assert analysis.possible_combinations == 50
        assert analysis.eliminated_colors == []  # Default empty list
        assert analysis.fixed_positions == []  # Default empty list

    def test_analysis_all_colors_high_probability(self) -> None:
        """Test analysis with all colors as high probability."""
        all_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        analysis = MastermindAnalysis(
            possible_combinations=1296,  # 6^4
            high_probability_colors=all_colors,
            strategy="Initial guess",
            reasoning="No information available yet",
            confidence=1,
        )

        assert len(analysis.high_probability_colors) == 6

    def test_analysis_no_possible_combinations(self) -> None:
        """Test analysis with zero possible combinations."""
        analysis = MastermindAnalysis(
            possible_combinations=0,
            high_probability_colors=[],
            strategy="Error state",
            reasoning="No valid combinations match all feedback",
            confidence=10,
        )

        assert analysis.possible_combinations == 0

    def test_analysis_multiple_fixed_positions(self) -> None:
        """Test analysis with multiple fixed positions."""
        fixed = [
            {"index": "0", "color": "red"},
            {"index": "2", "color": "blue"},
            {"index": "3", "color": "green"},
        ]
        analysis = MastermindAnalysis(
            possible_combinations=6,
            high_probability_colors=["yellow", "purple", "orange"],
            fixed_positions=fixed,
            strategy="Fill remaining position",
            reasoning="Three positions are fixed, only one remains",
            confidence=9,
        )

        assert len(analysis.fixed_positions) == 3
        assert analysis.fixed_positions[0]["color"] == "red"

    def test_analysis_invalid_confidence_low(self) -> None:
        """Test that confidence < 1 raises error."""
        with pytest.raises(ValidationError):
            MastermindAnalysis(
                possible_combinations=100,
                high_probability_colors=["red"],
                strategy="Test",
                reasoning="Test",
                confidence=0,
            )

    def test_analysis_invalid_confidence_high(self) -> None:
        """Test that confidence > 10 raises error."""
        with pytest.raises(ValidationError):
            MastermindAnalysis(
                possible_combinations=100,
                high_probability_colors=["red"],
                strategy="Test",
                reasoning="Test",
                confidence=11,
            )

    def test_analysis_invalid_color_in_high_probability(self) -> None:
        """Test that invalid color in high_probability_colors raises error."""
        with pytest.raises(ValidationError):
            MastermindAnalysis(
                possible_combinations=100,
                high_probability_colors=["red", "pink"],
                strategy="Test",
                reasoning="Test",
                confidence=5,
            )

    def test_analysis_invalid_color_in_eliminated(self) -> None:
        """Test that invalid color in eliminated_colors raises error."""
        with pytest.raises(ValidationError):
            MastermindAnalysis(
                possible_combinations=100,
                high_probability_colors=["red"],
                eliminated_colors=["black"],
                strategy="Test",
                reasoning="Test",
                confidence=5,
            )

    def test_analysis_negative_combinations(self) -> None:
        """Test that negative possible_combinations is allowed."""
        # Note: Model doesn't validate >= 0, which might be worth adding
        analysis = MastermindAnalysis(
            possible_combinations=-1,
            high_probability_colors=["red"],
            strategy="Error",
            reasoning="Invalid state",
            confidence=1,
        )

        assert analysis.possible_combinations == -1

    def test_analysis_empty_strategy(self) -> None:
        """Test that empty strategy is allowed."""
        analysis = MastermindAnalysis(
            possible_combinations=100,
            high_probability_colors=["red"],
            strategy="",
            reasoning="Test",
            confidence=5,
        )

        assert analysis.strategy == ""

    def test_analysis_long_reasoning(self) -> None:
        """Test analysis with long reasoning text."""
        long_reasoning = "A" * 1000  # Very long reasoning
        analysis = MastermindAnalysis(
            possible_combinations=100,
            high_probability_colors=["red"],
            strategy="Test",
            reasoning=long_reasoning,
            confidence=5,
        )

        assert len(analysis.reasoning) == 1000

    def test_analysis_serialization(self) -> None:
        """Test serialization and deserialization of MastermindAnalysis."""
        original_analysis = MastermindAnalysis(
            possible_combinations=25,
            high_probability_colors=["yellow", "orange"],
            eliminated_colors=["red", "blue"],
            fixed_positions=[{"index": "1", "color": "green"}],
            strategy="Narrow down remaining positions",
            reasoning="Eliminated 2 colors, fixed 1 position",
            confidence=6,
        )

        # Serialize to dict
        analysis_dict = original_analysis.model_dump()

        # Deserialize from dict
        restored_analysis = MastermindAnalysis(**analysis_dict)
        assert restored_analysis == original_analysis
        assert restored_analysis.confidence == 6
        assert len(restored_analysis.eliminated_colors) == 2
