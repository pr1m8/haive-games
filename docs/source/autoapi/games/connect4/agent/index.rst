games.connect4.agent
====================

.. py:module:: games.connect4.agent

.. autoapi-nested-parse::

   Agent for playing Connect 4.

   This module defines the Connect 4 agent, which uses language models to generate moves
   and analyze positions in the game.


   .. autolink-examples:: games.connect4.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.connect4.agent.logger


Classes
-------

.. autoapisummary::

   games.connect4.agent.Connect4Agent


Module Contents
---------------

.. py:class:: Connect4Agent(config: haive.games.connect4.config.Connect4AgentConfig)

   Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.connect4.config.Connect4AgentConfig`\ ]


   Agent for playing Connect 4.

   This class implements the Connect 4 agent, which uses language models to generate
   moves and analyze positions in the game.



   .. autolink-examples:: Connect4Agent
      :collapse:

   .. py:method:: _calculate_threats(state: haive.games.connect4.state.Connect4State, player: str) -> dict[str, list[int]]

      Calculate immediate threats and opportunities.

      This method calculates the immediate threats and opportunities for the given
      player in the current game state.



      .. autolink-examples:: _calculate_threats
         :collapse:


   .. py:method:: analyze_player1(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

      Analyze position for the red player.

      This method analyzes the position for the red player in the current game state.



      .. autolink-examples:: analyze_player1
         :collapse:


   .. py:method:: analyze_player2(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

      Analyze position for the yellow player.

      This method analyzes the position for the yellow player in the current game
      state.



      .. autolink-examples:: analyze_player2
         :collapse:


   .. py:method:: extract_move(response: haive.games.connect4.models.Connect4PlayerDecision) -> haive.games.connect4.models.Connect4Move

      Extract move from engine response.

      This method extracts the move from the engine response.



      .. autolink-examples:: extract_move
         :collapse:


   .. py:method:: make_player1_move(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

      Make a move for the red player.

      This method makes a move for the red player in the current game state.



      .. autolink-examples:: make_player1_move
         :collapse:


   .. py:method:: make_player2_move(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

      Make a move for the yellow player.

      This method makes a move for the yellow player in the current game state.



      .. autolink-examples:: make_player2_move
         :collapse:


   .. py:method:: prepare_analysis_context(state: haive.games.connect4.state.Connect4State, player: str) -> dict[str, Any]

      Prepare context for position analysis with correct variables.

      This method prepares the context for position analysis by calculating threats
      and formatting the required fields.



      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.connect4.state.Connect4State, player: str) -> dict[str, Any]

      Prepare context for move generation.

      This method prepares the context for move generation by formatting the legal
      moves and getting the player's last analysis.



      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: visualize_state(state: dict[str, Any]) -> None

      Visualize the current game state with better formatting and insights.

      This method visualizes the current game state with better formatting and
      insights. It displays the current player, game status, board, last move, and
      analysis from the previous turn.



      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: state_manager


.. py:data:: logger

