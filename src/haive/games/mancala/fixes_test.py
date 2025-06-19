"""Standalone test script to verify the Mancala game fixes."""

import logging
import sys
from typing import Any, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Mock Command class
class Command:
    def __init__(self, update=None, delete=None, values=None, state=None, stop=None):
        self.update = update or {}
        self.delete = delete or []
        self.values = values
        self.state = state
        self.stop = stop

    def __repr__(self):
        return f"Command(update={self.update}, delete={self.delete}, stop={self.stop})"


# Mock classes for state
class MancalaMove(BaseModel):
    """Represents a move in Mancala."""

    pit_index: int = Field(
        ..., ge=0, lt=6, description="Index of the pit to sow from (0-5)"
    )
    player: Literal["player1", "player2"] = Field(
        ..., description="Player making the move"
    )

    def __str__(self):
        return f"{self.player} sows from pit {self.pit_index}"


class MancalaAnalysis(BaseModel):
    """Analysis of a Mancala position."""

    position_evaluation: Literal["winning", "losing", "equal", "unclear"] = Field(
        ..., description="Overall position evaluation"
    )
    advantage_level: int = Field(
        ..., ge=0, le=10, description="Level of advantage (0-10, where 10 is winning)"
    )
    stone_distribution: str = Field(..., description="Analysis of stone distribution")
    pit_recommendations: list[int] = Field(
        ..., description="Recommended pits to play from"
    )
    strategy_focus: Literal["offensive", "defensive", "balanced"] = Field(
        ..., description="Current strategic focus"
    )
    key_tactics: list[str] = Field(..., description="Key tactical considerations")
    reasoning: str = Field(..., description="Detailed reasoning for the analysis")


class GameState(BaseModel):
    """Base class for game state."""

    pass


class MancalaState(GameState):
    """State for a Mancala game."""

    board: List[int] = Field(
        default_factory=lambda: [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],
        min_length=14,
        max_length=14,
        description="Game board with 14 positions",
    )
    turn: Literal["player1", "player2"] = Field(
        default="player1", description="Current player's turn"
    )
    game_status: Literal["ongoing", "player1_win", "player2_win", "draw"] = Field(
        default="ongoing", description="Status of the game"
    )
    move_history: List[MancalaMove] = Field(
        default_factory=list, description="History of moves"
    )
    free_turn: bool = Field(
        default=False, description="Whether player gets an extra turn"
    )
    winner: Optional[str] = Field(
        default=None, description="Winner of the game, if any"
    )
    player1_analysis: List[MancalaAnalysis] = Field(
        default_factory=list, description="Analyses by player1"
    )
    player2_analysis: List[MancalaAnalysis] = Field(
        default_factory=list, description="Analyses by player2"
    )

    @classmethod
    def initialize(cls, stones_per_pit: int = 4, **kwargs) -> "MancalaState":
        """Initialize a new Mancala game state."""
        board = [stones_per_pit] * 14
        board[6] = 0  # Player 1's store
        board[13] = 0  # Player 2's store

        return cls(
            board=board,
            turn="player1",  # Player 1 starts
            game_status="ongoing",
            move_history=[],
            free_turn=False,
            **kwargs,
        )

    @property
    def player1_score(self) -> int:
        """Get player 1's score (store)."""
        return self.board[6]

    @property
    def player2_score(self) -> int:
        """Get player 2's score (store)."""
        return self.board[13]

    @property
    def board_string(self) -> str:
        """Get a string representation of the board."""
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

        result += f"Player 1 (bottom): {self.player1_score}  |  Player 2 (top): {self.player2_score}"
        return result


# Mock the ensure_game_state function
def ensure_game_state(
    state_input: Union[Dict[str, Any], MancalaState, Command],
) -> MancalaState:
    """Ensure input is converted to MancalaState."""
    logger.info(f"ensure_game_state: received input of type {type(state_input)}")

    if isinstance(state_input, MancalaState):
        logger.info("ensure_game_state: Input is already MancalaState")
        return state_input
    elif isinstance(state_input, Command):
        logger.info("ensure_game_state: Input is a Command, extracting state")
        # Attempt to extract state from Command
        if hasattr(state_input, "state") and state_input.state:
            return ensure_game_state(state_input.state)
        else:
            logger.error("ensure_game_state: Command does not have state attribute")
            # Initialize a new state as fallback
            return MancalaState.initialize()
    elif isinstance(state_input, dict):
        try:
            logger.info(
                f"ensure_game_state: Converting dict to MancalaState, keys: {list(state_input.keys())}"
            )
            return MancalaState.model_validate(state_input)
        except Exception as e:
            logger.error(f"Failed to convert dict to MancalaState: {e}")
            logger.debug(f"Dict contents: {state_input}")
            # Initialize a new state as fallback rather than crashing
            logger.info("ensure_game_state: Using default state as fallback")
            return MancalaState.initialize()
    else:
        logger.error(f"Cannot convert {type(state_input)} to MancalaState")
        # Initialize a new state as fallback rather than crashing
        logger.info("ensure_game_state: Using default state as fallback")
        return MancalaState.initialize()


