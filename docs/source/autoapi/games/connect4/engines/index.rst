
:py:mod:`games.connect4.engines`
================================

.. py:module:: games.connect4.engines



Functions
---------

.. autoapisummary::

   games.connect4.engines.generate_analysis_prompt
   games.connect4.engines.generate_move_prompt

.. py:function:: generate_analysis_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a structured and detailed prompt for analyzing a Connect 4 position.


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a move in Connect 4.


   .. autolink-examples:: generate_move_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.connect4.engines
   :collapse:
   
.. autolink-skip:: next
