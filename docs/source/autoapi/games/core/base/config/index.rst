games.core.base.config
======================

.. py:module:: games.core.base.config

Module documentation for games.core.base.config


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.core.base.config.GameAgentConfig

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameAgentConfig

            Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`, :py:obj:`abc.ABC`


            Base configuration for game agents.


            .. py:attribute:: game
               :type:  type[Game]
               :value: None



            .. py:attribute:: state_schema
               :type:  type[haive.games.core.base.state.GameState]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.base.config import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

