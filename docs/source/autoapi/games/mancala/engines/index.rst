games.mancala.engines
=====================

.. py:module:: games.mancala.engines

Engines for the Mancala game.

This module defines the engines for the Mancala game, including the move and analysis
prompts.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Engines for the Mancala game.

   This module defines the engines for the Mancala game, including the move and analysis
   prompts.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mancala.engines.mancala_engines

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.mancala.engines.generate_analysis_prompt
      games.mancala.engines.generate_move_prompt

            

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

            Generate a prompt for analyzing a Mancala position.

            This function constructs a prompt template for the analysis engine, which analyzes
            the current game state from the perspective of the specified player.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for making a move in Mancala.

            This function constructs a prompt template for the move engine, which generates a
            move for the Mancala game.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: mancala_engines




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mancala.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

