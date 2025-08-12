
:py:mod:`games.among_us.configurable_config`
============================================

.. py:module:: games.among_us.configurable_config

Configurable Among Us configuration using the generic player agent system.

This module provides configurable Among Us game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.among_us.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.among_us.configurable_config.ConfigurableAmongUsConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableAmongUsConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableAmongUsConfig {
        node [shape=record];
        "ConfigurableAmongUsConfig" [label="ConfigurableAmongUsConfig"];
        "haive.games.among_us.config.AmongUsConfig" -> "ConfigurableAmongUsConfig";
      }

.. autoclass:: games.among_us.configurable_config.ConfigurableAmongUsConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.among_us.configurable_config.create_among_us_config
   games.among_us.configurable_config.create_among_us_config_from_example
   games.among_us.configurable_config.create_among_us_config_from_player_configs
   games.among_us.configurable_config.create_budget_among_us_config
   games.among_us.configurable_config.create_detective_among_us_config
   games.among_us.configurable_config.create_experimental_among_us_config
   games.among_us.configurable_config.get_example_config
   games.among_us.configurable_config.list_example_configurations

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


   .. autolink-examples:: create_among_us_config
      :collapse:

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


   .. autolink-examples:: create_among_us_config_from_example
      :collapse:

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


   .. autolink-examples:: create_among_us_config_from_player_configs
      :collapse:

.. py:function:: create_budget_among_us_config(**kwargs) -> ConfigurableAmongUsConfig

   Create a budget-friendly Among Us configuration.


   .. autolink-examples:: create_budget_among_us_config
      :collapse:

.. py:function:: create_detective_among_us_config(**kwargs) -> ConfigurableAmongUsConfig

   Create a detective-style Among Us configuration with powerful models.


   .. autolink-examples:: create_detective_among_us_config
      :collapse:

.. py:function:: create_experimental_among_us_config(**kwargs) -> ConfigurableAmongUsConfig

   Create an experimental Among Us configuration with mixed providers.


   .. autolink-examples:: create_experimental_among_us_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableAmongUsConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableAmongUsConfig

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

.. autolink-examples:: games.among_us.configurable_config
   :collapse:
   
.. autolink-skip:: next
