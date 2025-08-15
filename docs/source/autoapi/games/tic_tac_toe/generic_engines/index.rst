games.tic_tac_toe.generic_engines
=================================

.. py:module:: games.tic_tac_toe.generic_engines

.. autoapi-nested-parse::

   Generic Tic Tac Toe engines using the new generic player agent system.

   This module demonstrates how to use the generic player agent system for Tic Tac Toe,
   showing the same pattern working across different games with different player
   identifiers.


   .. autolink-examples:: games.tic_tac_toe.generic_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.tic_tac_toe.generic_engines.ttt_engine_factory
   games.tic_tac_toe.generic_engines.ttt_players
   games.tic_tac_toe.generic_engines.ttt_prompt_generator


Classes
-------

.. autoapisummary::

   games.tic_tac_toe.generic_engines.TicTacToePromptGenerator


Functions
---------

.. autoapisummary::

   games.tic_tac_toe.generic_engines.compare_chess_vs_ttt_patterns
   games.tic_tac_toe.generic_engines.create_generic_ttt_config_from_example
   games.tic_tac_toe.generic_engines.create_generic_ttt_engines
   games.tic_tac_toe.generic_engines.create_generic_ttt_engines_simple
   games.tic_tac_toe.generic_engines.create_multi_game_comparison


Module Contents
---------------

.. py:class:: TicTacToePromptGenerator

   Bases: :py:obj:`haive.games.core.agent.generic_player_agent.GenericPromptGenerator`\ [\ :py:obj:`str`\ , :py:obj:`str`\ ]


   Tic Tac Toe-specific prompt generator using the generic system.


   .. autolink-examples:: TicTacToePromptGenerator
      :collapse:

   .. py:method:: create_analysis_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create a Tic Tac Toe analysis prompt for the specified player.

      :param player: Player symbol ("X" or "O")

      :returns: Prompt template for position analysis
      :rtype: ChatPromptTemplate


      .. autolink-examples:: create_analysis_prompt
         :collapse:


   .. py:method:: create_move_prompt(player: str) -> langchain_core.prompts.ChatPromptTemplate

      Create a Tic Tac Toe move prompt for the specified player.

      :param player: Player symbol ("X" or "O")

      :returns: Prompt template for move generation
      :rtype: ChatPromptTemplate


      .. autolink-examples:: create_move_prompt
         :collapse:


   .. py:method:: get_analysis_output_model() -> type

      Get the structured output model for Tic Tac Toe analysis.


      .. autolink-examples:: get_analysis_output_model
         :collapse:


   .. py:method:: get_move_output_model() -> type

      Get the structured output model for Tic Tac Toe moves.


      .. autolink-examples:: get_move_output_model
         :collapse:


.. py:function:: compare_chess_vs_ttt_patterns()

   Compare the chess vs tic-tac-toe patterns to show generalization.

   This function demonstrates how the same generic system works for different games
   with different player naming conventions.



   .. autolink-examples:: compare_chess_vs_ttt_patterns
      :collapse:

.. py:function:: create_generic_ttt_config_from_example(example_name: str, temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Tic Tac Toe engines from predefined examples using generics.

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



   .. autolink-examples:: create_generic_ttt_config_from_example
      :collapse:

.. py:function:: create_generic_ttt_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Tic Tac Toe engines using the generic system.

   :param player_configs: Dictionary of role name to player configuration

   :returns: Dictionary of configured engines
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> configs = {
   ...     "X_player": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "O_player": PlayerAgentConfig(llm_config="claude-3-opus"),
   ...     "X_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "O_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
   ... }
   >>> engines = create_generic_ttt_engines(configs)


   .. autolink-examples:: create_generic_ttt_engines
      :collapse:

.. py:function:: create_generic_ttt_engines_simple(x_model: str | haive.core.models.llm.LLMConfig = 'gpt-4o', o_model: str | haive.core.models.llm.LLMConfig = 'claude-3-5-sonnet-20240620', temperature: float = 0.3, **kwargs) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Tic Tac Toe engines with simple model configurations using generics.

   :param x_model: Model for X player and analyzer
   :param o_model: Model for O player and analyzer
   :param temperature: Temperature for player engines
   :param \*\*kwargs: Additional configuration parameters

   :returns: Dictionary of engines
   :rtype: dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> engines = create_generic_ttt_engines_simple("gpt-4", "claude-3-opus")
   >>> engines = create_generic_ttt_engines_simple(
   ...     "openai:gpt-4o",
   ...     "anthropic:claude-3-5-sonnet-20240620",
   ...     temperature=0.5
   ... )


   .. autolink-examples:: create_generic_ttt_engines_simple
      :collapse:

.. py:function:: create_multi_game_comparison()

   Create engines for multiple games to show the pattern.

   This demonstrates how the same configuration approach works across different games
   with the generic system.



   .. autolink-examples:: create_multi_game_comparison
      :collapse:

.. py:data:: ttt_engine_factory

.. py:data:: ttt_players

.. py:data:: ttt_prompt_generator

