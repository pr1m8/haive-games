#!/usr/bin/env python3
"""Standalone test for the Mancala game logic.

This script tests the core logic of the Mancala game without requiring
language models or the Haive framework. It verifies that the state management
and game rules are working correctly.
"""

import sys
from typing import List, Optional

from haive.games.mancala.models import MancalaMove
from haive.games.mancala.state import MancalaState
from haive.games.mancala.state_manager import MancalaStateManager


def print_board(state: MancalaState) -> None:
    """Print the current board state."""
    print("\n" + "=" * 40)
    print(f"Current Player: {state.turn}")
    print(f"Game Status: {state.game_status}")
    if state.free_turn:
        print("Free Turn: Yes")
    print("=" * 40)
    print(state.board_string)
    print()


def get_valid_moves(state: MancalaState) -> List[int]:
    """Get valid pit indices for the current player."""
    return state.get_valid_moves()


def make_move(state: MancalaState, pit_index: int) -> MancalaState:
    """Make a move and return the new state."""
    player = state.turn

    # Convert board index to pit index (0-5) for player2
    # This is necessary because MancalaMove expects pit indices 0-5 for both players
    if player == "player2" and pit_index >= 7:
        pit_index = pit_index - 7

    move = MancalaMove(pit_index=pit_index, player=player)

    try:
        new_state = MancalaStateManager.apply_move(state, move)
        print(f"Move: {player} chose pit {pit_index}")
        return new_state
    except ValueError as e:
        print(f"Invalid move: {e}")
        return state


def play_test_game() -> None:
    """Run a test game with predetermined moves."""
    # Initialize the game state
    state = MancalaState.initialize(stones_per_pit=4)
    print("\n--- Initial State ---")
    print_board(state)

    # Test sequence of moves
    moves = [
        # Player 1's moves (even indices)
        0,
        2,
        4,
        5,
        3,
        1,
        # Player 2's moves (odd indices)
        0,
        2,
        4,
        5,
        3,
        1,
    ]

    # Play the moves
    for i, pit in enumerate(moves):
        print(f"\n--- Move {i+1} ---")
        valid_moves = get_valid_moves(state)

        # Adjust move if it's not valid
        if pit not in valid_moves:
            print(f"Pit {pit} is not valid. Valid moves: {valid_moves}")
            if valid_moves:
                pit = valid_moves[0]
                print(f"Choosing pit {pit} instead")
            else:
                print("No valid moves available. Game might be over.")
                break

        # Make the move
        state = make_move(state, pit)
        print_board(state)

        # Check if game is over
        if state.is_game_over():
            print("\n--- Game Over ---")
            winner = state.get_winner()
            print(f"Winner: {winner}")
            print(
                f"Final Scores - Player 1: {state.player1_score}, Player 2: {state.player2_score}"
            )
            break

    # Print final state if game not over
    if not state.is_game_over():
        print("\n--- Game not finished ---")
        print(
            f"Current Scores - Player 1: {state.player1_score}, Player 2: {state.player2_score}"
        )


def run_interactive_game() -> None:
    """Run an interactive game where the user inputs moves."""
    # Initialize the game state
    state = MancalaState.initialize(stones_per_pit=4)
    print("\n--- Initial State ---")
    print_board(state)

    while not state.is_game_over():
        # Get valid moves
        valid_moves = get_valid_moves(state)
        if not valid_moves:
            print("No valid moves available. Game over.")
            break

        # Prompt for move
        print(f"Valid moves for {state.turn}: {valid_moves}")
        try:
            pit = int(input(f"{state.turn}, choose a pit (0-5): "))
            if pit not in valid_moves:
                print(f"Invalid pit {pit}. Try again.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        # Make the move
        state = make_move(state, pit)
        print_board(state)

    # Print final result
    print("\n--- Game Over ---")
    winner = state.get_winner()
    print(f"Winner: {winner}")
    print(
        f"Final Scores - Player 1: {state.player1_score}, Player 2: {state.player2_score}"
    )


if __name__ == "__main__":
    print("MANCALA GAME TEST")
    print("=================")

    # Default to test mode
    mode = "test"

    # Check for command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        mode = "interactive"

    # Run the selected mode
    if mode == "interactive":
        print("Running in interactive mode (you will be prompted for moves)")
        run_interactive_game()
    else:
        print("Running test game with predetermined moves")
        play_test_game()
