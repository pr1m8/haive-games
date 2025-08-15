games.hold_em.generic_engines
=============================

.. py:module:: games.hold_em.generic_engines

.. autoapi-nested-parse::

   Generic Hold'em engine creation using the generic player agent system.

   This module provides generic engine creation functions for Texas Hold'em games, allowing
   for configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.hold_em.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.hold_em.generic_engines.holdem_factory


Classes
-------

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

.. py:class:: HoldemEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Texas Hold'em game engines.


   .. autolink-examples:: HoldemEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: HoldemPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Texas Hold'em game.


   .. autolink-examples:: HoldemPlayerIdentifiers
      :collapse:

.. py:class:: HoldemPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Texas Hold'em game.


   .. autolink-examples:: HoldemPromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Hold'em game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Hold'em player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_budget_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Hold'em engines.


   .. autolink-examples:: create_budget_holdem_engines
      :collapse:

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



   .. autolink-examples:: create_generic_holdem_config_from_example
      :collapse:

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



   .. autolink-examples:: create_generic_holdem_engines
      :collapse:

.. py:function:: create_generic_holdem_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.4) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Hold'em engines with simple model specifications.

   :param player1_model: Model for player 1 and analyzer
   :param player2_model: Model for player 2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Hold'em engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_holdem_engines_simple
      :collapse:

.. py:function:: create_heads_up_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create specialized Hold'em engines for heads-up play.


   .. autolink-examples:: create_heads_up_holdem_engines
      :collapse:

.. py:function:: create_mixed_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Hold'em engines.


   .. autolink-examples:: create_mixed_holdem_engines
      :collapse:

.. py:function:: create_poker_pro_holdem_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create poker professional-style Hold'em engines with high-powered models.


   .. autolink-examples:: create_poker_pro_holdem_engines
      :collapse:

.. py:data:: holdem_factory

