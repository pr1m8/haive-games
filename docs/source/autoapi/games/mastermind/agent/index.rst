
:py:mod:`games.mastermind.agent`
================================

.. py:module:: games.mastermind.agent


Classes
-------

.. autoapisummary::

   games.mastermind.agent.MastermindAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindAgent:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindAgent {
        node [shape=record];
        "MastermindAgent" [label="MastermindAgent"];
        "haive.games.framework.base.agent.GameAgent[haive.games.mastermind.config.MastermindConfig]" -> "MastermindAgent";
      }

.. autoclass:: games.mastermind.agent.MastermindAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mastermind.agent.ensure_game_state

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mastermind.state.MastermindState | langgraph.types.Command) -> haive.games.mastermind.state.MastermindState

   Ensure input is converted to MastermindState.

   :param state_input: State input as dict, MastermindState, or Command

   :returns: MastermindState instance


   .. autolink-examples:: ensure_game_state
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mastermind.agent
   :collapse:
   
.. autolink-skip:: next
