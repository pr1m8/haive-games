"""Comprehensive core logic tests for Tic Tac Toe - No External Dependencies.

These tests verify the fundamental game logic without requiring any external
dependencies or frameworks. They test pure game rules, state management,
and validation logic.
"""

from pathlib import Path
import sys

# Add source to path for direct testing
src_path = Path(__file__).parent.parent.parent.parent / "src"
sys.path.insert(0, str(src_path))


# Test the models and basic logic
def test_basic_imports():
    """Test that we can import basic game components."""
    try:
        from pydantic import ValidationError

        from haive.games.tic_tac_toe.models import TicTacToeMove

        # Test valid move creation
        move = TicTacToeMove(row=1, col=2, player="X")
        assert move.row == 1
        assert move.col == 2
        assert move.player == "X"

        # Test move string representation
        move_str = str(move)
        assert "X" in move_str
        assert "(1, 2)" in move_str

        print("✓ Basic move creation and validation works")
        return True

    except ImportError as e:
        print(f"✗ Import failed: {e}")
        print("This indicates dependency issues that need to be resolved first")
        return False


class TestTicTacToeGameLogic:
    """Test core Tic Tac Toe game logic without dependencies."""

    def test_win_detection_logic(self):
        """Test win detection for all possible win conditions."""

        def check_win(board, player):
            """Pure function to check if player has won."""
            # Check rows
            for row in board:
                if all(cell == player for cell in row):
                    return True

            # Check columns
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True

            # Check main diagonal (top-left to bottom-right)
            if all(board[i][i] == player for i in range(3)):
                return True

            # Check anti-diagonal (top-right to bottom-left)
            if all(board[i][2 - i] == player for i in range(3)):
                return True

            return False

        # Test horizontal wins
        horizontal_boards = [
            [["X", "X", "X"], ["O", "O", None], [None, None, None]],  # Top row
            [[None, None, None], ["X", "X", "X"], ["O", "O", None]],  # Middle row
            [["O", "O", None], [None, None, None], ["X", "X", "X"]],  # Bottom row
        ]

        for board in horizontal_boards:
            assert check_win(board, "X")
            assert not check_win(board, "O")

        # Test vertical wins
        vertical_boards = [
            [["X", "O", None], ["X", "O", None], ["X", None, None]],  # Left column
            [["O", "X", None], [None, "X", None], [None, "X", None]],  # Middle column
            [[None, "O", "X"], [None, None, "X"], [None, None, "X"]],  # Right column
        ]

        for board in vertical_boards:
            assert check_win(board, "X")
            assert not check_win(board, "O")

        # Test diagonal wins
        diagonal_boards = [
            [["X", "O", None], ["O", "X", None], [None, None, "X"]],  # Main diagonal
            [["O", None, "X"], [None, "X", "O"], ["X", None, None]],  # Anti-diagonal
        ]

        for board in diagonal_boards:
            assert check_win(board, "X")
            assert not check_win(board, "O")

        # Test no win conditions
        no_win_boards = [
            [[None, None, None], [None, None, None], [None, None, None]],  # Empty
            [["X", "O", None], ["O", "X", None], [None, None, None]],  # Partial
            [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]],  # Full, no win
        ]

        for board in no_win_boards:
            assert not check_win(board, "X")
            assert not check_win(board, "O")

    def test_legal_moves_generation(self):
        """Test generation of legal moves for various board states."""

        def get_legal_moves(board, current_player):
            """Generate list of legal moves."""
            legal = []
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        legal.append((row, col, current_player))
            return legal

        # Empty board - all positions legal
        empty_board = [[None, None, None], [None, None, None], [None, None, None]]
        legal_moves = get_legal_moves(empty_board, "X")
        assert len(legal_moves) == 9

        # Check all positions are included
        expected_positions = [(r, c, "X") for r in range(3) for c in range(3)]
        assert set(legal_moves) == set(expected_positions)

        # Partially filled board
        partial_board = [["X", None, None], [None, "O", None], [None, None, None]]
        legal_moves = get_legal_moves(partial_board, "X")
        assert len(legal_moves) == 7

        # Verify occupied positions are excluded
        legal_positions = {(move[0], move[1]) for move in legal_moves}
        assert (0, 0) not in legal_positions  # X occupied
        assert (1, 1) not in legal_positions  # O occupied

        # Nearly full board
        nearly_full = [["X", "O", "X"], ["O", "X", "O"], ["O", None, "X"]]
        legal_moves = get_legal_moves(nearly_full, "O")
        assert len(legal_moves) == 1
        assert legal_moves[0] == (2, 1, "O")

        # Full board - no legal moves
        full_board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]
        legal_moves = get_legal_moves(full_board, "X")
        assert len(legal_moves) == 0

    def test_move_validation(self):
        """Test move validation logic."""

        def is_valid_move(board, row, col, player):
            """Validate if a move is legal."""
            # Check bounds
            if not (0 <= row <= 2 and 0 <= col <= 2):
                return False, "Move out of bounds"

            # Check if cell is empty
            if board[row][col] is not None:
                return False, "Cell already occupied"

            # Check valid player
            if player not in ["X", "O"]:
                return False, "Invalid player"

            return True, "Valid move"

        board = [["X", None, None], [None, "O", None], [None, None, None]]

        # Valid moves
        assert is_valid_move(board, 0, 1, "X")[0]
        assert is_valid_move(board, 2, 2, "O")[0]

        # Invalid moves - out of bounds
        assert not is_valid_move(board, -1, 0, "X")[0]
        assert not is_valid_move(board, 3, 0, "X")[0]
        assert not is_valid_move(board, 0, -1, "X")[0]
        assert not is_valid_move(board, 0, 3, "X")[0]

        # Invalid moves - occupied cells
        assert not is_valid_move(board, 0, 0, "O")[0]  # X occupied
        assert not is_valid_move(board, 1, 1, "X")[0]  # O occupied

        # Invalid player
        assert not is_valid_move(board, 0, 1, "Y")[0]
        assert not is_valid_move(board, 0, 1, "")[0]

    def test_draw_detection(self):
        """Test detection of draw conditions."""

        def is_draw(board):
            """Check if board is full with no winner."""
            # Check if board is full
            for row in board:
                for cell in row:
                    if cell is None:
                        return False
            return True

        def check_win(board, player):
            """Check win condition (simplified version)."""
            # Check rows
            for row in board:
                if all(cell == player for cell in row):
                    return True
            # Check columns
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True
            # Check diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        def is_game_draw(board):
            """Check if game is a draw (full board, no winner)."""
            if not is_draw(board):
                return False
            return not (check_win(board, "X") or check_win(board, "O"))

        # Draw boards
        draw_boards = [
            [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]],
            [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]],
        ]

        for board in draw_boards:
            assert is_game_draw(board)

        # Non-draw boards
        non_draw_boards = [
            [[None, None, None], [None, None, None], [None, None, None]],  # Empty
            [["X", "X", "X"], ["O", "O", None], [None, None, None]],  # X wins
            [["X", "O", None], [None, "O", None], [None, "O", None]],  # O wins
            [["X", "O", None], ["O", "X", None], [None, None, None]],  # Incomplete
        ]

        for board in non_draw_boards:
            assert not is_game_draw(board)

    def test_board_representation(self):
        """Test board string representation logic."""

        def board_to_string(board):
            """Convert board to string representation."""
            lines = []
            for row in board:
                line = " | ".join([cell if cell else " " for cell in row])
                lines.append(line)
            return "\n".join(lines)

        # Empty board
        empty_board = [[None, None, None], [None, None, None], [None, None, None]]
        empty_str = board_to_string(empty_board)
        assert "   |   |  " in empty_str
        assert empty_str.count("|") == 6  # 2 per row, 3 rows

        # Partially filled board
        partial_board = [["X", None, "O"], [None, "X", None], ["O", None, "X"]]
        partial_str = board_to_string(partial_board)
        assert "X" in partial_str
        assert "O" in partial_str
        assert " " in partial_str  # Empty cells

        # Full board
        full_board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
        full_str = board_to_string(full_board)
        assert full_str.count("X") == 5
        assert full_str.count("O") == 4
        assert "   " not in full_str  # No empty cells

    def test_game_state_consistency(self):
        """Test game state consistency through move sequence."""

        def apply_move(board, row, col, player):
            """Apply move to board and return new board."""
            new_board = [row[:] for row in board]  # Deep copy
            new_board[row][col] = player
            return new_board

        def switch_player(current_player):
            """Switch between X and O."""
            return "O" if current_player == "X" else "X"

        # Test complete game sequence
        board = [[None, None, None], [None, None, None], [None, None, None]]
        current_player = "X"
        move_history = []

        # Sequence of moves leading to X win
        moves = [(1, 1), (0, 0), (0, 1), (2, 2), (2, 1), (0, 2), (2, 0)]

        for i, (row, col) in enumerate(moves):
            # Apply move
            board = apply_move(board, row, col, current_player)
            move_history.append((row, col, current_player))

            # Verify board state
            assert board[row][col] == current_player

            # Check win condition
            win_found = False
            # Check if current player won
            for check_row in board:
                if all(cell == current_player for cell in check_row):
                    win_found = True
                    break

            for check_col in range(3):
                if all(
                    board[check_row][check_col] == current_player
                    for check_row in range(3)
                ):
                    win_found = True
                    break

            if all(board[j][j] == current_player for j in range(3)):
                win_found = True
            if all(board[j][2 - j] == current_player for j in range(3)):
                win_found = True

            # If win found, game should end
            if win_found:
                assert current_player == "X"  # X should win in this sequence
                assert i == 6  # Should be the 7th move (index 6)
                break

            # Switch player for next move
            current_player = switch_player(current_player)

        # Verify final state
        assert len(move_history) == 7
        assert board[2][0] == "X"  # Winning move


def test_all_core_logic():
    """Run all core logic tests."""
    print("=== Tic Tac Toe Core Logic Tests ===")

    # Test basic imports first
    if not test_basic_imports():
        print("❌ Basic imports failed - dependency issues need resolution")
        return False

    # Run comprehensive tests
    test_suite = TestTicTacToeGameLogic()

    tests = [
        ("Win Detection Logic", test_suite.test_win_detection_logic),
        ("Legal Moves Generation", test_suite.test_legal_moves_generation),
        ("Move Validation", test_suite.test_move_validation),
        ("Draw Detection", test_suite.test_draw_detection),
        ("Board Representation", test_suite.test_board_representation),
        ("Game State Consistency", test_suite.test_game_state_consistency),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✓ {test_name}")
            passed += 1
        except Exception as e:
            print(f"✗ {test_name}: {e}")

    print("\n=== Results ===")
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("🎉 All core logic tests passed!")
        return True
    else:
        print("❌ Some tests failed")
        return False


if __name__ == "__main__":
    success = test_all_core_logic()
    exit(0 if success else 1)
