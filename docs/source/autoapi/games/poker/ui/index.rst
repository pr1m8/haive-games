games.poker.ui
==============

.. py:module:: games.poker.ui

Module documentation for games.poker.ui


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.poker.ui.PokerUI

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerUI

            Clean, readable UI for the poker game simulation.


            .. py:method:: _format_card(card)

               Format a card with unicode symbols.



            .. py:method:: _get_position_name(position, num_players)

               Get the poker position name.



            .. py:method:: _setup_layout()

               Set up the UI layout with clean, simple sections.



            .. py:method:: assign_ai_models(player_names)

               Assign consistent AI models to players.



            .. py:method:: render_action_history()

               Render clean action history.



            .. py:method:: render_active_player()

               Render active player information.



            .. py:method:: render_footer()

               Render a simple footer with controls.



            .. py:method:: render_game_info()

               Render clean game info panel.



            .. py:method:: render_header()

               Render a clean header with title.



            .. py:method:: render_players()

               Render players table with clear information.



            .. py:method:: render_table()

               Render poker table with community cards.



            .. py:attribute:: animation_frame
               :value: 0



            .. py:attribute:: current_game_state
               :value: None



            .. py:attribute:: layout


            .. py:attribute:: player_models





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.poker.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

