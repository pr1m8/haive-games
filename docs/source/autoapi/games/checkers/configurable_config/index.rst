games.checkers.configurable_config
==================================

.. py:module:: games.checkers.configurable_config

.. autoapi-nested-parse::

   Configurable Checkers configuration using the generic player agent system.

   This module provides configurable Checkers game configurations that replace hardcoded
   LLM settings with dynamic, configurable player agents.



Attributes
----------

.. autoapisummary::

   games.checkers.configurable_config.EXAMPLE_CONFIGURATIONS
   games.checkers.configurable_config.config1


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/checkers/configurable_config/ConfigurableCheckersConfig

.. autoapisummary::

   games.checkers.configurable_config.ConfigurableCheckersConfig


Functions
---------

.. autoapisummary::

   games.checkers.configurable_config.create_budget_checkers_config
   games.checkers.configurable_config.create_checkers_config
   games.checkers.configurable_config.create_checkers_config_from_example
   games.checkers.configurable_config.create_checkers_config_from_player_configs
   games.checkers.configurable_config.create_competitive_checkers_config
   games.checkers.configurable_config.create_experimental_checkers_config
   games.checkers.configurable_config.get_example_config
   games.checkers.configurable_config.list_example_configurations


Module Contents
---------------

.. py:function:: create_budget_checkers_config(**kwargs) -> ConfigurableCheckersConfig

   Create a budget-friendly Checkers configuration.


.. py:function:: create_checkers_config(red_model: str = 'gpt-4o', black_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableCheckersConfig

   Create a configurable Checkers configuration with simple model specifications.

   :param red_model: Model for red player and analyzer
   :param black_model: Model for black player and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Checkers game
   :rtype: ConfigurableCheckersConfig

   .. rubric:: Examples

   >>> config = create_checkers_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_checkers_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     max_moves=150
   ... )


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

   .. rubric:: Examples

   >>> config = create_checkers_config_from_example("budget", max_moves=80)
   >>> config = create_checkers_config_from_example("gpt_vs_claude", enable_analysis=False)


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

   .. rubric:: Examples

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


.. py:function:: create_competitive_checkers_config(**kwargs) -> ConfigurableCheckersConfig

   Create a competitive Checkers configuration with powerful models.


.. py:function:: create_experimental_checkers_config(**kwargs) -> ConfigurableCheckersConfig

   Create an experimental Checkers configuration with mixed providers.


.. py:function:: get_example_config(name: str) -> ConfigurableCheckersConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableCheckersConfig

   :raises ValueError: If the example name is not found


.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

