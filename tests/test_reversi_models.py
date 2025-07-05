"""Test cases for Reversi game models.

This module tests all the data models and classes used in the Reversi game,
ensuring they behave correctly and validate input properly.
"""

import pytest
from pydantic import ValidationError

from haive.games.reversi.models import Position, ReversiAnalysis, ReversiMove


class TestPosition:
    """Test cases for Position model."""

    def test_position_creation_valid(self) -> None:
        """Test creating a valid position."""
        position = Position(row=3, col=4)
        assert position.row == 3
        assert position.col == 4

    def test_position_creation_boundary_values(self) -> None:
        """Test creating positions at board boundaries."""
        # Test corners
        top_left = Position(row=0, col=0)
        assert top_left.row == 0
        assert top_left.col == 0

        bottom_right = Position(row=7, col=7)
        assert bottom_right.row == 7
        assert bottom_right.col == 7

    def test_position_creation_invalid_row(self) -> None:
        """Test that invalid row values raise validation error."""
        with pytest.raises(ValidationError):
            Position(row=-1, col=4)

        with pytest.raises(ValidationError):
            Position(row=8, col=4)

    def test_position_creation_invalid_col(self) -> None:
        """Test that invalid column values raise validation error."""
        with pytest.raises(ValidationError):
            Position(row=3, col=-1)

        with pytest.raises(ValidationError):
            Position(row=3, col=8)


class TestReversiMove:
    """Test cases for ReversiMove model."""

    def test_reversi_move_creation_valid(self) -> None:
        """Test creating a valid Reversi move."""
        move = ReversiMove(row=3, col=4, player="B")
        assert move.row == 3
        assert move.col == 4
        assert move.player == "B"

    def test_reversi_move_creation_white_player(self) -> None:
        """Test creating a move for white player."""
        move = ReversiMove(row=2, col=5, player="W")
        assert move.row == 2
        assert move.col == 5
        assert move.player == "W"

    def test_reversi_move_string_representation_black(self) -> None:
        """Test string representation of black move."""
        move = ReversiMove(row=0, col=0, player="B")
        expected = "B places at A1 (0, 0)"
        assert str(move) == expected

    def test_reversi_move_string_representation_white(self) -> None:
        """Test string representation of white move."""
        move = ReversiMove(row=7, col=7, player="W")
        expected = "W places at H8 (7, 7)"
        assert str(move) == expected

    def test_reversi_move_string_representation_middle(self) -> None:
        """Test string representation of move in middle of board."""
        move = ReversiMove(row=3, col=4, player="B")
        expected = "B places at D5 (3, 4)"
        assert str(move) == expected

    def test_reversi_move_invalid_row(self) -> None:
        """Test that invalid row values raise validation error."""
        with pytest.raises(ValidationError):
            ReversiMove(row=-1, col=4, player="B")

        with pytest.raises(ValidationError):
            ReversiMove(row=8, col=4, player="B")

    def test_reversi_move_invalid_col(self) -> None:
        """Test that invalid column values raise validation error."""
        with pytest.raises(ValidationError):
            ReversiMove(row=3, col=-1, player="B")

        with pytest.raises(ValidationError):
            ReversiMove(row=3, col=8, player="B")

    def test_reversi_move_invalid_player(self) -> None:
        """Test that invalid player values raise validation error."""
        with pytest.raises(ValidationError):
            ReversiMove(row=3, col=4, player="X")

        with pytest.raises(ValidationError):
            ReversiMove(row=3, col=4, player="black")


