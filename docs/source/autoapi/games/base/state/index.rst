games.base.state
================

.. py:module:: games.base.state

.. autoapi-nested-parse::

   Base state module for game agents.

   This module provides the foundational state class for game agents,
   defining the core state attributes that all games need to track.

   .. rubric:: Examples

   >>> state = GameState(
   ...     turn="player1",
   ...     game_status="ongoing",
   ...     move_history=[]
   ... )

   Typical usage:
       - Inherit from GameState to create game-specific state classes
       - Use as the state schema in game configurations
       - Track game progress and history



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/base/state/GameState

.. autoapisummary::

   games.base.state.GameState


