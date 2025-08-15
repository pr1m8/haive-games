games.checkers.state_manager
============================

.. py:module:: games.checkers.state_manager

.. autoapi-nested-parse::

   Checkers game state management module.

   This module provides comprehensive state management functionality for the classic
   Checkers game, including board management, move validation, jump detection, and
   king promotion handling.

   Checkers is a classic strategy game played on an 8×8 board with 64 squares, using
   only the dark squares. Each player starts with 12 pieces on their side of the board.
   Regular pieces move diagonally forward, but kings can move diagonally in any direction.
   Players capture opponent pieces by jumping over them, and multiple jumps are possible.

   Classes:
       CheckersStateManager: Main state management class for checkers operations.

   .. rubric:: Example

   Basic checkers game setup and play:

       >>> from haive.games.checkers.state_manager import CheckersStateManager
       >>> from haive.games.checkers.models import CheckersMove
       >>>
       >>> # Initialize standard checkers game
       >>> state = CheckersStateManager.initialize()
       >>> print(f"Current player: {state.current_player}")  # "red"
       >>> print(f"Board size: 8x8 with {len(state.pieces)} total pieces")
       >>>
       >>> # Get legal moves (including mandatory jumps)
       >>> legal_moves = CheckersStateManager.get_legal_moves(state)
       >>> print(f"Available moves: {len(legal_moves)}")
       >>>
       >>> # Make a move
       >>> if legal_moves:
       ...     move = legal_moves[0]
       ...     new_state = CheckersStateManager.apply_move(state, move)
       ...     print(f"Move applied: {move.from_square} to {move.to_square}")

   .. note::

      - Uses standard 8×8 checkers board with 64 squares (only dark squares used)
      - Players are "red" and "black" with red moving first
      - Mandatory jump rule: if a jump is available, it must be taken
      - Kings are promoted when pieces reach the opposite end of the board
      - Multiple jumps in sequence are supported when available


   .. autolink-examples:: games.checkers.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.checkers.state_manager.CheckersStateManager


Module Contents
---------------

.. py:class:: CheckersStateManager

   Manager for checkers game state.

   This class provides static methods for managing checkers game states:
       - Game initialization with default settings
       - Legal move generation (including mandatory jumps)
       - Move application with validation
       - Analysis updates
       - Game status checks
       - King promotion handling

   The manager implements a functional approach where methods take the current
   state and return a new state, rather than modifying the state in place.

   .. attribute:: BOARD_SIZE

      Size of the checkers board (8x8)

      :type: int


   .. autolink-examples:: CheckersStateManager
      :collapse:

   .. py:method:: _create_board_string(board: list[list[int]]) -> str
      :classmethod:


      Create a string representation of the board.

      Converts the 2D grid board representation to a human-readable string
      with row and column coordinates for display and debugging.

      :param board: 2D list representing the checkers board
      :type board: list[list[int]]

      :returns: String representation of the board with coordinates
      :rtype: str

      .. rubric:: Examples

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


      .. autolink-examples:: _create_board_string
         :collapse:


   .. py:method:: _get_jump_moves(board: list[list[int]], player: str, piece_values: list[int]) -> list[haive.games.checkers.models.CheckersMove]
      :classmethod:


      Get all possible jump moves for a player.

      Finds all possible jump (capture) moves for the specified player by
      checking each piece of that player on the board.

      :param board: The current board
      :type board: list[list[int]]
      :param player: The current player ("red" or "black")
      :type player: str
      :param piece_values: Values representing the player's pieces
      :type piece_values: list[int]

      :returns: List of jump moves
      :rtype: list[CheckersMove]


      .. autolink-examples:: _get_jump_moves
         :collapse:


   .. py:method:: _get_piece_jumps(board: list[list[int]], row: int, col: int, player: str) -> list[haive.games.checkers.models.CheckersMove]
      :classmethod:


      Get all possible jumps for a single piece.

      Checks all possible jump directions for a specific piece based on
      its type (regular or king) and finds valid jumps.

      :param board: The current board
      :type board: list[list[int]]
      :param row: Row of the piece
      :type row: int
      :param col: Column of the piece
      :type col: int
      :param player: The current player
      :type player: str

      :returns: List of jump moves for this piece
      :rtype: list[CheckersMove]


      .. autolink-examples:: _get_piece_jumps
         :collapse:


   .. py:method:: _get_piece_moves(board: list[list[int]], row: int, col: int, player: str) -> list[haive.games.checkers.models.CheckersMove]
      :classmethod:


      Get all possible regular moves for a single piece.

      Checks all possible move directions for a specific piece based on
      its type (regular or king) and finds valid moves.

      :param board: The current board
      :type board: list[list[int]]
      :param row: Row of the piece
      :type row: int
      :param col: Column of the piece
      :type col: int
      :param player: The current player
      :type player: str

      :returns: List of regular moves for this piece
      :rtype: list[CheckersMove]


      .. autolink-examples:: _get_piece_moves
         :collapse:


   .. py:method:: _get_regular_moves(board: list[list[int]], player: str, piece_values: list[int]) -> list[haive.games.checkers.models.CheckersMove]
      :classmethod:


      Get all possible regular moves for a player.

      Finds all possible non-jump moves for the specified player by
      checking each piece of that player on the board.

      :param board: The current board
      :type board: list[list[int]]
      :param player: The current player
      :type player: str
      :param piece_values: Values representing the player's pieces
      :type piece_values: list[int]

      :returns: List of regular moves
      :rtype: list[CheckersMove]


      .. autolink-examples:: _get_regular_moves
         :collapse:


   .. py:method:: _index_to_notation(row: int, col: int) -> str
      :classmethod:


      Convert board indices to algebraic notation.

      Converts the zero-based row and column indices to algebraic notation
      where columns are a-h and rows are 1-8 (bottom to top).

      :param row: Row index (0-7)
      :type row: int
      :param col: Column index (0-7)
      :type col: int

      :returns: Position in algebraic notation (e.g., "a3")
      :rtype: str

      .. rubric:: Examples

      >>> CheckersStateManager._index_to_notation(0, 0)
      'a8'
      >>> CheckersStateManager._index_to_notation(7, 7)
      'h1'


      .. autolink-examples:: _index_to_notation
         :collapse:


   .. py:method:: _notation_to_index(notation: str) -> tuple[int, int]
      :classmethod:


      Convert algebraic notation to board indices.

      Converts algebraic notation (e.g., "a3") to zero-based row and column indices.

      :param notation: Position in algebraic notation (e.g., "a3")
      :type notation: str

      :returns: (row, col) indices
      :rtype: tuple[int, int]

      .. rubric:: Examples

      >>> CheckersStateManager._notation_to_index("a8")
      (0, 0)
      >>> CheckersStateManager._notation_to_index("h1")
      (7, 7)


      .. autolink-examples:: _notation_to_index
         :collapse:


   .. py:method:: apply_move(state: haive.games.checkers.state.CheckersState, move: haive.games.checkers.models.CheckersMove) -> haive.games.checkers.state.CheckersState
      :classmethod:


      Apply a move to the current game state.

      Takes a move and applies it to the current state, returning a new state.
      Handles piece movement, captures, king promotion, and game status updates.

      :param state: Current game state
      :type state: CheckersState
      :param move: Move to apply
      :type move: CheckersMove

      :returns: New game state after the move
      :rtype: CheckersState

      .. rubric:: Examples

      >>> state = CheckersStateManager.initialize()
      >>> moves = CheckersStateManager.get_legal_moves(state)
      >>> new_state = CheckersStateManager.apply_move(state, moves[0])
      >>> new_state.turn
      'black'
      >>> len(new_state.move_history)
      1


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.checkers.state.CheckersState) -> haive.games.checkers.state.CheckersState
      :classmethod:


      Check and update the game status.

      Evaluates the current game state to determine if the game is over
      and who the winner is, if any.

      Game-ending conditions include:
      - A player has no pieces left
      - A player has no legal moves

      :param state: Current game state
      :type state: CheckersState

      :returns: Updated game state with correct status
      :rtype: CheckersState


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.checkers.state.CheckersState) -> list[haive.games.checkers.models.CheckersMove]
      :classmethod:


      Get all legal moves for the current player.

      Checks for all legal moves in the current position, following checkers rules:
      - If jump moves are available, only jump moves are returned (mandatory jumps)
      - Otherwise, regular moves are returned
      - Kings can move in all diagonal directions
      - Regular pieces can only move forward (down for black, up for red)

      :param state: Current game state
      :type state: CheckersState

      :returns: List of legal moves for the current player
      :rtype: list[CheckersMove]

      .. rubric:: Examples

      >>> state = CheckersStateManager.initialize()
      >>> moves = CheckersStateManager.get_legal_moves(state)
      >>> len(moves) > 0
      True
      >>> all(move.player == "red" for move in moves)
      True


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize() -> haive.games.checkers.state.CheckersState
      :classmethod:


      Initialize a new checkers game.

      Creates a fresh checkers game state with the standard starting board
      configuration, red to move first, and initial values for all tracking fields.

      :returns: A new game state with the initial board setup.
      :rtype: CheckersState

      .. rubric:: Examples

      >>> state = CheckersStateManager.initialize()
      >>> state.turn
      'red'
      >>> state.game_status
      'ongoing'
      >>> len(state.move_history)
      0


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: update_analysis(state: haive.games.checkers.state.CheckersState, analysis: dict[str, Any], player: str) -> haive.games.checkers.state.CheckersState
      :classmethod:


      Update the state with new analysis.

      Adds new position analysis data to the state for the specified player,
      keeping only the most recent analyses.

      :param state: Current game state
      :type state: CheckersState
      :param analysis: Analysis data to add
      :type analysis: dict[str, Any]
      :param player: Player the analysis is for ("red" or "black")
      :type player: str

      :returns: Updated game state with new analysis
      :rtype: CheckersState


      .. autolink-examples:: update_analysis
         :collapse:


   .. py:attribute:: BOARD_SIZE
      :value: 8



