"""Tests for Fox and Geese models with real component validation.

This module provides comprehensive tests for Fox and Geese models including:
    - Position validation and representation
    - Move validation and constraints
    - Game analysis structures
    - Data model boundaries and edge cases

All tests use real components without mocks, following the no-mocks methodology.
"""

from pydantic import ValidationError
import pytest

from haive.games.fox_and_geese.models import (
    FoxAndGeeseAnalysis,
    FoxAndGeeseMove,
    FoxAndGeesePosition,
)


class TestFoxAndGeesePosition:
    """Test suite for FoxAndGeesePosition model with real validation."""

    def test_fox_and_geese_position_creation_valid_coordinates(self):
        """Test FoxAndGeesePosition creation with valid coordinates."""
        # Test all corners and center positions
        valid_positions = [
            (0, 0),  # Top-left
            (0, 6),  # Top-right
            (6, 0),  # Bottom-left
            (6, 6),  # Bottom-right
            (3, 3),  # Center
            (2, 4),  # Middle area
        ]

        for row, col in valid_positions:
            position = FoxAndGeesePosition(row=row, col=col)
            assert position.row == row
            assert position.col == col

    def test_fox_and_geese_position_validation_negative_coordinates(self):
        """Test FoxAndGeesePosition validation rejects negative coordinates."""
        # Negative row
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=-1, col=3)
        assert "greater than or equal to 0" in str(exc_info.value)

        # Negative column
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=3, col=-1)
        assert "greater than or equal to 0" in str(exc_info.value)

        # Both negative
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=-1, col=-1)
        assert "greater than or equal to 0" in str(exc_info.value)

    def test_fox_and_geese_position_validation_high_coordinates(self):
        """Test FoxAndGeesePosition validation rejects coordinates above 6."""
        # High row
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=7, col=3)
        assert "less than or equal to 6" in str(exc_info.value)

        # High column
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=3, col=7)
        assert "less than or equal to 6" in str(exc_info.value)

        # Both high
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=7, col=7)
        assert "less than or equal to 6" in str(exc_info.value)

    def test_fox_and_geese_position_validation_extreme_coordinates(self):
        """Test FoxAndGeesePosition validation with extreme values."""
        # Very high values
        with pytest.raises(ValidationError):
            FoxAndGeesePosition(row=100, col=3)

        with pytest.raises(ValidationError):
            FoxAndGeesePosition(row=3, col=100)

        # Very negative values
        with pytest.raises(ValidationError):
            FoxAndGeesePosition(row=-100, col=3)

        with pytest.raises(ValidationError):
            FoxAndGeesePosition(row=3, col=-100)

    def test_fox_and_geese_position_validation_float_coordinates(self):
        """Test FoxAndGeesePosition validation rejects float coordinates."""
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=3.5, col=3)
        assert "Input should be a valid integer" in str(exc_info.value)

        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=3, col=3.5)
        assert "Input should be a valid integer" in str(exc_info.value)

    def test_fox_and_geese_position_validation_string_coordinates(self):
        """Test FoxAndGeesePosition validation rejects string coordinates."""
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row="3", col=3)
        assert "Input should be a valid integer" in str(exc_info.value)

        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeesePosition(row=3, col="3")
        assert "Input should be a valid integer" in str(exc_info.value)

    def test_fox_and_geese_position_equality_comparison(self):
        """Test FoxAndGeesePosition equality comparison."""
        pos1 = FoxAndGeesePosition(row=3, col=3)
        pos2 = FoxAndGeesePosition(row=3, col=3)
        pos3 = FoxAndGeesePosition(row=3, col=4)
        pos4 = FoxAndGeesePosition(row=4, col=3)

        assert pos1 == pos2
        assert pos1 != pos3
        assert pos1 != pos4
        assert pos3 != pos4

    def test_fox_and_geese_position_hash_functionality(self):
        """Test FoxAndGeesePosition can be used as dictionary key."""
        pos1 = FoxAndGeesePosition(row=3, col=3)
        pos2 = FoxAndGeesePosition(row=3, col=3)
        pos3 = FoxAndGeesePosition(row=3, col=4)

        # Should be hashable for use in sets/dicts
        position_set = {pos1, pos2, pos3}
        assert len(position_set) == 2  # pos1 and pos2 are equal

        position_dict = {pos1: "fox", pos3: "goose"}
        assert position_dict[pos2] == "fox"  # pos2 equals pos1

    def test_fox_and_geese_position_serialization(self):
        """Test FoxAndGeesePosition serialization to dictionary."""
        position = FoxAndGeesePosition(row=3, col=4)
        position_dict = position.model_dump()

        assert position_dict["row"] == 3
        assert position_dict["col"] == 4

    def test_fox_and_geese_position_deserialization(self):
        """Test FoxAndGeesePosition deserialization from dictionary."""
        position_dict = {"row": 3, "col": 4}
        position = FoxAndGeesePosition(**position_dict)

        assert position.row == 3
        assert position.col == 4


