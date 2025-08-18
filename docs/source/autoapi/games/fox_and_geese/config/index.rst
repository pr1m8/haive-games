games.fox_and_geese.config
==========================

.. py:module:: games.fox_and_geese.config

Configuration for the Fox and Geese game agent.

This module defines the configuration for the Fox and Geese game agent, which includes
the game name, state schema, AugLLM configurations, enable_analysis, visualize, and
max_turns.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration for the Fox and Geese game agent.

   This module defines the configuration for the Fox and Geese game agent, which includes
   the game name, state schema, AugLLM configurations, enable_analysis, visualize, and
   max_turns.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.fox_and_geese.config.FoxAndGeeseConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FoxAndGeeseConfig

            Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


            Configuration for the Fox and Geese game agent.

            This class defines the configuration for the Fox and Geese game agent, which
            includes the game name, state schema, AugLLM configurations, enable_analysis,
            visualize, recursion_limit and max_turns.



            .. py:method:: default_config()
               :classmethod:


               Create a default configuration.



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: input_schema
               :type:  type[haive.games.fox_and_geese.state.FoxAndGeeseState]
               :value: None



            .. py:attribute:: max_turns
               :type:  int
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: recursion_limit
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.fox_and_geese.state.FoxAndGeeseState]
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.fox_and_geese.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

