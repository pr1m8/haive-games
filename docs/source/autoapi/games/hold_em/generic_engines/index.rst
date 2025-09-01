games.hold_em.generic_engines
=============================

.. py:module:: games.hold_em.generic_engines

.. autoapi-nested-parse::

   Generic Hold'em engine creation using the generic player agent system.

   This module provides generic engine creation functions for Texas Hold'em games, allowing
   for configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.hold_em.generic_engines.holdem_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/generic_engines/HoldemEngineFactory
   /autoapi/games/hold_em/generic_engines/HoldemPlayerIdentifiers
   /autoapi/games/hold_em/generic_engines/HoldemPromptGenerator

.. autoapisummary::

   games.hold_em.generic_engines.HoldemEngineFactory
   games.hold_em.generic_engines.HoldemPlayerIdentifiers
   games.hold_em.generic_engines.HoldemPromptGenerator


Functions
---------

.. autoapisummary::

   games.hold_em.generic_engines.create_budget_holdem_engines
   games.hold_em.generic_engines.create_generic_holdem_config_from_example
   games.hold_em.generic_engines.create_generic_holdem_engines
   games.hold_em.generic_engines.create_generic_holdem_engines_simple
   games.hold_em.generic_engines.create_heads_up_holdem_engines
   games.hold_em.generic_engines.create_mixed_holdem_engines
   games.hold_em.generic_engines.create_poker_pro_holdem_engines


Module Contents
---------------

.. py:function:: create_budget_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Hold'em engines.


.. py:function:: create_generic_holdem_config_from_example(example_name: str, temperature: float = 0.4) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Hold'em engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Hold'em engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "poker_pros": High-powered models for strategic gameplay
       - "heads_up": Specialized for heads-up play



.. py:function:: create_generic_holdem_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Hold'em engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Hold'em engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



.. py:function:: create_generic_holdem_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.4) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Hold'em engines with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Hold'em engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_heads_up_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create specialized Hold'em engines for heads-up play.


.. py:function:: create_mixed_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Hold'em engines.


.. py:function:: create_poker_pro_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create poker professional-style Hold'em engines with high-powered models.


.. py:data:: holdem_factory

