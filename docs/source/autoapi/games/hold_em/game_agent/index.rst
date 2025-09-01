games.hold_em.game_agent
========================

.. py:module:: games.hold_em.game_agent

.. autoapi-nested-parse::

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

   .. rubric:: Examples

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



Attributes
----------

.. autoapisummary::

   games.hold_em.game_agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/game_agent/HoldemGameAgent
   /autoapi/games/hold_em/game_agent/HoldemGameAgentConfig

.. autoapisummary::

   games.hold_em.game_agent.HoldemGameAgent
   games.hold_em.game_agent.HoldemGameAgentConfig


Module Contents
---------------

.. py:data:: logger

