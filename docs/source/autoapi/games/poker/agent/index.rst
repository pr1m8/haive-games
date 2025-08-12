
:py:mod:`games.poker.agent`
===========================

.. py:module:: games.poker.agent

Enhanced Texas Hold'em Poker agent implementation.

This module implements a robust poker agent with improved:
- Structured output handling with proper schema validation
- Comprehensive logging and debugging
- Error handling and retry policies for invalid moves
- Enhanced prompts for LLM decisions


.. autolink-examples:: games.poker.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.poker.agent.PokerAgent
   games.poker.agent.RetryConfiguration


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerAgent:

   .. graphviz::
      :align: center

      digraph inheritance_PokerAgent {
        node [shape=record];
        "PokerAgent" [label="PokerAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.poker.config.PokerAgentConfig]" -> "PokerAgent";
      }

.. autoclass:: games.poker.agent.PokerAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RetryConfiguration:

   .. graphviz::
      :align: center

      digraph inheritance_RetryConfiguration {
        node [shape=record];
        "RetryConfiguration" [label="RetryConfiguration"];
      }

.. autoclass:: games.poker.agent.RetryConfiguration
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.poker.agent
   :collapse:
   
.. autolink-skip:: next
