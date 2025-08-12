
:py:mod:`games.mastermind.engines`
==================================

.. py:module:: games.mastermind.engines

Engines for the Mastermind game.

This module contains the engines for the Mastermind game, including the codemaker
engine, guess engines, and analyzer engines.


.. autolink-examples:: games.mastermind.engines
   :collapse:


Functions
---------

.. autoapisummary::

   games.mastermind.engines.generate_analysis_prompt
   games.mastermind.engines.generate_codemaker_prompt
   games.mastermind.engines.generate_guess_prompt

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing a Mastermind position.

   This function constructs a prompt template for the analyzer engine, which analyzes
   the current game state from the perspective of the specified player.



   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_codemaker_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for creating a secret code in Mastermind.

   This function constructs a prompt template for the codemaker engine, which generates
   a secret code for the Mastermind game.



   .. autolink-examples:: generate_codemaker_prompt
      :collapse:

.. py:function:: generate_guess_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a guess in Mastermind.

   This function constructs a prompt template for the guess engine, which generates a
   guess for the Mastermind game.



   .. autolink-examples:: generate_guess_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mastermind.engines
   :collapse:
   
.. autolink-skip:: next
