games.single_player.rubiks.agent
================================

.. py:module:: games.single_player.rubiks.agent

Rubik's Cube agent implementation.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Rubik's Cube agent implementation.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.single_player.rubiks.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.rubiks.agent.RubiksCubeAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RubiksCubeAgent(config: haive.games.single_player.rubiks.config.RubiksCubeConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.single_player.rubiks.config.RubiksCubeConfig`\ ]


            Rubik's Cube game agent.

            Initialize the chess agent.


            .. py:method:: check_solved(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

               Check if the cube is solved.



            .. py:method:: game_over(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

               Handle game over.



            .. py:method:: handle_player_turn(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

               Handle player input.



            .. py:method:: process_move(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

               Process a cube move.



            .. py:method:: route_game_status(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> str

               Route based on game status.



            .. py:method:: route_player_action(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> str

               Route based on player action.



            .. py:method:: scramble_cube(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

               Scramble the cube based on difficulty.



            .. py:method:: setup_workflow()

               Set up the workflow graph.



            .. py:attribute:: engines



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.rubiks.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

