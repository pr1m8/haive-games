games.llm_config_factory
========================

.. py:module:: games.llm_config_factory

.. autoapi-nested-parse::

   Unified LLM configuration factory for games.

   This module provides a simplified factory for creating LLM configurations for game
   agents, leveraging the new haive.core.models.llm factory system.


   .. autolink-examples:: games.llm_config_factory
      :collapse:


Classes
-------

.. autoapisummary::

   games.llm_config_factory.GameLLMFactory


Functions
---------

.. autoapisummary::

   games.llm_config_factory.get_model_info
   games.llm_config_factory.list_available_models


Module Contents
---------------

.. py:class:: GameLLMFactory

   Factory for creating game-specific LLM configurations.

   This factory simplifies the process of creating LLM configurations for games by
   providing game-optimized defaults and leveraging the core LLM factory.



   .. autolink-examples:: GameLLMFactory
      :collapse:

   .. py:method:: create_game_llm_pair(player1_model: str = 'gpt-4', player2_model: str = 'gpt-4', game_type: str = 'strategic', temperature: float | None = None) -> tuple[haive.games.models.llm.LLMConfig, haive.games.models.llm.LLMConfig]
      :classmethod:


      Create a pair of LLM configs for two-player games.

      :param player1_model: Model string for player 1
      :param player2_model: Model string for player 2
      :param game_type: Type of game for temperature defaults
      :param temperature: Override temperature for both players

      :returns: Tuple of (player1_config, player2_config)

      .. rubric:: Examples

      >>> # Same model
      >>> p1, p2 = GameLLMFactory.create_game_llm_pair("gpt-4")

      >>> # Different models
      >>> p1, p2 = GameLLMFactory.create_game_llm_pair(
      ...     "claude-3-opus",
      ...     "gpt-4"
      ... )

      >>> # With providers
      >>> p1, p2 = GameLLMFactory.create_game_llm_pair(
      ...     "anthropic:claude-3-opus",
      ...     "openai:gpt-4"
      ... )


      .. autolink-examples:: create_game_llm_pair
         :collapse:


   .. py:method:: create_llm_config(model: str, temperature: float | None = None, game_type: str = 'default', **kwargs) -> haive.games.models.llm.LLMConfig
      :classmethod:


      Create an LLM configuration for a game.

      This method wraps the core create_llm_config with game-specific defaults.

      :param model: Model string (e.g., "gpt-4", "claude-3-opus", "anthropic:claude-3-sonnet")
      :param temperature: Temperature setting (uses game_type default if None)
      :param game_type: Type of game ("strategic", "creative", "precise", "competitive")
      :param \*\*kwargs: Additional parameters

      :returns: Configured LLM instance
      :rtype: LLMConfig

      .. rubric:: Examples

      >>> # Simple usage
      >>> config = GameLLMFactory.create_llm_config("gpt-4")

      >>> # Game-specific temperature
      >>> config = GameLLMFactory.create_llm_config(
      ...     "claude-3-opus",
      ...     game_type="strategic"
      ... )

      >>> # Custom parameters
      >>> config = GameLLMFactory.create_llm_config(
      ...     "gpt-4",
      ...     temperature=0.5,
      ...     max_tokens=1000
      ... )


      .. autolink-examples:: create_llm_config
         :collapse:


   .. py:method:: get_recommended_model(game_type: str, performance: str = 'default') -> str
      :classmethod:


      Get recommended model for a game type.

      :param game_type: Type of game ("chess", "creative", "strategic")
      :param performance: Performance tier ("fast", "default", "strong")

      :returns: Recommended model string

      .. rubric:: Examples

      >>> # Get default chess model
      >>> model = GameLLMFactory.get_recommended_model("chess")
      >>> print(model)  # "gpt-4"

      >>> # Get fast creative model
      >>> model = GameLLMFactory.get_recommended_model("creative", "fast")
      >>> print(model)  # "gpt-3.5-turbo"


      .. autolink-examples:: get_recommended_model
         :collapse:


   .. py:method:: list_game_models(game_type: str | None = None) -> dict[str, Any]
      :classmethod:


      List available models for games.

      :param game_type: Optional game type to get recommendations for

      :returns: Dictionary with model information

      .. rubric:: Examples

      >>> models = GameLLMFactory.list_game_models("chess")
      >>> print(models["recommendations"])


      .. autolink-examples:: list_game_models
         :collapse:


   .. py:attribute:: GAME_RECOMMENDATIONS
      :type:  dict[str, dict[str, str]]


   .. py:attribute:: GAME_TEMPERATURES
      :type:  dict[str, float]


.. py:function:: get_model_info(model: str) -> dict[str, Any]

   Placeholder for model info - not yet implemented in core.


   .. autolink-examples:: get_model_info
      :collapse:

.. py:function:: list_available_models() -> list

   Placeholder for listing models - not yet implemented in core.


   .. autolink-examples:: list_available_models
      :collapse:

