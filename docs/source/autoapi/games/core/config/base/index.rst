games.core.config.base
======================

.. py:module:: games.core.config.base

.. autoapi-nested-parse::

   Base configuration classes for configurable games.

   from typing import Any This module provides the foundation for creating flexible game
   configurations that support multiple LLM providers and configuration modes.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/core/config/base/BaseGameConfig
   /autoapi/games/core/config/base/ConfigMode
   /autoapi/games/core/config/base/GamePlayerRole

.. autoapisummary::

   games.core.config.base.BaseGameConfig
   games.core.config.base.ConfigMode
   games.core.config.base.GamePlayerRole


Functions
---------

.. autoapisummary::

   games.core.config.base.create_advanced_config
   games.core.config.base.create_example_config
   games.core.config.base.create_llm_config
   games.core.config.base.create_simple_config


Module Contents
---------------

.. py:function:: create_advanced_config(config_class: type[BaseGameConfig], player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> BaseGameConfig

   Create a game configuration with detailed player configs.

   :param config_class: The game's configuration class
   :param player_configs: Dictionary mapping role names to PlayerAgentConfig
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured game instance


.. py:function:: create_example_config(config_class: type[BaseGameConfig], example_name: str, **kwargs) -> BaseGameConfig

   Create a game configuration from a predefined example.

   :param config_class: The game's configuration class
   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured game instance


.. py:function:: create_llm_config(model: str, **kwargs)

   Placeholder function until core factory is available.


.. py:function:: create_simple_config(config_class: type[BaseGameConfig], player1_model: str, player2_model: str, **kwargs) -> BaseGameConfig

   Create a simple game configuration with model strings.

   :param config_class: The game's configuration class
   :param player1_model: Model for player 1
   :param player2_model: Model for player 2
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured game instance


