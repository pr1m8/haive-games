games.checkers.generic_engines
==============================

.. py:module:: games.checkers.generic_engines

.. autoapi-nested-parse::

   Generic Checkers engines using the new generic player agent system.

   from typing import Any This module demonstrates how to use the generic player agent
   system for Checkers, showing the same pattern working across different games with
   different player identifiers.


   .. autolink-examples:: games.checkers.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.checkers.generic_engines.checkers_engine_factory
   games.checkers.generic_engines.checkers_players
   games.checkers.generic_engines.checkers_prompt_generator


Classes
-------

.. autoapisummary::

   games.checkers.generic_engines.CheckersPromptGenerator


Functions
---------

.. autoapisummary::

   games.checkers.generic_engines.compare_checkers_with_other_games
   games.checkers.generic_engines.create_generic_checkers_config_from_example
   games.checkers.generic_engines.create_generic_checkers_engines
   games.checkers.generic_engines.create_generic_checkers_engines_simple
   games.checkers.generic_engines.create_multi_game_checkers_demo


Module Contents
---------------

.. py:class:: CheckersPromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Checkers-specific prompt generator using the generic system.


   .. autolink-examples:: CheckersPromptGenerator
      :collapse:

   .. py:method:: create_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create a Checkers analysis prompt for the specified player.

      :param player: Player color ("red" or "black")

      :returns: Prompt template for position analysis
      :rtype: ChatPromptTemplate


      .. autolink-examples:: create_analysis_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create a Checkers move prompt for the specified player.

      :param player: Player color ("red" or "black")

      :returns: Prompt template for move generation
      :rtype: ChatPromptTemplate


      .. autolink-examples:: create_move_prompt
         :collapse:


   .. py:method:: get_analysis_output_model() -> type

      Get the structured output model for Checkers analysis.


      .. autolink-examples:: get_analysis_output_model
         :collapse:


   .. py:method:: get_move_output_model() -> type

      Get the structured output model for Checkers moves.


      .. autolink-examples:: get_move_output_model
         :collapse:


.. py:function:: compare_checkers_with_other_games() -> None

   Compare the checkers pattern with other games to show generalization.

   This function demonstrates how the same generic system works for different games
   with different player naming conventions.



   .. autolink-examples:: compare_checkers_with_other_games
      :collapse:

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



   .. autolink-examples:: create_generic_checkers_config_from_example
      :collapse:

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


   .. autolink-examples:: create_generic_checkers_engines
      :collapse:

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


   .. autolink-examples:: create_generic_checkers_engines_simple
      :collapse:

.. py:function:: create_multi_game_checkers_demo() -> Any

   Create engines for multiple games including checkers.

   This demonstrates how the same configuration approach works across different games
   with the generic system.



   .. autolink-examples:: create_multi_game_checkers_demo
      :collapse:

.. py:data:: checkers_engine_factory

.. py:data:: checkers_players

.. py:data:: checkers_prompt_generator

