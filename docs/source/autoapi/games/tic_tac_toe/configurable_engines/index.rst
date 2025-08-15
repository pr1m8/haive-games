games.tic_tac_toe.configurable_engines
======================================

.. py:module:: games.tic_tac_toe.configurable_engines

.. autoapi-nested-parse::

   Configurable Tic Tac Toe engines using the new player agent system.

   This module provides Tic Tac Toe engine configurations that use configurable player
   agents instead of hardcoded LLM configurations.


   .. autolink-examples:: games.tic_tac_toe.configurable_engines
      :collapse:


Attributes
----------

.. autoapisummary::

   games.tic_tac_toe.configurable_engines.EXAMPLE_TTT_CONFIGS


Functions
---------

.. autoapisummary::

   games.tic_tac_toe.configurable_engines.create_configurable_tic_tac_toe_engines
   games.tic_tac_toe.configurable_engines.create_simple_tic_tac_toe_player_configs
   games.tic_tac_toe.configurable_engines.create_tic_tac_toe_analysis_prompt
   games.tic_tac_toe.configurable_engines.create_tic_tac_toe_engines_from_models
   games.tic_tac_toe.configurable_engines.create_tic_tac_toe_move_prompt
   games.tic_tac_toe.configurable_engines.get_example_tic_tac_toe_engines
   games.tic_tac_toe.configurable_engines.get_tic_tac_toe_role_definitions


Module Contents
---------------

.. py:function:: create_configurable_tic_tac_toe_engines(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Tic Tac Toe engines from configurable player agents.

   :param player_configs: Dictionary of role name to player configuration

   :returns: Dictionary of configured engines
   :rtype: Dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> configs = {
   ...     "X_player": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "O_player": PlayerAgentConfig(llm_config="claude-3-opus"),
   ...     "X_analyzer": PlayerAgentConfig(llm_config="gpt-4"),
   ...     "O_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
   ... }
   >>> engines = create_configurable_tic_tac_toe_engines(configs)


   .. autolink-examples:: create_configurable_tic_tac_toe_engines
      :collapse:

.. py:function:: create_simple_tic_tac_toe_player_configs(x_model: str = 'gpt-4o', o_model: str = 'claude-3-5-sonnet-20240620', temperature: float = 0.3) -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

   Create simple player configurations for Tic Tac Toe.

   :param x_model: Model for X player
   :param o_model: Model for O player
   :param temperature: Temperature for both players

   :returns: Player configurations
   :rtype: Dict[str, PlayerAgentConfig]


   .. autolink-examples:: create_simple_tic_tac_toe_player_configs
      :collapse:

.. py:function:: create_tic_tac_toe_analysis_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

   Create a Tic Tac Toe analysis prompt for the specified player.

   :param player_symbol: Player symbol ("X" or "O")

   :returns: Prompt template for position analysis
   :rtype: ChatPromptTemplate


   .. autolink-examples:: create_tic_tac_toe_analysis_prompt
      :collapse:

.. py:function:: create_tic_tac_toe_engines_from_models(x_model: str = 'gpt-4o', o_model: str = 'claude-3-5-sonnet-20240620', temperature: float = 0.3) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Create Tic Tac Toe engines using simple model strings.

   :param x_model: Model for X player and analyzer
   :param o_model: Model for O player and analyzer
   :param temperature: Temperature for all engines

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]


   .. autolink-examples:: create_tic_tac_toe_engines_from_models
      :collapse:

.. py:function:: create_tic_tac_toe_move_prompt(player_symbol: str) -> langchain_core.prompts.ChatPromptTemplate

   Create a Tic Tac Toe move prompt for the specified player.

   :param player_symbol: Player symbol ("X" or "O")

   :returns: Prompt template for move generation
   :rtype: ChatPromptTemplate


   .. autolink-examples:: create_tic_tac_toe_move_prompt
      :collapse:

.. py:function:: get_example_tic_tac_toe_engines(config_name: str) -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

   Get example Tic Tac Toe engine configuration by name.

   :param config_name: Name of the configuration from EXAMPLE_TTT_CONFIGS

   :returns: Dictionary of engines
   :rtype: Dict[str, AugLLMConfig]

   Available configs: gpt_vs_claude, gpt_only, claude_only, budget, mixed



   .. autolink-examples:: get_example_tic_tac_toe_engines
      :collapse:

.. py:function:: get_tic_tac_toe_role_definitions() -> dict[str, haive.games.core.agent.player_agent.GamePlayerRole]

   Get role definitions for Tic Tac Toe players and analyzers.

   :returns: Dictionary of role definitions
   :rtype: Dict[str, GamePlayerRole]


   .. autolink-examples:: get_tic_tac_toe_role_definitions
      :collapse:

.. py:data:: EXAMPLE_TTT_CONFIGS

