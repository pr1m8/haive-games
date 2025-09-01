games.fox_and_geese.engines
===========================

.. py:module:: games.fox_and_geese.engines

.. autoapi-nested-parse::

   Engines for the Fox and Geese game.

   This module defines the engines for the Fox and Geese game, which includes the move and
   analysis prompts.



Attributes
----------

.. autoapisummary::

   games.fox_and_geese.engines.fox_and_geese_engines


Functions
---------

.. autoapisummary::

   games.fox_and_geese.engines.generate_fox_analysis_prompt
   games.fox_and_geese.engines.generate_fox_move_prompt
   games.fox_and_geese.engines.generate_geese_analysis_prompt
   games.fox_and_geese.engines.generate_geese_move_prompt


Module Contents
---------------

.. py:function:: generate_fox_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing the Fox's position.

   This function constructs a prompt template for the fox analysis engine, which
   analyzes the current game state from the perspective of the fox player.



.. py:function:: generate_fox_move_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for the fox to make a move.

   This function constructs a prompt template for the fox move engine, which generates
   a move for the Fox and Geese game.



.. py:function:: generate_geese_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing the Geese's position.

   This function constructs a prompt template for the geese analysis engine, which
   analyzes the current game state from the perspective of the geese player.



.. py:function:: generate_geese_move_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for the geese to make a move.

   This function constructs a prompt template for the geese move engine, which
   generates a move for the Fox and Geese game.



.. py:data:: fox_and_geese_engines

