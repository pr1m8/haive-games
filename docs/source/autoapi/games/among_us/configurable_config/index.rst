games.among_us.configurable_config
==================================

.. py:module:: games.among_us.configurable_config

Configurable Among Us configuration using the generic player agent system.

This module provides configurable Among Us game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">8 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Configurable Among Us configuration using the generic player agent system.

   This module provides configurable Among Us game configurations that replace hardcoded
   LLM settings with dynamic, configurable player agents.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.among_us.configurable_config.EXAMPLE_CONFIGURATIONS
      games.among_us.configurable_config.config1

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.among_us.configurable_config.ConfigurableAmongUsConfig

            

.. admonition:: Functions (8)
   :class: info

   .. autoapisummary::

      games.among_us.configurable_config.create_among_us_config
      games.among_us.configurable_config.create_among_us_config_from_example
      games.among_us.configurable_config.create_among_us_config_from_player_configs
      games.among_us.configurable_config.create_budget_among_us_config
      games.among_us.configurable_config.create_detective_among_us_config
      games.among_us.configurable_config.create_experimental_among_us_config
      games.among_us.configurable_config.get_example_config
      games.among_us.configurable_config.list_example_configurations

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigurableAmongUsConfig

            Bases: :py:obj:`haive.games.among_us.config.AmongUsConfig`


            Configurable Among Us configuration with dynamic LLM selection.

            This configuration allows users to specify different LLMs for different
            roles in the Among Us game, providing flexibility and avoiding hardcoded models.

            .. attribute:: crewmate_model

               Model for crewmate players (can be string or LLMConfig)

            .. attribute:: impostor_model

               Model for impostor players (can be string or LLMConfig)

            .. attribute:: crewmate_player_name

               Name for the crewmate players

            .. attribute:: impostor_player_name

               Name for the impostor players

            .. attribute:: example_config

               Optional example configuration name

            .. attribute:: player_configs

               Optional detailed player configurations

            .. attribute:: temperature

               Temperature for LLM generation

            .. attribute:: max_rounds

               Maximum number of rounds before game ends

            .. attribute:: enable_analysis

               Whether to enable game state analysis

            .. attribute:: recursion_limit

               Python recursion limit for game execution


            .. py:method:: _extract_player_names_from_configs()

               Extract player names from player configurations.



            .. py:method:: _generate_player_names_from_example()

               Generate player names based on example configuration.



            .. py:method:: _generate_player_names_from_models(crewmate_model: str, impostor_model: str)

               Generate player names based on model names.



            .. py:method:: model_post_init(__context: Any) -> None

               Initialize engines after model creation.



            .. py:attribute:: crewmate_model
               :type:  str | None
               :value: None



            .. py:attribute:: crewmate_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: example_config
               :type:  str | None
               :value: None



            .. py:attribute:: impostor_model
               :type:  str | None
               :value: None



            .. py:attribute:: impostor_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: max_rounds
               :type:  int
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

.. py:function:: create_among_us_config(crewmate_model: str = 'gpt-4o', impostor_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableAmongUsConfig

            Create a configurable Among Us configuration with simple model specifications.

            :param crewmate_model: Model for crewmate players and analyzers
            :param impostor_model: Model for impostor players and analyzers
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Among Us game
            :rtype: ConfigurableAmongUsConfig

            .. rubric:: Example

            >>> config = create_among_us_config("gpt-4o", "claude-3-opus", temperature=0.5)
            >>> config = create_among_us_config(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     max_rounds=75
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_among_us_config_from_example(example_name: str, **kwargs) -> ConfigurableAmongUsConfig

            Create a configurable Among Us configuration from a predefined example.

            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured Among Us game
            :rtype: ConfigurableAmongUsConfig

            Available examples:
                - "gpt_vs_claude": GPT crewmate vs Claude impostor
                - "gpt_only": GPT for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "detective_vs_mastermind": High-powered models for intense gameplay

            .. rubric:: Example

            >>> config = create_among_us_config_from_example("budget", max_rounds=40)
            >>> config = create_among_us_config_from_example("detective_vs_mastermind", enable_analysis=False)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_among_us_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableAmongUsConfig

            Create a configurable Among Us configuration from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured Among Us game
            :rtype: ConfigurableAmongUsConfig

            Expected roles:
                - "crewmate_player": Crewmate player configuration
                - "impostor_player": Impostor player configuration
                - "crewmate_analyzer": Crewmate analyzer configuration
                - "impostor_analyzer": Impostor analyzer configuration

            .. rubric:: Example

            >>> player_configs = {
            ...     "crewmate_player": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.7,
            ...         player_name="Detective Crewmate"
            ...     ),
            ...     "impostor_player": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.3,
            ...         player_name="Stealth Impostor"
            ...     ),
            ...     "crewmate_analyzer": PlayerAgentConfig(
            ...         llm_config="gpt-4o",
            ...         temperature=0.2,
            ...         player_name="Crew Analyst"
            ...     ),
            ...     "impostor_analyzer": PlayerAgentConfig(
            ...         llm_config="claude-3-opus",
            ...         temperature=0.2,
            ...         player_name="Impostor Strategist"
            ...     ),
            ... }
            >>> config = create_among_us_config_from_player_configs(player_configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_among_us_config(**kwargs) -> ConfigurableAmongUsConfig

            Create a budget-friendly Among Us configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_detective_among_us_config(**kwargs) -> ConfigurableAmongUsConfig

            Create a detective-style Among Us configuration with powerful models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_experimental_among_us_config(**kwargs) -> ConfigurableAmongUsConfig

            Create an experimental Among Us configuration with mixed providers.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: get_example_config(name: str) -> ConfigurableAmongUsConfig

            Get a predefined example configuration by name.

            :param name: Name of the example configuration

            :returns: The example configuration
            :rtype: ConfigurableAmongUsConfig

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

      from games.among_us.configurable_config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

