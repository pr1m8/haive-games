games.cards.standard.blackjack.state_manager
============================================

.. py:module:: games.cards.standard.blackjack.state_manager

Module documentation for games.cards.standard.blackjack.state_manager


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.cards.standard.blackjack.state_manager.BlackjackStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BlackjackStateManager

            Manages the state and core logic for a Blackjack game.


            .. py:method:: _advance_turn(state: haive.games.cards.standard.blackjack.models.BlackjackGameState)
               :classmethod:


               Advance to the next active hand or player.

               :param state: Current game state



            .. py:method:: _determine_winners(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Determine winners and distribute chips.

               :param state: Current game state

               :returns: Final game state with results



            .. py:method:: create_deck() -> list[haive.games.cards.standard.blackjack.models.Card]
               :classmethod:


               Create a full deck of 52 cards.



            .. py:method:: deal_initial_cards(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Deal initial cards to players and dealer.

               :param state: Current game state

               :returns: Updated game state with initial cards dealt



            .. py:method:: dealer_turn(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Execute dealer's turn according to standard Blackjack rules.

               :param state: Current game state

               :returns: Final game state with results



            .. py:method:: get_current_player_and_hand(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> tuple[haive.games.cards.standard.blackjack.models.PlayerState, haive.games.cards.standard.blackjack.models.PlayerHand]
               :classmethod:


               Get the current active player and their current hand.

               :param state: Current game state

               :returns: Tuple of current player and current hand



            .. py:method:: initialize_game(num_players: int = 1) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Initialize a new Blackjack game.

               :param num_players: Number of players in the game

               :returns: Initialized game state



            .. py:method:: place_bet(state: haive.games.cards.standard.blackjack.models.BlackjackGameState, player_index: int, bet_amount: float) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Place a bet for a player.

               :param state: Current game state
               :param player_index: Index of the player placing the bet
               :param bet_amount: Amount to bet

               :returns: Updated game state



            .. py:method:: process_player_action(state: haive.games.cards.standard.blackjack.models.BlackjackGameState, action: haive.games.cards.standard.blackjack.models.PlayerAction) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Process a player's action during their turn.

               :param state: Current game state
               :param action: Player's chosen action

               :returns: Updated game state



            .. py:method:: reset_game(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
               :classmethod:


               Reset the game for a new round.

               :param state: Current game state

               :returns: Reset game state






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.blackjack.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

