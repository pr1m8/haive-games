games.clue.configurable_config
==============================

.. py:module:: games.clue.configurable_config

.. autoapi-nested-parse::

   Configurable Clue configuration using the generic player agent system.

   This module provides configurable Clue game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.



Attributes
----------

.. autoapisummary::

   games.clue.configurable_config.EXAMPLE_CONFIGURATIONS
   games.clue.configurable_config.config1


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/clue/configurable_config/ConfigurableClueConfig

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

.. py:function:: create_advanced_clue_config(**kwargs) -> ConfigurableClueConfig

   Create an advanced Clue configuration with powerful models.


.. py:function:: create_budget_clue_config(**kwargs) -> ConfigurableClueConfig

   Create a budget-friendly Clue configuration.


.. py:function:: create_clue_config(detective_model: str = 'gpt-4o', suspect_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableClueConfig

   Create a configurable Clue configuration with simple model specifications.

   :param detective_model: Model for detective and analyzer
   :param suspect_model: Model for suspect and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Clue game
   :rtype: ConfigurableClueConfig

   .. rubric:: Examples

   >>> config = create_clue_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_clue_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


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

   .. rubric:: Examples

   >>> config = create_clue_config_from_example("budget", enable_analysis=False)
   >>> config = create_clue_config_from_example("advanced", visualize_game=True)


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

   .. rubric:: Examples

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


.. py:function:: create_experimental_clue_config(**kwargs) -> ConfigurableClueConfig

   Create an experimental Clue configuration with mixed providers.


.. py:function:: get_example_config(name: str) -> ConfigurableClueConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableClueConfig

   :raises ValueError: If the example name is not found


.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

