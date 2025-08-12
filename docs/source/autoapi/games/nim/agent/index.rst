
:py:mod:`games.nim.agent`
=========================

.. py:module:: games.nim.agent

Agent for playing Nim.

This module defines the Nim agent, which uses language models to generate moves and
analyze positions in the game.


.. autolink-examples:: games.nim.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.nim.agent.NimAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimAgent:

   .. graphviz::
      :align: center

      digraph inheritance_NimAgent {
        node [shape=record];
        "NimAgent" [label="NimAgent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.nim.config.NimConfig]" -> "NimAgent";
      }

.. autoclass:: games.nim.agent.NimAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.nim.agent.ensure_game_state

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.nim.state.NimState | langgraph.types.Command) -> haive.games.nim.state.NimState

   Ensure input is converted to NimState.

   This helper function ensures that the input state is properly converted to a NimState
   object, handling various input types (dict, NimState, Command).

   :param state_input: The state to convert, which can be a dictionary, NimState, or Command.

   :returns: The converted state.
   :rtype: NimState


   .. autolink-examples:: ensure_game_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.nim.agent
   :collapse:
   
.. autolink-skip:: next
