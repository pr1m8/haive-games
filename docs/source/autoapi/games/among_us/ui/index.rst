games.among_us.ui
=================

.. py:module:: games.among_us.ui


Classes
-------

.. autoapisummary::

   games.among_us.ui.AmongUsUI


Module Contents
---------------

.. py:class:: AmongUsUI(console: rich.console.Console | None = None)

   Rich UI implementation for the Among Us game.

   This class provides a visually appealing and informative interface for displaying
   game state and player information.


   Initialize the UI with an optional custom console.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: AmongUsUI
      :collapse:

   .. py:method:: _create_footer(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

      Create the footer with game status and instructions.


      .. autolink-examples:: _create_footer
         :collapse:


   .. py:method:: _create_header(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

      Create the game header.


      .. autolink-examples:: _create_header
         :collapse:


   .. py:method:: _create_map_view(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

      Create the map visualization.


      .. autolink-examples:: _create_map_view
         :collapse:


   .. py:method:: _create_player_list(layout_section, state: haive.games.among_us.state.AmongUsState, current_player: str | None = None)

      Create the player list section.


      .. autolink-examples:: _create_player_list
         :collapse:


   .. py:method:: _create_stats_view(layout_section, state: haive.games.among_us.state.AmongUsState)

      Create the game statistics section.


      .. autolink-examples:: _create_stats_view
         :collapse:


   .. py:method:: _get_task_completion_percentage(state: haive.games.among_us.state.AmongUsState) -> float

      Calculate task completion percentage.


      .. autolink-examples:: _get_task_completion_percentage
         :collapse:


   .. py:method:: _group_locations(locations: list[str]) -> list[list[str]]

      Group locations into rows for better display.


      .. autolink-examples:: _group_locations
         :collapse:


   .. py:method:: create_live_display(state: haive.games.among_us.state.AmongUsState, current_player: str | None = None) -> rich.live.Live

      Create a live display for the game that can be updated.


      .. autolink-examples:: create_live_display
         :collapse:


   .. py:method:: display_game(state: haive.games.among_us.state.AmongUsState, current_player: str | None = None) -> rich.layout.Layout

      Display the full game state.

      :param state: Current game state
      :param current_player: Optional player to highlight as currently active

      :returns: The complete layout object, which can be used in a Live display


      .. autolink-examples:: display_game
         :collapse:


   .. py:method:: display_game_over(state: haive.games.among_us.state.AmongUsState) -> rich.panel.Panel

      Display the game over screen.

      :param state: Final game state

      :returns: A panel showing the game results


      .. autolink-examples:: display_game_over
         :collapse:


   .. py:method:: display_meeting_view(state: haive.games.among_us.state.AmongUsState) -> rich.layout.Layout

      Display the meeting screen.

      :param state: Current game state

      :returns: A layout representing the meeting


      .. autolink-examples:: display_meeting_view
         :collapse:


   .. py:method:: display_player_view(state: haive.games.among_us.state.AmongUsState, player_id: str) -> rich.panel.Panel

      Display a detailed view for a specific player.

      :param state: Current game state
      :param player_id: Player to display

      :returns: A panel containing the player view


      .. autolink-examples:: display_player_view
         :collapse:


   .. py:attribute:: BOX_STYLES


   .. py:attribute:: COLORS


   .. py:attribute:: console


