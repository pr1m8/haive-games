games.single_player.towers_of_hanoi.ui
======================================

.. py:module:: games.single_player.towers_of_hanoi.ui

Module documentation for games.single_player.towers_of_hanoi.ui


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.single_player.towers_of_hanoi.ui.console

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.towers_of_hanoi.ui.HanoiUI

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.single_player.towers_of_hanoi.ui.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HanoiUI

            Rich UI for Tower of Hanoi game.


            .. py:method:: ai_move()

               Let AI make a move.



            .. py:method:: auto_play(live)

               Auto-play to completion.



            .. py:method:: create_display() -> rich.panel.Panel

               Create the game display.



            .. py:method:: format_moves() -> str

               Format recent moves for display.



            .. py:method:: manual_move()

               Allow manual move input.



            .. py:method:: play_game()

               Main game loop.



            .. py:method:: run()

               Run the interactive UI.



            .. py:attribute:: agent
               :type:  haive.games.single_player.towers_of_hanoi.agent.HanoiAgent | None
               :value: None



            .. py:attribute:: game
               :type:  haive.games.single_player.towers_of_hanoi.game.HanoiGame | None
               :value: None



            .. py:attribute:: state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run the Tower of Hanoi UI.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: console




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.towers_of_hanoi.ui import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

