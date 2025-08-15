games.reversi.configurable_config
=================================

.. py:module:: games.reversi.configurable_config

.. autoapi-nested-parse::

   Configurable Reversi configuration using the generic player agent system.

   This module provides configurable Reversi game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.


   .. autolink-examples:: games.reversi.configurable_config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.reversi.configurable_config.EXAMPLE_CONFIGURATIONS
   games.reversi.configurable_config.config1


Classes
-------

.. autoapisummary::

   games.reversi.configurable_config.ConfigurableReversiConfig


Functions
---------

.. autoapisummary::

   games.reversi.configurable_config.create_advanced_reversi_config
   games.reversi.configurable_config.create_budget_reversi_config
   games.reversi.configurable_config.create_experimental_reversi_config
   games.reversi.configurable_config.create_reversi_config
   games.reversi.configurable_config.create_reversi_config_from_example
   games.reversi.configurable_config.create_reversi_config_from_player_configs
   games.reversi.configurable_config.get_example_config
   games.reversi.configurable_config.list_example_configurations


Module Contents
---------------

.. py:class:: ConfigurableReversiConfig

   Bases: :py:obj:`haive.games.reversi.config.ReversiConfig`


   Configurable Reversi configuration with dynamic LLM selection.

   This configuration allows users to specify different LLMs for different
   roles in the Reversi game, providing flexibility and avoiding hardcoded models.

   .. attribute:: black_model

      Model for black (can be string or LLMConfig)

   .. attribute:: white_model

      Model for white (can be string or LLMConfig)

   .. attribute:: black_name

      Name for black

   .. attribute:: white_name

      Name for white

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


   .. autolink-examples:: ConfigurableReversiConfig
      :collapse:

   .. py:method:: _extract_player_names_from_configs()

      Extract player names from player configurations.


      .. autolink-examples:: _extract_player_names_from_configs
         :collapse:


   .. py:method:: _generate_player_names_from_example()

      Generate player names based on example configuration.


      .. autolink-examples:: _generate_player_names_from_example
         :collapse:


   .. py:method:: _generate_player_names_from_models(black_model: str, white_model: str)

      Generate player names based on model names.


      .. autolink-examples:: _generate_player_names_from_models
         :collapse:


   .. py:method:: model_post_init(__context: Any) -> None

      Initialize engines after model creation.


      .. autolink-examples:: model_post_init
         :collapse:


   .. py:attribute:: black_model
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



   .. py:attribute:: white_model
      :type:  str | None
      :value: None



.. py:function:: create_advanced_reversi_config(**kwargs) -> ConfigurableReversiConfig

   Create an advanced Reversi configuration with powerful models.


   .. autolink-examples:: create_advanced_reversi_config
      :collapse:

.. py:function:: create_budget_reversi_config(**kwargs) -> ConfigurableReversiConfig

   Create a budget-friendly Reversi configuration.


   .. autolink-examples:: create_budget_reversi_config
      :collapse:

.. py:function:: create_experimental_reversi_config(**kwargs) -> ConfigurableReversiConfig

   Create an experimental Reversi configuration with mixed providers.


   .. autolink-examples:: create_experimental_reversi_config
      :collapse:

.. py:function:: create_reversi_config(black_model: str = 'gpt-4o', white_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableReversiConfig

   Create a configurable Reversi configuration with simple model specifications.

   :param black_model: Model for black and analyzer
   :param white_model: Model for white and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Reversi game
   :rtype: ConfigurableReversiConfig

   .. rubric:: Example

   >>> config = create_reversi_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_reversi_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_reversi_config
      :collapse:

.. py:function:: create_reversi_config_from_example(example_name: str, **kwargs) -> ConfigurableReversiConfig

   Create a configurable Reversi configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Reversi game
   :rtype: ConfigurableReversiConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_reversi_config_from_example("budget", enable_analysis=False)
   >>> config = create_reversi_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_reversi_config_from_example
      :collapse:

.. py:function:: create_reversi_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableReversiConfig

   Create a configurable Reversi configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Reversi game
   :rtype: ConfigurableReversiConfig

   Expected roles:
       - "black_player": Player 1 configuration
       - "white_player": Player 2 configuration
       - "black_analyzer": Player 1 analyzer configuration
       - "white_analyzer": Player 2 analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "black_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Black Player"
   ...     ),
   ...     "white_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical White Player"
   ...     ),
   ...     "black_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Reversi Strategist"
   ...     ),
   ...     "white_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Reversi Analyst"
   ...     ),
   ... }
   >>> config = create_reversi_config_from_player_configs(player_configs)


   .. autolink-examples:: create_reversi_config_from_player_configs
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableReversiConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableReversiConfig

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

