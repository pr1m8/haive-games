games.monopoly.generic_engines
==============================

.. py:module:: games.monopoly.generic_engines

.. autoapi-nested-parse::

   Generic Monopoly engine creation using the generic player agent system.

   This module provides generic engine creation functions for Monopoly games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.monopoly.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.monopoly.generic_engines.monopoly_factory


Classes
-------

.. autoapisummary::

   games.monopoly.generic_engines.MonopolyEngineFactory
   games.monopoly.generic_engines.MonopolyPlayerIdentifiers
   games.monopoly.generic_engines.MonopolyPromptGenerator


Functions
---------

.. autoapisummary::

   games.monopoly.generic_engines.create_budget_monopoly_engines
   games.monopoly.generic_engines.create_generic_monopoly_config_from_example
   games.monopoly.generic_engines.create_generic_monopoly_engines
   games.monopoly.generic_engines.create_generic_monopoly_engines_simple
   games.monopoly.generic_engines.create_mixed_monopoly_engines
   games.monopoly.generic_engines.create_property_tycoon_monopoly_engines
   games.monopoly.generic_engines.create_real_estate_mogul_monopoly_engines


Module Contents
---------------

.. py:class:: MonopolyEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Monopoly game engines.


   .. autolink-examples:: MonopolyEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: MonopolyPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Monopoly game.


   .. autolink-examples:: MonopolyPlayerIdentifiers
      :collapse:

.. py:class:: MonopolyPromptGenerator(players: haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers[str, str])

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Monopoly game.


   .. autolink-examples:: MonopolyPromptGenerator
      :collapse:

   .. py:method:: create_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt - alias for create_analyzer_prompt.


      .. autolink-examples:: create_analysis_prompt
         :collapse:


   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Monopoly game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Monopoly player.


      .. autolink-examples:: create_move_prompt
         :collapse:


   .. py:method:: get_analysis_output_model(role: str) -> type

      Get analysis output model.


      .. autolink-examples:: get_analysis_output_model
         :collapse:


   .. py:method:: get_move_output_model(role: str) -> type

      Get move output model.


      .. autolink-examples:: get_move_output_model
         :collapse:


.. py:function:: create_budget_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Monopoly engines.


   .. autolink-examples:: create_budget_monopoly_engines
      :collapse:

.. py:function:: create_generic_monopoly_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Monopoly engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Monopoly engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "real_estate_moguls": High-powered models for strategic gameplay
       - "property_tycoons": Specialized for property investment



   .. autolink-examples:: create_generic_monopoly_config_from_example
      :collapse:

.. py:function:: create_generic_monopoly_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Monopoly engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Monopoly engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_monopoly_engines
      :collapse:

.. py:function:: create_generic_monopoly_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Monopoly engines with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Monopoly engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_monopoly_engines_simple
      :collapse:

.. py:function:: create_mixed_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Monopoly engines.


   .. autolink-examples:: create_mixed_monopoly_engines
      :collapse:

.. py:function:: create_property_tycoon_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create property tycoon-style Monopoly engines.


   .. autolink-examples:: create_property_tycoon_monopoly_engines
      :collapse:

.. py:function:: create_real_estate_mogul_monopoly_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create real estate mogul-style Monopoly engines with high-powered models.


   .. autolink-examples:: create_real_estate_mogul_monopoly_engines
      :collapse:

.. py:data:: monopoly_factory

