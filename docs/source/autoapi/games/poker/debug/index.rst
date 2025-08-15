games.poker.debug
=================

.. py:module:: games.poker.debug

.. autoapi-nested-parse::

   Debugging utilities for the poker agent.

   This module provides tools for debugging, testing and analyzing the poker agent's
   performance, including:
   - Test harnesses for structured output validation
   - Decision validation and verification
   - Error analysis and reporting
   - Game state visualization


   .. autolink-examples:: games.poker.debug
      :collapse:


Attributes
----------

.. autoapisummary::

   games.poker.debug.logger


Classes
-------

.. autoapisummary::

   games.poker.debug.DecisionAnalyzer
   games.poker.debug.GameStatePrinter
   games.poker.debug.StructuredOutputTester


Module Contents
---------------

.. py:class:: DecisionAnalyzer

   Analyze and validate player decisions for correctness.


   .. autolink-examples:: DecisionAnalyzer
      :collapse:

   .. py:method:: validate_decision(decision: haive.games.poker.models.AgentDecision, player: haive.games.poker.models.Player, game_state) -> dict[str, Any]
      :staticmethod:


      Validate if a decision is legal and reasonable.


      .. autolink-examples:: validate_decision
         :collapse:


.. py:class:: GameStatePrinter

   Utility for visualizing poker game state during debugging.


   .. autolink-examples:: GameStatePrinter
      :collapse:

   .. py:method:: _format_card(card: haive.games.poker.models.Card) -> str
      :staticmethod:


      Format a card for display.


      .. autolink-examples:: _format_card
         :collapse:


   .. py:method:: print_game_state(state)
      :staticmethod:


      Print a human-readable version of the current game state.


      .. autolink-examples:: print_game_state
         :collapse:


.. py:class:: StructuredOutputTester(llm_runnable, input_values: dict[str, Any])

   Test harness for validating LLM structured output handling.

   Initialize the tester with an LLM runnable and test inputs.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StructuredOutputTester
      :collapse:

   .. py:method:: print_report()

      Print a detailed report of the test results.


      .. autolink-examples:: print_report
         :collapse:


   .. py:method:: run_batch_test(iterations: int = 10) -> dict[str, Any]

      Run multiple tests and collect statistics.


      .. autolink-examples:: run_batch_test
         :collapse:


   .. py:method:: run_test(retries: int = 3) -> dict[str, Any]

      Run a single test of the LLM runnable with retries.


      .. autolink-examples:: run_test
         :collapse:


   .. py:attribute:: input_values


   .. py:attribute:: llm


   .. py:attribute:: results
      :value: []



.. py:data:: logger

