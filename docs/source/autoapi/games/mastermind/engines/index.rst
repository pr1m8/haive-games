games.mastermind.engines
========================

.. py:module:: games.mastermind.engines

Engines for the Mastermind game.

This module contains the engines for the Mastermind game, including the codemaker
engine, guess engines, and analyzer engines.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Engines for the Mastermind game.

   This module contains the engines for the Mastermind game, including the codemaker
   engine, guess engines, and analyzer engines.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mastermind.engines.mastermind_engines

            
            
            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.mastermind.engines.generate_analysis_prompt
      games.mastermind.engines.generate_codemaker_prompt
      games.mastermind.engines.generate_guess_prompt

            

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

            Generate a prompt for analyzing a Mastermind position.

            This function constructs a prompt template for the analyzer engine, which analyzes
            the current game state from the perspective of the specified player.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_codemaker_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for creating a secret code in Mastermind.

            This function constructs a prompt template for the codemaker engine, which generates
            a secret code for the Mastermind game.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_guess_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for making a guess in Mastermind.

            This function constructs a prompt template for the guess engine, which generates a
            guess for the Mastermind game.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: mastermind_engines




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mastermind.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

