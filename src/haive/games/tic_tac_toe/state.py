"""Comprehensive state management system for strategic Tic Tac Toe gameplay.

from typing import Any
This module provides sophisticated state management for Tic Tac Toe games with
complete support for game mechanics, strategic analysis, and LangGraph integration.
The state system maintains game rules, move validation, and comprehensive game
history for educational and competitive gameplay.

The state system supports:
- Complete 3x3 board representation with move validation
- Turn-based gameplay with X and O player management
- Move history tracking for game replay and analysis
- Strategic analysis integration for both players
- Win condition detection (rows, columns, diagonals)
- Draw detection and game status management
- LangGraph reducers for concurrent state updates
- Error handling and recovery mechanisms

Examples:
    Initializing a new game::

        state = TicTacToeState.initialize(
            first_player="X",
            player_X="player1",
            player_O="player2"
        )

    Making a move and checking status::

        # Make a center move
        state.board[1][1] = "X"
        state.move_history.append(
            TicTacToeMove(row=1, col=1, player="X")
        )

        # Check game state
        if state.is_board_full:
            state.game_status = "draw"

    Analyzing board positions::

        empty_cells = state.empty_cells
        print(f"Available moves: {empty_cells}")

        # Pretty print the board
        print(state.board_string)

    Managing player turns::

        current = state.current_player_name
        if state.turn == "X":
            state.turn = "O"
        else:
            state.turn = "X"

Note:
    All state updates should use LangGraph Commands to ensure proper
    reducer behavior and concurrent update handling.

"""

from typing import Annotated, Any, Literal

from pydantic import Field, field_validator

from haive.games.framework.base.state import GameState
from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove


def replace_reducer(left: Any, right: Any) -> Any:
    """Reducer that always takes the new value (right side).

    This reducer is used for fields that should be completely replaced
    on update rather than merged or concatenated.

    Args:
        left (Any): Existing value in the state.
        right (Any): New value to replace with.

    Returns:
        Any: The new value (right side).

    Examples:
        >>> replace_reducer("X", "O")
        'O'
        >>> replace_reducer([1, 2], [3, 4])
        [3, 4]

    """
    return right


def add_messages_reducer(left: list, right: list) -> list:
    """Reducer for message-like lists that should be concatenated.

    This reducer is used for accumulating lists like move history
    and analysis results, preserving all historical data.

    Args:
        left (list): Existing list in the state.
        right (list): New items to append.

    Returns:
        list: Concatenated list with all items.

    Examples:
        >>> add_messages_reducer([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> add_messages_reducer([], [1, 2])
        [1, 2]

    """
    if not isinstance(left, list):
        left = []
    if not isinstance(right, list):
        right = []
    return left + right


def replace_board_reducer(left: Any, right: Any) -> Any:
    """Special reducer for the board that always replaces with the new board.

    This ensures the board state is always consistent and prevents
    partial updates that could create invalid game states.

    Args:
        left (Any): Existing board state.
        right (Any): New board state.

    Returns:
        Any: The new board state.

    """
    return right


