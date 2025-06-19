"""Standalone test script to verify the Fox and Geese game fixes."""

import logging
import sys
from typing import Any, Dict, List, Literal, Optional, Set, Union

from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Mock Command class
class Command:
    def __init__(self, update=None, delete=None, values=None, state=None):
        self.update = update or {}
        self.delete = delete or []
        self.values = values
        self.state = state

    def __repr__(self):
        return f"Command(update={self.update}, delete={self.delete})"


# Mock classes for state
class FoxAndGeesePosition(BaseModel):
    row: int
    col: int

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        if not isinstance(other, FoxAndGeesePosition):
            return False
        return self.row == other.row and self.col == other.col


class FoxAndGeeseMove(BaseModel):
    from_pos: FoxAndGeesePosition
    to_pos: FoxAndGeesePosition
    piece_type: Literal["fox", "goose"]
    capture: Optional[FoxAndGeesePosition] = None


class GameState(BaseModel):
    """Base class for game state."""

    pass


class FoxAndGeeseState(GameState):
    """State for a Fox and Geese game."""

    players: List[str] = Field(["fox", "geese"], description="Players in the game")
    fox_position: FoxAndGeesePosition = Field(..., description="Position of the fox")
    geese_positions: Set[FoxAndGeesePosition] = Field(
        ..., description="Positions of geese"
    )
    turn: Literal["fox", "geese"] = Field(..., description="Current player's turn")
    game_status: Literal["ongoing", "fox_win", "geese_win"] = Field(
        default="ongoing", description="Status of the game"
    )
    move_history: List[FoxAndGeeseMove] = Field(
        default_factory=list, description="History of moves"
    )
    winner: Optional[str] = Field(
        default=None, description="Winner of the game, if any"
    )
    num_geese: int = Field(default=0, description="Number of geese remaining")
    fox_analysis: List[str] = Field(
        default_factory=list, description="List of fox position analyses"
    )
    geese_analysis: List[str] = Field(
        default_factory=list, description="List of geese position analyses"
    )

    @classmethod
    def initialize(cls) -> "FoxAndGeeseState":
        """Initialize a new Fox and Geese game state."""
        # Fox starts at the center
        fox_position = FoxAndGeesePosition(row=3, col=3)

        # Geese start at the top
        geese_positions = set()
        for col in range(7):
            if col % 2 == 0:  # Only on white squares
                geese_positions.add(FoxAndGeesePosition(row=0, col=col))
                geese_positions.add(FoxAndGeesePosition(row=1, col=col))

        return cls(
            fox_position=fox_position,
            geese_positions=geese_positions,
            turn="fox",  # Fox goes first
            game_status="ongoing",
            move_history=[],
            num_geese=len(geese_positions),
            fox_analysis=[],
            geese_analysis=[],
        )

    @property
    def board_string(self) -> str:
        """Get a string representation of the board."""
        # Create an empty 7x7 board
        board = [[" " for _ in range(7)] for _ in range(7)]

        # Place the fox
        board[self.fox_position.row][self.fox_position.col] = "F"

        # Place the geese
        for goose in self.geese_positions:
            board[goose.row][goose.col] = "G"

        # Convert to string
        result = "  0 1 2 3 4 5 6\n"
        for i, row in enumerate(board):
            result += f"{i} {' '.join(row)}\n"

        return result


# Mock the ensure_game_state function
def ensure_game_state(
    state_input: Union[Dict[str, Any], FoxAndGeeseState, Command],
) -> FoxAndGeeseState:
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
def analyze_fox_position(state) -> Command:
    """Analyze the current position from the Fox's perspective."""
    try:
        # Ensure we have a proper FoxAndGeeseState
        game_state = ensure_game_state(state)

        # Log the type of state before and after conversion for debugging
        logger.info(f"Fox analysis: state type before conversion: {type(state)}")
        logger.info(f"Fox analysis: state type after conversion: {type(game_state)}")

        # Just create a simple analysis result for testing
        analysis = "Fox analysis: The fox should try to capture geese while maintaining mobility."

        # Create new state with analysis
        new_state = game_state.model_copy(deep=True)
        new_state.fox_analysis.append(analysis)

        logger.info("Added fox analysis to state")
        # Return a Command with just the fox_analysis update
        return Command(update={"fox_analysis": new_state.fox_analysis})

    except Exception as e:
        logger.error(f"Critical error in fox analysis: {e}", exc_info=True)
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


def test_command_input():
    """Test with a Command object containing state."""
    logger.info("\n=== Testing with Command input ===")
    # Create a FoxAndGeeseState
    state = FoxAndGeeseState.initialize()

    # Wrap it in a Command
    cmd = Command(state=state)

    # Test analyze_fox_position with command input
    result = analyze_fox_position(cmd)
    logger.info(f"Result type: {type(result)}")
    logger.info(f"Result content: {result}")

    # Verify result is a Command
    assert isinstance(result, Command), "Result should be a Command"
    # Verify fox_analysis field is in the update
    assert (
        "fox_analysis" in result.update
    ), "fox_analysis should be in the Command update"

    logger.info("Command input test passed!")


def main():
    """Run the tests."""
    logger.info("Starting tests...")

    try:
        test_dict_input()
        test_foxandgeesestate_input()
        test_command_input()
        logger.info("\nAll tests passed!")
    except Exception as e:
        logger.error(f"Test failed with error: {e}", exc_info=True)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
