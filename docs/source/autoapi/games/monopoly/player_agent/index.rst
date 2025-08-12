
:py:mod:`games.monopoly.player_agent`
=====================================

.. py:module:: games.monopoly.player_agent

Monopoly player agent implementation.

This module provides the player agent (subgraph) for making individual
player decisions in Monopoly, including:
    - Property purchase decisions
    - Jail decisions
    - Building decisions
    - Trade negotiations


.. autolink-examples:: games.monopoly.player_agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.monopoly.player_agent.MonopolyGameAgentConfig
   games.monopoly.player_agent.MonopolyPlayerAgent
   games.monopoly.player_agent.MonopolyPlayerAgentConfig
   games.monopoly.player_agent.PlayerDecisionState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyGameAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyGameAgentConfig {
        node [shape=record];
        "MonopolyGameAgentConfig" [label="MonopolyGameAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "MonopolyGameAgentConfig";
      }

.. autoclass:: games.monopoly.player_agent.MonopolyGameAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyPlayerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyPlayerAgent {
        node [shape=record];
        "MonopolyPlayerAgent" [label="MonopolyPlayerAgent"];
        "haive.core.engine.agent.agent.Agent[MonopolyPlayerAgentConfig]" -> "MonopolyPlayerAgent";
      }

.. autoclass:: games.monopoly.player_agent.MonopolyPlayerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyPlayerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyPlayerAgentConfig {
        node [shape=record];
        "MonopolyPlayerAgentConfig" [label="MonopolyPlayerAgentConfig"];
        "haive.core.engine.agent.config.AgentConfig" -> "MonopolyPlayerAgentConfig";
      }

.. autoclass:: games.monopoly.player_agent.MonopolyPlayerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerDecisionState:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerDecisionState {
        node [shape=record];
        "PlayerDecisionState" [label="PlayerDecisionState"];
        "haive.core.schema.prebuilt.messages_state.MessagesState" -> "PlayerDecisionState";
      }

.. autoclass:: games.monopoly.player_agent.PlayerDecisionState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.monopoly.player_agent
   :collapse:
   
.. autolink-skip:: next
