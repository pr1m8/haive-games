games.monopoly.prompts
======================

.. py:module:: games.monopoly.prompts

Module documentation for games.monopoly.prompts


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 functions</span>   </div>


      
            
            
            

.. admonition:: Functions (4)
   :class: info

   .. autoapisummary::

      games.monopoly.prompts.generate_move_decision_prompt
      games.monopoly.prompts.generate_property_decision_prompt
      games.monopoly.prompts.generate_strategy_analysis_prompt
      games.monopoly.prompts.generate_turn_decision_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_decision_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Creates a prompt for the player to decide on movement-related actions.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_property_decision_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Creates a prompt for the player to decide on property-related actions.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_strategy_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Creates a prompt for the player to analyze their strategic position.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_turn_decision_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Creates a prompt for the player to make all decisions for their turn.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.prompts import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

