games.cards.standard.bs.state_manager
=====================================

.. py:module:: games.cards.standard.bs.state_manager

Module documentation for games.cards.standard.bs.state_manager


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.cards.standard.bs.state_manager.BullshitStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BullshitStateManager

            Manages the state and core logic for a Bullshit (BS) card game.


            .. py:method:: check_game_status(state: haive.games.cards.standard.bs.state.BullshitGameState) -> haive.games.cards.standard.bs.state.BullshitGameState
               :classmethod:


               Check if the game has ended.

               :param state: Current game state

               :returns: Updated game state



            .. py:method:: initialize_game(num_players: int = 4) -> haive.games.cards.standard.bs.state.BullshitGameState
               :classmethod:


               Initialize a new Bullshit game.

               :param num_players: Number of players in the game

               :returns: Initialized game state



            .. py:method:: process_challenge(state: haive.games.cards.standard.bs.state.BullshitGameState, challenge: haive.games.cards.standard.bs.models.ChallengeAction) -> haive.games.cards.standard.bs.state.BullshitGameState
               :classmethod:


               Process a challenge to a player's claim.

               :param state: Current game state
               :param challenge: Challenge action

               :returns: Updated game state



            .. py:method:: process_player_claim(state: haive.games.cards.standard.bs.state.BullshitGameState, claim: haive.games.cards.standard.bs.models.PlayerClaimAction) -> haive.games.cards.standard.bs.state.BullshitGameState
               :classmethod:


               Process a player's claim and card play.

               :param state: Current game state
               :param claim: Player's claim about played cards

               :returns: Updated game state



            .. py:method:: reset_game(state: haive.games.cards.standard.bs.state.BullshitGameState) -> haive.games.cards.standard.bs.state.BullshitGameState
               :classmethod:


               Reset the game for a new round.

               :param state: Current game state

               :returns: Reset game state



            .. py:method:: validate_claim(state: haive.games.cards.standard.bs.state.BullshitGameState, claim: haive.games.cards.standard.bs.models.PlayerClaimAction) -> bool
               :classmethod:


               Validate if a player's claim is potentially true.

               :param state: Current game state
               :param claim: Player's claim about played cards

               :returns: Whether the claim could be true






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.bs.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

