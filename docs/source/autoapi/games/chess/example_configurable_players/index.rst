games.chess.example_configurable_players
========================================

.. py:module:: games.chess.example_configurable_players

.. autoapi-nested-parse::

   Example of using configurable chess players.

   This example demonstrates how to create chess games with different LLM configurations
   for players without hardcoding them.



Functions
---------

.. autoapisummary::

   games.chess.example_configurable_players.example_1_simple_models
   games.chess.example_configurable_players.example_2_canonical_strings
   games.chess.example_configurable_players.example_3_example_configs
   games.chess.example_configurable_players.example_4_custom_player_configs
   games.chess.example_configurable_players.example_5_budget_friendly
   games.chess.example_configurable_players.example_6_same_model
   games.chess.example_configurable_players.main
   games.chess.example_configurable_players.run_short_game


Module Contents
---------------

.. py:function:: example_1_simple_models()

   Example 1: Simple model strings.


.. py:function:: example_2_canonical_strings()

   Example 2: Canonical model strings with providers.


.. py:function:: example_3_example_configs()

   Example 3: Using predefined example configurations.


.. py:function:: example_4_custom_player_configs()

   Example 4: Custom player agent configurations.


.. py:function:: example_5_budget_friendly()

   Example 5: Budget-friendly configuration.


.. py:function:: example_6_same_model()

   Example 6: Using the same model for all roles.


.. py:function:: main()

   Run all examples.


.. py:function:: run_short_game(config: haive.games.chess.configurable_config.ConfigurableChessConfig, max_moves: int = 10)
   :async:


   Run a short chess game to test the configuration.


