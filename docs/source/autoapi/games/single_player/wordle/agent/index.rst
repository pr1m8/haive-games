games.single_player.wordle.agent
================================

.. py:module:: games.single_player.wordle.agent


Classes
-------

.. autoapisummary::

   games.single_player.wordle.agent.WordConnectionsAgent


Module Contents
---------------

.. py:class:: WordConnectionsAgent

   Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.single_player.wordle.config.WordConnectionsAgentConfig`\ ]


   Agent for playing the Word Connections game.


   .. autolink-examples:: WordConnectionsAgent
      :collapse:

   .. py:method:: initialize_game(puzzle_data: dict = None) -> haive.games.single_player.wordle.models.WordConnectionsState

      Initialize a new game.


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: play_turn(state: dict[str, Any]) -> dict[str, Any]

      Play one turn of the game.


      .. autolink-examples:: play_turn
         :collapse:


   .. py:method:: setup_routing() -> None

      Set up the routing for the game.


      .. autolink-examples:: setup_routing
         :collapse:


   .. py:method:: setup_workflow() -> None

      Set up the game workflow using the graph_builder.


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_continue(state: dict[str, Any]) -> bool

      Check if game should continue.


      .. autolink-examples:: should_continue
         :collapse:


