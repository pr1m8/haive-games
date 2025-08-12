
:py:mod:`games.multi_player.state_manager`
==========================================

.. py:module:: games.multi_player.state_manager

State management interface for multi-player games.

This module provides the base state manager interface for multi-player games,
defining the core operations that game-specific state managers must implement.
The state manager handles:
    - Game initialization
    - Move application and validation
    - Legal move generation
    - Game status updates
    - Phase transitions
    - Information hiding

.. rubric:: Example

>>> from typing import List, Dict, Any
>>> from haive.agents.agent_games.framework.multi_player.state_manager import MultiPlayerGameStateManager
>>>
>>> class MyGameStateManager(MultiPlayerGameStateManager[MyGameState]):
...     @classmethod
...     def initialize(cls, player_names: List[str], **kwargs) -> MyGameState:
...         return MyGameState(players=player_names)


.. autolink-examples:: games.multi_player.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.multi_player.state_manager.MultiPlayerGameStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiPlayerGameStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_MultiPlayerGameStateManager {
        node [shape=record];
        "MultiPlayerGameStateManager" [label="MultiPlayerGameStateManager"];
        "Generic[T]" -> "MultiPlayerGameStateManager";
      }

.. autoclass:: games.multi_player.state_manager.MultiPlayerGameStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.multi_player.state_manager
   :collapse:
   
.. autolink-skip:: next
