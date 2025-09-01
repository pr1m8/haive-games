games.mastermind.configurable_config
====================================

.. py:module:: games.mastermind.configurable_config

.. autoapi-nested-parse::

   Configurable Mastermind configuration using the generic player agent system.

   This module provides configurable Mastermind game configurations that replace hardcoded
   LLM settings with dynamic, configurable player agents.



Attributes
----------

.. autoapisummary::

   games.mastermind.configurable_config.EXAMPLE_CONFIGURATIONS
   games.mastermind.configurable_config.config1


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mastermind/configurable_config/ConfigurableMastermindConfig

.. autoapisummary::

   games.mastermind.configurable_config.ConfigurableMastermindConfig


Functions
---------

.. autoapisummary::

   games.mastermind.configurable_config.create_advanced_mastermind_config
   games.mastermind.configurable_config.create_budget_mastermind_config
   games.mastermind.configurable_config.create_experimental_mastermind_config
   games.mastermind.configurable_config.create_mastermind_config
   games.mastermind.configurable_config.create_mastermind_config_from_example
   games.mastermind.configurable_config.create_mastermind_config_from_player_configs
   games.mastermind.configurable_config.get_example_config
   games.mastermind.configurable_config.list_example_configurations


Module Contents
---------------

.. py:function:: create_advanced_mastermind_config(**kwargs) -> ConfigurableMastermindConfig

   Create an advanced Mastermind configuration with powerful models.


.. py:function:: create_budget_mastermind_config(**kwargs) -> ConfigurableMastermindConfig

   Create a budget-friendly Mastermind configuration.


.. py:function:: create_experimental_mastermind_config(**kwargs) -> ConfigurableMastermindConfig

   Create an experimental Mastermind configuration with mixed providers.


.. py:function:: create_mastermind_config(codemaker_model: str = 'gpt-4o', codebreaker_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableMastermindConfig

   Create a configurable Mastermind configuration with simple model specifications.

   :param codemaker_model: Model for codemaker and analyzer
   :param codebreaker_model: Model for codebreaker and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mastermind game
   :rtype: ConfigurableMastermindConfig

   .. rubric:: Examples

   >>> config = create_mastermind_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_mastermind_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


.. py:function:: create_mastermind_config_from_example(example_name: str, **kwargs) -> ConfigurableMastermindConfig

   Create a configurable Mastermind configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Mastermind game
   :rtype: ConfigurableMastermindConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Examples

   >>> config = create_mastermind_config_from_example("budget", enable_analysis=False)
   >>> config = create_mastermind_config_from_example("advanced", visualize_game=True)


.. py:function:: create_mastermind_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableMastermindConfig

   Create a configurable Mastermind configuration from detailed player.
   configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mastermind game
   :rtype: ConfigurableMastermindConfig

   Expected roles:
       - "codemaker_player": Player 1 configuration
       - "codebreaker_player": Player 2 configuration
       - "codemaker_analyzer": Player 1 analyzer configuration
       - "codebreaker_analyzer": Player 2 analyzer configuration

   .. rubric:: Examples

   >>> player_configs = {
   ...     "codemaker_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Codemaker"
   ...     ),
   ...     "codebreaker_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Codebreaker"
   ...     ),
   ...     "codemaker_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Mastermind Strategist"
   ...     ),
   ...     "codebreaker_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Mastermind Analyst"
   ...     ),
   ... }
   >>> config = create_mastermind_config_from_player_configs(player_configs)


.. py:function:: get_example_config(name: str) -> ConfigurableMastermindConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableMastermindConfig

   :raises ValueError: If the example name is not found


.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

