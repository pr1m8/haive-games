"""Test cases for Nim game models.

This module tests all the data models and classes used in the Nim game,
ensuring they behave correctly and validate input properly.
"""

import pytest
from pydantic import ValidationError

from haive.games.nim.models import NimAnalysis, NimMove


class TestNimMove:
    """Test cases for NimMove model."""

    def test_nim_move_creation_valid(self) -> None:
        """Test creating a valid Nim move."""
        move = NimMove(pile_index=0, stones_taken=3)

        assert move.pile_index == 0
        assert move.stones_taken == 3

    def test_nim_move_creation_different_values(self) -> None:
        """Test creating moves with different values."""
        move1 = NimMove(pile_index=1, stones_taken=1)
        assert move1.pile_index == 1
        assert move1.stones_taken == 1

        move2 = NimMove(pile_index=2, stones_taken=7)
        assert move2.pile_index == 2
        assert move2.stones_taken == 7

    def test_nim_move_string_representation(self) -> None:
        """Test string representation of NimMove."""
        move = NimMove(pile_index=1, stones_taken=5)
        expected = "Take 5 stones from pile 1"
        assert str(move) == expected

    def test_nim_move_string_representation_single_stone(self) -> None:
        """Test string representation with single stone."""
        move = NimMove(pile_index=0, stones_taken=1)
        expected = "Take 1 stones from pile 0"
        assert str(move) == expected

    def test_nim_move_string_representation_zero_index(self) -> None:
        """Test string representation with pile index 0."""
        move = NimMove(pile_index=0, stones_taken=2)
        expected = "Take 2 stones from pile 0"
        assert str(move) == expected

    def test_nim_move_large_values(self) -> None:
        """Test creating moves with large values."""
        move = NimMove(pile_index=10, stones_taken=100)

        assert move.pile_index == 10
        assert move.stones_taken == 100
        assert "100 stones from pile 10" in str(move)

    def test_nim_move_negative_pile_index(self) -> None:
        """Test that negative pile index is accepted (validation done elsewhere)."""
        # Note: Validation is typically done in state manager, not model
        move = NimMove(pile_index=-1, stones_taken=1)
        assert move.pile_index == -1

    def test_nim_move_zero_stones(self) -> None:
        """Test that zero stones is accepted (validation done elsewhere)."""
        # Note: Validation is typically done in state manager, not model
        move = NimMove(pile_index=0, stones_taken=0)
        assert move.stones_taken == 0

    def test_nim_move_field_descriptions(self) -> None:
        """Test that field descriptions are properly set."""
        # Access field info through model fields
        fields = NimMove.model_fields

        assert "pile_index" in fields
        assert "stones_taken" in fields
        assert fields["pile_index"].description == "Index of the pile to take from"
        assert fields["stones_taken"].description == "Number of stones to take"

    def test_nim_move_equality(self) -> None:
        """Test equality comparison of NimMove objects."""
        move1 = NimMove(pile_index=1, stones_taken=3)
        move2 = NimMove(pile_index=1, stones_taken=3)
        move3 = NimMove(pile_index=1, stones_taken=4)
        move4 = NimMove(pile_index=2, stones_taken=3)

        assert move1 == move2
        assert move1 != move3
        assert move1 != move4

    def test_nim_move_serialization(self) -> None:
        """Test serialization and deserialization of NimMove."""
        original_move = NimMove(pile_index=2, stones_taken=5)

        # Serialize to dict
        move_dict = original_move.model_dump()
        assert move_dict == {"pile_index": 2, "stones_taken": 5}

        # Deserialize from dict
        restored_move = NimMove(**move_dict)
        assert restored_move == original_move


