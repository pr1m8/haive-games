games.mafia.configurable_config
===============================

.. py:module:: games.mafia.configurable_config

.. autoapi-nested-parse::

   Configurable Mafia configuration using the generic player agent system.

   This module provides configurable Mafia game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.



Attributes
----------

.. autoapisummary::

   games.mafia.configurable_config.EXAMPLE_CONFIGURATIONS
   games.mafia.configurable_config.config1


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/configurable_config/ConfigurableMafiaConfig

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

.. py:function:: create_advanced_mafia_config(**kwargs) -> ConfigurableMafiaConfig

   Create an advanced Mafia configuration with powerful models.


.. py:function:: create_budget_mafia_config(**kwargs) -> ConfigurableMafiaConfig

   Create a budget-friendly Mafia configuration.


.. py:function:: create_experimental_mafia_config(**kwargs) -> ConfigurableMafiaConfig

   Create an experimental Mafia configuration with mixed providers.


.. py:function:: create_mafia_config(mafia_model: str = 'gpt-4o', town_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableMafiaConfig

   Create a configurable Mafia configuration with simple model specifications.

   :param mafia_model: Model for mafia and analyzer
   :param town_model: Model for town and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mafia game
   :rtype: ConfigurableMafiaConfig

   .. rubric:: Examples

   >>> config = create_mafia_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_mafia_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


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

   .. rubric:: Examples

   >>> config = create_mafia_config_from_example("budget", enable_analysis=False)
   >>> config = create_mafia_config_from_example("advanced", visualize_game=True)


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

   .. rubric:: Examples

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


.. py:function:: get_example_config(name: str) -> ConfigurableMafiaConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableMafiaConfig

   :raises ValueError: If the example name is not found


.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

