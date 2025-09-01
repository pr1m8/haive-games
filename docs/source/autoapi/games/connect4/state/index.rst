games.connect4.state
====================

.. py:module:: games.connect4.state

.. autoapi-nested-parse::

   Connect4 game state module.

   This module defines the core state representation for Connect4 games,
   including board representation, move tracking, and game status.

   .. rubric:: Example

   >>> from haive.games.connect4.state import Connect4State
   >>> from haive.games.connect4.models import Connect4Move
   >>>
   >>> # Initialize a new game
   >>> state = Connect4State.initialize()
   >>> state.board_string  # Get string representation
   >>>
   >>> # Check game properties
   >>> state.is_column_full(3)  # Check if column is full
   >>> state.get_next_row(3)    # Get next available row in column



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/connect4/state/Connect4State

.. autoapisummary::

   games.connect4.state.Connect4State


