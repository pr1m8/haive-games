games.dominoes.state_manager
============================

.. py:module:: games.dominoes.state_manager


Attributes
----------

.. autoapisummary::

   games.dominoes.state_manager.logger


Classes
-------

.. autoapisummary::

   games.dominoes.state_manager.DominoesStateManager


Module Contents
---------------

.. py:class:: DominoesStateManager

   Bases: :py:obj:`haive.games.framework.base.GameStateManager`\ [\ :py:obj:`haive.games.dominoes.state.DominoesState`\ ]


   Manager for dominoes game state.


   .. autolink-examples:: DominoesStateManager
      :collapse:

   .. py:method:: apply_move(state: haive.games.dominoes.state.DominoesState, move: haive.games.dominoes.models.DominoMove | Literal['pass']) -> haive.games.dominoes.state.DominoesState
      :classmethod:


      Apply a move to the dominoes state.


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.dominoes.state.DominoesState) -> haive.games.dominoes.state.DominoesState
      :classmethod:


      Check and update the game status.


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.dominoes.state.DominoesState) -> list[haive.games.dominoes.models.DominoMove | Literal['pass']]
      :classmethod:


      Get all legal moves for the current player.


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize(player_names: list[str] = None, tiles_per_hand: int = 7) -> haive.games.dominoes.state.DominoesState
      :classmethod:


      Initialize a new dominoes game.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: update_analysis(state: haive.games.dominoes.state.DominoesState, analysis: Any, player: str) -> haive.games.dominoes.state.DominoesState
      :classmethod:


      Update state with analysis.

      :param state: Current game state
      :param analysis: Analysis to add
      :param player: Player who made the analysis

      :returns: Updated game state with analysis


      .. autolink-examples:: update_analysis
         :collapse:


.. py:data:: logger

