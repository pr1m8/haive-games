games.go.config
===============

.. py:module:: games.go.config

.. autoapi-nested-parse::

   Go game configuration module.


   .. autolink-examples:: games.go.config
      :collapse:


Classes
-------

.. autoapisummary::

   games.go.config.GoAgentConfig


Module Contents
---------------

.. py:class:: GoAgentConfig

   Bases: :py:obj:`haive.core.engine.agent.agent.AgentConfig`


   Configuration for the Go game agent.

   This class defines the configuration settings for a Go game agent,
   including state management, LLM configurations, visualization options,
   and analysis settings.

   .. attribute:: state_schema

      Schema class for game state (default: GoGameState).

      :type: type

   .. attribute:: engines

      LLM configurations for
      players and analysis.

      :type: Dict[str, AugLLMConfig]

   .. attribute:: should_visualize_graph

      Whether to generate a visualization
      of the game graph (default: True).

      :type: bool

   .. attribute:: graph_name

      Filename for the graph visualization
      (default: "go_game.png").

      :type: str

   .. attribute:: include_analysis

      Whether to include position analysis
      during the game (default: True).

      :type: bool

   .. rubric:: Example

   >>> config = GoAgentConfig(
   ...     include_analysis=True,
   ...     engines={
   ...         "black_player": AugLLMConfig(...),
   ...         "white_player": AugLLMConfig(...),
   ...         "analyzer": AugLLMConfig(...)
   ...     }
   ... )


   .. autolink-examples:: GoAgentConfig
      :collapse:

   .. py:attribute:: engines
      :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
      :value: None



   .. py:attribute:: graph_name
      :type:  str
      :value: None



   .. py:attribute:: include_analysis
      :type:  bool
      :value: None



   .. py:attribute:: should_visualize_graph
      :type:  bool
      :value: None



   .. py:attribute:: state_schema
      :type:  type
      :value: None



