
:py:mod:`games.fox_and_geese.agent`
===================================

.. py:module:: games.fox_and_geese.agent

Fox and Geese game agent with fixed state handling and UI integration.

This module defines the Fox and Geese game agent, which uses language models to generate
moves and analyze positions in the game.


.. autolink-examples:: games.fox_and_geese.agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.fox_and_geese.agent.FoxAndGeeseAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FoxAndGeeseAgent:

   .. graphviz::
      :align: center

      digraph inheritance_FoxAndGeeseAgent {
        node [shape=record];
        "FoxAndGeeseAgent" [label="FoxAndGeeseAgent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.fox_and_geese.config.FoxAndGeeseConfig]" -> "FoxAndGeeseAgent";
      }

.. autoclass:: games.fox_and_geese.agent.FoxAndGeeseAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.fox_and_geese.agent.ensure_game_state

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.fox_and_geese.state.FoxAndGeeseState) -> haive.games.fox_and_geese.state.FoxAndGeeseState

   Ensure input is converted to FoxAndGeeseState.

   :param state_input: State input as dict or FoxAndGeeseState

   :returns: FoxAndGeeseState instance


   .. autolink-examples:: ensure_game_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.fox_and_geese.agent
   :collapse:
   
.. autolink-skip:: next
