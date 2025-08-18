games.battleship.prompts
========================

.. py:module:: games.battleship.prompts

Battleship game prompt templates.

This module provides prompt templates for various game actions in Battleship, including:
    - Ship placement
    - Move selection
    - Strategic analysis



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 functions</span>   </div>

.. autoapi-nested-parse::

   Battleship game prompt templates.

   This module provides prompt templates for various game actions in Battleship, including:
       - Ship placement
       - Move selection
       - Strategic analysis



      
            
            
            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.battleship.prompts.generate_analysis_prompt
      games.battleship.prompts.generate_move_prompt
      games.battleship.prompts.generate_ship_placement_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for strategic analysis.

            :param player: Player name/identifier

            :returns: ChatPromptTemplate for strategic analysis



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for move selection.

            :param player: Player name/identifier

            :returns: ChatPromptTemplate for move selection



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_ship_placement_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for strategic ship placement.

            :param player: Player name/identifier

            :returns: ChatPromptTemplate for ship placement decisions





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.prompts import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

