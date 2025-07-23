"""State for the Mancala game.

This module defines the state for the Mancala game,
which includes the board, turn, game status, move history,
free turn, winner, and player analyses.
"""

import json
import logging
from typing import Any, Literal

from pydantic import Field, field_validator, model_validator

from haive.games.framework.base.state import GameState
from haive.games.mancala.models import MancalaAnalysis, MancalaMove

logger = logging.getLogger(__name__)


def extract_analysis_from_message(analysis: Any) -> dict[str, Any] | None:
    """Extract analysis data from an AIMessage object.

    Args:
        analysis: The analysis object to extract from.

    Returns:
        Extracted analysis data or None if extraction fails.
    """
    if isinstance(analysis, dict) and "position_evaluation" in analysis:
        return analysis

    if (
        hasattr(analysis, "additional_kwargs")
        and "tool_calls" in analysis.additional_kwargs
    ):
        try:
            tool_calls = analysis.additional_kwargs["tool_calls"]
            if tool_calls and len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call and "arguments" in tool_call["function"]:
                    args = json.loads(tool_call["function"]["arguments"])
                    return args
        except Exception as e:
            logger.exception(f"Error parsing analysis: {e}")

    return None


class MancalaState(GameState):
    """State for a Mancala game.

    This class defines the structure of the Mancala game state,
    which includes the board, turn, game status, move history,
    free turn, winner, and player analyses.

    Attributes:
        board: List of 14 integers representing the game board.
        turn: The current player's turn.
        game_status: The status of the game.
        move_history: List of moves made in the game.
        free_turn: Whether the current player gets a free turn.
        winner: The winner of the game, if any.
        player1_analysis: Analysis data for player 1.
        player2_analysis: Analysis data for player 2.
    """

    board: list[int] = Field(
        default_factory=lambda: [4] * 6 + [0] + [4] * 6 + [0],
        description="Mancala board with 14 positions",
    )
    turn: Literal["player1", "player2"] = Field(
        default="player1", description="Current player's turn"
    )
    game_status: Literal["ongoing", "ended"] = Field(
        default="ongoing", description="Status of the game"
    )
    move_history: list[MancalaMove] = Field(
        default_factory=list, description="History of moves"
    )
    free_turn: bool = Field(
        default=False, description="Whether the current player gets a free turn"
    )
    winner: Literal["player1", "player2", "draw", None] = Field(
        default=None, description="Winner of the game, if any"
    )
    player1_analyses: list[MancalaAnalysis] = Field(
        default_factory=list, description="Analysis for player 1"
    )
    player2_analyses: list[MancalaAnalysis] = Field(
        default_factory=list, description="Analysis for player 2"
    )

    @field_validator("board")
    @classmethod
    def validate_board(cls, v: list[int]) -> list[int]:
        """Validate that the board has exactly 14 positions.

        Args:
            v: The board to validate.

        Returns:
            The validated board.

        Raises:
            ValueError: If board doesn't have exactly 14 positions.
        """
        if len(v) != 14:
            raise ValueError("Board must have exactly 14 positions")
        return v

    @model_validator(mode="before")
    @classmethod
    def handle_initialization_data(cls, data: Any) -> Any:
        """Handle special initialization patterns from the framework."""
        if not isinstance(data, dict):
            return data

        # Handle the case where data comes wrapped in an 'initialize' key
        if "initialize" in data and isinstance(data["initialize"], dict):
            init_data = data["initialize"]
            stones_per_pit = init_data.get("stones_per_pit", 4)

            # Create proper board
            board = cls._create_initial_board(stones_per_pit)

            # Return properly structured data
            return {
                "board": board,
                "turn": "player1",
                "game_status": "ongoing",
                "move_history": [],
                "free_turn": False,
                "winner": None,
                "player1_analyses": [],
                "player2_analyses": [],
                "__pydantic_extra__": {
                    k: v
                    for k, v in data.items()
                    if k
                    not in [
                        "initialize",
                        "board",
                        "turn",
                        "game_status",
                        "move_history",
                        "free_turn",
                        "winner",
                        "player1_analyses",
                        "player2_analyses",
                    ]
                },
            }

        return data

    @model_validator(mode="before")
    @classmethod
    def handle_analysis_data(cls, data: Any) -> Any:
        """Handle conversion of analysis data to proper types."""
        if not isinstance(data, dict):
            return data

        # Convert player1_analyses items if needed
        if data.get("player1_analyses"):
            data["player1_analyses"] = cls._convert_analysis_list(
                data["player1_analyses"], "player1"
            )

        # Convert player2_analyses items if needed
        if data.get("player2_analyses"):
            data["player2_analyses"] = cls._convert_analysis_list(
                data["player2_analyses"], "player2"
            )

        return data

    @classmethod
    def initialize(cls, **kwargs) -> "MancalaState":
        """Initialize the Mancala game state.

        Args:
            **kwargs: Optional parameters including stones_per_pit.

        Returns:
            MancalaState: A fully initialized Mancala game state.
        """
        stones_per_pit = kwargs.get("stones_per_pit", 4)
        board = cls._create_initial_board(stones_per_pit)

        return cls(
            players=["player1", "player2"],
            board=board,
            turn="player1",
            game_status="ongoing",
            move_history=[],
            free_turn=False,
            winner=None,
            player1_analyses=[],
            player2_analyses=[],
        )

    @classmethod
    def _create_initial_board(cls, stones_per_pit: int) -> list[int]:
        """Create the initial board configuration.

        Args:
            stones_per_pit: Number of stones per pit.

        Returns:
            Initial board configuration.
        """
        board = [0] * 14
        # Player 1's pits (indices 0-5)
        for i in range(6):
            board[i] = stones_per_pit
        # Player 2's pits (indices 7-12)
        for i in range(7, 13):
            board[i] = stones_per_pit
        # Stores start empty (indices 6 and 13)
        board[6] = 0  # Player 1's store
        board[13] = 0  # Player 2's store
        return board

    @classmethod
    def _convert_analysis_list(
        cls, analyses: list[Any], player: str
    ) -> list[dict[str, Any]]:
        """Convert a list of analysis objects to proper format.

        Args:
            analyses: List of analysis objects to convert.
            player: Player name for logging.

        Returns:
            List of converted analysis dictionaries.
        """
        converted_analyses = []
        for analysis in analyses:
            extracted = extract_analysis_from_message(analysis)
            if extracted:
                converted_analyses.append(extracted)
            else:
                logger.warning(
                    f"Could not extract analysis for {player}: {type(analysis)}"
                )
        return converted_analyses

    def display_board(self) -> str:
        """Display the board in a human-readable format.

        Returns:
            A string representation of the current board state.
        """
        # Player 2's side (displayed on top, right to left)
        p2_pits = " ".join(f"{self.board[i]:2}" for i in range(12, 6, -1))
        # Stores
        p2_store = f"{self.board[13]:2}"
        p1_store = f"{self.board[6]:2}"
        # Player 1's side (displayed on bottom, left to right)
        p1_pits = " ".join(f"{self.board[i]:2}" for i in range(6))

        board_display = f"""
        Player 2
    {p2_pits}
{p2_store}                    {p1_store}
    {p1_pits}
        Player 1
        """
        return board_display.strip()

    def get_valid_moves(self, player: Literal["player1", "player2"]) -> list[int]:
        """Get valid moves for the specified player.

        Args:
            player: The player to get valid moves for.

        Returns:
            List of valid pit indices the player can choose from.
        """
        if player == "player1":
            # Player 1's pits are indices 0-5
            return [i for i in range(6) if self.board[i] > 0]
        # Player 2's pits are indices 7-12
        valid_indices = [i for i in range(7, 13) if self.board[i] > 0]
        # Convert to 0-5 range for consistency with MancalaMove
        return [i - 7 for i in valid_indices]

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            True if the game is over, False otherwise.
        """
        # Game is over if either side has no stones in their pits
        player1_empty = all(self.board[i] == 0 for i in range(6))
        player2_empty = all(self.board[i] == 0 for i in range(7, 13))
        return player1_empty or player2_empty

    def get_scores(self) -> dict[str, int]:
        """Get the current scores for both players.

        Returns:
            Dictionary with player1 and player2 scores.
        """
        return {
            "player1": self.board[6],
            "player2": self.board[13],
        }

    def determine_winner(self) -> Literal["player1", "player2", "draw"]:
        """Determine the winner of the game.

        Returns:
            The winner of the game or 'draw' if tied.
        """
        # Collect remaining stones into stores
        final_board = self.board.copy()

        # Player 1's remaining stones
        for i in range(6):
            final_board[6] += final_board[i]
            final_board[i] = 0

        # Player 2's remaining stones
        for i in range(7, 13):
            final_board[13] += final_board[i]
            final_board[i] = 0

        # Determine winner
        if final_board[6] > final_board[13]:
            return "player1"
        if final_board[13] > final_board[6]:
            return "player2"
        return "draw"
