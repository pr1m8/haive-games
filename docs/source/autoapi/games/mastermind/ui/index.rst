games.mastermind.ui
===================

.. py:module:: games.mastermind.ui

Rich UI for the Mastermind game.

This module provides a rich terminal UI for the Mastermind game using the Rich library.
It displays the game board, guesses, feedback, and analysis in a visually appealing way.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Rich UI for the Mastermind game.

   This module provides a rich terminal UI for the Mastermind game using the Rich library.
   It displays the game board, guesses, feedback, and analysis in a visually appealing way.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mastermind.ui.MastermindUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MastermindUI(console: rich.console.Console | None = None)

            Rich terminal UI for the Mastermind game.

            This class provides methods for displaying the Mastermind game state in a visually
            appealing way using the Rich library.


            Initialize the UI with a Rich console.

            :param console: Optional Rich console to use. If not provided, a new one is created.


            .. py:method:: color_to_styled_text(color: str) -> rich.text.Text

               Convert a color name to a styled text object.

               :param color: The name of the color.

               :returns: A Rich Text object with appropriate styling for the color.



            .. py:method:: create_analysis_panel(state: haive.games.mastermind.state.MastermindState) -> rich.panel.Panel | None

               Create a panel with the most recent analysis if available.

               :param state: The current game state.

               :returns: A Rich Panel object containing analysis information, or None if no analysis available.



            .. py:method:: create_guesses_table(state: haive.games.mastermind.state.MastermindState) -> rich.table.Table

               Create a table displaying all guesses and their feedback.

               :param state: The current game state.

               :returns: A Rich Table object containing the guesses and feedback.



            .. py:method:: create_info_panel(state: haive.games.mastermind.state.MastermindState) -> rich.panel.Panel

               Create a panel with game information.

               :param state: The current game state.

               :returns: A Rich Panel object containing game information.



            .. py:method:: create_layout(state: haive.games.mastermind.state.MastermindState) -> rich.layout.Layout

               Create a complete layout for the game state.

               :param state: The current game state.

               :returns: A Rich Layout object containing all game UI components.



            .. py:method:: display_final_results(state: haive.games.mastermind.state.MastermindState)

               Display the final results of the game.

               :param state: The final game state.



            .. py:method:: display_game_state(state: haive.games.mastermind.state.MastermindState)

               Display the current game state.

               :param state: The current game state.



            .. py:method:: display_welcome()

               Display a welcome message for the Mastermind game.



            .. py:method:: extract_game_state(state_dict: dict[str, Any]) -> haive.games.mastermind.state.MastermindState | None

               Extract a MastermindState from a state dictionary.

               :param state_dict: The state dictionary to convert.

               :returns: A MastermindState object, or None if conversion fails.



            .. py:method:: print_debug_info(data: Any, label: str = 'Debug')

               Print debug information.

               :param data: The data to print.
               :param label: A label for the debug panel.



            .. py:attribute:: COLOR_EMOJIS


            .. py:attribute:: COLOR_STYLES


            .. py:attribute:: console





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mastermind.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

