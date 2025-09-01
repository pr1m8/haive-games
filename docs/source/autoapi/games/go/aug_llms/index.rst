games.go.aug_llms
=================

.. py:module:: games.go.aug_llms

.. autoapi-nested-parse::

   Go game LLM augmentations.

   This module provides augmented LLM configurations for Go game agents, including:
       - Move generation prompts for black and white players
       - Position analysis prompts for both sides
       - Structured output models for moves and analysis
       - Pre-configured LLM configurations for easy agent setup

   .. rubric:: Example

   >>> from haive.games.go.aug_llms import aug_llm_configs
   >>>
   >>> # Get black player's move generation config
   >>> black_config = aug_llm_configs["black_player"]
   >>>
   >>> # Generate a prompt
   >>> prompt = black_config.prompt_template.format(
   ...     board_size=19,
   ...     recent_moves=[(0, "black", (3, 4))],
   ...     captured_stones={"black": 0, "white": 0},
   ...     player_analysis="Territory is balanced"
   ... )



Attributes
----------

.. autoapisummary::

   games.go.aug_llms.aug_llm_configs


Functions
---------

.. autoapisummary::

   games.go.aug_llms.generate_go_analysis_prompt
   games.go.aug_llms.generate_go_move_prompt


Module Contents
---------------

.. py:function:: generate_go_analysis_prompt(color: str) -> langchain.prompts.ChatPromptTemplate

   Generate a position analysis prompt for a Go player.

   This function creates a ChatPromptTemplate that guides an LLM to:
       - Analyze the position from a specific color's perspective
       - Evaluate territory and influence
       - Identify key positions
       - Suggest strategic plans

   :param color: The player color ("black" or "white") to analyze for.
   :type color: str

   :returns: A prompt template for position analysis.
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_go_analysis_prompt("black")
   >>> formatted = prompt.format(
   ...     board_size=19,
   ...     recent_moves=[(0, "black", (3, 4))],
   ...     captured_stones={"black": 0, "white": 0}
   ... )

   .. rubric:: Notes

   The prompt includes:
   - System role definition as an analyst
   - Game context (board size, move history)
   - Captured stones count
   - Structured analysis tasks:
       1. Territory assessment
       2. Key position identification
       3. Strategic planning


.. py:function:: generate_go_move_prompt(color: str) -> langchain.prompts.ChatPromptTemplate

   Generate a move prompt for a Go player.

   This function creates a ChatPromptTemplate that guides an LLM to:
       - Play as a specific color in Go
       - Consider the current game context
       - Make legal moves in coordinate format
       - Follow Go strategy and rules

   :param color: The player color ("black" or "white").
   :type color: str

   :returns: A prompt template for move generation.
   :rtype: ChatPromptTemplate

   .. rubric:: Example

   >>> prompt = generate_go_move_prompt("black")
   >>> formatted = prompt.format(
   ...     board_size=19,
   ...     recent_moves=[(0, "black", (3, 4))],
   ...     captured_stones={"black": 0, "white": 0},
   ...     player_analysis="Territory is balanced"
   ... )

   .. rubric:: Notes

   The prompt includes:
   - System role definition as the specified color
   - Game context (board size, move history)
   - Captured stones count
   - Previous position analysis
   - Clear instruction for move format


.. py:data:: aug_llm_configs

