games.single_player.flow_free.agent
===================================

.. py:module:: games.single_player.flow_free.agent

.. autoapi-nested-parse::

   Flow Free game agent implementation.

   This module implements the agent for the Flow Free puzzle game, handling move
   generation, analysis, and game flow.


   .. autolink-examples:: games.single_player.flow_free.agent
      :collapse:


Classes
-------

.. autoapisummary::

   games.single_player.flow_free.agent.FlowFreeAgent


Module Contents
---------------

.. py:class:: FlowFreeAgent(config: haive.games.single_player.flow_free.config.FlowFreeConfig = FlowFreeConfig())

   Bases: :py:obj:`haive.games.single_player.base.SinglePlayerGameAgent`


   Agent for playing Flow Free puzzle game.

   Initialize the Flow Free agent.

   :param config: Configuration for the agent.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FlowFreeAgent
      :collapse:

   .. py:method:: extract_move(response: Any) -> haive.games.single_player.flow_free.models.FlowFreeMove

      Extract a move from the engine response.

      :param response: Response from the engine.

      :returns: Extracted FlowFreeMove.


      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Flow Free game.

      :param state: Initial state.

      :returns: Command with the initialized game state.


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: prepare_analysis_context(state: haive.games.single_player.flow_free.state.FlowFreeState) -> dict[str, Any]

      Prepare context for position analysis.

      :param state: Current game state.

      :returns: Context for the analysis engine.


      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.single_player.flow_free.state.FlowFreeState) -> dict[str, Any]

      Prepare context for move generation.

      :param state: Current game state.

      :returns: Context for the move generation engine.


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: run_game(debug: bool = False) -> dict[str, Any]

      Run a complete Flow Free game.

      :param debug: Whether to show debug information.

      :returns: Final game state.


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current game state.

      :param state: Current game state.


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: console


   .. py:attribute:: state_manager


