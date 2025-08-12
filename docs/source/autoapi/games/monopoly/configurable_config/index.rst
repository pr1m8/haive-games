
:py:mod:`games.monopoly.configurable_config`
============================================

.. py:module:: games.monopoly.configurable_config

Configurable Monopoly configuration using the generic player agent system.

This module provides configurable Monopoly game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.monopoly.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.monopoly.configurable_config.ConfigurableMonopolyConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableMonopolyConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableMonopolyConfig {
        node [shape=record];
        "ConfigurableMonopolyConfig" [label="ConfigurableMonopolyConfig"];
        "haive.games.monopoly.config.MonopolyGameAgentConfig" -> "ConfigurableMonopolyConfig";
      }

.. autoclass:: games.monopoly.configurable_config.ConfigurableMonopolyConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.monopoly.configurable_config.create_budget_monopoly_config
   games.monopoly.configurable_config.create_experimental_monopoly_config
   games.monopoly.configurable_config.create_monopoly_config
   games.monopoly.configurable_config.create_monopoly_config_from_example
   games.monopoly.configurable_config.create_monopoly_config_from_player_configs
   games.monopoly.configurable_config.create_property_tycoon_monopoly_config
   games.monopoly.configurable_config.create_real_estate_mogul_monopoly_config
   games.monopoly.configurable_config.get_example_config
   games.monopoly.configurable_config.list_example_configurations

.. py:function:: create_budget_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig

   Create a budget-friendly Monopoly configuration.


   .. autolink-examples:: create_budget_monopoly_config
      :collapse:

.. py:function:: create_experimental_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig

   Create an experimental Monopoly configuration with mixed providers.


   .. autolink-examples:: create_experimental_monopoly_config
      :collapse:

.. py:function:: create_monopoly_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableMonopolyConfig

   Create a configurable Monopoly configuration with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Monopoly game
   :rtype: ConfigurableMonopolyConfig

   .. rubric:: Example

   >>> config = create_monopoly_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_monopoly_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_trading=True
   ... )


   .. autolink-examples:: create_monopoly_config
      :collapse:

.. py:function:: create_monopoly_config_from_example(example_name: str, **kwargs) -> ConfigurableMonopolyConfig

   Create a configurable Monopoly configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Monopoly game
   :rtype: ConfigurableMonopolyConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "real_estate_moguls": High-powered models for strategic gameplay
       - "property_tycoons": Specialized for property investment

   .. rubric:: Example

   >>> config = create_monopoly_config_from_example("budget", enable_trading=False)
   >>> config = create_monopoly_config_from_example("real_estate_moguls", enable_building=True)


   .. autolink-examples:: create_monopoly_config_from_example
      :collapse:

.. py:function:: create_monopoly_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableMonopolyConfig

   Create a configurable Monopoly configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Monopoly game
   :rtype: ConfigurableMonopolyConfig

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "player1_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Property Mogul"
   ...     ),
   ...     "player2_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Real Estate Tycoon"
   ...     ),
   ...     "player1_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Investment Strategist"
   ...     ),
   ...     "player2_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Market Analyst"
   ...     ),
   ... }
   >>> config = create_monopoly_config_from_player_configs(player_configs)


   .. autolink-examples:: create_monopoly_config_from_player_configs
      :collapse:

.. py:function:: create_property_tycoon_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig

   Create a property tycoon-style Monopoly configuration.


   .. autolink-examples:: create_property_tycoon_monopoly_config
      :collapse:

.. py:function:: create_real_estate_mogul_monopoly_config(**kwargs) -> ConfigurableMonopolyConfig

   Create a real estate mogul-style Monopoly configuration with powerful models.


   .. autolink-examples:: create_real_estate_mogul_monopoly_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableMonopolyConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableMonopolyConfig

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

.. autolink-examples:: games.monopoly.configurable_config
   :collapse:
   
.. autolink-skip:: next
