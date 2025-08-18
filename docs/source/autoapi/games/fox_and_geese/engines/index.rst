games.fox_and_geese.engines
===========================

.. py:module:: games.fox_and_geese.engines

Engines for the Fox and Geese game.

This module defines the engines for the Fox and Geese game, which includes the move and
analysis prompts.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Engines for the Fox and Geese game.

   This module defines the engines for the Fox and Geese game, which includes the move and
   analysis prompts.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.fox_and_geese.engines.fox_and_geese_engines

            
            
            

.. admonition:: Functions (4)
   :class: info

   .. autoapisummary::

      games.fox_and_geese.engines.generate_fox_analysis_prompt
      games.fox_and_geese.engines.generate_fox_move_prompt
      games.fox_and_geese.engines.generate_geese_analysis_prompt
      games.fox_and_geese.engines.generate_geese_move_prompt

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_fox_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for analyzing the Fox's position.

            This function constructs a prompt template for the fox analysis engine, which
            analyzes the current game state from the perspective of the fox player.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_fox_move_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for the fox to make a move.

            This function constructs a prompt template for the fox move engine, which generates
            a move for the Fox and Geese game.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_geese_analysis_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for analyzing the Geese's position.

            This function constructs a prompt template for the geese analysis engine, which
            analyzes the current game state from the perspective of the geese player.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: generate_geese_move_prompt() -> langchain_core.prompts.ChatPromptTemplate

            Generate a prompt for the geese to make a move.

            This function constructs a prompt template for the geese move engine, which
            generates a move for the Fox and Geese game.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: fox_and_geese_engines




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.fox_and_geese.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

