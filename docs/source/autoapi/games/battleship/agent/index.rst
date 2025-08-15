games.battleship.agent
======================

.. py:module:: games.battleship.agent

.. autoapi-nested-parse::

   Battleship game agent implementation.

   This module implements the main agent for the Battleship game, including:
       - LangGraph workflow for game logic
       - Turn-based gameplay management
       - LLM-powered player actions
       - Game state transitions
       - Ship placement and move execution


   .. autolink-examples:: games.battleship.agent
      :collapse:


Attributes
----------

.. autoapisummary::

   games.battleship.agent.logger


Classes
-------

.. autoapisummary::

   games.battleship.agent.BattleshipAgent


Module Contents
---------------

.. py:class:: BattleshipAgent(config: haive.games.battleship.config.BattleshipAgentConfig)

   Bases: :py:obj:`haive.core.engine.agent.agent.Agent`\ [\ :py:obj:`haive.games.battleship.config.BattleshipAgentConfig`\ ]


   Battleship game agent with LLM-powered players.

   This agent implements a complete Battleship game with:
   - LLM-powered ship placement strategy
   - Turn-based gameplay with move validation
   - Strategic analysis of board state
   - Game state tracking and persistence
   - Visualization options

   The agent uses LangGraph for workflow management and supports
   configurable LLM engines for different game actions.

   .. attribute:: state_manager

      Manager for game state transitions

      :type: BattleshipStateManager

   .. attribute:: engines

      LLM engine configurations for different game actions

      :type: dict

   .. attribute:: config

      Agent configuration

      :type: BattleshipAgentConfig

   .. attribute:: graph

      LangGraph workflow

      :type: Graph

   .. rubric:: Examples

   >>> config = BattleshipAgentConfig()
   >>> agent = BattleshipAgent(config)
   >>> result = agent.run_game(visualize=True)

   Initialize the Battleship agent.

   :param config: Configuration for the agent


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BattleshipAgent
      :collapse:

   .. py:method:: _find_valid_move(state: haive.games.battleship.state.BattleshipState, player: str) -> haive.games.battleship.models.MoveCommand

      Find a valid move when the LLM fails to provide one.

      Implements a deterministic fallback strategy for selecting a move
      when the LLM fails to generate a valid one, prioritizing:
      1. Cells adjacent to known hits (to finish sinking partially hit ships)
      2. Unexplored cells in a systematic scan
      3. Random selection as a last resort

      :param state: Current game state
      :param player: Player for whom to find a move

      :returns: A valid move command
      :rtype: MoveCommand


      .. autolink-examples:: _find_valid_move
         :collapse:


   .. py:method:: analyze_position(state: dict[str, Any], player: str) -> langgraph.types.Command

      Analyze game state and generate strategic insights.

      Uses the player's analyzer engine to generate strategic analysis
      of the current game state, which helps inform move decisions.

      :param state: Current game state
      :param player: Player for whom to generate analysis

      :returns: LangGraph command with updated state and next node
      :rtype: Command

      .. note::

         If an error occurs during analysis, it's logged but doesn't
         stop the game - control flows to the player's move node.


      .. autolink-examples:: analyze_position
         :collapse:


   .. py:method:: check_game_over(state: dict[str, Any]) -> langgraph.types.Command

      Check if the game is over and update game state accordingly.

      This node checks for game-ending conditions (all ships of a player
      being sunk) and updates the game state with the winner if the game
      is over.

      :param state: Current game state

      :returns: LangGraph command with updated state and next node
      :rtype: Command


      .. autolink-examples:: check_game_over
         :collapse:


   .. py:method:: check_game_status(state: dict[str, Any]) -> langgraph.types.Command

      Check the game status after a move.

      Assesses whether the game is over, updates the winner if needed,
      and determines the next player's turn.

      :param state: Current game state

      :returns: LangGraph command with updated state and next node
      :rtype: Command


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: ensure_state(state: Any) -> haive.games.battleship.state.BattleshipState

      Ensure that state is a proper BattleshipState instance.

      Converts dictionary representations to BattleshipState objects
      to ensure type safety throughout the agent.

      :param state: State object or dictionary

      :returns: Properly typed state object
      :rtype: BattleshipState

      .. rubric:: Examples

      >>> agent = BattleshipAgent(BattleshipAgentConfig())
      >>> state_dict = {"game_phase": "setup", "current_player": "player1"}
      >>> state_obj = agent.ensure_state(state_dict)
      >>> isinstance(state_obj, BattleshipState)
      True


      .. autolink-examples:: ensure_state
         :collapse:


   .. py:method:: initialize_game(state: dict[str, Any]) -> langgraph.types.Command

      Initialize a new Battleship game.

      Creates a fresh game state and starts the setup phase
      for ship placement.

      :param state: Initial state (usually empty)

      :returns: LangGraph command with initialized state
      :rtype: Command


      .. autolink-examples:: initialize_game
         :collapse:


   .. py:method:: make_move(state: dict[str, Any], player: str, next_node: str = 'check_game_over') -> langgraph.types.Command

      Make an attack move for a player.

      Uses the player's move engine to generate an attack coordinate,
      validates it, and updates the game state with the result.

      :param state: Current game state
      :param player: Player making the move
      :param next_node: Next node to route to after the move

      :returns: LangGraph command with updated state and next node
      :rtype: Command

      :raises ValueError: If the required engine is missing

      .. note::

         If the LLM fails to generate a valid move, a fallback move is
         generated using a deterministic strategy.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: place_ships(state: dict[str, Any], player: str) -> langgraph.types.Command

      Generate strategic ship placements for a player.

      Uses the player's ship placement engine to generate optimal placements
      for all ships, validates them, and updates the game state.

      :param state: Current game state
      :param player: Player for whom to place ships

      :returns: LangGraph command with updated state and next node
      :rtype: Command

      :raises ValueError: If the required engine is missing

      .. note:: If an error occurs during placement, the game is reinitialized.


      .. autolink-examples:: place_ships
         :collapse:


   .. py:method:: place_ships_player1(state: dict[str, Any]) -> langgraph.types.Command

      Place ships for player 1.

      Delegates to the common place_ships method for player1.

      :param state: Current game state

      :returns: LangGraph command with updated state
      :rtype: Command


      .. autolink-examples:: place_ships_player1
         :collapse:


   .. py:method:: place_ships_player2(state: dict[str, Any]) -> langgraph.types.Command

      Place ships for player 2.

      Delegates to the common place_ships method for player2.

      :param state: Current game state

      :returns: LangGraph command with updated state
      :rtype: Command


      .. autolink-examples:: place_ships_player2
         :collapse:


   .. py:method:: player1_analysis(state: dict[str, Any]) -> langgraph.types.Command

      Analyze position for player 1.

      Delegates to the common analyze_position method for player1.

      :param state: Current game state

      :returns: LangGraph command with updated state
      :rtype: Command


      .. autolink-examples:: player1_analysis
         :collapse:


   .. py:method:: player1_move(state: dict[str, Any]) -> langgraph.types.Command

      Make a move for player 1.

      Delegates to the common make_move method for player1.

      :param state: Current game state

      :returns: LangGraph command with updated state
      :rtype: Command


      .. autolink-examples:: player1_move
         :collapse:


   .. py:method:: player2_analysis(state: dict[str, Any]) -> langgraph.types.Command

      Analyze position for player 2.

      Delegates to the common analyze_position method for player2.

      :param state: Current game state

      :returns: LangGraph command with updated state
      :rtype: Command


      .. autolink-examples:: player2_analysis
         :collapse:


   .. py:method:: player2_move(state: dict[str, Any]) -> langgraph.types.Command

      Make a move for player 2.

      Delegates to the common make_move method for player2.

      :param state: Current game state

      :returns: LangGraph command with updated state
      :rtype: Command


      .. autolink-examples:: player2_move
         :collapse:


   .. py:method:: run_game(visualize: bool = True) -> dict[str, Any]

      Run a complete Battleship game with comprehensive state tracking.

      Executes the full game workflow from initialization through ship
      placement and gameplay to completion. Provides detailed game state
      tracking, error handling, and optional console visualization for
      monitoring game progress and debugging.

      The method handles all phases of Battleship gameplay:
      - Game initialization and state setup
      - Ship placement for both players
      - Turn-based combat with move validation
      - Game termination and winner determination
      - Comprehensive error handling and recovery

      :param visualize: Whether to display detailed game progress in console.
                        When True, shows turn-by-turn updates, board statistics, move history,
                        and error messages. When False, runs silently and returns final state.
      :type visualize: bool

      :returns:

                Final game state dictionary containing:
                    - winner: Winning player identifier or None
                    - game_phase: Final phase (typically "ended")
                    - move_history: Complete record of all moves made
                    - player1_state/player2_state: Final player board states
                    - error_message: Any error that occurred during gameplay
      :rtype: dict[str, Any]

      :raises RuntimeError: If the game workflow fails to compile or execute properly.
      :raises ConfigurationError: If the agent configuration is invalid.

      .. rubric:: Examples

      Running a visualized game for debugging::\n

          agent = BattleshipAgent(BattleshipAgentConfig())
          result = agent.run_game(visualize=True)

          # Console output shows:
          # --- GAME STATE (Step 1) ---
          # Turn: player1
          # Phase: setup
          # Player 1 placed ships: False
          # Player 2 placed ships: False
          #
          # --- GAME STATE (Step 2) ---
          # Turn: player1
          # Phase: playing
          # Player 1 Hits: 0, Ships Sunk: 0
          # Player 2 Hits: 0, Ships Sunk: 0
          #
          # 🎮 GAME OVER! Winner: player1 🎮

      Running a silent game for automated testing::\n

          agent = BattleshipAgent(BattleshipAgentConfig())
          result = agent.run_game(visualize=False)

          winner = result.get("winner")
          if winner:
              print(f"Game completed, winner: {winner}")

      Handling game errors gracefully::\n

          try:
              result = agent.run_game(visualize=True)
              if result.get("error_message"):
                  print(f"Game error: {result['error_message']}")
                  # Could retry with different configuration
          except Exception as e:
              print(f"Critical game failure: {e}")

      Analyzing game performance::\n

          result = agent.run_game(visualize=False)

          # Extract performance metrics
          move_history = result.get("move_history", [])
          total_moves = len(move_history)

          p1_state = result.get("player1_state", {})
          p1_hits = len(p1_state.get("board", {}).get("successful_hits", []))
          hit_rate = p1_hits / total_moves if total_moves > 0 else 0

          print(f"Game completed in {total_moves} moves")
          print(f"Player 1 hit rate: {hit_rate:.2%}")

      .. note::

         The visualization mode provides detailed game state information that is
         valuable for debugging agent behavior, understanding game flow, and
         monitoring performance. Silent mode is optimized for automated testing
         and batch game execution.


      .. autolink-examples:: run_game
         :collapse:


   .. py:method:: setup_workflow()

      Set up the workflow for the Battleship game.

      Creates a LangGraph workflow with nodes for:
      - Game initialization
      - Ship placement for both players
      - Move selection
      - Strategic analysis (if enabled)
      - Turn switching
      - Game over checking

      The workflow includes conditional routing based on game state
      and supports different paths depending on whether analysis is enabled.



      .. autolink-examples:: setup_workflow
         :collapse:


   .. py:method:: switch_to_player1(state: dict[str, Any]) -> langgraph.types.Command

      Switch to player 1's turn.

      Updates the current player to player1 and routes to the appropriate
      next node based on configuration (analysis or move).

      :param state: Current game state

      :returns: LangGraph command with updated state and next node
      :rtype: Command


      .. autolink-examples:: switch_to_player1
         :collapse:


   .. py:method:: switch_to_player2(state: dict[str, Any]) -> langgraph.types.Command

      Switch to player 2's turn.

      Updates the current player to player2 and routes to the appropriate
      next node based on configuration (analysis or move).

      :param state: Current game state

      :returns: LangGraph command with updated state and next node
      :rtype: Command


      .. autolink-examples:: switch_to_player2
         :collapse:


   .. py:attribute:: engines


   .. py:attribute:: state_manager


.. py:data:: logger

