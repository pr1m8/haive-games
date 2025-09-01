games.chess.engines
===================

.. py:module:: games.chess.engines

.. autoapi-nested-parse::

   Chess game engines using AugLLMConfig.

   This module provides LLM engine configurations for chess game agents, including:
       - Player engines for white and black
       - Analyzer engines for position evaluation
       - Prompt templates with chess-specific instructions
       - Structured output models for moves and analysis

   The engines use different LLM configurations optimized for their specific roles,
   with prompt templates designed to generate high-quality chess moves and analysis.



Functions
---------

.. autoapisummary::

   games.chess.engines.build_chess_aug_llms
   games.chess.engines.create_black_analyzer_engine
   games.chess.engines.create_black_player_engine
   games.chess.engines.create_white_analyzer_engine
   games.chess.engines.create_white_player_engine


Module Contents
---------------

.. py:function:: build_chess_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build AugLLMConfig dictionary for chess game engines.

   Creates a complete set of engine configurations for a chess agent,
   including players and analyzers for both white and black.

   :returns:

             Dictionary of engine configurations with keys:
                 - "white_player": Engine for white's moves
                 - "black_player": Engine for black's moves
                 - "white_analyzer": Engine for analyzing positions from white's perspective
                 - "black_analyzer": Engine for analyzing positions from black's perspective
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Examples

   >>> engines = build_chess_aug_llms()
   >>> len(engines)
   4
   >>> sorted(list(engines.keys()))
   ['black_analyzer', 'black_player', 'white_analyzer', 'white_player']


.. py:function:: create_black_analyzer_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Create black analyzer engine configuration.

   Configures an LLM engine for analyzing chess positions from black's
   perspective, providing structured analysis with:
   - Position evaluation score
   - Attacking opportunities
   - Defensive needs
   - Strategic plans

   :returns: Configuration for the black analyzer engine
   :rtype: AugLLMConfig

   .. rubric:: Examples

   >>> engine = create_black_analyzer_engine()
   >>> engine.name
   'black_analyzer'
   >>> engine.structured_output_model
   <class 'haive.games.chess.models.SegmentedAnalysis'>


.. py:function:: create_black_player_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Create black player engine configuration.

   Configures an LLM engine for generating black's chess moves with:
   - Specific instructions for UCI move format
   - Examples of valid moves
   - Structured output using ChessPlayerDecision model
   - Appropriate temperature for strategic play

   :returns: Configuration for the black player engine
   :rtype: AugLLMConfig

   .. rubric:: Examples

   >>> engine = create_black_player_engine()
   >>> engine.name
   'black_player'
   >>> engine.structured_output_model
   <class 'haive.games.chess.models.ChessPlayerDecision'>


.. py:function:: create_white_analyzer_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Create white analyzer engine configuration.

   Configures an LLM engine for analyzing chess positions from white's
   perspective, providing structured analysis with:
   - Position evaluation score
   - Attacking opportunities
   - Defensive needs
   - Strategic plans

   :returns: Configuration for the white analyzer engine
   :rtype: AugLLMConfig

   .. rubric:: Examples

   >>> engine = create_white_analyzer_engine()
   >>> engine.name
   'white_analyzer'
   >>> engine.structured_output_model
   <class 'haive.games.chess.models.SegmentedAnalysis'>


.. py:function:: create_white_player_engine() -> haive.core.engine.aug_llm.AugLLMConfig

   Create white player engine configuration.

   Configures an LLM engine for generating white's chess moves with:
   - Specific instructions for UCI move format
   - Examples of valid moves
   - Structured output using ChessPlayerDecision model
   - Appropriate temperature for strategic play

   :returns: Configuration for the white player engine
   :rtype: AugLLMConfig

   .. rubric:: Examples

   >>> engine = create_white_player_engine()
   >>> engine.name
   'white_player'
   >>> engine.structured_output_model
   <class 'haive.games.chess.models.ChessPlayerDecision'>


