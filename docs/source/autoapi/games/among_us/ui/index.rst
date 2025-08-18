games.among_us.ui
=================

.. py:module:: games.among_us.ui

Module documentation for games.among_us.ui


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.among_us.ui.AmongUsUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsUI(console: rich.console.Console | None = None)

            Rich UI implementation for the Among Us game.

            This class provides a visually appealing and informative interface for displaying
            game state and player information.


            Initialize the UI with an optional custom console.


            .. py:method:: _create_footer(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

               Create the footer with game status and instructions.



            .. py:method:: _create_header(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

               Create the game header.



            .. py:method:: _create_map_view(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

               Create the map visualization.



            .. py:method:: _create_player_list(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

               Create the player list section.



            .. py:method:: _create_stats_view(layout_section, state: haive.games.among_us.state.AmongUsState)

               Create the game statistics section.



            .. py:method:: _get_task_completion_percentage(state: haive.games.among_us.state.AmongUsState) -> float

               Calculate task completion percentage.



            .. py:method:: _group_locations(locations: list[str]) -> list[list[str]]

               Group locations into rows for better display.



            .. py:method:: create_live_display(state: haive.games.among_us.state.AmongUsState, current_player: str | None = None) -> rich.live.Live

               Create a live display for the game that can be updated.



            .. py:method:: display_game(state: haive.games.among_us.state.AmongUsState, current_player: str | None = None) -> rich.layout.Layout

               Display the full game state.

               :param state: Current game state
               :param current_player: Optional player to highlight as currently active

               :returns: The complete layout object, which can be used in a Live display



            .. py:method:: display_game_over(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

               Display the game over screen.

               :param state: Final game state

               :returns: A panel showing the game results



            .. py:method:: display_meeting_view(state: haive.games.among_us.state.AmongUsState) -> rich.layout.Layout

               Display the meeting screen.

               :param state: Current game state

               :returns: A layout representing the meeting



            .. py:method:: display_player_view(state: haive.games.among_us.state.AmongUsState, player_id: str) -> rich.panel.Panel

               Display a detailed view for a specific player.

               :param state: Current game state
               :param player_id: Player to display

               :returns: A panel containing the player view



            .. py:attribute:: BOX_STYLES


            .. py:attribute:: COLORS


            .. py:attribute:: console





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