class TestFoxAndGeeseMove:
    """Test suite for FoxAndGeeseMove model with real validation."""

    def test_fox_and_geese_move_creation_basic(self):
        """Test FoxAndGeeseMove creation with basic positions."""
        from_pos = FoxAndGeesePosition(row=3, col=3)
        to_pos = FoxAndGeesePosition(row=3, col=4)

        move = FoxAndGeeseMove(from_position=from_pos, to_position=to_pos)

        assert move.from_position == from_pos
        assert move.to_position == to_pos
        assert move.explanation is None

    def test_fox_and_geese_move_creation_with_explanation(self):
        """Test FoxAndGeeseMove creation with explanation."""
        from_pos = FoxAndGeesePosition(row=3, col=3)
        to_pos = FoxAndGeesePosition(row=3, col=4)
        explanation = "Fox moves to escape goose pressure"

        move = FoxAndGeeseMove(
            from_position=from_pos, to_position=to_pos, explanation=explanation
        )

        assert move.from_position == from_pos
        assert move.to_position == to_pos
        assert move.explanation == explanation

    def test_fox_and_geese_move_validation_missing_required_fields(self):
        """Test FoxAndGeeseMove validation requires all mandatory fields."""
        from_pos = FoxAndGeesePosition(row=3, col=3)
        to_pos = FoxAndGeesePosition(row=3, col=4)

        # Missing from_position
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeeseMove(to_position=to_pos)
        assert "Field required" in str(exc_info.value)

        # Missing to_position
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeeseMove(from_position=from_pos)
        assert "Field required" in str(exc_info.value)

    def test_fox_and_geese_move_validation_same_positions(self):
        """Test FoxAndGeeseMove with identical from and to positions."""
        same_pos = FoxAndGeesePosition(row=3, col=3)

        # Should be allowed (validation logic is in game rules, not model)
        move = FoxAndGeeseMove(from_position=same_pos, to_position=same_pos)

        assert move.from_position == same_pos
        assert move.to_position == same_pos

    def test_fox_and_geese_move_edge_positions(self):
        """Test FoxAndGeeseMove with edge board positions."""
        # Corner to corner
        corner1 = FoxAndGeesePosition(row=0, col=0)
        corner2 = FoxAndGeesePosition(row=6, col=6)

        move = FoxAndGeeseMove(from_position=corner1, to_position=corner2)

        assert move.from_position == corner1
        assert move.to_position == corner2

    def test_fox_and_geese_move_all_board_positions(self):
        """Test FoxAndGeeseMove with various board positions."""
        positions = [
            FoxAndGeesePosition(row=0, col=0),  # Top-left
            FoxAndGeesePosition(row=0, col=6),  # Top-right
            FoxAndGeesePosition(row=6, col=0),  # Bottom-left
            FoxAndGeesePosition(row=6, col=6),  # Bottom-right
            FoxAndGeesePosition(row=3, col=3),  # Center
        ]

        # Test moves between all combinations
        for from_pos in positions:
            for to_pos in positions:
                move = FoxAndGeeseMove(from_position=from_pos, to_position=to_pos)
                assert move.from_position == from_pos
                assert move.to_position == to_pos

    def test_fox_and_geese_move_equality_comparison(self):
        """Test FoxAndGeeseMove equality comparison."""
        from_pos = FoxAndGeesePosition(row=3, col=3)
        to_pos = FoxAndGeesePosition(row=3, col=4)

        move1 = FoxAndGeeseMove(from_position=from_pos, to_position=to_pos)
        move2 = FoxAndGeeseMove(from_position=from_pos, to_position=to_pos)
        move3 = FoxAndGeeseMove(
            from_position=from_pos,
            to_position=to_pos,
            explanation="Different explanation",
        )

        assert move1 == move2
        assert move1 != move3  # Different explanations

    def test_fox_and_geese_move_serialization(self):
        """Test FoxAndGeeseMove serialization to dictionary."""
        from_pos = FoxAndGeesePosition(row=3, col=3)
        to_pos = FoxAndGeesePosition(row=4, col=4)
        explanation = "Diagonal move"

        move = FoxAndGeeseMove(
            from_position=from_pos, to_position=to_pos, explanation=explanation
        )

        move_dict = move.model_dump()

        assert move_dict["from_position"]["row"] == 3
        assert move_dict["from_position"]["col"] == 3
        assert move_dict["to_position"]["row"] == 4
        assert move_dict["to_position"]["col"] == 4
        assert move_dict["explanation"] == explanation

    def test_fox_and_geese_move_deserialization(self):
        """Test FoxAndGeeseMove deserialization from dictionary."""
        move_dict = {
            "from_position": {"row": 3, "col": 3},
            "to_position": {"row": 4, "col": 4},
            "explanation": "Diagonal move",
        }

        move = FoxAndGeeseMove(**move_dict)

        assert move.from_position.row == 3
        assert move.from_position.col == 3
        assert move.to_position.row == 4
        assert move.to_position.col == 4
        assert move.explanation == "Diagonal move"


