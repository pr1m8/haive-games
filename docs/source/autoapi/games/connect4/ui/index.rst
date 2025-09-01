games.connect4.ui
=================

.. py:module:: games.connect4.ui

.. autoapi-nested-parse::

   Connect4 rich UI visualization module.

   This module provides a visually appealing terminal UI for Connect4 games,
   with styled components, animations, and comprehensive game information.

   It uses the Rich library to create a console-based UI with:
       - Colorful board display with piece symbols
       - Move history panel
       - Game status and information
       - Position analysis display
       - Move and thinking animations

   .. rubric:: Example

   >>> from haive.games.connect4.ui import Connect4UI
   >>> from haive.games.connect4.state import Connect4State
   >>>
   >>> ui = Connect4UI()
   >>> state = Connect4State.initialize()
   >>> ui.display_state(state)  # Display the initial board
   >>>
   >>> # Show thinking animation for player move
   >>> ui.show_thinking("red")
   >>>
   >>> # Display a move
   >>> from haive.games.connect4.models import Connect4Move
   >>> move = Connect4Move(column=3)
   >>> ui.show_move(move, "red")



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/connect4/ui/Connect4UI

.. autoapisummary::

   games.connect4.ui.Connect4UI


