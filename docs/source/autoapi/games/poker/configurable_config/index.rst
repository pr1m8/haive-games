
:py:mod:`games.poker.configurable_config`
=========================================

.. py:module:: games.poker.configurable_config

Configurable Poker configuration using the generic player agent system.

This module provides configurable Poker game configurations that replace hardcoded LLM
settings with dynamic, configurable player agents.


.. autolink-examples:: games.poker.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.poker.configurable_config.ConfigurablePokerConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurablePokerConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurablePokerConfig {
        node [shape=record];
        "ConfigurablePokerConfig" [label="ConfigurablePokerConfig"];
        "haive.games.poker.config.PokerAgentConfig" -> "ConfigurablePokerConfig";
      }

.. autoclass:: games.poker.configurable_config.ConfigurablePokerConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.poker.configurable_config.create_advanced_poker_config
   games.poker.configurable_config.create_budget_poker_config
   games.poker.configurable_config.create_experimental_poker_config
   games.poker.configurable_config.create_poker_config
   games.poker.configurable_config.create_poker_config_from_example
   games.poker.configurable_config.create_poker_config_from_player_configs
   games.poker.configurable_config.get_example_config
   games.poker.configurable_config.list_example_configurations

.. py:function:: create_advanced_poker_config(**kwargs) -> ConfigurablePokerConfig

   Create an advanced Poker configuration with powerful models.


   .. autolink-examples:: create_advanced_poker_config
      :collapse:

.. py:function:: create_budget_poker_config(**kwargs) -> ConfigurablePokerConfig

   Create a budget-friendly Poker configuration.


   .. autolink-examples:: create_budget_poker_config
      :collapse:

.. py:function:: create_experimental_poker_config(**kwargs) -> ConfigurablePokerConfig

   Create an experimental Poker configuration with mixed providers.


   .. autolink-examples:: create_experimental_poker_config
      :collapse:

.. py:function:: create_poker_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurablePokerConfig

   Create a configurable Poker configuration with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Poker game
   :rtype: ConfigurablePokerConfig

   .. rubric:: Example

   >>> config = create_poker_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_poker_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_poker_config
      :collapse:

.. py:function:: create_poker_config_from_example(example_name: str, **kwargs) -> ConfigurablePokerConfig

   Create a configurable Poker configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Poker game
   :rtype: ConfigurablePokerConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_poker_config_from_example("budget", enable_analysis=False)
   >>> config = create_poker_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_poker_config_from_example
      :collapse:

.. py:function:: create_poker_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurablePokerConfig

   Create a configurable Poker configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Poker game
   :rtype: ConfigurablePokerConfig

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
   ...         player_name="Strategic Poker Pro"
   ...     ),
   ...     "player2_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Poker Ace"
   ...     ),
   ...     "player1_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Poker Strategist"
   ...     ),
   ...     "player2_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Poker Analyst"
   ...     ),
   ... }
   >>> config = create_poker_config_from_player_configs(player_configs)


   .. autolink-examples:: create_poker_config_from_player_configs
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurablePokerConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurablePokerConfig

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

.. autolink-examples:: games.poker.configurable_config
   :collapse:
   
.. autolink-skip:: next
