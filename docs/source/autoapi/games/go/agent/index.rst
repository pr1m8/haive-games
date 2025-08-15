games.go.agent
==============

.. py:module:: games.go.agent

.. autoapi-nested-parse::

   Go game agent implementation.

   This module provides a Go game agent that supports:
       - Standard Go game rules and mechanics
       - Black and white player moves
       - Optional position analysis
       - Game state tracking and visualization
       - SGF format support via sente library

   .. rubric:: Example

   >>> from haive.games.go import GoAgent, GoAgentConfig
   >>>
   >>> # Create a Go agent with analysis enabled
   >>> config = GoAgentConfig(include_analysis=True)
   >>> agent = GoAgent(config)
   >>>
   >>> # Run a game
   >>> run_go_game(agent)


   .. autolink-examples:: games.go.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.go.agent.logger


Classes
-------

.. autoapisummary::

   games.go.agent.GoAgent


Functions
---------

.. autoapisummary::

   games.go.agent.run_go_game


Module Contents
---------------

.. py:class:: GoAgent(config: haive.games.go.config.GoAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.go.config.GoAgentConfig`\ ]


   Go game agent implementation.

   This class provides the core functionality for playing Go games, including:
       - Move generation for both black and white players
       - Position analysis and evaluation
       - Game state management and validation
       - Workflow control for game progression

   .. attribute:: config

      Configuration for the Go agent

      :type: GoAgentConfig

   .. attribute:: engines

      LLM engines for players and analysis

      :type: Dict[str, Any]

   .. attribute:: graph

      Game workflow graph

      :type: StateGraph

   .. rubric:: Example

   >>> config = GoAgentConfig(
   ...     include_analysis=True,
   ...     board_size=19
   ... )
   >>> agent = GoAgent(config)
   >>> run_go_game(agent)

   Initialize the Go agent.

   :param config: Configuration for the Go agent.
   :type config: GoAgentConfig


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GoAgent
      :collapse:

   .. py:method:: analyze_black_position(state: haive.games.go.state.GoGameState) -> langgraph.types.Command

      Analyze black's position if analysis is enabled.

      :param state: Current game state.
      :type state: GoGameState

      :returns: Command to update the game state with black's analysis.
      :rtype: Command


      .. autolink-examples:: analyze_black_position
         :collapse:


   .. py:method:: analyze_position(state: haive.games.go.state.GoGameState, color: str) -> langgraph.types.Command

      Analyze the current position for a player.

      :param state: Current game state.
      :type state: GoGameState
      :param color: Player color ("black" or "white").
      :type color: str

      :returns: Command to update the game state with the analysis.
      :rtype: Command

      :raises ValueError: If no LLM engine is found for analysis.

      .. rubric:: Notes

      - Maintains a history of the last 4 analyses
      - Provides territory evaluation and strategic advice
      - Identifies strong and weak positions


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: analyze_white_position(state: haive.games.go.state.GoGameState) -> langgraph.types.Command

      Analyze white's position if analysis is enabled.

      :param state: Current game state.
      :type state: GoGameState

      :returns: Command to update the game state with white's analysis.
      :rtype: Command


      .. autolink-examples:: analyze_white_position
         :collapse:


   .. py:method:: check_game_status(state: haive.games.go.state.GoGameState) -> langgraph.types.Command

      Check and update the Go game status.

      :param state: Current game state.
      :type state: GoGameState

      :returns: Command to update the game status.
      :rtype: Command

      .. rubric:: Notes

      - Uses sente library to validate game state
      - Detects game end conditions (resignation, passes)
      - Updates status to "ended" when game is complete


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: initialize_game(state: haive.games.go.state.GoGameState | None = None) -> langgraph.types.Command

      Initialize a new game of Go.

      :param state: Optional initial state. If None,
                    creates a new game with standard settings.
      :type state: Optional[GoGameState]

      :returns: Command to update the game state with initial settings.
      :rtype: Command


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: make_black_move(state: haive.games.go.state.GoGameState) -> langgraph.types.Command

      Handle black's move in the game.

      :param state: Current game state.
      :type state: GoGameState

      :returns: Command to update the game state with black's move.
      :rtype: Command


      .. autolink-examples:: make_black_move
         :collapse:


   .. py:method:: make_move(state: haive.games.go.state.GoGameState, color: str) -> langgraph.types.Command

      Execute a move for the given player.

      :param state: Current game state.
      :type state: GoGameState
      :param color: Player color ("black" or "white").
      :type color: str

      :returns: Command to update the game state with the new move.
      :rtype: Command

      :raises ValueError: If no LLM engine is found for the player.

      .. rubric:: Notes

      - Provides the last 5 moves as context to the LLM
      - Includes recent position analysis if available
      - Validates moves through the state manager


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: make_white_move(state: haive.games.go.state.GoGameState) -> langgraph.types.Command

      Handle white's move in the game.

      :param state: Current game state.
      :type state: GoGameState

      :returns: Command to update the game state with white's move.
      :rtype: Command


      .. autolink-examples:: make_white_move
         :collapse:


   .. py:method:: setup_workflow() -> None

      Define the Go game workflow.

      Sets up the game flow graph with nodes for:
          - Game initialization
          - Black and white moves
          - Position analysis (if enabled)
          - Game status checks

      The workflow supports two main paths:
          1. Basic: Initialize -> Black Move -> White Move -> Repeat
          2. With Analysis: Initialize -> Black Move -> Black Analysis ->
             White Move -> White Analysis -> Repeat



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: should_continue_game(state: haive.games.go.state.GoGameState) -> bool

      Determine if the game should continue.

      :param state: Current game state.
      :type state: GoGameState

      :returns: True if game is ongoing, False otherwise.
      :rtype: bool


      .. autolink-examples:: should_continue_game
         :collapse:


.. py:function:: run_go_game(agent: GoAgent) -> None

   Run a Go game with visualization and structured output.

   This function manages the game loop and provides rich visualization
   of the game state, including:
       - Board visualization using ASCII art
       - Move history tracking
       - Position analysis display
       - Captured stones counting
       - Game status updates

   :param agent: The Go agent to run the game with.
   :type agent: GoAgent

   .. rubric:: Example

   >>> agent = GoAgent(GoAgentConfig(include_analysis=True))
   >>> run_go_game(agent)

   🔷 Current Board Position:
   . . . . . . . . .
   . . . . . . . . .
   . . + . . . + . .
   . . . . . . . . .
   . . . . + . . . .
   . . . . . . . . .
   . . + . . . + . .
   . . . . . . . . .
   . . . . . . . . .

   🎮 Current Player: Black
   📌 Game Status: ongoing
   --------------------------------------------------


   .. autolink-examples:: run_go_game
      :collapse:

.. py:data:: logger

