games.mafia.state_manager
=========================

.. py:module:: games.mafia.state_manager

.. autoapi-nested-parse::

   State management for the Mafia game.

   This module provides the core state management functionality for the Mafia game,
   handling game state transitions, move validation, and game progression logic.

   The state manager is responsible for:
       - Game initialization and setup
       - Phase transitions (day/night cycles)
       - Move validation and application
       - Game state filtering for information hiding
       - Win condition checking


   .. autolink-examples:: games.mafia.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.mafia.state_manager.MafiaStateManager


Module Contents
---------------

.. py:class:: MafiaStateManager

   Bases: :py:obj:`haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager`\ [\ :py:obj:`haive.games.mafia.state.MafiaGameState`\ ]


   Manager for the Mafia game state.

   This class extends MultiPlayerGameStateManager to provide Mafia-specific
   state management functionality. It handles game progression, move validation,
   and state transitions.

   The manager maintains game state including:
       - Player roles and alive/dead status
       - Day/night cycle progression
       - Vote tracking and resolution
       - Night action resolution (kills, saves, investigations)
       - Win condition checking

   .. note::

      This class is designed to be used statically, with all methods being
      class methods that take and return game states.


   .. autolink-examples:: MafiaStateManager
      :collapse:

   .. py:method:: advance_phase(state: haive.games.mafia.state.MafiaGameState) -> haive.games.mafia.state.MafiaGameState
      :classmethod:


      Advance the game to the next phase.

      This method handles the transition between game phases, including:
          - Setup → Night (first night)
          - Night → Day Discussion (with night action resolution)
          - Day Discussion → Day Voting
          - Day Voting → Night (with vote resolution)
          - Game Over checks at appropriate points

      :param state: Current game state

      :returns: Updated game state with new phase and relevant changes


      .. autolink-examples:: advance_phase
         :collapse:


   .. py:method:: apply_move(state: haive.games.mafia.state.MafiaGameState, player_id: str, move: haive.games.mafia.models.MafiaAction | haive.games.mafia.models.NarratorAction) -> haive.games.mafia.state.MafiaGameState
      :classmethod:


      Apply a move to the game state.

      This method validates and applies a player's move or narrator's action
      to the game state, updating all relevant state fields.

      :param state: Current game state
      :param player_id: ID of the player making the move
      :param move: Move to apply

      :returns: Updated game state after applying the move


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.mafia.state.MafiaGameState) -> haive.games.mafia.state.MafiaGameState
      :classmethod:


      Check if the game has ended and determine the winner.

      This method checks win conditions:
          - Village wins if all mafia are dead
          - Mafia wins if they equal/outnumber villagers

      :param state: Current game state

      :returns: Updated state with game status and winner if game is over


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: filter_state_for_player(state: haive.games.mafia.state.MafiaGameState, player_id: str) -> dict[str, Any]
      :classmethod:


      Filter the state to include only information visible to a specific player.

      This method implements information hiding, ensuring players only see
      information they should have access to based on their role and the
      game phase.

      :param state: Full game state
      :param player_id: ID of the player to filter for

      :returns: Filtered state containing only visible information


      .. autolink-examples:: filter_state_for_player
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.mafia.state.MafiaGameState, player_id: str) -> list[haive.games.mafia.models.MafiaAction | haive.games.mafia.models.NarratorAction]
      :classmethod:


      Get legal moves for a specific player.

      This method determines what moves are legal for a player based on:
          - Current game phase
          - Player's role
          - Player's alive/dead status
          - Previous actions in the current phase

      :param state: Current game state
      :param player_id: ID of the player to get moves for

      :returns: List of legal moves (MafiaAction or NarratorAction)


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: handle_phase_transition(state: haive.games.mafia.state.MafiaGameState) -> haive.games.mafia.state.MafiaGameState
      :classmethod:


      Handle phase transition with error handling.

      This method safely transitions the game phase, handling any errors
      that might occur during the transition.

      :param state: Current game state

      :returns: Updated state after phase transition

      :raises ValueError: If critical game state fields are missing


      .. autolink-examples:: handle_phase_transition
         :collapse:


   .. py:method:: initialize(player_names: list[str], **kwargs) -> haive.games.mafia.state.MafiaGameState
      :classmethod:


      Initialize a new Mafia game with the given players.

      This method sets up a new game state with:
          - Random role assignment
          - Initial player states
          - Game phase setup
          - Role knowledge distribution

      :param player_names: List of player names/IDs
      :param \*\*kwargs: Additional configuration options
                         include_all_roles: Force inclusion of all special roles

      :returns: Initial game state

      :raises ValueError: If there aren't enough players (minimum 4)


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: resolve_night_actions(state: haive.games.mafia.state.MafiaGameState) -> haive.games.mafia.state.MafiaGameState
      :classmethod:


      Resolve night actions and determine outcomes.

      This method processes all night actions in the correct order:
          1. Mafia kill attempt
          2. Doctor save attempt
          3. Detective investigation results

      :param state: Current game state with night actions recorded

      :returns: Updated state with night actions resolved


      .. autolink-examples:: resolve_night_actions
         :collapse:


