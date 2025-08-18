games.mancala.config
====================

.. py:module:: games.mancala.config

Configuration for the Mancala game agent.

This module defines the configuration for the Mancala game agent, which includes the
game name, state schema, engine configurations, enable_analysis, visualize, and
stones_per_pit.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Configuration for the Mancala game agent.

   This module defines the configuration for the Mancala game agent, which includes the
   game name, state schema, engine configurations, enable_analysis, visualize, and
   stones_per_pit.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mancala.config.MancalaConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MancalaConfig

            Bases: :py:obj:`haive.games.framework.base.config.GameConfig`


            Configuration for the Mancala game agent.

            This class defines the configuration for the Mancala game agent, which includes the
            game name, state schema, engine configurations, enable_analysis, visualize, and
            stones_per_pit.



            .. py:method:: default_config()
               :classmethod:


               Create a default configuration.

               :returns: Default configuration for the Mancala game.
               :rtype: MancalaConfig



            .. py:attribute:: enable_analysis
               :type:  bool
               :value: None



            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.mancala.state.MancalaState]
               :value: None



            .. py:attribute:: stones_per_pit
               :type:  int
               :value: None



            .. py:attribute:: visualize
               :type:  bool
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mancala.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

