games.mancala.generic_engines
=============================

.. py:module:: games.mancala.generic_engines

.. autoapi-nested-parse::

   Generic Mancala engine creation using the generic player agent system.

   This module provides generic engine creation functions for Mancala games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.mancala.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mancala.generic_engines.mancala_factory


Classes
-------

.. autoapisummary::

   games.mancala.generic_engines.MancalaEngineFactory
   games.mancala.generic_engines.MancalaPlayerIdentifiers
   games.mancala.generic_engines.MancalaPromptGenerator


Functions
---------

.. autoapisummary::

   games.mancala.generic_engines.create_advanced_mancala_engines
   games.mancala.generic_engines.create_budget_mancala_engines
   games.mancala.generic_engines.create_generic_mancala_config_from_example
   games.mancala.generic_engines.create_generic_mancala_engines
   games.mancala.generic_engines.create_generic_mancala_engines_simple
   games.mancala.generic_engines.create_mixed_mancala_engines


Module Contents
---------------

.. py:class:: MancalaEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Mancala game engines.


   .. autolink-examples:: MancalaEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: MancalaPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Mancala game.


   .. autolink-examples:: MancalaPlayerIdentifiers
      :collapse:

.. py:class:: MancalaPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Mancala game.


   .. autolink-examples:: MancalaPromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Mancala game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Mancala player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_advanced_mancala_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Mancala engines with high-powered models.


   .. autolink-examples:: create_advanced_mancala_engines
      :collapse:

.. py:function:: create_budget_mancala_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Mancala engines.


   .. autolink-examples:: create_budget_mancala_engines
      :collapse:

.. py:function:: create_generic_mancala_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mancala engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Mancala engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_mancala_config_from_example
      :collapse:

.. py:function:: create_generic_mancala_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mancala engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Mancala engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_mancala_engines
      :collapse:

.. py:function:: create_generic_mancala_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mancala engines with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Mancala engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_mancala_engines_simple
      :collapse:

.. py:function:: create_mixed_mancala_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Mancala engines.


   .. autolink-examples:: create_mixed_mancala_engines
      :collapse:

.. py:data:: mancala_factory

