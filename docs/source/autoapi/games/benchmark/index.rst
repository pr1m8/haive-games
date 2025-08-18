games.benchmark
===============

.. py:module:: games.benchmark

Benchmark script for testing game agents.

This script runs benchmarks for the Monopoly and Poker agents to test their performance
and identify issues.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 functions</span> • <span class="module-stat">3 attributes</span>   </div>

.. autoapi-nested-parse::

   Benchmark script for testing game agents.

   This script runs benchmarks for the Monopoly and Poker agents to test their performance
   and identify issues.



      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.benchmark.PROJECT_ROOT
      games.benchmark.exit_code
      games.benchmark.logger

            
            
            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.benchmark.main
      games.benchmark.run_monopoly_benchmark
      games.benchmark.run_poker_benchmark

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run all benchmarks based on command line arguments.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_monopoly_benchmark()

            Run benchmark tests for the Monopoly agent.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_poker_benchmark()

            Run benchmark tests for the Poker agent.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: PROJECT_ROOT


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: exit_code
            :value: 0



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.benchmark import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

