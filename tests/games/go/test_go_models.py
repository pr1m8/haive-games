"""Unit tests for Go game models.

This module tests the Pydantic models used in the Go game,
including move validation and analysis models.
"""

import pytest
from pydantic import ValidationError

from haive.games.go.models import GoAnalysis, GoMove


class TestGoMove:
    """Test suite for GoMove model."""

    def test_valid_move_creation(self) -> None:
        """Test creating valid Go moves."""
        # Arrange & Act
        moves = [
            GoMove(move=(0, 0), player="black", board_size=19),
            GoMove(move=(9, 9), player="white", board_size=19),
            GoMove(move=(18, 18), player="black", board_size=19),
        ]

        # Assert
        for move in moves:
            assert isinstance(move.move, tuple)
            assert len(move.move) == 2
            assert move.player in ["black", "white"]
            assert move.board_size == 19

    def test_move_validation_rejects_out_of_bounds(self) -> None:
        """Test that moves outside board bounds are rejected."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            GoMove(move=(-1, 0), player="black", board_size=19)
        assert "out of bounds" in str(exc_info.value).lower()

        with pytest.raises(ValidationError):
            GoMove(move=(19, 19), player="black", board_size=19)

        with pytest.raises(ValidationError):
            GoMove(move=(0, 20), player="white", board_size=19)

    def test_move_validation_different_board_sizes(self) -> None:
        """Test move validation for different board sizes."""
        # Arrange & Act & Assert
        # 9x9 board
        valid_9x9 = GoMove(move=(8, 8), player="black", board_size=9)
        assert valid_9x9.move == (8, 8)

        with pytest.raises(ValidationError):
            GoMove(move=(9, 9), player="black", board_size=9)

        # 13x13 board
        valid_13x13 = GoMove(move=(12, 12), player="white", board_size=13)
        assert valid_13x13.move == (12, 12)

    def test_invalid_player_rejected(self) -> None:
        """Test that invalid player names are rejected."""
        # Act & Assert
        with pytest.raises(ValidationError):
            GoMove(move=(0, 0), player="red", board_size=19)

    def test_invalid_board_size_rejected(self) -> None:
        """Test that invalid board sizes are rejected."""
        # Act & Assert
        with pytest.raises(ValidationError):
            GoMove(move=(0, 0), player="black", board_size=0)

        with pytest.raises(ValidationError):
            GoMove(move=(0, 0), player="black", board_size=-1)


class TestGoAnalysis:
    """Test suite for GoAnalysis model."""

    def test_analysis_creation_with_all_fields(self) -> None:
        """Test creating analysis with all fields populated."""
        # Arrange & Act
        analysis = GoAnalysis(
            territory_evaluation="Black leads by 15 points",
            strong_positions=["upper right corner", "center influence"],
            weak_positions=["bottom left corner group"],
            strategic_advice=[
                "Secure territory in upper right",
                "Attack weak group in bottom left",
                "Build influence in center",
            ],
        )

        # Assert
        assert analysis.territory_evaluation is not None
        assert len(analysis.strong_positions) == 2
        assert len(analysis.weak_positions) == 1
        assert len(analysis.strategic_advice) == 3

    def test_analysis_creation_minimal(self) -> None:
        """Test creating analysis with only required fields."""
        # Arrange & Act
        analysis = GoAnalysis(
            territory_evaluation="Even position",
        )

        # Assert
        assert analysis.territory_evaluation == "Even position"
        assert analysis.strong_positions == []
        assert analysis.weak_positions == []
        assert analysis.strategic_advice == []

    def test_analysis_empty_lists_allowed(self) -> None:
        """Test that empty lists are allowed for optional fields."""
        # Arrange & Act
        analysis = GoAnalysis(
            territory_evaluation="Complex position",
            strong_positions=[],
            weak_positions=[],
            strategic_advice=[],
        )

        # Assert
        assert analysis.strong_positions == []
        assert analysis.weak_positions == []
        assert analysis.strategic_advice == []

    def test_analysis_with_complex_evaluation(self) -> None:
        """Test analysis with complex territory evaluation."""
        # Arrange & Act
        analysis = GoAnalysis(
            territory_evaluation="Black: 45 points, White: 50 points, White ahead by 5",
            strong_positions=[
                "Black has strong moyo in upper left",
                "White secure territory in lower right",
            ],
            weak_positions=[
                "Black group in center needs eyes",
                "White stones on left side under attack",
            ],
            strategic_advice=[
                "Black should secure center group",
                "White should defend left side",
                "Both players fight for upper right corner",
            ],
        )

        # Assert
        assert "Black: 45" in analysis.territory_evaluation
        assert "White: 50" in analysis.territory_evaluation
        assert len(analysis.strong_positions) == 2
        assert len(analysis.weak_positions) == 2
        assert len(analysis.strategic_advice) == 3
