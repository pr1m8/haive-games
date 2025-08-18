games.cards.standard.blackjack.factory
======================================

.. py:module:: games.cards.standard.blackjack.factory

Module documentation for games.cards.standard.blackjack.factory


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.cards.standard.blackjack.factory.final_state

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.cards.standard.blackjack.factory.create_blackjack_agent
      games.cards.standard.blackjack.factory.run_blackjack_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_blackjack_agent(num_players: int = 2, max_rounds: int = 10, initial_chips: float = 1000.0, visualize: bool = True) -> haive.games.cards.standard.blackjack.agent.BlackjackAgent

            Create a Blackjack agent with customizable parameters.

            :param num_players: Number of players in the game
            :param max_rounds: Maximum number of rounds to play
            :param initial_chips: Starting chip amount for each player
            :param visualize: Whether to visualize the game state during play

            :returns: Configured BlackjackAgent



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_blackjack_game(num_players: int = 2, max_rounds: int = 10, initial_chips: float = 1000.0, visualize: bool = True) -> dict

            Convenience function to create and run a Blackjack game.

            :param num_players: Number of players in the game
            :param max_rounds: Maximum number of rounds to play
            :param initial_chips: Starting chip amount for each player
            :param visualize: Whether to visualize the game state during play

            :returns: Final game state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: final_state




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.blackjack.factory import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

