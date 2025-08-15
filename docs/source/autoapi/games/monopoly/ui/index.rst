games.monopoly.ui
=================

.. py:module:: games.monopoly.ui

.. autoapi-nested-parse::

   Rich UI for displaying a live Monopoly game with proper error handling.

   This module provides a beautiful terminal interface for watching Monopoly games unfold
   in real-time using Rich, with fixes for the validation error.


   .. autolink-examples:: games.monopoly.ui
      :collapse:


Classes
-------

.. autoapisummary::

   games.monopoly.ui.MonopolyRichUI


Functions
---------

.. autoapisummary::

   games.monopoly.ui.main


Module Contents
---------------

.. py:class:: MonopolyRichUI

   Beautiful Rich UI for displaying a live Monopoly game.


   .. autolink-examples:: MonopolyRichUI
      :collapse:

   .. py:method:: _get_player_color(player_name: str) -> str

      Get color for a player based on their name.


      .. autolink-examples:: _get_player_color
         :collapse:


   .. py:method:: _get_position_name(position: int) -> str

      Get the name of a board position.


      .. autolink-examples:: _get_position_name
         :collapse:


   .. py:method:: _setup_layout()

      Initialize the layout structure.


      .. autolink-examples:: _setup_layout
         :collapse:


   .. py:method:: _update_layout()

      Update all layout components with current state.


      .. autolink-examples:: _update_layout
         :collapse:


   .. py:method:: render_board() -> rich.panel.Panel

      Render a simplified board view.


      .. autolink-examples:: render_board
         :collapse:


   .. py:method:: render_current_player() -> rich.panel.Panel

      Render current player information.


      .. autolink-examples:: render_current_player
         :collapse:


   .. py:method:: render_footer() -> rich.panel.Panel

      Render the footer with controls and game info.


      .. autolink-examples:: render_footer
         :collapse:


   .. py:method:: render_header() -> rich.panel.Panel

      Render the game header.


      .. autolink-examples:: render_header
         :collapse:


   .. py:method:: render_players() -> rich.panel.Panel

      Render all players summary.


      .. autolink-examples:: render_players
         :collapse:


   .. py:method:: render_recent_events() -> rich.panel.Panel

      Render recent game events.


      .. autolink-examples:: render_recent_events
         :collapse:


   .. py:method:: run(agent: haive.games.monopoly.main_agent.MonopolyAgent, delay: float = 2.0)

      Run the live UI with the Monopoly agent.

      :param agent: The Monopoly agent to run
      :param delay: Delay between updates for readability


      .. autolink-examples:: run
         :collapse:


   .. py:attribute:: console


   .. py:attribute:: layout


   .. py:attribute:: state
      :type:  haive.games.monopoly.state.MonopolyState | None
      :value: None



.. py:function:: main()

   Run a Monopoly game with the Rich UI.


   .. autolink-examples:: main
      :collapse:

