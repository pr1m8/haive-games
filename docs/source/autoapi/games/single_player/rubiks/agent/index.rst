games.single_player.rubiks.agent
================================

.. py:module:: games.single_player.rubiks.agent

.. autoapi-nested-parse::

   Rubik's Cube agent implementation.


   .. autolink-examples:: games.single_player.rubiks.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.single_player.rubiks.agent.logger


Classes
-------

.. autoapisummary::

   games.single_player.rubiks.agent.RubiksCubeAgent


Module Contents
---------------

.. py:class:: RubiksCubeAgent(config: haive.games.single_player.rubiks.config.RubiksCubeConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.single_player.rubiks.config.RubiksCubeConfig`\ ]


   Rubik's Cube game agent.

   Initialize the chess agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: RubiksCubeAgent
      :collapse:

   .. py:method:: check_solved(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

      Check if the cube is solved.


      .. autolink-examples:: check_solved
         :collapse:


   .. py:method:: game_over(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

      Handle game over.


      .. autolink-examples:: game_over
         :collapse:


   .. py:method:: handle_player_turn(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

      Handle player input.


      .. autolink-examples:: handle_player_turn
         :collapse:


   .. py:method:: process_move(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

      Process a cube move.


      .. autolink-examples:: process_move
         :collapse:


   .. py:method:: route_game_status(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> str

      Route based on game status.


      .. autolink-examples:: route_game_status
         :collapse:


   .. py:method:: route_player_action(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> str

      Route based on player action.


      .. autolink-examples:: route_player_action
         :collapse:


   .. py:method:: scramble_cube(state: haive.games.single_player.rubiks.state.RubiksCubeState) -> langgraph.types.Command

      Scramble the cube based on difficulty.


      .. autolink-examples:: scramble_cube
         :collapse:


   .. py:method:: setup_workflow()

      Set up the workflow graph.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:attribute:: engines


.. py:data:: logger

