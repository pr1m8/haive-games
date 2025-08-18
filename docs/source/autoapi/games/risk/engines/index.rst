games.risk.engines
==================

.. py:module:: games.risk.engines

Risk game engines.

This module defines engine configurations for the Risk game, including state management,
analysis, and strategic planning.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Risk game engines.

   This module defines engine configurations for the Risk game, including state management,
   analysis, and strategic planning.



      
            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.risk.engines.risk_engines

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: risk_engines(config: haive.games.risk.config.RiskConfig | None = None) -> dict[str, Any]

            Create a set of engines for the Risk game.

            :param config: Optional configuration for the Risk game.
                           If not provided, default configuration will be used.

            :returns: A dictionary of engine configurations for the Risk game.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.risk.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

