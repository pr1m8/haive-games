games.chess.configurable_engines
================================

.. py:module:: games.chess.configurable_engines

.. autoapi-nested-parse::

   Configurable chess engines using the new player agent system.

   This module provides chess engine configurations that use configurable player agents
   instead of hardcoded LLM configurations, making it easy to switch LLMs for different
   players.


   .. autolink-examples:: games.chess.configurable_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.chess.configurable_engines.EXAMPLE_CONFIGS


Functions
---------

.. autoapisummary::

   games.chess.configurable_engines.create_anthropic_vs_openai_engines
   games.chess.configurable_engines.create_chess_analysis_prompt
   games.chess.configurable_engines.create_chess_move_prompt
   games.chess.configurable_engines.create_configurable_chess_engines
   games.chess.configurable_engines.create_mixed_provider_engines
   games.chess.configurable_engines.create_same_model_engines
   games.chess.configurable_engines.get_chess_role_definitions
   games.chess.configurable_engines.get_example_engines


Module Contents
---------------

.. py:function:: create_anthropic_vs_openai_engines(white_model: str = 'claude-3-5-sonnet-20240620', black_model: str = 'gpt-4o', temperature: float = 0.7) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create chess engines with Anthropic vs OpenAI models.

   :param white_model: Anthropic model for white player
   :param black_model: OpenAI model for black player
   :param temperature: Temperature for all engines

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_anthropic_vs_openai_engines
      :collapse:

.. py:function:: create_chess_analysis_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Create a chess analysis prompt for the specified color.

   :param color: Player color ("white" or "black")

   :returns: Prompt template for position analysis
   :rtype: ChatPromptTemplate


   .. autolink-examples:: create_chess_analysis_prompt
      :collapse:

.. py:function:: create_chess_move_prompt(color: str) -> langchain_core.prompts.ChatPromptTemplate

   Create a chess move prompt for the specified color.

   :param color: Player color ("white" or "black")

   :returns: Prompt template for move generation
   :rtype: ChatPromptTemplate


   .. autolink-examples:: create_chess_move_prompt
      :collapse:

.. py:function:: create_configurable_chess_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create chess engines from configurable player agents.

   :param player_configs: Dictionary of role name to player configuration

   :returns: Dictionary of configured engines
   :rtype: Dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> configs = {
   ...     "white_player": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
   ...     "white_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
   ... }
   >>> engines = create_configurable_chess_engines(configs)


   .. autolink-examples:: create_configurable_chess_engines
      :collapse:

.. py:function:: create_mixed_provider_engines(providers: dict[str, str] = None, temperature: float = 0.7) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create chess engines with different providers for each role.

   :param providers: Dictionary of role to model string
   :param temperature: Temperature for all engines

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_mixed_provider_engines
      :collapse:

.. py:function:: create_same_model_engines(model: str = 'gpt-4o', temperature: float = 0.7) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create chess engines using the same model for all roles.

   :param model: Model string to use for all roles
   :param temperature: Temperature for all engines

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_same_model_engines
      :collapse:

.. py:function:: get_chess_role_definitions() -> dict[str, haive.games.core.agent.player_agent.GamePlayerRole]

   Get role definitions for chess players and analyzers.

   :returns: Dictionary of role definitions
   :rtype: Dict[str, GamePlayerRole]


   .. autolink-examples:: get_chess_role_definitions
      :collapse:

.. py:function:: get_example_engines(config_name: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Get example engine configuration by name.

   :param config_name: Name of the configuration from EXAMPLE_CONFIGS

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]

   Available configs: anthropic_vs_openai, gpt4_only, claude_only,
                     mixed_providers, budget_friendly



   .. autolink-examples:: get_example_engines
      :collapse:

.. py:data:: EXAMPLE_CONFIGS

