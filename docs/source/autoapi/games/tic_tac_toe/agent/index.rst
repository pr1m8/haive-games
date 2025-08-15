games.tic_tac_toe.agent
=======================

.. py:module:: games.tic_tac_toe.agent

.. autoapi-nested-parse::

   Comprehensive agent implementation for strategic Tic Tac Toe gameplay.

   This module provides the core agent class for managing Tic Tac Toe games with
   LLM-driven decision-making, strategic analysis, and flexible gameplay modes.
   The agent coordinates all aspects of the game including initialization, move
   generation, position analysis, and game flow management.

   The agent supports:
   - LLM-based move generation with perfect play capability
   - Strategic position analysis for educational insights
   - Flexible game flow with conditional analysis
   - Board visualization for interactive gameplay
   - Error handling and state validation
   - Integration with LangGraph for distributed execution
   - Multiple AI personalities through engine configuration

   .. rubric:: Examples

   Basic game execution::

       config = TicTacToeConfig.default_config()
       agent = TicTacToeAgent(config)
       final_state = agent.run_game()

   Tournament play without visualization::

       config = TicTacToeConfig.competitive_config()
       agent = TicTacToeAgent(config)
       result = agent.run_game(visualize=False)

   Educational game with analysis::

       config = TicTacToeConfig.educational_config()
       agent = TicTacToeAgent(config)
       agent.run_game(visualize=True, debug=True)

   Custom engine configuration::

       config = TicTacToeConfig(
           engines=custom_engines,
           enable_analysis=True
       )
       agent = TicTacToeAgent(config)

   .. note::

      The agent uses LangGraph for workflow management and supports
      concurrent execution with proper state reducers.


   .. autolink-examples:: games.tic_tac_toe.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.tic_tac_toe.agent.logger


Classes
-------

.. autoapisummary::

   games.tic_tac_toe.agent.TicTacToeAgent


Module Contents
---------------

