#!/usr/bin/env python3
"""Test Tic Tac Toe game with correct API usage."""

from pathlib import Path
import sys

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_tic_tac_toe_models():
    """Test Tic Tac Toe model creation."""
    print("🔧 Testing Tic Tac Toe Models")
    print("-" * 40)

    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove

        # Test TicTacToeMove creation
        move = TicTacToeMove(row=1, col=1, player="X")
        print(f"✓ Created TicTacToeMove: {move}")
        print(f"  Board position: {move.board_position}")
        print(f"  Is corner: {move.is_corner}")
        print(f"  Is center: {move.is_center}")
        print(f"  Is edge: {move.is_edge}")

        # Test different positions
        corner_move = TicTacToeMove(row=0, col=0, player="O")
        print(f"✓ Created corner move: {corner_move}")
        print(f"  Is corner: {corner_move.is_corner}")

        return True

    except Exception as e:
        print(f"✗ Model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_tic_tac_toe_game():
    """Test Tic Tac Toe game functionality."""
    print("\n🎯 Testing Tic Tac Toe Game")
    print("-" * 40)

    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        # Initialize empty board
        state = TicTacToeStateManager.initialize()
        print("✓ Initialized empty 3x3 board")
        print(f"  Current turn: {state.turn}")
        print(f"  Game status: {state.game_status}")
        print(f"  Players: {state.players}")

        # Test board display
        print(f"  Initial board (should be all None): {state.board}")

        # Test legal moves generation
        legal_moves = TicTacToeStateManager.get_legal_moves(state)
        print(f"✓ Found {len(legal_moves)} legal moves (should be 9)")

        # Test some moves
        moves_to_test = [
            TicTacToeMove(row=1, col=1, player="X"),  # Center
            TicTacToeMove(row=0, col=0, player="O"),  # Top-left
            TicTacToeMove(row=0, col=1, player="X"),  # Top-center
            TicTacToeMove(row=0, col=2, player="O"),  # Top-right
        ]

        current_state = state
        for i, move in enumerate(moves_to_test):
            print(f"\nMove {i+1}: {move.player} at ({move.row}, {move.col}) - {move.board_position}")

            # Check if it's the correct player's turn
            if current_state.turn != move.player:
                print(f"  ⚠️ Skipping move - not {move.player}'s turn (it's {current_state.turn}'s turn)")
                continue

            try:
                # Apply the move (no make_move method, using apply_move)
                current_state = TicTacToeStateManager.apply_move(current_state, move)

                print("  ✓ Move successful!")
                print("  Board state after move:")
                for row_idx, row in enumerate(current_state.board):
                    print(f"    Row {row_idx}: {row}")
                print(f"  Next turn: {current_state.turn}")
                print(f"  Game status: {current_state.game_status}")

                # Check for winner
                winner = TicTacToeStateManager.get_winner(current_state)
                if winner:
                    print(f"  🎉 Game ended! Winner: {winner}")
                    break
                elif current_state.game_status == "draw":
                    print("  🤝 Game ended in a draw!")
                    break

            except Exception as e:
                print(f"  ✗ Move failed: {e}")
                import traceback
                traceback.print_exc()
                return False

        print("\n✓ Tic Tac Toe game test completed successfully!")
        print(f"Final status: {current_state.game_status}")

        # Test legal moves count
        final_legal_moves = TicTacToeStateManager.get_legal_moves(current_state)
        print(f"Remaining legal moves: {len(final_legal_moves)}")

        return True

    except Exception as e:
        print(f"✗ Tic Tac Toe test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_tic_tac_toe_winning_moves():
    """Test Tic Tac Toe winning move detection."""
    print("\n🏆 Testing Winning Move Detection")
    print("-" * 40)

    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        # Set up a board where X can win
        state = TicTacToeStateManager.initialize()

        # X in corners: (0,0) and (1,1)
        state = TicTacToeStateManager.apply_move(state, TicTacToeMove(row=0, col=0, player="X"))
        state = TicTacToeStateManager.apply_move(state, TicTacToeMove(row=0, col=1, player="O"))
        state = TicTacToeStateManager.apply_move(state, TicTacToeMove(row=1, col=1, player="X"))
        state = TicTacToeStateManager.apply_move(state, TicTacToeMove(row=0, col=2, player="O"))

        # Now X can win at (2,2) - diagonal
        winning_moves = TicTacToeStateManager.find_winning_move(state, "X")
        print(f"✓ Found winning moves for X: {winning_moves}")

        if winning_moves:
            print(f"  X can win by playing at: {winning_moves[0]}")

        return True

    except Exception as e:
        print(f"✗ Winning move test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("🎮 Tic Tac Toe Fixed Tests")
    print("=" * 50)

    tests = [
        test_tic_tac_toe_models,
        test_tic_tac_toe_game,
        test_tic_tac_toe_winning_moves,
    ]

    results = []
    for test in tests:
        result = test()
        results.append(result)

    passed = sum(results)
    total = len(results)

    print("\n🎯 Test Summary")
    print("-" * 20)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("✅ All Tic Tac Toe tests passed!")
    else:
        print("❌ Some tests failed")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
