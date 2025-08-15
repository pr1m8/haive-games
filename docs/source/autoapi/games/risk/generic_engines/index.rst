games.risk.generic_engines
==========================

.. py:module:: games.risk.generic_engines

.. autoapi-nested-parse::

   Generic Risk engine creation using the generic player agent system.

   This module provides generic engine creation functions for Risk games, allowing for
   configurable LLM models and game-specific player identifiers.


   .. autolink-examples:: games.risk.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.risk.generic_engines.risk_factory


Classes
-------

.. autoapisummary::

   games.risk.generic_engines.RiskEngineFactory
   games.risk.generic_engines.RiskPlayerIdentifiers
   games.risk.generic_engines.RiskPromptGenerator


Functions
---------

.. autoapisummary::

   games.risk.generic_engines.create_advanced_risk_engines
   games.risk.generic_engines.create_budget_risk_engines
   games.risk.generic_engines.create_generic_risk_config_from_example
   games.risk.generic_engines.create_generic_risk_engines
   games.risk.generic_engines.create_generic_risk_engines_simple
   games.risk.generic_engines.create_mixed_risk_engines


Module Contents
---------------

.. py:class:: RiskEngineFactory

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Factory for creating Risk game engines.


   .. autolink-examples:: RiskEngineFactory
      :collapse:

   .. py:method:: get_structured_output_model(role: str) -> type

      Get the structured output model for a specific role.


      .. autolink-examples:: get_structured_output_model
         :collapse:


.. py:class:: RiskPlayerIdentifiers

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Player identifiers for Risk game.


   .. autolink-examples:: RiskPlayerIdentifiers
      :collapse:

.. py:class:: RiskPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Prompt generator for Risk game.


   .. autolink-examples:: RiskPromptGenerator
      :collapse:

   .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create analysis prompt for Risk game state.


      .. autolink-examples:: create_analyzer_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create move prompt for Risk player.


      .. autolink-examples:: create_move_prompt
         :collapse:


.. py:function:: create_advanced_risk_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create advanced Risk engines with high-powered models.


   .. autolink-examples:: create_advanced_risk_engines
      :collapse:

.. py:function:: create_budget_risk_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create budget-friendly Risk engines.


   .. autolink-examples:: create_budget_risk_engines
      :collapse:

.. py:function:: create_generic_risk_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Risk engines from a predefined example configuration.

   :param example_name: Name of the example configuration
   :param temperature: Generation temperature

   :returns: Dictionary of Risk engines
   :rtype: Dict[str, AugLLMConfig]

   Available examples:
       - "gpt_vs_claude": GPT vs Claude
       - "gpt_only": GPT for both players
       - "claude_only": Claude for both players
       - "budget": Cost-effective models
       - "mixed": Different provider per role
       - "advanced": High-powered models for strategic gameplay



   .. autolink-examples:: create_generic_risk_config_from_example
      :collapse:

.. py:function:: create_generic_risk_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Risk engines from detailed player configurations.

   :param player_configs: Dictionary mapping role names to player configurations

   :returns: Dictionary of Risk engines
   :rtype: Dict[str, AugLLMConfig]

   Expected roles:
       - "player1_player": Player 1 configuration
       - "player2_player": Player 2 configuration
       - "player1_analyzer": Player 1 analyzer configuration
       - "player2_analyzer": Player 2 analyzer configuration



   .. autolink-examples:: create_generic_risk_engines
      :collapse:

.. py:function:: create_generic_risk_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Risk engines with simple model specifications.

   :param player1_model: Model for player1 and analyzer
   :param player2_model: Model for player2 and analyzer
   :param temperature: Generation temperature

   :returns: Dictionary of Risk engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_generic_risk_engines_simple
      :collapse:

.. py:function:: create_mixed_risk_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create mixed-provider Risk engines.


   .. autolink-examples:: create_mixed_risk_engines
      :collapse:

.. py:data:: risk_factory

