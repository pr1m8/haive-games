"""Tests for Connect4 models with real component validation.

This module provides comprehensive tests for Connect4 models including:
    - Move validation and representation
    - Player decision structures
    - Position analysis models
    - Data model constraints and validation

All tests use real components without mocks, following the no-mocks methodology.
"""

from pydantic import ValidationError
import pytest

from haive.games.connect4.models import (
    Connect4Analysis,
    Connect4Move,
    Connect4PlayerDecision,
)


class TestConnect4Move:
    """Test suite for Connect4Move model with real validation."""

    def test_connect4_move_creation_valid_columns(self):
        """Test Connect4Move creation with valid column numbers."""
        # Test all valid columns (0-6)
        for col in range(7):
            move = Connect4Move(column=col)
            assert move.column == col
            assert move.explanation is None

    def test_connect4_move_creation_with_explanation(self):
        """Test Connect4Move creation with explanation."""
        move = Connect4Move(column=3, explanation="Control the center")
        assert move.column == 3
        assert move.explanation == "Control the center"

    def test_connect4_move_validation_invalid_negative_column(self):
        """Test Connect4Move validation rejects negative column numbers."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Move(column=-1)

        assert "Column must be an integer between 0 and 6" in str(exc_info.value)

    def test_connect4_move_validation_invalid_high_column(self):
        """Test Connect4Move validation rejects column numbers above 6."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Move(column=7)

        assert "Column must be an integer between 0 and 6" in str(exc_info.value)

    def test_connect4_move_validation_invalid_high_column_extreme(self):
        """Test Connect4Move validation rejects extreme high column numbers."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Move(column=100)

        assert "Column must be an integer between 0 and 6" in str(exc_info.value)

    def test_connect4_move_validation_invalid_float_column(self):
        """Test Connect4Move validation rejects float column numbers."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Move(column=3.5)

        assert "Column must be an integer between 0 and 6" in str(exc_info.value)

    def test_connect4_move_validation_invalid_string_column(self):
        """Test Connect4Move validation rejects string column numbers."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Move(column="3")

        # ValidationError should occur for type mismatch
        assert "Input should be a valid integer" in str(exc_info.value)

    def test_connect4_move_string_representation(self):
        """Test Connect4Move string representation is correct."""
        move = Connect4Move(column=3)
        assert str(move) == "Drop in column 3"

        move = Connect4Move(column=0)
        assert str(move) == "Drop in column 0"

        move = Connect4Move(column=6)
        assert str(move) == "Drop in column 6"

    def test_connect4_move_string_representation_with_explanation(self):
        """Test Connect4Move string representation ignores explanation."""
        move = Connect4Move(column=3, explanation="Strategic center play")
        assert str(move) == "Drop in column 3"

    def test_connect4_move_equality_comparison(self):
        """Test Connect4Move equality comparison between instances."""
        move1 = Connect4Move(column=3)
        move2 = Connect4Move(column=3)
        move3 = Connect4Move(column=4)

        assert move1 == move2
        assert move1 != move3

    def test_connect4_move_equality_with_explanation(self):
        """Test Connect4Move equality includes explanation in comparison."""
        move1 = Connect4Move(column=3, explanation="Center control")
        move2 = Connect4Move(column=3, explanation="Center control")
        move3 = Connect4Move(column=3, explanation="Different reason")
        move4 = Connect4Move(column=3)

        assert move1 == move2
        assert move1 != move3
        assert move1 != move4

    def test_connect4_move_serialization(self):
        """Test Connect4Move serialization to dictionary."""
        move = Connect4Move(column=3, explanation="Strategic play")
        move_dict = move.model_dump()

        assert move_dict["column"] == 3
        assert move_dict["explanation"] == "Strategic play"

    def test_connect4_move_deserialization(self):
        """Test Connect4Move deserialization from dictionary."""
        move_dict = {"column": 3, "explanation": "Strategic play"}
        move = Connect4Move(**move_dict)

        assert move.column == 3
        assert move.explanation == "Strategic play"


class TestConnect4PlayerDecision:
    """Test suite for Connect4PlayerDecision model with real validation."""

    def test_connect4_player_decision_creation_minimal(self):
        """Test Connect4PlayerDecision creation with minimal required fields."""
        move = Connect4Move(column=3, explanation="Control center")
        decision = Connect4PlayerDecision(
            move=move,
            position_eval="Strong position",
            reasoning="Center control is crucial",
        )

        assert decision.move == move
        assert decision.position_eval == "Strong position"
        assert decision.reasoning == "Center control is crucial"
        assert decision.alternatives == []

    def test_connect4_player_decision_creation_with_alternatives(self):
        """Test Connect4PlayerDecision creation with alternative moves."""
        main_move = Connect4Move(column=3, explanation="Control center")
        alt_move_1 = Connect4Move(column=2, explanation="Left side approach")
        alt_move_2 = Connect4Move(column=4, explanation="Right side approach")

        decision = Connect4PlayerDecision(
            move=main_move,
            position_eval="Multiple good options",
            alternatives=[alt_move_1, alt_move_2],
            reasoning="Center is best but sides are viable",
        )

        assert decision.move == main_move
        assert len(decision.alternatives) == 2
        assert decision.alternatives[0] == alt_move_1
        assert decision.alternatives[1] == alt_move_2

    def test_connect4_player_decision_validation_missing_required_fields(self):
        """Test Connect4PlayerDecision validation requires all mandatory fields."""
        move = Connect4Move(column=3)

        # Missing position_eval
        with pytest.raises(ValidationError) as exc_info:
            Connect4PlayerDecision(move=move, reasoning="Some reasoning")
        assert "Field required" in str(exc_info.value)

        # Missing reasoning
        with pytest.raises(ValidationError) as exc_info:
            Connect4PlayerDecision(move=move, position_eval="Good position")
        assert "Field required" in str(exc_info.value)

        # Missing move
        with pytest.raises(ValidationError) as exc_info:
            Connect4PlayerDecision(
                position_eval="Good position", reasoning="Some reasoning"
            )
        assert "Field required" in str(exc_info.value)

    def test_connect4_player_decision_serialization(self):
        """Test Connect4PlayerDecision serialization to dictionary."""
        move = Connect4Move(column=3, explanation="Center control")
        alt_move = Connect4Move(column=2, explanation="Alternative")

        decision = Connect4PlayerDecision(
            move=move,
            position_eval="Strong position",
            alternatives=[alt_move],
            reasoning="Center control strategy",
        )

        decision_dict = decision.model_dump()

        assert decision_dict["move"]["column"] == 3
        assert decision_dict["position_eval"] == "Strong position"
        assert len(decision_dict["alternatives"]) == 1
        assert decision_dict["alternatives"][0]["column"] == 2
        assert decision_dict["reasoning"] == "Center control strategy"

    def test_connect4_player_decision_deserialization(self):
        """Test Connect4PlayerDecision deserialization from dictionary."""
        decision_dict = {
            "move": {"column": 3, "explanation": "Center control"},
            "position_eval": "Strong position",
            "alternatives": [{"column": 2, "explanation": "Alternative"}],
            "reasoning": "Center control strategy",
        }

        decision = Connect4PlayerDecision(**decision_dict)

        assert decision.move.column == 3
        assert decision.position_eval == "Strong position"
        assert len(decision.alternatives) == 1
        assert decision.alternatives[0].column == 2
        assert decision.reasoning == "Center control strategy"


class TestConnect4Analysis:
    """Test suite for Connect4Analysis model with real validation."""

    def test_connect4_analysis_creation_with_defaults(self):
        """Test Connect4Analysis creation with default values."""
        analysis = Connect4Analysis()

        assert analysis.position_score == 0.0
        assert analysis.center_control == 5
        assert analysis.threats == {"winning_moves": [], "blocking_moves": []}
        assert analysis.suggested_columns == []
        assert analysis.winning_chances == 50

    def test_connect4_analysis_creation_with_custom_values(self):
        """Test Connect4Analysis creation with custom values."""
        analysis = Connect4Analysis(
            position_score=0.7,
            center_control=8,
            threats={"winning_moves": [3], "blocking_moves": [4, 5]},
            suggested_columns=[3, 2, 4],
            winning_chances=75,
        )

        assert analysis.position_score == 0.7
        assert analysis.center_control == 8
        assert analysis.threats["winning_moves"] == [3]
        assert analysis.threats["blocking_moves"] == [4, 5]
        assert analysis.suggested_columns == [3, 2, 4]
        assert analysis.winning_chances == 75

    def test_connect4_analysis_center_control_validation_valid_range(self):
        """Test Connect4Analysis center control validation accepts valid range."""
        # Test boundary values
        analysis_min = Connect4Analysis(center_control=0)
        assert analysis_min.center_control == 0

        analysis_max = Connect4Analysis(center_control=10)
        assert analysis_max.center_control == 10

        # Test middle values
        analysis_mid = Connect4Analysis(center_control=5)
        assert analysis_mid.center_control == 5

    def test_connect4_analysis_center_control_validation_invalid_negative(self):
        """Test Connect4Analysis center control validation rejects negative values."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Analysis(center_control=-1)

        assert "Center control must be an integer between 0 and 10" in str(
            exc_info.value
        )

    def test_connect4_analysis_center_control_validation_invalid_high(self):
        """Test Connect4Analysis center control validation rejects values above 10."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Analysis(center_control=11)

        assert "Center control must be an integer between 0 and 10" in str(
            exc_info.value
        )

    def test_connect4_analysis_center_control_validation_invalid_float(self):
        """Test Connect4Analysis center control validation rejects float values."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Analysis(center_control=5.5)

        assert "Center control must be an integer between 0 and 10" in str(
            exc_info.value
        )

    def test_connect4_analysis_winning_chances_validation_valid_range(self):
        """Test Connect4Analysis winning chances validation accepts valid range."""
        # Test boundary values
        analysis_min = Connect4Analysis(winning_chances=0)
        assert analysis_min.winning_chances == 0

        analysis_max = Connect4Analysis(winning_chances=100)
        assert analysis_max.winning_chances == 100

        # Test middle values
        analysis_mid = Connect4Analysis(winning_chances=50)
        assert analysis_mid.winning_chances == 50

    def test_connect4_analysis_winning_chances_validation_invalid_negative(self):
        """Test Connect4Analysis winning chances validation rejects negative values."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Analysis(winning_chances=-1)

        assert "Winning chances must be an integer between 0 and 100" in str(
            exc_info.value
        )

    def test_connect4_analysis_winning_chances_validation_invalid_high(self):
        """Test Connect4Analysis winning chances validation rejects values above 100."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Analysis(winning_chances=101)

        assert "Winning chances must be an integer between 0 and 100" in str(
            exc_info.value
        )

    def test_connect4_analysis_winning_chances_validation_invalid_float(self):
        """Test Connect4Analysis winning chances validation rejects float values."""
        with pytest.raises(ValidationError) as exc_info:
            Connect4Analysis(winning_chances=50.5)

        assert "Winning chances must be an integer between 0 and 100" in str(
            exc_info.value
        )

    def test_connect4_analysis_default_threats_factory(self):
        """Test Connect4Analysis default threats factory creates separate instances."""
        analysis1 = Connect4Analysis()
        analysis2 = Connect4Analysis()

        # Modify one instance
        analysis1.threats["winning_moves"].append(3)

        # Other instance should not be affected
        assert analysis2.threats["winning_moves"] == []
        assert analysis1.threats["winning_moves"] == [3]

    def test_connect4_analysis_default_suggested_columns_factory(self):
        """Test Connect4Analysis default suggested columns factory creates separate instances."""
        analysis1 = Connect4Analysis()
        analysis2 = Connect4Analysis()

        # Modify one instance
        analysis1.suggested_columns.append(3)

        # Other instance should not be affected
        assert analysis2.suggested_columns == []
        assert analysis1.suggested_columns == [3]

    def test_connect4_analysis_position_score_range(self):
        """Test Connect4Analysis position score accepts valid range."""
        # Test negative values (opponent favored)
        analysis_neg = Connect4Analysis(position_score=-1.0)
        assert analysis_neg.position_score == -1.0

        # Test positive values (current player favored)
        analysis_pos = Connect4Analysis(position_score=1.0)
        assert analysis_pos.position_score == 1.0

        # Test zero (equal position)
        analysis_zero = Connect4Analysis(position_score=0.0)
        assert analysis_zero.position_score == 0.0

    def test_connect4_analysis_serialization(self):
        """Test Connect4Analysis serialization to dictionary."""
        analysis = Connect4Analysis(
            position_score=0.5,
            center_control=7,
            threats={"winning_moves": [3], "blocking_moves": [4]},
            suggested_columns=[3, 2, 4],
            winning_chances=65,
        )

        analysis_dict = analysis.model_dump()

        assert analysis_dict["position_score"] == 0.5
        assert analysis_dict["center_control"] == 7
        assert analysis_dict["threats"]["winning_moves"] == [3]
        assert analysis_dict["threats"]["blocking_moves"] == [4]
        assert analysis_dict["suggested_columns"] == [3, 2, 4]
        assert analysis_dict["winning_chances"] == 65

    def test_connect4_analysis_deserialization(self):
        """Test Connect4Analysis deserialization from dictionary."""
        analysis_dict = {
            "position_score": 0.5,
            "center_control": 7,
            "threats": {"winning_moves": [3], "blocking_moves": [4]},
            "suggested_columns": [3, 2, 4],
            "winning_chances": 65,
        }

        analysis = Connect4Analysis(**analysis_dict)

        assert analysis.position_score == 0.5
        assert analysis.center_control == 7
        assert analysis.threats["winning_moves"] == [3]
        assert analysis.threats["blocking_moves"] == [4]
        assert analysis.suggested_columns == [3, 2, 4]
        assert analysis.winning_chances == 65

    def test_connect4_analysis_custom_threats_structure(self):
        """Test Connect4Analysis accepts custom threats structure."""
        custom_threats = {
            "winning_moves": [1, 2, 3],
            "blocking_moves": [4, 5],
            "fork_opportunities": [6],
        }

        analysis = Connect4Analysis(threats=custom_threats)

        assert analysis.threats["winning_moves"] == [1, 2, 3]
        assert analysis.threats["blocking_moves"] == [4, 5]
        assert analysis.threats["fork_opportunities"] == [6]

    def test_connect4_analysis_empty_suggested_columns(self):
        """Test Connect4Analysis handles empty suggested columns correctly."""
        analysis = Connect4Analysis(suggested_columns=[])

        assert analysis.suggested_columns == []
        assert isinstance(analysis.suggested_columns, list)

    def test_connect4_analysis_duplicate_suggested_columns(self):
        """Test Connect4Analysis accepts duplicate suggested columns."""
        analysis = Connect4Analysis(suggested_columns=[3, 3, 4, 4])

        assert analysis.suggested_columns == [3, 3, 4, 4]
