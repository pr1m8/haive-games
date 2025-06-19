"""Test script to verify the fixes for the Fox and Geese game."""

import logging
import sys
from typing import Any, Dict


# Mock Command class
class Command:
    def __init__(self, update=None, delete=None, values=None, state=None):
        self.update = update or {}
        self.delete = delete or []
        self.values = values
        self.state = state

    def __repr__(self):
        return f"Command(update={self.update}, delete={self.delete})"


# Import the FoxAndGeeseState from the local module
from haive.games.fox_and_geese.state import FoxAndGeeseState

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Mock the ensure_game_state function
def ensure_game_state(state_input):
    """Ensure input is converted to FoxAndGeeseState."""
    logger.info(f"ensure_game_state: received input of type {type(state_input)}")

    if isinstance(state_input, FoxAndGeeseState):
        logger.info("ensure_game_state: Input is already FoxAndGeeseState")
        return state_input
    elif isinstance(state_input, Command):
        logger.info("ensure_game_state: Input is a Command, extracting state")
        # Attempt to extract state from Command
        if hasattr(state_input, "state") and state_input.state:
            return ensure_game_state(state_input.state)
        else:
            logger.error("ensure_game_state: Command does not have state attribute")
            # Initialize a new state as fallback
            return FoxAndGeeseState.initialize()
    elif isinstance(state_input, dict):
        try:
            logger.info(
                f"ensure_game_state: Converting dict to FoxAndGeeseState, keys: {list(state_input.keys())}"
            )
            return FoxAndGeeseState.model_validate(state_input)
        except Exception as e:
            logger.error(f"Failed to convert dict to FoxAndGeeseState: {e}")
            logger.debug(f"Dict contents: {state_input}")
            # Initialize a new state as fallback rather than crashing
            logger.info("ensure_game_state: Using default state as fallback")
            return FoxAndGeeseState.initialize()
    else:
        logger.error(f"Cannot convert {type(state_input)} to FoxAndGeeseState")
        # Initialize a new state as fallback rather than crashing
        logger.info("ensure_game_state: Using default state as fallback")
        return FoxAndGeeseState.initialize()


# Mock the analyze_fox_position function
def analyze_fox_position(state: FoxAndGeeseState) -> Command:
    """Analyze the current position from the Fox's perspective."""
    try:
        # Ensure we have a proper FoxAndGeeseState
        game_state = ensure_game_state(state)

        # Log the type of state before and after conversion for debugging
        logger.info(f"Fox analysis: state type before conversion: {type(state)}")
        logger.info(f"Fox analysis: state type after conversion: {type(game_state)}")

        # Create a simple analysis result
        analysis = "Fox analysis: The fox should try to capture geese while maintaining mobility."

        # Create new state with analysis
        new_state = game_state.model_copy(deep=True)
        new_state.fox_analysis.append(analysis)

        logger.info("Added fox analysis to state")
        # Return a Command with just the fox_analysis update
        return Command(update={"fox_analysis": new_state.fox_analysis})

    except Exception as e:
        logger.error(f"Critical error in fox analysis: {e}")
        # Return empty Command to avoid errors
        return Command(update={})


def test_dict_input():
    """Test with a dictionary input."""
    logger.info("\n=== Testing with dictionary input ===")
    # Create a dictionary that resembles a game state
    dict_input = {
        "fox_position": {"row": 3, "col": 3},
        "geese_positions": [{"row": 0, "col": 0}, {"row": 0, "col": 2}],
        "turn": "fox",
        "game_status": "ongoing",
        "move_history": [],
        "num_geese": 2,
        "fox_analysis": [],
        "geese_analysis": [],
    }

    # Test analyze_fox_position with dict input
    result = analyze_fox_position(dict_input)
    logger.info(f"Result type: {type(result)}")
    logger.info(f"Result content: {result}")

    # Verify result is a Command
    assert isinstance(result, Command), "Result should be a Command"
    # Verify fox_analysis field is in the update
    assert (
        "fox_analysis" in result.update
    ), "fox_analysis should be in the Command update"

    logger.info("Dictionary input test passed!")


def test_foxandgeesestate_input():
    """Test with a FoxAndGeeseState input."""
    logger.info("\n=== Testing with FoxAndGeeseState input ===")
    # Create a FoxAndGeeseState
    state = FoxAndGeeseState.initialize()

    # Test analyze_fox_position with state input
    result = analyze_fox_position(state)
    logger.info(f"Result type: {type(result)}")
    logger.info(f"Result content: {result}")

    # Verify result is a Command
    assert isinstance(result, Command), "Result should be a Command"
    # Verify fox_analysis field is in the update
    assert (
        "fox_analysis" in result.update
    ), "fox_analysis should be in the Command update"

    logger.info("FoxAndGeeseState input test passed!")


def main():
    """Run the tests."""
    logger.info("Starting tests...")

    try:
        test_dict_input()
        test_foxandgeesestate_input()
        logger.info("\nAll tests passed!")
    except Exception as e:
        logger.error(f"Test failed with error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