class TestFoxAndGeeseAnalysis:
    """Test suite for FoxAndGeeseAnalysis model with real validation."""

    def test_fox_and_geese_analysis_creation_with_defaults(self):
        """Test FoxAndGeeseAnalysis creation with default values."""
        analysis = FoxAndGeeseAnalysis()

        assert analysis.position_eval == "balanced"
        assert analysis.fox_escape_routes == []
        assert analysis.goose_pressure_zones == []
        assert analysis.suggested_moves == []
        assert analysis.winning_probability == 50

    def test_fox_and_geese_analysis_creation_with_custom_values(self):
        """Test FoxAndGeeseAnalysis creation with custom values."""
        fox_routes = [
            FoxAndGeesePosition(row=3, col=4),
            FoxAndGeesePosition(row=4, col=3),
        ]
        pressure_zones = [
            FoxAndGeesePosition(row=2, col=3),
            FoxAndGeesePosition(row=3, col=2),
        ]
        moves = [
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=3),
                to_position=FoxAndGeesePosition(row=3, col=4),
            )
        ]

        analysis = FoxAndGeeseAnalysis(
            position_eval="fox_advantage",
            fox_escape_routes=fox_routes,
            goose_pressure_zones=pressure_zones,
            suggested_moves=moves,
            winning_probability=75,
        )

        assert analysis.position_eval == "fox_advantage"
        assert analysis.fox_escape_routes == fox_routes
        assert analysis.goose_pressure_zones == pressure_zones
        assert analysis.suggested_moves == moves
        assert analysis.winning_probability == 75

    def test_fox_and_geese_analysis_winning_probability_validation_valid_range(self):
        """Test FoxAndGeeseAnalysis winning probability validation accepts valid range."""
        # Test boundary values
        analysis_min = FoxAndGeeseAnalysis(winning_probability=0)
        assert analysis_min.winning_probability == 0

        analysis_max = FoxAndGeeseAnalysis(winning_probability=100)
        assert analysis_max.winning_probability == 100

        # Test middle values
        analysis_mid = FoxAndGeeseAnalysis(winning_probability=50)
        assert analysis_mid.winning_probability == 50

    def test_fox_and_geese_analysis_winning_probability_validation_invalid_negative(
        self,
    ):
        """Test FoxAndGeeseAnalysis winning probability validation rejects negative values."""
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeeseAnalysis(winning_probability=-1)

        assert "greater than or equal to 0" in str(exc_info.value)

    def test_fox_and_geese_analysis_winning_probability_validation_invalid_high(self):
        """Test FoxAndGeeseAnalysis winning probability validation rejects values above 100."""
        with pytest.raises(ValidationError) as exc_info:
            FoxAndGeeseAnalysis(winning_probability=101)

        assert "less than or equal to 100" in str(exc_info.value)

    def test_fox_and_geese_analysis_default_list_factories(self):
        """Test FoxAndGeeseAnalysis default list factories create separate instances."""
        analysis1 = FoxAndGeeseAnalysis()
        analysis2 = FoxAndGeeseAnalysis()

        # Modify one instance
        analysis1.fox_escape_routes.append(FoxAndGeesePosition(row=3, col=3))
        analysis1.goose_pressure_zones.append(FoxAndGeesePosition(row=2, col=2))

        # Other instance should not be affected
        assert analysis2.fox_escape_routes == []
        assert analysis2.goose_pressure_zones == []
        assert len(analysis1.fox_escape_routes) == 1
        assert len(analysis1.goose_pressure_zones) == 1

    def test_fox_and_geese_analysis_complex_scenario(self):
        """Test FoxAndGeeseAnalysis with complex game scenario."""
        # Create a complex analysis scenario
        fox_routes = [
            FoxAndGeesePosition(row=3, col=4),  # Right escape
            FoxAndGeesePosition(row=4, col=3),  # Down escape
            FoxAndGeesePosition(row=2, col=3),  # Up escape
        ]

        pressure_zones = [
            FoxAndGeesePosition(row=1, col=1),
            FoxAndGeesePosition(row=1, col=3),
            FoxAndGeesePosition(row=1, col=5),
        ]

        suggested_moves = [
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=3),
                to_position=FoxAndGeesePosition(row=3, col=4),
                explanation="Best escape route",
            ),
            FoxAndGeeseMove(
                from_position=FoxAndGeesePosition(row=3, col=3),
                to_position=FoxAndGeesePosition(row=4, col=3),
                explanation="Alternative escape",
            ),
        ]

        analysis = FoxAndGeeseAnalysis(
            position_eval="complex_scenario",
            fox_escape_routes=fox_routes,
            goose_pressure_zones=pressure_zones,
            suggested_moves=suggested_moves,
            winning_probability=45,
        )

        assert len(analysis.fox_escape_routes) == 3
        assert len(analysis.goose_pressure_zones) == 3
        assert len(analysis.suggested_moves) == 2
        assert analysis.winning_probability == 45

    def test_fox_and_geese_analysis_serialization(self):
        """Test FoxAndGeeseAnalysis serialization to dictionary."""
        fox_route = FoxAndGeesePosition(row=3, col=4)
        pressure_zone = FoxAndGeesePosition(row=2, col=3)
        move = FoxAndGeeseMove(
            from_position=FoxAndGeesePosition(row=3, col=3),
            to_position=FoxAndGeesePosition(row=3, col=4),
        )

        analysis = FoxAndGeeseAnalysis(
            position_eval="test_scenario",
            fox_escape_routes=[fox_route],
            goose_pressure_zones=[pressure_zone],
            suggested_moves=[move],
            winning_probability=65,
        )

        analysis_dict = analysis.model_dump()

        assert analysis_dict["position_eval"] == "test_scenario"
        assert len(analysis_dict["fox_escape_routes"]) == 1
        assert analysis_dict["fox_escape_routes"][0]["row"] == 3
        assert analysis_dict["fox_escape_routes"][0]["col"] == 4
        assert len(analysis_dict["goose_pressure_zones"]) == 1
        assert len(analysis_dict["suggested_moves"]) == 1
        assert analysis_dict["winning_probability"] == 65

    def test_fox_and_geese_analysis_deserialization(self):
        """Test FoxAndGeeseAnalysis deserialization from dictionary."""
        analysis_dict = {
            "position_eval": "test_scenario",
            "fox_escape_routes": [{"row": 3, "col": 4}],
            "goose_pressure_zones": [{"row": 2, "col": 3}],
            "suggested_moves": [
                {
                    "from_position": {"row": 3, "col": 3},
                    "to_position": {"row": 3, "col": 4},
                    "explanation": "Test move",
                }
            ],
            "winning_probability": 65,
        }

        analysis = FoxAndGeeseAnalysis(**analysis_dict)

        assert analysis.position_eval == "test_scenario"
        assert len(analysis.fox_escape_routes) == 1
        assert analysis.fox_escape_routes[0].row == 3
        assert analysis.fox_escape_routes[0].col == 4
        assert len(analysis.goose_pressure_zones) == 1
        assert analysis.goose_pressure_zones[0].row == 2
        assert len(analysis.suggested_moves) == 1
        assert analysis.suggested_moves[0].explanation == "Test move"
        assert analysis.winning_probability == 65

    def test_fox_and_geese_analysis_empty_lists(self):
        """Test FoxAndGeeseAnalysis handles empty lists correctly."""
        analysis = FoxAndGeeseAnalysis(
            fox_escape_routes=[], goose_pressure_zones=[], suggested_moves=[]
        )

        assert analysis.fox_escape_routes == []
        assert analysis.goose_pressure_zones == []
        assert analysis.suggested_moves == []
        assert isinstance(analysis.fox_escape_routes, list)
        assert isinstance(analysis.goose_pressure_zones, list)
        assert isinstance(analysis.suggested_moves, list)

    def test_fox_and_geese_analysis_position_eval_variations(self):
        """Test FoxAndGeeseAnalysis with various position evaluation strings."""
        eval_strings = [
            "fox_advantage",
            "goose_advantage",
            "balanced",
            "critical_position",
            "endgame_scenario",
            "complex_tactical_situation",
        ]

        for eval_str in eval_strings:
            analysis = FoxAndGeeseAnalysis(position_eval=eval_str)
            assert analysis.position_eval == eval_str
