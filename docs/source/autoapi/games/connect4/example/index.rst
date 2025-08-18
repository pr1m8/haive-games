games.connect4.example
======================

.. py:module:: games.connect4.example

Comprehensive examples for the Connect4 game module.

This module provides a complete set of examples demonstrating all aspects of the
Connect4 game implementation, from basic gameplay to advanced features like
strategic analysis, performance testing, and error handling.

The examples are organized into logical categories:
- Basic gameplay examples
- Rich UI demonstrations
- Strategic analysis showcases
- Performance and testing examples
- Error handling and debugging
- Advanced usage patterns
- Tournament and batch processing
- Custom configuration examples

Each example includes detailed comments explaining the concepts and can be run
independently or as part of the full demonstration suite.

Usage:
    Run all examples:
        python example.py

    Run specific example:
        python example.py basic
        python example.py rich-ui
        python example.py analysis
        python example.py performance
        python example.py error-handling
        python example.py tournament
        python example.py custom-ai
        python example.py async-batch

Examples provided:
    1. Basic Game - Simple game with minimal configuration
    2. Rich UI Game - Beautiful terminal interface with animations
    3. Strategic Analysis - Deep position analysis and explanations
    4. Performance Testing - Benchmarking and optimization
    5. Error Handling - Robust error management and debugging
    6. Tournament Mode - Multiple games and statistics
    7. Custom AI Configuration - Advanced engine customization
    8. Async Batch Processing - Concurrent game execution



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">9 functions</span> • <span class="module-stat">4 attributes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive examples for the Connect4 game module.

   This module provides a complete set of examples demonstrating all aspects of the
   Connect4 game implementation, from basic gameplay to advanced features like
   strategic analysis, performance testing, and error handling.

   The examples are organized into logical categories:
   - Basic gameplay examples
   - Rich UI demonstrations
   - Strategic analysis showcases
   - Performance and testing examples
   - Error handling and debugging
   - Advanced usage patterns
   - Tournament and batch processing
   - Custom configuration examples

   Each example includes detailed comments explaining the concepts and can be run
   independently or as part of the full demonstration suite.

   Usage:
       Run all examples:
           python example.py

       Run specific example:
           python example.py basic
           python example.py rich-ui
           python example.py analysis
           python example.py performance
           python example.py error-handling
           python example.py tournament
           python example.py custom-ai
           python example.py async-batch

   Examples provided:
       1. Basic Game - Simple game with minimal configuration
       2. Rich UI Game - Beautiful terminal interface with animations
       3. Strategic Analysis - Deep position analysis and explanations
       4. Performance Testing - Benchmarking and optimization
       5. Error Handling - Robust error management and debugging
       6. Tournament Mode - Multiple games and statistics
       7. Custom AI Configuration - Advanced engine customization
       8. Async Batch Processing - Concurrent game execution



      

.. admonition:: Attributes (4)
   :class: tip

   .. autoapisummary::

      games.connect4.example.console
      games.connect4.example.logger
      games.connect4.example.package_root
      games.connect4.example.result

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.connect4.example.GameResult

            

.. admonition:: Functions (9)
   :class: info

   .. autoapisummary::

      games.connect4.example.example_1_basic_game
      games.connect4.example.example_2_rich_ui_game
      games.connect4.example.example_3_strategic_analysis
      games.connect4.example.example_4_performance_testing
      games.connect4.example.example_5_error_handling
      games.connect4.example.example_6_tournament_mode
      games.connect4.example.example_7_custom_ai_configuration
      games.connect4.example.example_8_async_batch_processing
      games.connect4.example.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameResult

            Data class to store game results.


            .. py:attribute:: duration
               :type:  float


            .. py:attribute:: moves
               :type:  int


            .. py:attribute:: red_analysis_count
               :type:  int


            .. py:attribute:: status
               :type:  str


            .. py:attribute:: winner
               :type:  str | None


            .. py:attribute:: yellow_analysis_count
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_1_basic_game()

            Example 1: Basic Game - Simple gameplay with minimal configuration.

            This example demonstrates the simplest way to create and run a Connect4 game.
            Perfect for quick testing and understanding basic functionality.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_2_rich_ui_game()

            Example 2: Rich UI Game - Beautiful terminal interface with animations.

            This example showcases the Rich-based UI system with animated board display,
            AI thinking indicators, and comprehensive game state visualization.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_3_strategic_analysis()

            Example 3: Strategic Analysis - Deep position analysis and explanations.

            This example demonstrates the strategic analysis capabilities of the Connect4 AI,
            showing how it evaluates positions, detects threats, and plans moves.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_4_performance_testing()

            Example 4: Performance Testing - Benchmarking and optimization.

            This example demonstrates performance testing capabilities, measuring
            game execution speed, memory usage, and providing optimization insights.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_5_error_handling()

            Example 5: Error Handling - Robust error management and debugging.

            This example demonstrates various error conditions and how the system
            handles them gracefully with informative error messages.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_6_tournament_mode()

            Example 6: Tournament Mode - Multiple games and statistics.

            This example demonstrates running multiple games in succession and
            collecting comprehensive statistics about game patterns and outcomes.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_7_custom_ai_configuration()

            Example 7: Custom AI Configuration - Advanced engine customization.

            This example demonstrates advanced AI configuration options and
            how to customize the Connect4 agent for specific use cases.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: example_8_async_batch_processing()
            :async:


            Example 8: Async Batch Processing - Concurrent game execution.

            This example demonstrates asynchronous batch processing capabilities,
            running multiple games concurrently for maximum throughput.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Main function to run all examples or specific ones.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: console


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: package_root


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: result




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.connect4.example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

