games.clue.ui
=============

.. py:module:: games.clue.ui

.. autoapi-nested-parse::

   Clue rich UI visualization module.

   This module provides a visually appealing terminal UI for Clue games,
   with styled components, animations, and comprehensive game information.

   It uses the Rich library to create a console-based UI with:
       - Game board visualization with players, suspects, weapons, and rooms
       - Guess history with detailed responses
       - Player cards and deduction notes
       - Game status and information
       - Thinking animations and guess visualization

   .. rubric:: Example

   >>> from haive.games.clue.ui import ClueUI
   >>> from haive.games.clue.state import ClueState
   >>>
   >>> ui = ClueUI()
   >>> state = ClueState.initialize()
   >>> ui.display_state(state)  # Display the initial game state
   >>>
   >>> # Show thinking animation for player
   >>> ui.show_thinking("player1")
   >>>
   >>> # Display a guess
   >>> from haive.games.clue.models import ClueGuess, ValidSuspect, ValidWeapon, ValidRoom
   >>> guess = ClueGuess(
   >>>     suspect=ValidSuspect.COLONEL_MUSTARD,
   >>>     weapon=ValidWeapon.KNIFE,
   >>>     room=ValidRoom.KITCHEN
   >>> )
   >>> ui.show_guess(guess, "player1")



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/clue/ui/ClueUI

.. autoapisummary::

   games.clue.ui.ClueUI


