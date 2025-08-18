games.connect4.agent
====================

.. py:module:: games.connect4.agent

Agent for playing Connect 4.

This module defines the Connect 4 agent, which uses language models to generate moves
and analyze positions in the game.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Agent for playing Connect 4.

   This module defines the Connect 4 agent, which uses language models to generate moves
   and analyze positions in the game.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.connect4.agent.logger

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.connect4.agent.Connect4Agent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Connect4Agent(config: haive.games.connect4.config.Connect4AgentConfig)

            Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.connect4.config.Connect4AgentConfig`\ ]


            Agent for playing Connect 4.

            This class implements the Connect 4 agent, which uses language models to generate
            moves and analyze positions in the game.


            Initialize the game agent.

            :param config: Configuration for the game agent.
                           Defaults to GameConfig().
            :type config: GameConfig, optional


            .. py:method:: _calculate_threats(state: haive.games.connect4.state.Connect4State, player: str) -> dict[str, list[int]]

               Calculate immediate threats and opportunities.

               This method calculates the immediate threats and opportunities for the given
               player in the current game state.




            .. py:method:: analyze_player1(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

               Analyze position for the red player.

               This method analyzes the position for the red player in the current game state.




            .. py:method:: analyze_player2(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

               Analyze position for the yellow player.

               This method analyzes the position for the yellow player in the current game
               state.




            .. py:method:: extract_move(response: haive.games.connect4.models.Connect4PlayerDecision) -> haive.games.connect4.models.Connect4Move

               Extract move from engine response.

               This method extracts the move from the engine response.




            .. py:method:: make_player1_move(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

               Make a move for the red player.

               This method makes a move for the red player in the current game state.




            .. py:method:: make_player2_move(state: haive.games.connect4.state.Connect4State) -> langgraph.types.Command

               Make a move for the yellow player.

               This method makes a move for the yellow player in the current game state.




            .. py:method:: prepare_analysis_context(state: haive.games.connect4.state.Connect4State, player: str) -> dict[str, Any]

               Prepare context for position analysis with correct variables.

               This method prepares the context for position analysis by calculating threats
               and formatting the required fields.




            .. py:method:: prepare_move_context(state: haive.games.connect4.state.Connect4State, player: str) -> dict[str, Any]

               Prepare context for move generation.

               This method prepares the context for move generation by formatting the legal
               moves and getting the player's last analysis.




            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Visualize the current game state with better formatting and insights.

               This method visualizes the current game state with better formatting and
               insights. It displays the current player, game status, board, last move, and
               analysis from the previous turn.




            .. py:attribute:: state_manager



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.connect4.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

