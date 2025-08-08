#!/usr/bin/env python3
"""Test Tic Tac Toe models in isolation."""

import sys
from pathlib import Path

# Add source to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_models():
    """Test the basic model classes."""
    print("Testing Tic Tac Toe models...")

    try:
        # Test direct import without dependencies
        import pydantic

        print(f"✓ Pydantic available: {pydantic.__version__}")

        # Import the models file directly
        from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove

        print("✓ Successfully imported TicTacToe models")

        # Test TicTacToeMove
        move = TicTacToeMove(row=1, col=2, player="X")
        print(f"✓ Created move: {move}")

        # Test validation
        try:
            TicTacToeMove(row=5, col=1, player="X")  # Invalid row
            print("✗ Invalid move was accepted")
            return False
        except pydantic.ValidationError:
            print("✓ Invalid move correctly rejected")

        # Test TicTacToeAnalysis
        analysis = TicTacToeAnalysis(
            winning_moves=[{"row": 0, "col": 0}],
            blocking_moves=[{"row": 1, "col": 1}],
            center_available=False,
            corner_available=True,
            position_evaluation="unclear",
            strategy="Take the corner",
        )
        print(f"✓ Created analysis with {len(analysis.winning_moves)} winning moves")

        return True

    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False


def test_state_basic():
    """Test basic state creation."""
    print("\nTesting basic state creation...")

    try:
        # Create a minimal state implementation

        from pydantic import BaseModel

        class SimpleTicTacToeState(BaseModel):
            """Simplified state for testing."""

            board: list[list[str | None]]
            turn: str
            game_status: str
            player_X: str
            player_O: str
            winner: str | None = None

            @property
            def board_string(self) -> str:
                """Create a string representation of the board."""
                lines = []
                for row in self.board:
                    line = " | ".join([cell if cell else " " for cell in row])
                    lines.append(line)
                return "\n".join(lines)

        # Test state creation
        state = SimpleTicTacToeState(
            board=[[None, None, None], [None, "X", None], [None, None, None]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        print("✓ Created basic state")
        print(f"✓ Board string:\n{state.board_string}")

        return True

    except Exception as e:
        print(f"✗ State test failed: {e}")
        return False


def test_basic_game_logic():
    """Test basic game logic without dependencies."""
    print("\nTesting basic game logic...")

    try:
        # Simple win detection
        def check_win(board, player):
            """Check if player has won."""
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

        # Test winning positions
        win_board = [["X", "X", "X"], ["O", "O", None], [None, None, None]]
        assert check_win(win_board, "X")
        assert not check_win(win_board, "O")
        print("✓ Win detection works correctly")

        # Test legal moves
        def get_legal_positions(board):
            """Get legal move positions."""
            legal = []
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        legal.append((row, col))
            return legal

        empty_board = [[None, None, None], [None, None, None], [None, None, None]]
        legal_moves = get_legal_positions(empty_board)
        assert len(legal_moves) == 9
        print(f"✓ Found {len(legal_moves)} legal moves on empty board")

        partial_board = [["X", None, None], [None, "O", None], [None, None, None]]
        legal_moves = get_legal_positions(partial_board)
        assert len(legal_moves) == 7
        print(f"✓ Found {len(legal_moves)} legal moves on partial board")

        return True

    except Exception as e:
        print(f"✗ Game logic test failed: {e}")
        return False


def main():
    """Run all isolated tests."""
    print("=== Isolated Tic Tac Toe Tests ===")

    results = []
    results.append(test_models())
    results.append(test_state_basic())
    results.append(test_basic_game_logic())

    passed = sum(results)
    total = len(results)

    print("\n=== Results ===")
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("🎉 All isolated tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


if __name__ == "__main__":
    exit(main())
