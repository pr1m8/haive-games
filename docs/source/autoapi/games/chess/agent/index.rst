
:py:mod:`games.chess.agent`
===========================

.. py:module:: games.chess.agent

Chess agent implementation using LangGraph.

This module provides a chess agent implementation using LangGraph, featuring:
    - LLM-powered chess players
    - Position analysis
    - Game state management
    - Workflow graph for turn-based gameplay
    - Error handling and retry logic

The agent orchestrates the game flow between two LLM players and handles
all game mechanics including move validation, position analysis, and
game status tracking.


.. autolink-examples:: games.chess.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.agent.ChessAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ChessAgent {
        node [shape=record];
        "ChessAgent" [label="ChessAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.chess.config.ChessConfig]" -> "ChessAgent";
      }

.. autoclass:: games.chess.agent.ChessAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.chess.agent
   :collapse:
   
.. autolink-skip:: next
