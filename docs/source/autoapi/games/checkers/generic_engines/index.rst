games.checkers.generic_engines
==============================

.. py:module:: games.checkers.generic_engines

Generic Checkers engines using the new generic player agent system.

from typing import Any This module demonstrates how to use the generic player agent
system for Checkers, showing the same pattern working across different games with
different player identifiers.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">5 functions</span> • <span class="module-stat">3 attributes</span>   </div>

.. autoapi-nested-parse::

   Generic Checkers engines using the new generic player agent system.

   from typing import Any This module demonstrates how to use the generic player agent
   system for Checkers, showing the same pattern working across different games with
   different player identifiers.



      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.checkers.generic_engines.checkers_engine_factory
      games.checkers.generic_engines.checkers_players
      games.checkers.generic_engines.checkers_prompt_generator

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.checkers.generic_engines.CheckersPromptGenerator

            

.. admonition:: Functions (5)
   :class: info

   .. autoapisummary::

      games.checkers.generic_engines.compare_checkers_with_other_games
      games.checkers.generic_engines.create_generic_checkers_config_from_example
      games.checkers.generic_engines.create_generic_checkers_engines
      games.checkers.generic_engines.create_generic_checkers_engines_simple
      games.checkers.generic_engines.create_multi_game_checkers_demo

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CheckersPromptGenerator(players: GamePlayerIdentifiers[PlayerType, PlayerType2])

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Checkers-specific prompt generator using the generic system.


            .. py:method:: create_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create a Checkers analysis prompt for the specified player.

               :param player: Player color ("red" or "black")

               :returns: Prompt template for position analysis
               :rtype: ChatPromptTemplate



            .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create a Checkers move prompt for the specified player.

               :param player: Player color ("red" or "black")

               :returns: Prompt template for move generation
               :rtype: ChatPromptTemplate



            .. py:method:: get_analysis_output_model() -> type

               Get the structured output model for Checkers analysis.



            .. py:method:: get_move_output_model() -> type

               Get the structured output model for Checkers moves.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: compare_checkers_with_other_games() -> None

            Compare the checkers pattern with other games to show generalization.

            This function demonstrates how the same generic system works for different games
            with different player naming conventions.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_checkers_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Checkers engines from predefined examples using generics.

            :param example_name: Name of the example configuration
            :param temperature: Temperature for all engines

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]

            Available examples:
                - "gpt_vs_claude": GPT-4 vs Claude
                - "gpt_only": GPT-4 for both players
                - "claude_only": Claude for both players
                - "budget": Cost-effective models
                - "mixed": Different provider per role
                - "checkers_masters": High-powered models for competitive play




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_checkers_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Checkers engines using the generic system.

            :param player_configs: Dictionary of role name to player configuration

            :returns: Dictionary of configured engines
            :rtype: dict[str, AugLLMConfig]

            .. rubric:: Example

            >>> configs = {
            ...     "red_player": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
            ...     "red_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
            ... }
            >>> engines = create_generic_checkers_engines(configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_checkers_engines_simple(red_model: str | haive.games.models.llm.LLMConfig = 'gpt-4o', black_model: str | haive.games.models.llm.LLMConfig = 'claude-3-5-sonnet-20240620', temperature: float = 0.3, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Checkers engines with simple model configurations using generics.

            :param red_model: Model for red player and analyzer
            :param black_model: Model for black player and analyzer
            :param temperature: Temperature for player engines
            :param \*\*kwargs: Additional configuration parameters

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]

            .. rubric:: Example

            >>> engines = create_generic_checkers_engines_simple("gpt-4", "claude-3-opus")
            >>> engines = create_generic_checkers_engines_simple(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     temperature=0.5
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_multi_game_checkers_demo() -> Any

            Create engines for multiple games including checkers.

            This demonstrates how the same configuration approach works across different games
            with the generic system.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: checkers_engine_factory


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: checkers_players


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: checkers_prompt_generator




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.checkers.generic_engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

