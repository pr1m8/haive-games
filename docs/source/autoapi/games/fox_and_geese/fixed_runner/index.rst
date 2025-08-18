games.fox_and_geese.fixed_runner
================================

.. py:module:: games.fox_and_geese.fixed_runner

Fixed runner for Fox and Geese game without LangGraph streaming issues.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Fixed runner for Fox and Geese game without LangGraph streaming issues.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.fox_and_geese.fixed_runner.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.fox_and_geese.fixed_runner.FixedFoxAndGeeseAgent

            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.fox_and_geese.fixed_runner.main
      games.fox_and_geese.fixed_runner.parse_arguments

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FixedFoxAndGeeseAgent(config: haive.games.fox_and_geese.config.FoxAndGeeseConfig = FoxAndGeeseConfig())

            Bases: :py:obj:`haive.games.fox_and_geese.agent.FoxAndGeeseAgent`


            Fixed Fox and Geese agent that handles state directly.

            Initialize the Fox and Geese agent.

            :param config: The configuration for the Fox and Geese game.
            :type config: FoxAndGeeseConfig


            .. py:method:: run_fixed_game(delay: float = 1.0, max_moves: int = 100) -> haive.games.fox_and_geese.state.FoxAndGeeseState

               Run the Fox and Geese game step by step, managing state directly.

               This bypasses LangGraph's stream method, which can have issues with certain state types.

               :param delay: Time delay between moves for better visualization
               :param max_moves: Maximum number of moves before forcing a draw

               :returns: Final game state




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run the Fox and Geese game with the fixed runner.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: parse_arguments()

            Parse command line arguments.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.fox_and_geese.fixed_runner import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

