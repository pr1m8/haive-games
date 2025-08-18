games.core.config.base
======================

.. py:module:: games.core.config.base

Base configuration classes for configurable games.

from typing import Any This module provides the foundation for creating flexible game
configurations that support multiple LLM providers and configuration modes.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span> • <span class="module-stat">4 functions</span>   </div>

.. autoapi-nested-parse::

   Base configuration classes for configurable games.

   from typing import Any This module provides the foundation for creating flexible game
   configurations that support multiple LLM providers and configuration modes.



      
            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.core.config.base.BaseGameConfig
      games.core.config.base.ConfigMode
      games.core.config.base.GamePlayerRole

            

.. admonition:: Functions (4)
   :class: info

   .. autoapisummary::

      games.core.config.base.create_advanced_config
      games.core.config.base.create_example_config
      games.core.config.base.create_llm_config
      games.core.config.base.create_simple_config

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BaseGameConfig

            Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`, :py:obj:`abc.ABC`


            Base configuration for all configurable games.

            This class provides a unified configuration system that supports:
            - Legacy hardcoded engines (backward compatibility)
            - Simple model string configuration
            - Example-based configuration
            - Advanced PlayerAgentConfig configuration

            Games should extend this class and implement the required abstract methods.



            .. py:method:: build_legacy_engines() -> list[Any]
               :abstractmethod:


               Build legacy hardcoded engines for backward compatibility.

               :returns: List of game engines using hardcoded LLM configurations



            .. py:method:: configure_engines() -> BaseGameConfig

               Configure engines based on the determined mode.



            .. py:method:: create_engines_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> list[Any]
               :abstractmethod:


               Create engines from detailed player configurations.

               :param player_configs: Dictionary mapping role names to PlayerAgentConfig

               :returns: List of configured game engines



            .. py:method:: create_example_player_configs(example_name: str) -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

               Create player configs from example configuration.



            .. py:method:: create_simple_player_configs() -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

               Create player configs from simple model strings.

               This method should be overridden by games that use different field names (e.g.,
               white_model/black_model instead of player1_model/player2_model).




            .. py:method:: determine_config_mode() -> ConfigMode

               Automatically determine configuration mode based on provided fields.



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



            .. py:method:: get_player_names() -> dict[str, str]

               Get display names for all players.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ConfigMode

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Configuration mode for game setup.

            Initialize self.  See help(type(self)) for accurate signature.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePlayerRole(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Definition of a player role in a game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_advanced_config(config_class: type[BaseGameConfig], player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig], **kwargs) -> BaseGameConfig

            Create a game configuration with detailed player configs.

            :param config_class: The game's configuration class
            :param player_configs: Dictionary mapping role names to PlayerAgentConfig
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured game instance



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_example_config(config_class: type[BaseGameConfig], example_name: str, **kwargs) -> BaseGameConfig

            Create a game configuration from a predefined example.

            :param config_class: The game's configuration class
            :param example_name: Name of the example configuration
            :param \*\*kwargs: Additional configuration parameters to override

            :returns: Configured game instance



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_llm_config(model: str, **kwargs)

            Placeholder function until core factory is available.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: create_simple_config(config_class: type[BaseGameConfig], player1_model: str, player2_model: str, **kwargs) -> BaseGameConfig

            Create a simple game configuration with model strings.

            :param config_class: The game's configuration class
            :param player1_model: Model for player 1
            :param player2_model: Model for player 2
            :param \*\*kwargs: Additional configuration parameters

            :returns: Configured game instance





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.config.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

