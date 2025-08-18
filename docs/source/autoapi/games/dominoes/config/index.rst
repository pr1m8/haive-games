games.dominoes.config
=====================

.. py:module:: games.dominoes.config

Module documentation for games.dominoes.config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.dominoes.config.DominoesAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesAgentConfig

            Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


            Configuration for the dominoes agent.


            .. py:method:: default_config() -> Any
               :classmethod:



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: hand_size
               :type:  int
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.dominoes.state.DominoesState]
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.dominoes.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

