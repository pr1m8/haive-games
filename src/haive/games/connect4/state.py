"""Connect4 game state module.

This module defines the core state representation for Connect4 games,
including board representation, move tracking, and game status.

Example:
    >>> from haive.games.connect4.state import Connect4State
    >>> from haive.games.connect4.models import Connect4Move
    >>>
    >>> # Initialize a new game
    >>> state = Connect4State.initialize()
    >>> state.board_string  # Get string representation
    >>>
    >>> # Check game properties
    >>> state.is_column_full(3)  # Check if column is full
    >>> state.get_next_row(3)    # Get next available row in column
"""

from typing import Literal

from pydantic import Field, field_validator

from haive.games.connect4.models import Connect4Move
from haive.games.framework.base.state import GameState


class Connect4State(GameState):
    """State representation for a Connect4 game.

    This class represents the complete state of a Connect4 game, including:
        - Board representation (6x7 grid)
        - Current player's turn
        - Game status and winner
        - Move history
        - Position analysis for both players

    The board is represented as a 6x7 grid of cells, where each cell can be:
        - None: Empty cell
        - "red": Red player's piece
        - "yellow": Yellow player's piece

    Attributes:
        board (list[list[str | None]]): 6x7 board representation (rows x columns)
        turn (Literal["red", "yellow"]): Current player's turn
        game_status (Literal["ongoing", "red_win", "yellow_win", "draw"]): Game status
        move_history (list[Connect4Move]): History of moves made in the game
        red_analysis (list[dict]): Analysis history for the red player
        yellow_analysis (list[dict]): Analysis history for the yellow player
        winner (Optional[str]): Winner of the game, if any
        error_message (Optional[str]): Error message from the last operation

    Examples:
        >>> state = Connect4State.initialize()
        >>> state.turn
        'red'
        >>> state.is_column_full(3)
        False
    """

    board: list[list[str | None]] = Field(
        ..., description="6x7 board representation (rows x columns)"
    )
    turn: Literal["red", "yellow"] = Field(..., description="Current player's turn")
    game_status: Literal["ongoing", "red_win", "yellow_win", "draw"] = Field(
        default="ongoing", description="Status of the game"
    )
    move_history: list[Connect4Move] = Field(
        default_factory=list, description="History of moves"
    )
    red_analysis: list[dict] = Field(
        default_factory=list, description="Analysis history for red player"
    )
    yellow_analysis: list[dict] = Field(
        default_factory=list, description="Analysis history for yellow player"
    )
    winner: str | None = Field(default=None, description="Winner of the game, if any")
    error_message: str | None = Field(default=None, description="Error message if any")

    @property
    def board_string(self) -> str:
        """Get a string representation of the board.

        Returns a formatted string representation of the current board state,
        with column and row indices, cell contents, and borders.

        Returns:
            str: String representation of the board

        Example:
            >>> state = Connect4State.initialize()
            >>> print(state.board_string)
              0 1 2 3 4 5 6
              -------------
            0| | | | | | | |
            1| | | | | | | |
            2| | | | | | | |
            3| | | | | | | |
            4| | | | | | | |
            5| | | | | | | |
              -------------
              0 1 2 3 4 5 6
        """
        result = []

        # Column headers
        result.append("  0 1 2 3 4 5 6")
        result.append("  -------------")

        # Board rows (top to bottom)
        for i, row in enumerate(self.board):
            row_str = f"{i}|"
            for cell in row:
                if cell is None:
                    row_str += " |"
                elif cell == "red":
                    row_str += "R|"
                else:  # yellow
                    row_str += "Y|"
            result.append(row_str)

        result.append("  -------------")
        result.append("  0 1 2 3 4 5 6")

        return "\n".join(result)

    def is_column_full(self, column: int) -> bool:
        """Check if a column is full.

        Args:
            column: Column index to check (0-6)

        Returns:
            bool: True if the column is full, False otherwise

        Example:
            >>> state = Connect4State.initialize()
            >>> state.is_column_full(3)
            False
        """
        return self.board[0][column] is not None

    def get_next_row(self, column: int) -> int | None:
        """Get the next available row in a column.

        Returns the row index where a piece would land if dropped in the
        specified column, or None if the column is full.

        Args:
            column: Column index (0-6)

        Returns:
            Optional[int]: Row index for the next piece, or None if column is full

        Example:
            >>> state = Connect4State.initialize()
            >>> state.get_next_row(3)
            5  # Bottom row (gravity effect)
        """
        for row in range(len(self.board) - 1, -1, -1):
            if self.board[row][column] is None:
                return row
        return None

    @field_validator("board")
    @classmethod
    def validate_board_dimensions(cls, board):
        """Validate board dimensions are 6x7.

        Args:
            board: Board to validate

        Returns:
            list[list[str | None]]: Validated board

        Raises:
            ValueError: If board dimensions are invalid
        """
        if len(board) != 6:
            raise ValueError("Board must have 6 rows")
        if any(len(row) != 7 for row in board):
            raise ValueError("Each row must have 7 columns")
        return board

    @classmethod
    def initialize(cls):
        """Initialize a new Connect4 game.

        Creates a new Connect4 game state with an empty board,
        red player starting, and game status set to ongoing.

        Returns:
            Connect4State: A new game state

        Example:
            >>> state = Connect4State.initialize()
            >>> state.turn
            'red'
            >>> state.game_status
            'ongoing'
        """
        board = [[None for _ in range(7)] for _ in range(6)]
        return cls(board=board, turn="red", game_status="ongoing", move_history=[])
