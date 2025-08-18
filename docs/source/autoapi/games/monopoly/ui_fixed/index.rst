games.monopoly.ui_fixed
=======================

.. py:module:: games.monopoly.ui_fixed

Rich UI for displaying a live Monopoly game.

This module provides a beautiful terminal interface for watching Monopoly games unfold
in real-time using Rich.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Rich UI for displaying a live Monopoly game.

   This module provides a beautiful terminal interface for watching Monopoly games unfold
   in real-time using Rich.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.monopoly.ui_fixed.MonopolyRichUI

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.monopoly.ui_fixed.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyRichUI

            Beautiful Rich UI for displaying a live Monopoly game.


            .. py:method:: _get_player_color(player_name: str) -> str

               Get color for a player based on their name.



            .. py:method:: _get_position_name(position: int) -> str

               Get the name of a board position.



            .. py:method:: _setup_layout()

               Initialize the layout structure.



            .. py:method:: _update_layout()

               Update all layout components with current state.



            .. py:method:: render_board() -> rich.panel.Panel

               Render a simplified board view.



            .. py:method:: render_current_player() -> rich.panel.Panel

               Render current player information.



            .. py:method:: render_footer() -> rich.panel.Panel

               Render the footer with controls and game info.



            .. py:method:: render_header() -> rich.panel.Panel

               Render the game header.



            .. py:method:: render_players() -> rich.panel.Panel

               Render all players summary.



            .. py:method:: render_recent_events() -> rich.panel.Panel

               Render recent game events.



            .. py:method:: run(agent: haive.games.monopoly.main_agent.MonopolyAgent, delay: float = 2.0)

               Run the live UI with the Monopoly agent.

               :param agent: The Monopoly agent to run
               :param delay: Delay between updates for readability



            .. py:attribute:: console


            .. py:attribute:: layout


            .. py:attribute:: state
               :type:  haive.games.monopoly.state.MonopolyState | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run a Monopoly game with the Rich UI.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.ui_fixed import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

