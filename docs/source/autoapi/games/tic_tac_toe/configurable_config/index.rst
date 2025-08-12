
:py:mod:`games.tic_tac_toe.configurable_config`
===============================================

.. py:module:: games.tic_tac_toe.configurable_config

Configurable Tic-Tac-Toe configuration using the generic player agent system.

This module provides configurable Tic-Tac-Toe game configurations that replace hardcoded
LLM settings with dynamic, configurable player agents.


.. autolink-examples:: games.tic_tac_toe.configurable_config
   :collapse:

Classes
-------

.. autoapisummary::

   games.tic_tac_toe.configurable_config.ConfigurableTicTacToeConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableTicTacToeConfig:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableTicTacToeConfig {
        node [shape=record];
        "ConfigurableTicTacToeConfig" [label="ConfigurableTicTacToeConfig"];
        "haive.games.tic_tac_toe.config.TicTacToeConfig" -> "ConfigurableTicTacToeConfig";
      }

.. autoclass:: games.tic_tac_toe.configurable_config.ConfigurableTicTacToeConfig
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.tic_tac_toe.configurable_config.create_budget_ttt_config
   games.tic_tac_toe.configurable_config.create_experimental_ttt_config
   games.tic_tac_toe.configurable_config.create_quick_ttt_config
   games.tic_tac_toe.configurable_config.create_ttt_config
   games.tic_tac_toe.configurable_config.create_ttt_config_from_example
   games.tic_tac_toe.configurable_config.create_ttt_config_from_player_configs
   games.tic_tac_toe.configurable_config.get_example_config
   games.tic_tac_toe.configurable_config.list_example_configurations

.. py:function:: create_budget_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig

   Create a budget-friendly Tic-Tac-Toe configuration.


   .. autolink-examples:: create_budget_ttt_config
      :collapse:

.. py:function:: create_experimental_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig

   Create an experimental Tic-Tac-Toe configuration with mixed providers.


   .. autolink-examples:: create_experimental_ttt_config
      :collapse:

.. py:function:: create_quick_ttt_config(**kwargs) -> ConfigurableTicTacToeConfig

   Create a quick Tic-Tac-Toe configuration with fast models.


   .. autolink-examples:: create_quick_ttt_config
      :collapse:

.. py:function:: create_ttt_config(x_model: str = 'gpt-4o', o_model: str = 'claude-3-5-sonnet-20240620', **kwargs) -> ConfigurableTicTacToeConfig

   Create a configurable Tic-Tac-Toe configuration with simple model specifications.

   :param x_model: Model for X player and analyzer
   :param o_model: Model for O player and analyzer
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Tic-Tac-Toe game
   :rtype: ConfigurableTicTacToeConfig

   .. rubric:: Example

   >>> config = create_ttt_config("gpt-4o", "claude-3-opus", temperature=0.5)
   >>> config = create_ttt_config(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     max_moves=9
   ... )


   .. autolink-examples:: create_ttt_config
      :collapse:

.. py:function:: create_ttt_config_from_example(example_name: str, **kwargs) -> ConfigurableTicTacToeConfig

   Create a configurable Tic-Tac-Toe configuration from a predefined example.

   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured Tic-Tac-Toe game
   :rtype: ConfigurableTicTacToeConfig

   Available examples:
       - "gpt_vs_claude": GPT-4 vs Claude
       - "gpt_only": GPT-4 for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role

   .. rubric:: Example

   >>> config = create_ttt_config_from_example("budget", max_moves=9)
   >>> config = create_ttt_config_from_example("gpt_vs_claude", enable_analysis=False)


   .. autolink-examples:: create_ttt_config_from_example
      :collapse:

.. py:function:: create_ttt_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> ConfigurableTicTacToeConfig

   Create a configurable Tic-Tac-Toe configuration from detailed player.
   configurations.

   :param player_configs: Dictionary mapping role names to player configurations
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Tic-Tac-Toe game
   :rtype: ConfigurableTicTacToeConfig

   Expected roles:
       - "X_player": X player configuration
       - "O_player": O player configuration
       - "X_analyzer": X analyzer configuration
       - "O_analyzer": O analyzer configuration

   .. rubric:: Example

   >>> player_configs = {
   ...     "X_player": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.7,
   ...         player_name="Strategic X"
   ...     ),
   ...     "O_player": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.3,
   ...         player_name="Tactical O"
   ...     ),
   ...     "X_analyzer": PlayerAgentConfig(
   ...         llm_config="gpt-4o",
   ...         temperature=0.2,
   ...         player_name="X Analyst"
   ...     ),
   ...     "O_analyzer": PlayerAgentConfig(
   ...         llm_config="claude-3-opus",
   ...         temperature=0.2,
   ...         player_name="O Analyst"
   ...     ),
   ... }
   >>> config = create_ttt_config_from_player_configs(player_configs)


   .. autolink-examples:: create_ttt_config_from_player_configs
      :collapse:

.. py:function:: get_example_config(name: str) -> ConfigurableTicTacToeConfig

   Get a predefined example configuration by name.

   :param name: Name of the example configuration

   :returns: The example configuration
   :rtype: ConfigurableTicTacToeConfig

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

.. autolink-examples:: games.tic_tac_toe.configurable_config
   :collapse:
   
.. autolink-skip:: next
