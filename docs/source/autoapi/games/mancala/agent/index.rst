games.mancala.agent
===================

.. py:module:: games.mancala.agent

.. autoapi-nested-parse::

   Mancala game agent.

   This module defines the Mancala game agent, which uses language models to generate moves
   and analyze positions in the game.



Attributes
----------

.. autoapisummary::

   games.mancala.agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mancala/agent/MancalaAgent

.. autoapisummary::

   games.mancala.agent.MancalaAgent


Functions
---------

.. autoapisummary::

   games.mancala.agent.ensure_game_state
   games.mancala.agent.extract_data_from_response


Module Contents
---------------

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

   Ensure input is converted to MancalaState.

   :param state_input: Input that could be a dict, MancalaState, or Command.

   :returns: Properly typed game state.
   :rtype: MancalaState


.. py:function:: extract_data_from_response(response: Any, data_type: str = 'move') -> dict[str, Any] | None

   Extract move or analysis data from an LLM response.

   :param response: The response from the LLM.
   :param data_type: Type of data to extract ('move' or 'analysis').

   :returns: Extracted data dictionary or None.


.. py:data:: logger

