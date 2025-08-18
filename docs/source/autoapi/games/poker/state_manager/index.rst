games.poker.state_manager
=========================

.. py:module:: games.poker.state_manager

Module documentation for games.poker.state_manager


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.poker.state_manager.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.poker.state_manager.PokerStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerStateManager(debug: bool = False)

            Manager for Texas Hold'em Poker game state.

            This class provides methods for:
            - Game initialization and lifecycle management
            - Card dealing and deck management
            - Betting and pot management
            - Hand evaluation and winner determination
            - Player action validation and application
            - State observation


            Initialize the poker state manager.


            .. py:method:: _log_event(message: str)

               Log an event to the state game log and logger.



            .. py:method:: _save_state_snapshot(action_type: str)

               Save a snapshot of the current state.



            .. py:method:: advance_phase() -> tuple[bool, str]

               Advance to the next game phase.

               :returns: Tuple of (success, message)



            .. py:method:: complete_hand() -> dict[str, Any]

               Complete the current hand (showdown or single winner).

               :returns: Hand result information



            .. py:method:: export_history() -> list[dict[str, Any]]

               Export the full game history.



            .. py:method:: get_game_summary() -> dict[str, Any]

               Get a summary of the current game state.



            .. py:method:: get_legal_actions(player_id: str) -> list[dict[str, Any]]

               Get all legal actions for a player.



            .. py:method:: get_player_observation(player_id: str) -> haive.games.poker.models.PlayerObservation

               Get the game state from a specific player's perspective.



            .. py:method:: handle_player_action(player_id: str, action: haive.games.poker.models.PlayerAction, amount: int = 0) -> tuple[bool, str]

               Process a player's action.

               :param player_id: ID of the player making the action
               :param action: The action to take (fold, check, call, bet, raise, all-in)
               :param amount: The bet/raise amount (if applicable)

               :returns: Tuple of (success, message)



            .. py:method:: initialize_game(config: haive.games.poker.config.PokerAgentConfig)

               Initialize a new poker game with the given players.



            .. py:method:: is_game_over()

               Check if the game is over based on phase.



            .. py:method:: reset()

               Reset the state manager.



            .. py:method:: start_new_hand()

               Start a new hand - deal cards, post blinds, etc.



            .. py:attribute:: debug
               :value: False



            .. py:attribute:: history
               :value: []



            .. py:attribute:: state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.poker.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

