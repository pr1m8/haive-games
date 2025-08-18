games.checkers.configurable_config
==================================

.. py:module:: games.checkers.configurable_config

Configurable Checkers configuration using the generic player agent system.

This module provides configurable Checkers game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">8 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Configurable Checkers configuration using the generic player agent system.

   This module provides configurable Checkers game configurations that replace hardcoded
   LLM settings with dynamic, configurable player agents.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.checkers.configurable_config.EXAMPLE_CONFIGURATIONS
      games.checkers.configurable_config.config1

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.checkers.configurable_config.ConfigurableCheckersConfig

            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.checkers.configurable_config.create_budget_checkers_config
      games.checkers.configurable_config.create_checkers_config
      games.checkers.configurable_config.create_checkers_config_from_example
      games.checkers.configurable_config.create_checkers_config_from_player_configs
      games.checkers.configurable_config.create_competitive_checkers_config
      games.checkers.configurable_config.create_experimental_checkers_config
      games.checkers.configurable_config.get_example_config
      games.checkers.configurable_config.list_example_configurations

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableCheckersConfig

            Bases: :py:obj:`haive.games.checkers.config.CheckersAgentConfig`


            Configurable Checkers configuration with dynamic LLM selection.

            This configuration allows users to specify different LLMs for different
            roles in the Checkers game, providing flexibility and avoiding hardcoded models.

            .. attribute:: red_model

               Model for red player (can be string or LLMConfig)

            .. attribute:: black_model

               Model for black player (can be string or LLMConfig)

            .. attribute:: red_player_name

               Name for the red player

            .. attribute:: black_player_name

               Name for the black player

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



            .. py:method:: _generate_player_names_from_models(red_model: str, black_model: str)

               Generate player names based on model names.



            .. py:method:: model_post_init(__context: Any) -> None

               Initialize engines after model creation.



            .. py:attribute:: black_model
               :type:  str | None
               :value: None



            .. py:attribute:: black_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: example_config
               :type:  str | None
               :value: None



            .. py:attribute:: max_moves
               :type:  int
               :value: None



            .. py:attribute:: player_configs
               :type:  dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig] | None
               :value: None



            .. py:attribute:: recursion_limit
               :type:  int
               :value: None



            .. py:attribute:: red_model
               :type:  str | None
               :value: None



            .. py:attribute:: red_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: temperature
               :type:  float
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_checkers_config(**kwargs) -> ConfigurableCheckersConfig

            Create a budget-friendly Checkers configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_checkers_config(red_model: str = 'gpt-4o', black_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableCheckersConfig

            Create a configurable Checkers configuration with simple model specifications.

            :param red_model: Model for red player and analyzer
            :param black_model: Model for black player and analyzer
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Checkers game
            :rtype: ConfigurableCheckersConfig

            .. rubric:: Example

            >>> config = create_checkers_config("gpt-4o", "claude-3-opus", temperature=0.5)
            >>> config = create_checkers_config(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     max_moves=150
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_checkers_config_from_example(example_name: str, **kwargs) -> ConfigurableCheckersConfig

            Create a configurable Checkers configuration from a predefined example.

            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured Checkers game
            :rtype: ConfigurableCheckersConfig

            Available examples:
                - "gpt_vs_claude": GPT-4 vs Claude
                - "gpt_only": GPT-4 for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "checkers_masters": High-powered models for competitive play

            .. rubric:: Example

            >>> config = create_checkers_config_from_example("budget", max_moves=80)
            >>> config = create_checkers_config_from_example("gpt_vs_claude", enable_analysis=False)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_checkers_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableCheckersConfig

            Create a configurable Checkers configuration from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Checkers game
            :rtype: ConfigurableCheckersConfig

            Expected roles:
                - "red_player": Red player configuration
                - "black_player": Black player configuration
                - "red_analyzer": Red analyzer configuration
                - "black_analyzer": Black analyzer configuration

            .. rubric:: Example

            >>> player_configs = {
            ...     "red_player": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.7,
            ...         player_name="Aggressive Red"
            ...     ),
            ...     "black_player": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.3,
            ...         player_name="Strategic Black"
            ...     ),
            ...     "red_analyzer": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.2,
            ...         player_name="Red Analyst"
            ...     ),
            ...     "black_analyzer": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.2,
            ...         player_name="Black Analyst"
            ...     ),
            ... }
            >>> config = create_checkers_config_from_player_configs(player_configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_competitive_checkers_config(**kwargs) -> ConfigurableCheckersConfig

            Create a competitive Checkers configuration with powerful models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_experimental_checkers_config(**kwargs) -> ConfigurableCheckersConfig

            Create an experimental Checkers configuration with mixed providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_example_config(name: str) -> ConfigurableCheckersConfig

            Get a predefined example configuration by name.

            :param name: Name of the example configuration

            :returns: The example configuration
            :rtype: ConfigurableCheckersConfig

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

      from games.checkers.configurable_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

