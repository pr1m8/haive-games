
:py:mod:`games.mancala.agent`
=============================

.. py:module:: games.mancala.agent

Mancala game agent.

This module defines the Mancala game agent, which uses language models to generate moves
and analyze positions in the game.


.. autolink-examples:: games.mancala.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.mancala.agent.MancalaAgent


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

.. autoclass:: games.mancala.agent.MancalaAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mancala.agent.ensure_game_state
   games.mancala.agent.extract_data_from_response

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

   Ensure input is converted to MancalaState.

   :param state_input: Input that could be a dict, MancalaState, or Command.

   :returns: Properly typed game state.
   :rtype: MancalaState


   .. autolink-examples:: ensure_game_state
      :collapse:

.. py:function:: extract_data_from_response(response: Any, data_type: str = 'move') -> dict[str, Any] | None

   Extract move or analysis data from an LLM response.

   :param response: The response from the LLM.
   :param data_type: Type of data to extract ('move' or 'analysis').

   :returns: Extracted data dictionary or None.


   .. autolink-examples:: extract_data_from_response
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mancala.agent
   :collapse:
   
.. autolink-skip:: next
