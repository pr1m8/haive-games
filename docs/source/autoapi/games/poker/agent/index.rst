games.poker.agent
=================

.. py:module:: games.poker.agent

.. autoapi-nested-parse::

   Enhanced Texas Hold'em Poker agent implementation.

   This module implements a robust poker agent with improved:
   - Structured output handling with proper schema validation
   - Comprehensive logging and debugging
   - Error handling and retry policies for invalid moves
   - Enhanced prompts for LLM decisions


   .. autolink-examples:: games.poker.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.poker.agent.logger


Classes
-------

.. autoapisummary::

   games.poker.agent.PokerAgent
   games.poker.agent.RetryConfiguration


Module Contents
---------------

.. py:class:: PokerAgent(config: haive.games.poker.config.PokerAgentConfig = PokerAgentConfig())

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.poker.config.PokerAgentConfig`\ ]


   Enhanced agent class for managing a multi-player Texas Hold'em poker game.

   Key improvements:
   - Proper structured output handling
   - Comprehensive debug logging
   - Retry policies for failed operations
   - Enhanced prompts and decision handling


   Initialize the enhanced poker agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerAgent
      :collapse:

   .. py:method:: _apply_player_decision(game: haive.games.poker.state.PokerState, player: haive.games.poker.models.Player, decision: haive.games.poker.models.AgentDecision, legal_actions: list[dict[str, Any]])

      Apply the player's decision to the game state.


      .. autolink-examples:: _apply_player_decision
         :collapse:


   .. py:method:: _format_legal_actions(legal_actions: list[dict[str, Any]]) -> str

      Format legal actions as a readable string.


      .. autolink-examples:: _format_legal_actions
         :collapse:


   .. py:method:: _get_fallback_action(legal_actions)

      Get a fallback action when decision fails.


      .. autolink-examples:: _get_fallback_action
         :collapse:


   .. py:method:: _get_legal_actions(state: haive.games.poker.state.PokerState, player: haive.games.poker.models.Player) -> list[dict[str, Any]]

      Get legal actions for a player with enhanced error handling.


      .. autolink-examples:: _get_legal_actions
         :collapse:


   .. py:method:: _get_next_player_idx(game: haive.games.poker.state.PokerState) -> int

      Get the index of the next active player.


      .. autolink-examples:: _get_next_player_idx
         :collapse:


   .. py:method:: _get_player_decision_with_retry(runnable, messages, context, legal_actions, max_retries=3)

      Get player decision with retry logic for handling invalid outputs.


      .. autolink-examples:: _get_player_decision_with_retry
         :collapse:


   .. py:method:: _get_player_name(player_id: str) -> str

      Get player name from ID, with format 'P1' if not found.


      .. autolink-examples:: _get_player_name
         :collapse:


   .. py:method:: _is_valid_decision(decision, legal_actions)

      Check if a decision is valid given the legal actions.


      .. autolink-examples:: _is_valid_decision
         :collapse:


   .. py:method:: _prepare_decision_context(state: haive.games.poker.state.PokerState, player_idx: int, legal_actions: list[dict[str, Any]]) -> dict[str, Any]

      Prepare the context for decision-making.


      .. autolink-examples:: _prepare_decision_context
         :collapse:


   .. py:method:: _save_game_history(state: haive.games.poker.state.PokerState)

      Save the current game state and history to disk.


      .. autolink-examples:: _save_game_history
         :collapse:


   .. py:method:: _setup_agent_runnables() -> None

      Set up LLM runnables for all players with improved error handling.


      .. autolink-examples:: _setup_agent_runnables
         :collapse:


   .. py:method:: _update_player_stats(player_id: str, action: haive.games.poker.models.PlayerAction, amount: int)

      Update player statistics based on their decision.


      .. autolink-examples:: _update_player_stats
         :collapse:


   .. py:method:: end_game(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

      End the poker game and determine final results.


      .. autolink-examples:: end_game
         :collapse:


   .. py:method:: end_hand(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

      Handle the end of a hand - determine winner(s) and update stats.


      .. autolink-examples:: end_hand
         :collapse:


   .. py:method:: handle_player_decision(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

      Enhanced player decision handling with improved error recovery.

      This method:
      1. Determines the current player
      2. Calculates legal actions
      3. Gets decision from the player agent
      4. Validates and applies the decision
      5. Updates game state



      .. autolink-examples:: handle_player_decision
         :collapse:


   .. py:method:: initialize_game(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

      Initialize the poker game state with enhanced logging.


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: setup_hand(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

      Set up a new poker hand with enhanced error handling and debugging.


      .. autolink-examples:: setup_hand
         :collapse:


   .. py:method:: setup_workflow()

      Set up the poker game workflow graph with enhanced error handling.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_continue_round(state: haive.games.poker.state.PokerState) -> str

      Determine if we should continue the current betting round.


      .. autolink-examples:: should_continue_round
         :collapse:


   .. py:method:: should_continue_to_next_phase(state: haive.games.poker.state.PokerState) -> str

      Determine if the game should advance to the next phase.


      .. autolink-examples:: should_continue_to_next_phase
         :collapse:


   .. py:method:: should_play_another_hand(state: haive.games.poker.state.PokerState) -> bool

      Determine if another hand should be played.


      .. autolink-examples:: should_play_another_hand
         :collapse:


   .. py:method:: update_game_phase(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

      Update the game phase and handle phase transitions.


      .. autolink-examples:: update_game_phase
         :collapse:


   .. py:attribute:: hand_analyzer
      :value: None



   .. py:attribute:: hands_played
      :value: 0



   .. py:attribute:: player_agents


   .. py:attribute:: player_stats


   .. py:attribute:: retry_history


   .. py:attribute:: state_manager


.. py:class:: RetryConfiguration

   Configuration for retry policies.


   .. autolink-examples:: RetryConfiguration
      :collapse:

   .. py:attribute:: BACKOFF_FACTOR
      :value: 1.5



   .. py:attribute:: MAX_RETRIES
      :value: 3



   .. py:attribute:: RETRY_DELAY
      :value: 1.5



.. py:data:: logger

