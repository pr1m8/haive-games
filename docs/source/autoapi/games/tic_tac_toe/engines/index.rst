games.tic_tac_toe.engines
=========================

.. py:module:: games.tic_tac_toe.engines

.. autoapi-nested-parse::

   Prompt generation and engine configuration for Tic Tac Toe agents.

   This module defines prompt templates and model configurations for both move generation
   and board analysis. These are used by agents to communicate with LLMs in a structured
   and strategic way.



Attributes
----------

.. autoapisummary::

   games.tic_tac_toe.engines.tictactoe_engines


Functions
---------

.. autoapisummary::

   games.tic_tac_toe.engines.generate_analysis_prompt
   games.tic_tac_toe.engines.generate_move_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for analyzing a board position in Tic Tac Toe.

   :param player_symbol: The symbol ('X' or 'O') for the analyzing player.
   :type player_symbol: str

   :returns: A structured prompt for board analysis.
   :rtype: ChatPromptTemplate


.. py:function:: generate_move_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for making a move in Tic Tac Toe.

   :param player_symbol: The symbol ('X' or 'O') for which to generate the prompt.
   :type player_symbol: str

   :returns: A structured prompt for move generation.
   :rtype: ChatPromptTemplate


.. py:data:: tictactoe_engines

