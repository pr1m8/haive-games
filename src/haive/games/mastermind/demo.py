#!/usr/bin/env python3
"""
Standalone demo for the Mastermind game with Rich UI.
This script demonstrates the Mastermind game without requiring the full Haive framework.
"""

import argparse
import logging
import random
import sys
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


# Define game models
class ColorCode(BaseModel):
    """Color code for Mastermind game."""

    colors: List[str] = Field(default_factory=list)

    def __str__(self) -> str:
        return str(self.colors)


class Feedback(BaseModel):
    """Feedback for a guess in Mastermind."""

    correct_position: int = 0
    correct_color: int = 0

    def __str__(self) -> str:
        return f"Correct position: {self.correct_position}, Correct color: {self.correct_color}"


class MastermindState(BaseModel):
    """State for the Mastermind game."""

    secret_code: ColorCode
    turn: int = 1
    codemaker: str = "player1"
    guesses: List[ColorCode] = Field(default_factory=list)
    feedback: List[Feedback] = Field(default_factory=list)
    game_status: str = "in_progress"
    max_turns: int = 10

    @classmethod
    def initialize(
        cls, secret_code: Optional[List[str]] = None, max_turns: int = 10
    ) -> "MastermindState":
        """Initialize a new game state."""
        if secret_code is None:
            # Default colors
            colors = ["red", "blue", "green", "yellow", "purple", "orange"]
            secret_code = random.sample(colors, 4)

        return cls(secret_code=ColorCode(colors=secret_code), max_turns=max_turns)

    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_status != "in_progress"

    def make_guess(self, guess: List[str]) -> Feedback:
        """Make a guess and get feedback."""
        guess_obj = ColorCode(colors=guess)
        self.guesses.append(guess_obj)

        # Calculate feedback
        feedback = calculate_feedback(self.secret_code.colors, guess)
        feedback_obj = Feedback(
            correct_position=feedback["correct_position"],
            correct_color=feedback["correct_color"],
        )
        self.feedback.append(feedback_obj)

        # Update game status
        if feedback_obj.correct_position == len(self.secret_code.colors):
            self.game_status = "won"
        elif self.turn >= self.max_turns:
            self.game_status = "lost"
        else:
            self.turn += 1

        return feedback_obj


# Helper functions
def calculate_feedback(secret_code: List[str], guess: List[str]) -> Dict[str, int]:
    """Calculate feedback for a guess."""
    if len(secret_code) != len(guess):
        raise ValueError("Secret code and guess must be the same length")

    # Copy lists to avoid modifying originals
    secret = secret_code.copy()
    guess_copy = guess.copy()

    # Count correct positions
    correct_position = sum(1 for s, g in zip(secret, guess_copy) if s == g)

    # Remove correct positions for counting correct colors
    for i in range(len(secret) - 1, -1, -1):
        if secret[i] == guess_copy[i]:
            secret.pop(i)
            guess_copy.pop(i)

    # Count correct colors in wrong positions
    correct_color = 0
    for g in guess_copy[:]:
        if g in secret:
            correct_color += 1
            secret.remove(g)

    return {"correct_position": correct_position, "correct_color": correct_color}


