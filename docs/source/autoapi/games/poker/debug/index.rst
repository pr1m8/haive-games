games.poker.debug
=================

.. py:module:: games.poker.debug

Debugging utilities for the poker agent.

This module provides tools for debugging, testing and analyzing the poker agent's
performance, including:
- Test harnesses for structured output validation
- Decision validation and verification
- Error analysis and reporting
- Game state visualization



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Debugging utilities for the poker agent.

   This module provides tools for debugging, testing and analyzing the poker agent's
   performance, including:
   - Test harnesses for structured output validation
   - Decision validation and verification
   - Error analysis and reporting
   - Game state visualization



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.poker.debug.logger

            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.poker.debug.DecisionAnalyzer
      games.poker.debug.GameStatePrinter
      games.poker.debug.StructuredOutputTester

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DecisionAnalyzer

            Analyze and validate player decisions for correctness.


            .. py:method:: validate_decision(decision: haive.games.poker.models.AgentDecision, player: haive.games.poker.models.Player, game_state) -> dict[str, Any]
               :staticmethod:


               Validate if a decision is legal and reasonable.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameStatePrinter

            Utility for visualizing poker game state during debugging.


            .. py:method:: _format_card(card: haive.games.poker.models.Card) -> str
               :staticmethod:


               Format a card for display.



            .. py:method:: print_game_state(state)
               :staticmethod:


               Print a human-readable version of the current game state.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: StructuredOutputTester(llm_runnable, input_values: dict[str, Any])

            Test harness for validating LLM structured output handling.

            Initialize the tester with an LLM runnable and test inputs.


            .. py:method:: print_report()

               Print a detailed report of the test results.



            .. py:method:: run_batch_test(iterations: int = 10) -> dict[str, Any]

               Run multiple tests and collect statistics.



            .. py:method:: run_test(retries: int = 3) -> dict[str, Any]

               Run a single test of the LLM runnable with retries.



            .. py:attribute:: input_values


            .. py:attribute:: llm


            .. py:attribute:: results
               :value: []




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.poker.debug import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

