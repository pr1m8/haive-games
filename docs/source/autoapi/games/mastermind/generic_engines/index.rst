
:py:mod:`games.mastermind.generic_engines`
==========================================

.. py:module:: games.mastermind.generic_engines

Generic Mastermind engine creation using the generic player agent system.

This module provides generic engine creation functions for Mastermind games, allowing
for configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.mastermind.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.mastermind.generic_engines.MastermindEngineFactory
   games.mastermind.generic_engines.MastermindPlayerIdentifiers
   games.mastermind.generic_engines.MastermindPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindEngineFactory {
        node [shape=record];
        "MastermindEngineFactory" [label="MastermindEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "MastermindEngineFactory";
      }

.. autoclass:: games.mastermind.generic_engines.MastermindEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindPlayerIdentifiers {
        node [shape=record];
        "MastermindPlayerIdentifiers" [label="MastermindPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "MastermindPlayerIdentifiers";
      }

.. autoclass:: games.mastermind.generic_engines.MastermindPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MastermindPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_MastermindPromptGenerator {
        node [shape=record];
        "MastermindPromptGenerator" [label="MastermindPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "MastermindPromptGenerator";
      }

.. autoclass:: games.mastermind.generic_engines.MastermindPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mastermind.generic_engines.create_advanced_mastermind_engines
   games.mastermind.generic_engines.create_budget_mastermind_engines
   games.mastermind.generic_engines.create_generic_mastermind_config_from_example
   games.mastermind.generic_engines.create_generic_mastermind_engines
   games.mastermind.generic_engines.create_generic_mastermind_engines_simple
   games.mastermind.generic_engines.create_mixed_mastermind_engines

.. py:function:: create_advanced_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Mastermind engines with high-powered models.


   .. autolink-examples:: create_advanced_mastermind_engines
      :collapse:

.. py:function:: create_budget_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Mastermind engines.


   .. autolink-examples:: create_budget_mastermind_engines
      :collapse:

.. py:function:: create_generic_mastermind_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mastermind engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Mastermind engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_mastermind_config_from_example
      :collapse:

.. py:function:: create_generic_mastermind_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mastermind engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Mastermind engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "codemaker_player": Player 1 configuration
       - "codebreaker_player": Player 2 configuration
       - "codemaker_analyzer": Player 1 analyzer configuration
       - "codebreaker_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_mastermind_engines
      :collapse:

.. py:function:: create_generic_mastermind_engines_simple(codemaker_model: str, codebreaker_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mastermind engines with simple model specifications.

   :param codemaker_model: Model for codemaker and analyzer
   :param codebreaker_model: Model for codebreaker and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Mastermind engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_mastermind_engines_simple
      :collapse:

.. py:function:: create_mixed_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Mastermind engines.


   .. autolink-examples:: create_mixed_mastermind_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mastermind.generic_engines
   :collapse:
   
.. autolink-skip:: next
