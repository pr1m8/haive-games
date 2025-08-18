games.dominoes.generic_engines
==============================

.. py:module:: games.dominoes.generic_engines

Generic Dominoes engine creation using the generic player agent system.

This module provides generic engine creation functions for Dominoes games, allowing for
configurable LLM models and game-specific player identifiers.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span> • <span class="module-stat">6 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Generic Dominoes engine creation using the generic player agent system.

   This module provides generic engine creation functions for Dominoes games, allowing for
   configurable LLM models and game-specific player identifiers.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.dominoes.generic_engines.dominoes_factory

            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.dominoes.generic_engines.DominoesEngineFactory
      games.dominoes.generic_engines.DominoesPlayerIdentifiers
      games.dominoes.generic_engines.DominoesPromptGenerator

            

.. admonition:: Functions (6)
   :class: info

   .. autoapisummary::

      games.dominoes.generic_engines.create_advanced_dominoes_engines
      games.dominoes.generic_engines.create_budget_dominoes_engines
      games.dominoes.generic_engines.create_generic_dominoes_config_from_example
      games.dominoes.generic_engines.create_generic_dominoes_engines
      games.dominoes.generic_engines.create_generic_dominoes_engines_simple
      games.dominoes.generic_engines.create_mixed_dominoes_engines

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesEngineFactory

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Factory for creating Dominoes game engines.


            .. py:method:: get_structured_output_model(role: str) -> type

               Get the structured output model for a specific role.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesPlayerIdentifiers

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Player identifiers for Dominoes game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesPromptGenerator(players: GamePlayerIdentifiers[PlayerType, PlayerType2])

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Prompt generator for Dominoes game.


            .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create analysis prompt for Dominoes game state.



            .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create move prompt for Dominoes player.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_advanced_dominoes_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create advanced Dominoes engines with high-powered models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_dominoes_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create budget-friendly Dominoes engines.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_dominoes_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Dominoes engines from a predefined example configuration.

            :param example_name: Name of the example configuration
            :param temperature: Generation temperature

            :returns: Dictionary of Dominoes engines
            :rtype: Dict[str, AugLLMConfig]

            Available examples:
                - "gpt_vs_claude": GPT vs Claude
                - "gpt_only": GPT for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "advanced": High-powered models for strategic gameplay




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_dominoes_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Dominoes engines from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations

            :returns: Dictionary of Dominoes engines
            :rtype: Dict[str, AugLLMConfig]

            Expected roles:
                - "player1_player": Player 1 configuration
                - "player2_player": Player 2 configuration
                - "player1_analyzer": Player 1 analyzer configuration
                - "player2_analyzer": Player 2 analyzer configuration




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_dominoes_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Dominoes engines with simple model specifications.

            :param player1_model: Model for player1 and analyzer
            :param player2_model: Model for player2 and analyzer
            :param temperature: Generation temperature

            :returns: Dictionary of Dominoes engines
            :rtype: Dict[str, AugLLMConfig]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_mixed_dominoes_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create mixed-provider Dominoes engines.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: dominoes_factory




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.dominoes.generic_engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

