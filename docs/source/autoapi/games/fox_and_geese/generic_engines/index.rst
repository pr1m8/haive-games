games.fox_and_geese.generic_engines
===================================

.. py:module:: games.fox_and_geese.generic_engines

.. autoapi-nested-parse::

   Generic FoxAndGeese engine creation using the generic player agent system.

   This module provides generic engine creation functions for FoxAndGeese games, allowing
   for configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.fox_and_geese.generic_engines.fox_and_geese_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/fox_and_geese/generic_engines/FoxAndGeeseEngineFactory
   /autoapi/games/fox_and_geese/generic_engines/FoxAndGeesePlayerIdentifiers
   /autoapi/games/fox_and_geese/generic_engines/FoxAndGeesePromptGenerator

.. autoapisummary::

   games.fox_and_geese.generic_engines.FoxAndGeeseEngineFactory
   games.fox_and_geese.generic_engines.FoxAndGeesePlayerIdentifiers
   games.fox_and_geese.generic_engines.FoxAndGeesePromptGenerator


Functions
---------

.. autoapisummary::

   games.fox_and_geese.generic_engines.create_advanced_fox_and_geese_engines
   games.fox_and_geese.generic_engines.create_budget_fox_and_geese_engines
   games.fox_and_geese.generic_engines.create_generic_fox_and_geese_config_from_example
   games.fox_and_geese.generic_engines.create_generic_fox_and_geese_engines
   games.fox_and_geese.generic_engines.create_generic_fox_and_geese_engines_simple
   games.fox_and_geese.generic_engines.create_mixed_fox_and_geese_engines


Module Contents
---------------

.. py:function:: create_advanced_fox_and_geese_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced FoxAndGeese engines with high-powered models.


.. py:function:: create_budget_fox_and_geese_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly FoxAndGeese engines.


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



.. py:function:: create_generic_fox_and_geese_engines_simple(fox_model: str, geese_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create FoxAndGeese engines with simple model specifications.

   :param fox_model: Model for fox and analyzer
   :param geese_model: Model for geese and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of FoxAndGeese engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_fox_and_geese_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider FoxAndGeese engines.


.. py:data:: fox_and_geese_factory

