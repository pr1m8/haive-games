
:py:mod:`games.poker.prompts`
=============================

.. py:module:: games.poker.prompts

Enhanced prompt templates for poker agent with structured output.

This module provides improved prompt templates for the poker agent that:
1. Clearly instruct models to use structured output format
2. Include more detailed game context and examples
3. Provide clear instruction on legal moves
4. Have better formatting for readability by LLMs


.. autolink-examples:: games.poker.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   games.poker.prompts.get_example_decisions
   games.poker.prompts.get_system_prompt

.. py:function:: get_example_decisions(player_style: str) -> list

   Get example decisions appropriate for the playing style.


   .. autolink-examples:: get_example_decisions
      :collapse:

.. py:function:: get_system_prompt(player_style: str) -> str

   Get the system prompt for a given player style.


   .. autolink-examples:: get_system_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.poker.prompts
   :collapse:
   
.. autolink-skip:: next
