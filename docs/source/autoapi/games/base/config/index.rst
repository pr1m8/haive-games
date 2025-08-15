games.base.config
=================

.. py:module:: games.base.config

.. autoapi-nested-parse::

   Base configuration module for game agents.

   This module provides the foundational configuration class for game agents,
   defining common settings and parameters that all game agents need.

   .. rubric:: Example

   >>> config = GameConfig(
   ...     state_schema=ChessState,
   ...     engines={"player1": player1_engine},
   ...     enable_analysis=True
   ... )

   Typical usage:
       - Inherit from GameConfig to create game-specific configurations
       - Override default values to customize game behavior
       - Use as configuration for game agents


   .. autolink-examples:: games.base.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.base.config.GameConfig


Module Contents
---------------

.. py:class:: GameConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Base configuration for game agents.

   This class defines the core configuration parameters that all game agents
   need, including state schema, LLM engines, and analysis settings.

   .. attribute:: state_schema

      The state schema class for the game.

      :type: Type[GameState]

   .. attribute:: engines

      Configurations for game LLMs.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: enable_analysis

      Whether to enable move analysis.

      :type: bool

   .. attribute:: visualize

      Whether to visualize the game.

      :type: bool

   .. rubric:: Example

   >>> class ChessConfig(GameConfig):
   ...     state_schema: Type[GameState] = ChessState
   ...     engines: Dict[str, AugLLMConfig] = {
   ...         "player1": player1_engine,
   ...         "player2": player2_engine
   ...     }
   ...     enable_analysis: bool = True


   .. autolink-examples:: GameConfig
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: enable_analysis
      :type:  bool
      :value: None



   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: state_schema
      :type:  type[haive.games.framework.base.state.GameState]
      :value: None



   .. py:attribute:: visualize
      :type:  bool
      :value: None



