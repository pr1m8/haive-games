games.tic_tac_toe.ui
====================

.. py:module:: games.tic_tac_toe.ui

Rich UI Game Runner for Tic Tac Toe.

This module provides a beautiful, interactive UI for running Tic Tac Toe games using the
Rich library for enhanced terminal displays.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Rich UI Game Runner for Tic Tac Toe.

   This module provides a beautiful, interactive UI for running Tic Tac Toe games using the
   Rich library for enhanced terminal displays.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.tic_tac_toe.ui.RichTicTacToeRunner

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RichTicTacToeRunner(agent: haive.games.tic_tac_toe.agent.TicTacToeAgent)

            Rich UI runner for Tic Tac Toe games.

            Initialize the Rich UI runner.

            :param agent: The TicTacToe agent to run


            .. py:method:: create_analysis_panel(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.panel.Panel | None

               Create a panel showing the latest analysis.

               :param state: Current game state

               :returns: Rich Panel with analysis info, or None if no analysis



            .. py:method:: create_board_panel(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.panel.Panel

               Create a rich panel displaying the game board.

               :param state: Current game state

               :returns: Rich Panel with the game board



            .. py:method:: create_game_info_panel(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.panel.Panel

               Create a panel with game information.

               :param state: Current game state

               :returns: Rich Panel with game info



            .. py:method:: create_layout(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.layout.Layout

               Create the main layout for the game display.

               :param state: Current game state

               :returns: Rich Layout object



            .. py:method:: run_game(show_thinking: bool = True, step_delay: float = 1.0, debug: bool = False) -> dict[str, Any]

               Run the Tic Tac Toe game with Rich UI.

               :param show_thinking: Whether to show thinking animations
               :param step_delay: Delay between moves in seconds
               :param debug: Whether to show debug information

               :returns: Final game state



            .. py:method:: show_game_summary(final_state: dict[str, Any])

               Show a summary of the completed game.

               :param final_state: The final state of the game



            .. py:method:: show_thinking_animation(player: str, duration: float = 2.0)

               Show a thinking animation while AI is processing.

               :param player: The player who is thinking
               :param duration: How long to show the animation



            .. py:attribute:: agent


            .. py:attribute:: console


            .. py:attribute:: current_state
               :type:  haive.games.tic_tac_toe.state.TicTacToeState | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.tic_tac_toe.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

