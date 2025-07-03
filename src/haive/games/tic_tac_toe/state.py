"""Tic Tac Toe game models, including core state definition for gameplay and logic.

This module defines the `TicTacToeState` class used to represent the board, track players, and capture gameplay data such as history and analysis.
It includes helper properties to assess the board and enforce its structure.
"""

from typing import Annotated, Any, Literal

from pydantic import Field, field_validator

from haive.games.framework.base.state import GameState
from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove


def replace_reducer(left: Any, right: Any) -> Any:
    """Reducer that always takes the new value (right side)."""
    return right


def add_messages_reducer(left: list, right: list) -> list:
    """Reducer for message-like lists that should be concatenated."""
    if not isinstance(left, list):
        left = []
    if not isinstance(right, list):
        right = []
    return left + right


def replace_board_reducer(left: Any, right: Any) -> Any:
    """Special reducer for the board that always replaces with the new board."""
    return right


class TicTacToeState(GameState):
    """Represents the full game state of a Tic Tac Toe match.

    All fields use explicit reducers to avoid LangGraph concurrent update issues.
    """

    # Player management - this can accumulate
    players: Annotated[list[str], add_messages_reducer] = Field(
        default_factory=lambda: ["player1", "player2"],
        description="List of players in the game",
    )

    # Game board - always replace with new board
    board: Annotated[list[list[str | None]], replace_board_reducer] = Field(
        default_factory=lambda: [[None for _ in range(3)] for _ in range(3)],
        description="3x3 game board, each cell can be None, 'X', or 'O'",
    )

    # Game state fields - always replace with new value
    turn: Annotated[Literal["X", "O"], replace_reducer] = Field(
        default="X", description="Current player's turn"
    )
    game_status: Annotated[
        Literal["ongoing", "X_win", "O_win", "draw"], replace_reducer
    ] = Field(default="ongoing", description="Status of the game")

    # Move history - accumulate moves
    move_history: Annotated[list[TicTacToeMove], add_messages_reducer] = Field(
        default_factory=list, description="History of moves"
    )

    # Error handling - replace with new error
    error_message: Annotated[str | None, replace_reducer] = Field(
        default=None, description="Error message if any"
    )

    # Winner - replace with new value
    winner: Annotated[str | None, replace_reducer] = Field(
        default=None, description="Winner of the game, if any"
    )

    # Player assignment - replace with new values
    player_X: Annotated[Literal["player1", "player2"], replace_reducer] = Field(
        default="player1", description="Which player is X"
    )
    player_O: Annotated[Literal["player1", "player2"], replace_reducer] = Field(
        default="player2", description="Which player is O"
    )

    # Analysis storage - accumulate analyses
    player1_analysis: Annotated[list[TicTacToeAnalysis], add_messages_reducer] = Field(
        default_factory=list, description="Analyses by player1"
    )
    player2_analysis: Annotated[list[TicTacToeAnalysis], add_messages_reducer] = Field(
        default_factory=list, description="Analyses by player2"
    )

    @field_validator("board")
    def validate_board(cls, board):
        """Validate that the board is a 3x3 grid with valid symbols ('X', 'O', or None).

        Args:
            board (List[List[Optional[str]]]): The board to validate.

        Raises:
            ValueError: If the board does not meet shape or value constraints.

        Returns:
            List[List[Optional[str]]]: Validated board.
        """
        # If board is empty, initialize a proper 3x3 board
        if not board or len(board) == 0:
            return [[None for _ in range(3)] for _ in range(3)]

        if len(board) != 3:
            raise ValueError("Board must have 3 rows")
        for row in board:
            if len(row) != 3:
                raise ValueError("Each row must have 3 columns")
            for cell in row:
                if cell is not None and cell not in ["X", "O"]:
                    raise ValueError(
                        f"Cell values must be None, 'X', or 'O', got {cell}"
                    )
        return board

    @property
    def empty_cells(self) -> list[tuple[int, int]]:
        """Return a list of coordinates for all empty cells on the board."""
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]

    @property
    def is_board_full(self) -> bool:
        """Check whether the board is completely filled."""
        return all(self.board[i][j] is not None for i in range(3) for j in range(3))

    @property
    def current_player_name(self) -> str:
        """Get the name of the current player (player1 or player2).

        Returns:
            str: The identifier for the player whose turn it is.
        """
        return self.player_X if self.turn == "X" else self.player_O

    @property
    def board_string(self) -> str:
        """Get a pretty-printed string representation of the board.

        Returns:
            str: Multiline string representing the current board state.
        """
        result = []
        result.append("   0 1 2")
        result.append("  -------")
        for i, row in enumerate(self.board):
            row_str = f"{i} |"
            for cell in row:
                if cell is None:
                    row_str += " |"
                else:
                    row_str += f"{cell}|"
            result.append(row_str)
            result.append("  -------")
        return "\n".join(result)

    @classmethod
    def initialize(cls, **kwargs):
        """Initialize a new Tic Tac Toe game."""
        first_player = kwargs.get("first_player", "X")
        player_X = kwargs.get("player_X", "player1")
        player_O = kwargs.get("player_O", "player2")

        return cls(
            players=["player1", "player2"],
            board=[[None for _ in range(3)] for _ in range(3)],
            turn=first_player,
            game_status="ongoing",
            move_history=[],
            error_message=None,
            winner=None,
            player_X=player_X,
            player_O=player_O,
            player1_analysis=[],
            player2_analysis=[],
        )
