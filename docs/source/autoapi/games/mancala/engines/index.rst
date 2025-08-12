
:py:mod:`games.mancala.engines`
===============================

.. py:module:: games.mancala.engines

Engines for the Mancala game.

This module defines the engines for the Mancala game, including the move and analysis
prompts.


.. autolink-examples:: games.mancala.engines
   :collapse:


Functions
---------

.. autoapisummary::

   games.mancala.engines.generate_analysis_prompt
   games.mancala.engines.generate_move_prompt

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing a Mancala position.

   This function constructs a prompt template for the analysis engine, which analyzes
   the current game state from the perspective of the specified player.



   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a move in Mancala.

   This function constructs a prompt template for the move engine, which generates a
   move for the Mancala game.



   .. autolink-examples:: generate_move_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mancala.engines
   :collapse:
   
.. autolink-skip:: next
