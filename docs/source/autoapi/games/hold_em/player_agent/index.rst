
:py:mod:`games.hold_em.player_agent`
====================================

.. py:module:: games.hold_em.player_agent

Texas Hold'em Player Agent module for LLM-powered poker players.

This module implements the player decision-making system for Texas Hold'em poker,
providing a complete workflow for analyzing the game state and making strategic decisions.
The player agent is implemented as a subgraph in the main game graph, with each player
having their own autonomous decision-making process.

Key components:
    - PlayerSubgraphState: State model for player decision-making
    - HoldemPlayerAgentConfig: Configuration for player agents
    - HoldemPlayerAgent: The player agent implementation with decision workflow
    - Decision pipeline: Situation analysis -> Hand analysis -> Opponent analysis -> Decision

The agent uses a multi-step analysis process, with each step handled by a specialized
LLM engine to generate the final poker decision. This design allows for detailed reasoning
about poker strategy based on the current game state.

.. rubric:: Example

>>> from haive.games.hold_em.player_agent import HoldemPlayerAgent, HoldemPlayerAgentConfig
>>> from haive.games.hold_em.engines import build_player_engines
>>>
>>> # Create a player configuration
>>> player_engines = build_player_engines("Alice", "balanced")
>>> player_config = HoldemPlayerAgentConfig(
...     name="player_alice",
...     player_name="Alice",
...     player_style="balanced",
...     engines=player_engines
... )
>>>
>>> # Create the player agent
>>> player_agent = HoldemPlayerAgent(player_config)


.. autolink-examples:: games.hold_em.player_agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.hold_em.player_agent.HoldemPlayerAgent
   games.hold_em.player_agent.HoldemPlayerAgentConfig
   games.hold_em.player_agent.PlayerSubgraphState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldemPlayerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HoldemPlayerAgent {
        node [shape=record];
        "HoldemPlayerAgent" [label="HoldemPlayerAgent"];
        "haive.core.engine.agent.agent.Agent[HoldemPlayerAgentConfig]" -> "HoldemPlayerAgent";
      }

.. autoclass:: games.hold_em.player_agent.HoldemPlayerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldemPlayerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_HoldemPlayerAgentConfig {
        node [shape=record];
        "HoldemPlayerAgentConfig" [label="HoldemPlayerAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "HoldemPlayerAgentConfig";
      }

.. autoclass:: games.hold_em.player_agent.HoldemPlayerAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerSubgraphState:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerSubgraphState {
        node [shape=record];
        "PlayerSubgraphState" [label="PlayerSubgraphState"];
        "pydantic.BaseModel" -> "PlayerSubgraphState";
      }

.. autopydantic_model:: games.hold_em.player_agent.PlayerSubgraphState
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

.. autolink-examples:: games.hold_em.player_agent
   :collapse:
   
.. autolink-skip:: next
