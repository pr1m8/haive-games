games.clue.configurable_config
==============================

.. py:module:: games.clue.configurable_config

.. autoapi-nested-parse::

   Configurable Clue configuration using the generic player agent system.

   This module provides configurable Clue game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.


   .. autolink-examples:: games.clue.configurable_config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.clue.configurable_config.EXAMPLE_CONFIGURATIONS
   games.clue.configurable_config.config1


Classes
-------

.. autoapisummary::

   games.clue.configurable_config.ConfigurableClueConfig


Functions
---------

.. autoapisummary::

   games.clue.configurable_config.create_advanced_clue_config
   games.clue.configurable_config.create_budget_clue_config
   games.clue.configurable_config.create_clue_config
   games.clue.configurable_config.create_clue_config_from_example
   games.clue.configurable_config.create_clue_config_from_player_configs
   games.clue.configurable_config.create_experimental_clue_config
   games.clue.configurable_config.get_example_config
   games.clue.configurable_config.list_example_configurations


Module Contents
---------------

.. py:class:: ConfigurableClueConfig

   Bases: :py:obj:`haive.games.clue.config.ClueConfig`


   Configurable Clue configuration with dynamic LLM selection.

   This configuration allows users to specify different LLMs for different
   roles in the Clue game, providing flexibility and avoiding hardcoded models.

   .. attribute:: detective_model

      Model for detective (can be string or LLMConfig)

   .. attribute:: suspect_model

      Model for suspect (can be string or LLMConfig)

   .. attribute:: detective_name

      Name for detective

   .. attribute:: suspect_name

      Name for suspect

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


   .. autolink-examples:: ConfigurableClueConfig
      :collapse:

   .. py:method:: _extract_player_names_from_configs()

      Extract player names from player configurations.


      .. autolink-examples:: _extract_player_names_from_configs
         :collapse:


   .. py:method:: _generate_player_names_from_example()

      Generate player names based on example configuration.


      .. autolink-examples:: _generate_player_names_from_example
         :collapse:


   .. py:method:: _generate_player_names_from_models(detective_model: str, suspect_model: str)

      Generate player names based on model names.


      .. autolink-examples:: _generate_player_names_from_models
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize engines after model creation.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: detective_model
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



   .. py:attribute:: suspect_model
      :type:  str | None
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



.. py:function:: create_advanced_clue_config(**kwargs) -> ConfigurableClueConfig

   Create an advanced Clue configuration with powerful models.


   .. autolink-examples:: create_advanced_clue_config
      :collapse:

.. py:function:: create_budget_clue_config(**kwargs) -> ConfigurableClueConfig

   Create a budget-friendly Clue configuration.


   .. autolink-examples:: create_budget_clue_config
      :collapse:

.. py:function:: create_clue_config(detective_model: str = 'gpt-4o', suspect_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableClueConfig

   Create a configurable Clue configuration with simple model specifications.

   :param detective_model: Model for detective and analyzer
   :param suspect_model: Model for suspect and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Clue game
   :rtype: ConfigurableClueConfig

   .. rubric:: Example

   >>> config = create_clue_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_clue_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_clue_config
      :collapse:

.. py:function:: create_clue_config_from_example(example_name: str, **kwargs) -> ConfigurableClueConfig

   Create a configurable Clue configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Clue game
   :rtype: ConfigurableClueConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_clue_config_from_example("budget", enable_analysis=False)
   >>> config = create_clue_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_clue_config_from_example
      :collapse:

.. py:function:: create_clue_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableClueConfig

   Create a configurable Clue configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Clue game
   :rtype: ConfigurableClueConfig

   Expected roles:
       - "detective_player": Player 1 configuration
       - "suspect_player": Player 2 configuration
       - "detective_analyzer": Player 1 analyzer configuration
       - "suspect_analyzer": Player 2 analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "detective_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Detective"
   ...     ),
   ...     "suspect_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Suspect"
   ...     ),
   ...     "detective_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Clue Strategist"
   ...     ),
   ...     "suspect_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Clue Analyst"
   ...     ),
   ... }
   >>> config = create_clue_config_from_player_configs(player_configs)


   .. autolink-examples:: create_clue_config_from_player_configs
      :collapse:

.. py:function:: create_experimental_clue_config(**kwargs) -> ConfigurableClueConfig

   Create an experimental Clue configuration with mixed providers.


   .. autolink-examples:: create_experimental_clue_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableClueConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableClueConfig

   :raises ValueError: If the example name is not found


   .. autolink-examples:: get_example_config
      :collapse:

.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


   .. autolink-examples:: list_example_configurations
      :collapse:

.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

