
:py:mod:`games.monopoly.main_agent`
===================================

.. py:module:: games.monopoly.main_agent

Fixed Main Monopoly agent that orchestrates the complete game.

This module provides the corrected main agent implementation that:
    - Ensures BaseModel consistency throughout (no dict conversions)
    - Properly handles state schema compatibility
    - Fixes the validation error by maintaining BaseModel state


.. autolink-examples:: games.monopoly.main_agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.monopoly.main_agent.MonopolyAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyAgent {
        node [shape=record];
        "MonopolyAgent" [label="MonopolyAgent"];
        "haive.core.engine.agent.agent.Agent[haive.games.monopoly.game_agent.MonopolyGameAgentConfig]" -> "MonopolyAgent";
      }

.. autoclass:: games.monopoly.main_agent.MonopolyAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.monopoly.main_agent
   :collapse:
   
.. autolink-skip:: next
