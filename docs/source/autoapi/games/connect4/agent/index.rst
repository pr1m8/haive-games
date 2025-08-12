
:py:mod:`games.connect4.agent`
==============================

.. py:module:: games.connect4.agent

Agent for playing Connect 4.

This module defines the Connect 4 agent, which uses language models to generate moves
and analyze positions in the game.


.. autolink-examples:: games.connect4.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.connect4.agent.Connect4Agent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Connect4Agent:

   .. graphviz::
      :align: center

      digraph inheritance_Connect4Agent {
        node [shape=record];
        "Connect4Agent" [label="Connect4Agent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.connect4.config.Connect4AgentConfig]" -> "Connect4Agent";
      }

.. autoclass:: games.connect4.agent.Connect4Agent
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.connect4.agent
   :collapse:
   
.. autolink-skip:: next
