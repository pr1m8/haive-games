"""Test cases for Reversi game state.

This module tests the ReversiState class and its properties and methods
for managing the game board and player information.
"""

from pydantic import ValidationError
import pytest

from haive.games.reversi.models import ReversiMove
from haive.games.reversi.state import ReversiState


class TestReversiState:
    """Test cases for ReversiState class."""

    def test_reversi_state_initialization_default(self) -> None:
        """Test initializing ReversiState with default values."""
        # Create a standard initial board
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "W"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"

        state = ReversiState(
            board=board,
            turn="B",
        )

        assert state.turn == "B"
        assert state.game_status == "ongoing"
        assert state.move_history == []
        assert state.winner is None
        assert state.player_B == "player1"
        assert state.player_W == "player2"
        assert state.skip_count == 0
        assert len(state.player1_analysis) == 0
        assert len(state.player2_analysis) == 0

    def test_reversi_state_initialization_custom(self) -> None:
        """Test initializing ReversiState with custom values."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "W"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"

        move = ReversiMove(row=2, col=3, player="B")

        state = ReversiState(
            board=board,
            turn="W",
            game_status="B_win",
            move_history=[move],
            winner="B",
            player_B="player2",
            player_W="player1",
            skip_count=1,
        )

        assert state.turn == "W"
        assert state.game_status == "B_win"
        assert len(state.move_history) == 1
        assert state.winner == "B"
        assert state.player_B == "player2"
        assert state.player_W == "player1"
        assert state.skip_count == 1

    def test_board_validation_correct_size(self) -> None:
        """Test that board validation accepts correct 8x8 board."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "W"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"

        state = ReversiState(board=board, turn="B")
        assert len(state.board) == 8
        assert all(len(row) == 8 for row in state.board)

    def test_board_validation_wrong_row_count(self) -> None:
        """Test that board validation fails with wrong number of rows."""
        board = [[None for _ in range(8)] for _ in range(7)]  # Only 7 rows

        with pytest.raises(ValidationError, match="Board must have 8 rows"):
            ReversiState(board=board, turn="B")

    def test_board_validation_wrong_column_count(self) -> None:
        """Test that board validation fails with wrong number of columns."""
        board = [[None for _ in range(7)] for _ in range(8)]  # Only 7 columns

        with pytest.raises(ValidationError, match="Each row must have 8 columns"):
            ReversiState(board=board, turn="B")

    def test_board_validation_invalid_cell_values(self) -> None:
        """Test that board validation fails with invalid cell values."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "X"  # Invalid value

        with pytest.raises(
            ValidationError, match="Cell values must be None, 'B', or 'W'"
        ):
            ReversiState(board=board, turn="B")

    def test_current_player_name_black_turn(self) -> None:
        """Test current_player_name property when it's Black's turn."""
        board = [[None for _ in range(8)] for _ in range(8)]
        state = ReversiState(
            board=board,
            turn="B",
            player_B="player1",
            player_W="player2",
        )

        assert state.current_player_name == "player1"

    def test_current_player_name_white_turn(self) -> None:
        """Test current_player_name property when it's White's turn."""
        board = [[None for _ in range(8)] for _ in range(8)]
        state = ReversiState(
            board=board,
            turn="W",
            player_B="player1",
            player_W="player2",
        )

        assert state.current_player_name == "player2"

    def test_current_player_name_swapped_players(self) -> None:
        """Test current_player_name with swapped player assignments."""
        board = [[None for _ in range(8)] for _ in range(8)]
        state = ReversiState(
            board=board,
            turn="B",
            player_B="player2",  # Black is player2
            player_W="player1",  # White is player1
        )

        assert state.current_player_name == "player2"

    def test_disc_count_initial_position(self) -> None:
        """Test disc_count property with initial board position."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "W"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"

        state = ReversiState(board=board, turn="B")
        counts = state.disc_count

        assert counts["B"] == 2
        assert counts["W"] == 2

    def test_disc_count_unequal_position(self) -> None:
        """Test disc_count property with unequal disc counts."""
        board = [[None for _ in range(8)] for _ in range(8)]
        # Black has more discs
        board[3][3] = "B"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"
        board[2][2] = "B"

        state = ReversiState(board=board, turn="W")
        counts = state.disc_count

        assert counts["B"] == 4
        assert counts["W"] == 1

    def test_disc_count_empty_board(self) -> None:
        """Test disc_count property with empty board."""
        board = [[None for _ in range(8)] for _ in range(8)]

        state = ReversiState(board=board, turn="B")
        counts = state.disc_count

        assert counts["B"] == 0
        assert counts["W"] == 0

    def test_disc_count_full_board(self) -> None:
        """Test disc_count property with full board."""
        board = [["B" if (i + j) % 2 == 0 else "W" for j in range(8)] for i in range(8)]

        state = ReversiState(board=board, turn="B")
        counts = state.disc_count

        assert counts["B"] == 32
        assert counts["W"] == 32

    def test_board_string_initial_position(self) -> None:
        """Test board_string property with initial position."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "W"
        board[3][4] = "B"
        board[4][3] = "B"
        board[4][4] = "W"

        state = ReversiState(board=board, turn="B")
        board_str = state.board_string

        # Check that it contains expected elements
        assert "1 2 3 4 5 6 7 8" in board_str
        assert "A |" in board_str
        assert "B |" in board_str
        assert "W|" in board_str
        assert "B|" in board_str
        assert "Black: 2 discs, White: 2 discs" in board_str

    def test_board_string_empty_board(self) -> None:
        """Test board_string property with empty board."""
        board = [[None for _ in range(8)] for _ in range(8)]

        state = ReversiState(board=board, turn="B")
        board_str = state.board_string

        assert "Black: 0 discs, White: 0 discs" in board_str
        # Should contain only empty cells (represented by spaces)
        assert "W|" not in board_str
        assert "B|" not in board_str

    def test_board_string_format_structure(self) -> None:
        """Test that board_string has correct structure."""
        board = [[None for _ in range(8)] for _ in range(8)]
        board[0][0] = "B"
        board[7][7] = "W"

        state = ReversiState(board=board, turn="B")
        board_str = state.board_string

        lines = board_str.split("\n")

        # Should have header, 8 board rows with separators, and disc count
        # Header + 8 * (row + separator) + final separator + disc count
        expected_lines = 1 + 8 * 2 + 1
        assert len(lines) == expected_lines

        # Check header
        assert lines[0].strip() == "1 2 3 4 5 6 7 8"

        # Check that all board rows start with letter
        board_row_indices = [
            2,
            4,
            6,
            8,
            10,
            12,
            14,
            16,
        ]  # Every other line starting from 2
        for i, row_idx in enumerate(board_row_indices):
            expected_letter = chr(ord("A") + i)
            assert lines[row_idx].startswith(f"{expected_letter} |")

    def test_initialize_class_method_defaults(self) -> None:
        """Test ReversiState.initialize class method with defaults."""
        state = ReversiState.initialize()

        assert state.turn == "B"
        assert state.player_B == "player1"
        assert state.player_W == "player2"
        assert state.game_status == "ongoing"

        # Check initial board setup
        counts = state.disc_count
        assert counts["B"] == 2
        assert counts["W"] == 2

        # Check specific initial positions
        assert state.board[3][3] == "W"
        assert state.board[3][4] == "B"
        assert state.board[4][3] == "B"
        assert state.board[4][4] == "W"

    def test_initialize_class_method_custom_first_player(self) -> None:
        """Test ReversiState.initialize with custom first player."""
        state = ReversiState.initialize(first_player="W")

        assert state.turn == "W"
        assert state.player_B == "player1"
        assert state.player_W == "player2"

    def test_initialize_class_method_custom_players(self) -> None:
        """Test ReversiState.initialize with custom player assignments."""
        state = ReversiState.initialize(
            first_player="B",
            player_B="player2",
            player_W="player1",
        )

        assert state.turn == "B"
        assert state.player_B == "player2"
        assert state.player_W == "player1"
        assert state.current_player_name == "player2"

    def test_move_history_tracking(self) -> None:
        """Test that move history is properly tracked."""
        board = [[None for _ in range(8)] for _ in range(8)]

        move1 = ReversiMove(row=2, col=3, player="B")
        move2 = ReversiMove(row=4, col=5, player="W")

        state = ReversiState(
            board=board,
            turn="B",
            move_history=[move1, move2],
        )

        assert len(state.move_history) == 2
        assert state.move_history[0] == move1
        assert state.move_history[1] == move2

    def test_analysis_tracking(self) -> None:
        """Test that player analysis is properly tracked."""
        board = [[None for _ in range(8)] for _ in range(8)]

        analysis1 = {"mobility": 5, "evaluation": "winning"}
        analysis2 = {"mobility": 3, "evaluation": "losing"}

        state = ReversiState(
            board=board,
            turn="B",
            player1_analysis=[analysis1],
            player2_analysis=[analysis2],
        )

        assert len(state.player1_analysis) == 1
        assert len(state.player2_analysis) == 1
        assert state.player1_analysis[0] == analysis1
        assert state.player2_analysis[0] == analysis2

    def test_game_status_values(self) -> None:
        """Test valid game status values."""
        board = [[None for _ in range(8)] for _ in range(8)]

        # Test all valid status values
        valid_statuses = ["ongoing", "B_win", "W_win", "draw"]

        for status in valid_statuses:
            state = ReversiState(board=board, turn="B", game_status=status)
            assert state.game_status == status

    def test_invalid_game_status(self) -> None:
        """Test that invalid game status raises validation error."""
        board = [[None for _ in range(8)] for _ in range(8)]

        with pytest.raises(ValidationError):
            ReversiState(board=board, turn="B", game_status="invalid_status")

    def test_invalid_turn_value(self) -> None:
        """Test that invalid turn values raise validation error."""
        board = [[None for _ in range(8)] for _ in range(8)]

        with pytest.raises(ValidationError):
            ReversiState(board=board, turn="X")

    def test_invalid_player_assignment(self) -> None:
        """Test that invalid player assignments raise validation error."""
        board = [[None for _ in range(8)] for _ in range(8)]

        with pytest.raises(ValidationError):
            ReversiState(board=board, turn="B", player_B="invalid_player")
