
:py:mod:`games.mancala.generic_engines`
=======================================

.. py:module:: games.mancala.generic_engines

Generic Mancala engine creation using the generic player agent system.

This module provides generic engine creation functions for Mancala games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.mancala.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.mancala.generic_engines.MancalaEngineFactory
   games.mancala.generic_engines.MancalaPlayerIdentifiers
   games.mancala.generic_engines.MancalaPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MancalaEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_MancalaEngineFactory {
        node [shape=record];
        "MancalaEngineFactory" [label="MancalaEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "MancalaEngineFactory";
      }

.. autoclass:: games.mancala.generic_engines.MancalaEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MancalaPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MancalaPlayerIdentifiers {
        node [shape=record];
        "MancalaPlayerIdentifiers" [label="MancalaPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "MancalaPlayerIdentifiers";
      }

.. autoclass:: games.mancala.generic_engines.MancalaPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MancalaPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_MancalaPromptGenerator {
        node [shape=record];
        "MancalaPromptGenerator" [label="MancalaPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "MancalaPromptGenerator";
      }

.. autoclass:: games.mancala.generic_engines.MancalaPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mancala.generic_engines.create_advanced_mancala_engines
   games.mancala.generic_engines.create_budget_mancala_engines
   games.mancala.generic_engines.create_generic_mancala_config_from_example
   games.mancala.generic_engines.create_generic_mancala_engines
   games.mancala.generic_engines.create_generic_mancala_engines_simple
   games.mancala.generic_engines.create_mixed_mancala_engines

.. py:function:: create_advanced_mancala_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Mancala engines with high-powered models.


   .. autolink-examples:: create_advanced_mancala_engines
      :collapse:

.. py:function:: create_budget_mancala_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Mancala engines.


   .. autolink-examples:: create_budget_mancala_engines
      :collapse:

.. py:function:: create_generic_mancala_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mancala engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Mancala engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_mancala_config_from_example
      :collapse:

.. py:function:: create_generic_mancala_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mancala engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Mancala engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_mancala_engines
      :collapse:

.. py:function:: create_generic_mancala_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mancala engines with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Mancala engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_mancala_engines_simple
      :collapse:

.. py:function:: create_mixed_mancala_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Mancala engines.


   .. autolink-examples:: create_mixed_mancala_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mancala.generic_engines
   :collapse:
   
.. autolink-skip:: next
