games.chess.example_configurable_players
========================================

.. py:module:: games.chess.example_configurable_players

Example of using configurable chess players.

This example demonstrates how to create chess games with different LLM configurations
for players without hardcoding them.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">8 functions</span>   </div>

.. autoapi-nested-parse::

   Example of using configurable chess players.

   This example demonstrates how to create chess games with different LLM configurations
   for players without hardcoding them.



      
            
            
            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.chess.example_configurable_players.example_1_simple_models
      games.chess.example_configurable_players.example_2_canonical_strings
      games.chess.example_configurable_players.example_3_example_configs
      games.chess.example_configurable_players.example_4_custom_player_configs
      games.chess.example_configurable_players.example_5_budget_friendly
      games.chess.example_configurable_players.example_6_same_model
      games.chess.example_configurable_players.main
      games.chess.example_configurable_players.run_short_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_1_simple_models()

            Example 1: Simple model strings.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_2_canonical_strings()

            Example 2: Canonical model strings with providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_3_example_configs()

            Example 3: Using predefined example configurations.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_4_custom_player_configs()

            Example 4: Custom player agent configurations.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_5_budget_friendly()

            Example 5: Budget-friendly configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_6_same_model()

            Example 6: Using the same model for all roles.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run all examples.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_short_game(config: haive.games.chess.configurable_config.ConfigurableChessConfig, max_moves: int = 10)
            :async:


            Run a short chess game to test the configuration.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.example_configurable_players import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

