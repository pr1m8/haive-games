games.single_player.example
===========================

.. py:module:: games.single_player.example

Module documentation for games.single_player.example


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span>   </div>


      
            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.single_player.example.run_auto_game
      games.single_player.example.run_interactive_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_auto_game(agent: SinglePlayerGameAgent)

            Run a fully automated single-player game.

            :param agent: The game agent



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_interactive_game(agent: SinglePlayerGameAgent, commands: list[str] = None)

            Run an interactive single-player game.

            :param agent: The game agent
            :param commands: Optional list of commands to execute (for testing)





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

