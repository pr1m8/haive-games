games.fox_and_geese.ui
======================

.. py:module:: games.fox_and_geese.ui

.. autoapi-nested-parse::

   Rich UI module for Fox and Geese game visualization.

   This module provides rich console UI components for visualizing the Fox and Geese game.


   .. autolink-examples:: games.fox_and_geese.ui
      :collapse:


Attributes
----------

.. autoapisummary::

   games.fox_and_geese.ui.logger


Classes
-------

.. autoapisummary::

   games.fox_and_geese.ui.FoxAndGeeseUI


Module Contents
---------------

.. py:class:: FoxAndGeeseUI(console: rich.console.Console | None = None)

   Rich UI for Fox and Geese game visualization.

   Initialize the UI.

   :param console: Optional Rich console instance


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FoxAndGeeseUI
      :collapse:

   .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

      Check if a dict contains the required fields for FoxAndGeeseState.

      :param data: Dictionary to check

      :returns: True if the dict appears to be a valid game state


      .. autolink-examples:: _is_valid_game_state_dict
         :collapse:


   .. py:method:: create_analysis_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

      Create a panel showing the latest analysis.

      :param game_state: Current game state

      :returns: Rich panel with analysis info


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_board_table(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.table.Table

      Create a rich visual representation of the board.

      :param game_state: Current game state

      :returns: Rich table representing the board


      .. autolink-examples:: create_board_table
         :collapse:


   .. py:method:: create_game_info_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

      Create a panel with game information.

      :param game_state: Current game state

      :returns: Rich panel with game info


      .. autolink-examples:: create_game_info_panel
         :collapse:


   .. py:method:: create_last_move_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

      Create a panel showing the last move.

      :param game_state: Current game state

      :returns: Rich panel with last move info


      .. autolink-examples:: create_last_move_panel
         :collapse:


   .. py:method:: create_layout(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.layout.Layout

      Create the complete rich UI layout.

      :param game_state: Current game state

      :returns: Complete rich layout


      .. autolink-examples:: create_layout
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


   .. py:method:: extract_game_state(state_data: Any) -> haive.games.fox_and_geese.state.FoxAndGeeseState | None

      Extract FoxAndGeeseState from various input formats.

      :param state_data: State data in various formats

      :returns: FoxAndGeeseState instance or None if extraction fails


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

