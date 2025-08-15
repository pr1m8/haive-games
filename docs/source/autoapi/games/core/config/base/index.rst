games.core.config.base
======================

.. py:module:: games.core.config.base

.. autoapi-nested-parse::

   Base configuration classes for configurable games.

   from typing import Any This module provides the foundation for creating flexible game
   configurations that support multiple LLM providers and configuration modes.


   .. autolink-examples:: games.core.config.base
      :collapse:


Classes
-------

.. autoapisummary::

   games.core.config.base.BaseGameConfig
   games.core.config.base.ConfigMode
   games.core.config.base.GamePlayerRole


Functions
---------

.. autoapisummary::

   games.core.config.base.create_advanced_config
   games.core.config.base.create_example_config
   games.core.config.base.create_llm_config
   games.core.config.base.create_simple_config


Module Contents
---------------

.. py:class:: BaseGameConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`, :py:obj:`abc.ABC`


   Base configuration for all configurable games.

   This class provides a unified configuration system that supports:
   - Legacy hardcoded engines (backward compatibility)
   - Simple model string configuration
   - Example-based configuration
   - Advanced PlayerAgentConfig configuration

   Games should extend this class and implement the required abstract methods.



   .. autolink-examples:: BaseGameConfig
      :collapse:

   .. py:method:: build_legacy_engines() -> list[Any]
      :abstractmethod:


      Build legacy hardcoded engines for backward compatibility.

      :returns: List of game engines using hardcoded LLM configurations


      .. autolink-examples:: build_legacy_engines
         :collapse:


   .. py:method:: configure_engines() -> BaseGameConfig

      Configure engines based on the determined mode.


      .. autolink-examples:: configure_engines
         :collapse:


   .. py:method:: create_engines_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> list[Any]
      :abstractmethod:


      Create engines from detailed player configurations.

      :param player_configs: Dictionary mapping role names to PlayerAgentConfig

      :returns: List of configured game engines


      .. autolink-examples:: create_engines_from_player_configs
         :collapse:


   .. py:method:: create_example_player_configs(example_name: str) -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

      Create player configs from example configuration.


      .. autolink-examples:: create_example_player_configs
         :collapse:


   .. py:method:: create_simple_player_configs() -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

      Create player configs from simple model strings.

      This method should be overridden by games that use different field names (e.g.,
      white_model/black_model instead of player1_model/player2_model).



      .. autolink-examples:: create_simple_player_configs
         :collapse:


   .. py:method:: determine_config_mode() -> ConfigMode

      Automatically determine configuration mode based on provided fields.


      .. autolink-examples:: determine_config_mode
         :collapse:


   .. py:method:: get_example_configs() -> dict[str, dict[str, Any]]
      :abstractmethod:


      Define available example configurations.

      :returns: Dictionary mapping example names to configuration parameters

      .. rubric:: Example

      {
          "gpt_vs_claude": {
              "player1_model": "gpt-4",
              "player2_model": "claude-3-opus",
              "temperature": 0.7
          },
          "budget": {
              "player1_model": "gpt-3.5-turbo",
              "player2_model": "gpt-3.5-turbo",
              "temperature": 0.5
          }
      }


      .. autolink-examples:: get_example_configs
         :collapse:


   .. py:method:: get_player_names() -> dict[str, str]

      Get display names for all players.


      .. autolink-examples:: get_player_names
         :collapse:


   .. py:method:: get_role_definitions() -> dict[str, GamePlayerRole]
      :abstractmethod:


      Define the player roles for this game.

      :returns: Dictionary mapping role names to GamePlayerRole definitions

      .. rubric:: Example

      {
          "white_player": GamePlayerRole(name="white_player", display_name="White"),
          "black_player": GamePlayerRole(name="black_player", display_name="Black"),
          "white_analyzer": GamePlayerRole(name="white_analyzer", display_name="White Analyst", is_analyzer=True),
          "black_analyzer": GamePlayerRole(name="black_analyzer", display_name="Black Analyst", is_analyzer=True),
      }


      .. autolink-examples:: get_role_definitions
         :collapse:


   .. py:attribute:: config_mode
      :type:  ConfigMode
      :value: None



   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: example_config
      :type:  str | None
      :value: None



   .. py:attribute:: player1_model
      :type:  str | None
      :value: None



   .. py:attribute:: player2_model
      :type:  str | None
      :value: None



   .. py:attribute:: player_configs
      :type:  dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig] | None
      :value: None



   .. py:attribute:: recursion_limit
      :type:  int
      :value: None



   .. py:attribute:: temperature
      :type:  float
      :value: None



   .. py:attribute:: use_legacy_engines
      :type:  bool
      :value: None



.. py:class:: ConfigMode

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Configuration mode for game setup.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ConfigMode
      :collapse:

   .. py:attribute:: ADVANCED
      :value: 'advanced'



   .. py:attribute:: AUTO
      :value: 'auto'



   .. py:attribute:: EXAMPLE
      :value: 'example'



   .. py:attribute:: LEGACY
      :value: 'legacy'



   .. py:attribute:: SIMPLE
      :value: 'simple'



.. py:class:: GamePlayerRole(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Definition of a player role in a game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePlayerRole
      :collapse:

   .. py:attribute:: default_model
      :type:  str
      :value: None



   .. py:attribute:: display_name
      :type:  str
      :value: None



   .. py:attribute:: is_analyzer
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



.. py:function:: create_advanced_config(config_class: type[BaseGameConfig], player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> BaseGameConfig

   Create a game configuration with detailed player configs.

   :param config_class: The game's configuration class
   :param player_configs: Dictionary mapping role names to PlayerAgentConfig
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured game instance


   .. autolink-examples:: create_advanced_config
      :collapse:

.. py:function:: create_example_config(config_class: type[BaseGameConfig], example_name: str, **kwargs) -> BaseGameConfig

   Create a game configuration from a predefined example.

   :param config_class: The game's configuration class
   :param example_name: Name of the example configuration
   :param \*\*kwargs: Additional configuration parameters to override

   :returns: Configured game instance


   .. autolink-examples:: create_example_config
      :collapse:

.. py:function:: create_llm_config(model: str, **kwargs)

   Placeholder function until core factory is available.


   .. autolink-examples:: create_llm_config
      :collapse:

.. py:function:: create_simple_config(config_class: type[BaseGameConfig], player1_model: str, player2_model: str, **kwargs) -> BaseGameConfig

   Create a simple game configuration with model strings.

   :param config_class: The game's configuration class
   :param player1_model: Model for player 1
   :param player2_model: Model for player 2
   :param \*\*kwargs: Additional configuration parameters

   :returns: Configured game instance


   .. autolink-examples:: create_simple_config
      :collapse:

