games.mancala.agent_original
============================

.. py:module:: games.mancala.agent_original

.. autoapi-nested-parse::

   Mancala game agent.

   This module defines the Mancala game agent, which uses language models to generate moves
   and analyze positions in the game.



Attributes
----------

.. autoapisummary::

   games.mancala.agent_original.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mancala/agent_original/MancalaAgent

.. autoapisummary::

   games.mancala.agent_original.MancalaAgent


Functions
---------

.. autoapisummary::

   games.mancala.agent_original.ensure_game_state


Module Contents
---------------

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

   Ensure input is converted to MancalaState.

   :param state_input: State input as dict, MancalaState, or Command

   :returns: MancalaState instance


.. py:data:: logger

