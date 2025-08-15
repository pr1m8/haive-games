games.clue.generic_engines
==========================

.. py:module:: games.clue.generic_engines

.. autoapi-nested-parse::

   Generic Clue engine creation using the generic player agent system.

   This module provides generic engine creation functions for Clue games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.clue.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.clue.generic_engines.clue_factory


Classes
-------

.. autoapisummary::

   games.clue.generic_engines.ClueEngineFactory
   games.clue.generic_engines.CluePlayerIdentifiers
   games.clue.generic_engines.CluePromptGenerator


Functions
---------

.. autoapisummary::

   games.clue.generic_engines.create_advanced_clue_engines
   games.clue.generic_engines.create_budget_clue_engines
   games.clue.generic_engines.create_generic_clue_config_from_example
   games.clue.generic_engines.create_generic_clue_engines
   games.clue.generic_engines.create_generic_clue_engines_simple
   games.clue.generic_engines.create_mixed_clue_engines


Module Contents
---------------

.. py:class:: ClueEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Clue game engines.


   .. autolink-examples:: ClueEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: CluePlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Clue game.


   .. autolink-examples:: CluePlayerIdentifiers
      :collapse:

.. py:class:: CluePromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Clue game.


   .. autolink-examples:: CluePromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Clue game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Clue player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_advanced_clue_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Clue engines with high-powered models.


   .. autolink-examples:: create_advanced_clue_engines
      :collapse:

.. py:function:: create_budget_clue_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Clue engines.


   .. autolink-examples:: create_budget_clue_engines
      :collapse:

.. py:function:: create_generic_clue_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Clue engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Clue engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_clue_config_from_example
      :collapse:

.. py:function:: create_generic_clue_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Clue engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Clue engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "detective_player": Player 1 configuration
       - "suspect_player": Player 2 configuration
       - "detective_analyzer": Player 1 analyzer configuration
       - "suspect_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_clue_engines
      :collapse:

.. py:function:: create_generic_clue_engines_simple(detective_model: str, suspect_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Clue engines with simple model specifications.

   :param detective_model: Model for detective and analyzer
   :param suspect_model: Model for suspect and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Clue engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_clue_engines_simple
      :collapse:

.. py:function:: create_mixed_clue_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Clue engines.


   .. autolink-examples:: create_mixed_clue_engines
      :collapse:

.. py:data:: clue_factory

