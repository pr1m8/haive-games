games.single_player.flow_free.engines
=====================================

.. py:module:: games.single_player.flow_free.engines

.. autoapi-nested-parse::

   Prompt generation and engine configuration for Flow Free.

   This module defines prompt templates and LLM configurations for move generation and
   position analysis in the Flow Free game.


   .. autolink-examples:: games.single_player.flow_free.engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.single_player.flow_free.engines.flow_free_engines


Functions
---------

.. autoapisummary::

   games.single_player.flow_free.engines.generate_analysis_prompt
   games.single_player.flow_free.engines.generate_move_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for Flow Free position analysis.

   :returns: A prompt template for position analysis.


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt() -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt template for Flow Free move generation.

   :returns: A prompt template for move generation.


   .. autolink-examples:: generate_move_prompt
      :collapse:

.. py:data:: flow_free_engines

