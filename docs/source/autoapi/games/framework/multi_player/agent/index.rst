games.framework.multi_player.agent
==================================

.. py:module:: games.framework.multi_player.agent

.. autoapi-nested-parse::

   Multi-player game agent implementation.

   This module provides the base agent class for multi-player games, supporting:
       - Variable number of players
       - Role-based player configurations
       - Phase-based game flow
       - Information hiding between players
       - Concurrent or sequential player actions

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.agent import MultiPlayerGameAgent
   >>>
   >>> class ChessAgent(MultiPlayerGameAgent[ChessState]):
   ...     def __init__(self, config: ChessConfig):
   ...         super().__init__(config)
   ...         self.state_manager = ChessStateManager



Attributes
----------

.. autoapisummary::

   games.framework.multi_player.agent.T


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/framework/multi_player/agent/MultiPlayerGameAgent

.. autoapisummary::

   games.framework.multi_player.agent.MultiPlayerGameAgent


Module Contents
---------------

.. py:data:: T

