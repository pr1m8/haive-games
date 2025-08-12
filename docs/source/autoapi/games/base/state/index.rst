
:py:mod:`games.base.state`
==========================

.. py:module:: games.base.state

Base state module for game agents.

This module provides the foundational state class for game agents,
defining the core state attributes that all games need to track.

.. rubric:: Example

>>> state = GameState(
...     turn="player1",
...     game_status="ongoing",
...     move_history=[]
... )

Typical usage:
    - Inherit from GameState to create game-specific state classes
    - Use as the state schema in game configurations
    - Track game progress and history


.. autolink-examples:: games.base.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.base.state.GameState


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

.. autopydantic_model:: games.base.state.GameState
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

.. autolink-examples:: games.base.state
   :collapse:
   
.. autolink-skip:: next
