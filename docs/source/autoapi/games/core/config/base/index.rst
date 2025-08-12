
:py:mod:`games.core.config.base`
================================

.. py:module:: games.core.config.base

Base configuration classes for configurable games.

from typing import Any This module provides the foundation for creating flexible game
configurations that support multiple LLM providers and configuration modes.


.. autolink-examples:: games.core.config.base
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.config.base.BaseGameConfig
   games.core.config.base.ConfigMode
   games.core.config.base.GamePlayerRole


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BaseGameConfig:

   .. graphviz::
      :align: center

      digraph inheritance_BaseGameConfig {
        node [shape=record];
        "BaseGameConfig" [label="BaseGameConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "BaseGameConfig";
        "abc.ABC" -> "BaseGameConfig";
      }

.. autoclass:: games.core.config.base.BaseGameConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigMode:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigMode {
        node [shape=record];
        "ConfigMode" [label="ConfigMode"];
        "str" -> "ConfigMode";
        "enum.Enum" -> "ConfigMode";
      }

.. autoclass:: games.core.config.base.ConfigMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ConfigMode** is an Enum defined in ``games.core.config.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePlayerRole:

   .. graphviz::
      :align: center

      digraph inheritance_GamePlayerRole {
        node [shape=record];
        "GamePlayerRole" [label="GamePlayerRole"];
        "pydantic.BaseModel" -> "GamePlayerRole";
      }

.. autopydantic_model:: games.core.config.base.GamePlayerRole
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:



Functions
---------

.. autoapisummary::

   games.core.config.base.create_advanced_config
   games.core.config.base.create_example_config
   games.core.config.base.create_llm_config
   games.core.config.base.create_simple_config

.. py:function:: create_advanced_config(config_class: type[BaseGameConfig], player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> BaseGameConfig

   Create a game configuration with detailed player configs.

   :param config_class: The game's configuration class
   :param player_configs: Dictionary mapping role names to PlayerAgentConfig
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured game instance


   .. autolink-examples:: create_advanced_config
      :collapse:

.. py:function:: create_example_config(config_class: type[BaseGameConfig], example_name: str, **kwargs) -> BaseGameConfig

   Create a game configuration from a predefined example.

   :param config_class: The game's configuration class
   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured game instance


   .. autolink-examples:: create_example_config
      :collapse:

.. py:function:: create_llm_config(model: str, **kwargs)

   Placeholder function until core factory is available.


   .. autolink-examples:: create_llm_config
      :collapse:

.. py:function:: create_simple_config(config_class: type[BaseGameConfig], player1_model: str, player2_model: str, **kwargs) -> BaseGameConfig

   Create a simple game configuration with model strings.

   :param config_class: The game's configuration class
   :param player1_model: Model for player 1
   :param player2_model: Model for player 2
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured game instance


   .. autolink-examples:: create_simple_config
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.core.config.base
   :collapse:
   
.. autolink-skip:: next
