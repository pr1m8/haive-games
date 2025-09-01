games.battleship.prompts
========================

.. py:module:: games.battleship.prompts

.. autoapi-nested-parse::

   Battleship game prompt templates.

   This module provides prompt templates for various game actions in Battleship, including:
       - Ship placement
       - Move selection
       - Strategic analysis



Functions
---------

.. autoapisummary::

   games.battleship.prompts.generate_analysis_prompt
   games.battleship.prompts.generate_move_prompt
   games.battleship.prompts.generate_ship_placement_prompt


Module Contents
---------------

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for strategic analysis.

   :param player: Player name/identifier

   :returns: ChatPromptTemplate for strategic analysis


.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for move selection.

   :param player: Player name/identifier

   :returns: ChatPromptTemplate for move selection


.. py:function:: generate_ship_placement_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

   Generate a prompt for strategic ship placement.

   :param player: Player name/identifier

   :returns: ChatPromptTemplate for ship placement decisions


