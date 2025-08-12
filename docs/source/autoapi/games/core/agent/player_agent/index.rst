
:py:mod:`games.core.agent.player_agent`
=======================================

.. py:module:: games.core.agent.player_agent

Configurable player agent system for games.

This module provides a flexible player agent abstraction that allows games to use
different LLM configurations for players without hardcoding them in engines.

The system supports:
- Dynamic LLM configuration per player
- Role-based agent configuration (player, analyzer, etc.)
- Easy swapping of LLMs and models
- Integration with the new LLM factory system


.. autolink-examples:: games.core.agent.player_agent
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.agent.player_agent.ConfigurableGameAgent
   games.core.agent.player_agent.GamePlayerRole
   games.core.agent.player_agent.PlayerAgentConfig
   games.core.agent.player_agent.PlayerAgentFactory
   games.core.agent.player_agent.PlayerRole


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ConfigurableGameAgent:

   .. graphviz::
      :align: center

      digraph inheritance_ConfigurableGameAgent {
        node [shape=record];
        "ConfigurableGameAgent" [label="ConfigurableGameAgent"];
        "abc.ABC" -> "ConfigurableGameAgent";
      }

.. autoclass:: games.core.agent.player_agent.ConfigurableGameAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePlayerRole:

   .. graphviz::
      :align: center

      digraph inheritance_GamePlayerRole {
        node [shape=record];
        "GamePlayerRole" [label="GamePlayerRole"];
        "pydantic.BaseModel" -> "GamePlayerRole";
      }

.. autopydantic_model:: games.core.agent.player_agent.GamePlayerRole
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerAgentConfig:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerAgentConfig {
        node [shape=record];
        "PlayerAgentConfig" [label="PlayerAgentConfig"];
        "pydantic.BaseModel" -> "PlayerAgentConfig";
      }

.. autopydantic_model:: games.core.agent.player_agent.PlayerAgentConfig
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





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerAgentFactory:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerAgentFactory {
        node [shape=record];
        "PlayerAgentFactory" [label="PlayerAgentFactory"];
      }

.. autoclass:: games.core.agent.player_agent.PlayerAgentFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerRole:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerRole {
        node [shape=record];
        "PlayerRole" [label="PlayerRole"];
        "Protocol" -> "PlayerRole";
      }

.. autoclass:: games.core.agent.player_agent.PlayerRole
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.core.agent.player_agent.create_llm_config
   games.core.agent.player_agent.create_player_config
   games.core.agent.player_agent.create_simple_player_configs

.. py:function:: create_llm_config(model: str, **kwargs) -> haive.core.models.llm.LLMConfig

   Create an LLM config based on model string.

   This is a simple helper to create configs until a proper factory is available.



   .. autolink-examples:: create_llm_config
      :collapse:

.. py:function:: create_player_config(model: str | haive.core.models.llm.LLMConfig, temperature: float | None = None, player_name: str | None = None, **kwargs) -> PlayerAgentConfig

   Create a player agent configuration.

   :param model: Model string, LLMConfig instance, or config dict
   :param temperature: Temperature setting
   :param player_name: Human-readable name for the player
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured player agent
   :rtype: PlayerAgentConfig

   .. rubric:: Examples

   >>> config = create_player_config("gpt-4", temperature=0.7)
   >>> config = create_player_config("anthropic:claude-3-opus")
   >>> config = create_player_config({"model": "gpt-4", "provider": "openai"})


   .. autolink-examples:: create_player_config
      :collapse:

.. py:function:: create_simple_player_configs(white_model: str | haive.core.models.llm.LLMConfig = 'gpt-4', black_model: str | haive.core.models.llm.LLMConfig = 'claude-3-opus', temperature: float | None = None, **kwargs) -> dict[str, PlayerAgentConfig]

   Create simple player configurations for two-player games.

   :param white_model: Model for white/first player
   :param black_model: Model for black/second player
   :param temperature: Temperature for both players
   :param \*\*kwargs: Additional configuration parameters

   :returns: Player configurations
   :rtype: Dict[str, PlayerAgentConfig]

   .. rubric:: Example

   >>> configs = create_simple_player_configs("gpt-4", "claude-3-opus", temperature=0.7)
   >>> # Creates configs for white_player, black_player, white_analyzer, black_analyzer


   .. autolink-examples:: create_simple_player_configs
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.core.agent.player_agent
   :collapse:
   
.. autolink-skip:: next
