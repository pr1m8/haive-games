
:py:mod:`games.reversi.generic_engines`
=======================================

.. py:module:: games.reversi.generic_engines

Generic Reversi engine creation using the generic player agent system.

This module provides generic engine creation functions for Reversi games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.reversi.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.reversi.generic_engines.ReversiEngineFactory
   games.reversi.generic_engines.ReversiPlayerIdentifiers
   games.reversi.generic_engines.ReversiPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReversiEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_ReversiEngineFactory {
        node [shape=record];
        "ReversiEngineFactory" [label="ReversiEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "ReversiEngineFactory";
      }

.. autoclass:: games.reversi.generic_engines.ReversiEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReversiPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_ReversiPlayerIdentifiers {
        node [shape=record];
        "ReversiPlayerIdentifiers" [label="ReversiPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "ReversiPlayerIdentifiers";
      }

.. autoclass:: games.reversi.generic_engines.ReversiPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ReversiPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_ReversiPromptGenerator {
        node [shape=record];
        "ReversiPromptGenerator" [label="ReversiPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "ReversiPromptGenerator";
      }

.. autoclass:: games.reversi.generic_engines.ReversiPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.reversi.generic_engines.create_advanced_reversi_engines
   games.reversi.generic_engines.create_budget_reversi_engines
   games.reversi.generic_engines.create_generic_reversi_config_from_example
   games.reversi.generic_engines.create_generic_reversi_engines
   games.reversi.generic_engines.create_generic_reversi_engines_simple
   games.reversi.generic_engines.create_mixed_reversi_engines

.. py:function:: create_advanced_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Reversi engines with high-powered models.


   .. autolink-examples:: create_advanced_reversi_engines
      :collapse:

.. py:function:: create_budget_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Reversi engines.


   .. autolink-examples:: create_budget_reversi_engines
      :collapse:

.. py:function:: create_generic_reversi_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Reversi engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Reversi engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_reversi_config_from_example
      :collapse:

.. py:function:: create_generic_reversi_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Reversi engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Reversi engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "black_player": Player 1 configuration
       - "white_player": Player 2 configuration
       - "black_analyzer": Player 1 analyzer configuration
       - "white_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_reversi_engines
      :collapse:

.. py:function:: create_generic_reversi_engines_simple(black_model: str, white_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Reversi engines with simple model specifications.

   :param black_model: Model for black and analyzer
   :param white_model: Model for white and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Reversi engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_reversi_engines_simple
      :collapse:

.. py:function:: create_mixed_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Reversi engines.


   .. autolink-examples:: create_mixed_reversi_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.reversi.generic_engines
   :collapse:
   
.. autolink-skip:: next
