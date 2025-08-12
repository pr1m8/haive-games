
:py:mod:`games.framework.base.state`
====================================

.. py:module:: games.framework.base.state

Base state module for game agents.

This module provides the foundational state class for game agents,
defining the core state attributes that all games need to track.

.. rubric:: Example

>>> # GameState is abstract - inherit from it:
>>> class ConcreteGameState(GameState):
...     @classmethod
...     def initialize(cls, **kwargs):
...         return cls(turn="player1", game_status="ongoing")

Typical usage:
    - Inherit from GameState to create game-specific state classes
    - Use as the state schema in game configurations
    - Track game progress and history


.. autolink-examples:: games.framework.base.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.framework.base.state.GameState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameState:

   .. graphviz::
      :align: center

      digraph inheritance_GameState {
        node [shape=record];
        "GameState" [label="GameState"];
        "pydantic.BaseModel" -> "GameState";
        "abc.ABC" -> "GameState";
      }

.. autopydantic_model:: games.framework.base.state.GameState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: games.framework.base.state
   :collapse:
   
.. autolink-skip:: next
