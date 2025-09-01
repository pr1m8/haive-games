games.connect4.state_manager
============================

.. py:module:: games.connect4.state_manager

.. autoapi-nested-parse::

   Connect Four game state management module.

   This module provides comprehensive state management functionality for the Connect Four
   game, including board management, move validation, win detection, and game status tracking.

   Connect Four is a strategy game played on a 7×6 grid where players take turns dropping
   colored pieces into columns. The pieces fall to the lowest available position in the
   chosen column. The first player to get four pieces in a row (horizontally, vertically,
   or diagonally) wins the game.

   Classes:
       Connect4StateManager: Main state management class for Connect Four operations.

   .. rubric:: Example

   Basic Connect Four game setup and play:

       >>> from haive.games.connect4.state_manager import Connect4StateManager
       >>> from haive.games.connect4.models import Connect4Move
       >>>
       >>> # Initialize game (red player starts)
       >>> state = Connect4StateManager.initialize()
       >>> print(f"Current player: {state.current_player}")  # "red"
       >>> print(f"Board size: {len(state.board)}x{len(state.board[0])}")  # "6x7"
       >>>
       >>> # Drop piece in center column
       >>> move = Connect4Move(column=3, explanation="Center play")
       >>> new_state = Connect4StateManager.apply_move(state, move)
       >>>
       >>> # Check if column is full
       >>> legal_moves = Connect4StateManager.get_legal_moves(new_state)
       >>> print(f"Available columns: {[m.column for m in legal_moves]}")

   .. note::

      - Columns are 0-indexed (0-6 for a standard 7-column board)
      - Players alternate between "red" and "yellow"
      - Pieces are placed at the bottom-most available position in each column
      - The game ends when a player gets 4 in a row or the board is full (draw)



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/connect4/state_manager/Connect4StateManager

.. autoapisummary::

   games.connect4.state_manager.Connect4StateManager


