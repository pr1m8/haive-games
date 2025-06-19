#!/usr/bin/env python3
"""Test script to verify the Mastermind game fixes.

This script tests the state conversion and error handling in the Mastermind game.
"""

import logging
import sys
from typing import Any, Dict, List, Literal, Optional, Union

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import required components
try:
    from haive.games.mastermind.agent import ensure_game_state
    from haive.games.mastermind.models import (
        MastermindAnalysis,
        MastermindFeedback,
        MastermindGuess,
    )
    from haive.games.mastermind.state import MastermindState

    IMPORTS_OK = True
except ImportError as e:
    logger.error(f"Import error: {e}")
    IMPORTS_OK = False


# Mock Command class for testing
class Command:
    def __init__(self, update=None, delete=None, values=None, state=None, stop=None):
        self.update = update or {}
        self.delete = delete or []
        self.values = values
        self.state = state
        self.stop = stop

    def __repr__(self):
        return f"Command(update={self.update}, delete={self.delete}, stop={self.stop})"


def test_ensure_game_state():
    """Test the ensure_game_state function with various input types."""
    if not IMPORTS_OK:
        logger.error("Imports failed, skipping test")
        return False

    logger.info("Testing ensure_game_state function...")

    # Test with dictionary input
    dict_input = {
        "secret_code": ["red", "blue", "green", "yellow"],
        "turn": "player1",
        "codemaker": "player2",
        "guesses": [],
        "feedback": [],
        "game_status": "ongoing",
        "max_turns": 10,
    }

    result = ensure_game_state(dict_input)
    logger.info(f"Result type from dict input: {type(result)}")
    assert isinstance(result, MastermindState), "Result should be a MastermindState"
    assert result.secret_code == [
        "red",
        "blue",
        "green",
        "yellow",
    ], "Secret code should match input"

    # Test with MastermindState input
    state_input = MastermindState.initialize(
        secret_code=["red", "blue", "green", "yellow"], codemaker="player2"
    )
    result = ensure_game_state(state_input)
    logger.info(f"Result type from MastermindState input: {type(result)}")
    assert result is state_input, "Result should be the same object"

    # Test with Command input
    command_input = Command(state=state_input)
    result = ensure_game_state(command_input)
    logger.info(f"Result type from Command input: {type(result)}")
    assert isinstance(result, MastermindState), "Result should be a MastermindState"
    assert result.secret_code == [
        "red",
        "blue",
        "green",
        "yellow",
    ], "Secret code should match input"

    # Test with invalid input
    invalid_input = "not a valid input"
    result = ensure_game_state(invalid_input)
    logger.info(f"Result type from invalid input: {type(result)}")
    assert isinstance(
        result, MastermindState
    ), "Result should be a MastermindState (fallback)"

    logger.info("All ensure_game_state tests passed!")
    return True


def test_state_operations():
    """Test basic state operations to ensure they work correctly."""
    if not IMPORTS_OK:
        logger.error("Imports failed, skipping test")
        return False

    logger.info("Testing state operations...")

    # Create a state
    state = MastermindState.initialize(
        secret_code=["red", "blue", "green", "yellow"], codemaker="player1"
    )

    # Test that state has expected values
    assert state.turn == "player2", "Codebreaker should be player2"
    assert state.game_status == "ongoing", "Game status should be ongoing"
    assert len(state.guesses) == 0, "No guesses should be present"

    # Create a guess
    guess = MastermindGuess(
        colors=["red", "purple", "blue", "orange"], player="player2"
    )

    # Create feedback
    feedback = MastermindFeedback(correct_position=1, correct_color=1)

    # Update state
    new_state = state.model_copy(deep=True)
    new_state.guesses.append(guess)
    new_state.feedback.append(feedback)

    assert len(new_state.guesses) == 1, "Should have 1 guess"
    assert len(new_state.feedback) == 1, "Should have 1 feedback"
    assert new_state.current_turn_number == 2, "Should be turn 2"

    logger.info("All state operations tests passed!")
    return True


def main():
    """Run all tests."""
    logger.info("Starting Mastermind game fix tests...")

    tests_passed = []
    tests_passed.append(test_ensure_game_state())
    tests_passed.append(test_state_operations())

    if all(tests_passed):
        logger.info(
            "\nAll tests passed! The Mastermind game fixes are working correctly."
        )
        return 0
    else:
        logger.error("\nSome tests failed. Check the logs for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
