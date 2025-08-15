games.mancala.agent
===================

.. py:module:: games.mancala.agent

.. autoapi-nested-parse::

   Mancala game agent.

   This module defines the Mancala game agent, which uses language models to generate moves
   and analyze positions in the game.


   .. autolink-examples:: games.mancala.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mancala.agent.logger


Classes
-------

.. autoapisummary::

   games.mancala.agent.MancalaAgent


Functions
---------

.. autoapisummary::

   games.mancala.agent.ensure_game_state
   games.mancala.agent.extract_data_from_response


Module Contents
---------------

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


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MancalaAgent
      :collapse:

   .. py:method:: _analyze_position(state: haive.games.mancala.state.MancalaState, player: str) -> haive.games.mancala.state.MancalaState

      Analyze the current position for the specified player.

      :param state: Current game state.
      :param player: Player to analyze for.

      :returns: State with analysis added.


      .. autolink-examples:: _analyze_position
         :collapse:


   .. py:method:: _apply_move(state: haive.games.mancala.state.MancalaState, move: haive.games.mancala.models.MancalaMove) -> haive.games.mancala.state.MancalaState

      Apply a move to the game state.

      :param state: Current game state.
      :param move: Move to apply.

      :returns: Updated game state.


      .. autolink-examples:: _apply_move
         :collapse:


   .. py:method:: _build_graph() -> None

      Build the game flow graph.


      .. autolink-examples:: _build_graph
         :collapse:


   .. py:method:: _create_graph_structure() -> haive.core.graph.dynamic_graph_builder.DynamicGraph

      Create the full graph structure for the game.

      :returns: DynamicGraph configured for Mancala gameplay.


      .. autolink-examples:: _create_graph_structure
         :collapse:


   .. py:method:: _create_simple_graph() -> haive.core.graph.dynamic_graph_builder.DynamicGraph

      Create a simplified graph structure as fallback.

      :returns: Simplified DynamicGraph for basic gameplay.


      .. autolink-examples:: _create_simple_graph
         :collapse:


   .. py:method:: _prepare_move_prompt(state: haive.games.mancala.state.MancalaState, player: str, valid_moves: list[int]) -> dict[str, Any]

      Prepare the prompt data for move generation.

      :param state: Current game state.
      :param player: Player making the move.
      :param valid_moves: List of valid move indices.

      :returns: Dictionary with prompt data for the LLM.


      .. autolink-examples:: _prepare_move_prompt
         :collapse:


   .. py:method:: check_game_over(state: dict | haive.games.mancala.state.MancalaState) -> dict

      Check if the game is over and update state accordingly.

      :param state: Current game state.

      :returns: Updated game state as dictionary.


      .. autolink-examples:: check_game_over
         :collapse:


   .. py:method:: make_move(state: haive.games.mancala.state.MancalaState, player: str) -> haive.games.mancala.state.MancalaState

      Make a move for the specified player.

      This method handles move generation, validation, and state updates.
      It includes retry logic for invalid moves and fallback to random
      valid moves if the LLM fails.

      :param state: Current game state.
      :param player: Player making the move ('player1' or 'player2').

      :returns: Updated game state after the move.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: player1_turn(state: dict | haive.games.mancala.state.MancalaState) -> dict

      Execute player 1's turn.

      :param state: Current game state.

      :returns: Updated game state after player 1's move as dictionary.


      .. autolink-examples:: player1_turn
         :collapse:


   .. py:method:: player2_turn(state: dict | haive.games.mancala.state.MancalaState) -> dict

      Execute player 2's turn.

      :param state: Current game state.

      :returns: Updated game state after player 2's move as dictionary.


      .. autolink-examples:: player2_turn
         :collapse:


   .. py:method:: run(input_data: dict[str, Any] | None = None) -> dict[str, Any]

      Run the Mancala game.

      :param input_data: Optional input data for the game.

      :returns: The final game state as a dictionary.


      .. autolink-examples:: run
         :collapse:


   .. py:method:: simple_play(state: dict | haive.games.mancala.state.MancalaState) -> dict

      Simple play logic for fallback mode.

      :param state: Current game state.

      :returns: Updated game state as dictionary.


      .. autolink-examples:: simple_play
         :collapse:


   .. py:attribute:: state_manager


.. py:function:: ensure_game_state(state_input: dict[str, Any] | haive.games.mancala.state.MancalaState | langgraph.types.Command) -> haive.games.mancala.state.MancalaState

   Ensure input is converted to MancalaState.

   :param state_input: Input that could be a dict, MancalaState, or Command.

   :returns: Properly typed game state.
   :rtype: MancalaState


   .. autolink-examples:: ensure_game_state
      :collapse:

.. py:function:: extract_data_from_response(response: Any, data_type: str = 'move') -> dict[str, Any] | None

   Extract move or analysis data from an LLM response.

   :param response: The response from the LLM.
   :param data_type: Type of data to extract ('move' or 'analysis').

   :returns: Extracted data dictionary or None.


   .. autolink-examples:: extract_data_from_response
      :collapse:

.. py:data:: logger

