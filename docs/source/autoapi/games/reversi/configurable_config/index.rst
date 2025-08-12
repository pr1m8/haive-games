
:py:mod:`games.reversi.configurable_config`
===========================================

.. py:module:: games.reversi.configurable_config

Configurable Reversi configuration using the generic player agent system.

This module provides configurable Reversi game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.


.. autolink-examples:: games.reversi.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.reversi.configurable_config.ConfigurableReversiConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableReversiConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableReversiConfig {
        node [shape=record];
        "ConfigurableReversiConfig" [label="ConfigurableReversiConfig"];
        "haive.games.reversi.config.ReversiConfig" -> "ConfigurableReversiConfig";
      }

.. autoclass:: games.reversi.configurable_config.ConfigurableReversiConfig
   :members:
   :undoc-members:
   :show-inheritance:


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



.. rubric:: Related Links

.. autolink-examples:: games.reversi.configurable_config
   :collapse:
   
.. autolink-skip:: next
