
:py:mod:`games.mafia.agent`
===========================

.. py:module:: games.mafia.agent

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


.. autolink-examples:: games.mafia.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.mafia.agent.MafiaAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MafiaAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaAgent {
        node [shape=record];
        "MafiaAgent" [label="MafiaAgent"];
        "haive.games.framework.multi_player.agent.MultiPlayerGameAgent[haive.games.mafia.config.MafiaAgentConfig]" -> "MafiaAgent";
      }

.. autoclass:: games.mafia.agent.MafiaAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.mafia.agent
   :collapse:
   
.. autolink-skip:: next
