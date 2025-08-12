
:py:mod:`games.battleship.agent`
================================

.. py:module:: games.battleship.agent

Battleship game agent implementation.

This module implements the main agent for the Battleship game, including:
    - LangGraph workflow for game logic
    - Turn-based gameplay management
    - LLM-powered player actions
    - Game state transitions
    - Ship placement and move execution


.. autolink-examples:: games.battleship.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.battleship.agent.BattleshipAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BattleshipAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BattleshipAgent {
        node [shape=record];
        "BattleshipAgent" [label="BattleshipAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.battleship.config.BattleshipAgentConfig]" -> "BattleshipAgent";
      }

.. autoclass:: games.battleship.agent.BattleshipAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.battleship.agent
   :collapse:
   
.. autolink-skip:: next
