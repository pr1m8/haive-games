games.clue.state_manager
========================

.. py:module:: games.clue.state_manager

.. autoapi-nested-parse::

   State manager for the Clue game.

   This module defines the state management for the Clue game, providing methods for game
   logic and state transitions.


   .. autolink-examples:: games.clue.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.clue.state_manager.ClueStateManager


Module Contents
---------------

.. py:class:: ClueStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.clue.state.ClueState`\ ]


   Manager for Clue game state.


   .. autolink-examples:: ClueStateManager
      :collapse:

   .. py:method:: add_analysis(state: haive.games.clue.state.ClueState, player: str, hypothesis: dict[str, Any]) -> haive.games.clue.state.ClueState
      :classmethod:


      Add a hypothesis to the state.

      :param state: Current game state
      :param player: Player performing the analysis
      :param hypothesis: Hypothesis details

      :returns: Updated state with added hypothesis


      .. autolink-examples:: add_analysis
         :collapse:


   .. py:method:: apply_move(state: haive.games.clue.state.ClueState, move: haive.games.clue.models.ClueGuess) -> haive.games.clue.state.ClueState
      :classmethod:


      Apply a guess to the current state.

      :param state: Current game state
      :param move: The guess to apply

      :returns: Updated game state


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.clue.state.ClueState) -> haive.games.clue.state.ClueState
      :classmethod:


      Check and potentially update game status.

      :param state: Current game state

      :returns: Updated game state


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.clue.state.ClueState) -> list[haive.games.clue.models.ClueGuess]
      :classmethod:


      Get all legal moves for the current state.

      :param state: The current game state

      :returns: List of possible legal guesses


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: get_possible_solutions(state: haive.games.clue.state.ClueState) -> set[tuple[str, str, str]]
      :classmethod:


      Get possible solutions based on the current game state.

      :param state: Current game state

      :returns: Set of possible solutions as (suspect, weapon, room) tuples


      .. autolink-examples:: get_possible_solutions
         :collapse:


   .. py:method:: get_winner(state: haive.games.clue.state.ClueState) -> str | None
      :classmethod:


      Get the winner of the game.

      :param state: Current game state

      :returns: Winner of the game, or None if ongoing


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: initialize(**kwargs) -> haive.games.clue.state.ClueState
      :classmethod:


      Initialize a new Clue game.

      :param \*\*kwargs: Keyword arguments for game initialization

      :returns: A new Clue game state
      :rtype: ClueState


      .. autolink-examples:: initialize
         :collapse:


