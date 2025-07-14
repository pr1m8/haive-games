"""Test cases for Checkers game state.

This module tests the CheckersState class and its methods for managing
the game board, visualization, and state initialization.
"""

from haive.games.checkers.models import CheckersAnalysis, CheckersMove
from haive.games.checkers.state import CheckersState


class TestCheckersState:
    """Test cases for CheckersState class."""

    def test_checkers_state_default_creation(self) -> None:
        """Test creating CheckersState with default values."""
        state = CheckersState()

        # Check default board setup
        assert len(state.board) == 8
        assert all(len(row) == 8 for row in state.board)

        # Check that board has the right starting pieces
        # Black pieces in top 3 rows
        assert state.board[0][1] == 3  # Black piece
        assert state.board[1][0] == 3  # Black piece
        assert state.board[2][1] == 3  # Black piece

        # Empty middle rows
        assert all(cell == 0 for cell in state.board[3])
        assert all(cell == 0 for cell in state.board[4])

        # Red pieces in bottom 3 rows
        assert state.board[5][0] == 1  # Red piece
        assert state.board[6][1] == 1  # Red piece
        assert state.board[7][0] == 1  # Red piece

        # Check default values
        assert state.turn == "red"
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert len(state.move_history) == 0
        assert len(state.red_analysis) == 0
        assert len(state.black_analysis) == 0
        assert state.captured_pieces == {"red": [], "black": []}

    def test_checkers_state_explicit_creation(self) -> None:
        """Test creating CheckersState with explicit values."""
        custom_board = [[0 for _ in range(8)] for _ in range(8)]
        custom_board[0][0] = 1  # Red piece
        custom_board[7][7] = 3  # Black piece

        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )

        analysis = CheckersAnalysis(
            material_advantage="Equal",
            control_of_center="Balanced",
            suggested_moves=["c3-d4"],
            positional_evaluation="Equal position",
        )

        state = CheckersState(
            board=custom_board,
            turn="black",
            move_history=[move],
            game_status="game_over",
            winner="red",
            red_analysis=[analysis],
            captured_pieces={"red": ["b6"], "black": ["d4"]},
        )

        assert state.board[0][0] == 1
        assert state.board[7][7] == 3
        assert state.turn == "black"
        assert state.game_status == "game_over"
        assert state.winner == "red"
        assert len(state.move_history) == 1
        assert len(state.red_analysis) == 1
        assert state.captured_pieces["red"] == ["b6"]

    def test_checkers_state_board_string_creation(self) -> None:
        """Test board string creation and format."""
        state = CheckersState()

        board_string = state.board_string

        # Check that board string contains expected elements
        assert "8 |" in board_string  # Row number
        assert "1 |" in board_string  # Row number
        assert "a b c d e f g h" in board_string  # Column labels
        assert "b" in board_string  # Black pieces
        assert "r" in board_string  # Red pieces
        assert "." in board_string  # Empty squares

        # Check line structure
        lines = board_string.split("\n")
        assert len(lines) == 9  # 8 board rows + 1 column labels

        # Check that each board row starts with a number
        for i in range(8):
            assert lines[i].startswith(f"{8-i} |")

    def test_checkers_state_custom_board_string(self) -> None:
        """Test board string with custom board configuration."""
        # Create a simple test board
        test_board = [[0 for _ in range(8)] for _ in range(8)]
        test_board[0][0] = 1  # Red piece at a8
        test_board[0][2] = 2  # Red king at c8
        test_board[7][1] = 3  # Black piece at b1
        test_board[7][3] = 4  # Black king at d1

        board_string = CheckersState._create_board_string(test_board)

        lines = board_string.split("\n")

        # Check top row (rank 8)
        assert "r" in lines[0]  # Red piece
        assert "R" in lines[0]  # Red king

        # Check bottom row (rank 1)
        assert "b" in lines[7]  # Black piece
        assert "B" in lines[7]  # Black king

    def test_checkers_state_get_symbol(self) -> None:
        """Test the _get_symbol class method."""
        assert CheckersState._get_symbol(0) == "."
        assert CheckersState._get_symbol(1) == "r"
        assert CheckersState._get_symbol(2) == "R"
        assert CheckersState._get_symbol(3) == "b"
        assert CheckersState._get_symbol(4) == "B"

    def test_checkers_state_initialize_class_method(self) -> None:
        """Test the initialize class method."""
        state = CheckersState.initialize()

        # Should create a state with default starting position
        assert state.turn == "red"
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert len(state.move_history) == 0

        # Check board setup
        assert len(state.board) == 8
        assert all(len(row) == 8 for row in state.board)

        # Verify standard starting position
        # Top rows should have black pieces
        black_pieces_count = sum(
            1 for row in state.board[:3] for cell in row if cell == 3
        )
        assert black_pieces_count == 12

        # Bottom rows should have red pieces
        red_pieces_count = sum(
            1 for row in state.board[5:] for cell in row if cell == 1
        )
        assert red_pieces_count == 12

        # Middle rows should be empty
        middle_pieces = sum(1 for row in state.board[3:5] for cell in row if cell != 0)
        assert middle_pieces == 0

    def test_checkers_state_board_validation(self) -> None:
        """Test board structure validation."""
        # Valid board should work
        valid_board = [[0 for _ in range(8)] for _ in range(8)]
        state = CheckersState(board=valid_board)
        assert len(state.board) == 8

        # Test with pieces
        valid_board[0][0] = 1
        valid_board[1][1] = 2
        valid_board[2][2] = 3
        valid_board[3][3] = 4
        state = CheckersState(board=valid_board)
        assert state.board[0][0] == 1
        assert state.board[1][1] == 2
        assert state.board[2][2] == 3
        assert state.board[3][3] == 4

    def test_checkers_state_piece_values(self) -> None:
        """Test that all valid piece values are accepted."""
        board = [[0 for _ in range(8)] for _ in range(8)]

        # Test all valid piece values
        valid_values = [0, 1, 2, 3, 4]
        for i, value in enumerate(valid_values):
            board[0][i] = value

        state = CheckersState(board=board)
        for i, expected_value in enumerate(valid_values):
            assert state.board[0][i] == expected_value

    def test_checkers_state_turn_validation(self) -> None:
        """Test turn field validation."""
        # Valid turns
        state1 = CheckersState(turn="red")
        assert state1.turn == "red"

        state2 = CheckersState(turn="black")
        assert state2.turn == "black"

    def test_checkers_state_game_status_validation(self) -> None:
        """Test game status field validation."""
        # Valid statuses
        state1 = CheckersState(game_status="ongoing")
        assert state1.game_status == "ongoing"

        state2 = CheckersState(game_status="game_over")
        assert state2.game_status == "game_over"

    def test_checkers_state_winner_validation(self) -> None:
        """Test winner field validation."""
        # Valid winners
        state1 = CheckersState(winner=None)
        assert state1.winner is None

        state2 = CheckersState(winner="red")
        assert state2.winner == "red"

        state3 = CheckersState(winner="black")
        assert state3.winner == "black"

    def test_checkers_state_move_history_tracking(self) -> None:
        """Test move history tracking."""
        move1 = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )

        move2 = CheckersMove(
            from_position="c5",
            to_position="d6",
            player="black",
        )

        state = CheckersState(move_history=[move1, move2])

        assert len(state.move_history) == 2
        assert state.move_history[0] == move1
        assert state.move_history[1] == move2

    def test_checkers_state_analysis_tracking(self) -> None:
        """Test analysis tracking for both players."""
        red_analysis = CheckersAnalysis(
            material_advantage="Red ahead",
            control_of_center="Red controls center",
            suggested_moves=["e3-f4"],
            positional_evaluation="Red winning",
        )

        black_analysis = CheckersAnalysis(
            material_advantage="Black behind",
            control_of_center="Black needs center",
            suggested_moves=["b6-c5"],
            positional_evaluation="Black struggling",
        )

        state = CheckersState(
            red_analysis=[red_analysis],
            black_analysis=[black_analysis],
        )

        assert len(state.red_analysis) == 1
        assert len(state.black_analysis) == 1
        assert state.red_analysis[0] == red_analysis
        assert state.black_analysis[0] == black_analysis

    def test_checkers_state_captured_pieces_tracking(self) -> None:
        """Test captured pieces tracking."""
        captured_pieces = {
            "red": ["b6", "d6", "f6"],
            "black": ["a3", "c3"],
        }

        state = CheckersState(captured_pieces=captured_pieces)

        assert len(state.captured_pieces["red"]) == 3
        assert len(state.captured_pieces["black"]) == 2
        assert "b6" in state.captured_pieces["red"]
        assert "a3" in state.captured_pieces["black"]

    def test_checkers_state_default_board_structure(self) -> None:
        """Test the structure of the default board."""
        board = CheckersState._default_board()

        # Check board dimensions
        assert len(board) == 8
        assert all(len(row) == 8 for row in board)

        # Check starting positions in detail
        # Row 0 (rank 8): Black pieces on dark squares
        expected_row_0 = [0, 3, 0, 3, 0, 3, 0, 3]
        assert board[0] == expected_row_0

        # Row 1 (rank 7): Black pieces on dark squares
        expected_row_1 = [3, 0, 3, 0, 3, 0, 3, 0]
        assert board[1] == expected_row_1

        # Row 2 (rank 6): Black pieces on dark squares
        expected_row_2 = [0, 3, 0, 3, 0, 3, 0, 3]
        assert board[2] == expected_row_2

        # Rows 3-4 (ranks 5-4): Empty
        assert board[3] == [0] * 8
        assert board[4] == [0] * 8

        # Row 5 (rank 3): Red pieces on dark squares
        expected_row_5 = [1, 0, 1, 0, 1, 0, 1, 0]
        assert board[5] == expected_row_5

        # Row 6 (rank 2): Red pieces on dark squares
        expected_row_6 = [0, 1, 0, 1, 0, 1, 0, 1]
        assert board[6] == expected_row_6

        # Row 7 (rank 1): Red pieces on dark squares
        expected_row_7 = [1, 0, 1, 0, 1, 0, 1, 0]
        assert board[7] == expected_row_7

    def test_checkers_state_board_string_coordinates(self) -> None:
        """Test that board string has correct coordinate labels."""
        state = CheckersState()
        board_string = state.board_string

        lines = board_string.split("\n")

        # Check row numbers (8 down to 1)
        for i in range(8):
            expected_rank = 8 - i
            assert lines[i].startswith(f"{expected_rank} |")

        # Check column labels
        col_line = lines[8]  # Last line
        assert "a b c d e f g h" in col_line

    def test_checkers_state_empty_board_string(self) -> None:
        """Test board string representation of an empty board."""
        empty_board = [[0 for _ in range(8)] for _ in range(8)]
        board_string = CheckersState._create_board_string(empty_board)

        # Should contain only dots and coordinates
        assert "r" not in board_string
        assert "R" not in board_string
        assert "b" not in board_string
        assert "B" not in board_string

        # Should still have structure
        assert "8 |" in board_string
        assert "1 |" in board_string
        assert "a b c d e f g h" in board_string

        # Should be mostly dots
        dot_count = board_string.count(".")
        assert dot_count == 64  # 8x8 empty squares

    def test_checkers_state_mixed_pieces_board_string(self) -> None:
        """Test board string with various piece types."""
        mixed_board = [[0 for _ in range(8)] for _ in range(8)]
        mixed_board[0][0] = 1  # Red piece
        mixed_board[0][2] = 2  # Red king
        mixed_board[0][4] = 3  # Black piece
        mixed_board[0][6] = 4  # Black king

        board_string = CheckersState._create_board_string(mixed_board)

        # Check that all piece types appear
        assert "r" in board_string  # Red piece
        assert "R" in board_string  # Red king
        assert "b" in board_string  # Black piece
        assert "B" in board_string  # Black king
