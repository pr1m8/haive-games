games.monopoly.main_agent
=========================

.. py:module:: games.monopoly.main_agent

Fixed Main Monopoly agent that orchestrates the complete game.

This module provides the corrected main agent implementation that:
    - Ensures BaseModel consistency throughout (no dict conversions)
    - Properly handles state schema compatibility
    - Fixes the validation error by maintaining BaseModel state



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Fixed Main Monopoly agent that orchestrates the complete game.

   This module provides the corrected main agent implementation that:
       - Ensures BaseModel consistency throughout (no dict conversions)
       - Properly handles state schema compatibility
       - Fixes the validation error by maintaining BaseModel state



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.monopoly.main_agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.monopoly.main_agent.MonopolyAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MonopolyAgent(config: haive.games.monopoly.game_agent.MonopolyGameAgentConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.monopoly.game_agent.MonopolyGameAgentConfig`\ ]


            Main Monopoly agent that orchestrates the complete game.

            This agent combines:
                - Game rule enforcement and turn management
                - Player decision delegation to subgraphs
                - Complete game state management
                - Game end detection and winner determination


            Initialize the monopoly agent.


            .. py:method:: _display_final_results(final_state: haive.games.monopoly.state.MonopolyState) -> None

               Display final game results.



            .. py:method:: get_game_summary() -> dict[str, Any]

               Get a summary of the game configuration and status.



            .. py:method:: save_game_history(filename: str | None = None) -> None

               Save game history to a file.



            .. py:method:: setup_workflow() -> None

               Set up the complete monopoly workflow.

               This creates the main game workflow nodes and connects them properly.




            .. py:method:: start_game() -> haive.games.monopoly.state.MonopolyState

               Start a new monopoly game.

               CRITICAL: Keep everything as BaseModel - no dict conversions!

               :returns: Final game state as MonopolyState BaseModel



            .. py:attribute:: initial_state


            .. py:attribute:: player_agent



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.main_agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

