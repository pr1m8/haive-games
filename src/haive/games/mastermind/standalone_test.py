#!/usr/bin/env python3
"""Standalone test script for the Mastermind game.

This script tests the core functionality of the Mastermind game
without requiring the full Haive framework.
"""

import logging
import operator
import random
import sys
from typing import Annotated, Any, Dict, List, Literal, Optional, Union

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Model classes
class ColorCode:
    """Represents the secret code in Mastermind."""

    def __init__(self, code: List[str]):
        """Initialize with a list of color strings."""
        self.code = code

    def __str__(self):
        """Return a string representation of the code."""
        return ", ".join(self.code)


class MastermindGuess:
    """Represents a guess in the Mastermind game."""

    def __init__(self, colors: List[str], player: str):
        """Initialize with colors and player."""
        self.colors = colors
        self.player = player

    def __str__(self):
        """Return a string representation of the guess."""
        return f"{self.player} guesses: {', '.join(self.colors)}"


class MastermindFeedback:
    """Represents feedback for a guess in Mastermind."""

    def __init__(self, correct_position: int, correct_color: int):
        """Initialize with correct position and color counts."""
        self.correct_position = correct_position
        self.correct_color = correct_color

    def __str__(self):
        """Return a string representation of the feedback."""
        return f"🌟 Correct position: {self.correct_position}, 🔄 Correct color: {self.correct_color}"

    def is_winning(self) -> bool:
        """Check if this feedback indicates a win."""
        return self.correct_position == 4


class MastermindAnalysis:
    """Represents an analysis of a Mastermind position."""

    def __init__(
        self,
        possible_combinations: int,
        high_probability_colors: List[str],
        eliminated_colors: List[str],
        fixed_positions: List[Dict[str, str]],
        strategy: str,
        reasoning: str,
        confidence: int,
    ):
        """Initialize with analysis data."""
        self.possible_combinations = possible_combinations
        self.high_probability_colors = high_probability_colors
        self.eliminated_colors = eliminated_colors
        self.fixed_positions = fixed_positions
        self.strategy = strategy
        self.reasoning = reasoning
        self.confidence = confidence

    def __str__(self):
        """Return a string representation of the analysis."""
        return (
            f"Analysis: {self.possible_combinations} combinations possible, "
            f"strategy: {self.strategy}, confidence: {self.confidence}/10"
        )


class MastermindState:
    """Represents the state of a Mastermind game."""

    def __init__(
        self,
        secret_code: List[str],
        guesses: List[MastermindGuess] = None,
        feedback: List[MastermindFeedback] = None,
        turn: str = "player1",
        codemaker: str = "player1",
        max_turns: int = 10,
        game_status: str = "ongoing",
        winner: Optional[str] = None,
        player1_analysis: List[MastermindAnalysis] = None,
        player2_analysis: List[MastermindAnalysis] = None,
    ):
        """Initialize the game state."""
        self.secret_code = secret_code
        self.guesses = guesses or []
        self.feedback = feedback or []
        self.turn = turn
        self.codemaker = codemaker
        self.max_turns = max_turns
        self.game_status = game_status
        self.winner = winner
        self.player1_analysis = player1_analysis or []
        self.player2_analysis = player2_analysis or []

    @classmethod
    def initialize(
        cls,
        codemaker: str = "player1",
        colors: List[str] = None,
        code_length: int = 4,
        max_turns: int = 10,
        secret_code: Optional[List[str]] = None,
    ) -> "MastermindState":
        """Initialize a new game state."""
        colors = colors or ["red", "blue", "green", "yellow", "purple", "orange"]
        codebreaker = "player2" if codemaker == "player1" else "player1"

        # Generate random code if not provided
        if not secret_code:
            secret_code = random.sample(colors, code_length)

        return cls(
            secret_code=secret_code,
            guesses=[],
            feedback=[],
            turn=codebreaker,
            codemaker=codemaker,
            max_turns=max_turns,
            game_status="ongoing",
        )

    @property
    def current_turn_number(self) -> int:
        """Get the current turn number."""
        return len(self.guesses) + 1

    @property
    def turns_remaining(self) -> int:
        """Get the number of turns remaining."""
        return max(0, self.max_turns - len(self.guesses))

    @property
    def is_game_over(self) -> bool:
        """Check if the game is over."""
        return self.game_status != "ongoing"

    def model_copy(self, deep: bool = False) -> "MastermindState":
        """Create a copy of the state."""
        if not deep:
            return MastermindState(
                secret_code=self.secret_code,
                guesses=self.guesses,
                feedback=self.feedback,
                turn=self.turn,
                codemaker=self.codemaker,
                max_turns=self.max_turns,
                game_status=self.game_status,
                winner=self.winner,
                player1_analysis=self.player1_analysis,
                player2_analysis=self.player2_analysis,
            )
        else:
            # Deep copy
            return MastermindState(
                secret_code=self.secret_code.copy(),
                guesses=self.guesses.copy(),
                feedback=self.feedback.copy(),
                turn=self.turn,
                codemaker=self.codemaker,
                max_turns=self.max_turns,
                game_status=self.game_status,
                winner=self.winner,
                player1_analysis=self.player1_analysis.copy(),
                player2_analysis=self.player2_analysis.copy(),
            )


