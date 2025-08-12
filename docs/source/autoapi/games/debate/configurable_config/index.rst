
:py:mod:`games.debate.configurable_config`
==========================================

.. py:module:: games.debate.configurable_config

Configurable Debate configuration using the generic player agent system.

This module provides configurable Debate game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.


.. autolink-examples:: games.debate.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.debate.configurable_config.ConfigurableDebateConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableDebateConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableDebateConfig {
        node [shape=record];
        "ConfigurableDebateConfig" [label="ConfigurableDebateConfig"];
        "haive.games.debate.config.DebateAgentConfig" -> "ConfigurableDebateConfig";
      }

.. autoclass:: games.debate.configurable_config.ConfigurableDebateConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.debate.configurable_config.create_advanced_debate_config
   games.debate.configurable_config.create_budget_debate_config
   games.debate.configurable_config.create_debate_config
   games.debate.configurable_config.create_debate_config_from_example
   games.debate.configurable_config.create_debate_config_from_player_configs
   games.debate.configurable_config.create_experimental_debate_config
   games.debate.configurable_config.get_example_config
   games.debate.configurable_config.list_example_configurations

.. py:function:: create_advanced_debate_config(**kwargs) -> ConfigurableDebateConfig

   Create an advanced Debate configuration with powerful models.


   .. autolink-examples:: create_advanced_debate_config
      :collapse:

.. py:function:: create_budget_debate_config(**kwargs) -> ConfigurableDebateConfig

   Create a budget-friendly Debate configuration.


   .. autolink-examples:: create_budget_debate_config
      :collapse:

.. py:function:: create_debate_config(debater1_model: str = 'gpt-4o', debater2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableDebateConfig

   Create a configurable Debate configuration with simple model specifications.

   :param debater1_model: Model for debater1 and analyzer
   :param debater2_model: Model for debater2 and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Debate game
   :rtype: ConfigurableDebateConfig

   .. rubric:: Example

   >>> config = create_debate_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_debate_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_debate_config
      :collapse:

.. py:function:: create_debate_config_from_example(example_name: str, **kwargs) -> ConfigurableDebateConfig

   Create a configurable Debate configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Debate game
   :rtype: ConfigurableDebateConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_debate_config_from_example("budget", enable_analysis=False)
   >>> config = create_debate_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_debate_config_from_example
      :collapse:

.. py:function:: create_debate_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableDebateConfig

   Create a configurable Debate configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Debate game
   :rtype: ConfigurableDebateConfig

   Expected roles:
       - "debater1_player": Player 1 configuration
       - "debater2_player": Player 2 configuration
       - "debater1_analyzer": Player 1 analyzer configuration
       - "debater2_analyzer": Player 2 analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "debater1_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Debater A"
   ...     ),
   ...     "debater2_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Debater B"
   ...     ),
   ...     "debater1_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Debate Strategist"
   ...     ),
   ...     "debater2_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Debate Analyst"
   ...     ),
   ... }
   >>> config = create_debate_config_from_player_configs(player_configs)


   .. autolink-examples:: create_debate_config_from_player_configs
      :collapse:

.. py:function:: create_experimental_debate_config(**kwargs) -> ConfigurableDebateConfig

   Create an experimental Debate configuration with mixed providers.


   .. autolink-examples:: create_experimental_debate_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableDebateConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableDebateConfig

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

.. autolink-examples:: games.debate.configurable_config
   :collapse:
   
.. autolink-skip:: next
