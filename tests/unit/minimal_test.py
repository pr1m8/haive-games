#!/usr/bin/env python3
"""Minimal standalone test for Mancala game logic.

This script implements a minimal version of the Mancala game
that doesn't depend on any external frameworks.
"""

from enum import Enum


class Player(str, Enum):
    """Player enumeration."""

    PLAYER1 = "player1"
    PLAYER2 = "player2"


class GameStatus(str, Enum):
    """Game status enumeration."""

    ONGOING = "ongoing"
    PLAYER1_WIN = "player1_win"
    PLAYER2_WIN = "player2_win"
    DRAW = "draw"


class MancalaGame:
    """A minimal implementation of the Mancala game."""

    def __init__(self, stones_per_pit: int = 4):
        """Initialize the game.

        Args:
            stones_per_pit: Number of stones to place in each pit initially.
        """
        # Board layout:
        # - Indices 0-5: Player 1's pits (bottom row)
        # - Index 6: Player 1's store (right)
        # - Indices 7-12: Player 2's pits (top row)
        # - Index 13: Player 2's store (left)
        self.board = [stones_per_pit] * 14
        self.board[6] = 0  # Player 1's store
        self.board[13] = 0  # Player 2's store
        self.turn = Player.PLAYER1
        self.game_status = GameStatus.ONGOING
        self.free_turn = False
        self.winner = None
        self.move_history = []

    def print_board(self) -> None:
        """Print the current board state."""
        print("\n" + "=" * 40)
        print(f"Current Player: {self.turn}")
        print(f"Game Status: {self.game_status}")
        if self.free_turn:
            print("Free Turn: Yes")
        print("=" * 40)

        # Create board string
        result = "    "
        # Player 2's pits (reversed)
        for i in range(12, 6, -1):
            result += f"{self.board[i]:2d} "
        result += "\n"

        # Stores
        result += f"{self.board[13]:2d}" + " " * 20 + f"{self.board[6]:2d}\n"

        # Player 1's pits
        result += "    "
        for i in range(6):
            result += f"{self.board[i]:2d} "
        result += "\n\n"

        result += (
            f"Player 1 (bottom): {self.board[6]}  |  Player 2 (top): {self.board[13]}"
        )

        print(result)
        print()

    def get_valid_moves(self) -> list[int]:
        """Get valid pit indices for the current player.

        Returns:
            List of valid pit indices (0-5).
        """
        if self.turn == Player.PLAYER1:
            # Player 1 can move from pits 0-5 if they contain stones
            return [i for i in range(6) if self.board[i] > 0]
        # Player 2 can move from pits 7-12 if they contain stones
        # But we return 0-5 for consistency
        return [i - 7 for i in range(7, 13) if self.board[i] > 0]

    def make_move(self, pit_index: int) -> bool:
        """Make a move from the specified pit.

        Args:
            pit_index: The pit index (0-5) to move from.

        Returns:
            True if the move was successful, False otherwise.
        """
        # Convert to actual board index
        board_index = pit_index if self.turn == Player.PLAYER1 else pit_index + 7

        # Validate the move
        if board_index < 0 or board_index > 13:
            print(f"Invalid pit index: {pit_index}")
            return False

        if board_index == 6 or board_index == 13:
            print("Cannot move from a store")
            return False

        if self.board[board_index] == 0:
            print(f"Pit {pit_index} is empty")
            return False

        # Reset free turn flag
        self.free_turn = False

        # Record the move
        self.move_history.append((self.turn, pit_index))

        # Get stones from the starting pit
        stones = self.board[board_index]
        self.board[board_index] = 0

        # Sow the stones
        current_pit = board_index
        player_store = 6 if self.turn == Player.PLAYER1 else 13
        opponent_store = 13 if self.turn == Player.PLAYER1 else 6

        while stones > 0:
            current_pit = (current_pit + 1) % 14

            # Skip opponent's store
            if current_pit == opponent_store:
                continue

            # Add a stone to the current pit
            self.board[current_pit] += 1
            stones -= 1

        # Check for capture
        last_pit = current_pit
        if last_pit != player_store and self.board[last_pit] == 1:
            # The last stone landed in an empty pit on the player's side
            if (self.turn == Player.PLAYER1 and 0 <= last_pit < 6) or (
                self.turn == Player.PLAYER2 and 7 <= last_pit < 13
            ):
                opposite_pit = 12 - last_pit

                # If the opposite pit has stones, capture them
                if self.board[opposite_pit] > 0:
                    # Add the stones from both pits to the player's store
                    self.board[player_store] += (
                        self.board[last_pit] + self.board[opposite_pit]
                    )
                    self.board[last_pit] = 0
                    self.board[opposite_pit] = 0

        # Check for free turn
        if last_pit == player_store:
            self.free_turn = True

        # Switch turns if no free turn
        if not self.free_turn:
            self.turn = (
                Player.PLAYER2 if self.turn == Player.PLAYER1 else Player.PLAYER1
            )

        # Check if game is over
        self.check_game_over()

        return True

    def check_game_over(self) -> None:
        """Check if the game is over and update the game status."""
        # Check if any player's side is empty
        player1_empty = all(self.board[i] == 0 for i in range(6))
        player2_empty = all(self.board[i] == 0 for i in range(7, 13))

        if player1_empty or player2_empty:
            # Game is over, collect remaining stones
            if player1_empty:
                # Add player2's stones to their store
                for i in range(7, 13):
                    self.board[13] += self.board[i]
                    self.board[i] = 0
            else:
                # Add player1's stones to their store
                for i in range(6):
                    self.board[6] += self.board[i]
                    self.board[i] = 0

            # Determine the winner
            if self.board[6] > self.board[13]:
                self.game_status = GameStatus.PLAYER1_WIN
                self.winner = Player.PLAYER1
            elif self.board[13] > self.board[6]:
                self.game_status = GameStatus.PLAYER2_WIN
                self.winner = Player.PLAYER2
            else:
                self.game_status = GameStatus.DRAW
                self.winner = None

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            True if the game is over, False otherwise.
        """
        return self.game_status != GameStatus.ONGOING


def play_test_game() -> None:
    """Run a test game with predetermined moves."""
    # Initialize the game
    game = MancalaGame(stones_per_pit=4)
    print("\n--- Initial State ---")
    game.print_board()

    # Test sequence of moves
    moves = [
        # Player 1's moves
        3,
        0,
        4,
        1,
        5,
        2,
        # Player 2's moves
        1,
        3,
        5,
        2,
        0,
        4,
    ]

    # Play the moves
    for i, pit in enumerate(moves):
        print(f"\n--- Move {i + 1} ---")
        valid_moves = game.get_valid_moves()

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
        print(f"Move: {game.turn} chose pit {pit}")
        game.make_move(pit)
        game.print_board()

        # Check if game is over
        if game.is_game_over():
            print("\n--- Game Over ---")
            print(f"Winner: {game.winner}")
            print(
                f"Final Scores - Player 1: {game.board[6]}, Player 2: {game.board[13]}"
            )
            break

    # Print final state if game not over
    if not game.is_game_over():
        print("\n--- Game not finished ---")
        print(f"Current Scores - Player 1: {game.board[6]}, Player 2: {game.board[13]}")


def run_interactive_game() -> None:
    """Run an interactive game where the user inputs moves."""
    # Initialize the game
    game = MancalaGame(stones_per_pit=4)
    print("\n--- Initial State ---")
    game.print_board()

    while not game.is_game_over():
        # Get valid moves
        valid_moves = game.get_valid_moves()
        if not valid_moves:
            print("No valid moves available. Game over.")
            break

        # Prompt for move
        print(f"Valid moves for {game.turn}: {valid_moves}")
        try:
            pit = int(input(f"{game.turn}, choose a pit (0-5): "))
            if pit not in valid_moves:
                print(f"Invalid pit {pit}. Try again.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        # Make the move
        game.make_move(pit)
        game.print_board()

    # Print final result
    print("\n--- Game Over ---")
    print(f"Winner: {game.winner}")
    print(f"Final Scores - Player 1: {game.board[6]}, Player 2: {game.board[13]}")


if __name__ == "__main__":
    print("MANCALA GAME TEST")
    print("=================")

    # Default to test mode
    import sys

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
