
:py:mod:`games.chess.state_manager`
===================================

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


.. autolink-examples:: games.chess.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.state_manager.ChessGameStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessGameStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_ChessGameStateManager {
        node [shape=record];
        "ChessGameStateManager" [label="ChessGameStateManager"];
      }

.. autoclass:: games.chess.state_manager.ChessGameStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.chess.state_manager
   :collapse:
   
.. autolink-skip:: next
