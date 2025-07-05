"""Test cases for Checkers game models.

This module tests all the data models and classes used in the Checkers game,
ensuring they behave correctly and validate input properly.
"""

import pytest
from pydantic import ValidationError

from haive.games.checkers.models import (
    CheckersAnalysis,
    CheckersMove,
    CheckersPlayerDecision,
)


class TestCheckersMove:
    """Test cases for CheckersMove model."""

    def test_checkers_move_creation_regular(self) -> None:
        """Test creating a regular checkers move."""
        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
            is_jump=False,
        )

        assert move.from_position == "a3"
        assert move.to_position == "b4"
        assert move.player == "red"
        assert move.is_jump is False
        assert move.captured_position is None

    def test_checkers_move_creation_jump(self) -> None:
        """Test creating a jump move."""
        move = CheckersMove(
            from_position="c3",
            to_position="e5",
            player="black",
            is_jump=True,
            captured_position="d4",
        )

        assert move.from_position == "c3"
        assert move.to_position == "e5"
        assert move.player == "black"
        assert move.is_jump is True
        assert move.captured_position == "d4"

    def test_checkers_move_default_values(self) -> None:
        """Test that default values are set correctly."""
        move = CheckersMove(
            from_position="e3",
            to_position="f4",
            player="red",
        )

        assert move.is_jump is False  # Default value
        assert move.captured_position is None  # Default value

    def test_checkers_move_string_representation_regular(self) -> None:
        """Test string representation of regular move."""
        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
            is_jump=False,
        )

        assert str(move) == "a3-b4"

    def test_checkers_move_string_representation_jump(self) -> None:
        """Test string representation of jump move."""
        move = CheckersMove(
            from_position="c3",
            to_position="e5",
            player="black",
            is_jump=True,
            captured_position="d4",
        )

        assert str(move) == "c3xe5"

    def test_checkers_move_invalid_player(self) -> None:
        """Test that invalid player values raise validation error."""
        with pytest.raises(ValidationError):
            CheckersMove(
                from_position="a3",
                to_position="b4",
                player="blue",  # Invalid player
            )

    def test_checkers_move_red_player(self) -> None:
        """Test creating move with red player."""
        move = CheckersMove(
            from_position="g3",
            to_position="h4",
            player="red",
        )

        assert move.player == "red"

    def test_checkers_move_black_player(self) -> None:
        """Test creating move with black player."""
        move = CheckersMove(
            from_position="b6",
            to_position="a5",
            player="black",
        )

        assert move.player == "black"

    def test_checkers_move_edge_positions(self) -> None:
        """Test moves involving edge positions."""
        # Corner to adjacent
        move1 = CheckersMove(
            from_position="a1",
            to_position="b2",
            player="red",
        )
        assert move1.from_position == "a1"
        assert move1.to_position == "b2"

        # Edge positions
        move2 = CheckersMove(
            from_position="h8",
            to_position="g7",
            player="black",
        )
        assert move2.from_position == "h8"
        assert move2.to_position == "g7"

    def test_checkers_move_jump_without_captured_position(self) -> None:
        """Test jump move without specifying captured position."""
        move = CheckersMove(
            from_position="c3",
            to_position="e5",
            player="red",
            is_jump=True,
            # captured_position not specified
        )

        assert move.is_jump is True
        assert move.captured_position is None

    def test_checkers_move_multiple_positions(self) -> None:
        """Test various position combinations."""
        positions = [
            ("a1", "b2"),
            ("b2", "c3"),
            ("c3", "d4"),
            ("d4", "e5"),
            ("e5", "f6"),
            ("f6", "g7"),
            ("g7", "h8"),
            ("h6", "g5"),
        ]

        for from_pos, to_pos in positions:
            move = CheckersMove(
                from_position=from_pos,
                to_position=to_pos,
                player="red",
            )
            assert move.from_position == from_pos
            assert move.to_position == to_pos


