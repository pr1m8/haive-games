games.mastermind.generic_engines
================================

.. py:module:: games.mastermind.generic_engines

.. autoapi-nested-parse::

   Generic Mastermind engine creation using the generic player agent system.

   This module provides generic engine creation functions for Mastermind games, allowing
   for configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.mastermind.generic_engines.mastermind_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mastermind/generic_engines/MastermindEngineFactory
   /autoapi/games/mastermind/generic_engines/MastermindPlayerIdentifiers
   /autoapi/games/mastermind/generic_engines/MastermindPromptGenerator

.. autoapisummary::

   games.mastermind.generic_engines.MastermindEngineFactory
   games.mastermind.generic_engines.MastermindPlayerIdentifiers
   games.mastermind.generic_engines.MastermindPromptGenerator


Functions
---------

.. autoapisummary::

   games.mastermind.generic_engines.create_advanced_mastermind_engines
   games.mastermind.generic_engines.create_budget_mastermind_engines
   games.mastermind.generic_engines.create_generic_mastermind_config_from_example
   games.mastermind.generic_engines.create_generic_mastermind_engines
   games.mastermind.generic_engines.create_generic_mastermind_engines_simple
   games.mastermind.generic_engines.create_mixed_mastermind_engines


Module Contents
---------------

.. py:function:: create_advanced_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Mastermind engines with high-powered models.


.. py:function:: create_budget_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Mastermind engines.


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



.. py:function:: create_generic_mastermind_engines_simple(codemaker_model: str, codebreaker_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mastermind engines with simple model specifications.

   :param codemaker_model: Model for codemaker and analyzer
   :param codebreaker_model: Model for codebreaker and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Mastermind engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Mastermind engines.


.. py:data:: mastermind_factory

