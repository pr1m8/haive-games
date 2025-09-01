games.tic_tac_toe.state_manager
===============================

.. py:module:: games.tic_tac_toe.state_manager

.. autoapi-nested-parse::

   Tic Tac Toe game state management module.

   This module provides comprehensive state management functionality for the classic
   Tic Tac Toe game, including board initialization, move validation, win detection,
   and game status tracking.

   Tic Tac Toe is a classic strategy game played on a 3×3 grid where players take
   turns placing their marks (X or O) in empty squares. The first player to get
   three marks in a row (horizontally, vertically, or diagonally) wins.

   Classes:
       TicTacToeStateManager: Main state management class for Tic Tac Toe operations.

   .. rubric:: Example

   Basic Tic Tac Toe game setup and play:

       >>> from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager
       >>> from haive.games.tic_tac_toe.models import TicTacToeMove
       >>>
       >>> # Initialize game
       >>> state = TicTacToeStateManager.initialize()
       >>> print(f"Current player: {state.turn}")
       >>>
       >>> # Make a move in the center
       >>> move = TicTacToeMove(row=1, col=1, player="X")
       >>> new_state = TicTacToeStateManager.apply_move(state, move)
       >>>
       >>> # Check for winners
       >>> winner = TicTacToeStateManager.get_winner(new_state)
       >>> print(f"Winner: {winner}")

   .. note::

      The board uses 0-based indexing where (0,0) is top-left and (2,2) is bottom-right.
      Players are represented as "X" and "O" strings in the game state.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/tic_tac_toe/state_manager/TicTacToeStateManager

.. autoapisummary::

   games.tic_tac_toe.state_manager.TicTacToeStateManager


