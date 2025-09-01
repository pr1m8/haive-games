games.go.engines
================

.. py:module:: games.go.engines

.. autoapi-nested-parse::

   Go game engines using AugLLMConfig.

   This module provides LLM engine configurations for Go game agents, including:
       - Player engines for black and white players
       - Analyzer engines for position evaluation and strategy
       - Prompt templates with Go-specific instructions
       - Structured output models for moves and analysis

   The engines use LLM configurations optimized for strategic gameplay,
   with prompt templates designed to generate high-quality moves and analysis.



Functions
---------

.. autoapisummary::

   games.go.engines.build_go_aug_llms
   games.go.engines.generate_analysis_prompt
   games.go.engines.generate_black_prompt
   games.go.engines.generate_white_prompt
   games.go.engines.get_analyzer_engine
   games.go.engines.get_black_engine
   games.go.engines.get_white_engine


Module Contents
---------------

.. py:function:: build_go_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build augmented LLM configurations for Go game.

   :returns: Dictionary of engine configurations
   :rtype: dict[str, AugLLMConfig]


.. py:function:: generate_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate analysis prompt for Go position evaluation.

   :returns: A prompt template for position analysis
   :rtype: ChatPromptTemplate


.. py:function:: generate_black_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate prompt for black player.

   :returns: A prompt template for black player gameplay
   :rtype: ChatPromptTemplate


.. py:function:: generate_white_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate prompt for white player.

   :returns: A prompt template for white player gameplay
   :rtype: ChatPromptTemplate


.. py:function:: get_analyzer_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Get the game analyzer engine.


.. py:function:: get_black_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Get the black player engine.


.. py:function:: get_white_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Get the white player engine.


