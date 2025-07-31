#!/usr/bin/env python3
"""Standalone game implementation of Nim.

This script allows playing Nim without requiring the full Haive framework.

"""

import argparse
import logging
import random
import sys
import time

from pydantic import BaseModel, Field
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)

# Try to import Rich for UI
try:
    RICH_AVAILABLE = True
    logger.info("Rich UI available for visualization")
except ImportError:
    RICH_AVAILABLE = False
    logger.info("Rich UI not available, using text-based UI")


# Define game models
class NimMove(BaseModel):
    """Move in the Nim game."""

    pile_index: int
    stones_taken: int

    def __str__(self) -> str:
        return f"Take {self.stones_taken} stones from pile {self.pile_index}"


class NimState(BaseModel):
    """State for the Nim game."""

    piles: list[int] = Field(default=[3, 5, 7])
    turn: str = Field(default="player1")
    game_status: str = Field(default="in_progress")
    move_history: list[NimMove] = Field(default_factory=list)
    misere_mode: bool = Field(default=False)

    @property
    def board_string(self) -> str:
        """Return a string representation of the board."""
        result = []
        for i, pile_size in enumerate(self.piles):
            pile_str = "Pile " + str(i) + ": " + "O " * pile_size
            result.append(pile_str)
        return "\n".join(result)

    @property
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_status != "in_progress"

    @property
    def stones_left(self) -> int:
        """Return the total number of stones left."""
        return sum(self.piles)

    @property
    def nim_sum(self) -> int:
        """Calculate the nim-sum (XOR sum) of the pile sizes."""
        result = 0
        for pile_size in self.piles:
            result ^= pile_size
        return result


