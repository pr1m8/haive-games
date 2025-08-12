
:py:mod:`games.cards.standard.bs.agent`
=======================================

.. py:module:: games.cards.standard.bs.agent


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.agent.BullshitAgent


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BullshitAgent:

   .. graphviz::
      :align: center

      digraph inheritance_BullshitAgent {
        node [shape=record];
        "BullshitAgent" [label="BullshitAgent"];
        "haive.games.framework.base.GameAgent[haive.games.cards.standard.bs.config.BullshitAgentConfig]" -> "BullshitAgent";
      }

.. autoclass:: games.cards.standard.bs.agent.BullshitAgent
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.cards.standard.bs.agent.create_bullshit_agent
   games.cards.standard.bs.agent.run_game

.. py:function:: create_bullshit_agent(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> BullshitAgent

   Create a Bullshit agent with customizable parameters.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param visualize: Whether to visualize the game state

   :returns: Configured BullshitAgent


   .. autolink-examples:: create_bullshit_agent
      :collapse:

.. py:function:: run_game(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> dict

   Convenience function to create and run a Bullshit game.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param visualize: Whether to visualize the game state during play

   :returns: Final game state


   .. autolink-examples:: run_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.cards.standard.bs.agent
   :collapse:
   
.. autolink-skip:: next
