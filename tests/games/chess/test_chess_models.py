"""Unit tests for chess game models.

This module tests the Pydantic models used in the chess game,
including move validation, position analysis, and game state tracking.
"""

from pydantic import ValidationError
import pytest

from haive.games.chess.models import (
    ChessAnalysisResult,
    ChessDecisionModel,
    ChessMoveModel,
    ChessPositionEvaluation,
)


class TestChessMoveModel:
    """Test suite for ChessMoveModel."""

    def test_chess_move_model_accepts_valid_uci_notation(self) -> None:
        """Test that ChessMoveModel accepts valid UCI notation."""
        # Arrange
        valid_moves = ["e2e4", "Nf3", "O-O", "O-O-O", "a7a8=Q"]

        # Act & Assert
        for move in valid_moves:
            model = ChessMoveModel(move=move)
            assert model.move == move
            assert model.explanation is None

    def test_chess_move_model_accepts_move_with_explanation(self) -> None:
        """Test that ChessMoveModel accepts move with explanation."""
        # Arrange
        move = "e2e4"
        explanation = "Opening the center for rapid development"

        # Act
        model = ChessMoveModel(move=move, explanation=explanation)

        # Assert
        assert model.move == move
        assert model.explanation == explanation

    def test_chess_move_model_rejects_invalid_move_format(self) -> None:
        """Test that ChessMoveModel rejects invalid move formats."""
        # Arrange
        invalid_moves = ["", "e2", "xyz", "12"]

        # Act & Assert
        for move in invalid_moves:
            with pytest.raises(ValidationError) as exc_info:
                ChessMoveModel(move=move)
            assert "at least 4 characters" in str(exc_info.value)

    def test_chess_move_model_rejects_non_string_move(self) -> None:
        """Test that ChessMoveModel rejects non-string moves."""
        # Arrange
        invalid_types = [123, None, ["e2e4"], {"move": "e2e4"}]

        # Act & Assert
        for move in invalid_types:
            with pytest.raises(ValidationError):
                ChessMoveModel(move=move)


class TestChessDecisionModel:
    """Test suite for ChessDecisionModel."""

    @pytest.fixture
    def valid_position_eval(self) -> ChessPositionEvaluation:
        """Create a valid position evaluation for testing."""
        return ChessPositionEvaluation(
            material_balance=1.5,
            positional_advantage=0.3,
            threats=["Fork on f7", "Weak pawn on d6"],
            opportunities=["Open file for rook", "Knight outpost on e5"],
        )

    def test_chess_decision_model_with_all_fields(
        self, valid_position_eval: ChessPositionEvaluation
    ) -> None:
        """Test ChessDecisionModel creation with all fields."""
        # Arrange
        move = ChessMoveModel(move="Nf3", explanation="Developing knight")

        # Act
        decision = ChessDecisionModel(
            position_evaluation=valid_position_eval,
            candidate_moves=["Nf3", "e4", "d4"],
            selected_move=move,
            reasoning="Developing pieces before pushing pawns",
        )

        # Assert
        assert decision.position_evaluation == valid_position_eval
        assert len(decision.candidate_moves) == 3
        assert decision.selected_move == move
        assert "Developing pieces" in decision.reasoning

    def test_chess_decision_model_optional_fields(self) -> None:
        """Test ChessDecisionModel with optional fields omitted."""
        # Arrange
        move = ChessMoveModel(move="e2e4")

        # Act
        decision = ChessDecisionModel(
            selected_move=move,
            reasoning="Standard opening move",
        )

        # Assert
        assert decision.position_evaluation is None
        assert decision.candidate_moves == []
        assert decision.selected_move.move == "e2e4"


class TestChessPositionEvaluation:
    """Test suite for ChessPositionEvaluation."""

    def test_position_evaluation_with_all_fields(self) -> None:
        """Test creating position evaluation with all fields."""
        # Arrange & Act
        eval_pos = ChessPositionEvaluation(
            material_balance=2.5,
            positional_advantage=-0.5,
            threats=["Back rank mate threat", "Pinned knight"],
            opportunities=["Pawn break with f5", "Rook lift"],
        )

        # Assert
        assert eval_pos.material_balance == 2.5
        assert eval_pos.positional_advantage == -0.5
        assert len(eval_pos.threats) == 2
        assert len(eval_pos.opportunities) == 2

    def test_position_evaluation_with_empty_lists(self) -> None:
        """Test position evaluation with empty threat/opportunity lists."""
        # Arrange & Act
        eval_pos = ChessPositionEvaluation(
            material_balance=0.0,
            positional_advantage=0.0,
            threats=[],
            opportunities=[],
        )

        # Assert
        assert eval_pos.material_balance == 0.0
        assert eval_pos.threats == []
        assert eval_pos.opportunities == []


class TestChessAnalysisResult:
    """Test suite for ChessAnalysisResult."""

    def test_analysis_result_complete(self) -> None:
        """Test creating complete analysis result."""
        # Arrange
        best_moves = ["Rxe8+", "Qh5", "Nf6+"]

        # Act
        analysis = ChessAnalysisResult(
            best_moves=best_moves,
            evaluation_score=3.5,
            analysis_depth=20,
            key_variations={
                "Rxe8+": "Rxe8 Qxe8#",
                "Qh5": "g6 Qh6 threatening mate",
            },
        )

        # Assert
        assert analysis.best_moves == best_moves
        assert analysis.evaluation_score == 3.5
        assert analysis.analysis_depth == 20
        assert len(analysis.key_variations) == 2

    def test_analysis_result_minimal(self) -> None:
        """Test creating analysis with minimal fields."""
        # Arrange & Act
        analysis = ChessAnalysisResult(
            best_moves=["e4"],
            evaluation_score=0.1,
        )

        # Assert
        assert analysis.best_moves == ["e4"]
        assert analysis.evaluation_score == 0.1
        assert analysis.analysis_depth is None
        assert analysis.key_variations == {}

    def test_analysis_result_validation(self) -> None:
        """Test analysis result field validation."""
        # Act & Assert
        with pytest.raises(ValidationError):
            ChessAnalysisResult(
                best_moves=[],  # Empty list should fail
                evaluation_score=0.0,
            )
