games.fox_and_geese.enhanced_example
====================================

.. py:module:: games.fox_and_geese.enhanced_example

Enhanced example runner for Fox and Geese game with Rich UI visualization.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Enhanced example runner for Fox and Geese game with Rich UI visualization.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.fox_and_geese.enhanced_example.parser

            
            
            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.fox_and_geese.enhanced_example.demo_ui_features
      games.fox_and_geese.enhanced_example.run_fox_and_geese_game

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: demo_ui_features(delay: float = 0.5)

            Demonstrate UI features with a sample game state.

            :param delay: Delay between demonstrations in seconds



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: run_fox_and_geese_game(agent: haive.games.fox_and_geese.agent.FoxAndGeeseAgent, delay: float = 1.5, use_rich_ui: bool = True)

            Run a Fox and Geese game with visualization.

            :param agent: Configured FoxAndGeeseAgent
            :param delay: Delay between moves in seconds
            :param use_rich_ui: Whether to use the enhanced Rich UI (vs. the basic UI)

            :returns: The final game state



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: parser




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.fox_and_geese.enhanced_example import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

