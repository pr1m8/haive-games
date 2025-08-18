games.single_player.flow_free.agent
===================================

.. py:module:: games.single_player.flow_free.agent

Flow Free game agent implementation.

This module implements the agent for the Flow Free puzzle game, handling move
generation, analysis, and game flow.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Flow Free game agent implementation.

   This module implements the agent for the Flow Free puzzle game, handling move
   generation, analysis, and game flow.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.flow_free.agent.FlowFreeAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeAgent(config: haive.games.single_player.flow_free.config.FlowFreeConfig = FlowFreeConfig())

            Bases: :py:obj:`haive.games.single_player.base.SinglePlayerGameAgent`


            Agent for playing Flow Free puzzle game.

            Initialize the Flow Free agent.

            :param config: Configuration for the agent.


            .. py:method:: extract_move(response: Any) -> haive.games.single_player.flow_free.models.FlowFreeMove

               Extract a move from the engine response.

               :param response: Response from the engine.

               :returns: Extracted FlowFreeMove.



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new Flow Free game.

               :param state: Initial state.

               :returns: Command with the initialized game state.



            .. py:method:: prepare_analysis_context(state: haive.games.single_player.flow_free.state.FlowFreeState) -> dict[str, Any]

               Prepare context for position analysis.

               :param state: Current game state.

               :returns: Context for the analysis engine.



            .. py:method:: prepare_move_context(state: haive.games.single_player.flow_free.state.FlowFreeState) -> dict[str, Any]

               Prepare context for move generation.

               :param state: Current game state.

               :returns: Context for the move generation engine.



            .. py:method:: run_game(debug: bool = False) -> dict[str, Any]

               Run a complete Flow Free game.

               :param debug: Whether to show debug information.

               :returns: Final game state.



            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state.

               :param state: Current game state.



            .. py:attribute:: console


            .. py:attribute:: state_manager





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.flow_free.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

