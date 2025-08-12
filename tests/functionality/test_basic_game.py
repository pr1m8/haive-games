#!/usr/bin/env python3
"""Test basic game functionality without LLM dependencies."""

from pathlib import Path
import sys

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_nim_game():
    """Test basic Nim game functionality."""
    print("\n=== Testing Nim Game ===")
    try:
        from haive.games.nim.state_manager import NimStateManager

        # Create a simple game state
        state = NimStateManager.initialize(pile_sizes=[3, 5, 7])
        print(f"✓ Initialized Nim game with piles: {state.piles}")

        # Get legal moves
        legal_moves = NimStateManager.get_legal_moves(state)
        print(f"✓ Found {len(legal_moves)} legal moves")

        # Make a move
        if legal_moves:
            move = legal_moves[0]
            command = NimStateManager.make_move(state, "player1", move)
            new_state = command.state
            print(f"✓ Made move: Take {move.stones_to_remove} from pile {move.pile_index}")
            print(f"✓ New piles: {new_state.piles}")

        return True
    except Exception as e:
        print(f"✗ Nim test failed: {e}")
        return False


def test_tic_tac_toe_game():
    """Test basic Tic Tac Toe functionality."""
    print("\n=== Testing Tic Tac Toe ===")
    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        # Create initial state
        state = TicTacToeStateManager.initialize()
        print("✓ Initialized empty Tic Tac Toe board")

        # Make some moves
        moves = [
            TicTacToeMove(row=1, col=1, player="X"),  # Center
            TicTacToeMove(row=0, col=0, player="O"),  # Top-left
            TicTacToeMove(row=0, col=1, player="X"),  # Top-center
        ]

        current_state = state
        for move in moves:
            current_state = TicTacToeStateManager.make_move(current_state, move)
            print(f"✓ {move.player} played at ({move.row}, {move.col})")

        # Check game status
        print(f"✓ Game status: {current_state.game_status}")
        print(f"✓ Current turn: {current_state.turn}")

        return True
    except Exception as e:
        print(f"✗ Tic Tac Toe test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_connect4_game():
    """Test basic Connect4 functionality."""
    print("\n=== Testing Connect4 ===")
    try:
        from haive.games.connect4.models import Connect4Move
        from haive.games.connect4.state_manager import Connect4StateManager

        # Create initial state
        state = Connect4StateManager.initialize()
        print("✓ Initialized empty Connect4 board (6x7)")

        # Make some moves
        moves = [3, 3, 4, 4, 5]  # Column indices
        players = ["X", "O", "X", "O", "X"]

        current_state = state
        for col, player in zip(moves, players, strict=False):
            move = Connect4Move(column=col, player=player)
            current_state = Connect4StateManager.make_move(current_state, move)
            print(f"✓ {player} dropped piece in column {col}")

        # Check legal moves
        legal_moves = Connect4StateManager.get_legal_moves(current_state)
        print(f"✓ {len(legal_moves)} columns still available")

        return True
    except Exception as e:
        print(f"✗ Connect4 test failed: {e}")
        return False


def test_chess_game():
    """Test basic Chess functionality."""
    print("\n=== Testing Chess ===")
    try:
        from haive.games.chess.models import ChessMove
        from haive.games.chess.state_manager import ChessStateManager

        # Create initial state
        state = ChessStateManager.initialize()
        print("✓ Initialized chess board with starting position")

        # Test basic moves
        moves = [
            ChessMove(from_square="e2", to_square="e4", player="white"),  # King's pawn
            ChessMove(from_square="e7", to_square="e5", player="black"),  # King's pawn
        ]

        current_state = state
        for move in moves:
            print(f"  Attempting: {move.player} {move.from_square}-{move.to_square}")
            try:
                current_state = ChessStateManager.make_move(current_state, move)
                print(f"✓ {move.player} moved {move.from_square} to {move.to_square}")
            except Exception as e:
                print(f"  Move failed: {e}")

        return True
    except Exception as e:
        print(f"✗ Chess test failed: {e}")
        return False


def main():
    """Run all game tests."""
    print("=== Haive Games Basic Functionality Tests ===")
    print("Testing games without LLM dependencies...\n")

    tests = [
        test_nim_game,
        test_tic_tac_toe_game,
        test_connect4_game,
        test_chess_game,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
            failed += 1

    print("\n=== Test Summary ===")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total: {passed + failed}")

    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
