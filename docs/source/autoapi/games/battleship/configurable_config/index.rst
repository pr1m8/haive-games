
:py:mod:`games.battleship.configurable_config`
==============================================

.. py:module:: games.battleship.configurable_config

Configurable Battleship configuration using the generic player agent system.

This module provides configurable Battleship game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.battleship.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.battleship.configurable_config.ConfigurableBattleshipConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableBattleshipConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableBattleshipConfig {
        node [shape=record];
        "ConfigurableBattleshipConfig" [label="ConfigurableBattleshipConfig"];
        "haive.games.battleship.config.BattleshipAgentConfig" -> "ConfigurableBattleshipConfig";
      }

.. autoclass:: games.battleship.configurable_config.ConfigurableBattleshipConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.battleship.configurable_config.create_battleship_config
   games.battleship.configurable_config.create_battleship_config_from_example
   games.battleship.configurable_config.create_battleship_config_from_player_configs
   games.battleship.configurable_config.create_budget_battleship_config
   games.battleship.configurable_config.create_experimental_battleship_config
   games.battleship.configurable_config.create_naval_battleship_config
   games.battleship.configurable_config.get_example_config
   games.battleship.configurable_config.list_example_configurations

.. py:function:: create_battleship_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableBattleshipConfig

   Create a configurable Battleship configuration with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Battleship game
   :rtype: ConfigurableBattleshipConfig

   .. rubric:: Example

   >>> config = create_battleship_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_battleship_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_battleship_config
      :collapse:

.. py:function:: create_battleship_config_from_example(example_name: str, **kwargs) -> ConfigurableBattleshipConfig

   Create a configurable Battleship configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Battleship game
   :rtype: ConfigurableBattleshipConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "naval_commanders": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_battleship_config_from_example("budget", enable_analysis=False)
   >>> config = create_battleship_config_from_example("naval_commanders", visualize_board=True)


   .. autolink-examples:: create_battleship_config_from_example
      :collapse:

.. py:function:: create_battleship_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableBattleshipConfig

   Create a configurable Battleship configuration from detailed player.
   configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Battleship game
   :rtype: ConfigurableBattleshipConfig

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
   ...         player_name="Strategic Admiral"
   ...     ),
   ...     "player2_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Captain"
   ...     ),
   ...     "player1_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Naval Strategist"
   ...     ),
   ...     "player2_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Fleet Analyst"
   ...     ),
   ... }
   >>> config = create_battleship_config_from_player_configs(player_configs)


   .. autolink-examples:: create_battleship_config_from_player_configs
      :collapse:

.. py:function:: create_budget_battleship_config(**kwargs) -> ConfigurableBattleshipConfig

   Create a budget-friendly Battleship configuration.


   .. autolink-examples:: create_budget_battleship_config
      :collapse:

.. py:function:: create_experimental_battleship_config(**kwargs) -> ConfigurableBattleshipConfig

   Create an experimental Battleship configuration with mixed providers.


   .. autolink-examples:: create_experimental_battleship_config
      :collapse:

.. py:function:: create_naval_battleship_config(**kwargs) -> ConfigurableBattleshipConfig

   Create a naval commander-style Battleship configuration with powerful models.


   .. autolink-examples:: create_naval_battleship_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableBattleshipConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableBattleshipConfig

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

.. autolink-examples:: games.battleship.configurable_config
   :collapse:
   
.. autolink-skip:: next