class TicTacToeState(GameState):
    """Comprehensive state model for Tic Tac Toe gameplay with LangGraph integration.

    This class provides complete state management for Tic Tac Toe games, supporting
    both traditional gameplay mechanics and advanced features for AI analysis. The
    state system maintains game rules, validates moves, tracks history, and integrates
    with LangGraph for distributed gameplay and concurrent updates.

    The state model supports:
    - 3x3 board representation with None/X/O values
    - Turn management with alternating X and O players
    - Move history for game replay and analysis
    - Player-specific analysis storage
    - Win/draw detection and game status tracking
    - Error handling for invalid moves
    - LangGraph reducers for proper state updates
    - Pretty-printing for board visualization

    All fields use explicit reducers to ensure proper behavior with LangGraph's
    concurrent update system, preventing state corruption during parallel operations.

    Attributes:
        players (List[str]): Player identifiers with accumulating reducer.
        board (List[List[Optional[str]]]): 3x3 game board with replace reducer.
        turn (Literal["X", "O"]): Current player's turn with replace reducer.
        game_status (Literal): Game state (ongoing/X_win/O_win/draw) with replace reducer.
        move_history (List[TicTacToeMove]): Complete move history with accumulating reducer.
        error_message (Optional[str]): Error state with replace reducer.
        winner (Optional[str]): Winner identifier with replace reducer.
        player_X (Literal): Player using X symbol with replace reducer.
        player_O (Literal): Player using O symbol with replace reducer.
        player1_analysis (List[TicTacToeAnalysis]): Player 1's analyses with accumulating reducer.
        player2_analysis (List[TicTacToeAnalysis]): Player 2's analyses with accumulating reducer.

    Examples:
        Creating and initializing a game::

            state = TicTacToeState.initialize(
                first_player="X",
                player_X="Alice",
                player_O="Bob"
            )
            assert state.turn == "X"
            assert state.game_status == "ongoing"
            assert all(cell is None for row in state.board for cell in row)

        Making moves and updating state::

            # X plays center
            state.board[1][1] = "X"
            state.move_history.append(
                TicTacToeMove(row=1, col=1, player="X")
            )
            state.turn = "O"

            # O plays corner
            state.board[0][0] = "O"
            state.move_history.append(
                TicTacToeMove(row=0, col=0, player="O")
            )
            state.turn = "X"

        Checking win conditions::

            # X wins with diagonal
            state.board = [
                ["X", "O", None],
                ["O", "X", None],
                [None, None, "X"]
            ]
            state.game_status = "X_win"
            state.winner = "player1"

        Board visualization::

            print(state.board_string)
            # Output:
            #    0 1 2
            #   -------
            # 0 |X|O| |
            #   -------
            # 1 |O|X| |
            #   -------
            # 2 | | |X|
            #   -------

    Note:
        State updates should be performed through LangGraph Commands to ensure
        proper reducer behavior and prevent concurrent update conflicts.

    """

    @staticmethod
    def _default_players() -> list[str]:
        """Create default player list for a two-player game.

        Returns:
            list[str]: Default player identifiers ["player1", "player2"].

        """
        return ["player1", "player2"]

    @staticmethod
    def _default_board() -> list[list[str | None]]:
        """Create default empty 3x3 board for a new game.

        Returns:
            list[list[str | None]]: 3x3 grid with all cells set to None.

        Examples:
            >>> board = TicTacToeState._default_board()
            >>> len(board)
            3
            >>> all(len(row) == 3 for row in board)
            True
            >>> all(cell is None for row in board for cell in row)
            True

        """
        return [[None for _ in range(3)] for _ in range(3)]

    # Player management - this can accumulate
    players: Annotated[list[str], add_messages_reducer] = Field(
        default_factory=_default_players,
        description="List of player identifiers participating in the game",
        examples=[["player1", "player2"], ["Alice", "Bob"], ["Human", "AI"]],
    )

    # Game board - always replace with new board
    board: Annotated[list[list[str | None]], replace_board_reducer] = Field(
        default_factory=_default_board,
        description="3x3 game board where each cell contains None (empty), 'X', or 'O'",
        examples=[
            [[None, None, None], [None, "X", None], [None, None, None]],
            [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]],
        ],
    )

    # Game state fields - always replace with new value
    turn: Annotated[Literal["X", "O"], replace_reducer] = Field(
        default="X",
        description="Symbol of the player whose turn it is to move",
        examples=["X", "O"],
    )

    game_status: Annotated[
        Literal["ongoing", "X_win", "O_win", "draw"], replace_reducer
    ] = Field(
        default="ongoing",
        description="Current game status indicating if game is active or complete",
        examples=["ongoing", "X_win", "O_win", "draw"],
    )

    # Move history - accumulate moves
    move_history: Annotated[list[TicTacToeMove], add_messages_reducer] = Field(
        default_factory=list,
        description="Chronological history of all moves made during the game",
        examples=[
            [TicTacToeMove(row=1, col=1, player="X")],
            [
                TicTacToeMove(row=0, col=0, player="X"),
                TicTacToeMove(row=1, col=1, player="O"),
            ],
        ],
    )

    # Error handling - replace with new error
    error_message: Annotated[str | None, replace_reducer] = Field(
        default=None,
        description="Error message for invalid moves or game state issues",
        examples=[None, "Invalid move: cell already occupied", "Game is already over"],
    )

    # Winner - replace with new value
    winner: Annotated[str | None, replace_reducer] = Field(
        default=None,
        description="Player identifier of the winner when game ends",
        examples=[None, "player1", "player2", "Alice"],
    )

    # Player assignment - replace with new values
    player_X: Annotated[Literal["player1", "player2"], replace_reducer] = Field(
        default="player1",
        description="Player identifier assigned to use the X symbol",
        examples=["player1", "player2"],
    )

    player_O: Annotated[Literal["player1", "player2"], replace_reducer] = Field(
        default="player2",
        description="Player identifier assigned to use the O symbol",
        examples=["player1", "player2"],
    )

    # Analysis storage - accumulate analyses
    player1_analysis: Annotated[list[TicTacToeAnalysis], add_messages_reducer] = Field(
        default_factory=list,
        description="Strategic analyses performed by player1 during the game",
    )

    player2_analysis: Annotated[list[TicTacToeAnalysis], add_messages_reducer] = Field(
        default_factory=list,
        description="Strategic analyses performed by player2 during the game",
    )

    @field_validator("board")
    @classmethod
    def validate_board(cls, board) -> Any:
        """Validate that the board is a proper 3x3 grid with valid symbols.

        Ensures the board maintains the correct structure and contains only
        valid values (None for empty, 'X', or 'O' for occupied cells).

        Args:
            board (List[List[Optional[str]]]): The board to validate.

        Returns:
            List[List[Optional[str]]]: Validated board or default empty board.

        Raises:
            ValueError: If the board structure is invalid or contains invalid values.

        Examples:
            Valid board::

                board = [["X", None, "O"], [None, "X", None], ["O", None, "X"]]
                # Passes validation

            Invalid board (wrong size)::

                board = [["X", "O"], ["O", "X"]]  # 2x2 instead of 3x3
                # Raises ValueError: "Board must have 3 rows"

            Invalid board (invalid symbol)::

                board = [["X", "Y", "O"], [None, None, None], [None, None, None]]
                # Raises ValueError: "Cell values must be None, 'X', or 'O', got Y"

        """
        # If board is empty, initialize a proper 3x3 board
        if not board or len(board) == 0:
            return [[None for _ in range(3)] for _ in range(3)]

        if len(board) != 3:
            raise ValueError("Board must have 3 rows")

        for i, row in enumerate(board):
            if len(row) != 3:
                raise ValueError(f"Row {i} must have 3 columns, got {len(row)}")
            for j, cell in enumerate(row):
                if cell is not None and cell not in ["X", "O"]:
                    raise ValueError(
                        f"Cell at ({i}, {j}) has invalid value: '{cell}'. "
                        f"Must be None, 'X', or 'O'"
                    )
        return board

    @property
    def empty_cells(self) -> list[tuple[int, int]]:
        """Return a list of coordinates for all empty cells on the board.

        Useful for determining available moves and checking if the game can continue.

        Returns:
            list[tuple[int, int]]: List of (row, col) tuples for empty cells.

        Examples:
            >>> state = TicTacToeState.initialize()
            >>> state.empty_cells
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

            >>> state.board[1][1] = "X"
            >>> len(state.empty_cells)
            8

        """
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] is None]

    @property
    def is_board_full(self) -> bool:
        """Check whether the board is completely filled with no empty cells.

        Used to detect draw conditions when no player has won.

        Returns:
            bool: True if all cells are occupied, False otherwise.

        Examples:
            >>> state = TicTacToeState.initialize()
            >>> state.is_board_full
            False

            >>> # Fill the board
            >>> state.board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]
            >>> state.is_board_full
            True

        """
        return all(self.board[i][j] is not None for i in range(3) for j in range(3))

    @property
    def current_player_name(self) -> str:
        """Get the identifier of the player whose turn it is.

        Maps the current turn symbol (X or O) to the assigned player identifier.

        Returns:
            str: The player identifier ("player1" or "player2").

        Examples:
            >>> state = TicTacToeState.initialize()
            >>> state.turn = "X"
            >>> state.current_player_name
            'player1'

            >>> state.turn = "O"
            >>> state.current_player_name
            'player2'

        """
        return self.player_X if self.turn == "X" else self.player_O

    @property
    def board_string(self) -> str:
        """Get a pretty-printed string representation of the board.

        Creates a human-readable ASCII representation of the current board state
        with row and column indices for easy reference.

        Returns:
            str: Multiline string representing the current board state.

        Examples:
            Empty board::

                   0 1 2
                  -------
                0 | | | |
                  -------
                1 | | | |
                  -------
                2 | | | |
                  -------

            Game in progress::

                   0 1 2
                  -------
                0 |X|O| |
                  -------
                1 | |X| |
                  -------
                2 |O| |X|
                  -------

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
    def initialize(cls, **kwargs) -> "TicTacToeState":
        """Initialize a new Tic Tac Toe game with optional configuration.

        Factory method to create a properly initialized game state with all
        required fields set to appropriate starting values.

        Args:
            **kwargs: Optional configuration parameters:
                first_player (Literal["X", "O"]): Which player goes first (default: "X").
                player_X (Literal["player1", "player2"]): Player using X (default: "player1").
                player_O (Literal["player1", "player2"]): Player using O (default: "player2").

        Returns:
            TicTacToeState: Newly initialized game state ready for play.

        Examples:
            Default initialization::

                state = TicTacToeState.initialize()
                assert state.turn == "X"
                assert state.player_X == "player1"
                assert state.player_O == "player2"

            Custom player assignment::

                state = TicTacToeState.initialize(
                    first_player="O",
                    player_X="player2",
                    player_O="player1"
                )
                assert state.turn == "O"
                assert state.current_player_name == "player1"

            Tournament setup::

                state = TicTacToeState.initialize(
                    first_player="X",
                    player_X="player1",
                    player_O="player2"
                )
                # Ready for competitive play

        """
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
