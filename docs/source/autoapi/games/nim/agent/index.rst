games.nim.agent
===============

.. py:module:: games.nim.agent

.. autoapi-nested-parse::

   Agent for playing Nim.

   This module defines the Nim agent, which uses language models to generate moves and
   analyze positions in the game.



Attributes
----------

.. autoapisummary::

   games.nim.agent.RICH_AVAILABLE
   games.nim.agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/nim/agent/NimAgent

.. autoapisummary::

   games.nim.agent.NimAgent


Functions
---------

.. autoapisummary::

   games.nim.agent.ensure_game_state


Module Contents
---------------

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.nim.state.NimState | langgraph.types.Command) -> haive.games.nim.state.NimState

   Ensure input is converted to NimState.

   This helper function ensures that the input state is properly converted to a NimState
   object, handling various input types (dict, NimState, Command).

   :param state_input: The state to convert, which can be a dictionary, NimState, or Command.

   :returns: The converted state.
   :rtype: NimState


.. py:data:: RICH_AVAILABLE
   :value: False


.. py:data:: logger

