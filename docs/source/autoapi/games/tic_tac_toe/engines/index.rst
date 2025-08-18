games.tic_tac_toe.engines
=========================

.. py:module:: games.tic_tac_toe.engines

Prompt generation and engine configuration for Tic Tac Toe agents.

This module defines prompt templates and model configurations for both move generation
and board analysis. These are used by agents to communicate with LLMs in a structured
and strategic way.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Prompt generation and engine configuration for Tic Tac Toe agents.

   This module defines prompt templates and model configurations for both move generation
   and board analysis. These are used by agents to communicate with LLMs in a structured
   and strategic way.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.tic_tac_toe.engines.tictactoe_engines

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.tic_tac_toe.engines.generate_analysis_prompt
      games.tic_tac_toe.engines.generate_move_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_analysis_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt template for analyzing a board position in Tic Tac Toe.

            :param player_symbol: The symbol ('X' or 'O') for the analyzing player.
            :type player_symbol: str

            :returns: A structured prompt for board analysis.
            :rtype: ChatPromptTemplate



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt template for making a move in Tic Tac Toe.

            :param player_symbol: The symbol ('X' or 'O') for which to generate the prompt.
            :type player_symbol: str

            :returns: A structured prompt for move generation.
            :rtype: ChatPromptTemplate



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: tictactoe_engines




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.tic_tac_toe.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

