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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/checkers/state_manager/CheckersStateManager

.. autoapisummary::

   games.checkers.state_manager.CheckersStateManager


