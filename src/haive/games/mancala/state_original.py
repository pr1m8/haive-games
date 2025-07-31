"""State for the Mancala game.

This module defines the state for the Mancala game, which includes the board, turn, game
status, move history, free turn, winner, and player analyses.

"""

import json
import logging
from typing import Any, Literal

from pydantic import Field, field_validator, model_validator

from haive.games.framework.base.state import GameState
from haive.games.mancala.models import MancalaAnalysis, MancalaMove

logger = logging.getLogger(__name__)


class MancalaState(GameState):
    """State for a Mancala game.

    This class defines the structure of the Mancala game state, which includes the
    board, turn, game status, move history, free turn, winner, and player analyses.

    """

    # The board has 14 pits:
    # - Indices 0-5: Player 1's pits (bottom row, left to right)
    # - Index 6: Player 1's store (right)
    # - Indices 7-12: Player 2's pits (top row, right to left)
    # - Index 13: Player 2's store (left)
    board: list[int] = Field(
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
    move_history: list[MancalaMove] = Field(
        default_factory=list, description="History of moves"
    )
    free_turn: bool = Field(
        default=False, description="Whether player gets an extra turn"
    )
    winner: str | None = Field(default=None, description="Winner of the game, if any")
    player1_analysis: list[MancalaAnalysis] = Field(
        default_factory=list, description="Analyses by player1"
    )
    player2_analysis: list[MancalaAnalysis] = Field(
        default_factory=list, description="Analyses by player2"
    )

    @field_validator("board")
    @classmethod
    def validate_board(cls, v):
        """Validate the board has exactly 14 positions."""
        if len(v) != 14:
            raise ValueError("Board must have exactly 14 positions")
        return v

    @model_validator(mode="before")
    @classmethod
    def handle_initialization_data(cls, data):
        """Handle special initialization patterns from the framework."""
        if isinstance(data, dict):
            # Handle the case where data comes wrapped in an 'initialize' key
            if "initialize" in data and isinstance(data["initialize"], dict):
                init_data = data["initialize"]
                stones_per_pit = init_data.get("stones_per_pit", 4)

                # Create proper board
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

                # Return properly structured data
                return {
                    "board": board,
                    "turn": "player1",
                    "game_status": "ongoing",
                    "move_history": [],
                    "free_turn": False,
                    "winner": None,
                    "player1_analysis": [],
                    "player2_analysis": [],
                    # Include any additional fields from the outer dict
                    **{k: v for k, v in data.items() if k != "initialize"},
                }

            # Handle case where data has fields but no proper structure
            if "board" not in data or "turn" not in data:
                # This might be incomplete data, provide defaults
                stones_per_pit = data.get("stones_per_pit", 4)

                board = [0] * 14
                # Player 1's pits (indices 0-5)
                for i in range(6):
                    board[i] = stones_per_pit
                # Player 2's pits (indices 7-12)
                for i in range(7, 13):
                    board[i] = stones_per_pit
                # Stores start empty
                board[6] = 0  # Player 1's store
                board[13] = 0  # Player 2's store

                return {
                    "board": data.get("board", board),
                    "turn": data.get("turn", "player1"),
                    "game_status": data.get("game_status", "ongoing"),
                    "move_history": data.get("move_history", []),
                    "free_turn": data.get("free_turn", False),
                    "winner": data.get("winner", None),
                    "player1_analysis": data.get("player1_analysis", []),
                    "player2_analysis": data.get("player2_analysis", []),
                    **{
                        k: v
                        for k, v in data.items()
                        if k
                        not in [
                            "board",
                            "turn",
                            "game_status",
                            "move_history",
                            "free_turn",
                            "winner",
                            "player1_analysis",
                            "player2_analysis",
                        ]
                    },
                }

        return data

    @model_validator(mode="before")
    @classmethod
    def handle_analysis_data(cls, data):
        """Handle conversion of analysis data to proper types."""
        if isinstance(data, dict):
            # Convert player1_analysis items if needed
            if data.get("player1_analysis"):
                converted_analyses = []
                for analysis in data["player1_analysis"]:
                    # If it's a dict with required fields, use it
                    if isinstance(analysis, dict) and "position_evaluation" in analysis:
                        converted_analyses.append(analysis)
                    # If it's an AIMessage, try to extract the data
                    elif (
                        hasattr(analysis, "additional_kwargs")
                        and "tool_calls" in analysis.additional_kwargs
                    ):
                        try:
                            tool_calls = analysis.additional_kwargs["tool_calls"]
                            if tool_calls and len(tool_calls) > 0:
                                tool_call = tool_calls[0]
                                if (
                                    "function" in tool_call
                                    and "arguments" in tool_call["function"]
                                ):
                                    args = json.loads(
                                        tool_call["function"]["arguments"]
                                    )
                                    converted_analyses.append(args)
                        except Exception as e:
                            print(f"Error parsing player1_analysis: {e}")
                            # Skip this item
                            continue

                # Replace with converted data
                if converted_analyses:
                    data["player1_analysis"] = converted_analyses

            # Convert player2_analysis items if needed
            if data.get("player2_analysis"):
                converted_analyses = []
                for analysis in data["player2_analysis"]:
                    # If it's a dict with required fields, use it
                    if isinstance(analysis, dict) and "position_evaluation" in analysis:
                        converted_analyses.append(analysis)
                    # If it's an AIMessage, try to extract the data
                    elif (
                        hasattr(analysis, "additional_kwargs")
                        and "tool_calls" in analysis.additional_kwargs
                    ):
                        try:
                            tool_calls = analysis.additional_kwargs["tool_calls"]
                            if tool_calls and len(tool_calls) > 0:
                                tool_call = tool_calls[0]
                                if (
                                    "function" in tool_call
                                    and "arguments" in tool_call["function"]
                                ):
                                    args = json.loads(
                                        tool_call["function"]["arguments"]
                                    )
                                    converted_analyses.append(args)
                        except Exception as e:
                            print(f"Error parsing player2_analysis: {e}")
                            # Skip this item
                            continue

                # Replace with converted data
                if converted_analyses:
                    data["player2_analysis"] = converted_analyses

        return data

    @classmethod
    def initialize(cls, stones_per_pit: int = 4, **kwargs) -> "MancalaState":
        """Initialize a new Mancala game state.

        Args:
            stones_per_pit: Number of stones to place in each pit initially
            **kwargs: Additional keyword arguments for customization

        Returns:
            MancalaState: A new initialized game state

        """
        # Create board with 14 positions
        board = [0] * 14

        # Fill player pits with stones
        # Player 1's pits (indices 0-5)
        for i in range(6):
            board[i] = stones_per_pit

        # Player 2's pits (indices 7-12)
        for i in range(7, 13):
            board[i] = stones_per_pit

        # Stores start empty (indices 6 and 13)
        board[6] = 0  # Player 1's store
        board[13] = 0  # Player 2's store

        return cls(
            board=board,
            turn="player1",  # Player 1 starts
            game_status="ongoing",
            move_history=[],
            free_turn=False,
            winner=None,
            player1_analysis=[],
            player2_analysis=[],
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

        result += f"Player 1 (bottom): {self.player1_score}  |  Player 2 (top): {
            self.player2_score
        }"
        return result

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            bool: True if game is over, False otherwise

        """
        # Check if either player's side is empty
        player1_stones = sum(self.board[0:6])
        player2_stones = sum(self.board[7:13])

        return player1_stones == 0 or player2_stones == 0

    def get_winner(self) -> str | None:
        """Determine the winner of the game.

        Returns:
            Optional[str]: "player1", "player2", "draw", or None if game ongoing

        """
        if not self.is_game_over():
            return None

        if self.player1_score > self.player2_score:
            return "player1"
        if self.player2_score > self.player1_score:
            return "player2"
        return "draw"

    def get_valid_moves(self, player: str | None = None) -> list[int]:
        """Get valid moves for the current or specified player.

        Args:
            player: Player to get moves for ("player1" or "player2").
                   If None, uses current turn.

        Returns:
            List[int]: List of valid pit indices that can be played

        """
        if player is None:
            player = self.turn

        if player == "player1":
            # Player 1 can move from pits 0-5 if they contain stones
            return [i for i in range(6) if self.board[i] > 0]
        # Player 2 can move from pits 7-12 if they contain stones
        return [i for i in range(7, 13) if self.board[i] > 0]

    def copy(self) -> "MancalaState":
        """Create a deep copy of the current state.

        Returns:
            MancalaState: A new instance with the same values

        """
        return MancalaState(
            board=self.board.copy(),
            turn=self.turn,
            game_status=self.game_status,
            move_history=self.move_history.copy(),
            free_turn=self.free_turn,
            winner=self.winner,
            player1_analysis=self.player1_analysis.copy(),
            player2_analysis=self.player2_analysis.copy(),
        )

    def model_dump(self, **kwargs) -> dict[str, Any]:
        """Override model_dump to ensure proper serialization."""
        data = super().model_dump(**kwargs)
        # Ensure board is always a list of 14 integers
        if "board" in data and len(data["board"]) != 14:
            # Reset to default board if corrupted
            data["board"] = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        return data

    def __str__(self) -> str:
        """String representation of the state."""
        return f"MancalaState(turn={self.turn}, status={self.game_status}, score=({
            self.player1_score
        }, {self.player2_score}))"

    def __repr__(self) -> str:
        """Detailed representation of the state."""
        return (
            f"MancalaState(board={self.board}, turn='{self.turn}', "
            f"game_status='{self.game_status}', player1_score={self.player1_score}, "
            f"player2_score={self.player2_score})"
        )
