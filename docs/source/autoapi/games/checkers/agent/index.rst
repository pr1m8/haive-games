games.checkers.agent
====================

.. py:module:: games.checkers.agent

Checkers agent implementation module.

This module provides the main checkers agent implementation using LangGraph, including:
    - Dynamic graph-based workflow for turn management
    - LLM-powered player engines for move generation
    - Position analysis and evaluation
    - Error handling and retry logic
    - Rich UI visualization
    - Game flow orchestration

The agent uses a state-based approach with LangGraph for managing the game workflow
and supports both automated play and human interaction through a beautiful UI.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Checkers agent implementation module.

   This module provides the main checkers agent implementation using LangGraph, including:
       - Dynamic graph-based workflow for turn management
       - LLM-powered player engines for move generation
       - Position analysis and evaluation
       - Error handling and retry logic
       - Rich UI visualization
       - Game flow orchestration

   The agent uses a state-based approach with LangGraph for managing the game workflow
   and supports both automated play and human interaction through a beautiful UI.



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.checkers.agent.CheckersAgent

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CheckersAgent(config: haive.games.checkers.config.CheckersAgentConfig)

            Bases: :py:obj:`haive.games.framework.base.GameAgent`\ [\ :py:obj:`haive.games.checkers.config.CheckersAgentConfig`\ ]


            Agent for playing checkers with LLM-based players and rich UI.

            This agent implements a complete checkers game using language models for
            move generation and position analysis. It uses LangGraph to create a
            workflow graph that manages the game flow between players.

            Features:
                - LLM-powered checkers players with structured outputs
                - Position analysis for better decision making
                - Beautiful rich-text UI visualization
                - Move validation and retry logic
                - Game status tracking and termination
                - Error handling and fallback moves

            .. attribute:: config

               Configuration for the checkers agent

               :type: CheckersAgentConfig

            .. attribute:: state_manager

               Manager for game state operations

               :type: CheckersStateManager

            .. attribute:: ui

               Rich UI for game visualization

               :type: CheckersUI

            .. attribute:: engines

               LLM engines for players and analyzers

               :type: dict

            .. attribute:: graph

               LangGraph workflow for the checkers game

               :type: DynamicGraph

            .. rubric:: Examples

            >>> # Create and run a checkers game
            >>> agent = CheckersAgent(CheckersAgentConfig())
            >>> final_state = agent.run_game(visualize=True)
            >>>
            >>> # Check the final game state
            >>> print(f"Game winner: {final_state.get('winner')}")

            Initialize the checkers agent.

            Sets up the state manager, UI, and other components needed for
            the checkers game.

            :param config: Configuration for the checkers agent
            :type config: CheckersAgentConfig


            .. py:method:: analyze_player1(state: dict[str, Any]) -> langgraph.types.Command

               Analyze the position for player 1 (red).

               Handles position analysis for the red player.

               :param state: Current game state
               :type state: dict[str, Any]

               :returns: LangGraph command with updated state and next node
               :rtype: Command



            .. py:method:: analyze_player2(state: dict[str, Any]) -> langgraph.types.Command

               Analyze the position for player 2 (black).

               Handles position analysis for the black player.

               :param state: Current game state
               :type state: dict[str, Any]

               :returns: LangGraph command with updated state and next node
               :rtype: Command



            .. py:method:: analyze_position(state: haive.games.checkers.state.CheckersState, player: str) -> langgraph.types.Command

               Analyze the position for a player.

               Gets a detailed position analysis from the appropriate analyzer engine
               and updates the game state with the analysis.

               :param state: Current game state
               :type state: CheckersState
               :param player: Player to analyze for ("red" or "black")
               :type player: str

               :returns: LangGraph command with updated state and next node
               :rtype: Command



            .. py:method:: extract_move(response: haive.games.checkers.models.CheckersPlayerDecision) -> haive.games.checkers.models.CheckersMove

               Extract a move from a player decision.

               Gets the selected move from a player's decision object.

               :param response: Player's move decision
               :type response: CheckersPlayerDecision

               :returns: The selected move
               :rtype: CheckersMove



            .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

               Initialize a new checkers game.

               Creates a fresh checkers game state and routes to the first player's move.

               :param state: Initial state data (usually empty)
               :type state: dict[str, Any]

               :returns: LangGraph command with initialized game state
               :rtype: Command



            .. py:method:: make_move(state: haive.games.checkers.state.CheckersState, player: str) -> langgraph.types.Command

               Make a move with error handling and retry logic.

               Core method for generating and applying moves, with robust error handling
               and visualization.

               The method:
               1. Shows a thinking animation
               2. Gets legal moves
               3. Prepares context for the LLM
               4. Gets a move decision from the appropriate engine
               5. Validates and applies the move
               6. Updates the game state

               Includes retry logic for invalid moves and fallback to the first legal
               move if all attempts fail.

               :param state: Current game state
               :type state: CheckersState
               :param player: Player to make the move ("red" or "black")
               :type player: str

               :returns: LangGraph command with updated state and next node
               :rtype: Command



            .. py:method:: make_player1_move(state: dict[str, Any]) -> langgraph.types.Command

               Make a move for player 1 (red).

               Handles the red player's turn, routing appropriately based on the
               current game state.

               :param state: Current game state
               :type state: dict[str, Any]

               :returns: LangGraph command with updated state and next node
               :rtype: Command



            .. py:method:: make_player2_move(state: dict[str, Any]) -> langgraph.types.Command

               Make a move for player 2 (black).

               Handles the black player's turn, routing appropriately based on the
               current game state.

               :param state: Current game state
               :type state: dict[str, Any]

               :returns: LangGraph command with updated state and next node
               :rtype: Command



            .. py:method:: prepare_analysis_context(state: haive.games.checkers.state.CheckersState, player: str) -> dict[str, Any]

               Prepare context for position analysis.

               Creates a context dictionary with all necessary information for
               the analyzer engines to evaluate a position.

               :param state: Current game state
               :type state: CheckersState
               :param player: Player to analyze for ("red" or "black")
               :type player: str

               :returns: Context dictionary for analysis
               :rtype: dict[str, Any]



            .. py:method:: prepare_move_context(state: haive.games.checkers.state.CheckersState, player: str) -> dict[str, Any]

               Prepare context for move generation.

               Creates a context dictionary with all necessary information for
               the player engines to make a move decision.

               :param state: Current game state
               :type state: CheckersState
               :param player: Player to make the move ("red" or "black")
               :type player: str

               :returns: Context dictionary for move generation
               :rtype: dict[str, Any]



            .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

               Run the checkers game.

               Runs a complete checkers game with optional visualization.

               :param visualize: Whether to show the UI. Defaults to True.
               :type visualize: bool, optional

               :returns: Final game state
               :rtype: dict[str, Any]

               .. rubric:: Examples

               >>> agent = CheckersAgent(CheckersAgentConfig())
               >>> # Run with visualization
               >>> final_state = agent.run_game(visualize=True)
               >>> # Run without visualization
               >>> final_state = agent.run_game(visualize=False)



            .. py:method:: run_game_with_ui() -> dict[str, Any]

               Run game with beautiful UI visualization.

               Runs a complete checkers game with rich UI visualization,
               streaming the state updates and displaying them in real-time.

               :returns: Final game state
               :rtype: dict[str, Any]

               .. rubric:: Examples

               >>> agent = CheckersAgent(CheckersAgentConfig())
               >>> final_state = agent.run_game_with_ui()
               >>> print(f"Winner: {final_state.get('winner')}")



            .. py:method:: setup_workflow() -> None

               Set up the workflow graph for the checkers game.

               Creates a LangGraph workflow with nodes for initialization, moves,
               and analysis, with appropriate edges between them.

               The graph flow follows this pattern:
               initialize → player1_move → analyze_player2 → player2_move → analyze_player1 → loop




            .. py:method:: visualize_state(state: dict[str, Any]) -> None

               Use the rich UI to visualize the current game state.

               Displays the current board, game info, move history, and other
               visual elements using the rich UI.

               :param state: Current game state
               :type state: dict[str, Any]



            .. py:attribute:: state_manager


            .. py:attribute:: ui





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.checkers.agent import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

