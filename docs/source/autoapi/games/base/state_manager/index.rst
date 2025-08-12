
:py:mod:`games.base.state_manager`
==================================

.. py:module:: games.base.state_manager

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


.. autolink-examples:: games.base.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.base.state_manager.GameStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_GameStateManager {
        node [shape=record];
        "GameStateManager" [label="GameStateManager"];
        "Generic[T]" -> "GameStateManager";
      }

.. autoclass:: games.base.state_manager.GameStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.base.state_manager
   :collapse:
   
.. autolink-skip:: next