# Rich UI Implementation
try:
    from rich.console import Console
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text

    class MastermindUI:
        """Rich terminal UI for the Mastermind game."""

        COLOR_EMOJIS = {
            "red": "🔴",
            "blue": "🔵",
            "green": "🟢",
            "yellow": "🟡",
            "purple": "🟣",
            "orange": "🟠",
            "white": "⚪",
            "black": "⚫",
        }

        FEEDBACK_SYMBOLS = {
            "correct_position": "⚫",  # Black peg
            "correct_color": "⚪",  # White peg
        }

        def __init__(self):
            """Initialize the UI."""
            self.console = Console()

        def color_to_emoji(self, color: str) -> str:
            """Convert color name to emoji."""
            return self.COLOR_EMOJIS.get(color.lower(), "❓")

        def create_header(self, state: MastermindState) -> Panel:
            """Create header panel with game info."""
            if state.is_game_over():
                if state.game_status == "won":
                    status_text = "[bold green]Game Won![/]"
                else:
                    status_text = "[bold red]Game Lost![/]"
            else:
                status_text = f"[bold blue]Turn {state.turn}/{state.max_turns}[/]"

            return Panel(
                Text.from_markup(f"{status_text}\nCodemaker: {state.codemaker}"),
                title="Mastermind",
                border_style="bright_blue",
            )

        def create_secret_panel(
            self, state: MastermindState, show_secret: bool = False
        ) -> Panel:
            """Create panel showing the secret code (or hidden)."""
            if show_secret or state.is_game_over():
                code = " ".join(
                    self.color_to_emoji(color) for color in state.secret_code.colors
                )
                return Panel(code, title="Secret Code", border_style="red")
            else:
                hidden = " ".join("❓" for _ in range(len(state.secret_code.colors)))
                return Panel(hidden, title="Secret Code (Hidden)", border_style="red")

        def create_guesses_table(self, state: MastermindState) -> Table:
            """Create table of guesses and feedback."""
            table = Table(title="Guesses", border_style="blue")
            table.add_column("Turn", justify="center", style="cyan")
            table.add_column("Guess", justify="center")
            table.add_column("Feedback", justify="center")

            for i, (guess, feedback) in enumerate(zip(state.guesses, state.feedback)):
                # Format guess as emojis
                guess_str = " ".join(
                    self.color_to_emoji(color) for color in guess.colors
                )

                # Format feedback as symbols
                feedback_str = (
                    self.FEEDBACK_SYMBOLS["correct_position"]
                    * feedback.correct_position
                    + self.FEEDBACK_SYMBOLS["correct_color"] * feedback.correct_color
                )

                table.add_row(str(i + 1), guess_str, feedback_str)

            return table

        def create_layout(
            self, state: MastermindState, show_secret: bool = False
        ) -> Layout:
            """Create complete layout for the game."""
            layout = Layout()

            layout.split(
                Layout(name="header"),
                Layout(name="body"),
            )

            layout["header"].update(self.create_header(state))

            layout["body"].split_row(
                Layout(name="secret"),
                Layout(name="guesses"),
            )

            layout["secret"].update(self.create_secret_panel(state, show_secret))
            layout["guesses"].update(self.create_guesses_table(state))

            return layout

        def display_game_state(self, state: MastermindState, show_secret: bool = False):
            """Display the current game state."""
            self.console.clear()
            self.console.print(self.create_layout(state, show_secret))

        def input_guess(self, available_colors: List[str]) -> List[str]:
            """Get guess input from user."""
            self.console.print("\nAvailable colors:")
            color_display = " ".join(
                f"{self.color_to_emoji(color)} {color}" for color in available_colors
            )
            self.console.print(color_display)

            while True:
                self.console.print("\nEnter your guess (4 colors separated by spaces):")
                guess_input = self.console.input("> ")
                guess = [color.strip().lower() for color in guess_input.split()]

                if len(guess) != 4:
                    self.console.print("[bold red]Please enter exactly 4 colors.[/]")
                    continue

                if not all(color in available_colors for color in guess):
                    self.console.print(
                        "[bold red]Invalid color(s). Use the available colors.[/]"
                    )
                    continue

                return guess

        def show_result(self, state: MastermindState):
            """Show the game result."""
            self.display_game_state(state, show_secret=True)

            if state.game_status == "won":
                self.console.print(
                    "\n[bold green]Congratulations! You've cracked the code![/]"
                )
            else:
                self.console.print(
                    "\n[bold red]Game over! You didn't crack the code in time.[/]"
                )

            self.console.print(f"\nThe secret code was: {state.secret_code}")

except ImportError:
    # Fallback console UI if Rich is not available
    class MastermindUI:
        """Basic console UI for Mastermind game."""

        def __init__(self):
            pass

        def display_game_state(self, state: MastermindState, show_secret: bool = False):
            """Display the game state in plain text."""
            print("\n" + "=" * 50)
            print(f"MASTERMIND - Turn {state.turn}/{state.max_turns}")
            print("=" * 50)

            if show_secret or state.is_game_over():
                print(f"Secret code: {state.secret_code}")
            else:
                print(f"Secret code: {'? ' * len(state.secret_code.colors)}")

            print("\nGuesses:")
            for i, (guess, feedback) in enumerate(zip(state.guesses, state.feedback)):
                print(f"  {i+1}. {guess} -> {feedback}")

            if state.is_game_over():
                if state.game_status == "won":
                    print("\nCongratulations! You've cracked the code!")
                else:
                    print("\nGame over! You didn't crack the code in time.")

        def input_guess(self, available_colors: List[str]) -> List[str]:
            """Get guess input from user."""
            print("\nAvailable colors:", ", ".join(available_colors))

            while True:
                guess_input = input(
                    "\nEnter your guess (4 colors separated by spaces): "
                )
                guess = [color.strip().lower() for color in guess_input.split()]

                if len(guess) != 4:
                    print("Please enter exactly 4 colors.")
                    continue

                if not all(color in available_colors for color in guess):
                    print("Invalid color(s). Use the available colors.")
                    continue

                return guess

        def show_result(self, state: MastermindState):
            """Show the game result."""
            self.display_game_state(state, show_secret=True)


def main():
    """Run the Mastermind game."""
    parser = argparse.ArgumentParser(description="Play Mastermind")
    parser.add_argument(
        "--max-turns", type=int, default=10, help="Maximum number of turns"
    )
    parser.add_argument(
        "--show-secret",
        action="store_true",
        help="Show the secret code (for debugging)",
    )
    args = parser.parse_args()

    # Available colors
    available_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    # Create a new game
    secret_code = random.sample(available_colors, 4)
    state = MastermindState.initialize(
        secret_code=secret_code, max_turns=args.max_turns
    )

    # Create UI
    ui = MastermindUI()

    # Game loop
    while not state.is_game_over():
        ui.display_game_state(state, show_secret=args.show_secret)
        guess = ui.input_guess(available_colors)
        state.make_guess(guess)

    # Show final result
    ui.show_result(state)

    return 0


if __name__ == "__main__":
    sys.exit(main())
