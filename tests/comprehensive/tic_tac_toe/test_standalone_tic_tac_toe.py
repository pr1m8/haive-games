#!/usr/bin/env python3
"""Standalone Tic Tac Toe test to get the game working without external dependencies.

This script will test the basic functionality of the Tic Tac Toe game
to ensure we can get at least a working implementation.
"""

import os
import sys
from pathlib import Path

# Add the source directory to Python path
project_root = Path(__file__).parent.parent.parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))


def test_basic_tic_tac_toe_models():
    """Test basic Tic Tac Toe model imports and functionality."""
    print("=== Testing Basic Tic Tac Toe Models ===")

    try:
        # Try importing the basic models
        from haive.games.tic_tac_toe.models import TicTacToeMove

        print("✓ Successfully imported TicTacToeMove")

        # Test creating a move
        move = TicTacToeMove(row=1, col=2, player="X")
        print(f"✓ Created move: {move}")

        # Test move validation
        try:
            invalid_move = TicTacToeMove(row=5, col=2, player="X")
            print("✗ Invalid move creation should have failed")
            return False
        except Exception as e:
            print(f"✓ Invalid move correctly rejected: {e}")

        return True

    except ImportError as e:
        print(f"✗ Failed to import models: {e}")
        return False


def test_basic_tic_tac_toe_state():
    """Test basic Tic Tac Toe state functionality."""
    print("\n=== Testing Basic Tic Tac Toe State ===")

    try:
        from haive.games.tic_tac_toe.state import TicTacToeState

        print("✓ Successfully imported TicTacToeState")

        # Create a basic state
        state = TicTacToeState(
            board=[[None, None, None], [None, None, None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="Player1",
            player_O="Player2",
        )
        print(f"✓ Created basic state: turn={state.turn}, status={state.game_status}")

        # Test board string representation
        board_str = state.board_string
        print(f"✓ Board string representation works")
        print(f"Board:\n{board_str}")

        return True

    except ImportError as e:
        print(f"✗ Failed to import state: {e}")
        return False


def test_basic_tic_tac_toe_state_manager():
    """Test basic Tic Tac Toe state manager functionality."""
    print("\n=== Testing Basic Tic Tac Toe State Manager ===")

    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        print("✓ Successfully imported TicTacToeStateManager")

        # Initialize a game
        initial_state = TicTacToeStateManager.initialize(
            first_player="X", player_X="Player1", player_O="Player2"
        )
        print(f"✓ Initialized game: {initial_state.turn}, {initial_state.game_status}")

        # Get legal moves
        legal_moves = TicTacToeStateManager.get_legal_moves(initial_state)
        print(f"✓ Found {len(legal_moves)} legal moves")

        # Make a move
        if legal_moves:
            first_move = legal_moves[0]
            new_state = TicTacToeStateManager.apply_move(initial_state, first_move)
            print(f"✓ Applied move: {first_move}")
            print(f"✓ New state: turn={new_state.turn}, status={new_state.game_status}")
            print(f"Board after move:\n{new_state.board_string}")

        return True

    except ImportError as e:
        print(f"✗ Failed to import state manager: {e}")
        return False


def run_all_tests():
    """Run all standalone tests."""
    print("🎮 Starting Standalone Tic Tac Toe Tests\n")

    tests = [
        ("Basic Models", test_basic_tic_tac_toe_models),
        ("Basic State", test_basic_tic_tac_toe_state),
        ("Basic State Manager", test_basic_tic_tac_toe_state_manager),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            result = test_func()
            if result:
                passed += 1
                print(f"✅ {test_name} - PASSED")
            else:
                print(f"❌ {test_name} - FAILED")
        except Exception as e:
            print(f"❌ {test_name} - ERROR: {e}")
            import traceback

            traceback.print_exc()

    print(f"\n=== Final Results ===")
    print(f"Tests Passed: {passed}/{total}")

    if passed == total:
        print("🎉 All tests passed! Basic Tic Tac Toe functionality is working.")
        return True
    else:
        print("❌ Some tests failed. Dependency issues need to be resolved.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
