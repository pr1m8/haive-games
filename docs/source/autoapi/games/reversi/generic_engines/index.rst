games.reversi.generic_engines
=============================

.. py:module:: games.reversi.generic_engines

.. autoapi-nested-parse::

   Generic Reversi engine creation using the generic player agent system.

   This module provides generic engine creation functions for Reversi games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.reversi.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.reversi.generic_engines.reversi_factory


Classes
-------

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

.. py:class:: ReversiEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Reversi game engines.


   .. autolink-examples:: ReversiEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: ReversiPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Reversi game.


   .. autolink-examples:: ReversiPlayerIdentifiers
      :collapse:

.. py:class:: ReversiPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Reversi game.


   .. autolink-examples:: ReversiPromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Reversi game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Reversi player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_advanced_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Reversi engines with high-powered models.


   .. autolink-examples:: create_advanced_reversi_engines
      :collapse:

.. py:function:: create_budget_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Reversi engines.


   .. autolink-examples:: create_budget_reversi_engines
      :collapse:

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



   .. autolink-examples:: create_generic_reversi_config_from_example
      :collapse:

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



   .. autolink-examples:: create_generic_reversi_engines
      :collapse:

.. py:function:: create_generic_reversi_engines_simple(black_model: str, white_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Reversi engines with simple model specifications.

   :param black_model: Model for black and analyzer
   :param white_model: Model for white and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Reversi engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_reversi_engines_simple
      :collapse:

.. py:function:: create_mixed_reversi_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Reversi engines.


   .. autolink-examples:: create_mixed_reversi_engines
      :collapse:

.. py:data:: reversi_factory

