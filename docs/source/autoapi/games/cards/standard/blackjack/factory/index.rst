
:py:mod:`games.cards.standard.blackjack.factory`
================================================

.. py:module:: games.cards.standard.blackjack.factory



Functions
---------

.. autoapisummary::

   games.cards.standard.blackjack.factory.create_blackjack_agent
   games.cards.standard.blackjack.factory.run_blackjack_game

.. py:function:: create_blackjack_agent(num_players: int = 2, max_rounds: int = 10, initial_chips: float = 1000.0, visualize: bool = True) -> haive.games.cards.standard.blackjack.agent.BlackjackAgent

   Create a Blackjack agent with customizable parameters.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param initial_chips: Starting chip amount for each player
   :param visualize: Whether to visualize the game state during play

   :returns: Configured BlackjackAgent


   .. autolink-examples:: create_blackjack_agent
      :collapse:

.. py:function:: run_blackjack_game(num_players: int = 2, max_rounds: int = 10, initial_chips: float = 1000.0, visualize: bool = True) -> dict

   Convenience function to create and run a Blackjack game.

   :param num_players: Number of players in the game
   :param max_rounds: Maximum number of rounds to play
   :param initial_chips: Starting chip amount for each player
   :param visualize: Whether to visualize the game state during play

   :returns: Final game state


   .. autolink-examples:: run_blackjack_game
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.cards.standard.blackjack.factory
   :collapse:
   
.. autolink-skip:: next
