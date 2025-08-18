games.debate.engines
====================

.. py:module:: games.debate.engines

Module documentation for games.debate.engines


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">7 functions</span>   </div>


      
            
            
            

.. admonition:: Functions (7)
   :class: info

   .. autoapisummary::

      games.debate.engines.build_debate_engines
      games.debate.engines.generate_debater_prompt
      games.debate.engines.generate_defense_prompt
      games.debate.engines.generate_judge_prompt
      games.debate.engines.generate_moderator_prompt
      games.debate.engines.generate_persona_prompt
      games.debate.engines.generate_prosecutor_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_debate_engines() -> dict[str, dict[str, haive.core.engine.aug_llm.AugLLMConfig]]

            Build engines for different debate roles.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_debater_prompt(position: str = None) -> langchain_core.prompts.ChatPromptTemplate


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_defense_prompt() -> langchain_core.prompts.ChatPromptTemplate


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_judge_prompt() -> langchain_core.prompts.ChatPromptTemplate


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_moderator_prompt() -> langchain_core.prompts.ChatPromptTemplate


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_persona_prompt(persona_traits: dict[str, str]) -> langchain_core.prompts.ChatPromptTemplate


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_prosecutor_prompt() -> langchain_core.prompts.ChatPromptTemplate




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.debate.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

