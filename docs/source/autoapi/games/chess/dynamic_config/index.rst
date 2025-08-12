
:py:mod:`games.chess.dynamic_config`
====================================

.. py:module:: games.chess.dynamic_config

Dynamic configuration for chess game.

This module provides a flexible configuration system for chess that supports:
- Legacy hardcoded engines (backward compatibility)
- Simple model string configuration
- Example-based configuration
- Advanced PlayerAgentConfig configuration


.. autolink-examples:: games.chess.dynamic_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.dynamic_config.ChessConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ChessConfig {
        node [shape=record];
        "ChessConfig" [label="ChessConfig"];
        "haive.games.core.config.BaseGameConfig" -> "ChessConfig";
      }

.. autoclass:: games.chess.dynamic_config.ChessConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.chess.dynamic_config.budget_chess
   games.chess.dynamic_config.competitive_chess
   games.chess.dynamic_config.create_chess_config
   games.chess.dynamic_config.create_chess_config_from_example
   games.chess.dynamic_config.create_chess_config_with_players
   games.chess.dynamic_config.create_legacy_chess_config
   games.chess.dynamic_config.experimental_chess

.. py:function:: budget_chess(**kwargs) -> ChessConfig

   Create a budget-friendly chess configuration.


   .. autolink-examples:: budget_chess
      :collapse:

.. py:function:: competitive_chess(**kwargs) -> ChessConfig

   Create a competitive chess configuration with top models.


   .. autolink-examples:: competitive_chess
      :collapse:

.. py:function:: create_chess_config(white_model: str = 'gpt-4o', black_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ChessConfig

   Create a chess configuration with simple model strings.

   :param white_model: Model for white player
   :param black_model: Model for black player
   :param \*\*kwargs: Additional configuration parameters

   :returns: ChessConfig instance

   .. rubric:: Example

   >>> config = create_chess_config("gpt-4", "claude-3-opus")
   >>> config = create_chess_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet",
   ...     temperature=0.8
   ... )


   .. autolink-examples:: create_chess_config
      :collapse:

.. py:function:: create_chess_config_from_example(example_name: str, **kwargs) -> ChessConfig

   Create a chess configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional parameters to override

   :returns: ChessConfig instance

   Available examples:
       - "gpt_vs_claude": GPT-4 vs Claude
       - "anthropic_vs_openai": Claude vs GPT showdown
       - "gpt_only": GPT-4 for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different providers

   .. rubric:: Example

   >>> config = create_chess_config_from_example("budget")
   >>> config = create_chess_config_from_example("gpt_vs_claude", max_moves=150)


   .. autolink-examples:: create_chess_config_from_example
      :collapse:

.. py:function:: create_chess_config_with_players(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ChessConfig

   Create a chess configuration with detailed player configs.

   :param player_configs: Dictionary mapping role names to PlayerAgentConfig
   :param \*\*kwargs: Additional configuration parameters

   :returns: ChessConfig instance

   Expected roles:
       - "white_player": White player configuration
       - "black_player": Black player configuration
       - "white_analyzer": White analyzer configuration (optional)
       - "black_analyzer": Black analyzer configuration (optional)

   .. rubric:: Example

   >>> player_configs = {
   ...     "white_player": PlayerAgentConfig(
   ...         llm_config="gpt-4",
   ...         temperature=0.7,
   ...         player_name="Aggressive White"
   ...     ),
   ...     "black_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Defensive Black"
   ...     )
   ... }
   >>> config = create_chess_config_with_players(player_configs)


   .. autolink-examples:: create_chess_config_with_players
      :collapse:

.. py:function:: create_legacy_chess_config(**kwargs) -> ChessConfig

   Create a chess configuration using legacy hardcoded engines.

   This is for backward compatibility with existing code.

   :param \*\*kwargs: Additional configuration parameters

   :returns: ChessConfig instance with hardcoded engines


   .. autolink-examples:: create_legacy_chess_config
      :collapse:

.. py:function:: experimental_chess(**kwargs) -> ChessConfig

   Create an experimental chess configuration with mixed providers.


   .. autolink-examples:: experimental_chess
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.chess.dynamic_config
   :collapse:
   
.. autolink-skip:: next
