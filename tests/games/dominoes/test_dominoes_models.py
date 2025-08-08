"""Test cases for Dominoes game models.

This module tests all the data models and classes used in the Dominoes game,
ensuring they behave correctly and validate input properly.
"""

from pydantic import ValidationError
import pytest

from haive.games.dominoes.models import (
    DominoesAnalysis,
    DominoesPlayerDecision,
    DominoMove,
    DominoTile,
)


class TestDominoTile:
    """Test cases for DominoTile model."""

    def test_valid_tile_creation(self) -> None:
        """Test creating a valid domino tile."""
        tile = DominoTile(left=3, right=5)

        assert tile.left == 3
        assert tile.right == 5

    def test_double_tile_creation(self) -> None:
        """Test creating a double tile."""
        tile = DominoTile(left=6, right=6)

        assert tile.left == 6
        assert tile.right == 6
        assert tile.is_double() is True

    def test_tile_with_zeros(self) -> None:
        """Test creating a tile with zeros."""
        tile = DominoTile(left=0, right=3)

        assert tile.left == 0
        assert tile.right == 3
        assert tile.is_double() is False

    def test_double_zero_tile(self) -> None:
        """Test creating a double zero tile."""
        tile = DominoTile(left=0, right=0)

        assert tile.left == 0
        assert tile.right == 0
        assert tile.is_double() is True

    def test_is_double_method(self) -> None:
        """Test is_double method for various tiles."""
        double_tile = DominoTile(left=4, right=4)
        regular_tile = DominoTile(left=3, right=5)

        assert double_tile.is_double() is True
        assert regular_tile.is_double() is False

    def test_tile_string_representation(self) -> None:
        """Test string representation of tiles."""
        tile1 = DominoTile(left=3, right=5)
        tile2 = DominoTile(left=6, right=6)

        assert str(tile1) == "[3|5]"
        assert str(tile2) == "[6|6]"

    def test_tile_negative_values(self) -> None:
        """Test that negative values are accepted (no validation)."""
        # Note: Model doesn't validate >= 0, which might be worth adding
        tile = DominoTile(left=-1, right=5)

        assert tile.left == -1
        assert tile.right == 5

    def test_tile_large_values(self) -> None:
        """Test tiles with large pip values."""
        tile = DominoTile(left=12, right=15)

        assert tile.left == 12
        assert tile.right == 15

    def test_tile_equality(self) -> None:
        """Test equality comparison of DominoTile objects."""
        tile1 = DominoTile(left=3, right=5)
        tile2 = DominoTile(left=3, right=5)
        tile3 = DominoTile(left=5, right=3)  # Same values, different order
        tile4 = DominoTile(left=2, right=4)

        assert tile1 == tile2
        assert tile1 != tile3  # Order matters
        assert tile1 != tile4

    def test_tile_serialization(self) -> None:
        """Test serialization and deserialization of DominoTile."""
        original_tile = DominoTile(left=4, right=2)

        # Serialize to dict
        tile_dict = original_tile.model_dump()
        assert tile_dict == {"left": 4, "right": 2}

        # Deserialize from dict
        restored_tile = DominoTile(**tile_dict)
        assert restored_tile == original_tile

    def test_tile_field_descriptions(self) -> None:
        """Test that field descriptions are properly set."""
        fields = DominoTile.model_fields

        assert "left" in fields
        assert "right" in fields
        assert fields["left"].description == "The value on the left side of the tile"
        assert fields["right"].description == "The value on the right side of the tile"


