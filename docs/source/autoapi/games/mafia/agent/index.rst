games.mafia.agent
=================

.. py:module:: games.mafia.agent

.. autoapi-nested-parse::

   Mafia game agent implementation.

   This module provides the core agent implementation for the Mafia game,
   handling:
       - Game initialization and setup
       - Player turn management
       - Move generation and validation
       - Game state visualization
       - Role-specific behavior

   The agent uses LLMs to generate player decisions and narrator actions,
   creating an engaging and strategic game experience.

   .. rubric:: Example

   >>> from mafia.agent import MafiaAgent
   >>> from mafia.config import MafiaAgentConfig
   >>>
   >>> # Create and initialize agent
   >>> config = MafiaAgentConfig.default_config(player_count=7)
   >>> agent = MafiaAgent(config)
   >>>
   >>> # Run the game
   >>> for state in agent.app.stream(initial_state):
   ...     agent.visualize_state(state)



Attributes
----------

.. autoapisummary::

   games.mafia.agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/agent/MafiaAgent

.. autoapisummary::

   games.mafia.agent.MafiaAgent


Module Contents
---------------

.. py:data:: logger

