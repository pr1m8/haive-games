games.single_player.wordle.state_manager
========================================

.. py:module:: games.single_player.wordle.state_manager


Classes
-------

.. autoapisummary::

   games.single_player.wordle.state_manager.WordConnectionsStateManager


Module Contents
---------------

.. py:class:: WordConnectionsStateManager

   Bases: :py:obj:`haive.games.framework.base.GameStateManager`\ [\ :py:obj:`haive.games.single_player.wordle.models.WordConnectionsState`\ ]


   Manager for Word Connections game state.


   .. autolink-examples:: WordConnectionsStateManager
      :collapse:

   .. py:method:: apply_move(state: haive.games.single_player.wordle.models.WordConnectionsState, move: haive.games.single_player.wordle.models.WordConnectionsMove) -> haive.games.single_player.wordle.models.WordConnectionsState
      :classmethod:


      Apply a move to the game state.

      :param state: Current game state
      :param move: Move to apply

      :returns: Updated game state


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.single_player.wordle.models.WordConnectionsState) -> haive.games.single_player.wordle.models.WordConnectionsState
      :classmethod:


      Check and update game status.

      :param state: Current game state

      :returns: Updated game state


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_hint(state: haive.games.single_player.wordle.models.WordConnectionsState) -> str
      :classmethod:


      Get a hint for the current state.

      :param state: Current game state

      :returns: Hint string


      .. autolink-examples:: get_hint
         :collapse:


   .. py:method:: initialize(puzzle_index: int | None = None, **kwargs) -> haive.games.single_player.wordle.models.WordConnectionsState
      :classmethod:


      Initialize a new Word Connections game.

      :param puzzle_index: Optional index of puzzle to use (0 = most recent)
      :param \*\*kwargs: Additional options

      :returns: Initialized game state


      .. autolink-examples:: initialize
         :collapse:


   .. py:attribute:: NYT_PUZZLES


