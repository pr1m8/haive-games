games.framework.base.state
==========================

.. py:module:: games.framework.base.state

.. autoapi-nested-parse::

   Base state module for game agents.

   This module provides the foundational state class for game agents,
   defining the core state attributes that all games need to track.

   .. rubric:: Examples

   >>> # GameState is abstract - inherit from it:
   >>> class ConcreteGameState(GameState):
   ...     @classmethod
   ...     def initialize(cls, **kwargs):
   ...         return cls(turn="player1", game_status="ongoing")

   Typical usage:
       - Inherit from GameState to create game-specific state classes
       - Use as the state schema in game configurations
       - Track game progress and history



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/framework/base/state/GameState

.. autoapisummary::

   games.framework.base.state.GameState


