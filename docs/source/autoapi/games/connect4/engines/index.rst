games.connect4.engines
======================

.. py:module:: games.connect4.engines

Module documentation for games.connect4.engines


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.connect4.engines.aug_llm_configs

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.connect4.engines.generate_analysis_prompt
      games.connect4.engines.generate_move_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_analysis_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a structured and detailed prompt for analyzing a Connect 4 position.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for making a move in Connect 4.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: aug_llm_configs




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.connect4.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

