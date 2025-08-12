
:py:mod:`games.reversi.state_manager`
=====================================

.. py:module:: games.reversi.state_manager

Reversi (Othello) game state management module.

This module provides comprehensive state management functionality for Reversi/Othello,
including move validation, disc flipping mechanics, and game progression tracking.

Reversi (also known as Othello) is a strategy board game played on an 8×8 board with
64 discs that are black on one side and white on the other. Players take turns placing
discs with their color facing up, attempting to trap opponent discs between their own
to flip them. The game starts with four discs in the center in a cross pattern.

Classes:
    ReversiStateManager: Main state management class for Reversi/Othello operations.

.. rubric:: Example

Basic Reversi game setup and play:

    >>> from haive.games.reversi.state_manager import ReversiStateManager
    >>> from haive.games.reversi.models import ReversiMove
    >>>
    >>> # Initialize standard Reversi game
    >>> state = ReversiStateManager.initialize()
    >>> print(f"Current player: {state.turn}")  # "B" (Black)
    >>> print(f"Board size: 8x8")
    >>> print(f"Black discs: {state.black_count}, White discs: {state.white_count}")
    >>>
    >>> # Get legal moves (must flip at least one opponent disc)
    >>> legal_moves = ReversiStateManager.get_legal_moves(state)
    >>> print(f"Legal moves for Black: {len(legal_moves)}")
    >>>
    >>> # Make a move
    >>> if legal_moves:
    ...     move = legal_moves[0]
    ...     new_state = ReversiStateManager.apply_move(state, move)
    ...     print(f"Move at ({move.row}, {move.col}) flipped {move.flipped_count} discs")

.. note::

   - Standard 8×8 board with initial cross pattern in center
   - Players are "B" (Black) and "W" (White) with Black moving first
   - Legal moves must flip at least one opponent disc
   - Game ends when no legal moves exist for both players
   - Winner is determined by who has more discs when game ends
   - Pass moves are automatic when no legal moves exist


.. autolink-examples:: games.reversi.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.reversi.state_manager.ReversiStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReversiStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_ReversiStateManager {
        node [shape=record];
        "ReversiStateManager" [label="ReversiStateManager"];
        "haive.games.framework.base.state_manager.GameStateManager[haive.games.reversi.state.ReversiState]" -> "ReversiStateManager";
      }

.. autoclass:: games.reversi.state_manager.ReversiStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.reversi.state_manager
   :collapse:
   
.. autolink-skip:: next
