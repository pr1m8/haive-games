games.framework.base.config
===========================

.. py:module:: games.framework.base.config

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

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



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.base.config.GameConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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


            .. py:class:: Config

               Pydantic configuration.


               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: runnable_config
               :type:  langchain_core.runnables.RunnableConfig
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.framework.base.state.GameState]
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.base.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

