games.connect4.engines
======================

.. py:module:: games.connect4.engines


Attributes
----------

.. autoapisummary::

   games.connect4.engines.aug_llm_configs


Functions
---------

.. autoapisummary::

   games.connect4.engines.generate_analysis_prompt
   games.connect4.engines.generate_move_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a structured and detailed prompt for analyzing a Connect 4 position.


.. py:function:: generate_move_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a move in Connect 4.


.. py:data:: aug_llm_configs

