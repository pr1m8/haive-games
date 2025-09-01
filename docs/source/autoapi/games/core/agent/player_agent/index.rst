games.core.agent.player_agent
=============================

.. py:module:: games.core.agent.player_agent

.. autoapi-nested-parse::

   Configurable player agent system for games.

   This module provides a flexible player agent abstraction that allows games to use
   different LLM configurations for players without hardcoding them in engines.

   The system supports:
   - Dynamic LLM configuration per player
   - Role-based agent configuration (player, analyzer, etc.)
   - Easy swapping of LLMs and models
   - Integration with the new LLM factory system



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/core/agent/player_agent/ConfigurableGameAgent
   /autoapi/games/core/agent/player_agent/GamePlayerRole
   /autoapi/games/core/agent/player_agent/PlayerAgentConfig
   /autoapi/games/core/agent/player_agent/PlayerAgentFactory
   /autoapi/games/core/agent/player_agent/PlayerRole

.. autoapisummary::

   games.core.agent.player_agent.ConfigurableGameAgent
   games.core.agent.player_agent.GamePlayerRole
   games.core.agent.player_agent.PlayerAgentConfig
   games.core.agent.player_agent.PlayerAgentFactory
   games.core.agent.player_agent.PlayerRole


Functions
---------

.. autoapisummary::

   games.core.agent.player_agent.create_llm_config
   games.core.agent.player_agent.create_player_config
   games.core.agent.player_agent.create_simple_player_configs


Module Contents
---------------

.. py:function:: create_llm_config(model: str, **kwargs) -> haive.core.models.llm.LLMConfig

   Create an LLM config based on model string.

   This is a simple helper to create configs until a proper factory is available.



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


.. py:function:: create_simple_player_configs(white_model: str | haive.core.models.llm.LLMConfig = 'gpt-4', black_model: str | haive.core.models.llm.LLMConfig = 'claude-3-opus', temperature: float | None = None, **kwargs) -> dict[str, PlayerAgentConfig]

   Create simple player configurations for two-player games.

   :param white_model: Model for white/first player
   :param black_model: Model for black/second player
   :param temperature: Temperature for both players
   :param \*\*kwargs: Additional configuration parameters

   :returns: Player configurations
   :rtype: Dict[str, PlayerAgentConfig]

   .. rubric:: Examples

   >>> configs = create_simple_player_configs("gpt-4", "claude-3-opus", temperature=0.7)
   >>> # Creates configs for white_player, black_player, white_analyzer, black_analyzer


