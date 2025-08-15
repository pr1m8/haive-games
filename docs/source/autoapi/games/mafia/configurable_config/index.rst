games.mafia.configurable_config
===============================

.. py:module:: games.mafia.configurable_config

.. autoapi-nested-parse::

   Configurable Mafia configuration using the generic player agent system.

   This module provides configurable Mafia game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.


   .. autolink-examples:: games.mafia.configurable_config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mafia.configurable_config.EXAMPLE_CONFIGURATIONS
   games.mafia.configurable_config.config1


Classes
-------

.. autoapisummary::

   games.mafia.configurable_config.ConfigurableMafiaConfig


Functions
---------

.. autoapisummary::

   games.mafia.configurable_config.create_advanced_mafia_config
   games.mafia.configurable_config.create_budget_mafia_config
   games.mafia.configurable_config.create_experimental_mafia_config
   games.mafia.configurable_config.create_mafia_config
   games.mafia.configurable_config.create_mafia_config_from_example
   games.mafia.configurable_config.create_mafia_config_from_player_configs
   games.mafia.configurable_config.get_example_config
   games.mafia.configurable_config.list_example_configurations


Module Contents
---------------

.. py:class:: ConfigurableMafiaConfig

   Bases: :py:obj:`haive.games.mafia.config.MafiaAgentConfig`


   Configurable Mafia configuration with dynamic LLM selection.

   This configuration allows users to specify different LLMs for different
   roles in the Mafia game, providing flexibility and avoiding hardcoded models.

   .. attribute:: mafia_model

      Model for mafia (can be string or LLMConfig)

   .. attribute:: town_model

      Model for town (can be string or LLMConfig)

   .. attribute:: mafia_name

      Name for mafia

   .. attribute:: town_name

      Name for town

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


   .. autolink-examples:: ConfigurableMafiaConfig
      :collapse:

   .. py:method:: _extract_player_names_from_configs()

      Extract player names from player configurations.


      .. autolink-examples:: _extract_player_names_from_configs
         :collapse:


   .. py:method:: _generate_player_names_from_example()

      Generate player names based on example configuration.


      .. autolink-examples:: _generate_player_names_from_example
         :collapse:


   .. py:method:: _generate_player_names_from_models(mafia_model: str, town_model: str)

      Generate player names based on model names.


      .. autolink-examples:: _generate_player_names_from_models
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize engines after model creation.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: example_config
      :type:  str | None
      :value: None



   .. py:attribute:: mafia_model
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



   .. py:attribute:: town_model
      :type:  str | None
      :value: None



.. py:function:: create_advanced_mafia_config(**kwargs) -> ConfigurableMafiaConfig

   Create an advanced Mafia configuration with powerful models.


   .. autolink-examples:: create_advanced_mafia_config
      :collapse:

.. py:function:: create_budget_mafia_config(**kwargs) -> ConfigurableMafiaConfig

   Create a budget-friendly Mafia configuration.


   .. autolink-examples:: create_budget_mafia_config
      :collapse:

.. py:function:: create_experimental_mafia_config(**kwargs) -> ConfigurableMafiaConfig

   Create an experimental Mafia configuration with mixed providers.


   .. autolink-examples:: create_experimental_mafia_config
      :collapse:

.. py:function:: create_mafia_config(mafia_model: str = 'gpt-4o', town_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableMafiaConfig

   Create a configurable Mafia configuration with simple model specifications.

   :param mafia_model: Model for mafia and analyzer
   :param town_model: Model for town and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mafia game
   :rtype: ConfigurableMafiaConfig

   .. rubric:: Example

   >>> config = create_mafia_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_mafia_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_mafia_config
      :collapse:

.. py:function:: create_mafia_config_from_example(example_name: str, **kwargs) -> ConfigurableMafiaConfig

   Create a configurable Mafia configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Mafia game
   :rtype: ConfigurableMafiaConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_mafia_config_from_example("budget", enable_analysis=False)
   >>> config = create_mafia_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_mafia_config_from_example
      :collapse:

.. py:function:: create_mafia_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableMafiaConfig

   Create a configurable Mafia configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mafia game
   :rtype: ConfigurableMafiaConfig

   Expected roles:
       - "mafia_player": Player 1 configuration
       - "town_player": Player 2 configuration
       - "mafia_analyzer": Player 1 analyzer configuration
       - "town_analyzer": Player 2 analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "mafia_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Mafia"
   ...     ),
   ...     "town_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Town"
   ...     ),
   ...     "mafia_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Mafia Strategist"
   ...     ),
   ...     "town_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Mafia Analyst"
   ...     ),
   ... }
   >>> config = create_mafia_config_from_player_configs(player_configs)


   .. autolink-examples:: create_mafia_config_from_player_configs
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableMafiaConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableMafiaConfig

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