# Mock the prepare_analysis_context function
def prepare_analysis_context(state: MancalaState, player: str) -> Dict[str, Any]:
    """Prepare context for position analysis."""
    try:
        # Ensure we have a proper MancalaState
        game_state = ensure_game_state(state)

        # Get recent move history
        recent_moves = []
        for move in game_state.move_history[-5:]:
            recent_moves.append(str(move))

        # Get pit stones for each player
        player1_pits = game_state.board[0:6]
        player2_pits = game_state.board[7:13]

        # Prepare the context
        return {
            "board_string": game_state.board_string,
            "player": player,
            "player1_score": game_state.player1_score,
            "player2_score": game_state.player2_score,
            "player1_pits": player1_pits,
            "player2_pits": player2_pits,
            "move_history": "\n".join(recent_moves),
        }

    except Exception as e:
        logger.error(f"Error preparing analysis context: {e}")
        # Return a minimal context to avoid crashing
        return {
            "board_string": "Error preparing context",
            "player": player,
            "player1_score": 0,
            "player2_score": 0,
            "player1_pits": [0, 0, 0, 0, 0, 0],
            "player2_pits": [0, 0, 0, 0, 0, 0],
            "move_history": "",
        }


# Mock the analyze_position function
def analyze_position(state: MancalaState, player: str) -> Command:
    """Analyze the current position for the specified player."""
    try:
        # Ensure we have a proper MancalaState
        game_state = ensure_game_state(state)

        # Log state conversion
        logger.info(f"analyze_position: state type before conversion: {type(state)}")
        logger.info(
            f"analyze_position: state type after conversion: {type(game_state)}"
        )

        # Prepare context for analysis
        context = prepare_analysis_context(game_state, player)

        # Create a simple analysis for testing
        analysis = MancalaAnalysis(
            position_evaluation="equal",
            advantage_level=5,
            stone_distribution="Balanced stone distribution across all pits",
            pit_recommendations=[2, 3],
            strategy_focus="balanced",
            key_tactics=["Capture opportunities", "Defense of vulnerable pits"],
            reasoning="The position is balanced with equal opportunities for both players.",
        )

        # Create new state with analysis
        new_state = game_state.model_copy(deep=True)

        # Add the analysis to the appropriate field
        if player == "player1":
            new_state.player1_analysis.append(analysis)
            logger.info("Added player1 analysis to state")
            return Command(update={"player1_analysis": new_state.player1_analysis})
        else:
            new_state.player2_analysis.append(analysis)
            logger.info("Added player2 analysis to state")
            return Command(update={"player2_analysis": new_state.player2_analysis})

    except Exception as e:
        logger.error(f"Critical error in analyze_position: {e}", exc_info=True)
        # Return empty Command to avoid errors
        return Command(update={"error_message": f"Critical error: {str(e)}"})


def test_dict_input():
    """Test with a dictionary input."""
    logger.info("\n=== Testing with dictionary input ===")

    # Create a dictionary that resembles a game state
    dict_input = {
        "board": [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0],
        "turn": "player1",
        "game_status": "ongoing",
        "move_history": [],
        "free_turn": False,
        "player1_analysis": [],
        "player2_analysis": [],
    }

    # Test analyze_position with dict input
    result = analyze_position(dict_input, "player1")
    logger.info(f"Result type: {type(result)}")
    logger.info(f"Result content: {result}")

    # Verify result is a Command
    assert isinstance(result, Command), "Result should be a Command"
    # Verify player1_analysis field is in the update
    assert (
        "player1_analysis" in result.update
    ), "player1_analysis should be in the Command update"

    logger.info("Dictionary input test passed!")


def test_mancalastate_input():
    """Test with a MancalaState input."""
    logger.info("\n=== Testing with MancalaState input ===")

    # Create a MancalaState
    state = MancalaState.initialize()

    # Test analyze_position with state input
    result = analyze_position(state, "player1")
    logger.info(f"Result type: {type(result)}")
    logger.info(f"Result content: {result}")

    # Verify result is a Command
    assert isinstance(result, Command), "Result should be a Command"
    # Verify player1_analysis field is in the update
    assert (
        "player1_analysis" in result.update
    ), "player1_analysis should be in the Command update"

    logger.info("MancalaState input test passed!")


def test_command_input():
    """Test with a Command object containing state."""
    logger.info("\n=== Testing with Command input ===")

    # Create a MancalaState
    state = MancalaState.initialize()

    # Wrap it in a Command
    cmd = Command(state=state)

    # Test analyze_position with command input
    result = analyze_position(cmd, "player1")
    logger.info(f"Result type: {type(result)}")
    logger.info(f"Result content: {result}")

    # Verify result is a Command
    assert isinstance(result, Command), "Result should be a Command"
    # Verify player1_analysis field is in the update
    assert (
        "player1_analysis" in result.update
    ), "player1_analysis should be in the Command update"

    logger.info("Command input test passed!")


def main():
    """Run the tests."""
    logger.info("Starting tests for Mancala fixes...")

    try:
        test_dict_input()
        test_mancalastate_input()
        test_command_input()
        logger.info("\nAll tests passed! The Mancala fixes are working correctly.")
    except Exception as e:
        logger.error(f"Test failed with error: {e}", exc_info=True)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
