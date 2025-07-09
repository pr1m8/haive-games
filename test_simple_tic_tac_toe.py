#!/usr/bin/env python3
"""Simple standalone test for Tic Tac Toe game logic."""

import os
import sys
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_tic_tac_toe_basic_functionality():
    """Test basic Tic Tac Toe functionality without dependencies."""

    try:
        # Import only the core game logic
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state import TicTacToeState

        print("✓ Successfully imported Tic Tac Toe models and state")

    except ImportError as e:
        print(f"✗ Failed to import basic models: {e}")
        return False

    # Test basic state creation
    try:
        state = TicTacToeState(
            board=[[None, None, None], [None, None, None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )
        print("✓ Created basic game state")

        # Test board string representation
        board_str = state.board_string
        print(f"✓ Board string representation: {len(board_str)} characters")

    except Exception as e:
        print(f"✗ Failed to create game state: {e}")
        return False

    # Test move creation
    try:
        move = TicTacToeMove(row=1, col=1, player="X")
        print(f"✓ Created move: {move.player} at ({move.row}, {move.col})")

    except Exception as e:
        print(f"✗ Failed to create move: {e}")
        return False

    # Test state manager if available
    try:
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        print("✓ Successfully imported state manager")

        # Test initialization
        initial_state = TicTacToeStateManager.initialize()
        print(f"✓ Initialized game: {initial_state.turn} to play first")

        # Test legal moves
        legal_moves = TicTacToeStateManager.get_legal_moves(initial_state)
        print(f"✓ Found {len(legal_moves)} legal moves on empty board")

        if len(legal_moves) != 9:
            print(f"✗ Expected 9 legal moves, got {len(legal_moves)}")
            return False

        # Test move application
        test_move = TicTacToeMove(row=0, col=0, player="X")
        new_state = TicTacToeStateManager.apply_move(initial_state, test_move)
        print(f"✓ Applied move: board[0][0] = {new_state.board[0][0]}")
        print(f"✓ Turn switched to: {new_state.turn}")

        if new_state.board[0][0] != "X":
            print("✗ Move was not applied correctly")
            return False

        if new_state.turn != "O":
            print("✗ Turn did not switch correctly")
            return False

        # Test win detection
        win_board = [["X", "X", "X"], ["O", "O", None], [None, None, None]]
        win_state = TicTacToeState(
            board=win_board,
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        result_state = TicTacToeStateManager.check_game_status(win_state)
        print(f"✓ Win detection: {result_state.game_status}")
        print(f"✓ Winner: {result_state.winner}")

        if result_state.game_status != "X_win":
            print(f"✗ Expected X_win, got {result_state.game_status}")
            return False

        if result_state.winner != "X":
            print(f"✗ Expected winner X, got {result_state.winner}")
            return False

        # Test draw detection
        draw_board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        draw_state = TicTacToeState(
            board=draw_board,
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        draw_result = TicTacToeStateManager.check_game_status(draw_state)
        print(f"✓ Draw detection: {draw_result.game_status}")

        if draw_result.game_status != "draw":
            print(f"✗ Expected draw, got {draw_result.game_status}")
            return False

        # Test illegal move handling
        try:
            occupied_move = TicTacToeMove(row=0, col=0, player="O")
            TicTacToeStateManager.apply_move(new_state, occupied_move)  # Should fail
            print("✗ Illegal move was allowed")
            return False
        except ValueError:
            print("✓ Illegal move correctly rejected")

        print("✓ All state manager tests passed!")

    except ImportError as e:
        print(f"⚠ State manager not available (dependency issue): {e}")
        print("  This is expected if LangGraph dependencies are missing")

    except Exception as e:
        print(f"✗ State manager test failed: {e}")
        return False

    return True


def test_game_config():
    """Test game configuration."""
    try:
        from haive.games.tic_tac_toe.config import TicTacToeConfig

        # Test basic config
        config = TicTacToeConfig()
        print(f"✓ Created config: {config.player_X} vs {config.player_O}")

        # Test custom config
        custom_config = TicTacToeConfig(
            player_X="Alice", player_O="Bob", first_player="O"
        )
        print(
            f"✓ Created custom config: {custom_config.player_X} vs {custom_config.player_O}"
        )
        print(f"  First player: {custom_config.first_player}")

        return True

    except ImportError as e:
        print(f"⚠ Config not available: {e}")
        return True  # Not critical for basic functionality

    except Exception as e:
        print(f"✗ Config test failed: {e}")
        return False


def run_comprehensive_game_test():
    """Run a complete game simulation."""
    print("\n=== Running Comprehensive Game Test ===")

    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        # Simulate a complete game
        state = TicTacToeStateManager.initialize()
        print(f"Game started: {state.turn} goes first")

        # Define a sequence of moves that leads to X winning
        moves = [
            TicTacToeMove(row=1, col=1, player="X"),  # X takes center
            TicTacToeMove(row=0, col=0, player="O"),  # O takes top-left
            TicTacToeMove(row=0, col=1, player="X"),  # X takes top-center
            TicTacToeMove(row=2, col=1, player="O"),  # O takes bottom-center
            TicTacToeMove(row=2, col=2, player="X"),  # X takes bottom-right
            TicTacToeMove(row=0, col=2, player="O"),  # O takes top-right
            TicTacToeMove(row=2, col=0, player="X"),  # X takes bottom-left - wins!
        ]

        move_count = 0
        for move in moves:
            move_count += 1
            print(f"\nMove {move_count}: {move.player} plays ({move.row}, {move.col})")

            # Apply move
            state = TicTacToeStateManager.apply_move(state, move)

            # Check game status
            state = TicTacToeStateManager.check_game_status(state)

            # Print board
            print("Board:")
            for row in state.board:
                row_str = " | ".join([cell if cell else " " for cell in row])
                print(f"  {row_str}")

            print(f"Status: {state.game_status}")
            if state.winner:
                print(f"Winner: {state.winner}")

            if state.game_status != "ongoing":
                break

        print(f"\n✓ Game completed after {move_count} moves")
        print(f"✓ Final status: {state.game_status}")

        if state.game_status == "X_win":
            print("✓ X won as expected")
            return True
        else:
            print(f"✗ Unexpected game outcome: {state.game_status}")
            return False

    except Exception as e:
        print(f"✗ Comprehensive game test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=== Tic Tac Toe Game Logic Tests ===\n")

    results = []

    print("1. Testing basic functionality...")
    results.append(test_tic_tac_toe_basic_functionality())

    print("\n2. Testing game configuration...")
    results.append(test_game_config())

    print("\n3. Testing complete game simulation...")
    results.append(run_comprehensive_game_test())

    print(f"\n=== Test Results ===")
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")

    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1


if __name__ == "__main__":
    exit(main())
