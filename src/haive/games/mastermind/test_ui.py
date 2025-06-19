#!/usr/bin/env python3
"""Simple UI test for Mastermind game."""

import random
import sys
from typing import List

from models import ColorCode, Feedback

# Import directly from our files to avoid framework dependencies
from state import MastermindState

try:
    from ui import MastermindUI

    UI_AVAILABLE = True
except ImportError:
    UI_AVAILABLE = False
    print("Rich UI not available, using fallback text UI")

    class MastermindUI:
        """Basic fallback UI."""

        def __init__(self):
            pass

        def display_game_state(self, state):
            """Display state as text."""
            print(f"\nTurn: {state.turn}/{state.max_turns}")
            print(f"Secret: {'? ' * len(state.secret_code.colors)}")
            print("\nGuesses:")
            for i, (guess, feedback) in enumerate(zip(state.guesses, state.feedback)):
                print(f"  {i+1}. {guess} -> {feedback}")


def create_test_state():
    """Create a test game state with some guesses."""
    # Available colors
    available_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    # Create a secret code
    secret_code = ColorCode(colors=random.sample(available_colors, 4))

    # Initialize state
    state = MastermindState(secret_code=secret_code, turn=3, max_turns=10)

    # Add some test guesses and feedback
    guesses = [
        ["red", "blue", "green", "yellow"],
        ["purple", "orange", "red", "blue"],
    ]

    for guess_colors in guesses:
        guess = ColorCode(colors=guess_colors)
        state.guesses.append(guess)

        # Simple random feedback for testing
        correct_pos = random.randint(0, 2)
        correct_color = random.randint(0, 2)
        feedback = Feedback(correct_position=correct_pos, correct_color=correct_color)
        state.feedback.append(feedback)

    return state


def main():
    """Run a simple UI test."""
    print("Testing Mastermind UI...")

    # Create test state
    state = create_test_state()
    print(f"Created test state with secret code: {state.secret_code}")

    # Initialize UI
    ui = MastermindUI()

    # Display game state
    ui.display_game_state(state)

    print("\nUI test complete!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
