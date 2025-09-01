games.mancala.configurable_config
=================================

.. py:module:: games.mancala.configurable_config

.. autoapi-nested-parse::

   Configurable Mancala configuration using the generic player agent system.

   This module provides configurable Mancala game configurations that replace hardcoded LLM
   settings with dynamic, configurable player agents.



Attributes
----------

.. autoapisummary::

   games.mancala.configurable_config.EXAMPLE_CONFIGURATIONS
   games.mancala.configurable_config.config1


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mancala/configurable_config/ConfigurableMancalaConfig

.. autoapisummary::

   games.mancala.configurable_config.ConfigurableMancalaConfig


Functions
---------

.. autoapisummary::

   games.mancala.configurable_config.create_advanced_mancala_config
   games.mancala.configurable_config.create_budget_mancala_config
   games.mancala.configurable_config.create_experimental_mancala_config
   games.mancala.configurable_config.create_mancala_config
   games.mancala.configurable_config.create_mancala_config_from_example
   games.mancala.configurable_config.create_mancala_config_from_player_configs
   games.mancala.configurable_config.get_example_config
   games.mancala.configurable_config.list_example_configurations


Module Contents
---------------

.. py:function:: create_advanced_mancala_config(**kwargs) -> ConfigurableMancalaConfig

   Create an advanced Mancala configuration with powerful models.


.. py:function:: create_budget_mancala_config(**kwargs) -> ConfigurableMancalaConfig

   Create a budget-friendly Mancala configuration.


.. py:function:: create_experimental_mancala_config(**kwargs) -> ConfigurableMancalaConfig

   Create an experimental Mancala configuration with mixed providers.


.. py:function:: create_mancala_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableMancalaConfig

   Create a configurable Mancala configuration with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mancala game
   :rtype: ConfigurableMancalaConfig

   .. rubric:: Examples

   >>> config = create_mancala_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_mancala_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


.. py:function:: create_mancala_config_from_example(example_name: str, **kwargs) -> ConfigurableMancalaConfig

   Create a configurable Mancala configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Mancala game
   :rtype: ConfigurableMancalaConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Examples

   >>> config = create_mancala_config_from_example("budget", enable_analysis=False)
   >>> config = create_mancala_config_from_example("advanced", visualize_game=True)


.. py:function:: create_mancala_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableMancalaConfig

   Create a configurable Mancala configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Mancala game
   :rtype: ConfigurableMancalaConfig

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration

   .. rubric:: Examples

   >>> player_configs = {
   ...     "player1_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic Mancala Player"
   ...     ),
   ...     "player2_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Mancala Expert"
   ...     ),
   ...     "player1_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Mancala Strategist"
   ...     ),
   ...     "player2_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Mancala Analyst"
   ...     ),
   ... }
   >>> config = create_mancala_config_from_player_configs(player_configs)


.. py:function:: get_example_config(name: str) -> ConfigurableMancalaConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableMancalaConfig

   :raises ValueError: If the example name is not found


.. py:function:: list_example_configurations() -> dict[str, str]

   List all available example configurations.

   :returns: Mapping of configuration names to descriptions
   :rtype: Dict[str, str]


.. py:data:: EXAMPLE_CONFIGURATIONS

.. py:data:: config1

