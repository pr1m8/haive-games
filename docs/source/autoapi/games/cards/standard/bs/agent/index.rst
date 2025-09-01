games.cards.standard.bs.agent
=============================

.. py:module:: games.cards.standard.bs.agent


Attributes
----------

.. autoapisummary::

   games.cards.standard.bs.agent.final_state


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/cards/standard/bs/agent/BullshitAgent

.. autoapisummary::

   games.cards.standard.bs.agent.BullshitAgent


Functions
---------

.. autoapisummary::

   games.cards.standard.bs.agent.create_bullshit_agent
   games.cards.standard.bs.agent.run_game


Module Contents
---------------

.. py:function:: create_bullshit_agent(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> BullshitAgent

   Create a Bullshit agent with customizable parameters.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param visualize: Whether to visualize the game state

   :returns: Configured BullshitAgent


.. py:function:: run_game(num_players: int = 4, max_rounds: int = 20, visualize: bool = True) -> dict

   Convenience function to create and run a Bullshit game.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param visualize: Whether to visualize the game state during play

   :returns: Final game state


.. py:data:: final_state

