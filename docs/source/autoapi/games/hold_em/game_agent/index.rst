
:py:mod:`games.hold_em.game_agent`
==================================

.. py:module:: games.hold_em.game_agent

Texas Hold'em Game Agent module - Main game coordinator and manager.

This module implements the core game management system for Texas Hold'em poker,
coordinating the game flow, player interactions, betting rounds, and showdowns.
It serves as the central orchestrator that manages the complete lifecycle of a
poker game from setup to completion.

Key features:
    - Complete poker game flow management with LangGraph
    - Betting round coordination and hand progression
    - Player action validation and processing
    - Pot management and chip tracking
    - Showdown evaluation and winner determination
    - Game state persistence and history tracking

The game agent creates and manages subgraph agents for each player, allowing them
to make independent decisions within the overall game context. It handles all
aspects of the game rules, ensuring proper sequencing of rounds and actions.

.. rubric:: Example

>>> from haive.games.hold_em.game_agent import HoldemGameAgent
>>> from haive.games.hold_em.config import create_default_holdem_config
>>>
>>> # Create a game configuration
>>> config = create_default_holdem_config(num_players=4)
>>>
>>> # Initialize the game agent
>>> agent = HoldemGameAgent(config)
>>>
>>> # Run the game
>>> result = agent.app.invoke({}, debug=True)

Implementation details:
    - Enhanced player ID handling and validation
    - Robust error checking and recovery
    - Comprehensive logging for debugging
    - Fixed player lookup and identification


.. autolink-examples:: games.hold_em.game_agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.hold_em.game_agent.HoldemGameAgent
   games.hold_em.game_agent.HoldemGameAgentConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldemGameAgent:

   .. graphviz::
      :align: center

      digraph inheritance_HoldemGameAgent {
        node [shape=record];
        "HoldemGameAgent" [label="HoldemGameAgent"];
        "haive.core.engine.agent.agent.Agent[HoldemGameAgentConfig]" -> "HoldemGameAgent";
      }

.. autoclass:: games.hold_em.game_agent.HoldemGameAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldemGameAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_HoldemGameAgentConfig {
        node [shape=record];
        "HoldemGameAgentConfig" [label="HoldemGameAgentConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "HoldemGameAgentConfig";
      }

.. autoclass:: games.hold_em.game_agent.HoldemGameAgentConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.hold_em.game_agent
   :collapse:
   
.. autolink-skip:: next
