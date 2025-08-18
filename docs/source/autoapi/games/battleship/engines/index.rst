games.battleship.engines
========================

.. py:module:: games.battleship.engines

Battleship game engine configurations.

This module provides engine configurations for the Battleship game, including:
    - Player decision engines
    - Ship placement engines
    - Analysis engines



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 functions</span>   </div>

.. autoapi-nested-parse::

   Battleship game engine configurations.

   This module provides engine configurations for the Battleship game, including:
       - Player decision engines
       - Ship placement engines
       - Analysis engines



      
            
            
            

.. admonition:: Functions (1)
   :class: info

   .. autoapisummary::

      games.battleship.engines.build_battleship_engines

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: build_battleship_engines() -> dict[str, haive.core.engine.aug_llm.AugLLMConfig]

            Build engine configurations for the Battleship game.

            This function creates AugLLMConfig objects for:
                - Player 1 ship placement
                - Player 2 ship placement
                - Player 1 move selection
                - Player 2 move selection
                - Player 1 analysis
                - Player 2 analysis

            :returns: Dictionary of engine configurations
            :rtype: Dict[str, AugLLMConfig]





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.engines import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

