games.monopoly.engines
======================

.. py:module:: games.monopoly.engines

Monopoly engines and prompts module.

This module provides LLM configurations and prompts for monopoly player decisions,
including:
    - Property purchase decisions
    - Jail action decisions
    - Building decisions
    - Trade negotiations



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span> • <span class="module-stat">4 attributes</span>   </div>

.. autoapi-nested-parse::

   Monopoly engines and prompts module.

   This module provides LLM configurations and prompts for monopoly player decisions,
   including:
       - Property purchase decisions
       - Jail action decisions
       - Building decisions
       - Trade negotiations



      

.. admonition:: Attributes (4)
   :class: tip

   .. autoapisummary::

      games.monopoly.engines.building_decision_prompt
      games.monopoly.engines.jail_decision_prompt
      games.monopoly.engines.property_decision_prompt
      games.monopoly.engines.trade_decision_prompt

            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.monopoly.engines.build_monopoly_player_aug_llms

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_monopoly_player_aug_llms() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Build LLM configs for monopoly player decisions.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: building_decision_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: jail_decision_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: property_decision_prompt


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: trade_decision_prompt




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.monopoly.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

