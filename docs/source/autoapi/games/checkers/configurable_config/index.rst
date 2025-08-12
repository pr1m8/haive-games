
:py:mod:`games.checkers.configurable_config`
============================================

.. py:module:: games.checkers.configurable_config

Configurable Checkers configuration using the generic player agent system.

This module provides configurable Checkers game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.checkers.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.checkers.configurable_config.ConfigurableCheckersConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableCheckersConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableCheckersConfig {
        node [shape=record];
        "ConfigurableCheckersConfig" [label="ConfigurableCheckersConfig"];
        "haive.games.checkers.config.CheckersAgentConfig" -> "ConfigurableCheckersConfig";
      }

.. autoclass:: games.checkers.configurable_config.ConfigurableCheckersConfig
   :members:
   :undoc-members:
   :show-inheritance:


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

.. py:function:: create_budget_checkers_config(**kwargs) -> ConfigurableCheckersConfig

   Create a budget-friendly Checkers configuration.


   .. autolink-examples:: create_budget_checkers_config
      :collapse:

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


   .. autolink-examples:: create_checkers_config
      :collapse:

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


   .. autolink-examples:: create_checkers_config_from_example
      :collapse:

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


   .. autolink-examples:: create_checkers_config_from_player_configs
      :collapse:

.. py:function:: create_competitive_checkers_config(**kwargs) -> ConfigurableCheckersConfig

   Create a competitive Checkers configuration with powerful models.


   .. autolink-examples:: create_competitive_checkers_config
      :collapse:

.. py:function:: create_experimental_checkers_config(**kwargs) -> ConfigurableCheckersConfig

   Create an experimental Checkers configuration with mixed providers.


   .. autolink-examples:: create_experimental_checkers_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableCheckersConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableCheckersConfig

   :raises ValueError: If the example name is not found


   .. autolink-examples:: get_example_config
      :collapse:

.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


   .. autolink-examples:: list_example_configurations
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.checkers.configurable_config
   :collapse:
   
.. autolink-skip:: next
