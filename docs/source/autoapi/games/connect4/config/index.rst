games.connect4.config
=====================

.. py:module:: games.connect4.config

.. autoapi-nested-parse::

   Connect4 agent configuration module.

   This module provides configuration classes for the Connect4 game agent, including:
       - Base configuration for Connect4 agents
       - LLM configuration for players and analyzers
       - Game settings and visualization options

   .. rubric:: Example

   >>> from haive.games.connect4 import Connect4AgentConfig
   >>>
   >>> # Create a config with analysis enabled
   >>> config = Connect4AgentConfig(
   ...     enable_analysis=True,
   ...     should_visualize_graph=True,
   ...     max_moves=42  # Maximum possible moves in Connect4
   ... )


   .. autolink-examples:: games.connect4.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.connect4.config.Connect4AgentConfig


Module Contents
---------------

.. py:class:: Connect4AgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration class for Connect4 game agents.

   This class defines the configuration parameters for Connect4 agents, including:
       - Game settings (max moves, analysis options)
       - LLM configurations for players and analyzers
       - Visualization settings

   .. attribute:: enable_analysis

      Whether to enable position analysis.

      :type: bool

   .. attribute:: should_visualize_graph

      Whether to visualize the game workflow graph.

      :type: bool

   .. attribute:: max_moves

      Maximum number of moves before forcing a draw.

      :type: int

   .. attribute:: aug_llm_configs

      LLM configurations for players and analyzers.

      :type: Dict[str, AugLLMConfig]

   .. rubric:: Example

   >>> config = Connect4AgentConfig(
   ...     enable_analysis=True,
   ...     should_visualize_graph=True,
   ...     max_moves=42,
   ...     aug_llm_configs={
   ...         "red_player": red_player_config,
   ...         "yellow_player": yellow_player_config,
   ...         "red_analyzer": red_analyzer_config,
   ...         "yellow_analyzer": yellow_analyzer_config,
   ...     }
   ... )


   .. autolink-examples:: Connect4AgentConfig
      :collapse:

   .. py:class:: Config

      Pydantic configuration class.

      This inner class configures Pydantic behavior for the Connect4AgentConfig.



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



   .. py:attribute:: max_moves
      :type:  int
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type[pydantic.BaseModel]
      :value: None



