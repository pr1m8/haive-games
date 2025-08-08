"""Comprehensive tests for Tic Tac Toe game models.

This module tests all data models, enumerations, and data structures
used in the Tic Tac Toe game implementation.
"""

from pydantic import ValidationError
import pytest

from haive.games.tic_tac_toe.models import (
    TicTacToeAnalysis,
    TicTacToeMove,
)


class TestTicTacToeMove:
    """Test TicTacToeMove model."""

    def test_move_creation_valid_coordinates(self):
        """Test creating TicTacToeMove with valid coordinates."""
        move = TicTacToeMove(row=1, col=2)
        assert move.row == 1
        assert move.col == 2

    def test_move_creation_boundary_coordinates(self):
        """Test creating moves with boundary coordinates."""
        # Test all valid boundary positions
        valid_positions = [
            (0, 0),  # Top-left
            (0, 2),  # Top-right
            (2, 0),  # Bottom-left
            (2, 2),  # Bottom-right
            (1, 1),  # Center
        ]

        for row, col in valid_positions:
            move = TicTacToeMove(row=row, col=col)
            assert move.row == row
            assert move.col == col

    def test_move_validation_invalid_coordinates(self):
        """Test move validation with invalid coordinates."""
        invalid_positions = [
            (-1, 0),  # Row too small
            (3, 0),  # Row too large
            (0, -1),  # Col too small
            (0, 3),  # Col too large
            (-1, -1),  # Both negative
            (3, 3),  # Both too large
            (5, 5),  # Way out of bounds
        ]

        for row, col in invalid_positions:
            with pytest.raises(ValidationError):
                TicTacToeMove(row=row, col=col)

    def test_move_string_representation(self):
        """Test string representation of TicTacToeMove."""
        move = TicTacToeMove(row=1, col=2)
        str_repr = str(move)
        assert "row=1" in str_repr
        assert "col=2" in str_repr

    def test_move_equality(self):
        """Test equality comparison between moves."""
        move1 = TicTacToeMove(row=1, col=2)
        move2 = TicTacToeMove(row=1, col=2)
        move3 = TicTacToeMove(row=2, col=1)

        assert move1 == move2
        assert move1 != move3
        assert move2 != move3

    def test_move_hash_consistency(self):
        """Test that moves can be used as dictionary keys."""
        move1 = TicTacToeMove(row=1, col=2)
        move2 = TicTacToeMove(row=1, col=2)
        move3 = TicTacToeMove(row=2, col=1)

        move_dict = {move1: "first", move3: "second"}

        # Same coordinates should access same value
        assert move_dict[move2] == "first"
        assert len(move_dict) == 2

    def test_move_serialization(self):
        """Test move serialization and deserialization."""
        move = TicTacToeMove(row=2, col=0)

        # Serialize to dict
        move_dict = move.model_dump() if hasattr(move, "model_dump") else move.dict()

        # Deserialize back
        new_move = TicTacToeMove(**move_dict)

        assert new_move.row == move.row
        assert new_move.col == move.col
        assert new_move == move

    def test_all_valid_board_positions(self):
        """Test creating moves for all valid board positions."""
        valid_moves = []

        for row in range(3):
            for col in range(3):
                move = TicTacToeMove(row=row, col=col)
                valid_moves.append(move)
                assert 0 <= move.row <= 2
                assert 0 <= move.col <= 2

        # Should have 9 total valid positions
        assert len(valid_moves) == 9

        # All moves should be unique
        unique_moves = set(valid_moves)
        assert len(unique_moves) == 9


