
:py:mod:`games.fox_and_geese.generic_engines`
=============================================

.. py:module:: games.fox_and_geese.generic_engines

Generic FoxAndGeese engine creation using the generic player agent system.

This module provides generic engine creation functions for FoxAndGeese games, allowing
for configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.fox_and_geese.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.fox_and_geese.generic_engines.FoxAndGeeseEngineFactory
   games.fox_and_geese.generic_engines.FoxAndGeesePlayerIdentifiers
   games.fox_and_geese.generic_engines.FoxAndGeesePromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FoxAndGeeseEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_FoxAndGeeseEngineFactory {
        node [shape=record];
        "FoxAndGeeseEngineFactory" [label="FoxAndGeeseEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "FoxAndGeeseEngineFactory";
      }

.. autoclass:: games.fox_and_geese.generic_engines.FoxAndGeeseEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FoxAndGeesePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_FoxAndGeesePlayerIdentifiers {
        node [shape=record];
        "FoxAndGeesePlayerIdentifiers" [label="FoxAndGeesePlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "FoxAndGeesePlayerIdentifiers";
      }

.. autoclass:: games.fox_and_geese.generic_engines.FoxAndGeesePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FoxAndGeesePromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_FoxAndGeesePromptGenerator {
        node [shape=record];
        "FoxAndGeesePromptGenerator" [label="FoxAndGeesePromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "FoxAndGeesePromptGenerator";
      }

.. autoclass:: games.fox_and_geese.generic_engines.FoxAndGeesePromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.fox_and_geese.generic_engines.create_advanced_fox_and_geese_engines
   games.fox_and_geese.generic_engines.create_budget_fox_and_geese_engines
   games.fox_and_geese.generic_engines.create_generic_fox_and_geese_config_from_example
   games.fox_and_geese.generic_engines.create_generic_fox_and_geese_engines
   games.fox_and_geese.generic_engines.create_generic_fox_and_geese_engines_simple
   games.fox_and_geese.generic_engines.create_mixed_fox_and_geese_engines

.. py:function:: create_advanced_fox_and_geese_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced FoxAndGeese engines with high-powered models.


   .. autolink-examples:: create_advanced_fox_and_geese_engines
      :collapse:

.. py:function:: create_budget_fox_and_geese_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly FoxAndGeese engines.


   .. autolink-examples:: create_budget_fox_and_geese_engines
      :collapse:

.. py:function:: create_generic_fox_and_geese_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create FoxAndGeese engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of FoxAndGeese engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_fox_and_geese_config_from_example
      :collapse:

.. py:function:: create_generic_fox_and_geese_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create FoxAndGeese engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of FoxAndGeese engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "fox_player": Player 1 configuration
       - "geese_player": Player 2 configuration
       - "fox_analyzer": Player 1 analyzer configuration
       - "geese_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_fox_and_geese_engines
      :collapse:

.. py:function:: create_generic_fox_and_geese_engines_simple(fox_model: str, geese_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create FoxAndGeese engines with simple model specifications.

   :param fox_model: Model for fox and analyzer
   :param geese_model: Model for geese and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of FoxAndGeese engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_fox_and_geese_engines_simple
      :collapse:

.. py:function:: create_mixed_fox_and_geese_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider FoxAndGeese engines.


   .. autolink-examples:: create_mixed_fox_and_geese_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.fox_and_geese.generic_engines
   :collapse:
   
.. autolink-skip:: next
