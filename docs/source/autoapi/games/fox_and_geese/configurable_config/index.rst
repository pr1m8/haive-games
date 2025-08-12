
:py:mod:`games.fox_and_geese.configurable_config`
=================================================

.. py:module:: games.fox_and_geese.configurable_config

Configurable FoxAndGeese configuration using the generic player agent system.

This module provides configurable FoxAndGeese game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.fox_and_geese.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.fox_and_geese.configurable_config.ConfigurableFoxAndGeeseConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableFoxAndGeeseConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableFoxAndGeeseConfig {
        node [shape=record];
        "ConfigurableFoxAndGeeseConfig" [label="ConfigurableFoxAndGeeseConfig"];
        "haive.games.fox_and_geese.config.FoxAndGeeseConfig" -> "ConfigurableFoxAndGeeseConfig";
      }

.. autoclass:: games.fox_and_geese.configurable_config.ConfigurableFoxAndGeeseConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.fox_and_geese.configurable_config.create_advanced_fox_and_geese_config
   games.fox_and_geese.configurable_config.create_budget_fox_and_geese_config
   games.fox_and_geese.configurable_config.create_experimental_fox_and_geese_config
   games.fox_and_geese.configurable_config.create_fox_and_geese_config
   games.fox_and_geese.configurable_config.create_fox_and_geese_config_from_example
   games.fox_and_geese.configurable_config.create_fox_and_geese_config_from_player_configs
   games.fox_and_geese.configurable_config.get_example_config
   games.fox_and_geese.configurable_config.list_example_configurations

.. py:function:: create_advanced_fox_and_geese_config(**kwargs) -> ConfigurableFoxAndGeeseConfig

   Create an advanced FoxAndGeese configuration with powerful models.


   .. autolink-examples:: create_advanced_fox_and_geese_config
      :collapse:

.. py:function:: create_budget_fox_and_geese_config(**kwargs) -> ConfigurableFoxAndGeeseConfig

   Create a budget-friendly FoxAndGeese configuration.


   .. autolink-examples:: create_budget_fox_and_geese_config
      :collapse:

.. py:function:: create_experimental_fox_and_geese_config(**kwargs) -> ConfigurableFoxAndGeeseConfig

   Create an experimental FoxAndGeese configuration with mixed providers.


   .. autolink-examples:: create_experimental_fox_and_geese_config
      :collapse:

.. py:function:: create_fox_and_geese_config(fox_model: str = 'gpt-4o', geese_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableFoxAndGeeseConfig

   Create a configurable FoxAndGeese configuration with simple model specifications.

   :param fox_model: Model for fox and analyzer
   :param geese_model: Model for geese and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured FoxAndGeese game
   :rtype: ConfigurableFoxAndGeeseConfig

   .. rubric:: Example

   >>> config = create_fox_and_geese_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_fox_and_geese_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_fox_and_geese_config
      :collapse:

.. py:function:: create_fox_and_geese_config_from_example(example_name: str, **kwargs) -> ConfigurableFoxAndGeeseConfig

   Create a configurable FoxAndGeese configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured FoxAndGeese game
   :rtype: ConfigurableFoxAndGeeseConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_fox_and_geese_config_from_example("budget", enable_analysis=False)
   >>> config = create_fox_and_geese_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_fox_and_geese_config_from_example
      :collapse:

.. py:function:: create_fox_and_geese_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableFoxAndGeeseConfig

   Create a configurable FoxAndGeese configuration from detailed player.
   configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured FoxAndGeese game
   :rtype: ConfigurableFoxAndGeeseConfig

   Expected roles:
       - "fox_player": Player 1 configuration
       - "geese_player": Player 2 configuration
       - "fox_analyzer": Player 1 analyzer configuration
       - "geese_analyzer": Player 2 analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "fox_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Fox"
   ...     ),
   ...     "geese_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Geese"
   ...     ),
   ...     "fox_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="FoxAndGeese Strategist"
   ...     ),
   ...     "geese_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="FoxAndGeese Analyst"
   ...     ),
   ... }
   >>> config = create_fox_and_geese_config_from_player_configs(player_configs)


   .. autolink-examples:: create_fox_and_geese_config_from_player_configs
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableFoxAndGeeseConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableFoxAndGeeseConfig

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

.. autolink-examples:: games.fox_and_geese.configurable_config
   :collapse:
   
.. autolink-skip:: next
