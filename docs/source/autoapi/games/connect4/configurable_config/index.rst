games.connect4.configurable_config
==================================

.. py:module:: games.connect4.configurable_config

.. autoapi-nested-parse::

   Configurable Connect4 agent configuration using player agents.

   from typing import Any This module provides a Connect4 configuration that supports
   configurable player agents instead of hardcoded engine configurations.


   .. autolink-examples:: games.connect4.configurable_config
      :collapse:


Attributes
----------

.. autoapisummary::

   games.connect4.configurable_config.Connect4ConfigV2


Classes
-------

.. autoapisummary::

   games.connect4.configurable_config.ConfigurableConnect4Config


Functions
---------

.. autoapisummary::

   games.connect4.configurable_config.create_connect4_config
   games.connect4.configurable_config.create_connect4_config_from_example
   games.connect4.configurable_config.create_connect4_config_from_player_configs


Module Contents
---------------

.. py:class:: ConfigurableConnect4Config

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configurable Connect4 agent configuration.

   This configuration supports using different LLM configurations for
   different players without hardcoding them in engines.

   .. rubric:: Examples

   >>> # Simple string-based configuration
   >>> config = ConfigurableConnect4Config(
   ...     red_model="gpt-4",
   ...     yellow_model="claude-3-opus"
   ... )

   >>> # Using player agent configs
   >>> config = ConfigurableConnect4Config(
   ...     player_configs={
   ...         "red_player": PlayerAgentConfig(llm_config="gpt-4"),
   ...         "yellow_player": PlayerAgentConfig(llm_config="claude-3-opus"),
   ...     }
   ... )

   >>> # Using example configuration
   >>> config = ConfigurableConnect4Config(
   ...     example_config="gpt_vs_claude"
   ... )


   .. autolink-examples:: ConfigurableConnect4Config
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


   .. py:method:: _update_player_names_from_models(red_model: str, yellow_model: str)

      Update player names from model strings.


      .. autolink-examples:: _update_player_names_from_models
         :collapse:


   .. py:method:: configure_engines_and_names() -> Any

      Configure engines from the provided player configurations.


      .. autolink-examples:: configure_engines_and_names
         :collapse:


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



   .. py:attribute:: red_model
      :type:  str | None
      :value: None



   .. py:attribute:: red_player_name
      :type:  str
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



   .. py:attribute:: temperature
      :type:  float | None
      :value: None



   .. py:attribute:: yellow_model
      :type:  str | None
      :value: None



   .. py:attribute:: yellow_player_name
      :type:  str
      :value: None



.. py:function:: create_connect4_config(red_model: str = 'gpt-4o', yellow_model: str = 'claude-3-5-sonnet-20240620', temperature: float = 0.7, enable_analysis: bool = False, **kwargs) -> ConfigurableConnect4Config

   Create a Connect4 configuration with simple model strings.

   :param red_model: Model for red player
   :param yellow_model: Model for yellow player
   :param temperature: Temperature for all engines
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Connect4 agent
   :rtype: ConfigurableConnect4Config

   .. rubric:: Example

   >>> config = create_connect4_config("gpt-4", "claude-3-opus", temperature=0.8)


   .. autolink-examples:: create_connect4_config
      :collapse:

.. py:function:: create_connect4_config_from_example(example_name: str, enable_analysis: bool = False, **kwargs) -> ConfigurableConnect4Config

   Create a Connect4 configuration from an example.

   :param example_name: Name of the example configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Connect4 agent
   :rtype: ConfigurableConnect4Config

   Available examples: gpt_vs_claude, gpt_only, claude_only, budget, mixed

   .. rubric:: Example

   >>> config = create_connect4_config_from_example("budget")


   .. autolink-examples:: create_connect4_config_from_example
      :collapse:

.. py:function:: create_connect4_config_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], enable_analysis: bool = False, **kwargs) -> ConfigurableConnect4Config

   Create a Connect4 configuration from player agent configurations.

   :param player_configs: Dictionary of role to player configuration
   :param enable_analysis: Whether to enable position analysis
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured Connect4 agent
   :rtype: ConfigurableConnect4Config

   .. rubric:: Example

   >>> configs = {
   ...     "red_player": create_player_config("gpt-4", player_name="Red Master"),
   ...     "yellow_player": create_player_config("claude-3-opus", player_name="Yellow Pro"),
   ... }
   >>> config = create_connect4_config_from_player_configs(configs)


   .. autolink-examples:: create_connect4_config_from_player_configs
      :collapse:

.. py:data:: Connect4ConfigV2