class TestTicTacToeAnalysis:
    """Test TicTacToeAnalysis model."""

    def test_analysis_creation_minimal(self):
        """Test creating analysis with minimal required fields."""
        analysis = TicTacToeAnalysis(
            board_assessment="Center position is key",
            strategy_recommendation="Take center if available",
        )

        assert analysis.board_assessment == "Center position is key"
        assert analysis.strategy_recommendation == "Take center if available"
        assert analysis.winning_moves == []
        assert analysis.blocking_moves == []
        assert analysis.recommended_move is None

    def test_analysis_creation_full(self):
        """Test creating analysis with all fields."""
        winning_moves = [{"row": 0, "col": 0}, {"row": 1, "col": 1}]
        blocking_moves = [{"row": 2, "col": 2}]
        recommended_move = {"row": 1, "col": 1}

        analysis = TicTacToeAnalysis(
            board_assessment="Complex position with multiple threats",
            strategy_recommendation="Block opponent and set up fork",
            winning_moves=winning_moves,
            blocking_moves=blocking_moves,
            recommended_move=recommended_move,
        )

        assert analysis.board_assessment == "Complex position with multiple threats"
        assert analysis.strategy_recommendation == "Block opponent and set up fork"
        assert analysis.winning_moves == winning_moves
        assert analysis.blocking_moves == blocking_moves
        assert analysis.recommended_move == recommended_move

    def test_analysis_empty_lists_default(self):
        """Test that empty lists are properly initialized."""
        analysis = TicTacToeAnalysis(
            board_assessment="Empty board", strategy_recommendation="Take center"
        )

        # Should have empty lists, not None
        assert analysis.winning_moves == []
        assert analysis.blocking_moves == []
        assert isinstance(analysis.winning_moves, list)
        assert isinstance(analysis.blocking_moves, list)

    def test_analysis_move_dictionaries_structure(self):
        """Test that move dictionaries have correct structure."""
        winning_moves = [
            {"row": 0, "col": 1},
            {"row": 2, "col": 1},
        ]
        blocking_moves = [
            {"row": 1, "col": 0},
        ]
        recommended_move = {"row": 1, "col": 1}

        analysis = TicTacToeAnalysis(
            board_assessment="Test analysis",
            strategy_recommendation="Test strategy",
            winning_moves=winning_moves,
            blocking_moves=blocking_moves,
            recommended_move=recommended_move,
        )

        # Verify winning moves structure
        for move in analysis.winning_moves:
            assert "row" in move
            assert "col" in move
            assert isinstance(move["row"], int)
            assert isinstance(move["col"], int)

        # Verify blocking moves structure
        for move in analysis.blocking_moves:
            assert "row" in move
            assert "col" in move
            assert isinstance(move["row"], int)
            assert isinstance(move["col"], int)

        # Verify recommended move structure
        if analysis.recommended_move:
            assert "row" in analysis.recommended_move
            assert "col" in analysis.recommended_move

    def test_analysis_serialization(self):
        """Test analysis serialization and deserialization."""
        analysis = TicTacToeAnalysis(
            board_assessment="Serialization test",
            strategy_recommendation="Test recommendation",
            winning_moves=[{"row": 0, "col": 0}],
            blocking_moves=[{"row": 1, "col": 1}],
            recommended_move={"row": 2, "col": 2},
        )

        # Serialize to dict
        analysis_dict = (
            analysis.model_dump()
            if hasattr(analysis, "model_dump")
            else analysis.dict()
        )

        # Deserialize back
        new_analysis = TicTacToeAnalysis(**analysis_dict)

        assert new_analysis.board_assessment == analysis.board_assessment
        assert new_analysis.strategy_recommendation == analysis.strategy_recommendation
        assert new_analysis.winning_moves == analysis.winning_moves
        assert new_analysis.blocking_moves == analysis.blocking_moves
        assert new_analysis.recommended_move == analysis.recommended_move

    def test_analysis_with_multiple_winning_moves(self):
        """Test analysis with multiple winning opportunities."""
        # Simulate a situation with multiple winning moves
        winning_moves = [
            {"row": 0, "col": 2},  # Complete top row
            {"row": 2, "col": 0},  # Complete diagonal
            {"row": 1, "col": 1},  # Complete column
        ]

        analysis = TicTacToeAnalysis(
            board_assessment="Multiple winning opportunities available",
            strategy_recommendation="Choose best winning move",
            winning_moves=winning_moves,
        )

        assert len(analysis.winning_moves) == 3
        for move in analysis.winning_moves:
            assert 0 <= move["row"] <= 2
            assert 0 <= move["col"] <= 2

    def test_analysis_with_multiple_blocking_moves(self):
        """Test analysis with multiple blocking requirements."""
        blocking_moves = [
            {"row": 0, "col": 0},  # Block top-left
            {"row": 1, "col": 2},  # Block middle-right
            {"row": 2, "col": 1},  # Block bottom-center
        ]

        analysis = TicTacToeAnalysis(
            board_assessment="Opponent has multiple threats",
            strategy_recommendation="Prioritize most dangerous threat",
            blocking_moves=blocking_moves,
        )

        assert len(analysis.blocking_moves) == 3
        for move in analysis.blocking_moves:
            assert 0 <= move["row"] <= 2
            assert 0 <= move["col"] <= 2

    def test_analysis_none_recommended_move(self):
        """Test analysis when no specific move is recommended."""
        analysis = TicTacToeAnalysis(
            board_assessment="Unclear position",
            strategy_recommendation="Any move is acceptable",
            recommended_move=None,
        )

        assert analysis.recommended_move is None

    def test_analysis_field_validation(self):
        """Test that required fields are validated."""
        # Missing board_assessment should raise error
        with pytest.raises(ValidationError):
            TicTacToeAnalysis(strategy_recommendation="Test")

        # Missing strategy_recommendation should raise error
        with pytest.raises(ValidationError):
            TicTacToeAnalysis(board_assessment="Test")

    def test_analysis_string_field_types(self):
        """Test that string fields accept various string types."""
        # Test various string inputs
        test_cases = [
            ("Simple assessment", "Simple strategy"),
            ("Multi-line\nassessment\nwith\nbreaks", "Complex\nstrategy"),
            ("", ""),  # Empty strings
            ("Unicode: 🎮♔♕", "Symbols: ×○"),
        ]

        for assessment, strategy in test_cases:
            analysis = TicTacToeAnalysis(
                board_assessment=assessment, strategy_recommendation=strategy
            )
            assert analysis.board_assessment == assessment
            assert analysis.strategy_recommendation == strategy


