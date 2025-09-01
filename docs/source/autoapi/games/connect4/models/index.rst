games.connect4.models
=====================

.. py:module:: games.connect4.models

.. autoapi-nested-parse::

   Connect4 game models module.

   This module provides data models for the Connect4 game implementation, including:
       - Move validation and representation
       - Player decisions and analysis
       - Game state components
       - Structured output models for LLMs

   .. rubric:: Example

   >>> from haive.games.connect4.models import Connect4Move
   >>>
   >>> # Create and validate a move
   >>> move = Connect4Move(
   ...     column=3,
   ...     explanation="Control the center column"
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/connect4/models/Connect4Analysis
   /autoapi/games/connect4/models/Connect4Move
   /autoapi/games/connect4/models/Connect4PlayerDecision

.. autoapisummary::

   games.connect4.models.Connect4Analysis
   games.connect4.models.Connect4Move
   games.connect4.models.Connect4PlayerDecision


