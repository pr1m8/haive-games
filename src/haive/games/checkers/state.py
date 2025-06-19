"""Checkers game state module.

This module defines the state schema for checkers games, including:
    - Board representation as a 2D grid
    - String-based board visualization
    - Game turn tracking
    - Move history
    - Game status and winner tracking
    - Position analysis storage
    - Captured pieces tracking

The state schema provides a complete representation of a checkers game state
that can be used by the agent and state manager.
"""

from typing import ClassVar, Dict, List, Literal, Sequence

from pydantic import BaseModel, Field

from haive.games.checkers.models import CheckersAnalysis, CheckersMove


class CheckersState(BaseModel):
    """State schema for the checkers game.

    A comprehensive representation of a checkers game state, including the board,
    turn tracking, move history, game status, analysis data, and more.

    The board is represented as a 2D grid of integers, where:
    - 0: Empty square
    - 1: Red piece
    - 2: Red king
    - 3: Black piece
    - 4: Black king

    Attributes:
        board (List[List[Literal[0, 1, 2, 3, 4]]]): 2D grid representation of the board
        board_string (str): String representation of the board for display
        turn (Literal["red", "black"]): Current player's turn
        move_history (Sequence[CheckersMove]): History of moves made
        game_status (Literal["ongoing", "game_over"]): Current game status
        winner (Literal["red", "black"] | None): Winner of the game, if any
        red_analysis (Sequence[CheckersAnalysis]): Position analysis from red's perspective
        black_analysis (Sequence[CheckersAnalysis]): Position analysis from black's perspective
        captured_pieces (Dict[str, List[str]]): Pieces captured by each player

    Examples:
        >>> # Create a new checkers state with default board
        >>> state = CheckersState()
        >>> state.turn
        'red'
        >>> state.game_status
        'ongoing'

        >>> # Access the board
        >>> state.board[0][1]  # Position a2, black piece
        3

        >>> # Initialize a new game
        >>> new_game = CheckersState.initialize()
    """

    board: List[List[Literal[0, 1, 2, 3, 4]]] = Field(
        default_factory=lambda: CheckersState._default_board(),
        description="2D grid representation of the board",
    )
    # symbols = {0: ".", 1: "r", 2: "R", 3: "b", 4: "B"}
    board_string: str = Field(
        default_factory=lambda: CheckersState._create_board_string(
            CheckersState._default_board()
        ),
        description="String representation of the board",
    )
    turn: Literal["red", "black"] = Field(
        default="red", description="Current player's turn"
    )
    move_history: Sequence[CheckersMove] = Field(
        default_factory=list, description="History of moves made"
    )
    game_status: Literal["ongoing", "game_over"] = Field(
        default="ongoing", description="Current game status"
    )
    winner: Literal["red", "black"] | None = Field(
        default=None, description="Winner of the game, if any"
    )
    red_analysis: Sequence[CheckersAnalysis] = Field(
        default_factory=list, description="Position analysis from red's perspective"
    )
    black_analysis: Sequence[CheckersAnalysis] = Field(
        default_factory=list, description="Position analysis from black's perspective"
    )
    captured_pieces: Dict[str, List[str]] = Field(
        default_factory=lambda: {"red": [], "black": []},
        description="Pieces captured by each player",
    )

    __board_size: ClassVar[int] = 8
    __symbols: ClassVar[Dict[int, str]] = {0: ".", 1: "r", 2: "R", 3: "b", 4: "B"}

    @classmethod
    def _default_board(cls) -> list[list[int]]:
        """Create the default starting board for checkers.

        Creates an 8x8 checkers board with the standard starting positions:
        - Black pieces on top three rows
        - Red pieces on bottom three rows
        - Empty middle rows

        Returns:
            list[list[int]]: 2D grid representation of the default board

        Note:
            The board uses these values:
            - 0: Empty square
            - 1: Red piece
            - 2: Red king
            - 3: Black piece
            - 4: Black king
        """
        return [
            [0, 3, 0, 3, 0, 3, 0, 3],
            [3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

    @classmethod
    def _create_board_string(cls, board: list[list[int]]) -> str:
        """Create a string representation of the board for display.

        Converts the 2D grid representation to a human-readable string with
        row and column coordinates.

        Args:
            board (list[list[int]]): 2D grid representation of the board

        Returns:
            str: String representation of the board with coordinates

        Example:
            >>> board = CheckersState._default_board()
            >>> print(CheckersState._create_board_string(board))
            8 | . b . b . b . b
            7 | b . b . b . b .
            6 | . b . b . b . b
            5 | . . . . . . . .
            4 | . . . . . . . .
            3 | r . r . r . r .
            2 | . r . r . r . r
            1 | r . r . r . r .
                a b c d e f g h
        """
        rows = [
            f"{cls.__board_size - i} | "
            + " ".join(cls._get_symbol(cell) for cell in row)
            for i, row in enumerate(board)
        ]
        col_labels = "    " + " ".join("abcdefgh")
        return "\n".join(rows) + "\n" + col_labels

    @classmethod
    def _get_symbol(cls, cell: int) -> str:
        """Get the symbol for a cell value.

        Converts the numeric cell value to its corresponding symbol:
        - 0: "." (empty)
        - 1: "r" (red piece)
        - 2: "R" (red king)
        - 3: "b" (black piece)
        - 4: "B" (black king)

        Args:
            cell (int): Cell value (0-4)

        Returns:
            str: Symbol representing the cell
        """
        return cls.__symbols[cell]

    @classmethod
    def initialize(cls) -> "CheckersState":
        """Initialize a new checkers game state.

        Creates a fresh checkers state with the standard starting board,
        red to move first, and default values for all other fields.

        Returns:
            CheckersState: A new game state ready to play

        Example:
            >>> state = CheckersState.initialize()
            >>> state.turn
            'red'
            >>> state.game_status
            'ongoing'
        """
        board = cls._default_board()
        return cls(board=board, board_string=cls._create_board_string(board))

    class Config:
        """Pydantic configuration.

        Allows arbitrary types to be used in the model.
        """

        arbitrary_types_allowed = True