.. py:class:: TicTacToeAgent(config: haive.games.tic_tac_toe.config.TicTacToeConfig = TicTacToeConfig())

   Bases: :py:obj:`haive.games.framework.base.agent.GameAgent`\ [\ :py:obj:`haive.games.tic_tac_toe.config.TicTacToeConfig`\ ]


   Strategic agent for Tic Tac Toe gameplay with LLM-driven decision- making.

   This agent manages the complete Tic Tac Toe game lifecycle, from initialization
   through gameplay to completion. It coordinates LLM engines for move generation
   and position analysis, maintains game state consistency, and provides flexible
   gameplay modes for different use cases.

   The agent supports:
   - Automated game initialization with configurable parameters
   - LLM-based move generation for both X and O players
   - Optional strategic position analysis after each move
   - Board visualization for interactive experiences
   - Error handling and recovery mechanisms
   - Integration with state management system
   - Flexible workflow configuration

   .. attribute:: config

      Game configuration parameters.

      :type: TicTacToeConfig

   .. attribute:: state_manager

      State management system.

      :type: TicTacToeStateManager

   .. attribute:: engines

      LLM engines for players and analysis.

      :type: Dict[str, Engine]

   .. attribute:: graph

      LangGraph workflow for game execution.

      :type: StateGraph

   .. rubric:: Examples

   Standard gameplay::

       agent = TicTacToeAgent()
       result = agent.run_game()
       print(f"Winner: {result.winner}")

   Custom configuration::

       config = TicTacToeConfig(
           enable_analysis=False,
           first_player="O"
       )
       agent = TicTacToeAgent(config)

   Tournament mode::

       config = TicTacToeConfig.competitive_config()
       agent = TicTacToeAgent(config)
       # Fast gameplay without visualization

   Initialize the Tic Tac Toe agent with configuration.

   Sets up the agent with the provided configuration, initializes the
   state manager, and prepares the workflow graph for game execution.

   :param config: Game configuration with engine settings,
                  analysis options, and gameplay parameters.
   :type config: TicTacToeConfig

   .. rubric:: Examples

   Default initialization::

       agent = TicTacToeAgent()
       # Uses default configuration

   Custom configuration::

       config = TicTacToeConfig(
           enable_analysis=True,
           visualize=True
       )
       agent = TicTacToeAgent(config)


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TicTacToeAgent
      :collapse:

   .. py:method:: analyze_position(state) -> langgraph.types.Command

      Analyze the board position for strategic insights.

      Performs strategic analysis of the current board position for the player
      who just moved, providing insights about threats, opportunities, and
      optimal play. Analysis is only performed if enabled in configuration.

      :param state: Current game state (dict or TicTacToeState).

      :returns: LangGraph command with analysis results and next node.
      :rtype: Command

      .. rubric:: Examples

      Post-move analysis::

          # After X makes a move
          command = agent.analyze_position(state)
          # Analyzes position from X's perspective

      Analysis disabled::

          agent.config.enable_analysis = False
          command = agent.analyze_position(state)
          # Skips analysis, returns to make_move

      Game over analysis::

          state.game_status = "X_win"
          command = agent.analyze_position(state)
          # Returns Command with goto=END


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Tic Tac Toe game with starting configuration.

      Creates the initial game state with an empty board, assigns players
      to symbols based on configuration, and sets up the first turn.

      :param state: Initial state dictionary (typically empty).
      :type state: dict[str, Any]

      :returns: LangGraph command with initialized state and next node.
      :rtype: Command

      .. rubric:: Examples

      Standard initialization::

          command = agent.initialize_game({})
          # Returns Command with empty board, X to play

      Custom first player::

          agent.config.first_player = "O"
          command = agent.initialize_game({})
          # Returns Command with O to play first


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: make_move(state) -> langgraph.types.Command

      Generate and execute a move for the current player.

      Uses the appropriate LLM engine to generate a move for the current player,
      validates the move, updates the game state, and determines the next step
      in the workflow based on game status and configuration.

      :param state: Current game state (dict or TicTacToeState).

      :returns: LangGraph command with state updates and next node.
      :rtype: Command

      :raises Exception: If move generation or application fails.

      .. rubric:: Examples

      X player move::

          command = agent.make_move(state)
          # X engine generates move, state updated

      Game ending move::

          command = agent.make_move(near_end_state)
          # Returns Command with goto=END if game over

      With analysis enabled::

          agent.config.enable_analysis = True
          command = agent.make_move(state)
          # Returns Command with goto="analyze"


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: prepare_analysis_context(state: haive.games.tic_tac_toe.state.TicTacToeState, symbol: str) -> dict[str, Any]

      Prepare structured context for strategic position analysis.

      Creates a context dictionary for the analysis engine containing the
      current board state and player information for strategic evaluation.

      :param state: Current game state to analyze.
      :type state: TicTacToeState
      :param symbol: Symbol ('X' or 'O') of the player to analyze for.
      :type symbol: str

      :returns: Analysis context with board state and player symbols.
      :rtype: dict[str, Any]

      .. rubric:: Examples

      Analysis for X player::

          context = agent.prepare_analysis_context(state, "X")
          # Returns: {
          #     'board_string': '...',
          #     'player_symbol': 'X',
          #     'opponent_symbol': 'O'
          # }


      .. autolink-examples:: prepare_analysis_context
         :collapse:


   .. py:method:: prepare_move_context(state: haive.games.tic_tac_toe.state.TicTacToeState) -> dict[str, Any]

      Prepare structured context for LLM move generation.

      Creates a comprehensive context dictionary containing the current board
      state, legal moves, and previous analysis to enable informed decision-making
      by the LLM engine.

      :param state: Current game state with board and history.
      :type state: TicTacToeState

      :returns:

                Context dictionary with board representation,
                    legal moves, current player, and analysis history.
      :rtype: dict[str, Any]

      .. rubric:: Examples

      Context for opening move::

          context = agent.prepare_move_context(initial_state)
          # Returns: {
          #     'board_string': '   0 1 2\n  -------\n0 | | | |...',
          #     'current_player': 'X',
          #     'legal_moves': '(0, 0), (0, 1), (0, 2), ...',
          #     'player_analysis': 'No previous analysis available.'
          # }

      Mid-game context::

          context = agent.prepare_move_context(mid_game_state)
          # Includes previous analysis if available


      .. autolink-examples:: prepare_move_context
         :collapse:


   .. py:method:: run_game(visualize: bool = True, debug: bool = False)

      Execute a complete Tic Tac Toe game from start to finish.

      Runs the game workflow, optionally displaying board states and debug
      information. Returns the final game state with winner information.

      :param visualize: Whether to display board after each move.
                        Overrides config.visualize if provided.
      :type visualize: bool
      :param debug: Whether to enable debug logging for troubleshooting.
      :type debug: bool

      :returns: Final game state with winner and complete history.
      :rtype: TicTacToeState

      .. rubric:: Examples

      Standard game::

          final_state = agent.run_game()
          print(f"Winner: {final_state.winner}")

      Fast execution without visualization::

          result = agent.run_game(visualize=False)
          # Runs at maximum speed

      Debug mode::

          result = agent.run_game(debug=True)
          # Shows detailed execution logs

      Tournament execution::

          config = TicTacToeConfig.competitive_config()
          agent = TicTacToeAgent(config)
          result = agent.run_game(visualize=False, debug=False)
          # Optimized for performance


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: setup_workflow()

      Configure the LangGraph workflow for game execution.

      Creates the state graph with nodes for initialization, move generation,
      and position analysis. Sets up edges to define game flow based on
      configuration settings.

      Workflow structure:
      - initialize -> make_move: Start game and make first move
      - make_move -> analyze: Analyze if enabled
      - make_move -> make_move: Continue play without analysis
      - analyze -> make_move: Return to play after analysis
      - Any -> END: When game is complete

      .. rubric:: Examples

      Standard workflow::

          agent.setup_workflow()
          # Creates graph with all nodes

      Analysis disabled::

          agent.config.enable_analysis = False
          agent.setup_workflow()
          # Skips analyze node in practice


      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: visualize_state(state: haive.games.tic_tac_toe.state.TicTacToeState) -> None

      Visualize the current game state for interactive gameplay.

      Displays a formatted representation of the board, game status, current
      turn, and recent moves. Only shows visualization if enabled in config.

      :param state: Game state to visualize.
      :type state: TicTacToeState

      .. rubric:: Examples

      Standard visualization::

          agent.visualize_state(state)
          # Prints:
          # ==================================================
          # 🎮 Game Status: ongoing
          # Current Turn: X (player1)
          # ==================================================
          #    0 1 2
          #   -------
          # 0 |X| | |
          #   -------
          # 1 | |O| |
          #   -------
          # 2 | | | |
          #   -------
          #
          # 📝 Last Move: X places at (0, 0) - top-left corner

      Game over visualization::

          agent.visualize_state(final_state)
          # Shows final board with winner


      .. autolink-examples:: visualize_state
         :collapse:


   .. py:attribute:: state_manager


.. py:data:: logger