# Nim UI class
class NimUI:
    """UI for the Nim game."""

    # Stone representation
    STONE_SYMBOL = "🔵"  # Blue circle
    EMPTY_SYMBOL = "⚫"  # Black circle (for visualization spacing)

    def __init__(self, delay: float = 0.5):
        """Initialize the UI."""
        self.delay = delay
        if RICH_AVAILABLE:
            self.console = Console()
        else:
            self.console = None

    def display_game_state(self, state: NimState):
        """Display the current game state."""
        if RICH_AVAILABLE and self.console:
            self._display_rich_ui(state)
        else:
            self._display_text_ui(state)

        time.sleep(self.delay)

    def _display_rich_ui(self, state: NimState):
        """Display game state using Rich UI."""
        self.console.clear()

        # Create header
        status_text = (
            "[bold blue]Game in Progress[/]"
            if state.game_status == "in_progress"
            else "[bold green]Game Over![/]"
        )
        game_mode = (
            "[bold red]Misère Mode[/]"
            if state.misere_mode
            else "[bold blue]Standard Mode[/]"
        )

        header = Panel(
            Text.from_markup(
                f"{status_text} - {state.turn}'s Turn\n"
                f"Game Mode: {game_mode} - "
                f"{'Last player to take a stone loses' if state.misere_mode else 'Last player to take a stone wins'}"
            ),
            title="[bold cyan]Nim Game[/]",
            border_style="cyan",
        )

        # Create piles visualization
        pile_lines = []
        for i, pile_size in enumerate(state.piles):
            stones = self.STONE_SYMBOL * pile_size
            pile_line = f"[bold white]Pile {i}[/] ({pile_size}): {stones}"
            pile_lines.append(pile_line)

        piles_panel = Panel(
            Text.from_markup("\n".join(pile_lines)),
            title="[bold blue]Piles[/]",
            border_style="blue",
        )

        # Create moves table
        moves_table = Table(title="Move History", box=box.SIMPLE)
        moves_table.add_column("Turn", style="cyan")
        moves_table.add_column("Player", style="green")
        moves_table.add_column("Move", style="white")

        for i, move in enumerate(state.move_history):
            player = "Player 1" if i % 2 == 0 else "Player 2"
            move_text = f"Took {move.stones_taken} stone(s) from pile {move.pile_index}"
            moves_table.add_row(str(i + 1), player, move_text)

        # Print components
        self.console.print(header)
        self.console.print(piles_panel)

        if state.move_history:
            self.console.print(moves_table)

    def _display_text_ui(self, state: NimState):
        """Display game state using text UI."""
        print("\n" + "=" * 50)
        print(f"NIM GAME - {state.turn}'s Turn")
        print(f"Game Status: {state.game_status}")
        print(
            f"Game Mode: {
                'Misère (last takes loses)'
                if state.misere_mode
                else 'Standard (last takes wins)'
            }"
        )
        print("=" * 50)

        # Print piles
        print("\nPiles:")
        for i, pile_size in enumerate(state.piles):
            print(f"Pile {i} ({pile_size}): " + "O " * pile_size)

        # Print move history
        if state.move_history:
            print("\nRecent Moves:")
            for i, move in enumerate(state.move_history[-5:]):
                player = (
                    "Player 1"
                    if (len(state.move_history) - 5 + i) % 2 == 0
                    else "Player 2"
                )
                print(
                    f"- {player}: Took {move.stones_taken} stone(s) from pile {move.pile_index}"
                )

    def prompt_for_move(self, state: NimState) -> NimMove:
        """Prompt the user for a move."""
        while True:
            try:
                # Display pile information
                print("\nCurrent piles:", state.piles)

                # Get pile index
                pile_idx_input = input(f"Enter pile index (0-{len(state.piles) - 1}): ")
                pile_idx = int(pile_idx_input)

                # Validate pile index
                if pile_idx < 0 or pile_idx >= len(state.piles):
                    print(
                        f"Invalid pile index! Please choose between 0 and {len(state.piles) - 1}."
                    )
                    continue

                # Check if pile is empty
                if state.piles[pile_idx] == 0:
                    print("This pile is empty! Please choose a non-empty pile.")
                    continue

                # Get stones to take
                stones_input = input(
                    f"Enter stones to take (1-{state.piles[pile_idx]}): "
                )
                stones = int(stones_input)

                # Validate stones
                if stones < 1 or stones > state.piles[pile_idx]:
                    print(
                        f"Invalid number of stones! Please choose between 1 and {
                            state.piles[pile_idx]
                        }."
                    )
                    continue

                # Return valid move
                return NimMove(pile_index=pile_idx, stones_taken=stones)

            except ValueError:
                print("Please enter valid numbers!")

    def get_computer_move(self, state: NimState) -> NimMove:
        """Generate a computer move."""
        # Get legal moves
        legal_moves = []
        for pile_idx, pile_size in enumerate(state.piles):
            if pile_size > 0:
                for stones in range(1, pile_size + 1):
                    legal_moves.append(
                        NimMove(pile_index=pile_idx, stones_taken=stones)
                    )

        # Calculate nim-sum for optimal play
        nim_sum = state.nim_sum

        # If the nim-sum is 0, we're in a losing position, so make a random
        # move
        if nim_sum == 0:
            move = random.choice(legal_moves)
            return move

        # Otherwise, make a winning move if possible
        for move in legal_moves:
            # Calculate new state after this move
            new_piles = state.piles.copy()
            new_piles[move.pile_index] -= move.stones_taken

            # Calculate new nim-sum
            new_nim_sum = 0
            for pile in new_piles:
                new_nim_sum ^= pile

            # If this move makes nim-sum 0, it's an optimal move
            if new_nim_sum == 0:
                return move

        # If we can't make the nim-sum 0, just make a random move
        return random.choice(legal_moves)

    def announce_winner(self, state: NimState):
        """Announce the winner of the game."""
        if state.game_status == "player1_win":
            winner = "Player 1"
        elif state.game_status == "player2_win":
            winner = "Player 2"
        else:
            winner = "Unknown"

        if RICH_AVAILABLE and self.console:
            self.console.print(
                Panel(
                    Text.from_markup(f"[bold green]Game Over! {winner} wins![/]"),
                    title="[bold cyan]Result[/]",
                    border_style="green",
                )
            )
        else:
            print("\n" + "=" * 50)
            print(f"Game Over! {winner} wins!")
            print("=" * 50)


