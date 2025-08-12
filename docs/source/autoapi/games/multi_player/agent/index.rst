
:py:mod:`games.multi_player.agent`
==================================

.. py:module:: games.multi_player.agent

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


.. autolink-examples:: games.multi_player.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.multi_player.agent.MultiPlayerGameAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiPlayerGameAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MultiPlayerGameAgent {
        node [shape=record];
        "MultiPlayerGameAgent" [label="MultiPlayerGameAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.framework.multi_player.config.MultiPlayerGameConfig]" -> "MultiPlayerGameAgent";
        "Generic[T]" -> "MultiPlayerGameAgent";
      }

.. autoclass:: games.multi_player.agent.MultiPlayerGameAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.multi_player.agent
   :collapse:
   
.. autolink-skip:: next
