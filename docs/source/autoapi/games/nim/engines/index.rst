games.nim.engines
=================

.. py:module:: games.nim.engines

Engines for the Nim game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Engines for the Nim game.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.nim.engines.nim_engines

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.nim.engines.generate_analysis_prompt
      games.nim.engines.generate_move_prompt

            

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

            Generate a prompt for analyzing a Nim position with structured output.

            :param player: The player to generate the analysis for.
            :type player: str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for making a move in Nim.

            :param player: The player to generate the prompt for.
            :type player: str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: nim_engines




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

