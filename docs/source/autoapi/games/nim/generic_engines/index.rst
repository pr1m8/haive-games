
:py:mod:`games.nim.generic_engines`
===================================

.. py:module:: games.nim.generic_engines

Generic Nim engine creation using the generic player agent system.

This module provides generic engine creation functions for Nim games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.nim.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.nim.generic_engines.NimEngineFactory
   games.nim.generic_engines.NimPlayerIdentifiers
   games.nim.generic_engines.NimPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_NimEngineFactory {
        node [shape=record];
        "NimEngineFactory" [label="NimEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "NimEngineFactory";
      }

.. autoclass:: games.nim.generic_engines.NimEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_NimPlayerIdentifiers {
        node [shape=record];
        "NimPlayerIdentifiers" [label="NimPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "NimPlayerIdentifiers";
      }

.. autoclass:: games.nim.generic_engines.NimPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_NimPromptGenerator {
        node [shape=record];
        "NimPromptGenerator" [label="NimPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "NimPromptGenerator";
      }

.. autoclass:: games.nim.generic_engines.NimPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.nim.generic_engines.create_advanced_nim_engines
   games.nim.generic_engines.create_budget_nim_engines
   games.nim.generic_engines.create_generic_nim_config_from_example
   games.nim.generic_engines.create_generic_nim_engines
   games.nim.generic_engines.create_generic_nim_engines_simple
   games.nim.generic_engines.create_mixed_nim_engines

.. py:function:: create_advanced_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Nim engines with high-powered models.


   .. autolink-examples:: create_advanced_nim_engines
      :collapse:

.. py:function:: create_budget_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Nim engines.


   .. autolink-examples:: create_budget_nim_engines
      :collapse:

.. py:function:: create_generic_nim_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Nim engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Nim engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_nim_config_from_example
      :collapse:

.. py:function:: create_generic_nim_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Nim engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Nim engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_nim_engines
      :collapse:

.. py:function:: create_generic_nim_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Nim engines with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Nim engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_nim_engines_simple
      :collapse:

.. py:function:: create_mixed_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Nim engines.


   .. autolink-examples:: create_mixed_nim_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.nim.generic_engines
   :collapse:
   
.. autolink-skip:: next
