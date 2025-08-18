games.chess.state_manager
=========================

.. py:module:: games.chess.state_manager

Chess game state management module.

This module provides comprehensive state management functionality for chess games,
including game initialization, move validation, position tracking, and game status
management using the standard chess library.

Chess is a strategic board game played on an 8×8 checkered board between two players.
Each player begins with 16 pieces: one king, one queen, two rooks, two bishops,
two knights, and eight pawns. The objective is to checkmate the opponent's king.

Classes:
    ChessGameStateManager: Main state management class for chess game operations.

.. rubric:: Example

Basic chess game setup and play:

    >>> from haive.games.chess.state_manager import ChessGameStateManager
    >>>
    >>> # Initialize game in starting position
    >>> state = ChessGameStateManager.initialize()
    >>> print(f"Starting position: {state.board_fen}")
    >>> print(f"Current turn: {state.turn}")  # "white"
    >>>
    >>> # Apply opening moves
    >>> state = ChessGameStateManager.apply_move(state, "e2e4")  # King's pawn
    >>> print(f"After e2e4, turn: {state.turn}")  # "black"
    >>>
    >>> state = ChessGameStateManager.apply_move(state, "e7e5")  # Mirror move
    >>> print(f"Move history: {state.move_history}")

.. note::

   - Moves must be in UCI notation (e.g., "e2e4", "Ng1f3")
   - The chess library handles all rule validation and special moves
   - Game states include full FEN position, move history, and captured pieces
   - This module has known issues with the apply_move method accessing analysis fields

.. warning::

   The apply_move method currently has a bug when trying to access state.analysis
   instead of the correct state.white_analysis/state.black_analysis fields.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Chess game state management module.

   This module provides comprehensive state management functionality for chess games,
   including game initialization, move validation, position tracking, and game status
   management using the standard chess library.

   Chess is a strategic board game played on an 8×8 checkered board between two players.
   Each player begins with 16 pieces: one king, one queen, two rooks, two bishops,
   two knights, and eight pawns. The objective is to checkmate the opponent's king.

   Classes:
       ChessGameStateManager: Main state management class for chess game operations.

   .. rubric:: Example

   Basic chess game setup and play:

       >>> from haive.games.chess.state_manager import ChessGameStateManager
       >>>
       >>> # Initialize game in starting position
       >>> state = ChessGameStateManager.initialize()
       >>> print(f"Starting position: {state.board_fen}")
       >>> print(f"Current turn: {state.turn}")  # "white"
       >>>
       >>> # Apply opening moves
       >>> state = ChessGameStateManager.apply_move(state, "e2e4")  # King's pawn
       >>> print(f"After e2e4, turn: {state.turn}")  # "black"
       >>>
       >>> state = ChessGameStateManager.apply_move(state, "e7e5")  # Mirror move
       >>> print(f"Move history: {state.move_history}")

   .. note::

      - Moves must be in UCI notation (e.g., "e2e4", "Ng1f3")
      - The chess library handles all rule validation and special moves
      - Game states include full FEN position, move history, and captured pieces
      - This module has known issues with the apply_move method accessing analysis fields

   .. warning::

      The apply_move method currently has a bug when trying to access state.analysis
      instead of the correct state.white_analysis/state.black_analysis fields.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.state_manager.ChessGameStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessGameStateManager

            Chess game state manager.

            This class provides static methods for managing chess game states:
                - Game initialization with default settings
                - Move application with validation
                - Game status updates
                - Captured pieces tracking

            The manager implements a functional approach where methods take the current
            state and return a new state, rather than modifying the state in place.

            .. rubric:: Examples

            >>> state = ChessGameStateManager.initialize()
            >>> print(state.board_fen)
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

            >>> new_state = ChessGameStateManager.apply_move(state, "e2e4")
            >>> print(new_state.board_fen)
            'rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'


            .. py:method:: apply_move(state: haive.games.chess.state.ChessState, move_uci: str) -> haive.games.chess.state.ChessState
               :staticmethod:


               Apply a move to the current game state.

               Takes the current game state and a move in UCI format, validates it,
               applies it to the board, and returns a new state with updated properties.

               :param state: Current game state.
               :type state: ChessState
               :param move_uci: Move in UCI notation (e.g., "e2e4").
               :type move_uci: str

               :returns: New game state after applying the move.
               :rtype: ChessState

               :raises ValueError: If the move is not valid in the current position.

               .. note::

                  This method handles:
                  - Board position updates
                  - Captured pieces tracking
                  - Game status changes (check, checkmate, stalemate)
                  - Player turn switching

               .. rubric:: Examples

               >>> state = ChessGameStateManager.initialize()
               >>> new_state = ChessGameStateManager.apply_move(state, "e2e4")
               >>> assert new_state.turn == "black"
               >>> assert "e2e4" in new_state.move_history

               >>> # Detecting checkmate
               >>> from chess import Board
               >>> board = Board.from_epd("8/8/8/8/8/5K2/4Q3/7k w - - 0 1")
               >>> state = ChessState(board_fen=board.fen())
               >>> new_state = ChessGameStateManager.apply_move(state, "e2e1")
               >>> assert new_state.game_status == "checkmate"



            .. py:method:: initialize() -> haive.games.chess.state.ChessState
               :staticmethod:


               Initialize a new chess game state.

               Creates a fresh chess game state with standard initial position and default
               settings for all game parameters.

               :returns: A fresh game state with standard starting position.
               :rtype: ChessState

               .. rubric:: Examples

               >>> state = ChessGameStateManager.initialize()
               >>> assert state.turn == "white"
               >>> assert state.game_status == "ongoing"
               >>> assert state.board_fen.startswith("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

