games.mastermind.generic_engines
================================

.. py:module:: games.mastermind.generic_engines

.. autoapi-nested-parse::

   Generic Mastermind engine creation using the generic player agent system.

   This module provides generic engine creation functions for Mastermind games, allowing
   for configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.mastermind.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mastermind.generic_engines.mastermind_factory


Classes
-------

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

.. py:class:: MastermindEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Mastermind game engines.


   .. autolink-examples:: MastermindEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: MastermindPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Mastermind game.


   .. autolink-examples:: MastermindPlayerIdentifiers
      :collapse:

.. py:class:: MastermindPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Mastermind game.


   .. autolink-examples:: MastermindPromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Mastermind game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Mastermind player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_advanced_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Mastermind engines with high-powered models.


   .. autolink-examples:: create_advanced_mastermind_engines
      :collapse:

.. py:function:: create_budget_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Mastermind engines.


   .. autolink-examples:: create_budget_mastermind_engines
      :collapse:

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



   .. autolink-examples:: create_generic_mastermind_config_from_example
      :collapse:

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



   .. autolink-examples:: create_generic_mastermind_engines
      :collapse:

.. py:function:: create_generic_mastermind_engines_simple(codemaker_model: str, codebreaker_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Mastermind engines with simple model specifications.

   :param codemaker_model: Model for codemaker and analyzer
   :param codebreaker_model: Model for codebreaker and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Mastermind engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_mastermind_engines_simple
      :collapse:

.. py:function:: create_mixed_mastermind_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Mastermind engines.


   .. autolink-examples:: create_mixed_mastermind_engines
      :collapse:

.. py:data:: mastermind_factory