class TestCheckersPlayerDecision:
    """Test cases for CheckersPlayerDecision model."""

    def test_checkers_player_decision_creation(self) -> None:
        """Test creating a player decision."""
        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )

        decision = CheckersPlayerDecision(
            move=move,
            reasoning="Developing a piece toward the center",
            evaluation="Slightly better position with center control",
            alternatives=["c3-d4", "e3-f4"],
        )

        assert decision.move == move
        assert "center" in decision.reasoning.lower()
        assert "control" in decision.evaluation.lower()
        assert len(decision.alternatives) == 2
        assert "c3-d4" in decision.alternatives
        assert "e3-f4" in decision.alternatives

    def test_checkers_player_decision_empty_alternatives(self) -> None:
        """Test player decision with no alternatives."""
        move = CheckersMove(
            from_position="f2",
            to_position="g3",
            player="black",
        )

        decision = CheckersPlayerDecision(
            move=move,
            reasoning="Only legal move available",
            evaluation="Forced move, maintaining position",
        )

        assert decision.move == move
        assert decision.alternatives == []  # Default empty list

    def test_checkers_player_decision_jump_move(self) -> None:
        """Test player decision with jump move."""
        jump_move = CheckersMove(
            from_position="c5",
            to_position="e7",
            player="red",
            is_jump=True,
            captured_position="d6",
        )

        decision = CheckersPlayerDecision(
            move=jump_move,
            reasoning="Mandatory capture available",
            evaluation="Material advantage gained",
            alternatives=[],
        )

        assert decision.move.is_jump is True
        assert decision.move.captured_position == "d6"
        assert "capture" in decision.reasoning.lower()
        assert "advantage" in decision.evaluation.lower()

    def test_checkers_player_decision_multiple_alternatives(self) -> None:
        """Test player decision with multiple alternatives."""
        move = CheckersMove(
            from_position="d2",
            to_position="e3",
            player="black",
        )

        alternatives = ["a3-b4", "c3-d4", "e3-f4", "g3-h4", "b2-c3"]

        decision = CheckersPlayerDecision(
            move=move,
            reasoning="Central advance seems strongest",
            evaluation="Good position with multiple options",
            alternatives=alternatives,
        )

        assert len(decision.alternatives) == 5
        assert all(alt in decision.alternatives for alt in alternatives)

    def test_checkers_player_decision_detailed_reasoning(self) -> None:
        """Test player decision with detailed reasoning."""
        move = CheckersMove(
            from_position="b4",
            to_position="c5",
            player="red",
        )

        detailed_reasoning = (
            "This move advances the piece toward the opponent's back rank "
            "while maintaining protection from the piece on a3. It also "
            "creates a potential fork threat if the opponent doesn't respond carefully."
        )

        detailed_evaluation = (
            "Red maintains a slight advantage with better piece activity "
            "and more advanced position. The center control is improving."
        )

        decision = CheckersPlayerDecision(
            move=move,
            reasoning=detailed_reasoning,
            evaluation=detailed_evaluation,
            alternatives=["a3-b4", "e3-f4"],
        )

        assert "back rank" in decision.reasoning
        assert "protection" in decision.reasoning
        assert "advantage" in decision.evaluation
        assert "activity" in decision.evaluation

    def test_checkers_player_decision_required_fields(self) -> None:
        """Test that required fields must be provided."""
        move = CheckersMove(
            from_position="a1",
            to_position="b2",
            player="red",
        )

        # All required fields provided - should work
        decision = CheckersPlayerDecision(
            move=move,
            reasoning="Test reasoning",
            evaluation="Test evaluation",
        )

        assert decision.move is not None
        assert decision.reasoning == "Test reasoning"
        assert decision.evaluation == "Test evaluation"

        # Missing reasoning - should fail
        with pytest.raises(ValidationError):
            CheckersPlayerDecision(
                move=move,
                evaluation="Test evaluation",
                # reasoning missing
            )

        # Missing evaluation - should fail
        with pytest.raises(ValidationError):
            CheckersPlayerDecision(
                move=move,
                reasoning="Test reasoning",
                # evaluation missing
            )


