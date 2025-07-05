"""Unit tests for mancala game models.

This module tests the Pydantic models used in the mancala game,
including move validation and analysis models.
"""

import pytest
from pydantic import ValidationError

from haive.games.mancala.models import MancalaAnalysis, MancalaMove


class TestMancalaMove:
    """Test suite for MancalaMove model."""

    def test_valid_move_creation_player1(self) -> None:
        """Test creating valid moves for player1."""
        # Arrange & Act
        moves = [
            MancalaMove(pit_index=0, player="player1"),
            MancalaMove(pit_index=3, player="player1"),
            MancalaMove(pit_index=5, player="player1"),
        ]

        # Assert
        for i, move in enumerate(moves):
            assert move.pit_index == [0, 3, 5][i]
            assert move.player == "player1"

    def test_valid_move_creation_player2(self) -> None:
        """Test creating valid moves for player2."""
        # Arrange & Act
        moves = [
            MancalaMove(pit_index=0, player="player2"),
            MancalaMove(pit_index=2, player="player2"),
            MancalaMove(pit_index=5, player="player2"),
        ]

        # Assert
        for move in moves:
            assert 0 <= move.pit_index < 6
            assert move.player == "player2"

    def test_pit_index_validation_rejects_negative(self) -> None:
        """Test that negative pit indices are rejected."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            MancalaMove(pit_index=-1, player="player1")
        assert "greater than or equal to 0" in str(exc_info.value)

    def test_pit_index_validation_rejects_too_large(self) -> None:
        """Test that pit indices >= 6 are rejected."""
        # Act & Assert
        with pytest.raises(ValidationError) as exc_info:
            MancalaMove(pit_index=6, player="player1")
        assert "less than 6" in str(exc_info.value)

    def test_invalid_player_name_rejected(self) -> None:
        """Test that invalid player names are rejected."""
        # Act & Assert
        with pytest.raises(ValidationError):
            MancalaMove(pit_index=0, player="player3")

    def test_move_string_representation(self) -> None:
        """Test the string representation of moves."""
        # Arrange
        move1 = MancalaMove(pit_index=2, player="player1")
        move2 = MancalaMove(pit_index=4, player="player2")

        # Act & Assert
        assert str(move1) == "player1 sows from pit 2"
        assert str(move2) == "player2 sows from pit 4"


class TestMancalaAnalysis:
    """Test suite for MancalaAnalysis model."""

    def test_analysis_creation_with_all_fields(self) -> None:
        """Test creating analysis with all fields populated."""
        # Arrange & Act
        analysis = MancalaAnalysis(
            position_evaluation="Player has a strong lead with 5 more stones",
            recommended_move=3,
            expected_outcome="Likely win if continuing optimal play",
            strategic_considerations=[
                "Control the tempo",
                "Force opponent to empty their side",
                "Maintain stone advantage",
            ],
        )

        # Assert
        assert analysis.position_evaluation is not None
        assert analysis.recommended_move == 3
        assert analysis.expected_outcome is not None
        assert len(analysis.strategic_considerations) == 3

    def test_analysis_creation_minimal(self) -> None:
        """Test creating analysis with only required fields."""
        # Arrange & Act
        analysis = MancalaAnalysis(
            position_evaluation="Even position",
            recommended_move=0,
        )

        # Assert
        assert analysis.position_evaluation == "Even position"
        assert analysis.recommended_move == 0
        assert analysis.expected_outcome is None
        assert analysis.strategic_considerations == []

    def test_analysis_recommended_move_validation(self) -> None:
        """Test that recommended move must be valid pit index."""
        # Act & Assert
        with pytest.raises(ValidationError):
            MancalaAnalysis(
                position_evaluation="Test",
                recommended_move=-1,
            )

        with pytest.raises(ValidationError):
            MancalaAnalysis(
                position_evaluation="Test",
                recommended_move=6,
            )

    def test_analysis_empty_strategic_considerations(self) -> None:
        """Test that strategic considerations can be empty list."""
        # Arrange & Act
        analysis = MancalaAnalysis(
            position_evaluation="Simple position",
            recommended_move=2,
            strategic_considerations=[],
        )

        # Assert
        assert analysis.strategic_considerations == []
        assert isinstance(analysis.strategic_considerations, list)
