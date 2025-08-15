games.cards.standard.blackjack.state_manager
============================================

.. py:module:: games.cards.standard.blackjack.state_manager


Classes
-------

.. autoapisummary::

   games.cards.standard.blackjack.state_manager.BlackjackStateManager


Module Contents
---------------

.. py:class:: BlackjackStateManager

   Manages the state and core logic for a Blackjack game.


   .. autolink-examples:: BlackjackStateManager
      :collapse:

   .. py:method:: _advance_turn(state: haive.games.cards.standard.blackjack.models.BlackjackGameState)
      :classmethod:


      Advance to the next active hand or player.

      :param state: Current game state


      .. autolink-examples:: _advance_turn
         :collapse:


   .. py:method:: _determine_winners(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Determine winners and distribute chips.

      :param state: Current game state

      :returns: Final game state with results


      .. autolink-examples:: _determine_winners
         :collapse:


   .. py:method:: create_deck() -> list[haive.games.cards.standard.blackjack.models.Card]
      :classmethod:


      Create a full deck of 52 cards.


      .. autolink-examples:: create_deck
         :collapse:


   .. py:method:: deal_initial_cards(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Deal initial cards to players and dealer.

      :param state: Current game state

      :returns: Updated game state with initial cards dealt


      .. autolink-examples:: deal_initial_cards
         :collapse:


   .. py:method:: dealer_turn(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Execute dealer's turn according to standard Blackjack rules.

      :param state: Current game state

      :returns: Final game state with results


      .. autolink-examples:: dealer_turn
         :collapse:


   .. py:method:: get_current_player_and_hand(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> tuple[haive.games.cards.standard.blackjack.models.PlayerState, haive.games.cards.standard.blackjack.models.PlayerHand]
      :classmethod:


      Get the current active player and their current hand.

      :param state: Current game state

      :returns: Tuple of current player and current hand


      .. autolink-examples:: get_current_player_and_hand
         :collapse:


   .. py:method:: initialize_game(num_players: int = 1) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Initialize a new Blackjack game.

      :param num_players: Number of players in the game

      :returns: Initialized game state


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: place_bet(state: haive.games.cards.standard.blackjack.models.BlackjackGameState, player_index: int, bet_amount: float) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Place a bet for a player.

      :param state: Current game state
      :param player_index: Index of the player placing the bet
      :param bet_amount: Amount to bet

      :returns: Updated game state


      .. autolink-examples:: place_bet
         :collapse:


   .. py:method:: process_player_action(state: haive.games.cards.standard.blackjack.models.BlackjackGameState, action: haive.games.cards.standard.blackjack.models.PlayerAction) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Process a player's action during their turn.

      :param state: Current game state
      :param action: Player's chosen action

      :returns: Updated game state


      .. autolink-examples:: process_player_action
         :collapse:


   .. py:method:: reset_game(state: haive.games.cards.standard.blackjack.models.BlackjackGameState) -> haive.games.cards.standard.blackjack.models.BlackjackGameState
      :classmethod:


      Reset the game for a new round.

      :param state: Current game state

      :returns: Reset game state


      .. autolink-examples:: reset_game
         :collapse:


