games.nim.generic_engines
=========================

.. py:module:: games.nim.generic_engines

.. autoapi-nested-parse::

   Generic Nim engine creation using the generic player agent system.

   This module provides generic engine creation functions for Nim games, allowing for
   configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.nim.generic_engines.nim_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/nim/generic_engines/NimEngineFactory
   /autoapi/games/nim/generic_engines/NimPlayerIdentifiers
   /autoapi/games/nim/generic_engines/NimPromptGenerator

.. autoapisummary::

   games.nim.generic_engines.NimEngineFactory
   games.nim.generic_engines.NimPlayerIdentifiers
   games.nim.generic_engines.NimPromptGenerator


Functions
---------

.. autoapisummary::

   games.nim.generic_engines.create_advanced_nim_engines
   games.nim.generic_engines.create_budget_nim_engines
   games.nim.generic_engines.create_generic_nim_config_from_example
   games.nim.generic_engines.create_generic_nim_engines
   games.nim.generic_engines.create_generic_nim_engines_simple
   games.nim.generic_engines.create_mixed_nim_engines


Module Contents
---------------

.. py:function:: create_advanced_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Nim engines with high-powered models.


.. py:function:: create_budget_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Nim engines.


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



.. py:function:: create_generic_nim_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Nim engines with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Nim engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Nim engines.


.. py:data:: nim_factory

