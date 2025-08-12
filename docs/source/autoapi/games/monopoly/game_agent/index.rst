
:py:mod:`games.monopoly.game_agent`
===================================

.. py:module:: games.monopoly.game_agent

Fixed Monopoly game agent implementation.

This module provides the corrected main game agent for orchestrating a Monopoly game,
with proper handling of BaseModel objects from LangGraph instead of dictionaries.


.. autolink-examples:: games.monopoly.game_agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.monopoly.game_agent.MonopolyGameAgent
   games.monopoly.game_agent.MonopolyGameAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyGameAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyGameAgent {
        node [shape=record];
        "MonopolyGameAgent" [label="MonopolyGameAgent"];
        "haive.core.engine.agent.agent.Agent[MonopolyGameAgentConfig]" -> "MonopolyGameAgent";
      }

.. autoclass:: games.monopoly.game_agent.MonopolyGameAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyGameAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyGameAgentConfig {
        node [shape=record];
        "MonopolyGameAgentConfig" [label="MonopolyGameAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "MonopolyGameAgentConfig";
      }

.. autoclass:: games.monopoly.game_agent.MonopolyGameAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.monopoly.game_agent
   :collapse:
   
.. autolink-skip:: next
