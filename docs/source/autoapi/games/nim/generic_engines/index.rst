games.nim.generic_engines
=========================

.. py:module:: games.nim.generic_engines

Generic Nim engine creation using the generic player agent system.

This module provides generic engine creation functions for Nim games, allowing for
configurable LLM models and game-specific player identifiers.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span> • <span class="module-stat">6 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Generic Nim engine creation using the generic player agent system.

   This module provides generic engine creation functions for Nim games, allowing for
   configurable LLM models and game-specific player identifiers.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.nim.generic_engines.nim_factory

            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.nim.generic_engines.NimEngineFactory
      games.nim.generic_engines.NimPlayerIdentifiers
      games.nim.generic_engines.NimPromptGenerator

            

.. admonition:: Functions (6)
   :class: info

   .. autoapisummary::

      games.nim.generic_engines.create_advanced_nim_engines
      games.nim.generic_engines.create_budget_nim_engines
      games.nim.generic_engines.create_generic_nim_config_from_example
      games.nim.generic_engines.create_generic_nim_engines
      games.nim.generic_engines.create_generic_nim_engines_simple
      games.nim.generic_engines.create_mixed_nim_engines

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimEngineFactory

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericGameEngineFactory`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Factory for creating Nim game engines.


            .. py:method:: get_structured_output_model(role: str) -> type

               Get the structured output model for a specific role.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimPlayerIdentifiers

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GamePlayerIdentifiers`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Player identifiers for Nim game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimPromptGenerator(players: GamePlayerIdentifiers[PlayerType, PlayerType2])

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Prompt generator for Nim game.


            .. py:method:: create_analyzer_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create analysis prompt for Nim game state.



            .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create move prompt for Nim player.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_advanced_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create advanced Nim engines with high-powered models.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_budget_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create budget-friendly Nim engines.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_nim_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Nim engines from a predefined example configuration.

            :param example_name: Name of the example configuration
            :param temperature: Generation temperature

            :returns: Dictionary of Nim engines
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

.. py:function:: create_generic_nim_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Nim engines from detailed player configurations.

            :param player_configs: Dictionary mapping role names to player configurations

            :returns: Dictionary of Nim engines
            :rtype: Dict[str, AugLLMConfig]

            Expected roles:
                - "player1_player": Player 1 configuration
                - "player2_player": Player 2 configuration
                - "player1_analyzer": Player 1 analyzer configuration
                - "player2_analyzer": Player 2 analyzer configuration




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_nim_engines_simple(player1_model: str, player2_model: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Nim engines with simple model specifications.

            :param player1_model: Model for player1 and analyzer
            :param player2_model: Model for player2 and analyzer
            :param temperature: Generation temperature

            :returns: Dictionary of Nim engines
            :rtype: Dict[str, AugLLMConfig]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_mixed_nim_engines(**kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create mixed-provider Nim engines.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: nim_factory




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.generic_engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

