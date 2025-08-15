games.chess.ui
==============

.. py:module:: games.chess.ui

.. autoapi-nested-parse::

   Chess game UI using Rich for beautiful terminal display.


   .. autolink-examples:: games.chess.ui
      :collapse:


Classes
-------

.. autoapisummary::

   games.chess.ui.ChessRichUI


Functions
---------

.. autoapisummary::

   games.chess.ui.main


Module Contents
---------------

.. py:class:: ChessRichUI

   Beautiful Rich UI for displaying a live chess agent game.


   .. autolink-examples:: ChessRichUI
      :collapse:

   .. py:method:: _create_score_bar(score: float) -> rich.text.Text

      Create a visual score bar.


      .. autolink-examples:: _create_score_bar
         :collapse:


   .. py:method:: _setup_layout()

      Initialize the layout structure.


      .. autolink-examples:: _setup_layout
         :collapse:


   .. py:method:: _update_layout()

      Update all layout components with current state.


      .. autolink-examples:: _update_layout
         :collapse:


   .. py:method:: render_analysis(color: str) -> rich.panel.Panel

      Render position analysis for a player.


      .. autolink-examples:: render_analysis
         :collapse:


   .. py:method:: render_board() -> rich.panel.Panel

      Render the chess board with pieces.


      .. autolink-examples:: render_board
         :collapse:


   .. py:method:: render_current_move() -> rich.panel.Panel

      Render the current move being made.


      .. autolink-examples:: render_current_move
         :collapse:


   .. py:method:: render_footer() -> rich.panel.Panel

      Render the footer with controls and status.


      .. autolink-examples:: render_footer
         :collapse:


   .. py:method:: render_game_info() -> rich.panel.Panel

      Render game information and statistics.


      .. autolink-examples:: render_game_info
         :collapse:


   .. py:method:: render_header() -> rich.panel.Panel

      Render the header with title and game time.


      .. autolink-examples:: render_header
         :collapse:


   .. py:method:: render_move_history() -> rich.panel.Panel

      Render the move history.


      .. autolink-examples:: render_move_history
         :collapse:


   .. py:method:: render_player_info(color: str) -> rich.panel.Panel

      Render player information panel.


      .. autolink-examples:: render_player_info
         :collapse:


   .. py:method:: run(agent: haive.games.chess.agent.ChessAgent, delay: float = 0.5)

      Run the live UI with the chess agent.

      :param agent: The chess agent to run
      :param delay: Minimum delay between UI updates (seconds)


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: console


   .. py:attribute:: last_move
      :type:  str | None
      :value: None



   .. py:attribute:: layout


   .. py:attribute:: move_count
      :value: 0



   .. py:attribute:: start_time


   .. py:attribute:: state
      :type:  haive.games.chess.state.ChessState | None
      :value: None



.. py:function:: main()

   Run a chess game with the Rich UI.


   .. autolink-examples:: main
      :collapse:

