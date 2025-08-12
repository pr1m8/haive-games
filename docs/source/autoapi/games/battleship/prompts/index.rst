
:py:mod:`games.battleship.prompts`
==================================

.. py:module:: games.battleship.prompts

Battleship game prompt templates.

This module provides prompt templates for various game actions in Battleship, including:
    - Ship placement
    - Move selection
    - Strategic analysis


.. autolink-examples:: games.battleship.prompts
   :collapse:


Functions
---------

.. autoapisummary::

   games.battleship.prompts.generate_analysis_prompt
   games.battleship.prompts.generate_move_prompt
   games.battleship.prompts.generate_ship_placement_prompt

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for strategic analysis.

   :param player: Player name/identifier

   :returns: ChatPromptTemplate for strategic analysis


   .. autolink-examples:: generate_analysis_prompt
      :collapse:

.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for move selection.

   :param player: Player name/identifier

   :returns: ChatPromptTemplate for move selection


   .. autolink-examples:: generate_move_prompt
      :collapse:

.. py:function:: generate_ship_placement_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for strategic ship placement.

   :param player: Player name/identifier

   :returns: ChatPromptTemplate for ship placement decisions


   .. autolink-examples:: generate_ship_placement_prompt
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.battleship.prompts
   :collapse:
   
.. autolink-skip:: next