class TestCheckersAnalysis:
    """Test cases for CheckersAnalysis model."""

    def test_checkers_analysis_creation(self) -> None:
        """Test creating a checkers analysis."""
        analysis = CheckersAnalysis(
            material_advantage="Red has 12 pieces vs. Black's 10",
            control_of_center="Red controls 3 of 4 center squares",
            suggested_moves=["e3-f4", "c3-d4", "g3-h4"],
            positional_evaluation="Red has a strong position with material advantage",
        )

        assert "12 pieces" in analysis.material_advantage
        assert "3 of 4" in analysis.control_of_center
        assert len(analysis.suggested_moves) == 3
        assert "e3-f4" in analysis.suggested_moves
        assert "strong position" in analysis.positional_evaluation

    def test_checkers_analysis_empty_suggested_moves(self) -> None:
        """Test analysis with no suggested moves."""
        analysis = CheckersAnalysis(
            material_advantage="Equal material - 8 pieces each",
            control_of_center="Neither player controls the center",
            positional_evaluation="Balanced position with equal chances",
        )

        assert analysis.suggested_moves == []  # Default empty list
        assert "equal" in analysis.material_advantage.lower()

    def test_checkers_analysis_detailed_evaluation(self) -> None:
        """Test analysis with detailed evaluation."""
        analysis = CheckersAnalysis(
            material_advantage=(
                "Black has a significant material advantage with 11 pieces "
                "compared to Red's 7 pieces, including one Black king"
            ),
            control_of_center=(
                "Black completely dominates the center with pieces on d4, e5, "
                "and f4, while Red has no central presence"
            ),
            suggested_moves=["d4-e3", "e5-d6", "f4-g5", "b6-c7", "h6-g5"],
            positional_evaluation=(
                "Black is winning decisively with superior material, "
                "better piece activity, and complete center control. "
                "Red needs to find counterplay quickly."
            ),
        )

        assert "significant" in analysis.material_advantage
        assert "dominates" in analysis.control_of_center
        assert len(analysis.suggested_moves) == 5
        assert "winning decisively" in analysis.positional_evaluation

    def test_checkers_analysis_balanced_position(self) -> None:
        """Test analysis of a balanced position."""
        analysis = CheckersAnalysis(
            material_advantage="Equal material with 9 pieces each",
            control_of_center="Shared center control - each player has one central piece",
            suggested_moves=["c3-d4", "e3-f4", "g3-f4"],
            positional_evaluation="Balanced position with chances for both sides",
        )

        assert "equal" in analysis.material_advantage.lower()
        assert "shared" in analysis.control_of_center.lower()
        assert "balanced" in analysis.positional_evaluation.lower()

    def test_checkers_analysis_king_advantage(self) -> None:
        """Test analysis highlighting king advantage."""
        analysis = CheckersAnalysis(
            material_advantage=(
                "Red has 2 kings vs Black's 0 kings, though material count is equal at 6 pieces each"
            ),
            control_of_center="Red's kings control the center effectively",
            suggested_moves=["King-d4", "King-e5", "c3-d4"],
            positional_evaluation="Red's king advantage provides superior mobility and control",
        )

        assert "2 kings" in analysis.material_advantage
        assert "king" in analysis.control_of_center.lower()
        assert "King-" in analysis.suggested_moves[0]
        assert "mobility" in analysis.positional_evaluation

    def test_checkers_analysis_endgame_position(self) -> None:
        """Test analysis of an endgame position."""
        analysis = CheckersAnalysis(
            material_advantage="Red: 3 pieces (2 kings), Black: 2 pieces (1 king)",
            control_of_center="Limited relevance in endgame - focus on king activity",
            suggested_moves=["King-h8", "King-f6"],
            positional_evaluation="Red should win with careful play - advance kings methodically",
        )

        assert (
            "endgame" in analysis.control_of_center.lower()
            or "limited" in analysis.control_of_center.lower()
        )
        assert "should win" in analysis.positional_evaluation
        assert len(analysis.suggested_moves) == 2

    def test_checkers_analysis_tactical_position(self) -> None:
        """Test analysis of a tactical position."""
        analysis = CheckersAnalysis(
            material_advantage="Material equal but Red has tactical threats",
            control_of_center="Red's advanced pieces create tactical opportunities",
            suggested_moves=["c5xd6", "e5xf6", "g5-h6"],
            positional_evaluation="Sharp tactical position favoring Red with multiple threats",
        )

        assert "tactical" in analysis.material_advantage.lower()
        assert "opportunities" in analysis.control_of_center.lower()
        assert any("x" in move for move in analysis.suggested_moves)  # Capture notation
        assert "threats" in analysis.positional_evaluation.lower()

    def test_checkers_analysis_required_fields(self) -> None:
        """Test that all required fields must be provided."""
        # All fields provided - should work
        analysis = CheckersAnalysis(
            material_advantage="Test material",
            control_of_center="Test center control",
            suggested_moves=["a1-b2"],
            positional_evaluation="Test evaluation",
        )

        assert analysis.material_advantage == "Test material"

        # Missing material_advantage - should fail
        with pytest.raises(ValidationError):
            CheckersAnalysis(
                control_of_center="Test center control",
                suggested_moves=["a1-b2"],
                positional_evaluation="Test evaluation",
            )

        # Missing control_of_center - should fail
        with pytest.raises(ValidationError):
            CheckersAnalysis(
                material_advantage="Test material",
                suggested_moves=["a1-b2"],
                positional_evaluation="Test evaluation",
            )

        # Missing positional_evaluation - should fail
        with pytest.raises(ValidationError):
            CheckersAnalysis(
                material_advantage="Test material",
                control_of_center="Test center control",
                suggested_moves=["a1-b2"],
            )