class TestModelIntegration:
    """Test integration between TicTacToe models."""

    def test_move_and_analysis_integration(self):
        """Test using moves within analysis."""
        # Create a move
        move = TicTacToeMove(row=1, col=1)

        # Use move coordinates in analysis
        analysis = TicTacToeAnalysis(
            board_assessment="Center position analysis",
            strategy_recommendation="Take center",
            recommended_move={"row": move.row, "col": move.col},
        )

        # Verify integration
        assert analysis.recommended_move["row"] == move.row
        assert analysis.recommended_move["col"] == move.col

    def test_analysis_moves_as_tic_tac_toe_moves(self):
        """Test converting analysis move dicts to TicTacToeMove objects."""
        analysis = TicTacToeAnalysis(
            board_assessment="Conversion test",
            strategy_recommendation="Test moves",
            winning_moves=[{"row": 0, "col": 1}, {"row": 2, "col": 0}],
            blocking_moves=[{"row": 1, "col": 2}],
        )

        # Convert winning moves to TicTacToeMove objects
        winning_move_objects = [
            TicTacToeMove(row=move["row"], col=move["col"])
            for move in analysis.winning_moves
        ]

        # Convert blocking moves to TicTacToeMove objects
        blocking_move_objects = [
            TicTacToeMove(row=move["row"], col=move["col"])
            for move in analysis.blocking_moves
        ]

        # Verify conversions
        assert len(winning_move_objects) == 2
        assert len(blocking_move_objects) == 1

        assert winning_move_objects[0].row == 0
        assert winning_move_objects[0].col == 1
        assert blocking_move_objects[0].row == 1
        assert blocking_move_objects[0].col == 2

    def test_comprehensive_game_scenario(self):
        """Test models in a comprehensive game scenario."""
        # Simulate mid-game analysis
        analysis = TicTacToeAnalysis(
            board_assessment="X has two in top row, O has two in center column",
            strategy_recommendation="Block X's winning move in top row",
            winning_moves=[],  # No immediate wins for current player
            blocking_moves=[{"row": 0, "col": 2}],  # Block X's win
            recommended_move={"row": 0, "col": 2},  # Same as blocking move
        )

        # Create the recommended move
        recommended_move = TicTacToeMove(
            row=analysis.recommended_move["row"], col=analysis.recommended_move["col"]
        )

        # Verify the move makes sense
        assert recommended_move.row == 0
        assert recommended_move.col == 2

        # Verify it matches the blocking move
        blocking_move = analysis.blocking_moves[0]
        assert recommended_move.row == blocking_move["row"]
        assert recommended_move.col == blocking_move["col"]

    def test_model_boundary_conditions(self):
        """Test models at boundary conditions."""
        # Test corner moves
        corner_moves = [
            TicTacToeMove(row=0, col=0),  # Top-left
            TicTacToeMove(row=0, col=2),  # Top-right
            TicTacToeMove(row=2, col=0),  # Bottom-left
            TicTacToeMove(row=2, col=2),  # Bottom-right
        ]

        # Use corner moves in analysis
        corner_move_dicts = [
            {"row": move.row, "col": move.col} for move in corner_moves
        ]

        analysis = TicTacToeAnalysis(
            board_assessment="Corner strategy analysis",
            strategy_recommendation="Control corners",
            winning_moves=corner_move_dicts[:2],  # First two corners
            blocking_moves=corner_move_dicts[2:],  # Last two corners
        )

        # Verify all corners are represented
        all_moves = analysis.winning_moves + analysis.blocking_moves
        assert len(all_moves) == 4

        # Verify all coordinates are valid
        for move_dict in all_moves:
            assert 0 <= move_dict["row"] <= 2
            assert 0 <= move_dict["col"] <= 2
