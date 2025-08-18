games.clue.runner
=================

.. py:module:: games.clue.runner

Runner script for the Clue game.

This script demonstrates how to initialize and run a Clue game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span>   </div>

.. autoapi-nested-parse::

   Runner script for the Clue game.

   This script demonstrates how to initialize and run a Clue game.



      
            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.clue.runner.main
      games.clue.runner.run_clue_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()
            :async:


            Run the Clue game as a demonstration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_clue_game(player_names: list[str], max_turns: int = 20, num_ai_players: int = 0) -> dict[str, Any]
            :async:


            Run a complete Clue game with the specified players.

            :param player_names: Names of the players
            :param max_turns: Maximum number of turns
            :param num_ai_players: Number of AI players (the first n players will be AI)

            :returns: Final game state information





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.runner import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

