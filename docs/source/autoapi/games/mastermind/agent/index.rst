games.mastermind.agent
======================

.. py:module:: games.mastermind.agent


Attributes
----------

.. autoapisummary::

   games.mastermind.agent.UI_AVAILABLE
   games.mastermind.agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mastermind/agent/MastermindAgent

.. autoapisummary::

   games.mastermind.agent.MastermindAgent


Functions
---------

.. autoapisummary::

   games.mastermind.agent.ensure_game_state


Module Contents
---------------

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mastermind.state.MastermindState | langgraph.types.Command) -> haive.games.mastermind.state.MastermindState

   Ensure input is converted to MastermindState.

   :param state_input: State input as dict, MastermindState, or Command

   :returns: MastermindState instance


.. py:data:: UI_AVAILABLE
   :value: True


.. py:data:: logger

