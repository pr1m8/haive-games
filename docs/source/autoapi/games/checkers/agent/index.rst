
:py:mod:`games.checkers.agent`
==============================

.. py:module:: games.checkers.agent

Checkers agent implementation module.

This module provides the main checkers agent implementation using LangGraph, including:
    - Dynamic graph-based workflow for turn management
    - LLM-powered player engines for move generation
    - Position analysis and evaluation
    - Error handling and retry logic
    - Rich UI visualization
    - Game flow orchestration

The agent uses a state-based approach with LangGraph for managing the game workflow
and supports both automated play and human interaction through a beautiful UI.


.. autolink-examples:: games.checkers.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.checkers.agent.CheckersAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CheckersAgent:

   .. graphviz::
      :align: center

      digraph inheritance_CheckersAgent {
        node [shape=record];
        "CheckersAgent" [label="CheckersAgent"];
        "haive.games.framework.base.GameAgent[haive.games.checkers.config.CheckersAgentConfig]" -> "CheckersAgent";
      }

.. autoclass:: games.checkers.agent.CheckersAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.checkers.agent
   :collapse:
   
.. autolink-skip:: next
