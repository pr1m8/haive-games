games.framework.multi_player.state_manager
==========================================

.. py:module:: games.framework.multi_player.state_manager

.. autoapi-nested-parse::

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



Attributes
----------

.. autoapisummary::

   games.framework.multi_player.state_manager.T


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/framework/multi_player/state_manager/MultiPlayerGameStateManager

.. autoapisummary::

   games.framework.multi_player.state_manager.MultiPlayerGameStateManager


Module Contents
---------------

.. py:data:: T

