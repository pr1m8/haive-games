games.clue.engines
==================

.. py:module:: games.clue.engines

.. autoapi-nested-parse::

   Engines for the Clue game.

   This module contains the engines for the Clue game, including the player engines, guess
   engines, and analysis engines.



Attributes
----------

.. autoapisummary::

   games.clue.engines.clue_engines


Functions
---------

.. autoapisummary::

   games.clue.engines.generate_analysis_prompt
   games.clue.engines.generate_player_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing Clue game state.

   This function constructs a prompt template for the analysis engine, which analyzes
   the current game state and provides insights.



.. py:function:: generate_player_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for playing Clue.

   This function constructs a prompt template for the player engine, which makes
   guesses in the Clue game.



.. py:data:: clue_engines
   :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]

