games.single_player.wordle.agent
================================

.. py:module:: games.single_player.wordle.agent

Module documentation for games.single_player.wordle.agent


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.wordle.agent.WordConnectionsAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsAgent(config: haive.games.framework.base.config.GameConfig)

            Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.single_player.wordle.config.WordConnectionsAgentConfig`\ ]


            Agent for playing the Word Connections game.

            Initialize the game agent.

            :param config: Configuration for the game agent.
                           Defaults to GameConfig().
            :type config: GameConfig, optional


            .. py:method:: initialize_game(puzzle_data: dict = None) -> haive.games.single_player.wordle.models.WordConnectionsState

               Initialize a new game.



            .. py:method:: play_turn(state: dict[str, Any]) -> dict[str, Any]

               Play one turn of the game.



            .. py:method:: setup_routing() -> None

               Set up the routing for the game.



            .. py:method:: setup_workflow() -> None

               Set up the game workflow using the graph_builder.



            .. py:method:: should_continue(state: dict[str, Any]) -> bool

               Check if game should continue.






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.wordle.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