# Game state manager
class NimGameManager:
    """Manager for the Nim game."""

    @staticmethod
    def initialize(pile_sizes: list[int] = None, misere_mode: bool = False) -> NimState:
        """Initialize a new game state."""
        return NimState(piles=pile_sizes, misere_mode=misere_mode)

    @staticmethod
    def apply_move(state: NimState, move: NimMove) -> NimState:
        """Apply a move to the current state."""
        # Validate move
        if move.pile_index < 0 or move.pile_index >= len(state.piles):
            raise ValueError(f"Invalid pile index: {move.pile_index}")

        if move.stones_taken < 1 or move.stones_taken > state.piles[move.pile_index]:
            raise ValueError(f"Invalid number of stones: {move.stones_taken}")

        # Create new state
        new_state = state.model_copy()

        # Apply move
        new_state.piles[move.pile_index] -= move.stones_taken
        new_state.move_history.append(move)

        # Switch turns
        new_state.turn = "player2" if state.turn == "player1" else "player1"

        # Check game status
        return NimGameManager.check_game_status(new_state)

    @staticmethod
    def check_game_status(state: NimState) -> NimState:
        """Check and update the game status."""
        # Create a copy to avoid modifying the original
        new_state = state

        # Check for game over
        if sum(new_state.piles) == 0:
            # In standard Nim, the player who takes the last stone wins
            # In misere Nim, the player who takes the last stone loses
            last_player = "player1" if new_state.turn == "player2" else "player2"

            if new_state.misere_mode:
                # Last player loses in misere mode
                winner = "player1" if last_player == "player2" else "player2"
            else:
                # Last player wins in standard mode
                winner = last_player

            new_state.game_status = f"{winner}_win"

        return new_state


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Play Nim")

    parser.add_argument(
        "--pile-sizes",
        type=int,
        nargs="+",
        default=[3, 5, 7],
        help="Initial pile sizes (default: 3 5 7)",
    )

    parser.add_argument(
        "--misere",
        action="store_true",
        default=False,
        help="Use misère mode - last player to take a stone loses (default: false)",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between moves in seconds (default: 0.5)",
    )

    parser.add_argument(
        "--player1",
        choices=["human", "computer"],
        default="human",
        help="Player 1 type (default: human)",
    )

    parser.add_argument(
        "--player2",
        choices=["human", "computer"],
        default="computer",
        help="Player 2 type (default: computer)",
    )

    return parser.parse_args()


def main():
    """Run the Nim game."""
    args = parse_args()

    # Print welcome message
    print("\n" + "=" * 60)
    print("WELCOME TO NIM")
    print("=" * 60)

    # Show game configuration
    print("\nGame Configuration:")
    print(f"- Pile Sizes: {args.pile_sizes}")
    print(
        f"- Game Mode: {'Misère (last takes loses)' if args.misere else 'Standard (last takes wins)'}"
    )
    print(f"- Player 1: {args.player1.capitalize()}")
    print(f"- Player 2: {args.player2.capitalize()}")
    print(f"- Move Delay: {args.delay} seconds\n")

    # Initialize game manager and UI
    game_manager = NimGameManager()
    ui = NimUI(delay=args.delay)

    # Initialize game state
    state = game_manager.initialize(pile_sizes=args.pile_sizes, misere_mode=args.misere)

    # Main game loop
    try:
        print("Starting game...\n")
        time.sleep(1)  # Brief pause before starting

        while not state.is_game_over:
            # Display current state
            ui.display_game_state(state)

            # Determine current player type
            current_player_type = (
                args.player1 if state.turn == "player1" else args.player2
            )

            # Get move based on player type
            if current_player_type == "human":
                print(f"\n{state.turn}'s turn (Human)")
                move = ui.prompt_for_move(state)
            else:
                print(f"\n{state.turn}'s turn (Computer)")
                move = ui.get_computer_move(state)
                print(
                    f"Computer chooses: Take {move.stones_taken} stone(s) from pile {
                        move.pile_index
                    }"
                )
                time.sleep(1)  # Brief pause for computer move

            # Apply move
            state = game_manager.apply_move(state, move)

        # Game over, display final state
        ui.display_game_state(state)
        ui.announce_winner(state)

        return 0

    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        return 0
    except Exception as e:
        logger.error(f"Error running game: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
