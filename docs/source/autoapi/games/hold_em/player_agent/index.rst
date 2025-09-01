games.hold_em.player_agent
==========================

.. py:module:: games.hold_em.player_agent

.. autoapi-nested-parse::

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

   .. rubric:: Examples

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



Attributes
----------

.. autoapisummary::

   games.hold_em.player_agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/player_agent/HoldemPlayerAgent
   /autoapi/games/hold_em/player_agent/HoldemPlayerAgentConfig
   /autoapi/games/hold_em/player_agent/PlayerSubgraphState

.. autoapisummary::

   games.hold_em.player_agent.HoldemPlayerAgent
   games.hold_em.player_agent.HoldemPlayerAgentConfig
   games.hold_em.player_agent.PlayerSubgraphState


Module Contents
---------------

.. py:data:: logger

