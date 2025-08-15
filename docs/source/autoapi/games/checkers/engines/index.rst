games.checkers.engines
======================

.. py:module:: games.checkers.engines

.. autoapi-nested-parse::

   Checkers game engines using AugLLMConfig.

   This module provides LLM engine configurations for checkers game agents, including:
       - Player engines for red and black
       - Analyzer engines for position evaluation
       - Prompt templates with checkers-specific instructions
       - Structured output models for moves and analysis

   The engines use LLM configurations optimized for checkers gameplay,
   with prompt templates designed to generate high-quality moves and analysis.


   .. autolink-examples:: games.checkers.engines
      :collapse:


Functions
---------

.. autoapisummary::

   games.checkers.engines.build_checkers_aug_llms
   games.checkers.engines.generate_analysis_prompt
   games.checkers.engines.generate_move_prompt


Module Contents
---------------

.. py:function:: build_checkers_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build LLM configs for checkers players and analyzers.

   Creates a complete set of AugLLMConfig objects for checkers gameplay,
   including player and analyzer engines for both red and black.

   All engines use the same LLM model (GPT-4o) with appropriate temperature
   for move generation and analysis, with the corresponding prompt templates
   and structured output models.

   :returns:

             Dictionary with configurations for all checkers roles:
                 - "red_player": Engine for red's moves
                 - "black_player": Engine for black's moves
                 - "red_analyzer": Engine for analyzing positions from red's perspective
                 - "black_analyzer": Engine for analyzing positions from black's perspective
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Examples

   >>> engines = build_checkers_aug_llms()
   >>> len(engines)
   4
   >>> sorted(list(engines.keys()))
   ['black_analyzer', 'black_player', 'red_analyzer', 'red_player']
   >>> engines["red_player"].structured_output_model
   <class 'haive.games.checkers.models.CheckersPlayerDecision'>


   .. autolink-examples:: build_checkers_aug_llms
      :collapse:

.. py:function:: generate_analysis_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate analysis prompt for checkers.

   Creates a ChatPromptTemplate with system and human messages designed
   to elicit detailed position analysis from an LLM. The prompt includes:
   - Instructions on what aspects to analyze
   - Current board state and game context
   - Output format specifications

   :param color: Player color to analyze for ("red" or "black")
   :type color: str

   :returns: A prompt template for generating position analysis
   :rtype: ChatPromptTemplate

   .. rubric:: Examples

   >>> black_prompt = generate_analysis_prompt("black")
   >>> "BLACK" in black_prompt.messages[0][1]  # First message content
   True
   >>> "material_advantage" in black_prompt.messages[0][1]  # Output format specification
   True


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate move selection prompt for checkers.

   Creates a ChatPromptTemplate with system and human messages designed
   to elicit high-quality checkers moves from an LLM. The prompt includes:
   - Clear instructions on move format and rules
   - Game context like board state and move history
   - Error feedback for retries
   - Output format specifications

   :param color: Player color ("red" or "black")
   :type color: str

   :returns: A prompt template for generating checkers moves
   :rtype: ChatPromptTemplate

   .. rubric:: Examples

   >>> red_prompt = generate_move_prompt("red")
   >>> red_prompt.messages[0][0]  # First message role
   'system'
   >>> "You are playing checkers as RED" in red_prompt.messages[0][1]  # First message content
   True


   .. autolink-examples:: generate_move_prompt
      :collapse:

