"""Checkers game state manager module.

This module provides state management functionality for checkers games, including:
    - Game state initialization
    - Legal move generation for regular moves and jumps
    - Move application with validation
    - Game status tracking and winner determination
    - King promotion handling
    - Position analysis updates
    - Coordinate conversion between algebraic notation and indices

The state manager offers a clean, functional interface for manipulating
checkers game states without directly modifying them.
"""

import copy
from typing import Any

from .checkers.models import CheckersMove
from .checkers.state import CheckersState


class CheckersStateManager:
    """Manager for checkers game state.

    This class provides static methods for managing checkers game states:
        - Game initialization with default settings
        - Legal move generation (including mandatory jumps)
        - Move application with validation
        - Analysis updates
        - Game status checks
        - King promotion handling

    The manager implements a functional approach where methods take the current
    state and return a new state, rather than modifying the state in place.

    Attributes:
        BOARD_SIZE (int): Size of the checkers board (8x8)
    """

    BOARD_SIZE = 8

    @classmethod
    def initialize(cls) -> CheckersState:
        """Initialize a new checkers game.

        Creates a fresh checkers game state with the standard starting board
        configuration, red to move first, and initial values for all tracking fields.

        Returns:
            CheckersState: A new game state with the initial board setup.

        Examples:
            >>> state = CheckersStateManager.initialize()
            >>> state.turn
            'red'
            >>> state.game_status
            'ongoing'
            >>> len(state.move_history)
            0
        """
        # Create initial board
        # 0 = empty, 1 = red piece, 2 = red king, 3 = black piece, 4 = black king
        board = [
            [0, 3, 0, 3, 0, 3, 0, 3],
            [3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

        # Create the board string representation
        board_string = cls._create_board_string(board)

        # Return initial state
        return CheckersState(
            board=board,
            board_string=board_string,
            turn="red",  # Red goes first
            move_history=[],
            game_status="ongoing",
            winner=None,
            red_analysis=[],
            black_analysis=[],
            captured_pieces={"red": [], "black": []},
        )

    @classmethod
    def _create_board_string(cls, board: list[list[int]]) -> str:
        r"""Create a string representation of the board.

        Converts the 2D grid board representation to a human-readable string
        with row and column coordinates for display and debugging.

        Args:
            board (list[list[int]]): 2D list representing the checkers board

        Returns:
            str: String representation of the board with coordinates

        Examples:
            >>> board = [[0, 3, 0, 0, 0, 0, 0, 0],
            ...          [0, 0, 0, 0, 0, 0, 0, 0],
            ...          [0, 0, 0, 0, 0, 0, 0, 0],
            ...          [0, 0, 0, 0, 0, 0, 0, 0],
            ...          [0, 0, 0, 0, 0, 0, 0, 0],
            ...          [0, 0, 0, 0, 0, 0, 0, 0],
            ...          [0, 0, 0, 0, 0, 0, 0, 0],
            ...          [1, 0, 0, 0, 0, 0, 0, 0]]
            >>> print(CheckersStateManager._create_board_string(board).split('\\n')[0])
            '8 | . b . . . . . .'
        """
        symbols = {
            0: ".",  # Empty square
            1: "r",  # Red piece
            2: "R",  # Red king
            3: "b",  # Black piece
            4: "B",  # Black king
        }

        rows = []
        for i in range(cls.BOARD_SIZE):
            row = " ".join(symbols[board[i][j]] for j in range(cls.BOARD_SIZE))
            rows.append(f"{8-i} | {row}")

        # Add column labels
        col_labels = "    " + " ".join("abcdefgh")
        board_str = "\n".join(rows) + "\n" + col_labels

        return board_str

    @classmethod
    def get_legal_moves(cls, state: CheckersState) -> list[CheckersMove]:
        """Get all legal moves for the current player.

        Checks for all legal moves in the current position, following checkers rules:
        - If jump moves are available, only jump moves are returned (mandatory jumps)
        - Otherwise, regular moves are returned
        - Kings can move in all diagonal directions
        - Regular pieces can only move forward (down for black, up for red)

        Args:
            state (CheckersState): Current game state

        Returns:
            list[CheckersMove]: List of legal moves for the current player

        Examples:
            >>> state = CheckersStateManager.initialize()
            >>> moves = CheckersStateManager.get_legal_moves(state)
            >>> len(moves) > 0
            True
            >>> all(move.player == "red" for move in moves)
            True
        """
        board = state.board
        current_player = state.turn

        # Determine piece values for current player
        if current_player == "red":
            piece_values = [1, 2]  # Regular and king
        else:
            piece_values = [3, 4]  # Regular and king

        # Check for jumps first (these are mandatory in most checkers variants)
        jump_moves = cls._get_jump_moves(board, current_player, piece_values)

        # If there are jump moves, they are mandatory
        if jump_moves:
            return jump_moves

        # Otherwise, get regular moves
        return cls._get_regular_moves(board, current_player, piece_values)

    @classmethod
    def _get_jump_moves(
        cls, board: list[list[int]], player: str, piece_values: list[int]
    ) -> list[CheckersMove]:
        """Get all possible jump moves for a player.

        Finds all possible jump (capture) moves for the specified player by
        checking each piece of that player on the board.

        Args:
            board (list[list[int]]): The current board
            player (str): The current player ("red" or "black")
            piece_values (list[int]): Values representing the player's pieces

        Returns:
            list[CheckersMove]: List of jump moves
        """
        jumps = []

        for row in range(cls.BOARD_SIZE):
            for col in range(cls.BOARD_SIZE):
                if board[row][col] in piece_values:
                    # Check all possible jumps from this position
                    piece_jumps = cls._get_piece_jumps(board, row, col, player)
                    jumps.extend(piece_jumps)

        return jumps

    @classmethod
    def _get_piece_jumps(
        cls, board: list[list[int]], row: int, col: int, player: str
    ) -> list[CheckersMove]:
        """Get all possible jumps for a single piece.

        Checks all possible jump directions for a specific piece based on
        its type (regular or king) and finds valid jumps.

        Args:
            board (list[list[int]]): The current board
            row (int): Row of the piece
            col (int): Column of the piece
            player (str): The current player

        Returns:
            list[CheckersMove]: List of jump moves for this piece
        """
        jumps = []
        piece = board[row][col]

        # Determine possible jump directions based on piece type
        directions = []

        # Red pieces move up the board (decreasing row)
        if piece == 1:  # Red piece
            directions = [(-2, -2), (-2, 2)]  # Up-left, up-right
        # Black pieces move down the board (increasing row)
        elif piece == 3:  # Black piece
            directions = [(2, -2), (2, 2)]  # Down-left, down-right
        # Kings can move in all directions
        elif piece in [2, 4]:  # King (either color)
            directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]

        # Check each direction for a valid jump
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the landing square is in bounds and empty
            if (
                0 <= new_row < cls.BOARD_SIZE
                and 0 <= new_col < cls.BOARD_SIZE
                and board[new_row][new_col] == 0
            ):
                # Check if there's an opponent's piece to jump over
                jumped_row, jumped_col = row + dr // 2, col + dc // 2

                # Determine opponent's piece values
                opponent_values = [3, 4] if player == "red" else [1, 2]

                if board[jumped_row][jumped_col] in opponent_values:
                    # Valid jump
                    from_pos = cls._index_to_notation(row, col)
                    to_pos = cls._index_to_notation(new_row, new_col)

                    jumps.append(
                        CheckersMove(
                            from_position=from_pos,
                            to_position=to_pos,
                            player=player,
                            is_jump=True,
                            captured_position=cls._index_to_notation(
                                jumped_row, jumped_col
                            ),
                        )
                    )

        return jumps

    @classmethod
    def _get_regular_moves(
        cls, board: list[list[int]], player: str, piece_values: list[int]
    ) -> list[CheckersMove]:
        """Get all possible regular moves for a player.

        Finds all possible non-jump moves for the specified player by
        checking each piece of that player on the board.

        Args:
            board (list[list[int]]): The current board
            player (str): The current player
            piece_values (list[int]): Values representing the player's pieces

        Returns:
            list[CheckersMove]: List of regular moves
        """
        moves = []

        for row in range(cls.BOARD_SIZE):
            for col in range(cls.BOARD_SIZE):
                if board[row][col] in piece_values:
                    # Check all possible moves from this position
                    piece_moves = cls._get_piece_moves(board, row, col, player)
                    moves.extend(piece_moves)

        return moves

    @classmethod
    def _get_piece_moves(
        cls, board: list[list[int]], row: int, col: int, player: str
    ) -> list[CheckersMove]:
        """Get all possible regular moves for a single piece.

        Checks all possible move directions for a specific piece based on
        its type (regular or king) and finds valid moves.

        Args:
            board (list[list[int]]): The current board
            row (int): Row of the piece
            col (int): Column of the piece
            player (str): The current player

        Returns:
            list[CheckersMove]: List of regular moves for this piece
        """
        moves = []
        piece = board[row][col]

        # Determine possible move directions based on piece type
        directions = []

        # Red pieces move up the board (decreasing row)
        if piece == 1:  # Red piece
            directions = [(-1, -1), (-1, 1)]  # Up-left, up-right
        # Black pieces move down the board (increasing row)
        elif piece == 3:  # Black piece
            directions = [(1, -1), (1, 1)]  # Down-left, down-right
        # Kings can move in all directions
        elif piece in [2, 4]:  # King (either color)
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        # Check each direction for a valid move
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check if the new square is in bounds and empty
            if (
                0 <= new_row < cls.BOARD_SIZE
                and 0 <= new_col < cls.BOARD_SIZE
                and board[new_row][new_col] == 0
            ):
                # Valid move
                from_pos = cls._index_to_notation(row, col)
                to_pos = cls._index_to_notation(new_row, new_col)

                moves.append(
                    CheckersMove(
                        from_position=from_pos,
                        to_position=to_pos,
                        player=player,
                        is_jump=False,
                    )
                )

        return moves

    @classmethod
    def _index_to_notation(cls, row: int, col: int) -> str:
        """Convert board indices to algebraic notation.

        Converts the zero-based row and column indices to algebraic notation
        where columns are a-h and rows are 1-8 (bottom to top).

        Args:
            row (int): Row index (0-7)
            col (int): Column index (0-7)

        Returns:
            str: Position in algebraic notation (e.g., "a3")

        Examples:
            >>> CheckersStateManager._index_to_notation(0, 0)
            'a8'
            >>> CheckersStateManager._index_to_notation(7, 7)
            'h1'
        """
        return f"{chr(97 + col)}{8 - row}"

    @classmethod
    def _notation_to_index(cls, notation: str) -> tuple[int, int]:
        """Convert algebraic notation to board indices.

        Converts algebraic notation (e.g., "a3") to zero-based row and column indices.

        Args:
            notation (str): Position in algebraic notation (e.g., "a3")

        Returns:
            tuple[int, int]: (row, col) indices

        Examples:
            >>> CheckersStateManager._notation_to_index("a8")
            (0, 0)
            >>> CheckersStateManager._notation_to_index("h1")
            (7, 7)
        """
        col = ord(notation[0]) - 97
        row = 8 - int(notation[1])
        return row, col

    @classmethod
    def apply_move(cls, state: CheckersState, move: CheckersMove) -> CheckersState:
        """Apply a move to the current game state.

        Takes a move and applies it to the current state, returning a new state.
        Handles piece movement, captures, king promotion, and game status updates.

        Args:
            state (CheckersState): Current game state
            move (CheckersMove): Move to apply

        Returns:
            CheckersState: New game state after the move

        Examples:
            >>> state = CheckersStateManager.initialize()
            >>> moves = CheckersStateManager.get_legal_moves(state)
            >>> new_state = CheckersStateManager.apply_move(state, moves[0])
            >>> new_state.turn
            'black'
            >>> len(new_state.move_history)
            1
        """
        # Create a deep copy of the state to avoid modifying the original
        new_state = copy.deepcopy(state)

        # Convert positions to indices
        from_row, from_col = cls._notation_to_index(move.from_position)
        to_row, to_col = cls._notation_to_index(move.to_position)

        # Get the piece being moved
        piece = new_state.board[from_row][from_col]

        # Update the board
        new_state.board[to_row][to_col] = piece
        new_state.board[from_row][from_col] = 0

        # Check for king promotion
        if (piece == 1 and to_row == 0) or (piece == 3 and to_row == 7):
            # Promote to king
            new_state.board[to_row][to_col] = 2 if piece == 1 else 4

        # Handle jump and captured piece
        captured_pieces = list(new_state.captured_pieces.get(move.player, []))

        if move.is_jump and move.captured_position:
            captured_row, captured_col = cls._notation_to_index(move.captured_position)
            captured_piece = new_state.board[captured_row][captured_col]

            # Record the captured piece
            if captured_piece in [1, 2]:  # Red piece or king
                captured_pieces.append("red" + ("_king" if captured_piece == 2 else ""))
            else:  # Black piece or king
                captured_pieces.append(
                    "black" + ("_king" if captured_piece == 4 else "")
                )

            # Remove the captured piece from the board
            new_state.board[captured_row][captured_col] = 0

        # Update captured pieces
        new_state.captured_pieces[move.player] = captured_pieces

        # Update move history
        new_state.move_history.append(move)

        # Update turn
        new_state.turn = "black" if move.player == "red" else "red"

        # Update board string
        new_state.board_string = cls._create_board_string(new_state.board)

        # Check game status (win, draw, etc.)
        new_state = cls.check_game_status(new_state)

        return new_state

    @classmethod
    def check_game_status(cls, state: CheckersState) -> CheckersState:
        """Check and update the game status.

        Evaluates the current game state to determine if the game is over
        and who the winner is, if any.

        Game-ending conditions include:
        - A player has no pieces left
        - A player has no legal moves

        Args:
            state (CheckersState): Current game state

        Returns:
            CheckersState: Updated game state with correct status
        """
        # Create a deep copy to avoid modifying the original
        new_state = copy.deepcopy(state)

        # Count pieces
        red_pieces = sum(row.count(1) + row.count(2) for row in new_state.board)
        black_pieces = sum(row.count(3) + row.count(4) for row in new_state.board)

        # Check for win by capturing all pieces
        if red_pieces == 0:
            new_state.game_status = "game_over"
            new_state.winner = "black"
            return new_state

        if black_pieces == 0:
            new_state.game_status = "game_over"
            new_state.winner = "red"
            return new_state

        # Check if current player has any legal moves
        legal_moves = cls.get_legal_moves(new_state)

        if not legal_moves:
            # No legal moves means the current player loses
            new_state.game_status = "game_over"
            new_state.winner = "red" if new_state.turn == "black" else "black"

        return new_state

    @classmethod
    def update_analysis(
        cls, state: CheckersState, analysis: dict[str, Any], player: str
    ) -> CheckersState:
        """Update the state with new analysis.

        Adds new position analysis data to the state for the specified player,
        keeping only the most recent analyses.

        Args:
            state (CheckersState): Current game state
            analysis (dict[str, Any]): Analysis data to add
            player (str): Player the analysis is for ("red" or "black")

        Returns:
            CheckersState: Updated game state with new analysis
        """
        # Create a deep copy to avoid modifying the original
        new_state = copy.deepcopy(state)

        # Add the analysis to the appropriate list
        if player == "red":
            new_state.red_analysis.append(analysis)
            # Keep only the last 5 analyses
            new_state.red_analysis = new_state.red_analysis[-5:]
        else:
            new_state.black_analysis.append(analysis)
            # Keep only the last 5 analyses
            new_state.black_analysis = new_state.black_analysis[-5:]

        return new_state
