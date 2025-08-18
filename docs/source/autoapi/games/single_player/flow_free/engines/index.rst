games.single_player.flow_free.engines
=====================================

.. py:module:: games.single_player.flow_free.engines

Prompt generation and engine configuration for Flow Free.

This module defines prompt templates and LLM configurations for move generation and
position analysis in the Flow Free game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Prompt generation and engine configuration for Flow Free.

   This module defines prompt templates and LLM configurations for move generation and
   position analysis in the Flow Free game.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.single_player.flow_free.engines.flow_free_engines

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.single_player.flow_free.engines.generate_analysis_prompt
      games.single_player.flow_free.engines.generate_move_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt template for Flow Free position analysis.

            :returns: A prompt template for position analysis.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt template for Flow Free move generation.

            :returns: A prompt template for move generation.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: flow_free_engines




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.flow_free.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

