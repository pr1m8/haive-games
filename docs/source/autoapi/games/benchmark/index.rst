games.benchmark
===============

.. py:module:: games.benchmark

.. autoapi-nested-parse::

   Benchmark script for testing game agents.

   This script runs benchmarks for the Monopoly and Poker agents to test their performance
   and identify issues.


   .. autolink-examples:: games.benchmark
      :collapse:


Attributes
----------

.. autoapisummary::

   games.benchmark.PROJECT_ROOT
   games.benchmark.exit_code
   games.benchmark.logger


Functions
---------

.. autoapisummary::

   games.benchmark.main
   games.benchmark.run_monopoly_benchmark
   games.benchmark.run_poker_benchmark


Module Contents
---------------

.. py:function:: main()

   Run all benchmarks based on command line arguments.


   .. autolink-examples:: main
      :collapse:

.. py:function:: run_monopoly_benchmark()

   Run benchmark tests for the Monopoly agent.


   .. autolink-examples:: run_monopoly_benchmark
      :collapse:

.. py:function:: run_poker_benchmark()

   Run benchmark tests for the Poker agent.


   .. autolink-examples:: run_poker_benchmark
      :collapse:

.. py:data:: PROJECT_ROOT

.. py:data:: exit_code
   :value: 0


.. py:data:: logger

