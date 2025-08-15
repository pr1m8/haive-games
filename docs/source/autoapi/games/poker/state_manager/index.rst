games.poker.state_manager
=========================

.. py:module:: games.poker.state_manager


Attributes
----------

.. autoapisummary::

   games.poker.state_manager.logger


Classes
-------

.. autoapisummary::

   games.poker.state_manager.PokerStateManager


Module Contents
---------------

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


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerStateManager
      :collapse:

   .. py:method:: _log_event(message: str)

      Log an event to the state game log and logger.


      .. autolink-examples:: _log_event
         :collapse:


   .. py:method:: _save_state_snapshot(action_type: str)

      Save a snapshot of the current state.


      .. autolink-examples:: _save_state_snapshot
         :collapse:


   .. py:method:: advance_phase() -> tuple[bool, str]

      Advance to the next game phase.

      :returns: Tuple of (success, message)


      .. autolink-examples:: advance_phase
         :collapse:


   .. py:method:: complete_hand() -> dict[str, Any]

      Complete the current hand (showdown or single winner).

      :returns: Hand result information


      .. autolink-examples:: complete_hand
         :collapse:


   .. py:method:: export_history() -> list[dict[str, Any]]

      Export the full game history.


      .. autolink-examples:: export_history
         :collapse:


   .. py:method:: get_game_summary() -> dict[str, Any]

      Get a summary of the current game state.


      .. autolink-examples:: get_game_summary
         :collapse:


   .. py:method:: get_legal_actions(player_id: str) -> list[dict[str, Any]]

      Get all legal actions for a player.


      .. autolink-examples:: get_legal_actions
         :collapse:


   .. py:method:: get_player_observation(player_id: str) -> haive.games.poker.models.PlayerObservation

      Get the game state from a specific player's perspective.


      .. autolink-examples:: get_player_observation
         :collapse:


   .. py:method:: handle_player_action(player_id: str, action: haive.games.poker.models.PlayerAction, amount: int = 0) -> tuple[bool, str]

      Process a player's action.

      :param player_id: ID of the player making the action
      :param action: The action to take (fold, check, call, bet, raise, all-in)
      :param amount: The bet/raise amount (if applicable)

      :returns: Tuple of (success, message)


      .. autolink-examples:: handle_player_action
         :collapse:


   .. py:method:: initialize_game(config: haive.games.poker.config.PokerAgentConfig)

      Initialize a new poker game with the given players.


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: is_game_over()

      Check if the game is over based on phase.


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: reset()

      Reset the state manager.


      .. autolink-examples:: reset
         :collapse:


   .. py:method:: start_new_hand()

      Start a new hand - deal cards, post blinds, etc.


      .. autolink-examples:: start_new_hand
         :collapse:


   .. py:attribute:: debug
      :value: False



   .. py:attribute:: history
      :value: []



   .. py:attribute:: state


.. py:data:: logger

