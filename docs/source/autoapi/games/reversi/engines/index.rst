games.reversi.engines
=====================

.. py:module:: games.reversi.engines


Attributes
----------

.. autoapisummary::

   games.reversi.engines.reversi_engines


Functions
---------

.. autoapisummary::

   games.reversi.engines.generate_analysis_prompt
   games.reversi.engines.generate_move_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing a Reversi/Othello position.


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a move in Reversi/Othello.


   .. autolink-examples:: generate_move_prompt
      :collapse:

.. py:data:: reversi_engines

