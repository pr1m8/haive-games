games.chess.configurable_config
===============================

.. py:module:: games.chess.configurable_config

.. autoapi-nested-parse::

   Configurable chess agent configuration using player agents.

   This module provides a chess configuration that supports configurable player agents
   instead of hardcoded engine configurations.


   .. autolink-examples:: games.chess.configurable_config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.chess.configurable_config.ChessConfigV2


Classes
-------

.. autoapisummary::

   games.chess.configurable_config.ConfigurableChessConfig


Functions
---------

.. autoapisummary::

   games.chess.configurable_config.create_chess_config
   games.chess.configurable_config.create_chess_config_from_example
   games.chess.configurable_config.create_chess_config_from_player_configs


Module Contents
---------------

.. py:class:: ConfigurableChessConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configurable chess agent configuration.

   This configuration supports using different LLM configurations for
   different players without hardcoding them in engines.

   .. rubric:: Examples

   >>> # Simple string-based configuration
   >>> config = ConfigurableChessConfig(
   ...     white_model="gpt-4",
   ...     black_model="claude-3-opus"
   ... )

   >>> # Using player agent configs
   >>> config = ConfigurableChessConfig(
   ...     player_configs={
   ...         "white_player": PlayerAgentConfig(llm_config="gpt-4"),
   ...         "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
   ...     }
   ... )

   >>> # Using example configuration
   >>> config = ConfigurableChessConfig(
   ...     example_config="anthropic_vs_openai"
   ... )


   .. autolink-examples:: ConfigurableChessConfig
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: _extract_model_name(model_string: str) -> str

      Extract a friendly model name from a model string.


      .. autolink-examples:: _extract_model_name
         :collapse:


   .. py:method:: _get_player_name_from_config(llm_config: haive.core.models.llm.LLMConfig, color: str) -> str

      Extract player name from LLM config.


      .. autolink-examples:: _get_player_name_from_config
         :collapse:


   .. py:method:: _update_player_names_from_configs()

      Update player names from player agent configurations.


      .. autolink-examples:: _update_player_names_from_configs
         :collapse:


   .. py:method:: _update_player_names_from_engines()

      Update player names based on engine configurations.


      .. autolink-examples:: _update_player_names_from_engines
         :collapse:


   .. py:method:: _update_player_names_from_models(white_model: str, black_model: str)

      Update player names from model strings.


      .. autolink-examples:: _update_player_names_from_models
         :collapse:


   .. py:method:: configure_engines_and_names() -> Any

      Configure engines from the provided player configurations.


      .. autolink-examples:: configure_engines_and_names
         :collapse:


   .. py:attribute:: black_model
      :type:  str | None
      :value: None



   .. py:attribute:: black_player_name
      :type:  str
      :value: None



   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: example_config
      :type:  str | None
      :value: None



   .. py:attribute:: max_moves
      :type:  int
      :value: None



   .. py:attribute:: player_configs
      :type:  dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig] | None
      :value: None



   .. py:attribute:: runnable_config
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.chess.state.ChessState]
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



   .. py:attribute:: white_model
      :type:  str | None
      :value: None



   .. py:attribute:: white_player_name
      :type:  str
      :value: None



.. py:function:: create_chess_config(white_model: str = 'gpt-4o', black_model: str = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, enable_analysis: bool = True, **kwargs) -> ConfigurableChessConfig

   Create a chess configuration with simple model strings.

   :param white_model: Model for white player
   :param black_model: Model for black player
   :param temperature: Temperature for all engines
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured chess agent
   :rtype: ConfigurableChessConfig

   .. rubric:: Example

   >>> config = create_chess_config("gpt-4", "claude-3-opus", temperature=0.8)


   .. autolink-examples:: create_chess_config
      :collapse:

.. py:function:: create_chess_config_from_example(example_name: str, enable_analysis: bool = True, **kwargs) -> ConfigurableChessConfig

   Create a chess configuration from an example.

   :param example_name: Name of the example configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured chess agent
   :rtype: ConfigurableChessConfig

   Available examples: anthropic_vs_openai, gpt4_only, claude_only,
                      mixed_providers, budget_friendly

   .. rubric:: Example

   >>> config = create_chess_config_from_example("budget_friendly")


   .. autolink-examples:: create_chess_config_from_example
      :collapse:

.. py:function:: create_chess_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], enable_analysis: bool = True, **kwargs) -> ConfigurableChessConfig

   Create a chess configuration from player agent configurations.

   :param player_configs: Dictionary of role to player configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured chess agent
   :rtype: ConfigurableChessConfig

   .. rubric:: Example

   >>> configs = {
   ...     "white_player": create_player_config("gpt-4", player_name="Deep Blue"),
   ...     "black_player": create_player_config("claude-3-opus", player_name="AlphaZero"),
   ... }
   >>> config = create_chess_config_from_player_configs(configs)


   .. autolink-examples:: create_chess_config_from_player_configs
      :collapse:

.. py:data:: ChessConfigV2

