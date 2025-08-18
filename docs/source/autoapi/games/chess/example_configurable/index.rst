games.chess.example_configurable
================================

.. py:module:: games.chess.example_configurable

Example of running chess with configurable LLMs.

This example demonstrates how to run chess games with different LLM providers and
models, showing the flexibility of the new configuration system.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 functions</span>   </div>

.. autoapi-nested-parse::

   Example of running chess with configurable LLMs.

   This example demonstrates how to run chess games with different LLM providers and
   models, showing the flexibility of the new configuration system.



      
            
            
            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.chess.example_configurable.list_available_providers
      games.chess.example_configurable.run_advanced_chess_example
      games.chess.example_configurable.run_chess_with_custom_llms

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: list_available_providers()

            List all available LLM providers for chess.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_advanced_chess_example()

            Run an example with advanced configuration.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_chess_with_custom_llms(white_provider: str = 'anthropic', white_model: str = None, black_provider: str = 'anthropic', black_model: str = None, max_moves: int = 50, enable_analysis: bool = True)

            Run a chess game with custom LLM configurations.

            :param white_provider: LLM provider for white (e.g., "anthropic", "openai")
            :param white_model: Model for white (uses default if None)
            :param black_provider: LLM provider for black
            :param black_model: Model for black (uses default if None)
            :param max_moves: Maximum moves before draw
            :param enable_analysis: Whether to enable position analysis





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.example_configurable import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

