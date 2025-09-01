games.base.state_manager
========================

.. py:module:: games.base.state_manager

.. autoapi-nested-parse::

   Base state manager module for game agents.

   This module provides the foundational state manager class that handles
   game state transitions and operations. It defines the interface that all
   game-specific state managers should implement.

   .. rubric:: Example

   >>> class ChessStateManager(GameStateManager[ChessMove]):
   ...     @classmethod
   ...     def initialize(cls) -> ChessState:
   ...         return ChessState.new_game()
   ...
   ...     @classmethod
   ...     def apply_move(cls, state: ChessState, move: ChessMove) -> ChessState:
   ...         return state.apply_move(move)

   Typical usage:
       - Inherit from GameStateManager to create game-specific state managers
       - Implement the required methods for state initialization and transitions
       - Use in conjunction with game agents to manage game flow



Attributes
----------

.. autoapisummary::

   games.base.state_manager.T


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/base/state_manager/GameStateManager

.. autoapisummary::

   games.base.state_manager.GameStateManager


Module Contents
---------------

.. py:data:: T

