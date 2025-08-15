games.cards.standard.bs.state_manager
=====================================

.. py:module:: games.cards.standard.bs.state_manager


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.state_manager.BullshitStateManager


Module Contents
---------------

.. py:class:: BullshitStateManager

   Manages the state and core logic for a Bullshit (BS) card game.


   .. autolink-examples:: BullshitStateManager
      :collapse:

   .. py:method:: check_game_status(state: haive.games.cards.standard.bs.state.BullshitGameState) -> haive.games.cards.standard.bs.state.BullshitGameState
      :classmethod:


      Check if the game has ended.

      :param state: Current game state

      :returns: Updated game state


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: initialize_game(num_players: int = 4) -> haive.games.cards.standard.bs.state.BullshitGameState
      :classmethod:


      Initialize a new Bullshit game.

      :param num_players: Number of players in the game

      :returns: Initialized game state


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: process_challenge(state: haive.games.cards.standard.bs.state.BullshitGameState, challenge: haive.games.cards.standard.bs.models.ChallengeAction) -> haive.games.cards.standard.bs.state.BullshitGameState
      :classmethod:


      Process a challenge to a player's claim.

      :param state: Current game state
      :param challenge: Challenge action

      :returns: Updated game state


      .. autolink-examples:: process_challenge
         :collapse:


   .. py:method:: process_player_claim(state: haive.games.cards.standard.bs.state.BullshitGameState, claim: haive.games.cards.standard.bs.models.PlayerClaimAction) -> haive.games.cards.standard.bs.state.BullshitGameState
      :classmethod:


      Process a player's claim and card play.

      :param state: Current game state
      :param claim: Player's claim about played cards

      :returns: Updated game state


      .. autolink-examples:: process_player_claim
         :collapse:


   .. py:method:: reset_game(state: haive.games.cards.standard.bs.state.BullshitGameState) -> haive.games.cards.standard.bs.state.BullshitGameState
      :classmethod:


      Reset the game for a new round.

      :param state: Current game state

      :returns: Reset game state


      .. autolink-examples:: reset_game
         :collapse:


   .. py:method:: validate_claim(state: haive.games.cards.standard.bs.state.BullshitGameState, claim: haive.games.cards.standard.bs.models.PlayerClaimAction) -> bool
      :classmethod:


      Validate if a player's claim is potentially true.

      :param state: Current game state
      :param claim: Player's claim about played cards

      :returns: Whether the claim could be true


      .. autolink-examples:: validate_claim
         :collapse:


