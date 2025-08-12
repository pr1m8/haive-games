
:py:mod:`games.monopoly.generic_engines`
========================================

.. py:module:: games.monopoly.generic_engines

Generic Monopoly engine creation using the generic player agent system.

This module provides generic engine creation functions for Monopoly games, allowing for
configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.monopoly.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.monopoly.generic_engines.MonopolyEngineFactory
   games.monopoly.generic_engines.MonopolyPlayerIdentifiers
   games.monopoly.generic_engines.MonopolyPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyEngineFactory {
        node [shape=record];
        "MonopolyEngineFactory" [label="MonopolyEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "MonopolyEngineFactory";
      }

.. autoclass:: games.monopoly.generic_engines.MonopolyEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyPlayerIdentifiers {
        node [shape=record];
        "MonopolyPlayerIdentifiers" [label="MonopolyPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "MonopolyPlayerIdentifiers";
      }

.. autoclass:: games.monopoly.generic_engines.MonopolyPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyPromptGenerator {
        node [shape=record];
        "MonopolyPromptGenerator" [label="MonopolyPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "MonopolyPromptGenerator";
      }

.. autoclass:: games.monopoly.generic_engines.MonopolyPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.monopoly.generic_engines.create_budget_monopoly_engines
   games.monopoly.generic_engines.create_generic_monopoly_config_from_example
   games.monopoly.generic_engines.create_generic_monopoly_engines
   games.monopoly.generic_engines.create_generic_monopoly_engines_simple
   games.monopoly.generic_engines.create_mixed_monopoly_engines
   games.monopoly.generic_engines.create_property_tycoon_monopoly_engines
   games.monopoly.generic_engines.create_real_estate_mogul_monopoly_engines

.. py:function:: create_budget_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Monopoly engines.


   .. autolink-examples:: create_budget_monopoly_engines
      :collapse:

.. py:function:: create_generic_monopoly_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Monopoly engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Monopoly engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "real_estate_moguls": High-powered models for strategic gameplay
       - "property_tycoons": Specialized for property investment



   .. autolink-examples:: create_generic_monopoly_config_from_example
      :collapse:

.. py:function:: create_generic_monopoly_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Monopoly engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Monopoly engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_monopoly_engines
      :collapse:

.. py:function:: create_generic_monopoly_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Monopoly engines with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Monopoly engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_monopoly_engines_simple
      :collapse:

.. py:function:: create_mixed_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Monopoly engines.


   .. autolink-examples:: create_mixed_monopoly_engines
      :collapse:

.. py:function:: create_property_tycoon_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create property tycoon-style Monopoly engines.


   .. autolink-examples:: create_property_tycoon_monopoly_engines
      :collapse:

.. py:function:: create_real_estate_mogul_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create real estate mogul-style Monopoly engines with high-powered models.


   .. autolink-examples:: create_real_estate_mogul_monopoly_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.monopoly.generic_engines
   :collapse:
   
.. autolink-skip:: next
