games.risk.configurable_config
==============================

.. py:module:: games.risk.configurable_config

Configurable Risk configuration using the generic player agent system.

This module provides configurable Risk game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">8 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Configurable Risk configuration using the generic player agent system.

   This module provides configurable Risk game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.risk.configurable_config.EXAMPLE_CONFIGURATIONS
      games.risk.configurable_config.config1

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.risk.configurable_config.ConfigurableRiskConfig

            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.risk.configurable_config.create_advanced_risk_config
      games.risk.configurable_config.create_budget_risk_config
      games.risk.configurable_config.create_experimental_risk_config
      games.risk.configurable_config.create_risk_config
      games.risk.configurable_config.create_risk_config_from_example
      games.risk.configurable_config.create_risk_config_from_player_configs
      games.risk.configurable_config.get_example_config
      games.risk.configurable_config.list_example_configurations

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableRiskConfig(/, **data: Any)

            Bases: :py:obj:`haive.games.risk.config.RiskConfig`


            Configurable Risk configuration with dynamic LLM selection.

            This configuration allows users to specify different LLMs for different
            roles in the Risk game, providing flexibility and avoiding hardcoded models.

            .. attribute:: player1_model

               Model for player1 (can be string or LLMConfig)

            .. attribute:: player2_model

               Model for player2 (can be string or LLMConfig)

            .. attribute:: player1_name

               Name for player1

            .. attribute:: player2_name

               Name for player2

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

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: _extract_player_names_from_configs()

               Extract player names from player configurations.



            .. py:method:: _generate_player_names_from_example()

               Generate player names based on example configuration.



            .. py:method:: _generate_player_names_from_models(player1_model: str, player2_model: str)

               Generate player names based on model names.



            .. py:method:: model_post_init(__context: Any) -> None

               Initialize engines after model creation.



            .. py:attribute:: example_config
               :type:  str | None
               :value: None



            .. py:attribute:: player1_model
               :type:  str | None
               :value: None



            .. py:attribute:: player2_model
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

.. py:function:: create_advanced_risk_config(**kwargs) -> ConfigurableRiskConfig

            Create an advanced Risk configuration with powerful models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_risk_config(**kwargs) -> ConfigurableRiskConfig

            Create a budget-friendly Risk configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_experimental_risk_config(**kwargs) -> ConfigurableRiskConfig

            Create an experimental Risk configuration with mixed providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_risk_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableRiskConfig

            Create a configurable Risk configuration with simple model specifications.

            :param player1_model: Model for player1 and analyzer
            :param player2_model: Model for player2 and analyzer
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Risk game
            :rtype: ConfigurableRiskConfig

            .. rubric:: Example

            >>> config = create_risk_config("gpt-4o", "claude-3-opus", temperature=0.5)
            >>> config = create_risk_config(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     enable_analysis=True
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_risk_config_from_example(example_name: str, **kwargs) -> ConfigurableRiskConfig

            Create a configurable Risk configuration from a predefined example.

            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured Risk game
            :rtype: ConfigurableRiskConfig

            Available examples:
                - "gpt_vs_claude": GPT vs Claude
                - "gpt_only": GPT for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "advanced": High-powered models for strategic gameplay

            .. rubric:: Example

            >>> config = create_risk_config_from_example("budget", enable_analysis=False)
            >>> config = create_risk_config_from_example("advanced", visualize_game=True)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_risk_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableRiskConfig

            Create a configurable Risk configuration from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Risk game
            :rtype: ConfigurableRiskConfig

            Expected roles:
                - "player1_player": Player 1 configuration
                - "player2_player": Player 2 configuration
                - "player1_analyzer": Player 1 analyzer configuration
                - "player2_analyzer": Player 2 analyzer configuration

            .. rubric:: Example

            >>> player_configs = {
            ...     "player1_player": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.7,
            ...         player_name="Strategic General"
            ...     ),
            ...     "player2_player": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.3,
            ...         player_name="Tactical Commander"
            ...     ),
            ...     "player1_analyzer": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.2,
            ...         player_name="Risk Strategist"
            ...     ),
            ...     "player2_analyzer": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.2,
            ...         player_name="Risk Analyst"
            ...     ),
            ... }
            >>> config = create_risk_config_from_player_configs(player_configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_example_config(name: str) -> ConfigurableRiskConfig

            Get a predefined example configuration by name.

            :param name: Name of the example configuration

            :returns: The example configuration
            :rtype: ConfigurableRiskConfig

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

      from games.risk.configurable_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

