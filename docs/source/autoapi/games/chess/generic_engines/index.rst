games.chess.generic_engines
===========================

.. py:module:: games.chess.generic_engines

Generic chess engines using the new generic player agent system.

This module demonstrates how to use the generic player agent system for chess, providing
a clean, type-safe implementation that eliminates hardcoded LLM configurations.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">6 functions</span> • <span class="module-stat">3 attributes</span>   </div>

.. autoapi-nested-parse::

   Generic chess engines using the new generic player agent system.

   This module demonstrates how to use the generic player agent system for chess, providing
   a clean, type-safe implementation that eliminates hardcoded LLM configurations.



      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.chess.generic_engines.chess_engine_factory
      games.chess.generic_engines.chess_players
      games.chess.generic_engines.chess_prompt_generator

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.generic_engines.ChessPromptGenerator

            

.. admonition:: Functions (6)
   :class: info

   .. autoapisummary::

      games.chess.generic_engines.create_generic_chess_config_from_example
      games.chess.generic_engines.create_generic_chess_engines
      games.chess.generic_engines.create_generic_chess_engines_simple
      games.chess.generic_engines.create_role_specific_chess_engines
      games.chess.generic_engines.create_typed_chess_engines
      games.chess.generic_engines.demonstrate_generic_pattern

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessPromptGenerator(players: GamePlayerIdentifiers[PlayerType, PlayerType2])

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Chess-specific prompt generator using the generic system.


            .. py:method:: create_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create a chess analysis prompt for the specified player.

               :param player: Player color ("white" or "black")

               :returns: Prompt template for position analysis
               :rtype: ChatPromptTemplate



            .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create a chess move prompt for the specified player.

               :param player: Player color ("white" or "black")

               :returns: Prompt template for move generation
               :rtype: ChatPromptTemplate



            .. py:method:: get_analysis_output_model() -> type

               Get the structured output model for chess analysis.



            .. py:method:: get_move_output_model() -> type

               Get the structured output model for chess moves.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_chess_config_from_example(example_name: str, temperature: float = 0.7) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create chess engines from predefined examples using generics.

            :param example_name: Name of the example configuration
            :param temperature: Temperature for all engines

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]

            Available examples:
                - "anthropic_vs_openai": Claude vs GPT-4
                - "gpt4_only": GPT-4 for all roles
                - "claude_only": Claude for all roles
                - "mixed_providers": Different provider per role
                - "budget_friendly": Cost-effective models




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_chess_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create chess engines using the generic system.

            :param player_configs: Dictionary of role name to player configuration

            :returns: Dictionary of configured engines
            :rtype: dict[str, AugLLMConfig]

            .. rubric:: Example

            >>> configs = {
            ...     "white_player": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
            ...     "white_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
            ... }
            >>> engines = create_generic_chess_engines(configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_chess_engines_simple(white_model: str | haive.core.models.llm.LLMConfig = 'gpt-4o', black_model: str | haive.core.models.llm.LLMConfig = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create chess engines with simple model configurations using generics.

            :param white_model: Model for white player and analyzer
            :param black_model: Model for black player and analyzer
            :param temperature: Temperature for player engines
            :param \*\*kwargs: Additional configuration parameters

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]

            .. rubric:: Example

            >>> engines = create_generic_chess_engines_simple("gpt-4", "claude-3-opus")
            >>> engines = create_generic_chess_engines_simple(
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     "openai:gpt-4o",
            ...     temperature=0.8
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_role_specific_chess_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create chess engines with different models per role using generics.

            This example shows how to use different LLM models for players vs analyzers,
            demonstrating the flexibility of the generic system.

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_typed_chess_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Demonstrate type-safe engine creation using the generic system.

            This function shows how the generic system provides compile-time type checking
            for player identifiers and role names.

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: demonstrate_generic_pattern()

            Demonstrate how the generic pattern works across different games.

            This function shows how the same generic system can be used for any two-player game
            with just different player identifiers and prompts.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: chess_engine_factory


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: chess_players


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: chess_prompt_generator




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.generic_engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

