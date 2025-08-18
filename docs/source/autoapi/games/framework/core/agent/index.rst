games.framework.core.agent
==========================

.. py:module:: games.framework.core.agent

Module documentation for games.framework.core.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.agent.BasePlayerAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BasePlayerAgent(config: haive.core.engine.agent.config.AgentConfig)

            Bases: :py:obj:`haive.core.engine.agent.config.AgentConfig`


            Base configuration for an agent architecture.
            Extends InvokableEngine to provide a consistent interface with the Engine framework.

            This class is designed to NEVER include __runnable_config__ in any schemas.
            By default, it uses PostgreSQL for persistence if available.

            This implementation supports protocol validation to ensure that agent
            implementations conform to the expected interfaces.


            .. py:method:: setup_workflow()


            .. py:attribute:: engines
               :type:  dict[str, haive.core.engine.aug_llm.AugLLMConfig]


            .. py:attribute:: graph
               :type:  haive.core.graph.state_graph.base_graph2.BaseGraph | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

