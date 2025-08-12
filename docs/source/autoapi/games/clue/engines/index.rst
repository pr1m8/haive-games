
:py:mod:`games.clue.engines`
============================

.. py:module:: games.clue.engines

Engines for the Clue game.

This module contains the engines for the Clue game, including the player engines, guess
engines, and analysis engines.


.. autolink-examples:: games.clue.engines
   :collapse:


Functions
---------

.. autoapisummary::

   games.clue.engines.generate_analysis_prompt
   games.clue.engines.generate_player_prompt

.. py:function:: generate_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing Clue game state.

   This function constructs a prompt template for the analysis engine, which analyzes
   the current game state and provides insights.



   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_player_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for playing Clue.

   This function constructs a prompt template for the player engine, which makes
   guesses in the Clue game.



   .. autolink-examples:: generate_player_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.clue.engines
   :collapse:
   
.. autolink-skip:: next
