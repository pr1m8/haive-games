games.go.config
===============

.. py:module:: games.go.config

Go game configuration module.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Go game configuration module.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.go.config.GoAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.go.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