class TestDominoMove:
    """Test cases for DominoMove model."""

    def test_valid_move_creation(self) -> None:
        """Test creating a valid domino move."""
        tile = DominoTile(left=3, right=5)
        move = DominoMove(tile=tile, end="left")

        assert move.tile == tile
        assert move.end == "left"

    def test_move_right_end(self) -> None:
        """Test creating a move for the right end."""
        tile = DominoTile(left=2, right=4)
        move = DominoMove(tile=tile, end="right")

        assert move.tile.left == 2
        assert move.tile.right == 4
        assert move.end == "right"

    def test_move_with_double_tile(self) -> None:
        """Test creating a move with a double tile."""
        double_tile = DominoTile(left=6, right=6)
        move = DominoMove(tile=double_tile, end="left")

        assert move.tile.is_double() is True
        assert move.end == "left"

    def test_move_invalid_end(self) -> None:
        """Test that invalid end value raises error."""
        tile = DominoTile(left=3, right=5)

        with pytest.raises(ValidationError) as exc_info:
            DominoMove(tile=tile, end="middle")

        errors = exc_info.value.errors()
        assert any("middle" in str(error) for error in errors)

    def test_move_string_representation(self) -> None:
        """Test string representation of move."""
        tile = DominoTile(left=3, right=5)
        move = DominoMove(tile=tile, end="left")

        expected = "Play [3|5] on the left end"
        assert str(move) == expected

    def test_move_string_representation_right_end(self) -> None:
        """Test string representation for right end move."""
        tile = DominoTile(left=2, right=4)
        move = DominoMove(tile=tile, end="right")

        expected = "Play [2|4] on the right end"
        assert str(move) == expected

    def test_move_equality(self) -> None:
        """Test equality comparison of DominoMove objects."""
        tile1 = DominoTile(left=3, right=5)
        tile2 = DominoTile(left=3, right=5)
        tile3 = DominoTile(left=2, right=4)

        move1 = DominoMove(tile=tile1, end="left")
        move2 = DominoMove(tile=tile2, end="left")
        move3 = DominoMove(tile=tile1, end="right")
        move4 = DominoMove(tile=tile3, end="left")

        assert move1 == move2
        assert move1 != move3  # Different end
        assert move1 != move4  # Different tile

    def test_move_serialization(self) -> None:
        """Test serialization and deserialization of DominoMove."""
        tile = DominoTile(left=5, right=3)
        original_move = DominoMove(tile=tile, end="right")

        # Serialize to dict
        move_dict = original_move.model_dump()
        assert move_dict == {"tile": {"left": 5, "right": 3}, "end": "right"}

        # Deserialize from dict
        restored_move = DominoMove(**move_dict)
        assert restored_move == original_move


