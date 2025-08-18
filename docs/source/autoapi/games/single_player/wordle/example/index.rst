games.single_player.wordle.example
==================================

.. py:module:: games.single_player.wordle.example

Example Word Connections game with interactive UI.

Uses the May 22, 2025 puzzle (#711).



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Example Word Connections game with interactive UI.

   Uses the May 22, 2025 puzzle (#711).



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.wordle.example.WordConnectionsUI

            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.single_player.wordle.example.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsUI

            Interactive UI for Word Connections game.


            .. py:method:: display_grid(state: haive.games.single_player.wordle.models.WordConnectionsState)

               Display the game grid in a nice format.



            .. py:method:: display_solution(state: haive.games.single_player.wordle.models.WordConnectionsState)

               Display the full solution.



            .. py:method:: play_game()
               :async:


               Play the game with AI assistance.



            .. py:attribute:: agent


            .. py:attribute:: config


            .. py:attribute:: state
               :type:  haive.games.single_player.wordle.models.WordConnectionsState | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()
            :async:


            Run the example game.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.wordle.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

