games.mastermind.ui
===================

.. py:module:: games.mastermind.ui

.. autoapi-nested-parse::

   Rich UI for the Mastermind game.

   This module provides a rich terminal UI for the Mastermind game using the Rich library.
   It displays the game board, guesses, feedback, and analysis in a visually appealing way.


   .. autolink-examples:: games.mastermind.ui
      :collapse:


Classes
-------

.. autoapisummary::

   games.mastermind.ui.MastermindUI


Module Contents
---------------

.. py:class:: MastermindUI(console: rich.console.Console | None = None)

   Rich terminal UI for the Mastermind game.

   This class provides methods for displaying the Mastermind game state in a visually
   appealing way using the Rich library.


   Initialize the UI with a Rich console.

   :param console: Optional Rich console to use. If not provided, a new one is created.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MastermindUI
      :collapse:

   .. py:method:: color_to_styled_text(color: str) -> rich.text.Text

      Convert a color name to a styled text object.

      :param color: The name of the color.

      :returns: A Rich Text object with appropriate styling for the color.


      .. autolink-examples:: color_to_styled_text
         :collapse:


   .. py:method:: create_analysis_panel(state: haive.games.mastermind.state.MastermindState) -> rich.panel.Panel | None

      Create a panel with the most recent analysis if available.

      :param state: The current game state.

      :returns: A Rich Panel object containing analysis information, or None if no analysis available.


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_guesses_table(state: haive.games.mastermind.state.MastermindState) -> rich.table.Table

      Create a table displaying all guesses and their feedback.

      :param state: The current game state.

      :returns: A Rich Table object containing the guesses and feedback.


      .. autolink-examples:: create_guesses_table
         :collapse:


   .. py:method:: create_info_panel(state: haive.games.mastermind.state.MastermindState) -> rich.panel.Panel

      Create a panel with game information.

      :param state: The current game state.

      :returns: A Rich Panel object containing game information.


      .. autolink-examples:: create_info_panel
         :collapse:


   .. py:method:: create_layout(state: haive.games.mastermind.state.MastermindState) -> rich.layout.Layout

      Create a complete layout for the game state.

      :param state: The current game state.

      :returns: A Rich Layout object containing all game UI components.


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: display_final_results(state: haive.games.mastermind.state.MastermindState)

      Display the final results of the game.

      :param state: The final game state.


      .. autolink-examples:: display_final_results
         :collapse:


   .. py:method:: display_game_state(state: haive.games.mastermind.state.MastermindState)

      Display the current game state.

      :param state: The current game state.


      .. autolink-examples:: display_game_state
         :collapse:


   .. py:method:: display_welcome()

      Display a welcome message for the Mastermind game.


      .. autolink-examples:: display_welcome
         :collapse:


   .. py:method:: extract_game_state(state_dict: dict[str, Any]) -> haive.games.mastermind.state.MastermindState | None

      Extract a MastermindState from a state dictionary.

      :param state_dict: The state dictionary to convert.

      :returns: A MastermindState object, or None if conversion fails.


      .. autolink-examples:: extract_game_state
         :collapse:


   .. py:method:: print_debug_info(data: Any, label: str = 'Debug')

      Print debug information.

      :param data: The data to print.
      :param label: A label for the debug panel.


      .. autolink-examples:: print_debug_info
         :collapse:


   .. py:attribute:: COLOR_EMOJIS


   .. py:attribute:: COLOR_STYLES


   .. py:attribute:: console


