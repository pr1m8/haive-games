games.fox_and_geese.agent
=========================

.. py:module:: games.fox_and_geese.agent

.. autoapi-nested-parse::

   Fox and Geese game agent with fixed state handling and UI integration.

   This module defines the Fox and Geese game agent, which uses language models to generate
   moves and analyze positions in the game.



Attributes
----------

.. autoapisummary::

   games.fox_and_geese.agent.UI_AVAILABLE
   games.fox_and_geese.agent.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/fox_and_geese/agent/FoxAndGeeseAgent

.. autoapisummary::

   games.fox_and_geese.agent.FoxAndGeeseAgent


Functions
---------

.. autoapisummary::

   games.fox_and_geese.agent.ensure_game_state


Module Contents
---------------

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.fox_and_geese.state.FoxAndGeeseState) -> haive.games.fox_and_geese.state.FoxAndGeeseState

   Ensure input is converted to FoxAndGeeseState.

   :param state_input: State input as dict or FoxAndGeeseState

   :returns: FoxAndGeeseState instance


.. py:data:: UI_AVAILABLE
   :value: True


.. py:data:: logger