class TestDominoesAnalysis:
    """Test cases for DominoesAnalysis model."""

    def test_valid_analysis_creation(self) -> None:
        """Test creating a valid dominoes analysis."""
        analysis = DominoesAnalysis(
            hand_strength=8,
            pip_count_assessment="High pip count",
            open_ends=["5", "3"],
            missing_values=[1, 2],
            suggested_strategy="Play high tiles first",
            blocking_potential="Can block on 5",
            reasoning="Strong hand with blocking options",
        )

        assert analysis.hand_strength == 8
        assert analysis.pip_count_assessment == "High pip count"
        assert analysis.open_ends == ["5", "3"]
        assert analysis.missing_values == [1, 2]

    def test_analysis_minimal_creation(self) -> None:
        """Test creating analysis with minimal fields."""
        analysis = DominoesAnalysis(
            hand_strength=5,
            pip_count_assessment="Average",
            open_ends=["2"],
            missing_values=[],
            suggested_strategy="Play normally",
            blocking_potential="None",
            reasoning="Standard position",
        )

        assert analysis.hand_strength == 5
        assert len(analysis.missing_values) == 0

    def test_analysis_low_hand_strength(self) -> None:
        """Test analysis with low hand strength."""
        analysis = DominoesAnalysis(
            hand_strength=1,
            pip_count_assessment="Very low",
            open_ends=["1", "6"],
            missing_values=[0, 2, 3, 4, 5],
            suggested_strategy="Draw tiles when possible",
            blocking_potential="Limited",
            reasoning="Weak hand, need more tiles",
        )

        assert analysis.hand_strength == 1
        assert len(analysis.missing_values) == 5

    def test_analysis_invalid_hand_strength_low(self) -> None:
        """Test that hand_strength < 1 raises error."""
        with pytest.raises(ValidationError):
            DominoesAnalysis(
                hand_strength=0,
                pip_count_assessment="Invalid",
                open_ends=["1"],
                missing_values=[],
                suggested_strategy="Test",
                blocking_potential="None",
                reasoning="Test",
            )

    def test_analysis_invalid_hand_strength_high(self) -> None:
        """Test that hand_strength > 10 raises error."""
        with pytest.raises(ValidationError):
            DominoesAnalysis(
                hand_strength=11,
                pip_count_assessment="Invalid",
                open_ends=["1"],
                missing_values=[],
                suggested_strategy="Test",
                blocking_potential="None",
                reasoning="Test",
            )

    def test_analysis_multiple_open_ends(self) -> None:
        """Test analysis with multiple open ends."""
        analysis = DominoesAnalysis(
            hand_strength=7,
            pip_count_assessment="Good",
            open_ends=["0", "3", "5", "6"],  # More than 2 for special variants
            missing_values=[],
            suggested_strategy="Multiple options available",
            blocking_potential="High",
            reasoning="Many playable tiles",
        )

        assert len(analysis.open_ends) == 4

    def test_analysis_empty_open_ends(self) -> None:
        """Test analysis with no open ends (blocked game)."""
        analysis = DominoesAnalysis(
            hand_strength=3,
            pip_count_assessment="Low",
            open_ends=[],
            missing_values=[1, 2, 3],
            suggested_strategy="Game is blocked",
            blocking_potential="N/A",
            reasoning="No playable moves",
        )

        assert len(analysis.open_ends) == 0

    def test_analysis_long_strategy_text(self) -> None:
        """Test analysis with long strategy text."""
        long_strategy = "A" * 200
        analysis = DominoesAnalysis(
            hand_strength=5,
            pip_count_assessment="Average",
            open_ends=["4"],
            missing_values=[],
            suggested_strategy=long_strategy,
            blocking_potential="Medium",
            reasoning="Test",
        )

        assert len(analysis.suggested_strategy) == 200

    def test_analysis_negative_missing_values(self) -> None:
        """Test that negative values in missing_values are accepted."""
        # Note: Model doesn't validate pip values, which might be worth adding
        analysis = DominoesAnalysis(
            hand_strength=5,
            pip_count_assessment="Test",
            open_ends=["3"],
            missing_values=[-1, 0, 7, 100],
            suggested_strategy="Test",
            blocking_potential="Test",
            reasoning="Test",
        )

        assert -1 in analysis.missing_values
        assert 100 in analysis.missing_values

    def test_analysis_serialization(self) -> None:
        """Test serialization and deserialization of DominoesAnalysis."""
        original_analysis = DominoesAnalysis(
            hand_strength=6,
            pip_count_assessment="Above average",
            open_ends=["2", "5"],
            missing_values=[0, 1],
            suggested_strategy="Control the board",
            blocking_potential="Medium",
            reasoning="Good position",
        )

        # Serialize to dict
        analysis_dict = original_analysis.model_dump()

        # Deserialize from dict
        restored_analysis = DominoesAnalysis(**analysis_dict)
        assert restored_analysis == original_analysis
        assert restored_analysis.hand_strength == 6
        assert len(restored_analysis.open_ends) == 2


