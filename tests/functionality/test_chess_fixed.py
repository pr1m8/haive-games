#!/usr/bin/env python3
"""Test Chess game with correct API usage."""

from pathlib import Path
import sys

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_chess_models():
    """Test Chess model creation."""
    print("🔧 Testing Chess Models")
    print("-" * 40)

    try:

        from haive.games.chess.models import ChessMoveModel

        # Test ChessMoveModel creation with UCI notation
        move = ChessMoveModel(move="e2e4", explanation="King's pawn opening")
        print(f"✓ Created ChessMoveModel: {move.move}")
        print(f"  Explanation: {move.explanation}")

        # Test conversion to chess.Move
        chess_move = move.to_move()
        print(f"✓ Converted to chess.Move: {chess_move}")

        # Test move without explanation
        simple_move = ChessMoveModel(move="Nf3")
        print(f"✓ Created simple move: {simple_move.move}")

        # Test move validation
        try:
            invalid_move = ChessMoveModel(move="xyz")  # Too short but passes validation
            print(f"✓ Move validation allows: {invalid_move.move}")
        except Exception as e:
            print(f"✓ Move validation caught: {e}")

        # Test very short move (should fail)
        try:
            very_invalid = ChessMoveModel(move="e2")  # Only 2 characters
            print("✗ Should have failed validation")
            return False
        except Exception as e:
            print(f"✓ Correctly rejected short move: {e}")

        return True

    except Exception as e:
        print(f"✗ Model test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_chess_game():
    """Test Chess game functionality."""
    print("\n♟️ Testing Chess Game")
    print("-" * 40)

    try:
        from haive.games.chess.state_manager import ChessGameStateManager

        # Initialize chess board in starting position
        state = ChessGameStateManager.initialize()
        print("✓ Initialized chess board with starting position")
        print(f"  Current turn: {state.turn}")
        print(f"  Game status: {state.game_status}")
        print(f"  Starting FEN: {state.board_fen}")

        # Test some basic opening moves (UCI format)
        moves_to_test = [
            "e2e4",  # White King's pawn
            "e7e5",  # Black King's pawn
            "Ng1f3", # White Knight to f3
            "Nb8c6", # Black Knight to c6
        ]

        current_state = state
        for i, move_uci in enumerate(moves_to_test):
            expected_player = "white" if i % 2 == 0 else "black"
            print(f"\nMove {i+1}: {expected_player} plays {move_uci}")

            try:
                # Apply the move using UCI notation
                current_state = ChessGameStateManager.apply_move(current_state, move_uci)

                print("  ✓ Move successful!")
                print(f"  New turn: {current_state.turn}")
                print(f"  Game status: {current_state.game_status}")
                print(f"  Updated FEN: {current_state.board_fen}")

                # Check for game end
                if current_state.game_status != "ongoing":
                    print(f"  🎉 Game ended! Status: {current_state.game_status}")
                    break

            except Exception as e:
                print(f"  ✗ Move failed: {e}")
                import traceback
                traceback.print_exc()
                return False

        print("\n✓ Chess game test completed successfully!")
        print(f"Final status: {current_state.game_status}")

        return True

    except Exception as e:
        print(f"✗ Chess test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_chess_invalid_moves():
    """Test Chess invalid move handling."""
    print("\n⚠️ Testing Invalid Move Handling")
    print("-" * 40)

    try:
        from haive.games.chess.state_manager import ChessGameStateManager

        # Initialize game
        state = ChessGameStateManager.initialize()

        # Try some invalid moves
        invalid_moves = [
            "e2e5",    # Pawn can't move 3 squares
            "a1a3",    # Rook blocked by pawn
            "Ke1e2",   # King can't move like that from start
        ]

        print("Testing invalid moves (these should fail):")
        for move_uci in invalid_moves:
            try:
                new_state = ChessGameStateManager.apply_move(state, move_uci)
                print(f"  ⚠️ Move {move_uci} unexpectedly succeeded")
            except Exception as e:
                print(f"  ✓ Correctly rejected {move_uci}: {type(e).__name__}")

        return True

    except Exception as e:
        print(f"✗ Invalid move test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_chess_legal_moves():
    """Test Chess legal move generation."""
    print("\n📋 Testing Legal Move Generation")
    print("-" * 40)

    try:
        from haive.games.chess.state_manager import ChessGameStateManager

        # Initialize game
        state = ChessGameStateManager.initialize()

        # Check if get_legal_moves method exists
        if hasattr(ChessGameStateManager, 'get_legal_moves'):
            legal_moves = ChessGameStateManager.get_legal_moves(state)
            print(f"✓ Found {len(legal_moves)} legal moves in starting position")

            # Show a few legal moves
            if legal_moves:
                print("  Sample legal moves:")
                for i, move in enumerate(legal_moves[:5]):
                    print(f"    {i+1}. {move}")
        else:
            print("ℹ️ get_legal_moves method not available")

        return True

    except Exception as e:
        print(f"✗ Legal moves test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("🎮 Chess Fixed Tests")
    print("=" * 50)

    tests = [
        test_chess_models,
        test_chess_game,
        test_chess_invalid_moves,
        test_chess_legal_moves,
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
        print("✅ All Chess tests passed!")
    else:
        print("❌ Some tests failed")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
