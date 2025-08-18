games.clue.engines
==================

.. py:module:: games.clue.engines

Engines for the Clue game.

This module contains the engines for the Clue game, including the player engines, guess
engines, and analysis engines.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Engines for the Clue game.

   This module contains the engines for the Clue game, including the player engines, guess
   engines, and analysis engines.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.clue.engines.clue_engines

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.clue.engines.generate_analysis_prompt
      games.clue.engines.generate_player_prompt

            

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

            Generate a prompt for analyzing Clue game state.

            This function constructs a prompt template for the analysis engine, which analyzes
            the current game state and provides insights.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_player_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for playing Clue.

            This function constructs a prompt template for the player engine, which makes
            guesses in the Clue game.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: clue_engines
            :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.clue.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

