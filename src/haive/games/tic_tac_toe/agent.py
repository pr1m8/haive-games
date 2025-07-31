"""Comprehensive agent implementation for strategic Tic Tac Toe gameplay.

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

Examples:
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

Note:
    The agent uses LangGraph for workflow management and supports
    concurrent execution with proper state reducers.

"""

import logging
import time
import traceback
from typing import Any

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.graph import END
from langgraph.types import Command

from haive.games.framework.base.agent import GameAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.state import TicTacToeState
from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager

logger = logging.getLogger(__name__)


@register_agent(TicTacToeConfig)
class TicTacToeAgent(GameAgent[TicTacToeConfig]):
    """Strategic agent for Tic Tac Toe gameplay with LLM-driven decision- making.

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

    Attributes:
        config (TicTacToeConfig): Game configuration parameters.
        state_manager (TicTacToeStateManager): State management system.
        engines (Dict[str, Engine]): LLM engines for players and analysis.
        graph (StateGraph): LangGraph workflow for game execution.

    Examples:
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

    """

    def __init__(self, config: TicTacToeConfig = TicTacToeConfig()):
        """Initialize the Tic Tac Toe agent with configuration.

        Sets up the agent with the provided configuration, initializes the
        state manager, and prepares the workflow graph for game execution.

        Args:
            config (TicTacToeConfig): Game configuration with engine settings,
                analysis options, and gameplay parameters.

        Examples:
            Default initialization::

                agent = TicTacToeAgent()
                # Uses default configuration

            Custom configuration::

                config = TicTacToeConfig(
                    enable_analysis=True,
                    visualize=True
                )
                agent = TicTacToeAgent(config)

        """
        self.state_manager = TicTacToeStateManager
        super().__init__(config)

    def initialize_game(self, state: dict[str, Any]) -> Command:
        """Initialize a new Tic Tac Toe game with starting configuration.

        Creates the initial game state with an empty board, assigns players
        to symbols based on configuration, and sets up the first turn.

        Args:
            state (dict[str, Any]): Initial state dictionary (typically empty).

        Returns:
            Command: LangGraph command with initialized state and next node.

        Examples:
            Standard initialization::

                command = agent.initialize_game({})
                # Returns Command with empty board, X to play

            Custom first player::

                agent.config.first_player = "O"
                command = agent.initialize_game({})
                # Returns Command with O to play first

        """
        logger.debug("initialize_game called")

        game_state = self.state_manager.initialize(
            first_player=self.config.first_player,
            player_X=self.config.player_X,
            player_O=self.config.player_O,
        )

        logger.debug(
            "Game state initialized",
            extra={
                "turn": game_state.turn,
                "status": game_state.game_status,
                "board": game_state.board,
            },
        )

        # Return only the essential fields for initialization
        return Command(
            update={
                "board": game_state.board,
                "turn": game_state.turn,
                "game_status": game_state.game_status,
                "player_X": game_state.player_X,
                "player_O": game_state.player_O,
                "winner": game_state.winner,
                "error_message": game_state.error_message,
                # Don't include lists that might cause issues
            },
            goto="make_move",
        )

    def prepare_move_context(self, state: TicTacToeState) -> dict[str, Any]:
        r"""Prepare structured context for LLM move generation.

        Creates a comprehensive context dictionary containing the current board
        state, legal moves, and previous analysis to enable informed decision-making
        by the LLM engine.

        Args:
            state (TicTacToeState): Current game state with board and history.

        Returns:
            dict[str, Any]: Context dictionary with board representation,
                legal moves, current player, and analysis history.

        Examples:
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

        """
        legal_moves = self.state_manager.get_legal_moves(state)
        formatted_legal_moves = ", ".join(
            [f"({move.row}, {move.col})" for move in legal_moves]
        )

        current_player = (
            "player1"
            if (state.turn == "X" and state.player_X == "player1")
            or (state.turn == "O" and state.player_O == "player1")
            else "player2"
        )

        player_analysis = "No previous analysis available."
        if current_player == "player1" and state.player1_analysis:
            player_analysis = state.player1_analysis[-1]
        elif current_player == "player2" and state.player2_analysis:
            player_analysis = state.player2_analysis[-1]

        return {
            "board_string": state.board_string,
            "current_player": state.turn,
            "legal_moves": formatted_legal_moves,
            "player_analysis": player_analysis,
        }

    def prepare_analysis_context(
        self, state: TicTacToeState, symbol: str
    ) -> dict[str, Any]:
        """Prepare structured context for strategic position analysis.

        Creates a context dictionary for the analysis engine containing the
        current board state and player information for strategic evaluation.

        Args:
            state (TicTacToeState): Current game state to analyze.
            symbol (str): Symbol ('X' or 'O') of the player to analyze for.

        Returns:
            dict[str, Any]: Analysis context with board state and player symbols.

        Examples:
            Analysis for X player::

                context = agent.prepare_analysis_context(state, "X")
                # Returns: {
                #     'board_string': '...',
                #     'player_symbol': 'X',
                #     'opponent_symbol': 'O'
                # }

        """
        return {
            "board_string": state.board_string,
            "player_symbol": symbol,
            "opponent_symbol": "O" if symbol == "X" else "X",
        }

    def make_move(self, state) -> Command:
        """Generate and execute a move for the current player.

        Uses the appropriate LLM engine to generate a move for the current player,
        validates the move, updates the game state, and determines the next step
        in the workflow based on game status and configuration.

        Args:
            state: Current game state (dict or TicTacToeState).

        Returns:
            Command: LangGraph command with state updates and next node.

        Raises:
            Exception: If move generation or application fails.

        Examples:
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

        """
        logger.debug("make_move called", extra={"state_type": type(state).__name__})

        # Convert dict to TicTacToeState if needed
        if isinstance(state, dict):
            try:
                game_state = TicTacToeState(**state)
                logger.debug(
                    "Converted dict to TicTacToeState successfully",
                    extra={
                        "turn": game_state.turn,
                        "status": game_state.game_status,
                        "board": game_state.board,
                    },
                )
            except Exception as e:
                logger.error("State conversion failed", extra={"error": str(e)})
                return Command(
                    update={"error_message": f"State conversion failed: {e!s}"},
                    goto=END,
                )
        else:
            game_state = state
            logger.debug("Using state directly")

        if game_state.game_status != "ongoing":
            logger.debug("Game not ongoing", extra={"status": game_state.game_status})
            return Command(update={}, goto=END)

        # Determine which engine to use based on current player
        if game_state.turn == "X":
            engine = self.engines["X_player"]
            engine_name = "X_player"
        else:
            engine = self.engines["O_player"]
            engine_name = "O_player"

        logger.debug(
            "Using engine for turn",
            extra={"engine": engine_name, "turn": game_state.turn},
        )

        try:
            context = self.prepare_move_context(game_state)
            print(f"[DEBUG] Prepared context keys: {list(context.keys())}")

            print("[DEBUG] Invoking engine...")
            move = engine.invoke(context)
            print(f"[DEBUG] Engine returned move: {move}")
            print(f"[DEBUG] Move type: {type(move)}")

            print("[DEBUG] Applying move...")
            new_state = self.state_manager.apply_move(game_state, move)
            print("[DEBUG] Move applied successfully")
            print(f"[DEBUG] New board: {new_state.board}")
            print(f"[DEBUG] New turn: {new_state.turn}")
            print(f"[DEBUG] New status: {new_state.game_status}")

            # Determine next node
            if new_state.game_status != "ongoing":
                next_node = END
            elif self.config.enable_analysis:
                next_node = "analyze"
            else:
                next_node = "make_move"

            print(f"[DEBUG] Next node: {next_node}")

            # Create targeted updates that work with our reducers
            update = {
                "board": new_state.board,  # Replace board
                "turn": new_state.turn,  # Replace turn
                "game_status": new_state.game_status,  # Replace status
                "winner": new_state.winner,  # Replace winner
                "move_history": [move],  # Add to move history
            }

            print(f"[DEBUG] Update dict: {update}")

            return Command(update=update, goto=next_node)

        except Exception as e:
            logger.error("Error in make_move", extra={"error": str(e)}, exc_info=True)

            traceback.print_exc()
            return Command(update={"error_message": f"Move failed: {e!s}"}, goto=END)

    def analyze_position(self, state) -> Command:
        """Analyze the board position for strategic insights.

        Performs strategic analysis of the current board position for the player
        who just moved, providing insights about threats, opportunities, and
        optimal play. Analysis is only performed if enabled in configuration.

        Args:
            state: Current game state (dict or TicTacToeState).

        Returns:
            Command: LangGraph command with analysis results and next node.

        Examples:
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

        """
        logger.debug("analyze_position called")

        # Convert dict to TicTacToeState if needed
        if isinstance(state, dict):
            try:
                game_state = TicTacToeState(**state)
            except Exception as e:
                return Command(
                    update={"error_message": f"State conversion failed: {e!s}"},
                    goto=END,
                )
        else:
            game_state = state

        if not self.config.enable_analysis or game_state.game_status != "ongoing":
            return Command(
                update={},
                goto="make_move" if game_state.game_status == "ongoing" else END,
            )

        # Analyze for the player who just moved (opposite of current turn)
        last_player = "O" if game_state.turn == "X" else "X"

        try:
            if last_player == "X":
                engine = self.engines["X_analyzer"]
                player_name = game_state.player_X
            else:
                engine = self.engines["O_analyzer"]
                player_name = game_state.player_O

            context = self.prepare_analysis_context(game_state, last_player)
            analysis = engine.invoke(context)

            print(f"[DEBUG] Analysis completed for {player_name}")

            # Determine next step
            next_node = "make_move" if game_state.game_status == "ongoing" else END

            # Add analysis to appropriate player using the accumulating reducer
            update = {}
            if player_name == "player1":
                update["player1_analysis"] = [analysis]
            else:
                update["player2_analysis"] = [analysis]

            return Command(update=update, goto=next_node)

        except Exception as e:
            logger.error(
                "Error in analyze_position", extra={"error": str(e)}, exc_info=True
            )
            return Command(
                update={"error_message": f"Analysis failed: {e!s}"},
                goto="make_move" if game_state.game_status == "ongoing" else END,
            )

    def visualize_state(self, state: TicTacToeState) -> None:
        """Visualize the current game state for interactive gameplay.

        Displays a formatted representation of the board, game status, current
        turn, and recent moves. Only shows visualization if enabled in config.

        Args:
            state (TicTacToeState): Game state to visualize.

        Examples:
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

        """
        if not self.config.visualize:
            return

        try:
            game_state = TicTacToeState(**state)
            print("\n" + "=" * 50)
            print(f"🎮 Game Status: {game_state.game_status}")
            if game_state.game_status == "ongoing":
                current_player = (
                    game_state.player_X
                    if game_state.turn == "X"
                    else game_state.player_O
                )
                print(f"Current Turn: {game_state.turn} ({current_player})")
            print("=" * 50)
            print(game_state.board_string)

            if game_state.move_history:
                last_move = game_state.move_history[-1]
                print(f"\n📝 Last Move: {last_move}")

            if game_state.error_message:
                print(f"\n⚠️ Error: {game_state.error_message}")

            time.sleep(0.5)

        except Exception as e:
            print(f"Error in visualize_state: {e}")

    def setup_workflow(self):
        """Configure the LangGraph workflow for game execution.

        Creates the state graph with nodes for initialization, move generation,
        and position analysis. Sets up edges to define game flow based on
        configuration settings.

        Workflow structure:
        - initialize -> make_move: Start game and make first move
        - make_move -> analyze: Analyze if enabled
        - make_move -> make_move: Continue play without analysis
        - analyze -> make_move: Return to play after analysis
        - Any -> END: When game is complete

        Examples:
            Standard workflow::

                agent.setup_workflow()
                # Creates graph with all nodes

            Analysis disabled::

                agent.config.enable_analysis = False
                agent.setup_workflow()
                # Skips analyze node in practice

        """
        builder = DynamicGraph(state_schema=self.state_schema)

        # Add nodes
        builder.add_node("initialize", self.initialize_game)
        builder.add_node("make_move", self.make_move)
        builder.add_node("analyze", self.analyze_position)

        # Set entry point
        builder.set_entry_point("initialize")

        # Add explicit edges
        builder.add_edge("initialize", "make_move")
        # Self-loop for continuous play
        builder.add_edge("make_move", "make_move")
        # For when analysis is enabled
        builder.add_edge("make_move", "analyze")
        builder.add_edge("analyze", "make_move")  # Back to move after analysis

        self.graph = builder.build()

    def run_game(self, visualize: bool = True, debug: bool = False):
        """Execute a complete Tic Tac Toe game from start to finish.

        Runs the game workflow, optionally displaying board states and debug
        information. Returns the final game state with winner information.

        Args:
            visualize (bool): Whether to display board after each move.
                Overrides config.visualize if provided.
            debug (bool): Whether to enable debug logging for troubleshooting.

        Returns:
            TicTacToeState: Final game state with winner and complete history.

        Examples:
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

        """
        initial_state = TicTacToeStateManager.initialize(
            first_player=self.config.first_player,
            player_X=self.config.player_X,
            player_O=self.config.player_O,
        )

        # Run the game
        if visualize:
            for step in self.app.stream(
                initial_state,
                stream_mode="values",
                debug=debug,
                config=self.runnable_config,
            ):
                self.visualize_state(step)
                time.sleep(1)
            return step  # Final state

        return super().run(initial_state, debug=debug)