class TestNimAnalysis:
    """Test cases for NimAnalysis model."""

    def test_nim_analysis_creation_basic(self) -> None:
        """Test creating a basic Nim analysis."""
        move = NimMove(pile_index=1, stones_taken=2)

        analysis = NimAnalysis(
            nim_sum=3,
            position_evaluation="winning",
            recommended_move=move,
            explanation="The nim-sum is non-zero, indicating a winning position",
        )

        assert analysis.nim_sum == 3
        assert analysis.position_evaluation == "winning"
        assert analysis.recommended_move == move
        assert "nim-sum" in analysis.explanation
        assert "winning" in analysis.explanation

    def test_nim_analysis_losing_position(self) -> None:
        """Test creating analysis for a losing position."""
        move = NimMove(pile_index=0, stones_taken=1)

        analysis = NimAnalysis(
            nim_sum=0,
            position_evaluation="losing",
            recommended_move=move,
            explanation="The nim-sum is zero, indicating a losing position",
        )

        assert analysis.nim_sum == 0
        assert analysis.position_evaluation == "losing"
        assert analysis.recommended_move == move
        assert "zero" in analysis.explanation

    def test_nim_analysis_unclear_position(self) -> None:
        """Test creating analysis for an unclear position."""
        move = NimMove(pile_index=2, stones_taken=3)

        analysis = NimAnalysis(
            nim_sum=5,
            position_evaluation="unclear",
            recommended_move=move,
            explanation="Complex position requiring deep calculation",
        )

        assert analysis.nim_sum == 5
        assert analysis.position_evaluation == "unclear"
        assert "complex" in analysis.explanation.lower()

    def test_nim_analysis_string_representation(self) -> None:
        """Test string representation of NimAnalysis."""
        move = NimMove(pile_index=1, stones_taken=4)

        analysis = NimAnalysis(
            nim_sum=2,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Take stones to force nim-sum to zero",
        )

        result = str(analysis)
        assert "Analysis:" in result
        assert "winning" in result
        assert "force nim-sum" in result

    def test_nim_analysis_zero_nim_sum(self) -> None:
        """Test analysis with zero nim-sum."""
        move = NimMove(pile_index=0, stones_taken=2)

        analysis = NimAnalysis(
            nim_sum=0,
            position_evaluation="losing",
            recommended_move=move,
            explanation="Nim-sum is zero - any move gives opponent winning position",
        )

        assert analysis.nim_sum == 0
        assert "zero" in analysis.explanation

    def test_nim_analysis_large_nim_sum(self) -> None:
        """Test analysis with large nim-sum."""
        move = NimMove(pile_index=3, stones_taken=15)

        analysis = NimAnalysis(
            nim_sum=63,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Large nim-sum indicates many winning moves available",
        )

        assert analysis.nim_sum == 63
        assert analysis.position_evaluation == "winning"

    def test_nim_analysis_detailed_explanation(self) -> None:
        """Test analysis with detailed explanation."""
        move = NimMove(pile_index=1, stones_taken=3)

        detailed_explanation = (
            "The current nim-sum is 6 (3 XOR 5 XOR 0). To win, we need to make a move "
            "that reduces the nim-sum to 0. Taking 3 stones from pile 1 will change "
            "pile 1 from 5 to 2, giving us nim-sum of 3 XOR 2 XOR 0 = 1. This is not "
            "optimal. We should take 4 stones instead."
        )

        analysis = NimAnalysis(
            nim_sum=6,
            position_evaluation="winning",
            recommended_move=move,
            explanation=detailed_explanation,
        )

        assert "XOR" in analysis.explanation
        assert "optimal" in analysis.explanation
        assert "3 stones from pile 1" in analysis.explanation

    def test_nim_analysis_field_descriptions(self) -> None:
        """Test that field descriptions are properly set."""
        fields = NimAnalysis.model_fields

        assert "nim_sum" in fields
        assert "position_evaluation" in fields
        assert "recommended_move" in fields
        assert "explanation" in fields

        assert "XOR sum" in fields["nim_sum"].description
        assert "winning, losing" in fields["position_evaluation"].description
        assert "Recommended move" in fields["recommended_move"].description
        assert "Explanation" in fields["explanation"].description

    def test_nim_analysis_different_evaluations(self) -> None:
        """Test analysis with different position evaluations."""
        move = NimMove(pile_index=0, stones_taken=1)

        evaluations = ["winning", "losing", "unclear", "draw", "complex"]

        for eval_str in evaluations:
            analysis = NimAnalysis(
                nim_sum=1,
                position_evaluation=eval_str,
                recommended_move=move,
                explanation=f"Position is {eval_str}",
            )

            assert analysis.position_evaluation == eval_str
            assert eval_str in analysis.explanation

    def test_nim_analysis_serialization(self) -> None:
        """Test serialization and deserialization of NimAnalysis."""
        move = NimMove(pile_index=2, stones_taken=6)

        original_analysis = NimAnalysis(
            nim_sum=7,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Strategic advantage available",
        )

        # Serialize to dict
        analysis_dict = original_analysis.model_dump()
        expected_keys = {
            "nim_sum",
            "position_evaluation",
            "recommended_move",
            "explanation",
        }
        assert set(analysis_dict.keys()) == expected_keys

        # Deserialize from dict
        restored_analysis = NimAnalysis(**analysis_dict)
        assert restored_analysis == original_analysis

    def test_nim_analysis_move_consistency(self) -> None:
        """Test that the recommended move is consistent with analysis."""
        move = NimMove(pile_index=1, stones_taken=5)

        analysis = NimAnalysis(
            nim_sum=5,
            position_evaluation="winning",
            recommended_move=move,
            explanation="Take 5 stones from pile 1 to achieve nim-sum of 0",
        )

        # The move in the analysis should match the move we created
        assert analysis.recommended_move.pile_index == 1
        assert analysis.recommended_move.stones_taken == 5
        assert str(analysis.recommended_move) == "Take 5 stones from pile 1"

    def test_nim_analysis_negative_nim_sum(self) -> None:
        """Test that negative nim-sum is handled properly."""
        # Note: Nim-sum should never be negative in practice, but test edge case
        move = NimMove(pile_index=0, stones_taken=1)

        analysis = NimAnalysis(
            nim_sum=-1,  # Invalid in practice, but test model flexibility
            position_evaluation="error",
            recommended_move=move,
            explanation="Invalid nim-sum detected",
        )

        assert analysis.nim_sum == -1
        assert "error" in analysis.position_evaluation

    def test_nim_analysis_empty_explanation(self) -> None:
        """Test analysis with empty explanation."""
        move = NimMove(pile_index=0, stones_taken=1)

        analysis = NimAnalysis(
            nim_sum=3,
            position_evaluation="winning",
            recommended_move=move,
            explanation="",
        )

        assert analysis.explanation == ""
        assert str(analysis) == "Analysis: winning - "

    def test_nim_analysis_multiple_moves_in_explanation(self) -> None:
        """Test analysis that mentions multiple possible moves."""
        move = NimMove(pile_index=1, stones_taken=2)

        explanation = (
            "Several winning moves exist: take 2 from pile 1, take 3 from pile 2, "
            "or take 1 from pile 0. The recommended move is take 2 from pile 1 "
            "as it leaves the most balanced position."
        )

        analysis = NimAnalysis(
            nim_sum=4,
            position_evaluation="winning",
            recommended_move=move,
            explanation=explanation,
        )

        assert "several winning moves" in analysis.explanation.lower()
        assert "take 2 from pile 1" in analysis.explanation.lower()
        assert "balanced position" in analysis.explanation.lower()
