games.mancala.agent
===================

.. py:module:: games.mancala.agent

Mancala game agent.

This module defines the Mancala game agent, which uses language models to generate moves
and analyze positions in the game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Mancala game agent.

   This module defines the Mancala game agent, which uses language models to generate moves
   and analyze positions in the game.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mancala.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.mancala.agent.MancalaAgent

            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.mancala.agent.ensure_game_state
      games.mancala.agent.extract_data_from_response

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MancalaAgent(config: haive.games.mancala.config.MancalaConfig)

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.mancala.config.MancalaConfig`\ ]


            Agent for playing Mancala using language models.

            This agent uses LLMs to generate moves and analyze positions
            in the Mancala game. It builds a dynamic graph for game flow
            and uses structured outputs for reliable move generation.

            .. attribute:: config

               Configuration for the Mancala game.

            .. attribute:: graph_builder

               Dynamic graph builder for game flow.

            .. attribute:: state_manager

               Manager for game state transitions.

            Initialize the Mancala agent.

            :param config: Configuration for the Mancala game.


            .. py:method:: _analyze_position(state: haive.games.mancala.state.MancalaState, player: str) -> haive.games.mancala.state.MancalaState

               Analyze the current position for the specified player.

               :param state: Current game state.
               :param player: Player to analyze for.

               :returns: State with analysis added.



            .. py:method:: _apply_move(state: haive.games.mancala.state.MancalaState, move: haive.games.mancala.models.MancalaMove) -> haive.games.mancala.state.MancalaState

               Apply a move to the game state.

               :param state: Current game state.
               :param move: Move to apply.

               :returns: Updated game state.



            .. py:method:: _build_graph() -> None

               Build the game flow graph.



            .. py:method:: _create_graph_structure() -> haive.core.graph.dynamic_graph_builder.DynamicGraph

               Create the full graph structure for the game.

               :returns: DynamicGraph configured for Mancala gameplay.



            .. py:method:: _create_simple_graph() -> haive.core.graph.dynamic_graph_builder.DynamicGraph

               Create a simplified graph structure as fallback.

               :returns: Simplified DynamicGraph for basic gameplay.



            .. py:method:: _prepare_move_prompt(state: haive.games.mancala.state.MancalaState, player: str, valid_moves: list[int]) -> dict[str, Any]

               Prepare the prompt data for move generation.

               :param state: Current game state.
               :param player: Player making the move.
               :param valid_moves: List of valid move indices.

               :returns: Dictionary with prompt data for the LLM.



            .. py:method:: check_game_over(state: dict | haive.games.mancala.state.MancalaState) -> dict

               Check if the game is over and update state accordingly.

               :param state: Current game state.

               :returns: Updated game state as dictionary.



            .. py:method:: make_move(state: haive.games.mancala.state.MancalaState, player: str) -> haive.games.mancala.state.MancalaState

               Make a move for the specified player.

               This method handles move generation, validation, and state updates.
               It includes retry logic for invalid moves and fallback to random
               valid moves if the LLM fails.

               :param state: Current game state.
               :param player: Player making the move ('player1' or 'player2').

               :returns: Updated game state after the move.



            .. py:method:: player1_turn(state: dict | haive.games.mancala.state.MancalaState) -> dict

               Execute player 1's turn.

               :param state: Current game state.

               :returns: Updated game state after player 1's move as dictionary.



            .. py:method:: player2_turn(state: dict | haive.games.mancala.state.MancalaState) -> dict

               Execute player 2's turn.

               :param state: Current game state.

               :returns: Updated game state after player 2's move as dictionary.



            .. py:method:: run(input_data: dict[str, Any] | None = None) -> dict[str, Any]

               Run the Mancala game.

               :param input_data: Optional input data for the game.

               :returns: The final game state as a dictionary.



            .. py:method:: simple_play(state: dict | haive.games.mancala.state.MancalaState) -> dict

               Simple play logic for fallback mode.

               :param state: Current game state.

               :returns: Updated game state as dictionary.



            .. py:attribute:: state_manager



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

            Ensure input is converted to MancalaState.

            :param state_input: Input that could be a dict, MancalaState, or Command.

            :returns: Properly typed game state.
            :rtype: MancalaState



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: extract_data_from_response(response: Any, data_type: str = 'move') -> dict[str, Any] | None

            Extract move or analysis data from an LLM response.

            :param response: The response from the LLM.
            :param data_type: Type of data to extract ('move' or 'analysis').

            :returns: Extracted data dictionary or None.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mancala.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

