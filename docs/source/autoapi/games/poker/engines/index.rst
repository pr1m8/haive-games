games.poker.engines
===================

.. py:module:: games.poker.engines

.. autoapi-nested-parse::

   Poker agent LLM configurations and prompts.

   This module defines the language model configurations and prompt templates
   for different poker playing styles and roles. It includes:
       - Player prompt generation for different styles
       - Hand analysis prompt generation
       - LLM provider selection and configuration
       - Agent configuration creation

   The module supports multiple LLM providers (Azure, DeepSeek, Anthropic, Gemini, Mistral) and
   configures them with appropriate models and prompts for poker gameplay.



Attributes
----------

.. autoapisummary::

   games.poker.engines.poker_agent_configs


Functions
---------

.. autoapisummary::

   games.poker.engines.create_default_agent_configs
   games.poker.engines.create_llm_config_for_provider
   games.poker.engines.create_poker_agent_configs
   games.poker.engines.generate_hand_analysis_prompt
   games.poker.engines.generate_poker_prompt
   games.poker.engines.get_available_providers
   games.poker.engines.get_model_for_provider
   games.poker.engines.get_poker_llm_provider


Module Contents
---------------

.. py:function:: create_default_agent_configs(config)

   Create default configurations for poker agents based on config.


.. py:function:: create_llm_config_for_provider(provider: haive.core.models.llm.base.LLMProvider, **kwargs)

   Create an LLM configuration for a specific provider.


.. py:function:: create_poker_agent_configs() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create structured configurations for poker agents.


.. py:function:: generate_hand_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a structured prompt for poker hand analysis.


.. py:function:: generate_poker_prompt(player_style: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a structured prompt for a poker player.


.. py:function:: get_available_providers() -> list[haive.core.models.llm.base.LLMProvider]

   Determine all available LLM providers based on environment variables.


.. py:function:: get_model_for_provider(provider: haive.core.models.llm.base.LLMProvider) -> str

   Get the best model for a given provider.


.. py:function:: get_poker_llm_provider() -> haive.core.models.llm.base.LLMProvider

   Determine the best available LLM provider.


.. py:data:: poker_agent_configs

