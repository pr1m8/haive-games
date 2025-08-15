games.chess.aug_llms
====================

.. py:module:: games.chess.aug_llms

.. autoapi-nested-parse::

   Chess game augmented LLM configurations module.

   This module provides augmented LLM configurations for the chess game, including:
       - Move generation prompts for white and black players
       - Position analysis prompts for both sides
       - Structured output models for moves and analysis
       - Pre-configured LLM configurations for easy agent setup

   The module provides an alternative to the engines.py approach, with a focus
   on customizability and different prompt styles for chess gameplay.

   .. rubric:: Example

   >>> from haive.games.chess.aug_llms import aug_llm_configs
   >>>
   >>> # Access white player's move generation configuration
   >>> white_config = aug_llm_configs["white_player"]
   >>> white_prompt = white_config.prompt_template


   .. autolink-examples:: games.chess.aug_llms
      :collapse:


Attributes
----------

.. autoapisummary::

   games.chess.aug_llms.aug_llm_configs


Functions
---------

.. autoapisummary::

   games.chess.aug_llms.build_chess_aug_llms_per_color
   games.chess.aug_llms.generate_analysis_prompt
   games.chess.aug_llms.generate_move_prompt


Module Contents
---------------

.. py:function:: build_chess_aug_llms_per_color(*, white_llm: haive.core.models.llm.base.LLMConfig | None = AzureLLMConfig(), black_llm: haive.core.models.llm.base.LLMConfig | None = DeepSeekLLMConfig()) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Build LLM configs for both players and analyzers using per-color LLMs.

   Creates a comprehensive set of AugLLMConfig objects for chess gameplay,
   allowing different LLM providers for white and black players.

   :param white_llm: LLM configuration for white player and analyzer
   :type white_llm: LLMConfig | None
   :param black_llm: LLM configuration for black player and analyzer
   :type black_llm: LLMConfig | None

   :returns: Dictionary with configurations for all chess roles
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Examples

   >>> # Using default LLMs
   >>> configs = build_chess_aug_llms_per_color()
   >>> len(configs)
   4
   >>> sorted(list(configs.keys()))
   ['black_analyzer', 'black_player', 'white_analyzer', 'white_player']

   >>> # Using custom LLMs
   >>> from haive.core.models.llm.base import AnthropicLLMConfig
   >>> configs = build_chess_aug_llms_per_color(
   ...     white_llm=AnthropicLLMConfig(model="claude-3-opus-20240229"),
   ...     black_llm=AnthropicLLMConfig(model="claude-3-sonnet-20240229"),
   ... )
   >>> configs["white_player"].llm_config.model
   'claude-3-opus-20240229'


   .. autolink-examples:: build_chess_aug_llms_per_color
      :collapse:

.. py:function:: generate_analysis_prompt(color: str) -> langchain.prompts.ChatPromptTemplate

   Generate an analysis prompt for a given player color.

   Creates a ChatPromptTemplate with system and human messages designed
   to elicit detailed position analysis from an LLM.

   :param color: Player color ("white" or "black")
   :type color: str

   :returns: A prompt template for generating chess position analysis
   :rtype: ChatPromptTemplate

   .. rubric:: Examples

   >>> black_prompt = generate_analysis_prompt("black")
   >>> isinstance(black_prompt, ChatPromptTemplate)
   True
   >>> "strategic themes" in black_prompt.messages[1][1]
   True


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(color: str) -> langchain.prompts.ChatPromptTemplate

   Generate a move prompt for a given player color.

   Creates a ChatPromptTemplate with system and human messages designed
   to elicit high-quality chess moves from an LLM.

   :param color: Player color ("white" or "black")
   :type color: str

   :returns: A prompt template for generating chess moves
   :rtype: ChatPromptTemplate

   .. rubric:: Examples

   >>> white_prompt = generate_move_prompt("white")
   >>> isinstance(white_prompt, ChatPromptTemplate)
   True
   >>> "UCI format" in white_prompt.messages[0][1]
   True


   .. autolink-examples:: generate_move_prompt
      :collapse:

.. py:data:: aug_llm_configs
   :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]

