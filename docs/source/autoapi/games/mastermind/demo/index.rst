games.mastermind.demo
=====================

.. py:module:: games.mastermind.demo

.. autoapi-nested-parse::

   Standalone demo for the Mastermind game with Rich UI.

   This script demonstrates the Mastermind game without requiring the full Haive framework.



Attributes
----------

.. autoapisummary::

   games.mastermind.demo.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mastermind/demo/ColorCode
   /autoapi/games/mastermind/demo/Feedback
   /autoapi/games/mastermind/demo/MastermindState
   /autoapi/games/mastermind/demo/MastermindUI

.. autoapisummary::

   games.mastermind.demo.ColorCode
   games.mastermind.demo.Feedback
   games.mastermind.demo.MastermindState
   games.mastermind.demo.MastermindUI


Functions
---------

.. autoapisummary::

   games.mastermind.demo.calculate_feedback
   games.mastermind.demo.main


Module Contents
---------------

.. py:function:: calculate_feedback(secret_code: list[str], guess: list[str]) -> dict[str, int]

   Calculate feedback for a guess.


.. py:function:: main()

   Run the Mastermind game.


.. py:data:: logger

