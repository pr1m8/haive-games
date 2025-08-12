
:py:mod:`games.debate_v2.agent`
===============================

.. py:module:: games.debate_v2.agent

Gamified Debate Agent - Modern Implementation.

This module implements a gamified debate using the modern conversation agent
pattern from haive-agents, providing proper topic handling and state management
without the deprecated DynamicGraph system.


.. autolink-examples:: games.debate_v2.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.debate_v2.agent.GameDebateAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameDebateAgent:

   .. graphviz::
      :align: center

      digraph inheritance_GameDebateAgent {
        node [shape=record];
        "GameDebateAgent" [label="GameDebateAgent"];
        "haive.agents.conversation.debate.agent.DebateConversation" -> "GameDebateAgent";
      }

.. autoclass:: games.debate_v2.agent.GameDebateAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.debate_v2.agent
   :collapse:
   
.. autolink-skip:: next
