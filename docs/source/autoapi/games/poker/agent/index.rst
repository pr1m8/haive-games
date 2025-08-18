games.poker.agent
=================

.. py:module:: games.poker.agent

Enhanced Texas Hold'em Poker agent implementation.

This module implements a robust poker agent with improved:
- Structured output handling with proper schema validation
- Comprehensive logging and debugging
- Error handling and retry policies for invalid moves
- Enhanced prompts for LLM decisions



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Enhanced Texas Hold'em Poker agent implementation.

   This module implements a robust poker agent with improved:
   - Structured output handling with proper schema validation
   - Comprehensive logging and debugging
   - Error handling and retry policies for invalid moves
   - Enhanced prompts for LLM decisions



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.poker.agent.logger

            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.poker.agent.PokerAgent
      games.poker.agent.RetryConfiguration

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerAgent(config: haive.games.poker.config.PokerAgentConfig = PokerAgentConfig())

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.poker.config.PokerAgentConfig`\ ]


            Enhanced agent class for managing a multi-player Texas Hold'em poker game.

            Key improvements:
            - Proper structured output handling
            - Comprehensive debug logging
            - Retry policies for failed operations
            - Enhanced prompts and decision handling


            Initialize the enhanced poker agent.


            .. py:method:: _apply_player_decision(game: haive.games.poker.state.PokerState, player: haive.games.poker.models.Player, decision: haive.games.poker.models.AgentDecision, legal_actions: list[dict[str, Any]])

               Apply the player's decision to the game state.



            .. py:method:: _format_legal_actions(legal_actions: list[dict[str, Any]]) -> str

               Format legal actions as a readable string.



            .. py:method:: _get_fallback_action(legal_actions)

               Get a fallback action when decision fails.



            .. py:method:: _get_legal_actions(state: haive.games.poker.state.PokerState, player: haive.games.poker.models.Player) -> list[dict[str, Any]]

               Get legal actions for a player with enhanced error handling.



            .. py:method:: _get_next_player_idx(game: haive.games.poker.state.PokerState) -> int

               Get the index of the next active player.



            .. py:method:: _get_player_decision_with_retry(runnable, messages, context, legal_actions, max_retries=3)

               Get player decision with retry logic for handling invalid outputs.



            .. py:method:: _get_player_name(player_id: str) -> str

               Get player name from ID, with format 'P1' if not found.



            .. py:method:: _is_valid_decision(decision, legal_actions)

               Check if a decision is valid given the legal actions.



            .. py:method:: _prepare_decision_context(state: haive.games.poker.state.PokerState, player_idx: int, legal_actions: list[dict[str, Any]]) -> dict[str, Any]

               Prepare the context for decision-making.



            .. py:method:: _save_game_history(state: haive.games.poker.state.PokerState)

               Save the current game state and history to disk.



            .. py:method:: _setup_agent_runnables() -> None

               Set up LLM runnables for all players with improved error handling.



            .. py:method:: _update_player_stats(player_id: str, action: haive.games.poker.models.PlayerAction, amount: int)

               Update player statistics based on their decision.



            .. py:method:: end_game(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

               End the poker game and determine final results.



            .. py:method:: end_hand(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

               Handle the end of a hand - determine winner(s) and update stats.



            .. py:method:: handle_player_decision(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

               Enhanced player decision handling with improved error recovery.

               This method:
               1. Determines the current player
               2. Calculates legal actions
               3. Gets decision from the player agent
               4. Validates and applies the decision
               5. Updates game state




            .. py:method:: initialize_game(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

               Initialize the poker game state with enhanced logging.



            .. py:method:: setup_hand(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

               Set up a new poker hand with enhanced error handling and debugging.



            .. py:method:: setup_workflow()

               Set up the poker game workflow graph with enhanced error handling.



            .. py:method:: should_continue_round(state: haive.games.poker.state.PokerState) -> str

               Determine if we should continue the current betting round.



            .. py:method:: should_continue_to_next_phase(state: haive.games.poker.state.PokerState) -> str

               Determine if the game should advance to the next phase.



            .. py:method:: should_play_another_hand(state: haive.games.poker.state.PokerState) -> bool

               Determine if another hand should be played.



            .. py:method:: update_game_phase(state: haive.games.poker.state.PokerState) -> haive.games.poker.state.PokerState

               Update the game phase and handle phase transitions.



            .. py:attribute:: hand_analyzer
               :value: None



            .. py:attribute:: hands_played
               :value: 0



            .. py:attribute:: player_agents


            .. py:attribute:: player_stats


            .. py:attribute:: retry_history


            .. py:attribute:: state_manager



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RetryConfiguration

            Configuration for retry policies.


            .. py:attribute:: BACKOFF_FACTOR
               :value: 1.5



            .. py:attribute:: MAX_RETRIES
               :value: 3



            .. py:attribute:: RETRY_DELAY
               :value: 1.5




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.poker.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

