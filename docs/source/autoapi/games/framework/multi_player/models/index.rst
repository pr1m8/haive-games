games.framework.multi_player.models
===================================

.. py:module:: games.framework.multi_player.models

.. autoapi-nested-parse::

   Models for multi-player game framework.

   This module provides common enumerations and base models used across
   multi-player games. These models serve as building blocks for creating
   game-specific implementations.

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.models import GamePhase
   >>>
   >>> # Use game phases in your game state
   >>> current_phase = GamePhase.SETUP
   >>> if current_phase == GamePhase.MAIN:
   ...     # Handle main game phase
   ...     pass



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/framework/multi_player/models/GamePhase

.. autoapisummary::

   games.framework.multi_player.models.GamePhase


