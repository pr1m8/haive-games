games.mafia.generic_engines
===========================

.. py:module:: games.mafia.generic_engines

.. autoapi-nested-parse::

   Generic Mafia engine creation using the generic player agent system.

   This module provides generic engine creation functions for Mafia games, allowing for
   configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.mafia.generic_engines.mafia_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/generic_engines/MafiaEngineFactory
   /autoapi/games/mafia/generic_engines/MafiaPlayerIdentifiers
   /autoapi/games/mafia/generic_engines/MafiaPromptGenerator

.. autoapisummary::

   games.mafia.generic_engines.MafiaEngineFactory
   games.mafia.generic_engines.MafiaPlayerIdentifiers
   games.mafia.generic_engines.MafiaPromptGenerator


Functions
---------

.. autoapisummary::

   games.mafia.generic_engines.create_advanced_mafia_engines
   games.mafia.generic_engines.create_budget_mafia_engines
   games.mafia.generic_engines.create_generic_mafia_config_from_example
   games.mafia.generic_engines.create_generic_mafia_engines
   games.mafia.generic_engines.create_generic_mafia_engines_simple
   games.mafia.generic_engines.create_mixed_mafia_engines


Module Contents
---------------

.. py:function:: create_advanced_mafia_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Mafia engines with high-powered models.


.. py:function:: create_budget_mafia_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Mafia engines.


.. py:function:: create_generic_mafia_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mafia engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Mafia engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



.. py:function:: create_generic_mafia_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mafia engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Mafia engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "mafia_player": Player 1 configuration
       - "town_player": Player 2 configuration
       - "mafia_analyzer": Player 1 analyzer configuration
       - "town_analyzer": Player 2 analyzer configuration



.. py:function:: create_generic_mafia_engines_simple(mafia_model: str, town_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mafia engines with simple model specifications.

   :param mafia_model: Model for mafia and analyzer
   :param town_model: Model for town and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Mafia engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_mafia_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Mafia engines.


.. py:data:: mafia_factory

