games.debate.configurable_config
================================

.. py:module:: games.debate.configurable_config

Configurable Debate configuration using the generic player agent system.

This module provides configurable Debate game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">8 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Configurable Debate configuration using the generic player agent system.

   This module provides configurable Debate game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.debate.configurable_config.EXAMPLE_CONFIGURATIONS
      games.debate.configurable_config.config1

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.debate.configurable_config.ConfigurableDebateConfig

            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.debate.configurable_config.create_advanced_debate_config
      games.debate.configurable_config.create_budget_debate_config
      games.debate.configurable_config.create_debate_config
      games.debate.configurable_config.create_debate_config_from_example
      games.debate.configurable_config.create_debate_config_from_player_configs
      games.debate.configurable_config.create_experimental_debate_config
      games.debate.configurable_config.get_example_config
      games.debate.configurable_config.list_example_configurations

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableDebateConfig

            Bases: :py:obj:`haive.games.debate.config.DebateAgentConfig`


            Configurable Debate configuration with dynamic LLM selection.

            This configuration allows users to specify different LLMs for different
            roles in the Debate game, providing flexibility and avoiding hardcoded models.

            .. attribute:: debater1_model

               Model for debater1 (can be string or LLMConfig)

            .. attribute:: debater2_model

               Model for debater2 (can be string or LLMConfig)

            .. attribute:: debater1_name

               Name for debater1

            .. attribute:: debater2_name

               Name for debater2

            .. attribute:: example_config

               Optional example configuration name

            .. attribute:: player_configs

               Optional detailed player configurations

            .. attribute:: temperature

               Temperature for LLM generation

            .. attribute:: enable_analysis

               Whether to enable strategic analysis

            .. attribute:: visualize_game

               Whether to visualize game state

            .. attribute:: recursion_limit

               Python recursion limit for game execution


            .. py:method:: _extract_player_names_from_configs()

               Extract player names from player configurations.



            .. py:method:: _generate_player_names_from_example()

               Generate player names based on example configuration.



            .. py:method:: _generate_player_names_from_models(debater1_model: str, debater2_model: str)

               Generate player names based on model names.



            .. py:method:: model_post_init(__context: Any) -> None

               Initialize engines after model creation.



            .. py:attribute:: debater1_model
               :type:  str | None
               :value: None



            .. py:attribute:: debater2_model
               :type:  str | None
               :value: None



            .. py:attribute:: example_config
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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_advanced_debate_config(**kwargs) -> ConfigurableDebateConfig

            Create an advanced Debate configuration with powerful models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_debate_config(**kwargs) -> ConfigurableDebateConfig

            Create a budget-friendly Debate configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_debate_config(debater1_model: str = 'gpt-4o', debater2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableDebateConfig

            Create a configurable Debate configuration with simple model specifications.

            :param debater1_model: Model for debater1 and analyzer
            :param debater2_model: Model for debater2 and analyzer
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Debate game
            :rtype: ConfigurableDebateConfig

            .. rubric:: Example

            >>> config = create_debate_config("gpt-4o", "claude-3-opus", temperature=0.5)
            >>> config = create_debate_config(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     enable_analysis=True
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_debate_config_from_example(example_name: str, **kwargs) -> ConfigurableDebateConfig

            Create a configurable Debate configuration from a predefined example.

            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured Debate game
            :rtype: ConfigurableDebateConfig

            Available examples:
                - "gpt_vs_claude": GPT vs Claude
                - "gpt_only": GPT for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "advanced": High-powered models for strategic gameplay

            .. rubric:: Example

            >>> config = create_debate_config_from_example("budget", enable_analysis=False)
            >>> config = create_debate_config_from_example("advanced", visualize_game=True)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_debate_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableDebateConfig

            Create a configurable Debate configuration from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Debate game
            :rtype: ConfigurableDebateConfig

            Expected roles:
                - "debater1_player": Player 1 configuration
                - "debater2_player": Player 2 configuration
                - "debater1_analyzer": Player 1 analyzer configuration
                - "debater2_analyzer": Player 2 analyzer configuration

            .. rubric:: Example

            >>> player_configs = {
            ...     "debater1_player": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.7,
            ...         player_name="Strategic Debater A"
            ...     ),
            ...     "debater2_player": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.3,
            ...         player_name="Tactical Debater B"
            ...     ),
            ...     "debater1_analyzer": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.2,
            ...         player_name="Debate Strategist"
            ...     ),
            ...     "debater2_analyzer": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.2,
            ...         player_name="Debate Analyst"
            ...     ),
            ... }
            >>> config = create_debate_config_from_player_configs(player_configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_experimental_debate_config(**kwargs) -> ConfigurableDebateConfig

            Create an experimental Debate configuration with mixed providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_example_config(name: str) -> ConfigurableDebateConfig

            Get a predefined example configuration by name.

            :param name: Name of the example configuration

            :returns: The example configuration
            :rtype: ConfigurableDebateConfig

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

      from games.debate.configurable_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

