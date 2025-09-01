games.battleship.generic_engines
================================

.. py:module:: games.battleship.generic_engines

.. autoapi-nested-parse::

   Generic Battleship engine creation using the generic player agent system.

   This module provides generic engine creation functions for Battleship games, allowing
   for configurable LLM models and game-specific player identifiers.



Attributes
----------

.. autoapisummary::

   games.battleship.generic_engines.battleship_factory


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/battleship/generic_engines/BattleshipEngineFactory
   /autoapi/games/battleship/generic_engines/BattleshipPlayerIdentifiers
   /autoapi/games/battleship/generic_engines/BattleshipPromptGenerator

.. autoapisummary::

   games.battleship.generic_engines.BattleshipEngineFactory
   games.battleship.generic_engines.BattleshipPlayerIdentifiers
   games.battleship.generic_engines.BattleshipPromptGenerator


Functions
---------

.. autoapisummary::

   games.battleship.generic_engines.create_budget_battleship_engines
   games.battleship.generic_engines.create_generic_battleship_config_from_example
   games.battleship.generic_engines.create_generic_battleship_engines
   games.battleship.generic_engines.create_generic_battleship_engines_simple
   games.battleship.generic_engines.create_mixed_battleship_engines
   games.battleship.generic_engines.create_naval_battleship_engines


Module Contents
---------------

.. py:function:: create_budget_battleship_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Battleship engines.


.. py:function:: create_generic_battleship_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Battleship engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Battleship engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "naval_commanders": High-powered models for strategic gameplay



.. py:function:: create_generic_battleship_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Battleship engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Battleship engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



.. py:function:: create_generic_battleship_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Battleship engines with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Battleship engines
   :rtype: Dict[str, AugLLMConfig]


.. py:function:: create_mixed_battleship_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Battleship engines.


.. py:function:: create_naval_battleship_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create naval commander-style Battleship engines with high-powered models.


.. py:data:: battleship_factory

