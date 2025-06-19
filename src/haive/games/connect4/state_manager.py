"""Connect4 state manager module.

This module provides the state manager for Connect4 games, handling:
    - Game initialization
    - Move application
    - Win condition checking
    - Game state validation and conversion

Example:
    >>> from haive.games.connect4.state_manager import Connect4StateManager
    >>> from haive.games.connect4.models import Connect4Move
    >>>
    >>> # Initialize a new game
    >>> state = Connect4StateManager.initialize()
    >>>
    >>> # Apply a move
    >>> move = Connect4Move(column=3)
    >>> new_state = Connect4StateManager.apply_move(state, move)
"""

import copy
from typing import Any, Dict, Union

from haive.games.connect4.models import Connect4Move
from haive.games.connect4.state import Connect4State
from haive.games.framework.base.state_manager import GameStateManager


class Connect4StateManager(GameStateManager[Connect4State]):
    """Manager for Connect4 game state.

    This class provides methods for managing Connect4 game state, including:
        - Game initialization
        - Move application and validation
        - Win condition checking
        - Game state conversion

    The state manager follows the immutable state pattern, creating
    new state instances rather than modifying existing ones.
    """

    @classmethod
    def initialize(cls) -> Connect4State:
        """Initialize a new Connect4 game.

        Creates a fresh Connect4 game state with an empty board,
        red player starting, and game status set to ongoing.

        Returns:
            Connect4State: A new game state with default settings

        Example:
            >>> state = Connect4StateManager.initialize()
            >>> state.turn
            'red'
            >>> state.game_status
            'ongoing'
        """
        board = [[None for _ in range(7)] for _ in range(6)]
        return Connect4State(
            board=board, turn="red", game_status="ongoing", move_history=[]
        )

    @classmethod
    def apply_move(cls, state: Connect4State, move: Connect4Move) -> Connect4State:
        """Apply a move to the Connect4 state.

        Applies the given move to the game state, updating the board,
        checking win conditions, and switching turns as appropriate.

        Args:
            state: Current game state
            move: Move to apply

        Returns:
            Connect4State: Updated game state after applying the move

        Raises:
            ValueError: If the move is invalid (column full or out of range)

        Example:
            >>> state = Connect4StateManager.initialize()
            >>> move = Connect4Move(column=3)
            >>> new_state = Connect4StateManager.apply_move(state, move)
            >>> new_state.turn
            'yellow'
        """
        new_state = copy.deepcopy(state)
        board = new_state.board
        column = move.column

        # Validate column
        if not (0 <= column < 7):
            raise ValueError(f"Column {column} is out of range (0-6)")

        # Find next available row
        row = new_state.get_next_row(column)
        if row is None:
            raise ValueError(f"Column {column} is full")

        # Place piece
        board[row][column] = new_state.turn
        new_state.move_history.append(move)

        # Check win condition
        if cls._check_win(new_state, row, column):
            new_state.game_status = f"{new_state.turn}_win"
            new_state.winner = new_state.turn
        elif all(cell is not None for row in board for cell in row):
            new_state.game_status = "draw"
        else:
            new_state.turn = "yellow" if new_state.turn == "red" else "red"

        return new_state

    @classmethod
    def get_legal_moves(cls, state: Connect4State) -> list[Connect4Move]:
        """Get all legal moves for the current game state.

        Returns a list of all valid moves (non-full columns) for the current player.

        Args:
            state: Current game state

        Returns:
            list[Connect4Move]: List of legal moves

        Example:
            >>> state = Connect4StateManager.initialize()
            >>> legal_moves = Connect4StateManager.get_legal_moves(state)
            >>> len(legal_moves)
            7  # All columns are empty in a new game
        """
        return [
            Connect4Move(column=col)
            for col in range(7)
            if not state.is_column_full(col)
        ]

    @classmethod
    def check_game_over(cls, state: Connect4State) -> bool:
        """Check if the game is over (win or draw).

        Args:
            state: Current game state

        Returns:
            bool: True if the game is over, False otherwise

        Example:
            >>> state = Connect4StateManager.initialize()
            >>> Connect4StateManager.check_game_over(state)
            False
        """
        return state.game_status in ["red_win", "yellow_win", "draw"]

    @classmethod
    def ensure_state(cls, state: Union[Dict[str, Any], Connect4State]) -> Connect4State:
        """Ensure the input is a proper Connect4State object.

        Args:
            state: State object or dictionary

        Returns:
            Connect4State: Properly typed state object

        Example:
            >>> state_dict = {"board": [[None for _ in range(7)] for _ in range(6)],
            ...               "turn": "red", "game_status": "ongoing"}
            >>> state = Connect4StateManager.ensure_state(state_dict)
            >>> isinstance(state, Connect4State)
            True
        """
        if isinstance(state, dict):
            return Connect4State(**state)
        return state

    @classmethod
    def _check_win(cls, state: Connect4State, row: int, col: int) -> bool:
        """Check if there's a win at the specified position.

        Checks for four in a row horizontally, vertically, and diagonally
        after a piece is placed at the specified position.

        Args:
            state: Current game state
            row: Row index where the piece was placed
            col: Column index where the piece was placed

        Returns:
            bool: True if there's a win, False otherwise
        """
        player = state.turn
        board = state.board

        # Check horizontal
        for c in range(max(0, col - 3), min(4, col + 1)):
            if all(board[row][c + i] == player for i in range(4)):
                return True

        # Check vertical
        if row <= 2:  # Only check if there are enough rows below
            if all(board[row + i][col] == player for i in range(4)):
                return True

        # Check diagonal /
        for offset in range(-3, 1):
            if 0 <= row + offset <= 2 and 0 <= col + offset <= 3:
                if all(
                    board[row + offset + i][col + offset + i] == player
                    for i in range(4)
                ):
                    return True

        # Check diagonal \
        for offset in range(-3, 1):
            if 0 <= row + offset <= 2 and 3 <= col - offset <= 6:
                if all(
                    board[row + offset + i][col - offset - i] == player
                    for i in range(4)
                ):
                    return True

        return False
