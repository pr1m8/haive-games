
:py:mod:`games.mancala.agent_original`
======================================

.. py:module:: games.mancala.agent_original

Mancala game agent.

This module defines the Mancala game agent, which uses language models to generate moves
and analyze positions in the game.


.. autolink-examples:: games.mancala.agent_original
   :collapse:

Classes
-------

.. autoapisummary::

   games.mancala.agent_original.MancalaAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MancalaAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MancalaAgent {
        node [shape=record];
        "MancalaAgent" [label="MancalaAgent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.mancala.config.MancalaConfig]" -> "MancalaAgent";
      }

.. autoclass:: games.mancala.agent_original.MancalaAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mancala.agent_original.ensure_game_state

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

   Ensure input is converted to MancalaState.

   :param state_input: State input as dict, MancalaState, or Command

   :returns: MancalaState instance


   .. autolink-examples:: ensure_game_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mancala.agent_original
   :collapse:
   
.. autolink-skip:: next
