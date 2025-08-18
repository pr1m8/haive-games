games.nim.config
================

.. py:module:: games.nim.config

Configuration for the Nim game.

This module defines the configuration for the Nim game, which includes the state schema,
engines, enable_analysis, visualize, and pile_sizes.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration for the Nim game.

   This module defines the configuration for the Nim game, which includes the state schema,
   engines, enable_analysis, visualize, and pile_sizes.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.nim.config.NimConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimConfig

            Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


            Configuration for the Nim agent.

            .. attribute:: state_schema

               The state schema for the Nim game.

               :type: Type[NimState]

            .. attribute:: engines

               The engines for the Nim game.

               :type: Dict[str, AugLLMConfig]

            .. attribute:: enable_analysis

               Whether to enable analysis.

               :type: bool

            .. attribute:: visualize

               Whether to visualize the game.

               :type: bool


            .. py:method:: default_config()
               :classmethod:


               Create a default configuration.

               :returns: The default configuration.
               :rtype: NimConfig



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: misere_mode
               :type:  bool
               :value: None



            .. py:attribute:: pile_sizes
               :type:  list[int]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.nim.state.NimState]
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

