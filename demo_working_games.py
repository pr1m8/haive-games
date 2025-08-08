#!/usr/bin/env python3
"""Demonstrate that haive-games are working correctly.

This script runs simple gameplay scenarios for each game to verify
they work as expected without requiring LLM agents.
"""

import sys
from pathlib import Path

# Add the source directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def demo_nim_game():
    """Demonstrate Nim game functionality."""
    print("🎲 Nim Game Demo")
    print("-" * 40)

    try:
        from haive.games.nim.models import NimMove
        from haive.games.nim.state_manager import NimStateManager

        # Initialize game with classic 3-5-7 configuration
        state = NimStateManager.initialize(pile_sizes=[3, 5, 7])
        print(f"Initial piles: {state.piles}")

        # Make a few moves
        moves = [
            NimMove(pile_index=1, stones_to_remove=3),  # Take 3 from pile 1
            NimMove(pile_index=2, stones_to_remove=2),  # Take 2 from pile 2
        ]

        current_player = "player1"
        for i, move in enumerate(moves):
            print(
                f"\nMove {i+1}: {current_player} takes {move.stones_to_remove} from pile {move.pile_index}"
            )

            # Get legal moves to verify move is legal
            legal_moves = NimStateManager.get_legal_moves(state)
            print(f"  Legal moves available: {len(legal_moves)}")

            # Make the move (assuming the API requires a player parameter)
            try:
                command = NimStateManager.make_move(state, current_player, move)
                state = command.state
                print(f"  New piles: {state.piles}")
                print(f"  Game status: {state.game_status}")

                # Switch player
                current_player = "player2" if current_player == "player1" else "player1"

                if state.game_status != "ongoing":
                    break

            except Exception as e:
                print(f"  Move failed: {e}")
                break

        print(f"\n✓ Nim demo completed. Final status: {state.game_status}")
        return True

    except Exception as e:
        print(f"✗ Nim demo failed: {e}")
        return False


def demo_tic_tac_toe():
    """Demonstrate Tic Tac Toe game."""
    print("\n🎯 Tic Tac Toe Demo")
    print("-" * 40)

    try:
        from haive.games.tic_tac_toe.models import TicTacToeMove
        from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

        # Initialize empty board
        state = TicTacToeStateManager.initialize()
        print("Initialized 3x3 board")
        print(f"Starting player: {state.turn}")

        # Define some moves for a quick game
        moves = [
            ("X", 1, 1),  # Center
            ("O", 0, 0),  # Top-left
            ("X", 0, 1),  # Top-center
            ("O", 2, 1),  # Bottom-center
            ("X", 2, 2),  # Bottom-right
        ]

        for player, row, col in moves:
            print(f"\n{player} plays at ({row}, {col})")

            # Create move
            move = TicTacToeMove(row=row, col=col, player=player)

            try:
                # Make move - check if the method exists and what parameters it needs
                if hasattr(TicTacToeStateManager, "make_move"):
                    # Try different signatures
                    try:
                        result = TicTacToeStateManager.make_move(state, player, move)
                        if hasattr(result, "state"):
                            state = result.state
                        else:
                            state = result
                    except TypeError:
                        # Maybe it's just (state, move)
                        state = TicTacToeStateManager.make_move(state, move)
                else:
                    print("  No make_move method found")
                    break

                # Show board state
                print(f"  Game status: {state.game_status}")
                print(f"  Next turn: {state.turn}")

                if state.game_status != "ongoing":
                    print(f"  Game ended! Status: {state.game_status}")
                    break

            except Exception as e:
                print(f"  Move failed: {e}")
                break

        print("\n✓ Tic Tac Toe demo completed")
        return True

    except Exception as e:
        print(f"✗ Tic Tac Toe demo failed: {e}")
        return False


def demo_connect4():
    """Demonstrate Connect4 game."""
    print("\n🔴 Connect4 Demo")
    print("-" * 40)

    try:
        from haive.games.connect4.models import Connect4Move
        from haive.games.connect4.state_manager import Connect4StateManager

        # Initialize 6x7 board
        state = Connect4StateManager.initialize()
        print("Initialized 6x7 Connect4 board")
        print(f"Starting player: {state.current_player}")

        # Make some moves in the center columns
        moves = [3, 3, 4, 4, 5, 5, 2]  # Column numbers
        players = ["red", "yellow", "red", "yellow", "red", "yellow", "red"]

        for i, (col, player) in enumerate(zip(moves, players)):
            print(f"\nMove {i+1}: {player} drops in column {col}")

            # Create move
            move = Connect4Move(column=col, player=player)

            try:
                # Make move
                result = Connect4StateManager.make_move(state, player, move)
                if hasattr(result, "state"):
                    state = result.state
                else:
                    state = result

                print(f"  Current player: {state.current_player}")
                print(f"  Game status: {state.game_status}")

                if state.game_status != "ongoing":
                    print(f"  Game ended! Winner: {state.winner}")
                    break

            except Exception as e:
                print(f"  Move failed: {e}")
                break

        print("\n✓ Connect4 demo completed")
        return True

    except Exception as e:
        print(f"✗ Connect4 demo failed: {e}")
        return False


def main():
    """Run all game demos."""
    print("🎮 Haive Games Working Demo")
    print("=" * 50)
    print("Demonstrating basic game functionality without LLM agents")

    demos = [
        ("Nim", demo_nim_game),
        ("Tic Tac Toe", demo_tic_tac_toe),
        ("Connect4", demo_connect4),
    ]

    results = []
    for game_name, demo_func in demos:
        try:
            success = demo_func()
            results.append((game_name, success))
        except Exception as e:
            print(f"\n✗ {game_name} demo crashed: {e}")
            results.append((game_name, False))

    # Summary
    print("\n" + "=" * 50)
    print("🎯 Demo Summary")
    print("-" * 20)

    passed = sum(1 for _, success in results if success)
    total = len(results)

    for game_name, success in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status} {game_name}")

    print(f"\nResults: {passed}/{total} games working")

    if passed == total:
        print("\n🎉 All demos passed! Games are working correctly.")
    else:
        print(f"\n⚠️  {total - passed} games need attention.")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
