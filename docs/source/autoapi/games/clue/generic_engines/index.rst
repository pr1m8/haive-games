
:py:mod:`games.clue.generic_engines`
====================================

.. py:module:: games.clue.generic_engines

Generic Clue engine creation using the generic player agent system.

This module provides generic engine creation functions for Clue games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.clue.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.clue.generic_engines.ClueEngineFactory
   games.clue.generic_engines.CluePlayerIdentifiers
   games.clue.generic_engines.CluePromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_ClueEngineFactory {
        node [shape=record];
        "ClueEngineFactory" [label="ClueEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "ClueEngineFactory";
      }

.. autoclass:: games.clue.generic_engines.ClueEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CluePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_CluePlayerIdentifiers {
        node [shape=record];
        "CluePlayerIdentifiers" [label="CluePlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "CluePlayerIdentifiers";
      }

.. autoclass:: games.clue.generic_engines.CluePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CluePromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_CluePromptGenerator {
        node [shape=record];
        "CluePromptGenerator" [label="CluePromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "CluePromptGenerator";
      }

.. autoclass:: games.clue.generic_engines.CluePromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.clue.generic_engines.create_advanced_clue_engines
   games.clue.generic_engines.create_budget_clue_engines
   games.clue.generic_engines.create_generic_clue_config_from_example
   games.clue.generic_engines.create_generic_clue_engines
   games.clue.generic_engines.create_generic_clue_engines_simple
   games.clue.generic_engines.create_mixed_clue_engines

.. py:function:: create_advanced_clue_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Clue engines with high-powered models.


   .. autolink-examples:: create_advanced_clue_engines
      :collapse:

.. py:function:: create_budget_clue_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Clue engines.


   .. autolink-examples:: create_budget_clue_engines
      :collapse:

.. py:function:: create_generic_clue_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Clue engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Clue engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_clue_config_from_example
      :collapse:

.. py:function:: create_generic_clue_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Clue engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Clue engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "detective_player": Player 1 configuration
       - "suspect_player": Player 2 configuration
       - "detective_analyzer": Player 1 analyzer configuration
       - "suspect_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_clue_engines
      :collapse:

.. py:function:: create_generic_clue_engines_simple(detective_model: str, suspect_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Clue engines with simple model specifications.

   :param detective_model: Model for detective and analyzer
   :param suspect_model: Model for suspect and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Clue engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_clue_engines_simple
      :collapse:

.. py:function:: create_mixed_clue_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Clue engines.


   .. autolink-examples:: create_mixed_clue_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.clue.generic_engines
   :collapse:
   
.. autolink-skip:: next
