
:py:mod:`games.nim.engines`
===========================

.. py:module:: games.nim.engines

Engines for the Nim game.


.. autolink-examples:: games.nim.engines
   :collapse:


Functions
---------

.. autoapisummary::

   games.nim.engines.generate_analysis_prompt
   games.nim.engines.generate_move_prompt

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for analyzing a Nim position with structured output.

   :param player: The player to generate the analysis for.
   :type player: str


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for making a move in Nim.

   :param player: The player to generate the prompt for.
   :type player: str


   .. autolink-examples:: generate_move_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.nim.engines
   :collapse:
   
.. autolink-skip:: next
