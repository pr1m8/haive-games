games.chess.example_configurable
================================

.. py:module:: games.chess.example_configurable

.. autoapi-nested-parse::

   Example of running chess with configurable LLMs.

   This example demonstrates how to run chess games with different LLM providers and
   models, showing the flexibility of the new configuration system.



Functions
---------

.. autoapisummary::

   games.chess.example_configurable.list_available_providers
   games.chess.example_configurable.run_advanced_chess_example
   games.chess.example_configurable.run_chess_with_custom_llms


Module Contents
---------------

.. py:function:: list_available_providers()

   List all available LLM providers for chess.


.. py:function:: run_advanced_chess_example()

   Run an example with advanced configuration.


.. py:function:: run_chess_with_custom_llms(white_provider: str = 'anthropic', white_model: str = None, black_provider: str = 'anthropic', black_model: str = None, max_moves: int = 50, enable_analysis: bool = True)

   Run a chess game with custom LLM configurations.

   :param white_provider: LLM provider for white (e.g., "anthropic", "openai")
   :param white_model: Model for white (uses default if None)
   :param black_provider: LLM provider for black
   :param black_model: Model for black (uses default if None)
   :param max_moves: Maximum moves before draw
   :param enable_analysis: Whether to enable position analysis


