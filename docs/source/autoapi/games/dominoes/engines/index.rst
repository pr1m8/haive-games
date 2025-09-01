games.dominoes.engines
======================

.. py:module:: games.dominoes.engines


Attributes
----------

.. autoapisummary::

   games.dominoes.engines.aug_llm_configs


Functions
---------

.. autoapisummary::

   games.dominoes.engines.generate_analysis_prompt
   games.dominoes.engines.generate_move_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing a dominoes position.


.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a move in dominoes.


.. py:data:: aug_llm_configs

