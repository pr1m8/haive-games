games.chess.llm_utils
=====================

.. py:module:: games.chess.llm_utils

.. autoapi-nested-parse::

   Chess-specific LLM utilities using the game LLM factory.

   This module provides chess-specific utilities for creating and configuring LLMs for
   chess gameplay, building on the core LLM factory system.


   .. autolink-examples:: games.chess.llm_utils
      :collapse:


Functions
---------

.. autoapisummary::

   games.chess.llm_utils.create_chess_engines_from_config
   games.chess.llm_utils.create_chess_engines_simple
   games.chess.llm_utils.get_available_chess_providers
   games.chess.llm_utils.get_recommended_chess_models


Module Contents
---------------

.. py:function:: create_chess_engines_from_config(white_config: dict[str, Any], black_config: dict[str, Any], enable_analysis: bool = True, analyzer_configs: dict[str, dict[str, Any]] | None = None) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create chess engines from simple configuration dictionaries.

   :param white_config: Config for white player with 'provider', 'model', etc.
   :param black_config: Config for black player with 'provider', 'model', etc.
   :param enable_analysis: Whether to create analyzer engines
   :param analyzer_configs: Optional separate configs for analyzers

   :returns: Dictionary of AugLLMConfig objects for all chess roles

   .. rubric:: Examples

   >>> # Simple provider-only config
   >>> engines = create_chess_engines_from_config(
   ...     white_config={"provider": "anthropic"},
   ...     black_config={"provider": "openai"}
   ... )

   >>> # With custom models
   >>> engines = create_chess_engines_from_config(
   ...     white_config={
   ...         "provider": "anthropic",
   ...         "model": "claude-3-opus-20240229"
   ...     },
   ...     black_config={
   ...         "provider": "azure",
   ...         "model": "gpt-4-turbo"
   ...     }
   ... )

   >>> # Separate analyzer configs
   >>> engines = create_chess_engines_from_config(
   ...     white_config={"provider": "anthropic"},
   ...     black_config={"provider": "openai"},
   ...     analyzer_configs={
   ...         "white": {"provider": "azure"},
   ...         "black": {"provider": "azure"}
   ...     }
   ... )


   .. autolink-examples:: create_chess_engines_from_config
      :collapse:

.. py:function:: create_chess_engines_simple(white_provider: str = 'anthropic', white_model: str | None = None, black_provider: str = 'anthropic', black_model: str | None = None, temperature: float | None = None, enable_analysis: bool = True) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create chess engines with simple provider/model specification.

   :param white_provider: Provider for white (e.g., "anthropic", "openai")
   :param white_model: Model for white (uses default if None)
   :param black_provider: Provider for black
   :param black_model: Model for black (uses default if None)
   :param temperature: Temperature for all engines
   :param enable_analysis: Whether to create analyzer engines

   :returns: Dictionary of AugLLMConfig objects

   .. rubric:: Examples

   >>> # Use defaults
   >>> engines = create_chess_engines_simple()

   >>> # Different providers
   >>> engines = create_chess_engines_simple(
   ...     white_provider="anthropic",
   ...     black_provider="openai"
   ... )

   >>> # Custom models
   >>> engines = create_chess_engines_simple(
   ...     white_provider="anthropic",
   ...     white_model="claude-3-opus-20240229",
   ...     black_provider="openai",
   ...     black_model="gpt-4-turbo"
   ... )


   .. autolink-examples:: create_chess_engines_simple
      :collapse:

.. py:function:: get_available_chess_providers() -> list[str]

   Get list of available LLM providers for chess.

   :returns: List of provider names


   .. autolink-examples:: get_available_chess_providers
      :collapse:

.. py:function:: get_recommended_chess_models() -> dict[str, str]

   Get recommended models for chess gameplay.

   :returns: Dictionary mapping providers to recommended models


   .. autolink-examples:: get_recommended_chess_models
      :collapse:

