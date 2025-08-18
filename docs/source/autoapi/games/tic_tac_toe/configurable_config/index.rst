games.tic_tac_toe.configurable_config
=====================================

.. py:module:: games.tic_tac_toe.configurable_config

Configurable Tic-Tac-Toe configuration using the generic player agent system.

This module provides configurable Tic-Tac-Toe game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">8 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Configurable Tic-Tac-Toe configuration using the generic player agent system.

   This module provides configurable Tic-Tac-Toe game configurations that replace hardcoded
   LLM settings with dynamic, configurable player agents.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.tic_tac_toe.configurable_config.EXAMPLE_CONFIGURATIONS
      games.tic_tac_toe.configurable_config.config1

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.tic_tac_toe.configurable_config.ConfigurableTicTacToeConfig

            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.tic_tac_toe.configurable_config.create_budget_ttt_config
      games.tic_tac_toe.configurable_config.create_experimental_ttt_config
      games.tic_tac_toe.configurable_config.create_quick_ttt_config
      games.tic_tac_toe.configurable_config.create_ttt_config
      games.tic_tac_toe.configurable_config.create_ttt_config_from_example
      games.tic_tac_toe.configurable_config.create_ttt_config_from_player_configs
      games.tic_tac_toe.configurable_config.get_example_config
      games.tic_tac_toe.configurable_config.list_example_configurations

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableTicTacToeConfig

            Bases: :py:obj:`haive.games.tic_tac_toe.config.TicTacToeConfig`


            Configurable Tic-Tac-Toe configuration with dynamic LLM selection.

            This configuration allows users to specify different LLMs for different
            roles in the Tic-Tac-Toe game, providing flexibility and avoiding hardcoded models.

            .. attribute:: x_model

               Model for X player (can be string or LLMConfig)

            .. attribute:: o_model

               Model for O player (can be string or LLMConfig)

            .. attribute:: x_player_name

               Name for the X player

            .. attribute:: o_player_name

               Name for the O player

            .. attribute:: example_config

               Optional example configuration name

            .. attribute:: player_configs

               Optional detailed player configurations

            .. attribute:: temperature

               Temperature for LLM generation

            .. attribute:: max_moves

               Maximum number of moves before draw

            .. attribute:: enable_analysis

               Whether to enable position analysis

            .. attribute:: recursion_limit

               Python recursion limit for game execution


            .. py:method:: _extract_player_names_from_configs()

               Extract player names from player configurations.



            .. py:method:: _generate_player_names_from_example()

               Generate player names based on example configuration.



            .. py:method:: _generate_player_names_from_models(x_model: str, o_model: str)

               Generate player names based on model names.



            .. py:method:: model_post_init(__context: Any) -> None

               Initialize engines after model creation.



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: example_config
               :type:  str | None
               :value: None



            .. py:attribute:: max_moves
               :type:  int
               :value: None



            .. py:attribute:: o_model
               :type:  str | None
               :value: None



            .. py:attribute:: o_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: player_configs
               :type:  dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig] | None
               :value: None



            .. py:attribute:: recursion_limit
               :type:  int
               :value: None



            .. py:attribute:: temperature
               :type:  float
               :value: None



            .. py:attribute:: x_model
               :type:  str | None
               :value: None



            .. py:attribute:: x_player_name
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig

            Create a budget-friendly Tic-Tac-Toe configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_experimental_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig

            Create an experimental Tic-Tac-Toe configuration with mixed providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_quick_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig

            Create a quick Tic-Tac-Toe configuration with fast models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_ttt_config(x_model: str = 'gpt-4o', o_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableTicTacToeConfig

            Create a configurable Tic-Tac-Toe configuration with simple model specifications.

            :param x_model: Model for X player and analyzer
            :param o_model: Model for O player and analyzer
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Tic-Tac-Toe game
            :rtype: ConfigurableTicTacToeConfig

            .. rubric:: Example

            >>> config = create_ttt_config("gpt-4o", "claude-3-opus", temperature=0.5)
            >>> config = create_ttt_config(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     max_moves=9
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_ttt_config_from_example(example_name: str, **kwargs) -> ConfigurableTicTacToeConfig

            Create a configurable Tic-Tac-Toe configuration from a predefined example.

            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured Tic-Tac-Toe game
            :rtype: ConfigurableTicTacToeConfig

            Available examples:
                - "gpt_vs_claude": GPT-4 vs Claude
                - "gpt_only": GPT-4 for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role

            .. rubric:: Example

            >>> config = create_ttt_config_from_example("budget", max_moves=9)
            >>> config = create_ttt_config_from_example("gpt_vs_claude", enable_analysis=False)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_ttt_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableTicTacToeConfig

            Create a configurable Tic-Tac-Toe configuration from detailed player.
            configurations.

            :param player_configs: Dictionary mapping role names to player configurations
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Tic-Tac-Toe game
            :rtype: ConfigurableTicTacToeConfig

            Expected roles:
                - "X_player": X player configuration
                - "O_player": O player configuration
                - "X_analyzer": X analyzer configuration
                - "O_analyzer": O analyzer configuration

            .. rubric:: Example

            >>> player_configs = {
            ...     "X_player": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.7,
            ...         player_name="Strategic X"
            ...     ),
            ...     "O_player": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.3,
            ...         player_name="Tactical O"
            ...     ),
            ...     "X_analyzer": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.2,
            ...         player_name="X Analyst"
            ...     ),
            ...     "O_analyzer": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.2,
            ...         player_name="O Analyst"
            ...     ),
            ... }
            >>> config = create_ttt_config_from_player_configs(player_configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_example_config(name: str) -> ConfigurableTicTacToeConfig

            Get a predefined example configuration by name.

            :param name: Name of the example configuration

            :returns: The example configuration
            :rtype: ConfigurableTicTacToeConfig

            :raises ValueError: If the example name is not found



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: list_example_configurations() -> dict[str, str]

            List all available example configurations.

            :returns: Mapping of configuration names to descriptions
            :rtype: Dict[str, str]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: EXAMPLE_CONFIGURATIONS


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: config1




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.tic_tac_toe.configurable_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

