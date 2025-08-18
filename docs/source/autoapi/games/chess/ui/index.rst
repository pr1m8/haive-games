games.chess.ui
==============

.. py:module:: games.chess.ui

Chess game UI using Rich for beautiful terminal display.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Chess game UI using Rich for beautiful terminal display.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.ui.ChessRichUI

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.chess.ui.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessRichUI

            Beautiful Rich UI for displaying a live chess agent game.


            .. py:method:: _create_score_bar(score: float) -> rich.text.Text

               Create a visual score bar.



            .. py:method:: _setup_layout()

               Initialize the layout structure.



            .. py:method:: _update_layout()

               Update all layout components with current state.



            .. py:method:: render_analysis(color: str) -> rich.panel.Panel

               Render position analysis for a player.



            .. py:method:: render_board() -> rich.panel.Panel

               Render the chess board with pieces.



            .. py:method:: render_current_move() -> rich.panel.Panel

               Render the current move being made.



            .. py:method:: render_footer() -> rich.panel.Panel

               Render the footer with controls and status.



            .. py:method:: render_game_info() -> rich.panel.Panel

               Render game information and statistics.



            .. py:method:: render_header() -> rich.panel.Panel

               Render the header with title and game time.



            .. py:method:: render_move_history() -> rich.panel.Panel

               Render the move history.



            .. py:method:: render_player_info(color: str) -> rich.panel.Panel

               Render player information panel.



            .. py:method:: run(agent: haive.games.chess.agent.ChessAgent, delay: float = 0.5)

               Run the live UI with the chess agent.

               :param agent: The chess agent to run
               :param delay: Minimum delay between UI updates (seconds)



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run a chess game with the Rich UI.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

