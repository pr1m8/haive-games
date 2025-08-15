games.debate.generic_engines
============================

.. py:module:: games.debate.generic_engines

.. autoapi-nested-parse::

   Generic Debate engine creation using the generic player agent system.

   This module provides generic engine creation functions for Debate games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.debate.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.debate.generic_engines.debate_factory


Classes
-------

.. autoapisummary::

   games.debate.generic_engines.DebateEngineFactory
   games.debate.generic_engines.DebatePlayerIdentifiers
   games.debate.generic_engines.DebatePromptGenerator


Functions
---------

.. autoapisummary::

   games.debate.generic_engines.create_advanced_debate_engines
   games.debate.generic_engines.create_budget_debate_engines
   games.debate.generic_engines.create_generic_debate_config_from_example
   games.debate.generic_engines.create_generic_debate_engines
   games.debate.generic_engines.create_generic_debate_engines_simple
   games.debate.generic_engines.create_mixed_debate_engines


Module Contents
---------------

.. py:class:: DebateEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Debate game engines.


   .. autolink-examples:: DebateEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: DebatePlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Debate game.


   .. autolink-examples:: DebatePlayerIdentifiers
      :collapse:

.. py:class:: DebatePromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Debate game.


   .. autolink-examples:: DebatePromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Debate game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Debate player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_advanced_debate_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Debate engines with high-powered models.


   .. autolink-examples:: create_advanced_debate_engines
      :collapse:

.. py:function:: create_budget_debate_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Debate engines.


   .. autolink-examples:: create_budget_debate_engines
      :collapse:

.. py:function:: create_generic_debate_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Debate engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Debate engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_debate_config_from_example
      :collapse:

.. py:function:: create_generic_debate_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Debate engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Debate engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "debater1_player": Player 1 configuration
       - "debater2_player": Player 2 configuration
       - "debater1_analyzer": Player 1 analyzer configuration
       - "debater2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_debate_engines
      :collapse:

.. py:function:: create_generic_debate_engines_simple(debater1_model: str, debater2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Debate engines with simple model specifications.

   :param debater1_model: Model for debater1 and analyzer
   :param debater2_model: Model for debater2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Debate engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_debate_engines_simple
      :collapse:

.. py:function:: create_mixed_debate_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Debate engines.


   .. autolink-examples:: create_mixed_debate_engines
      :collapse:

.. py:data:: debate_factory