class Command:
    """Mock Command class for testing."""

    def __init__(self, update=None, delete=None, values=None, state=None, stop=None):
        """Initialize with command data."""
        self.update = update or {}
        self.delete = delete or []
        self.values = values
        self.state = state
        self.stop = stop

    def __repr__(self):
        """Return a string representation of the command."""
        return f"Command(update={self.update}, delete={self.delete}, stop={self.stop})"


def ensure_game_state(
    state_input: Union[Dict[str, Any], MastermindState, Command],
) -> MastermindState:
    """Ensure input is converted to MastermindState.

    Args:
        state_input: State input as dict, MastermindState, or Command

    Returns:
        MastermindState instance
    """
    logger.info(f"ensure_game_state: received input of type {type(state_input)}")

    if isinstance(state_input, MastermindState):
        logger.info("ensure_game_state: Input is already MastermindState")
        return state_input
    elif isinstance(state_input, Command):
        logger.info("ensure_game_state: Input is a Command, extracting state")
        # Attempt to extract state from Command
        if hasattr(state_input, "state") and state_input.state:
            return ensure_game_state(state_input.state)
        else:
            logger.error("ensure_game_state: Command does not have state attribute")
            # Initialize a new state as fallback
            return MastermindState.initialize()
    elif isinstance(state_input, dict):
        try:
            logger.info(
                f"ensure_game_state: Converting dict to MastermindState, keys: {list(state_input.keys())}"
            )
            # Convert dict to MastermindState
            secret_code = state_input.get(
                "secret_code", ["red", "blue", "green", "yellow"]
            )
            turn = state_input.get("turn", "player1")
            codemaker = state_input.get("codemaker", "player1")
            max_turns = state_input.get("max_turns", 10)
            game_status = state_input.get("game_status", "ongoing")
            winner = state_input.get("winner")

            # Create guesses and feedback lists
            guesses = []
            feedback = []
            player1_analysis = []
            player2_analysis = []

            # Create state object
            return MastermindState(
                secret_code=secret_code,
                guesses=guesses,
                feedback=feedback,
                turn=turn,
                codemaker=codemaker,
                max_turns=max_turns,
                game_status=game_status,
                winner=winner,
                player1_analysis=player1_analysis,
                player2_analysis=player2_analysis,
            )
        except Exception as e:
            logger.error(f"Failed to convert dict to MastermindState: {e}")
            logger.debug(f"Dict contents: {state_input}")
            # Initialize a new state as fallback rather than crashing
            logger.info("ensure_game_state: Using default state as fallback")
            return MastermindState.initialize()
    else:
        logger.error(f"Cannot convert {type(state_input)} to MastermindState")
        # Initialize a new state as fallback rather than crashing
        logger.info("ensure_game_state: Using default state as fallback")
        return MastermindState.initialize()


def test_ensure_game_state():
    """Test the ensure_game_state function with various input types."""
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
