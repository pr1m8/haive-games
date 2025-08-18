games.single_player.flow_free.state_manager
===========================================

.. py:module:: games.single_player.flow_free.state_manager

State manager for Flow Free game logic and mechanics.

This module handles game initialization, move validation, and state transitions for the
Flow Free puzzle game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   State manager for Flow Free game logic and mechanics.

   This module handles game initialization, move validation, and state transitions for the
   Flow Free puzzle game.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.flow_free.state_manager.FlowFreeStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: FlowFreeStateManager

            Bases: :py:obj:`haive.games.single_player.base.SinglePlayerStateManager`\ [\ :py:obj:`haive.games.single_player.flow_free.state.FlowFreeState`\ ]


            Manager for Flow Free game state.


            .. py:method:: _calculate_pipe_direction(prev_pos: haive.games.single_player.flow_free.models.Position, curr_pos: haive.games.single_player.flow_free.models.Position) -> haive.games.single_player.flow_free.models.PipeDirection
               :classmethod:


               Calculate the direction of a pipe segment.

               :param prev_pos: Previous position in the path.
               :param curr_pos: Current position in the path.

               :returns: Direction of the pipe.



            .. py:method:: _get_potential_positions(state: haive.games.single_player.flow_free.state.FlowFreeState, flow_id: str) -> list[haive.games.single_player.flow_free.models.Position]
               :classmethod:


               Get potential positions for the next segment of a flow.

               :param state: Current game state.
               :param flow_id: ID of the flow to extend.

               :returns: List of potential positions.



            .. py:method:: _is_flow_completed(state: haive.games.single_player.flow_free.state.FlowFreeState, flow: haive.games.single_player.flow_free.state.Flow) -> bool
               :classmethod:


               Check if a flow is completed.

               A flow is completed if there's a path from the start endpoint to the end endpoint.

               :param state: Current game state.
               :param flow: Flow to check.

               :returns: True if the flow is completed, False otherwise.



            .. py:method:: apply_move(state: haive.games.single_player.flow_free.state.FlowFreeState, move: haive.games.single_player.flow_free.models.FlowFreeMove) -> haive.games.single_player.flow_free.state.FlowFreeState
               :classmethod:


               Apply a move to the current state.

               :param state: Current game state.
               :param move: Move to apply.

               :returns: Updated game state.

               :raises ValueError: If the move is invalid.



            .. py:method:: check_game_status(state: haive.games.single_player.flow_free.state.FlowFreeState) -> haive.games.single_player.flow_free.state.FlowFreeState
               :classmethod:


               Check and update the game status.

               :param state: Current game state.

               :returns: Updated game state with status checked.



            .. py:method:: generate_hint(state: haive.games.single_player.flow_free.state.FlowFreeState) -> tuple[haive.games.single_player.flow_free.state.FlowFreeState, str]
               :classmethod:


               Generate a hint for the current game state.

               :param state: Current game state.

               :returns: Tuple of (updated state, hint text).



            .. py:method:: get_legal_moves(state: haive.games.single_player.flow_free.state.FlowFreeState) -> list[haive.games.single_player.flow_free.models.FlowFreeMove]
               :classmethod:


               Get all legal moves for the current state.

               :param state: Current game state.

               :returns: List of all legal moves.



            .. py:method:: initialize(difficulty: haive.games.single_player.base.GameDifficulty = GameDifficulty.MEDIUM, player_type: haive.games.single_player.base.PlayerType = PlayerType.LLM, rows: int = 5, cols: int = 5, num_flows: int | None = None, **kwargs) -> haive.games.single_player.flow_free.state.FlowFreeState
               :classmethod:


               Initialize a new Flow Free game state.

               :param difficulty: Difficulty level of the game.
               :param player_type: Type of player.
               :param rows: Number of rows in the grid.
               :param cols: Number of columns in the grid.
               :param num_flows: Number of flows to include. If None, determined by difficulty.
               :param \*\*kwargs: Additional initialization parameters.

               :returns: A new Flow Free game state.



            .. py:method:: interactive_input(state: haive.games.single_player.flow_free.state.FlowFreeState, user_input: str) -> haive.games.single_player.flow_free.state.FlowFreeState
               :classmethod:


               Process interactive input from the player.

               :param state: Current game state.
               :param user_input: User input string.

               :returns: Updated game state.



            .. py:attribute:: SAMPLE_PUZZLES





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.flow_free.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

