#!/usr/bin/env python3
"""Test Connect4 game with correct API usage."""

from pathlib import Path
import sys

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_connect4_models():
    """Test Connect4 model creation."""
    print("🔧 Testing Connect4 Models")
    print("-" * 40)

    try:
        from haive.games.connect4.models import Connect4Move

        # Test Connect4Move creation
        move = Connect4Move(column=3, explanation="Control the center")
        print(f"✓ Created Connect4Move: {move}")
        print(f"  Column: {move.column}")
        print(f"  Explanation: {move.explanation}")

        # Test move without explanation
        simple_move = Connect4Move(column=0)
        print(f"✓ Created simple move: {simple_move}")

        # Test column validation
        try:
            invalid_move = Connect4Move(column=8)  # Should fail
            print("✗ Invalid move validation failed")
            return False
        except ValueError as e:
            print(f"✓ Column validation working: {e}")

        return True

    except Exception as e:
        print(f"✗ Model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_connect4_game():
    """Test Connect4 game functionality."""
    print("\n🔴 Testing Connect4 Game")
    print("-" * 40)

    try:
        from haive.games.connect4.models import Connect4Move
        from haive.games.connect4.state_manager import Connect4StateManager

        # Initialize empty 6x7 board
        state = Connect4StateManager.initialize()
        print("✓ Initialized empty 6x7 board")
        print(f"  Starting player: {state.turn}")
        print(f"  Game status: {state.game_status}")
        print(f"  Board dimensions: {len(state.board)} rows x {len(state.board[0])} columns")

        # Test legal moves generation
        legal_moves = Connect4StateManager.get_legal_moves(state)
        print(f"✓ Found {len(legal_moves)} legal moves (should be 7 columns)")

        # Test some moves in the center columns
        moves_to_test = [
            Connect4Move(column=3, explanation="Center play"),      # Red
            Connect4Move(column=3, explanation="Stack on red"),     # Yellow (stacks on red)
            Connect4Move(column=4, explanation="Adjacent center"),  # Red
            Connect4Move(column=4, explanation="Block red"),        # Yellow
            Connect4Move(column=2, explanation="Left side"),        # Red
            Connect4Move(column=5, explanation="Right side"),       # Yellow
        ]

        current_state = state
        for i, move in enumerate(moves_to_test):
            print(f"\nMove {i+1}: {current_state.turn} plays column {move.column}")
            if move.explanation:
                print(f"  Strategy: {move.explanation}")

            try:
                # Apply the move
                current_state = Connect4StateManager.apply_move(current_state, move)

                print("  ✓ Move successful!")
                print(f"  Next turn: {current_state.turn}")
                print(f"  Game status: {current_state.game_status}")

                # Show board state (simplified)
                print("  Board preview (bottom 3 rows):")
                for row_idx in range(3, 6):  # Show bottom 3 rows only
                    row = current_state.board[row_idx]
                    row_display = []
                    for cell in row:
                        if cell is None:
                            row_display.append(".")
                        elif cell == "red":
                            row_display.append("R")
                        else:  # yellow
                            row_display.append("Y")
                    print(f"    Row {row_idx}: {' '.join(row_display)}")

                # Check for winner
                if current_state.game_status != "ongoing":
                    winner = current_state.winner
                    print(f"  🎉 Game ended! Status: {current_state.game_status}")
                    if winner:
                        print(f"  Winner: {winner}")
                    break

            except Exception as e:
                print(f"  ✗ Move failed: {e}")
                import traceback
                traceback.print_exc()
                return False

        print("\n✓ Connect4 game test completed successfully!")
        print(f"Final status: {current_state.game_status}")

        # Test remaining legal moves
        final_legal_moves = Connect4StateManager.get_legal_moves(current_state)
        print(f"Remaining legal moves: {len(final_legal_moves)}")

        return True

    except Exception as e:
        print(f"✗ Connect4 test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_connect4_column_full():
    """Test Connect4 column full detection."""
    print("\n📚 Testing Column Full Detection")
    print("-" * 40)

    try:
        from haive.games.connect4.models import Connect4Move
        from haive.games.connect4.state_manager import Connect4StateManager

        # Initialize game
        state = Connect4StateManager.initialize()

        # Fill column 0 completely (should take 6 moves, alternating players)
        print("Filling column 0 completely...")
        current_state = state
        for i in range(6):
            move = Connect4Move(column=0)
            current_state = Connect4StateManager.apply_move(current_state, move)
            print(f"  Move {i+1}: {['red', 'yellow'][i % 2]} in column 0")

        # Now column 0 should be full
        legal_moves = Connect4StateManager.get_legal_moves(current_state)
        print(f"✓ Legal moves after filling column 0: {len(legal_moves)} (should be 6)")

        # Verify column 0 is not in legal moves
        column_0_legal = any(move.column == 0 for move in legal_moves)
        if column_0_legal:
            print("✗ Column 0 should not be legal but is")
            return False
        else:
            print("✓ Column 0 correctly marked as full")

        return True

    except Exception as e:
        print(f"✗ Column full test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("🎮 Connect4 Fixed Tests")
    print("=" * 50)

    tests = [
        test_connect4_models,
        test_connect4_game,
        test_connect4_column_full,
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
        print("✅ All Connect4 tests passed!")
    else:
        print("❌ Some tests failed")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
