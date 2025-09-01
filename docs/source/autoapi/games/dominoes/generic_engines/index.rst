games.dominoes.generic_engines
==============================

.. py:module:: games.dominoes.generic_engines

.. autoapi-nested-parse::

   Generic Dominoes engine creation using the generic player agent system.

   This module provides generic engine creation functions for Dominoes games, allowing for
   configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.dominoes.generic_engines.dominoes_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/dominoes/generic_engines/DominoesEngineFactory
   /autoapi/games/dominoes/generic_engines/DominoesPlayerIdentifiers
   /autoapi/games/dominoes/generic_engines/DominoesPromptGenerator

.. autoapisummary::

   games.dominoes.generic_engines.DominoesEngineFactory
   games.dominoes.generic_engines.DominoesPlayerIdentifiers
   games.dominoes.generic_engines.DominoesPromptGenerator


Functions
---------

.. autoapisummary::

   games.dominoes.generic_engines.create_advanced_dominoes_engines
   games.dominoes.generic_engines.create_budget_dominoes_engines
   games.dominoes.generic_engines.create_generic_dominoes_config_from_example
   games.dominoes.generic_engines.create_generic_dominoes_engines
   games.dominoes.generic_engines.create_generic_dominoes_engines_simple
   games.dominoes.generic_engines.create_mixed_dominoes_engines


Module Contents
---------------

.. py:function:: create_advanced_dominoes_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Dominoes engines with high-powered models.


.. py:function:: create_budget_dominoes_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Dominoes engines.


.. py:function:: create_generic_dominoes_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Dominoes engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Dominoes engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



.. py:function:: create_generic_dominoes_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Dominoes engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Dominoes engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



.. py:function:: create_generic_dominoes_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Dominoes engines with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Dominoes engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_dominoes_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Dominoes engines.


.. py:data:: dominoes_factory

