games.chess.configurable_config
===============================

.. py:module:: games.chess.configurable_config

.. autoapi-nested-parse::

   Configurable chess agent configuration using player agents.

   This module provides a chess configuration that supports configurable player agents
   instead of hardcoded engine configurations.



Attributes
----------

.. autoapisummary::

   games.chess.configurable_config.ChessConfigV2


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/chess/configurable_config/ConfigurableChessConfig

.. autoapisummary::

   games.chess.configurable_config.ConfigurableChessConfig


Functions
---------

.. autoapisummary::

   games.chess.configurable_config.create_chess_config
   games.chess.configurable_config.create_chess_config_from_example
   games.chess.configurable_config.create_chess_config_from_player_configs


Module Contents
---------------

.. py:function:: create_chess_config(white_model: str = 'gpt-4o', black_model: str = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, enable_analysis: bool = True, **kwargs) -> ConfigurableChessConfig

   Create a chess configuration with simple model strings.

   :param white_model: Model for white player
   :param black_model: Model for black player
   :param temperature: Temperature for all engines
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured chess agent
   :rtype: ConfigurableChessConfig

   .. rubric:: Example

   >>> config = create_chess_config("gpt-4", "claude-3-opus", temperature=0.8)


.. py:function:: create_chess_config_from_example(example_name: str, enable_analysis: bool = True, **kwargs) -> ConfigurableChessConfig

   Create a chess configuration from an example.

   :param example_name: Name of the example configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured chess agent
   :rtype: ConfigurableChessConfig

   Available examples: anthropic_vs_openai, gpt4_only, claude_only,
                      mixed_providers, budget_friendly

   .. rubric:: Example

   >>> config = create_chess_config_from_example("budget_friendly")


.. py:function:: create_chess_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], enable_analysis: bool = True, **kwargs) -> ConfigurableChessConfig

   Create a chess configuration from player agent configurations.

   :param player_configs: Dictionary of role to player configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured chess agent
   :rtype: ConfigurableChessConfig

   .. rubric:: Example

   >>> configs = {
   ...     "white_player": create_player_config("gpt-4", player_name="Deep Blue"),
   ...     "black_player": create_player_config("claude-3-opus", player_name="AlphaZero"),
   ... }
   >>> config = create_chess_config_from_player_configs(configs)


.. py:data:: ChessConfigV2

