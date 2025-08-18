games.chess.dynamic_config
==========================

.. py:module:: games.chess.dynamic_config

Dynamic configuration for chess game.

This module provides a flexible configuration system for chess that supports:
- Legacy hardcoded engines (backward compatibility)
- Simple model string configuration
- Example-based configuration
- Advanced PlayerAgentConfig configuration



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">7 functions</span>   </div>

.. autoapi-nested-parse::

   Dynamic configuration for chess game.

   This module provides a flexible configuration system for chess that supports:
   - Legacy hardcoded engines (backward compatibility)
   - Simple model string configuration
   - Example-based configuration
   - Advanced PlayerAgentConfig configuration



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.dynamic_config.ChessConfig

            

.. admonition:: Functions (7)
   :class: info

   .. autoapisummary::

      games.chess.dynamic_config.budget_chess
      games.chess.dynamic_config.competitive_chess
      games.chess.dynamic_config.create_chess_config
      games.chess.dynamic_config.create_chess_config_from_example
      games.chess.dynamic_config.create_chess_config_with_players
      games.chess.dynamic_config.create_legacy_chess_config
      games.chess.dynamic_config.experimental_chess

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessConfig

            Bases: :py:obj:`haive.games.core.config.BaseGameConfig`


            Dynamic configuration for chess game.

            This configuration supports multiple modes:
            1. Legacy: Use hardcoded engines from engines.py
            2. Simple: Specify models as strings (white_model, black_model)
            3. Example: Use predefined configurations (e.g., "gpt_vs_claude")
            4. Advanced: Full PlayerAgentConfig specifications

            .. attribute:: white_model

               Model for white player (simple mode)

            .. attribute:: black_model

               Model for black player (simple mode)

            .. attribute:: white_player_name

               Display name for white player

            .. attribute:: black_player_name

               Display name for black player

            .. attribute:: max_moves

               Maximum moves before draw (default: 200)

            .. attribute:: enable_fen_visualization

               Show FEN strings in analysis


            .. py:method:: build_legacy_engines() -> list[Any]

               Build legacy hardcoded engines.



            .. py:method:: create_engines_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> list[Any]

               Create engines from player configurations.



            .. py:method:: create_simple_player_configs() -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

               Create player configs from simple model strings.



            .. py:method:: get_example_configs() -> dict[str, dict[str, Any]]

               Define example chess configurations.



            .. py:method:: get_role_definitions() -> dict[str, haive.games.core.config.GamePlayerRole]

               Define chess player roles.



            .. py:attribute:: black_model
               :type:  str | None
               :value: None



            .. py:attribute:: black_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: enable_fen_visualization
               :type:  bool
               :value: None



            .. py:attribute:: max_moves
               :type:  int
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: recursion_limit
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.chess.state.ChessState]
               :value: None



            .. py:attribute:: white_model
               :type:  str | None
               :value: None



            .. py:attribute:: white_player_name
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: budget_chess(**kwargs) -> ChessConfig

            Create a budget-friendly chess configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: competitive_chess(**kwargs) -> ChessConfig

            Create a competitive chess configuration with top models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_legacy_chess_config(**kwargs) -> ChessConfig

            Create a chess configuration using legacy hardcoded engines.

            This is for backward compatibility with existing code.

            :param \*\*kwargs: Additional configuration parameters

            :returns: ChessConfig instance with hardcoded engines



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: experimental_chess(**kwargs) -> ChessConfig

            Create an experimental chess configuration with mixed providers.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.dynamic_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