class TestDominoesPlayerDecision:
    """Test cases for DominoesPlayerDecision model."""

    def test_valid_move_decision(self) -> None:
        """Test creating a valid move decision."""
        tile = DominoTile(left=3, right=5)
        move = DominoMove(tile=tile, end="left")

        decision = DominoesPlayerDecision(
            move=move, pass_turn=False, reasoning="Playing my highest tile"
        )

        assert decision.move == move
        assert decision.pass_turn is False
        assert decision.reasoning == "Playing my highest tile"

    def test_pass_decision(self) -> None:
        """Test creating a pass decision."""
        decision = DominoesPlayerDecision(
            move=None, pass_turn=True, reasoning="No playable tiles"
        )

        assert decision.move is None
        assert decision.pass_turn is True

    def test_decision_with_empty_reasoning(self) -> None:
        """Test decision with empty reasoning."""
        tile = DominoTile(left=2, right=2)
        move = DominoMove(tile=tile, end="right")

        decision = DominoesPlayerDecision(move=move, pass_turn=False, reasoning="")

        assert decision.reasoning == ""

    def test_decision_pass_with_move(self) -> None:
        """Test that passing with a move is allowed (though illogical)."""
        # Note: Model doesn't validate this constraint
        tile = DominoTile(left=1, right=1)
        move = DominoMove(tile=tile, end="left")

        decision = DominoesPlayerDecision(
            move=move, pass_turn=True, reasoning="Confusing decision"
        )

        assert decision.move is not None
        assert decision.pass_turn is True

    def test_decision_string_representation_move(self) -> None:
        """Test string representation of move decision."""
        tile = DominoTile(left=4, right=6)
        move = DominoMove(tile=tile, end="left")

        decision = DominoesPlayerDecision(
            move=move, pass_turn=False, reasoning="Best move available"
        )

        expected = "Decision: Play [4|6] on the left end - Best move available"
        assert str(decision) == expected

    def test_decision_string_representation_pass(self) -> None:
        """Test string representation of pass decision."""
        decision = DominoesPlayerDecision(
            move=None, pass_turn=True, reasoning="Cannot play"
        )

        expected = "Decision: Pass - Cannot play"
        assert str(decision) == expected

    def test_decision_long_reasoning(self) -> None:
        """Test decision with long reasoning text."""
        long_reasoning = "This is a complex strategic decision " * 10

        decision = DominoesPlayerDecision(
            move=None, pass_turn=True, reasoning=long_reasoning
        )

        assert len(decision.reasoning) > 300

    def test_decision_equality(self) -> None:
        """Test equality comparison of DominoesPlayerDecision objects."""
        tile = DominoTile(left=3, right=3)
        move1 = DominoMove(tile=tile, end="left")
        move2 = DominoMove(tile=tile, end="left")

        decision1 = DominoesPlayerDecision(
            move=move1, pass_turn=False, reasoning="Test"
        )
        decision2 = DominoesPlayerDecision(
            move=move2, pass_turn=False, reasoning="Test"
        )
        decision3 = DominoesPlayerDecision(
            move=move1,
            pass_turn=True,
            reasoning="Test",  # Different
        )

        assert decision1 == decision2
        assert decision1 != decision3

    def test_decision_serialization(self) -> None:
        """Test serialization and deserialization of DominoesPlayerDecision."""
        tile = DominoTile(left=5, right=5)
        move = DominoMove(tile=tile, end="right")

        original_decision = DominoesPlayerDecision(
            move=move, pass_turn=False, reasoning="Playing double five"
        )

        # Serialize to dict
        decision_dict = original_decision.model_dump()
        assert decision_dict == {
            "move": {"tile": {"left": 5, "right": 5}, "end": "right"},
            "pass_turn": False,
            "reasoning": "Playing double five",
        }

        # Deserialize from dict
        restored_decision = DominoesPlayerDecision(**decision_dict)
        assert restored_decision == original_decision

    def test_decision_field_descriptions(self) -> None:
        """Test that field descriptions are properly set."""
        fields = DominoesPlayerDecision.model_fields

        assert "move" in fields
        assert "pass_turn" in fields
        assert "reasoning" in fields

        assert "domino move to make" in fields["move"].description
        assert "whether to pass" in fields["pass_turn"].description
        assert "explanation" in fields["reasoning"].description
