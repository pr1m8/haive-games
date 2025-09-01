games.go.state
==============

.. py:module:: games.go.state

.. autoapi-nested-parse::

   Go game state management.

   This module provides state tracking and management for Go games, including:
       - Game state representation
       - Move validation and application
       - Board state tracking in SGF format
       - Capture counting
       - Game status management

   .. rubric:: Example

   >>> from haive.games.go.state import GoGameState, GoGameStateManager
   >>>
   >>> # Initialize a new game
   >>> state = GoGameStateManager.initialize(board_size=19)
   >>>
   >>> # Apply moves
   >>> state = GoGameStateManager.apply_move(state, (3, 4))  # Black's move
   >>> state = GoGameStateManager.apply_move(state, (15, 15))  # White's move
   >>>
   >>> # Check game status
   >>> print(state.game_status)  # 'ongoing'
   >>> print(state.captured_stones)  # {'black': 0, 'white': 0}



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/go/state/GoGameState

.. autoapisummary::

   games.go.state.GoGameState


