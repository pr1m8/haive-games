games.tic_tac_toe.ui
====================

.. py:module:: games.tic_tac_toe.ui

.. autoapi-nested-parse::

   Rich UI Game Runner for Tic Tac Toe.

   This module provides a beautiful, interactive UI for running Tic Tac Toe games using the
   Rich library for enhanced terminal displays.


   .. autolink-examples:: games.tic_tac_toe.ui
      :collapse:


Classes
-------

.. autoapisummary::

   games.tic_tac_toe.ui.RichTicTacToeRunner


Module Contents
---------------

.. py:class:: RichTicTacToeRunner(agent: haive.games.tic_tac_toe.agent.TicTacToeAgent)

   Rich UI runner for Tic Tac Toe games.

   Initialize the Rich UI runner.

   :param agent: The TicTacToe agent to run


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RichTicTacToeRunner
      :collapse:

   .. py:method:: create_analysis_panel(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.panel.Panel | None

      Create a panel showing the latest analysis.

      :param state: Current game state

      :returns: Rich Panel with analysis info, or None if no analysis


      .. autolink-examples:: create_analysis_panel
         :collapse:


   .. py:method:: create_board_panel(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.panel.Panel

      Create a rich panel displaying the game board.

      :param state: Current game state

      :returns: Rich Panel with the game board


      .. autolink-examples:: create_board_panel
         :collapse:


   .. py:method:: create_game_info_panel(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.panel.Panel

      Create a panel with game information.

      :param state: Current game state

      :returns: Rich Panel with game info


      .. autolink-examples:: create_game_info_panel
         :collapse:


   .. py:method:: create_layout(state: haive.games.tic_tac_toe.state.TicTacToeState) -> rich.layout.Layout

      Create the main layout for the game display.

      :param state: Current game state

      :returns: Rich Layout object


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: run_game(show_thinking: bool = True, step_delay: float = 1.0, debug: bool = False) -> dict[str, Any]

      Run the Tic Tac Toe game with Rich UI.

      :param show_thinking: Whether to show thinking animations
      :param step_delay: Delay between moves in seconds
      :param debug: Whether to show debug information

      :returns: Final game state


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: show_game_summary(final_state: dict[str, Any])

      Show a summary of the completed game.

      :param final_state: The final state of the game


      .. autolink-examples:: show_game_summary
         :collapse:


   .. py:method:: show_thinking_animation(player: str, duration: float = 2.0)

      Show a thinking animation while AI is processing.

      :param player: The player who is thinking
      :param duration: How long to show the animation


      .. autolink-examples:: show_thinking_animation
         :collapse:


   .. py:attribute:: agent


   .. py:attribute:: console


   .. py:attribute:: current_state
      :type:  haive.games.tic_tac_toe.state.TicTacToeState | None
      :value: None



