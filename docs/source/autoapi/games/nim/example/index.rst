games.nim.example
=================

.. py:module:: games.nim.example

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


   .. autolink-examples:: games.nim.example
      :collapse:


Attributes
----------

.. autoapisummary::

   games.nim.example.initial_piles
   games.nim.example.logger


Functions
---------

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


Module Contents
---------------

.. py:function:: binary_representation(piles: list[int]) -> None

   Display binary representation of piles for educational purposes.


   .. autolink-examples:: binary_representation
      :collapse:

.. py:function:: calculate_nim_sum(piles: list[int]) -> int

   Calculate the nim-sum (XOR) of pile sizes.


   .. autolink-examples:: calculate_nim_sum
      :collapse:

.. py:function:: example_1_basic_standard_nim()
   :async:


   Example 1: Basic Standard Nim with Optimal Play Strategy.

   Demonstrates the fundamental concepts of Nim including:
   - Standard game rules
   - Nim-sum calculation
   - Optimal move selection
   - Strategic reasoning


   .. autolink-examples:: example_1_basic_standard_nim
      :collapse:

.. py:function:: example_2_misere_nim()
   :async:


   Example 2: Misère Nim with Endgame Analysis.

   Demonstrates:
   - Misère rules (last player loses)
   - Strategy differences from standard Nim
   - Endgame analysis with single-stone piles
   - Transition from normal to misère strategy


   .. autolink-examples:: example_2_misere_nim
      :collapse:

.. py:function:: example_3_mathematical_analysis()
   :async:


   Example 3: Mathematical Analysis of Nim Positions.

   Demonstrates:
   - Nim-sum calculation methods
   - Position classification (P/N positions)
   - Optimal move calculation
   - Mathematical proofs and theorems


   .. autolink-examples:: example_3_mathematical_analysis
      :collapse:

.. py:function:: example_4_game_theory_positions()
   :async:


   Example 4: Game Theory Demonstration with P/N Positions.

   Demonstrates:
   - P-positions (Previous player wins)
   - N-positions (Next player wins)
   - Move sequences and transitions
   - Winning and losing strategies


   .. autolink-examples:: example_4_game_theory_positions
      :collapse:

.. py:function:: example_5_multiple_pile_variants()
   :async:


   Example 5: Multiple Pile Variants and Strategic Considerations.

   Demonstrates:
   - Games with different numbers of piles
   - Large pile configurations
   - Strategic complexity analysis
   - Computational efficiency


   .. autolink-examples:: example_5_multiple_pile_variants
      :collapse:

.. py:function:: example_6_performance_analysis()
   :async:


   Example 6: Performance Analysis and Algorithm Benchmarking.

   Demonstrates:
   - Algorithm efficiency measurement
   - Performance scaling with problem size
   - Optimization techniques
   - Benchmarking results


   .. autolink-examples:: example_6_performance_analysis
      :collapse:

.. py:function:: example_7_educational_tutorial()
   :async:


   Example 7: Educational Game Theory Tutorial.

   Demonstrates:
   - Step-by-step learning progression
   - Mathematical concepts explanation
   - Interactive analysis
   - Teaching optimal play


   .. autolink-examples:: example_7_educational_tutorial
      :collapse:

.. py:function:: example_8_advanced_integration()
   :async:


   Example 8: Advanced Tournament and ML Integration.

   Demonstrates:
   - Tournament systems
   - Statistical analysis
   - Machine learning integration concepts
   - Advanced configuration options


   .. autolink-examples:: example_8_advanced_integration
      :collapse:

.. py:function:: main()
   :async:


   Main entry point.


   .. autolink-examples:: main
      :collapse:

.. py:function:: parse_args()

   Parse command line arguments.


   .. autolink-examples:: parse_args
      :collapse:

.. py:function:: print_section_header(title: str, subtitle: str = '') -> None

   Print a formatted section header.


   .. autolink-examples:: print_section_header
      :collapse:

.. py:function:: print_subsection(title: str) -> None

   Print a formatted subsection header.


   .. autolink-examples:: print_subsection
      :collapse:

.. py:function:: run_all_examples()
   :async:


   Run all examples sequentially.


   .. autolink-examples:: run_all_examples
      :collapse:

.. py:data:: initial_piles
   :value: [3, 5, 7]


.. py:data:: logger

