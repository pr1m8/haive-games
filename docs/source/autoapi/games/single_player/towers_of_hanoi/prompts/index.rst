games.single_player.towers_of_hanoi.prompts
===========================================

.. py:module:: games.single_player.towers_of_hanoi.prompts

Tower of Hanoi prompts.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">6 attributes</span>   </div>

.. autoapi-nested-parse::

   Tower of Hanoi prompts.



      

.. admonition:: Attributes (6)
   :class: tip

   .. autoapisummary::

      games.single_player.towers_of_hanoi.prompts.HANOI_ANALYSIS_HUMAN_PROMPT
      games.single_player.towers_of_hanoi.prompts.HANOI_ANALYSIS_SYSTEM_PROMPT
      games.single_player.towers_of_hanoi.prompts.HANOI_MOVE_HUMAN_PROMPT
      games.single_player.towers_of_hanoi.prompts.HANOI_MOVE_SYSTEM_PROMPT
      games.single_player.towers_of_hanoi.prompts.analysis_prompt_template
      games.single_player.towers_of_hanoi.prompts.move_prompt_template

            
            
            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: HANOI_ANALYSIS_HUMAN_PROMPT
            :value: Multiline-String

            .. raw:: html

               <details><summary>Show Value</summary>

            .. code-block:: python

               """# Current State
               {state}
               
               # Game Information
               - Number of disks: {num_disks}
               - Moves made so far: {moves_made}
               - Optimal solution requires: {optimal_moves} moves
               
               # Valid Moves
               {valid_moves}
               
               Please provide a detailed strategic analysis of this position. Think step-by-step about the best approach to solve the puzzle optimally."""

            .. raw:: html

               </details>




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: HANOI_ANALYSIS_SYSTEM_PROMPT
            :value: Multiline-String

            .. raw:: html

               <details><summary>Show Value</summary>

            .. code-block:: python

               """You are an expert Tower of Hanoi solver providing in-depth analysis.
               
               The Tower of Hanoi is a puzzle with the following rules:
               1. There are three pegs labeled 1, 2, and 3
               2. There are different sized disks stacked on the pegs
               3. Only one disk can be moved at a time
               4. A larger disk cannot be placed on top of a smaller disk
               5. The goal is to move all disks from Peg 1 to Peg 3 in the minimum number of moves
               
               Analyze the current state with exceptional depth:
               1. Evaluate the current configuration of disks
               2. Identify the progress toward the goal
               3. Determine the key strategic principles to apply
               4. Consider the optimal solution path
               5. Analyze potential next moves and their consequences
               
               Your analysis should be thorough but well-organized with clear sections."""

            .. raw:: html

               </details>




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: HANOI_MOVE_HUMAN_PROMPT
            :value: Multiline-String

            .. raw:: html

               <details><summary>Show Value</summary>

            .. code-block:: python

               """# Current State
               {state}
               
               # Previous Analysis
               {analysis}
               
               # Valid Moves
               {valid_moves}
               
               Based on the analysis, select the best move for this position. Be sure to explain your reasoning."""

            .. raw:: html

               </details>




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: HANOI_MOVE_SYSTEM_PROMPT
            :value: Multiline-String

            .. raw:: html

               <details><summary>Show Value</summary>

            .. code-block:: python

               """You are an expert Tower of Hanoi player who must select the optimal move.
               
               Based on the provided analysis and your own assessment of the board, you must determine the single best move for the current position.
               
               You MUST return your move in the required format with the source peg (from_peg) and destination peg (to_peg), along with your reasoning.
               
               Remember the Tower of Hanoi rules:
               1. Only one disk can be moved at a time
               2. Only the top disk from any peg can be moved
               3. A larger disk cannot be placed on top of a smaller disk
               4. The goal is to move all disks from Peg 1 to Peg 3 in the minimum number of moves"""

            .. raw:: html

               </details>




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: analysis_prompt_template


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: move_prompt_template




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.towers_of_hanoi.prompts import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

