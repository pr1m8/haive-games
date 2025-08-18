games.chess.agent
=================

.. py:module:: games.chess.agent

Chess agent implementation using LangGraph.

This module provides a chess agent implementation using LangGraph, featuring:
    - LLM-powered chess players
    - Position analysis
    - Game state management
    - Workflow graph for turn-based gameplay
    - Error handling and retry logic

The agent orchestrates the game flow between two LLM players and handles
all game mechanics including move validation, position analysis, and
game status tracking.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Chess agent implementation using LangGraph.

   This module provides a chess agent implementation using LangGraph, featuring:
       - LLM-powered chess players
       - Position analysis
       - Game state management
       - Workflow graph for turn-based gameplay
       - Error handling and retry logic

   The agent orchestrates the game flow between two LLM players and handles
   all game mechanics including move validation, position analysis, and
   game status tracking.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.chess.agent.ChessAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ChessAgent(config: haive.games.chess.config.ChessConfig)

            Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.chess.config.ChessConfig`\ ]


            Chess agent implementation using LangGraph.

            This agent implements a complete chess game using language models for
            move generation and position analysis. It uses LangGraph to create a
            workflow graph that manages the game flow between players.

            Features:
                - LLM-powered chess players with structured outputs
                - Optional position analysis for enhanced play
                - Move validation and retry logic
                - Game status tracking and termination
                - Error handling and fallback moves

            .. attribute:: config

               Configuration for the chess agent

               :type: ChessConfig

            .. attribute:: engines

               LLM engines for players and analyzers

               :type: Dict[str, Any]

            .. attribute:: graph

               LangGraph workflow for the chess game

               :type: StateGraph

            Initialize the chess agent.

            :param config: Configuration for the chess agent,
                           including LLM engine settings, analysis options, and
                           game parameters.
            :type config: ChessConfig


            .. py:method:: analyze_black_position(state: haive.games.chess.state.ChessState) -> langgraph.types.Command

               Analyze the board position for the black player.

               :param state: Current game state
               :type state: ChessState

               :returns: LangGraph command with black analysis updates
               :rtype: Command



            .. py:method:: analyze_position(state: haive.games.chess.state.ChessState, color: str) -> langgraph.types.Command

               Analyze the board position for the specified player.

               This method uses the configured analyzer engine to generate
               a detailed position analysis from the perspective of the
               given player color.

               :param state: Current game state
               :type state: ChessState
               :param color: Player color ("white" or "black")
               :type color: str

               :returns: LangGraph command with analysis updates
               :rtype: Command

               .. note::

                  Analysis results are stored in the state's white_analysis
                  or black_analysis fields, depending on the color.



            .. py:method:: analyze_white_position(state: haive.games.chess.state.ChessState) -> langgraph.types.Command

               Analyze the board position for the white player.

               :param state: Current game state
               :type state: ChessState

               :returns: LangGraph command with white analysis updates
               :rtype: Command



            .. py:method:: check_game_status(state: haive.games.chess.state.ChessState) -> langgraph.types.Command

               Check and update the game status.

               This method evaluates the current board position to determine
               if the game has ended (checkmate, stalemate, draw) or if it
               should continue.

               Game-ending conditions include:
               - Checkmate
               - Stalemate
               - Insufficient material
               - Maximum move limit reached

               :param state: Current game state
               :type state: ChessState

               :returns: LangGraph command with game status updates
               :rtype: Command



            .. py:method:: make_black_move(state: haive.games.chess.state.ChessState) -> langgraph.types.Command

               Make a move for the black player.

               :param state: Current game state
               :type state: ChessState

               :returns: LangGraph command with state updates
               :rtype: Command



            .. py:method:: make_move(state: haive.games.chess.state.ChessState, color: str) -> langgraph.types.Command

               Make a move for the specified player with retry logic.

               This method handles the complete move generation process:
                   1. Gets legal moves from the current position
                   2. Sends context to the appropriate LLM engine
                   3. Validates the returned move
                   4. Updates the game state with the new move

               Includes retry logic for invalid moves, with fallback to a safe
               move if all attempts fail.

               :param state: Current game state
               :type state: ChessState
               :param color: Player color ("white" or "black")
               :type color: str

               :returns: LangGraph command with state updates
               :rtype: Command

               .. rubric:: Examples

               >>> command = agent.make_move(state, "white")
               >>> command.update  # Contains the updated game state
               {'board_fens': [...], 'move_history': [...], ...}



            .. py:method:: make_white_move(state: haive.games.chess.state.ChessState) -> langgraph.types.Command

               Make a move for the white player.

               :param state: Current game state
               :type state: ChessState

               :returns: LangGraph command with state updates
               :rtype: Command



            .. py:method:: route_next_step(state: haive.games.chess.state.ChessState) -> str

               Determine the next step in the workflow.

               This conditional router decides where to direct the flow next
               based on the current game state:
               - If the game is over, route to the end
               - Otherwise, route to the next player's turn

               :param state: Current game state
               :type state: ChessState

               :returns: The next step key for the workflow graph
               :rtype: str

               .. note::

                  Return values correspond to the keys in the conditional
                  edges of the graph: "game_over", "continue_white", or
                  "continue_black".



            .. py:method:: setup_workflow() -> None

               Set up the workflow graph for the chess game.

               Creates a LangGraph StateGraph with nodes for:
                   - White player's moves
                   - Black player's moves
                   - Game status checking
                   - Optional position analysis

               The graph flow depends on the current player and game status,
               with conditional edges for routing between nodes.




            .. py:attribute:: engines





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.chess.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