class TestReversiAnalysis:
    """Test cases for ReversiAnalysis model."""

    def test_reversi_analysis_creation_basic(self) -> None:
        """Test creating a basic Reversi analysis."""
        analysis = ReversiAnalysis(
            mobility=5,
            frontier_discs=8,
            corner_discs=1,
            stable_discs=3,
            positional_score=42,
            position_evaluation="winning",
            recommended_moves=[Position(row=2, col=3)],
            danger_zones=[Position(row=1, col=1)],
            strategy="Control corners and edges",
            reasoning="Having corner control provides strategic advantage",
        )

        assert analysis.mobility == 5
        assert analysis.frontier_discs == 8
        assert analysis.corner_discs == 1
        assert analysis.stable_discs == 3
        assert analysis.positional_score == 42
        assert analysis.position_evaluation == "winning"
        assert len(analysis.recommended_moves) == 1
        assert len(analysis.danger_zones) == 1
        assert "corner" in analysis.strategy.lower()
        assert "advantage" in analysis.reasoning.lower()

    def test_reversi_analysis_losing_position(self) -> None:
        """Test creating analysis for a losing position."""
        analysis = ReversiAnalysis(
            mobility=2,
            frontier_discs=12,
            corner_discs=0,
            stable_discs=1,
            positional_score=-15,
            position_evaluation="losing",
            recommended_moves=[Position(row=5, col=6)],
            danger_zones=[Position(row=0, col=0), Position(row=0, col=7)],
            strategy="Defensive play required",
            reasoning="Limited mobility and no corner control",
        )

        assert analysis.mobility == 2
        assert analysis.position_evaluation == "losing"
        assert analysis.positional_score == -15
        assert len(analysis.danger_zones) == 2
        assert "defensive" in analysis.strategy.lower()

    def test_reversi_analysis_equal_position(self) -> None:
        """Test creating analysis for an equal position."""
        analysis = ReversiAnalysis(
            mobility=6,
            frontier_discs=10,
            corner_discs=1,
            stable_discs=4,
            positional_score=0,
            position_evaluation="equal",
            recommended_moves=[
                Position(row=2, col=3),
                Position(row=5, col=4),
            ],
            danger_zones=[],
            strategy="Balanced approach",
            reasoning="Position is roughly equal, focus on mobility",
        )

        assert analysis.position_evaluation == "equal"
        assert analysis.positional_score == 0
        assert len(analysis.recommended_moves) == 2
        assert len(analysis.danger_zones) == 0

    def test_reversi_analysis_unclear_position(self) -> None:
        """Test creating analysis for an unclear position."""
        analysis = ReversiAnalysis(
            mobility=4,
            frontier_discs=9,
            corner_discs=0,
            stable_discs=2,
            positional_score=3,
            position_evaluation="unclear",
            recommended_moves=[Position(row=3, col=2)],
            danger_zones=[Position(row=1, col=0)],
            strategy="Careful positioning",
            reasoning="Complex position requires deep calculation",
        )

        assert analysis.position_evaluation == "unclear"
        assert analysis.positional_score == 3
        assert "complex" in analysis.reasoning.lower()

    def test_reversi_analysis_invalid_position_evaluation(self) -> None:
        """Test that invalid position evaluation raises validation error."""
        with pytest.raises(ValidationError):
            ReversiAnalysis(
                mobility=5,
                frontier_discs=8,
                corner_discs=1,
                stable_discs=3,
                positional_score=42,
                position_evaluation="definitely_winning",  # Invalid value
                recommended_moves=[],
                danger_zones=[],
                strategy="Test strategy",
                reasoning="Test reasoning",
            )

    def test_reversi_analysis_empty_moves_and_zones(self) -> None:
        """Test analysis with empty recommended moves and danger zones."""
        analysis = ReversiAnalysis(
            mobility=0,
            frontier_discs=5,
            corner_discs=2,
            stable_discs=8,
            positional_score=20,
            position_evaluation="winning",
            recommended_moves=[],
            danger_zones=[],
            strategy="Maintain control",
            reasoning="No legal moves available",
        )

        assert analysis.mobility == 0
        assert len(analysis.recommended_moves) == 0
        assert len(analysis.danger_zones) == 0
        assert analysis.position_evaluation == "winning"

    def test_reversi_analysis_multiple_recommendations(self) -> None:
        """Test analysis with multiple recommended moves and danger zones."""
        recommended_moves = [
            Position(row=2, col=3),
            Position(row=4, col=1),
            Position(row=6, col=5),
        ]
        danger_zones = [
            Position(row=0, col=0),
            Position(row=0, col=7),
            Position(row=7, col=0),
            Position(row=7, col=7),
        ]

        analysis = ReversiAnalysis(
            mobility=8,
            frontier_discs=6,
            corner_discs=0,
            stable_discs=2,
            positional_score=5,
            position_evaluation="equal",
            recommended_moves=recommended_moves,
            danger_zones=danger_zones,
            strategy="Avoid corners until late game",
            reasoning="Multiple good options available",
        )

        assert len(analysis.recommended_moves) == 3
        assert len(analysis.danger_zones) == 4
        assert analysis.recommended_moves[0].row == 2
        assert analysis.danger_zones[0].row == 0

    def test_reversi_analysis_negative_values(self) -> None:
        """Test analysis with negative positional score."""
        analysis = ReversiAnalysis(
            mobility=1,
            frontier_discs=15,
            corner_discs=0,
            stable_discs=0,
            positional_score=-25,
            position_evaluation="losing",
            recommended_moves=[Position(row=4, col=4)],
            danger_zones=[Position(row=0, col=0)],
            strategy="Emergency defense",
            reasoning="Severely behind in position",
        )

        assert analysis.positional_score == -25
        assert analysis.position_evaluation == "losing"
        assert "emergency" in analysis.strategy.lower()

    def test_reversi_analysis_high_values(self) -> None:
        """Test analysis with high metric values."""
        analysis = ReversiAnalysis(
            mobility=10,
            frontier_discs=20,
            corner_discs=4,
            stable_discs=15,
            positional_score=100,
            position_evaluation="winning",
            recommended_moves=[Position(row=3, col=3)],
            danger_zones=[],
            strategy="Press the advantage",
            reasoning="Dominant position in all aspects",
        )

        assert analysis.mobility == 10
        assert analysis.frontier_discs == 20
        assert analysis.corner_discs == 4
        assert analysis.stable_discs == 15
        assert analysis.positional_score == 100
        assert len(analysis.danger_zones) == 0
