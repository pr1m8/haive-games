games.connect4.generic_engines
==============================

.. py:module:: games.connect4.generic_engines

Generic Connect4 engines using the new generic player agent system.

This module demonstrates how to use the generic player agent system for Connect4,
showing the same pattern working with red/yellow player identifiers.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">3 functions</span> • <span class="module-stat">3 attributes</span>   </div>

.. autoapi-nested-parse::

   Generic Connect4 engines using the new generic player agent system.

   This module demonstrates how to use the generic player agent system for Connect4,
   showing the same pattern working with red/yellow player identifiers.



      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.connect4.generic_engines.connect4_engine_factory
      games.connect4.generic_engines.connect4_players
      games.connect4.generic_engines.connect4_prompt_generator

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.connect4.generic_engines.Connect4PromptGenerator

            

.. admonition:: Functions (3)
   :class: info

   .. autoapisummary::

      games.connect4.generic_engines.create_generic_connect4_config_from_example
      games.connect4.generic_engines.create_generic_connect4_engines
      games.connect4.generic_engines.create_generic_connect4_engines_simple

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Connect4PromptGenerator(players: GamePlayerIdentifiers[PlayerType, PlayerType2])

            Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


            Connect4-specific prompt generator using the generic system.


            .. py:method:: create_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create a Connect4 analysis prompt for the specified player.

               :param player: Player color ("red" or "yellow")

               :returns: Prompt template for position analysis
               :rtype: ChatPromptTemplate



            .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

               Create a Connect4 move prompt for the specified player.

               :param player: Player color ("red" or "yellow")

               :returns: Prompt template for move generation
               :rtype: ChatPromptTemplate



            .. py:method:: get_analysis_output_model() -> type

               Get the structured output model for Connect4 analysis.



            .. py:method:: get_move_output_model() -> type

               Get the structured output model for Connect4 moves.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_connect4_config_from_example(example_name: str, temperature: float = 0.7) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Connect4 engines from predefined examples using generics.

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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_connect4_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Connect4 engines using the generic system.

            :param player_configs: Dictionary of role name to player configuration

            :returns: Dictionary of configured engines
            :rtype: dict[str, AugLLMConfig]

            .. rubric:: Example

            >>> configs = {
            ...     "red_player": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "yellow_player": PlayerAgentConfig(llm_config="claude-3-opus"),
            ...     "red_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
            ...     "yellow_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
            ... }
            >>> engines = create_generic_connect4_engines(configs)



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_generic_connect4_engines_simple(red_model: str | haive.core.models.llm.LLMConfig = 'gpt-4o', yellow_model: str | haive.core.models.llm.LLMConfig = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Create Connect4 engines with simple model configurations using generics.

            :param red_model: Model for red player and analyzer
            :param yellow_model: Model for yellow player and analyzer
            :param temperature: Temperature for player engines
            :param \*\*kwargs: Additional configuration parameters

            :returns: Dictionary of engines
            :rtype: dict[str, AugLLMConfig]

            .. rubric:: Example

            >>> engines = create_generic_connect4_engines_simple("gpt-4", "claude-3-opus")
            >>> engines = create_generic_connect4_engines_simple(
            ...     "openai:gpt-4o",
            ...     "anthropic:claude-3-5-sonnet-20240620",
            ...     temperature=0.8
            ... )



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: connect4_engine_factory


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: connect4_players


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: connect4_prompt_generator




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.connect4.generic_engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

