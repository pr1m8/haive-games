games.poker.ui
==============

.. py:module:: games.poker.ui


Classes
-------

.. autoapisummary::

   games.poker.ui.PokerUI


Module Contents
---------------

.. py:class:: PokerUI

   Clean, readable UI for the poker game simulation.


   .. autolink-examples:: PokerUI
      :collapse:

   .. py:method:: _format_card(card)

      Format a card with unicode symbols.


      .. autolink-examples:: _format_card
         :collapse:


   .. py:method:: _get_position_name(position, num_players)

      Get the poker position name.


      .. autolink-examples:: _get_position_name
         :collapse:


   .. py:method:: _setup_layout()

      Set up the UI layout with clean, simple sections.


      .. autolink-examples:: _setup_layout
         :collapse:


   .. py:method:: assign_ai_models(player_names)

      Assign consistent AI models to players.


      .. autolink-examples:: assign_ai_models
         :collapse:


   .. py:method:: render_action_history()

      Render clean action history.


      .. autolink-examples:: render_action_history
         :collapse:


   .. py:method:: render_active_player()

      Render active player information.


      .. autolink-examples:: render_active_player
         :collapse:


   .. py:method:: render_footer()

      Render a simple footer with controls.


      .. autolink-examples:: render_footer
         :collapse:


   .. py:method:: render_game_info()

      Render clean game info panel.


      .. autolink-examples:: render_game_info
         :collapse:


   .. py:method:: render_header()

      Render a clean header with title.


      .. autolink-examples:: render_header
         :collapse:


   .. py:method:: render_players()

      Render players table with clear information.


      .. autolink-examples:: render_players
         :collapse:


   .. py:method:: render_table()

      Render poker table with community cards.


      .. autolink-examples:: render_table
         :collapse:


   .. py:attribute:: animation_frame
      :value: 0



   .. py:attribute:: current_game_state
      :value: None



   .. py:attribute:: layout


   .. py:attribute:: player_models


