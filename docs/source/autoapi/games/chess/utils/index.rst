games.chess.utils
=================

.. py:module:: games.chess.utils

.. autoapi-nested-parse::

   Chess game utility functions.

   This module provides helper functions for the chess game, including:
       - Game status determination
       - Board visualization
       - Move validation

   These utilities support the core functionality of the chess module
   by providing common operations used across different components.



Functions
---------

.. autoapisummary::

   games.chess.utils.determine_game_status
   games.chess.utils.generate_ascii_board
   games.chess.utils.validate_move


Module Contents
---------------

.. py:function:: determine_game_status(board: chess.Board) -> str

   Determine the current game status based on the board position.

   Analyzes a chess board to determine its current status (checkmate,
   stalemate, check, etc.) based on the rules of chess.

   :param board: Chess board to analyze
   :type board: chess.Board

   :returns:

             Game status as one of: "checkmate", "stalemate", "draw",
                 "check", or "ongoing"
   :rtype: str

   .. rubric:: Examples

   >>> board = chess.Board()
   >>> determine_game_status(board)
   'ongoing'

   >>> # Fool's mate position
   >>> board = chess.Board("rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 2")
   >>> board.push_san("Qh4#")
   >>> determine_game_status(board)
   'checkmate'


.. py:function:: generate_ascii_board(fen: str, last_move: str | None = None) -> str

   Generate an ASCII representation of the chess board.

   Creates a text-based visualization of a chess board from its FEN
   representation, optionally highlighting the last move made.

   :param fen: FEN string representation of the board
   :type fen: str
   :param last_move: Last move in UCI notation (e.g., "e2e4")
                     to highlight on the board. Defaults to None.
   :type last_move: str | None, optional

   :returns:

             ASCII representation of the board with coordinates and
                 optional move highlighting
   :rtype: str

   .. rubric:: Examples

   >>> # Starting position
   >>> board_ascii = generate_ascii_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
   >>> print(board_ascii.split("\\n")[0])
   '8 r n b q k b n r'

   >>> # With last move highlighted
   >>> board_ascii = generate_ascii_board(
   ...     "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",
   ...     "e2e4"
   ... )


.. py:function:: validate_move(fen: str, move_uci: str) -> tuple[bool, str | None, str | None]

   Validate a chess move and return the resulting position.

   Checks if a move is valid in the given position and returns validation
   results including error messages and the resulting position if valid.

   :param fen: FEN string of the current position
   :type fen: str
   :param move_uci: Move in UCI notation (e.g., "e2e4")
   :type move_uci: str

   :returns:

             A tuple containing:
                 - is_valid (bool): Whether the move is legal
                 - error_message (str | None): Error message if move is invalid, None otherwise
                 - resulting_fen (str | None): FEN of the position after the move if valid, None otherwise
   :rtype: tuple[bool, str | None, str | None]

   .. rubric:: Examples

   >>> # Valid move
   >>> is_valid, error, new_fen = validate_move(
   ...     "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
   ...     "e2e4"
   ... )
   >>> is_valid
   True
   >>> error is None
   True
   >>> new_fen.startswith("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR")
   True

   >>> # Invalid move
   >>> is_valid, error, new_fen = validate_move(
   ...     "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
   ...     "e2e5"
   ... )
   >>> is_valid
   False
   >>> "not legal" in error
   True
   >>> new_fen is None
   True


