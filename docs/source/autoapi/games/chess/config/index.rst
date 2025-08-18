games.chess.config
==================

.. py:module:: games.chess.config

Chess agent configuration module.

from typing import Any
This module provides configuration classes for chess agents, including:
    - Core game parameters
    - LLM engine settings
    - Analysis options
    - Visualization settings
    - State schema definition

The configuration system uses Pydantic for validation and default values,
making it easy to create and customize chess agent instances.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Chess agent configuration module.

   from typing import Any
   This module provides configuration classes for chess agents, including:
       - Core game parameters
       - LLM engine settings
       - Analysis options
       - Visualization settings
       - State schema definition

   The configuration system uses Pydantic for validation and default values,
   making it easy to create and customize chess agent instances.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.config.ChessConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessConfig

            Bases: :py:obj:`haive.games.core.config.BaseGameConfig`


            Configuration class for chess game agents.

            This class defines all configuration parameters for a chess agent,
            including state schema, LLM engines, game settings, and visualization
            options.

            .. attribute:: state_schema

               The state schema for the game.

               :type: Type[ChessState]

            .. attribute:: white_player_name

               Name of the white player.

               :type: str

            .. attribute:: black_player_name

               Name of the black player.

               :type: str

            .. attribute:: enable_analysis

               Whether to enable position analysis during gameplay.

               :type: bool

            .. attribute:: should_visualize_graph

               Whether to visualize the game workflow graph.

               :type: bool

            .. attribute:: max_moves

               Maximum number of moves before forcing a draw.

               :type: int

            .. attribute:: engines

               LLM configurations for players and analyzers.

               :type: Dict[str, AugLLMConfig]

            .. attribute:: runnable_config

               Runtime configuration for the agent.

               :type: Dict[str, Any]

            .. rubric:: Examples

            >>> # Create a basic configuration
            >>> config = ChessConfig()
            >>>
            >>> # Create a configuration with analysis disabled
            >>> config = ChessConfig(enable_analysis=False)
            >>>
            >>> # Create a configuration with custom LLM engines
            >>> from haive.core.engine.aug_llm import build_aug_llm
            >>> engines = {
            ...     "white_player": build_aug_llm("openai", "gpt-4"),
            ...     "black_player": build_aug_llm("anthropic", "claude-3-opus-20240229"),
            ... }
            >>> config = ChessConfig(engines=engines)


            .. py:class:: Config

               Pydantic configuration.

               This inner class configures Pydantic behavior for the ChessAgentConfig.

               .. attribute:: arbitrary_types_allowed

                  Whether to allow arbitrary types in the model.

                  :type: bool


               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: build_legacy_engines() -> list[Any]

               Build legacy hardcoded engines.



            .. py:method:: create_engines_from_player_configs(player_configs: dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]) -> list[Any]

               Create engines from player configurations.



            .. py:method:: create_simple_player_configs() -> dict[str, haive.games.core.agent.player_agent.PlayerAgentConfig]

               Create player configs from simple model strings.



            .. py:method:: finalize_config() -> ChessConfig

               Finalize configuration after engine setup.



            .. py:method:: get_example_configs() -> dict[str, dict[str, Any]]

               Define example chess configurations.



            .. py:method:: get_role_definitions() -> dict[str, haive.games.core.config.GamePlayerRole]

               Define chess player roles.



            .. py:attribute:: black_model
               :type:  str | None
               :value: None



            .. py:attribute:: black_player_name
               :type:  str | None
               :value: None



            .. py:attribute:: engines
               :type:  list[Any] | None
               :value: None



            .. py:attribute:: max_moves
               :type:  int
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: recursion_limit
               :type:  int
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



            .. py:attribute:: white_model
               :type:  str | None
               :value: None



            .. py:attribute:: white_player_name
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

