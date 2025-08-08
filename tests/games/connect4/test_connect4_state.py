"""Tests for Connect4 state with real component validation.

This module provides comprehensive tests for Connect4 state management including:
    - State initialization and structure
    - Board representation and manipulation
    - Game status tracking
    - Move history management
    - Player analysis storage

All tests use real components without mocks, following the no-mocks methodology.
"""

import pytest

from haive.games.connect4.models import Connect4Move
from haive.games.connect4.state import Connect4State


class TestConnect4State:
    """Test suite for Connect4State with real state validation."""

    def test_connect4_state_initialization_default(self):
        """Test Connect4State initialization with default values."""
        state = Connect4State()

        # Check board structure
        assert len(state.board) == 6  # 6 rows
        assert all(len(row) == 7 for row in state.board)  # 7 columns each
        assert all(cell is None for row in state.board for cell in row)  # Empty cells

        # Check initial state
        assert state.turn == "red"
        assert state.move_history == []
        assert state.red_analysis == []
        assert state.yellow_analysis == []
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert state.captured is None
        assert state.error_message is None

    def test_connect4_state_initialization_custom(self):
        """Test Connect4State initialization with custom values."""
        custom_board = [[None for _ in range(7)] for _ in range(6)]
        custom_board[5][3] = "red"  # Red piece at bottom center

        moves = [Connect4Move(column=3, explanation="Center control")]

        state = Connect4State(
            board=custom_board,
            turn="yellow",
            move_history=moves,
            game_status="ongoing",
            winner=None,
        )

        assert state.board[5][3] == "red"
        assert state.turn == "yellow"
        assert len(state.move_history) == 1
        assert state.move_history[0].column == 3
        assert state.game_status == "ongoing"

    def test_connect4_state_board_string_empty_board(self):
        """Test Connect4State board string representation for empty board."""
        state = Connect4State()
        board_str = state.board_string

        # Should contain column headers
        assert "0" in board_str
        assert "1" in board_str
        assert "6" in board_str

        # Should contain empty cells representation
        lines = board_str.split("\n")
        assert len(lines) >= 6  # At least 6 rows plus headers

    def test_connect4_state_board_string_with_pieces(self):
        """Test Connect4State board string representation with pieces."""
        state = Connect4State()
        # Place some pieces manually
        state.board[5][3] = "red"  # Bottom center
        state.board[4][3] = "yellow"  # Above red piece
        state.board[5][2] = "red"  # Bottom left of center

        board_str = state.board_string

        # Should contain piece representations
        assert "R" in board_str  # Red pieces
        assert "Y" in board_str  # Yellow pieces
        assert "." in board_str  # Empty cells

    def test_connect4_state_is_column_full_empty_column(self):
        """Test Connect4State is_column_full for empty columns."""
        state = Connect4State()

        # All columns should be empty initially
        for col in range(7):
            assert not state.is_column_full(col)

    def test_connect4_state_is_column_full_partially_filled(self):
        """Test Connect4State is_column_full for partially filled columns."""
        state = Connect4State()

        # Fill bottom 3 rows of column 3
        state.board[5][3] = "red"
        state.board[4][3] = "yellow"
        state.board[3][3] = "red"

        # Column 3 should not be full yet
        assert not state.is_column_full(3)

        # Other columns should still be empty
        for col in range(7):
            if col != 3:
                assert not state.is_column_full(col)

    def test_connect4_state_is_column_full_completely_filled(self):
        """Test Connect4State is_column_full for completely filled columns."""
        state = Connect4State()

        # Fill entire column 3
        for row in range(6):
            state.board[row][3] = "red" if row % 2 == 0 else "yellow"

        # Column 3 should be full
        assert state.is_column_full(3)

        # Other columns should still be empty
        for col in range(7):
            if col != 3:
                assert not state.is_column_full(col)

    def test_connect4_state_is_column_full_invalid_column(self):
        """Test Connect4State is_column_full with invalid column numbers."""
        state = Connect4State()

        # Invalid negative column
        with pytest.raises(IndexError):
            state.is_column_full(-1)

        # Invalid high column
        with pytest.raises(IndexError):
            state.is_column_full(7)

    def test_connect4_state_get_next_row_empty_column(self):
        """Test Connect4State get_next_row for empty columns."""
        state = Connect4State()

        # All columns should return bottom row (5) when empty
        for col in range(7):
            assert state.get_next_row(col) == 5

    def test_connect4_state_get_next_row_partially_filled(self):
        """Test Connect4State get_next_row for partially filled columns."""
        state = Connect4State()

        # Fill bottom 2 rows of column 3
        state.board[5][3] = "red"
        state.board[4][3] = "yellow"

        # Next row should be row 3
        assert state.get_next_row(3) == 3

        # Other columns should still return bottom row
        for col in range(7):
            if col != 3:
                assert state.get_next_row(col) == 5

    def test_connect4_state_get_next_row_almost_full(self):
        """Test Connect4State get_next_row for almost full columns."""
        state = Connect4State()

        # Fill bottom 5 rows of column 3
        for row in range(5, 0, -1):
            state.board[row][3] = "red" if row % 2 == 0 else "yellow"

        # Next row should be top row (0)
        assert state.get_next_row(3) == 0

    def test_connect4_state_get_next_row_full_column(self):
        """Test Connect4State get_next_row for full columns."""
        state = Connect4State()

        # Fill entire column 3
        for row in range(6):
            state.board[row][3] = "red" if row % 2 == 0 else "yellow"

        # Should return None for full column
        assert state.get_next_row(3) is None

    def test_connect4_state_get_next_row_invalid_column(self):
        """Test Connect4State get_next_row with invalid column numbers."""
        state = Connect4State()

        # Invalid negative column
        with pytest.raises(IndexError):
            state.get_next_row(-1)

        # Invalid high column
        with pytest.raises(IndexError):
            state.get_next_row(7)

    def test_connect4_state_move_history_management(self):
        """Test Connect4State move history management."""
        state = Connect4State()

        # Initially empty
        assert state.move_history == []

        # Add moves
        move1 = Connect4Move(column=3, explanation="Center control")
        move2 = Connect4Move(column=4, explanation="Counter attack")

        state.move_history = [move1, move2]

        assert len(state.move_history) == 2
        assert state.move_history[0].column == 3
        assert state.move_history[1].column == 4

    def test_connect4_state_analysis_storage(self):
        """Test Connect4State analysis storage for both players."""
        state = Connect4State()

        # Initially empty
        assert state.red_analysis == []
        assert state.yellow_analysis == []

        # Add analysis
        red_analysis = {
            "position_score": 0.5,
            "center_control": 7,
            "winning_chances": 65,
        }

        yellow_analysis = {
            "position_score": -0.3,
            "center_control": 4,
            "winning_chances": 35,
        }

        state.red_analysis = [red_analysis]
        state.yellow_analysis = [yellow_analysis]

        assert len(state.red_analysis) == 1
        assert len(state.yellow_analysis) == 1
        assert state.red_analysis[0]["position_score"] == 0.5
        assert state.yellow_analysis[0]["position_score"] == -0.3

    def test_connect4_state_game_status_transitions(self):
        """Test Connect4State game status transitions."""
        state = Connect4State()

        # Start with ongoing
        assert state.game_status == "ongoing"
        assert state.winner is None

        # Red wins
        state.game_status = "red_win"
        state.winner = "red"
        assert state.game_status == "red_win"
        assert state.winner == "red"

        # Yellow wins
        state.game_status = "yellow_win"
        state.winner = "yellow"
        assert state.game_status == "yellow_win"
        assert state.winner == "yellow"

        # Draw
        state.game_status = "draw"
        state.winner = None
        assert state.game_status == "draw"
        assert state.winner is None

    def test_connect4_state_turn_management(self):
        """Test Connect4State turn management."""
        state = Connect4State()

        # Start with red
        assert state.turn == "red"

        # Switch to yellow
        state.turn = "yellow"
        assert state.turn == "yellow"

        # Switch back to red
        state.turn = "red"
        assert state.turn == "red"

    def test_connect4_state_error_message_handling(self):
        """Test Connect4State error message handling."""
        state = Connect4State()

        # Initially no error
        assert state.error_message is None

        # Set error message
        state.error_message = "Invalid move: Column is full"
        assert state.error_message == "Invalid move: Column is full"

        # Clear error message
        state.error_message = None
        assert state.error_message is None

    def test_connect4_state_captured_field_usage(self):
        """Test Connect4State captured field for compatibility."""
        state = Connect4State()

        # Should exist and be None (for compatibility with other games)
        assert state.captured is None

        # Can be set if needed
        state.captured = "some_value"
        assert state.captured == "some_value"

    def test_connect4_state_board_integrity_validation(self):
        """Test Connect4State board integrity validation."""
        # Valid board structure
        valid_board = [[None for _ in range(7)] for _ in range(6)]
        state = Connect4State(board=valid_board)

        assert len(state.board) == 6
        assert all(len(row) == 7 for row in state.board)

    def test_connect4_state_serialization(self):
        """Test Connect4State serialization to dictionary."""
        move = Connect4Move(column=3, explanation="Center control")
        state = Connect4State(turn="yellow", move_history=[move], game_status="ongoing")

        state_dict = state.model_dump()

        assert state_dict["turn"] == "yellow"
        assert len(state_dict["move_history"]) == 1
        assert state_dict["move_history"][0]["column"] == 3
        assert state_dict["game_status"] == "ongoing"

    def test_connect4_state_deserialization(self):
        """Test Connect4State deserialization from dictionary."""
        state_dict = {
            "board": [[None for _ in range(7)] for _ in range(6)],
            "turn": "yellow",
            "move_history": [{"column": 3, "explanation": "Center control"}],
            "red_analysis": [],
            "yellow_analysis": [],
            "game_status": "ongoing",
            "winner": None,
            "captured": None,
            "error_message": None,
        }

        state = Connect4State(**state_dict)

        assert state.turn == "yellow"
        assert len(state.move_history) == 1
        assert state.move_history[0].column == 3
        assert state.game_status == "ongoing"

    def test_connect4_state_board_coordinates_validation(self):
        """Test Connect4State board coordinate system validation."""
        state = Connect4State()

        # Test valid coordinates
        for row in range(6):
            for col in range(7):
                # Should not raise exception
                state.board[row][col] = "red"
                assert state.board[row][col] == "red"
                state.board[row][col] = None

    def test_connect4_state_complex_board_scenario(self):
        """Test Connect4State with complex board scenario."""
        state = Connect4State()

        # Create a complex board situation
        moves = [
            (5, 3, "red"),  # Bottom center
            (5, 4, "yellow"),  # Bottom right of center
            (4, 3, "red"),  # Stack on center
            (5, 2, "yellow"),  # Bottom left of center
            (3, 3, "red"),  # Continue stacking center
            (4, 4, "yellow"),  # Stack right of center
        ]

        for row, col, player in moves:
            state.board[row][col] = player

        # Verify board state
        assert state.board[5][3] == "red"
        assert state.board[4][3] == "red"
        assert state.board[3][3] == "red"
        assert state.board[5][4] == "yellow"
        assert state.board[4][4] == "yellow"
        assert state.board[5][2] == "yellow"

        # Test column fullness
        assert not state.is_column_full(3)  # 3 pieces, not full
        assert not state.is_column_full(4)  # 2 pieces, not full
        assert not state.is_column_full(2)  # 1 piece, not full

        # Test next row calculations
        assert state.get_next_row(3) == 2  # Next available in center
        assert state.get_next_row(4) == 3  # Next available right
        assert state.get_next_row(2) == 4  # Next available left

        # Test board string contains pieces
        board_str = state.board_string
        assert "R" in board_str
        assert "Y" in board_str

    def test_connect4_state_multiple_analysis_entries(self):
        """Test Connect4State with multiple analysis entries per player."""
        state = Connect4State()

        # Add multiple analysis entries
        red_analyses = [
            {"position_score": 0.1, "winning_chances": 55},
            {"position_score": 0.3, "winning_chances": 60},
            {"position_score": 0.5, "winning_chances": 65},
        ]

        yellow_analyses = [
            {"position_score": -0.1, "winning_chances": 45},
            {"position_score": -0.3, "winning_chances": 40},
        ]

        state.red_analysis = red_analyses
        state.yellow_analysis = yellow_analyses

        assert len(state.red_analysis) == 3
        assert len(state.yellow_analysis) == 2

        # Check latest analysis
        assert state.red_analysis[-1]["position_score"] == 0.5
        assert state.yellow_analysis[-1]["position_score"] == -0.3

    def test_connect4_state_initialization_static_method(self):
        """Test Connect4State static initialization method compatibility."""
        # Test if there's a static initialize method or similar
        state = Connect4State()

        # Basic initialization should work
        assert isinstance(state, Connect4State)
        assert state.game_status == "ongoing"
        assert state.turn == "red"
        assert len(state.board) == 6
        assert len(state.board[0]) == 7
