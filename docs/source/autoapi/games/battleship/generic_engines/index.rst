
:py:mod:`games.battleship.generic_engines`
==========================================

.. py:module:: games.battleship.generic_engines

Generic Battleship engine creation using the generic player agent system.

This module provides generic engine creation functions for Battleship games, allowing
for configurable LLM models and game-specific player identifiers.


.. autolink-examples:: games.battleship.generic_engines
   :collapse:

Classes
-------

.. autoapisummary::

   games.battleship.generic_engines.BattleshipEngineFactory
   games.battleship.generic_engines.BattleshipPlayerIdentifiers
   games.battleship.generic_engines.BattleshipPromptGenerator


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BattleshipEngineFactory:

   .. graphviz::
      :align: center

      digraph inheritance_BattleshipEngineFactory {
        node [shape=record];
        "BattleshipEngineFactory" [label="BattleshipEngineFactory"];
        "haive.games.core.agent.generic_player_agent.GenericGameEngineFactory[str, str]" -> "BattleshipEngineFactory";
      }

.. autoclass:: games.battleship.generic_engines.BattleshipEngineFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BattleshipPlayerIdentifiers:

   .. graphviz::
      :align: center

      digraph inheritance_BattleshipPlayerIdentifiers {
        node [shape=record];
        "BattleshipPlayerIdentifiers" [label="BattleshipPlayerIdentifiers"];
        "haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str]" -> "BattleshipPlayerIdentifiers";
      }

.. autoclass:: games.battleship.generic_engines.BattleshipPlayerIdentifiers
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BattleshipPromptGenerator:

   .. graphviz::
      :align: center

      digraph inheritance_BattleshipPromptGenerator {
        node [shape=record];
        "BattleshipPromptGenerator" [label="BattleshipPromptGenerator"];
        "haive.games.core.agent.generic_player_agent.GenericPromptGenerator[str, str]" -> "BattleshipPromptGenerator";
      }

.. autoclass:: games.battleship.generic_engines.BattleshipPromptGenerator
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.battleship.generic_engines.create_budget_battleship_engines
   games.battleship.generic_engines.create_generic_battleship_config_from_example
   games.battleship.generic_engines.create_generic_battleship_engines
   games.battleship.generic_engines.create_generic_battleship_engines_simple
   games.battleship.generic_engines.create_mixed_battleship_engines
   games.battleship.generic_engines.create_naval_battleship_engines

.. py:function:: create_budget_battleship_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Battleship engines.


   .. autolink-examples:: create_budget_battleship_engines
      :collapse:

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



   .. autolink-examples:: create_generic_battleship_config_from_example
      :collapse:

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



   .. autolink-examples:: create_generic_battleship_engines
      :collapse:

.. py:function:: create_generic_battleship_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Battleship engines with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Battleship engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_battleship_engines_simple
      :collapse:

.. py:function:: create_mixed_battleship_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Battleship engines.


   .. autolink-examples:: create_mixed_battleship_engines
      :collapse:

.. py:function:: create_naval_battleship_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create naval commander-style Battleship engines with high-powered models.


   .. autolink-examples:: create_naval_battleship_engines
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.battleship.generic_engines
   :collapse:
   
.. autolink-skip:: next
