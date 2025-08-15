games.hold_em.state_manager
===========================

.. py:module:: games.hold_em.state_manager

.. autoapi-nested-parse::

   Texas Hold'em game state management module.

   This module provides a dedicated state manager for Texas Hold'em poker games,
   offering static methods for state manipulation, including:
       - Creating and initializing game states
       - Advancing game phases
       - Applying player actions
       - Handling betting rounds
       - Managing pot and chip distribution
       - Tracking hand history

   The state manager serves as a central interface for manipulating the game state
   in a consistent manner, separating state manipulation logic from the game agent.

   .. rubric:: Example

   >>> from haive.games.hold_em.state_manager import HoldemGameStateManager
   >>> from haive.games.hold_em.state import HoldemState, PlayerState
   >>>
   >>> # Create player states
   >>> players = [
   >>>     PlayerState(player_id="p1", name="Alice", chips=1000, position=0),
   >>>     PlayerState(player_id="p2", name="Bob", chips=1000, position=1),
   >>> ]
   >>>
   >>> # Initialize a new game state
   >>> state = HoldemGameStateManager.create_initial_state(
   >>>     players=players,
   >>>     small_blind=10,
   >>>     big_blind=20
   >>> )
   >>>
   >>> # Advance the game to the next phase
   >>> updated_state = HoldemGameStateManager.advance_phase(state)


   .. autolink-examples:: games.hold_em.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.hold_em.state_manager.HoldemGameStateManager


Module Contents
---------------

.. py:class:: HoldemGameStateManager

   State manager for Texas Hold'em poker games.

   This class provides static methods for manipulating the game state, separating state
   logic from the game agent. It handles state transitions, player actions, and game
   flow management in a functional manner.

   All methods are static and take a state object as input, returning a new state
   object with the requested changes applied, following an immutable approach to state
   management.



   .. autolink-examples:: HoldemGameStateManager
      :collapse:

   .. py:method:: _apply_bet_raise(player: haive.games.hold_em.state.PlayerState, state: haive.games.hold_em.state.HoldemState, bet_amount: int) -> None
      :staticmethod:


      Apply a bet or raise action.


      .. autolink-examples:: _apply_bet_raise
         :collapse:


   .. py:method:: _apply_call(player: haive.games.hold_em.state.PlayerState, state: haive.games.hold_em.state.HoldemState, call_amount: int) -> None
      :staticmethod:


      Apply a call action.


      .. autolink-examples:: _apply_call
         :collapse:


   .. py:method:: _get_next_player_index(state: haive.games.hold_em.state.HoldemState) -> int | None
      :staticmethod:


      Get the index of the next player to act.


      .. autolink-examples:: _get_next_player_index
         :collapse:


   .. py:method:: _set_player_positions(state: haive.games.hold_em.state.HoldemState, dealer_pos: int) -> None
      :staticmethod:


      Set player positions for the hand.


      .. autolink-examples:: _set_player_positions
         :collapse:


   .. py:method:: advance_phase(state: haive.games.hold_em.state.HoldemState) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Advance the game to the next phase based on current phase.

      :param state: Current game state

      :returns: Updated state in the next game phase


      .. autolink-examples:: advance_phase
         :collapse:


   .. py:method:: apply_player_action(state: haive.games.hold_em.state.HoldemState, player_index: int, action: str, amount: int = 0) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Apply a player's action to the game state.

      :param state: Current game state
      :param player_index: Index of the player taking the action
      :param action: Action to take (fold, check, call, bet, raise, all_in)
      :param amount: Amount for bet/raise (if applicable)

      :returns: Updated state with the action applied


      .. autolink-examples:: apply_player_action
         :collapse:


   .. py:method:: award_pot(state: haive.games.hold_em.state.HoldemState) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Award the pot to the winner and record hand history.

      :param state: Current game state

      :returns: Updated state with pot awarded and hand recorded


      .. autolink-examples:: award_pot
         :collapse:


   .. py:method:: check_game_end(state: haive.games.hold_em.state.HoldemState) -> tuple[haive.games.hold_em.state.HoldemState, bool]
      :staticmethod:


      Check if the game should end.

      :param state: Current game state

      :returns: Tuple of (updated state, game_over flag)


      .. autolink-examples:: check_game_end
         :collapse:


   .. py:method:: create_initial_state(players: list[haive.games.hold_em.state.PlayerState], small_blind: int = 10, big_blind: int = 20, starting_chips: int = 1000, game_id: str | None = None) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Create an initial game state for a new poker game.

      :param players: List of player states
      :param small_blind: Small blind amount
      :param big_blind: Big blind amount
      :param starting_chips: Starting chips for each player
      :param game_id: Optional game identifier (generated if not provided)

      :returns: A new HoldemState instance ready for the first hand


      .. autolink-examples:: create_initial_state
         :collapse:


   .. py:method:: deal_community_cards(state: haive.games.hold_em.state.HoldemState, num_cards: int, phase: haive.games.hold_em.state.GamePhase) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Deal community cards (flop, turn, or river).

      :param state: Current game state
      :param num_cards: Number of cards to deal
      :param phase: New game phase

      :returns: Updated state with community cards dealt


      .. autolink-examples:: deal_community_cards
         :collapse:


   .. py:method:: deal_hole_cards(state: haive.games.hold_em.state.HoldemState) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Deal two hole cards to each active player.

      :param state: Current game state

      :returns: Updated state with hole cards dealt


      .. autolink-examples:: deal_hole_cards
         :collapse:


   .. py:method:: evaluate_showdown(state: haive.games.hold_em.state.HoldemState) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Evaluate player hands at showdown and determine winner.

      :param state: Current game state

      :returns: Updated state with winner determined


      .. autolink-examples:: evaluate_showdown
         :collapse:


   .. py:method:: post_blinds(state: haive.games.hold_em.state.HoldemState) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Post small and big blinds to start the betting.

      :param state: Current game state

      :returns: Updated state with blinds posted


      .. autolink-examples:: post_blinds
         :collapse:


   .. py:method:: setup_new_hand(state: haive.games.hold_em.state.HoldemState) -> haive.games.hold_em.state.HoldemState
      :staticmethod:


      Set up a new poker hand with shuffled deck and reset player states.

      :param state: Current game state

      :returns: Updated state with new hand setup


      .. autolink-examples:: setup_new_hand
         :collapse:


