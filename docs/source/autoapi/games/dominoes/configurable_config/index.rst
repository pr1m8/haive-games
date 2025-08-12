
:py:mod:`games.dominoes.configurable_config`
============================================

.. py:module:: games.dominoes.configurable_config

Configurable Dominoes configuration using the generic player agent system.

This module provides configurable Dominoes game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.dominoes.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.dominoes.configurable_config.ConfigurableDominoesConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableDominoesConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableDominoesConfig {
        node [shape=record];
        "ConfigurableDominoesConfig" [label="ConfigurableDominoesConfig"];
        "haive.games.dominoes.config.DominoesAgentConfig" -> "ConfigurableDominoesConfig";
      }

.. autoclass:: games.dominoes.configurable_config.ConfigurableDominoesConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.dominoes.configurable_config.create_advanced_dominoes_config
   games.dominoes.configurable_config.create_budget_dominoes_config
   games.dominoes.configurable_config.create_dominoes_config
   games.dominoes.configurable_config.create_dominoes_config_from_example
   games.dominoes.configurable_config.create_dominoes_config_from_player_configs
   games.dominoes.configurable_config.create_experimental_dominoes_config
   games.dominoes.configurable_config.get_example_config
   games.dominoes.configurable_config.list_example_configurations

.. py:function:: create_advanced_dominoes_config(**kwargs) -> ConfigurableDominoesConfig

   Create an advanced Dominoes configuration with powerful models.


   .. autolink-examples:: create_advanced_dominoes_config
      :collapse:

.. py:function:: create_budget_dominoes_config(**kwargs) -> ConfigurableDominoesConfig

   Create a budget-friendly Dominoes configuration.


   .. autolink-examples:: create_budget_dominoes_config
      :collapse:

.. py:function:: create_dominoes_config(player1_model: str = 'gpt-4o', player2_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableDominoesConfig

   Create a configurable Dominoes configuration with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Dominoes game
   :rtype: ConfigurableDominoesConfig

   .. rubric:: Example

   >>> config = create_dominoes_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_dominoes_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     enable_analysis=True
   ... )


   .. autolink-examples:: create_dominoes_config
      :collapse:

.. py:function:: create_dominoes_config_from_example(example_name: str, **kwargs) -> ConfigurableDominoesConfig

   Create a configurable Dominoes configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Dominoes game
   :rtype: ConfigurableDominoesConfig

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay

   .. rubric:: Example

   >>> config = create_dominoes_config_from_example("budget", enable_analysis=False)
   >>> config = create_dominoes_config_from_example("advanced", visualize_game=True)


   .. autolink-examples:: create_dominoes_config_from_example
      :collapse:

.. py:function:: create_dominoes_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableDominoesConfig

   Create a configurable Dominoes configuration from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Dominoes game
   :rtype: ConfigurableDominoesConfig

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
   ...         player_name="Strategic Domino Master"
   ...     ),
   ...     "player2_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical Domino Expert"
   ...     ),
   ...     "player1_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="Dominoes Strategist"
   ...     ),
   ...     "player2_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="Dominoes Analyst"
   ...     ),
   ... }
   >>> config = create_dominoes_config_from_player_configs(player_configs)


   .. autolink-examples:: create_dominoes_config_from_player_configs
      :collapse:

.. py:function:: create_experimental_dominoes_config(**kwargs) -> ConfigurableDominoesConfig

   Create an experimental Dominoes configuration with mixed providers.


   .. autolink-examples:: create_experimental_dominoes_config
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableDominoesConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableDominoesConfig

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

.. autolink-examples:: games.dominoes.configurable_config
   :collapse:
   
.. autolink-skip:: next
