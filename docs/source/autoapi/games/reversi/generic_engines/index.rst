games.reversi.generic_engines
=============================

.. py:module:: games.reversi.generic_engines

.. autoapi-nested-parse::

   Generic Reversi engine creation using the generic player agent system.

   This module provides generic engine creation functions for Reversi games, allowing for
   configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.reversi.generic_engines.reversi_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/reversi/generic_engines/ReversiEngineFactory
   /autoapi/games/reversi/generic_engines/ReversiPlayerIdentifiers
   /autoapi/games/reversi/generic_engines/ReversiPromptGenerator

.. autoapisummary::

   games.reversi.generic_engines.ReversiEngineFactory
   games.reversi.generic_engines.ReversiPlayerIdentifiers
   games.reversi.generic_engines.ReversiPromptGenerator


Functions
---------

.. autoapisummary::

   games.reversi.generic_engines.create_advanced_reversi_engines
   games.reversi.generic_engines.create_budget_reversi_engines
   games.reversi.generic_engines.create_generic_reversi_config_from_example
   games.reversi.generic_engines.create_generic_reversi_engines
   games.reversi.generic_engines.create_generic_reversi_engines_simple
   games.reversi.generic_engines.create_mixed_reversi_engines


Module Contents
---------------

.. py:function:: create_advanced_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Reversi engines with high-powered models.


.. py:function:: create_budget_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Reversi engines.


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



.. py:function:: create_generic_reversi_engines_simple(black_model: str, white_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Reversi engines with simple model specifications.

   :param black_model: Model for black and analyzer
   :param white_model: Model for white and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Reversi engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Reversi engines.


.. py:data:: reversi_factory

