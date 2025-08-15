games.checkers.example
======================

.. py:module:: games.checkers.example

.. autoapi-nested-parse::

   Comprehensive Checkers Game Examples - Strategic Gameplay and AI Analysis.

   This module provides 8 comprehensive examples demonstrating the strategic aspects
   of the Checkers game, from basic gameplay to advanced tournament analysis,
   strategic decision-making, and educational gameplay patterns.

   The examples cover:
   1. Basic Checkers gameplay with LLM-powered players
   2. Advanced player personality configuration
   3. Tournament play with multiple game simulation
   4. Position analysis and strategic evaluation
   5. Educational mode with move explanations
   6. Performance testing and optimization
   7. Custom strategy implementation
   8. Game state management and persistence

   Each example includes detailed explanations of strategic concepts,
   gameplay mechanics, and configuration options for educational purposes.


   .. autolink-examples:: games.checkers.example
      :collapse:


Attributes
----------

.. autoapisummary::

   games.checkers.example.logger


Functions
---------

.. autoapisummary::

   games.checkers.example.create_tournament_config
   games.checkers.example.display_board_position
   games.checkers.example.example_1_basic_checkers_game
   games.checkers.example.example_2_advanced_player_configuration
   games.checkers.example.example_3_tournament_play
   games.checkers.example.example_4_position_analysis
   games.checkers.example.example_5_educational_mode
   games.checkers.example.example_6_performance_testing
   games.checkers.example.example_7_custom_strategy
   games.checkers.example.example_8_game_state_management
   games.checkers.example.main
   games.checkers.example.print_section_header
   games.checkers.example.print_subsection


Module Contents
---------------

.. py:function:: create_tournament_config(player1_style: str, player2_style: str) -> haive.games.checkers.config.CheckersAgentConfig

   Create tournament configuration with different player styles.


   .. autolink-examples:: create_tournament_config
      :collapse:

.. py:function:: display_board_position(state: haive.games.checkers.state.CheckersState, title: str = 'Board Position') -> None

   Display board position in a readable format.


   .. autolink-examples:: display_board_position
      :collapse:

.. py:function:: example_1_basic_checkers_game()
   :async:


   Example 1: Basic Checkers Game with LLM Players.

   Demonstrates the fundamental concepts of Checkers gameplay including:
   - Standard game rules and mechanics
   - LLM-powered player decision-making
   - Basic position evaluation
   - Game flow and termination


   .. autolink-examples:: example_1_basic_checkers_game
      :collapse:

.. py:function:: example_2_advanced_player_configuration()
   :async:


   Example 2: Advanced Player Configuration with Personalities.

   Demonstrates different player personalities and configurations:
   - Aggressive vs. Defensive playing styles
   - Custom system messages and temperature settings
   - Enhanced analysis and strategic depth
   - Player behavior customization


   .. autolink-examples:: example_2_advanced_player_configuration
      :collapse:

.. py:function:: example_3_tournament_play()
   :async:


   Example 3: Tournament Play with Multiple Games.

   Demonstrates tournament-style gameplay including:
   - Multiple game simulation
   - Statistical analysis of results
   - Different player matchups
   - Performance metrics tracking


   .. autolink-examples:: example_3_tournament_play
      :collapse:

.. py:function:: example_4_position_analysis()
   :async:


   Example 4: Advanced Position Analysis and Strategic Evaluation.

   Demonstrates comprehensive position analysis including:
   - Static position evaluation
   - Tactical opportunity identification
   - Strategic planning assessment
   - Move quality analysis


   .. autolink-examples:: example_4_position_analysis
      :collapse:

.. py:function:: example_5_educational_mode()
   :async:


   Example 5: Educational Mode with Move Explanations.

   Demonstrates educational features including:
   - Detailed move explanations
   - Strategic concept teaching
   - Interactive learning elements
   - Beginner-friendly guidance


   .. autolink-examples:: example_5_educational_mode
      :collapse:

.. py:function:: example_6_performance_testing()
   :async:


   Example 6: Performance Testing and Optimization.

   Demonstrates performance optimization including:
   - Speed vs. quality trade-offs
   - Batch game processing
   - Memory usage optimization
   - Timing analysis


   .. autolink-examples:: example_6_performance_testing
      :collapse:

.. py:function:: example_7_custom_strategy()
   :async:


   Example 7: Custom Strategy Implementation.

   Demonstrates custom strategy development including:
   - Strategy pattern implementation
   - Custom evaluation functions
   - Move selection algorithms
   - Strategy comparison


   .. autolink-examples:: example_7_custom_strategy
      :collapse:

.. py:function:: example_8_game_state_management()
   :async:


   Example 8: Game State Management and Persistence.

   Demonstrates game state handling including:
   - Game state serialization
   - Save/load functionality
   - Move history tracking
   - State validation


   .. autolink-examples:: example_8_game_state_management
      :collapse:

.. py:function:: main()
   :async:


   Main function to run all examples.


   .. autolink-examples:: main
      :collapse:

.. py:function:: print_section_header(title: str, subtitle: str = '') -> None

   Print a formatted section header.


   .. autolink-examples:: print_section_header
      :collapse:

.. py:function:: print_subsection(title: str) -> None

   Print a formatted subsection header.


   .. autolink-examples:: print_subsection
      :collapse:

.. py:data:: logger

