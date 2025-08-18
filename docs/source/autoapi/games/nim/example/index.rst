games.nim.example
=================

.. py:module:: games.nim.example

Comprehensive Nim Game Examples - Mathematical Strategy and Game Theory Demonstration.

This module provides 8 comprehensive examples demonstrating the mathematical properties
and strategic aspects of the Nim game, from basic gameplay to advanced analysis,
perfect play algorithms, and educational game theory concepts.

The examples cover:
1. Basic Standard Nim gameplay with optimal strategy
2. Misère Nim with endgame analysis
3. Mathematical analysis of positions using nim-sum
4. Game theory demonstration with P/N positions
5. Multiple pile variants and strategic considerations
6. Performance analysis and algorithm benchmarking
7. Educational game theory tutorial
8. Advanced tournament and ML integration

Each example includes detailed explanations of the mathematical concepts,
strategic reasoning, and implementation details for educational purposes.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">15 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive Nim Game Examples - Mathematical Strategy and Game Theory Demonstration.

   This module provides 8 comprehensive examples demonstrating the mathematical properties
   and strategic aspects of the Nim game, from basic gameplay to advanced analysis,
   perfect play algorithms, and educational game theory concepts.

   The examples cover:
   1. Basic Standard Nim gameplay with optimal strategy
   2. Misère Nim with endgame analysis
   3. Mathematical analysis of positions using nim-sum
   4. Game theory demonstration with P/N positions
   5. Multiple pile variants and strategic considerations
   6. Performance analysis and algorithm benchmarking
   7. Educational game theory tutorial
   8. Advanced tournament and ML integration

   Each example includes detailed explanations of the mathematical concepts,
   strategic reasoning, and implementation details for educational purposes.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.nim.example.initial_piles
      games.nim.example.logger

            
            
            

.. admonition:: Functions (15)
   :class: info

   .. autoapisummary::

      games.nim.example.binary_representation
      games.nim.example.calculate_nim_sum
      games.nim.example.example_1_basic_standard_nim
      games.nim.example.example_2_misere_nim
      games.nim.example.example_3_mathematical_analysis
      games.nim.example.example_4_game_theory_positions
      games.nim.example.example_5_multiple_pile_variants
      games.nim.example.example_6_performance_analysis
      games.nim.example.example_7_educational_tutorial
      games.nim.example.example_8_advanced_integration
      games.nim.example.main
      games.nim.example.parse_args
      games.nim.example.print_section_header
      games.nim.example.print_subsection
      games.nim.example.run_all_examples

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: binary_representation(piles: list[int]) -> None

            Display binary representation of piles for educational purposes.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: calculate_nim_sum(piles: list[int]) -> int

            Calculate the nim-sum (XOR) of pile sizes.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_1_basic_standard_nim()
            :async:


            Example 1: Basic Standard Nim with Optimal Play Strategy.

            Demonstrates the fundamental concepts of Nim including:
            - Standard game rules
            - Nim-sum calculation
            - Optimal move selection
            - Strategic reasoning



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_2_misere_nim()
            :async:


            Example 2: Misère Nim with Endgame Analysis.

            Demonstrates:
            - Misère rules (last player loses)
            - Strategy differences from standard Nim
            - Endgame analysis with single-stone piles
            - Transition from normal to misère strategy



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_3_mathematical_analysis()
            :async:


            Example 3: Mathematical Analysis of Nim Positions.

            Demonstrates:
            - Nim-sum calculation methods
            - Position classification (P/N positions)
            - Optimal move calculation
            - Mathematical proofs and theorems



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_4_game_theory_positions()
            :async:


            Example 4: Game Theory Demonstration with P/N Positions.

            Demonstrates:
            - P-positions (Previous player wins)
            - N-positions (Next player wins)
            - Move sequences and transitions
            - Winning and losing strategies



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_5_multiple_pile_variants()
            :async:


            Example 5: Multiple Pile Variants and Strategic Considerations.

            Demonstrates:
            - Games with different numbers of piles
            - Large pile configurations
            - Strategic complexity analysis
            - Computational efficiency



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_6_performance_analysis()
            :async:


            Example 6: Performance Analysis and Algorithm Benchmarking.

            Demonstrates:
            - Algorithm efficiency measurement
            - Performance scaling with problem size
            - Optimization techniques
            - Benchmarking results



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_7_educational_tutorial()
            :async:


            Example 7: Educational Game Theory Tutorial.

            Demonstrates:
            - Step-by-step learning progression
            - Mathematical concepts explanation
            - Interactive analysis
            - Teaching optimal play



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_8_advanced_integration()
            :async:


            Example 8: Advanced Tournament and ML Integration.

            Demonstrates:
            - Tournament systems
            - Statistical analysis
            - Machine learning integration concepts
            - Advanced configuration options



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()
            :async:


            Main entry point.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: parse_args()

            Parse command line arguments.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: print_section_header(title: str, subtitle: str = '') -> None

            Print a formatted section header.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: print_subsection(title: str) -> None

            Print a formatted subsection header.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_all_examples()
            :async:


            Run all examples sequentially.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: initial_piles
            :value: [3, 5, 7]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

