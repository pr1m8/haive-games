
:py:mod:`games.debate.generic_engines`
======================================

.. py:module:: games.debate.generic_engines

Generic Debate engine creation using the generic player agent system.

This module provides generic engine creation functions for Debate games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.debate.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.debate.generic_engines.DebateEngineFactory
   games.debate.generic_engines.DebatePlayerIdentifiers
   games.debate.generic_engines.DebatePromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebateEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_DebateEngineFactory {
        node [shape=record];
        "DebateEngineFactory" [label="DebateEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "DebateEngineFactory";
      }

.. autoclass:: games.debate.generic_engines.DebateEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebatePlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_DebatePlayerIdentifiers {
        node [shape=record];
        "DebatePlayerIdentifiers" [label="DebatePlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "DebatePlayerIdentifiers";
      }

.. autoclass:: games.debate.generic_engines.DebatePlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DebatePromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_DebatePromptGenerator {
        node [shape=record];
        "DebatePromptGenerator" [label="DebatePromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "DebatePromptGenerator";
      }

.. autoclass:: games.debate.generic_engines.DebatePromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.debate.generic_engines.create_advanced_debate_engines
   games.debate.generic_engines.create_budget_debate_engines
   games.debate.generic_engines.create_generic_debate_config_from_example
   games.debate.generic_engines.create_generic_debate_engines
   games.debate.generic_engines.create_generic_debate_engines_simple
   games.debate.generic_engines.create_mixed_debate_engines

.. py:function:: create_advanced_debate_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Debate engines with high-powered models.


   .. autolink-examples:: create_advanced_debate_engines
      :collapse:

.. py:function:: create_budget_debate_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Debate engines.


   .. autolink-examples:: create_budget_debate_engines
      :collapse:

.. py:function:: create_generic_debate_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Debate engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Debate engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_debate_config_from_example
      :collapse:

.. py:function:: create_generic_debate_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Debate engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Debate engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "debater1_player": Player 1 configuration
       - "debater2_player": Player 2 configuration
       - "debater1_analyzer": Player 1 analyzer configuration
       - "debater2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_debate_engines
      :collapse:

.. py:function:: create_generic_debate_engines_simple(debater1_model: str, debater2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Debate engines with simple model specifications.

   :param debater1_model: Model for debater1 and analyzer
   :param debater2_model: Model for debater2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Debate engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_debate_engines_simple
      :collapse:

.. py:function:: create_mixed_debate_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Debate engines.


   .. autolink-examples:: create_mixed_debate_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.debate.generic_engines
   :collapse:
   
.. autolink-skip:: next
