games.fox_and_geese.ui
======================

.. py:module:: games.fox_and_geese.ui

Rich UI module for Fox and Geese game visualization.

This module provides rich console UI components for visualizing the Fox and Geese game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Rich UI module for Fox and Geese game visualization.

   This module provides rich console UI components for visualizing the Fox and Geese game.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.fox_and_geese.ui.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.fox_and_geese.ui.FoxAndGeeseUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FoxAndGeeseUI(console: rich.console.Console | None = None)

            Rich UI for Fox and Geese game visualization.

            Initialize the UI.

            :param console: Optional Rich console instance


            .. py:method:: _is_valid_game_state_dict(data: dict) -> bool

               Check if a dict contains the required fields for FoxAndGeeseState.

               :param data: Dictionary to check

               :returns: True if the dict appears to be a valid game state



            .. py:method:: create_analysis_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

               Create a panel showing the latest analysis.

               :param game_state: Current game state

               :returns: Rich panel with analysis info



            .. py:method:: create_board_table(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.table.Table

               Create a rich visual representation of the board.

               :param game_state: Current game state

               :returns: Rich table representing the board



            .. py:method:: create_game_info_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

               Create a panel with game information.

               :param game_state: Current game state

               :returns: Rich panel with game info



            .. py:method:: create_last_move_panel(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.panel.Panel

               Create a panel showing the last move.

               :param game_state: Current game state

               :returns: Rich panel with last move info



            .. py:method:: create_layout(game_state: haive.games.fox_and_geese.state.FoxAndGeeseState) -> rich.layout.Layout

               Create the complete rich UI layout.

               :param game_state: Current game state

               :returns: Complete rich layout



            .. py:method:: display_final_results(final_state: Any) -> None

               Display final game results.

               :param final_state: Final game state



            .. py:method:: display_state(state_data: Any) -> bool

               Display the game state using rich UI.

               :param state_data: State data in various formats

               :returns: True if display was successful, False otherwise



            .. py:method:: display_welcome() -> None

               Display welcome message.



            .. py:method:: extract_game_state(state_data: Any) -> haive.games.fox_and_geese.state.FoxAndGeeseState | None

               Extract FoxAndGeeseState from various input formats.

               :param state_data: State data in various formats

               :returns: FoxAndGeeseState instance or None if extraction fails



            .. py:method:: print_debug_info(state_data: Any, context: str = '') -> None

               Print debug information about the state.

               :param state_data: State data to debug
               :param context: Context string for debugging



            .. py:attribute:: console



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.fox_and_geese.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

