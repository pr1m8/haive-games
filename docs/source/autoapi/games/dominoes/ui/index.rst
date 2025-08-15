games.dominoes.ui
=================

.. py:module:: games.dominoes.ui

.. autoapi-nested-parse::

   Rich UI module for Dominoes game visualization.

   This module provides rich console UI components for visualizing the Dominoes game.


   .. autolink-examples:: games.dominoes.ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.dominoes.ui.logger


Classes
-------

.. autoapisummary::

   games.dominoes.ui.DominoesUI


Module Contents
---------------

.. py:class:: DominoesUI(console: rich.console.Console | None = None)

   Rich UI for Dominoes game visualization.

   Initialize the UI.

   :param console: Optional Rich console instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DominoesUI
      :collapse:

   .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

      Check if a dict contains the required fields for DominoesState.

      :param data: Dictionary to check

      :returns: True if the dict appears to be a valid game state


      .. autolink-examples:: _is_valid_game_state_dict
         :collapse:


   .. py:method:: create_analysis_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a panel showing the latest analysis.

      :param game_state: Current game state

      :returns: Rich panel with analysis info


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_board_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a visual representation of the dominoes board.

      :param game_state: Current game state

      :returns: Rich panel representing the board


      .. autolink-examples:: create_board_panel
         :collapse:


   .. py:method:: create_game_info_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a panel with game information.

      :param game_state: Current game state

      :returns: Rich panel with game info


      .. autolink-examples:: create_game_info_panel
         :collapse:


   .. py:method:: create_last_move_panel(game_state: haive.games.dominoes.state.DominoesState) -> rich.panel.Panel

      Create a panel showing the last move.

      :param game_state: Current game state

      :returns: Rich panel with last move info


      .. autolink-examples:: create_last_move_panel
         :collapse:


   .. py:method:: create_layout(game_state: haive.games.dominoes.state.DominoesState) -> rich.layout.Layout

      Create the complete rich UI layout.

      :param game_state: Current game state

      :returns: Complete rich layout


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: create_player_hand_panel(game_state: haive.games.dominoes.state.DominoesState, player: str) -> rich.panel.Panel

      Create a panel showing a player's hand.

      :param game_state: Current game state
      :param player: Player whose hand to display

      :returns: Rich panel with player's hand


      .. autolink-examples:: create_player_hand_panel
         :collapse:


   .. py:method:: display_final_results(final_state: Any) -> None

      Display final game results.

      :param final_state: Final game state


      .. autolink-examples:: display_final_results
         :collapse:


   .. py:method:: display_state(state_data: Any) -> bool

      Display the game state using rich UI.

      :param state_data: State data in various formats

      :returns: True if display was successful, False otherwise


      .. autolink-examples:: display_state
         :collapse:


   .. py:method:: display_welcome() -> None

      Display welcome message.


      .. autolink-examples:: display_welcome
         :collapse:


   .. py:method:: extract_game_state(state_data: Any) -> haive.games.dominoes.state.DominoesState | None

      Extract DominoesState from various input formats.

      :param state_data: State data in various formats

      :returns: DominoesState instance or None if extraction fails


      .. autolink-examples:: extract_game_state
         :collapse:


   .. py:method:: print_debug_info(state_data: Any, context: str = '') -> None

      Print debug information about the state.

      :param state_data: State data to debug
      :param context: Context string for debugging


      .. autolink-examples:: print_debug_info
         :collapse:


   .. py:attribute:: console


.. py:data:: logger

