"""Checkers agent implementation module.

This module provides the main checkers agent implementation using LangGraph, including:
    - Dynamic graph-based workflow for turn management
    - LLM-powered player engines for move generation
    - Position analysis and evaluation
    - Error handling and retry logic
    - Rich UI visualization
    - Game flow orchestration

The agent uses a state-based approach with LangGraph for managing the game workflow
and supports both automated play and human interaction through a beautiful UI.
"""

import sys
import time
from typing import Any

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.graph import END
from langgraph.types import Command

from haive.games.checkers.config import CheckersAgentConfig
from haive.games.checkers.models import CheckersMove, CheckersPlayerDecision
from haive.games.checkers.state import CheckersState
from haive.games.checkers.state_manager import CheckersStateManager
from haive.games.checkers.ui import CheckersUI
from haive.games.framework.base import GameAgent


@register_agent(CheckersAgentConfig)
class CheckersAgent(GameAgent[CheckersAgentConfig]):
    """Agent for playing checkers with LLM-based players and rich UI.

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

    Attributes:
        config (CheckersAgentConfig): Configuration for the checkers agent
        state_manager (CheckersStateManager): Manager for game state operations
        ui (CheckersUI): Rich UI for game visualization
        engines (dict): LLM engines for players and analyzers
        graph (DynamicGraph): LangGraph workflow for the checkers game

    Examples:
        >>> # Create and run a checkers game
        >>> agent = CheckersAgent(CheckersAgentConfig())
        >>> final_state = agent.run_game(visualize=True)
        >>>
        >>> # Check the final game state
        >>> print(f"Game winner: {final_state.get('winner')}")
    """

    def __init__(self, config: CheckersAgentConfig):
        """Initialize the checkers agent.

        Sets up the state manager, UI, and other components needed for
        the checkers game.

        Args:
            config (CheckersAgentConfig): Configuration for the checkers agent
        """
        self.state_manager = CheckersStateManager
        self.ui = CheckersUI()
        super().__init__(config)

        # Set higher recursion limit for complex games
        sys.setrecursionlimit(10000)

    def initialize_game(self, state: dict[str, Any]) -> Command:
        """Initialize a new checkers game.

        Creates a fresh checkers game state and routes to the first player's move.

        Args:
            state (dict[str, Any]): Initial state data (usually empty)

        Returns:
            Command: LangGraph command with initialized game state
        """
        game_state = self.state_manager.initialize()
        return Command(update=game_state, goto="player1_move")

    def prepare_analysis_context(
        self, state: CheckersState, player: str
    ) -> dict[str, Any]:
        """Prepare context for position analysis.

        Creates a context dictionary with all necessary information for
        the analyzer engines to evaluate a position.

        Args:
            state (CheckersState): Current game state
            player (str): Player to analyze for ("red" or "black")

        Returns:
            dict[str, Any]: Context dictionary for analysis
        """
        return {
            "board": state.board_string,
            "turn": state.turn,
            "color": player,
            "captured_red": state.captured_pieces["red"],
            "captured_black": state.captured_pieces["black"],
            "move_history": [str(move) for move in state.move_history[-5:]],
        }

    def extract_move(self, response: CheckersPlayerDecision) -> CheckersMove:
        """Extract a move from a player decision.

        Gets the selected move from a player's decision object.

        Args:
            response (CheckersPlayerDecision): Player's move decision

        Returns:
            CheckersMove: The selected move
        """
        return response.move

    def make_player1_move(self, state: dict[str, Any]) -> Command:
        """Make a move for player 1 (red).

        Handles the red player's turn, routing appropriately based on the
        current game state.

        Args:
            state (dict[str, Any]): Current game state

        Returns:
            Command: LangGraph command with updated state and next node
        """
        state_obj = (
            state if isinstance(state, CheckersState) else CheckersState(**state)
        )
        if state_obj.turn != "red":
            goto = "analyze_player1" if state_obj.turn == "black" else "player2_move"
            return Command(update=state_obj.model_dump(), goto=goto)
        return self.make_move(state_obj, "red")

    def make_player2_move(self, state: dict[str, Any]) -> Command:
        """Make a move for player 2 (black).

        Handles the black player's turn, routing appropriately based on the
        current game state.

        Args:
            state (dict[str, Any]): Current game state

        Returns:
            Command: LangGraph command with updated state and next node
        """
        state_obj = (
            state if isinstance(state, CheckersState) else CheckersState(**state)
        )
        if state_obj.turn != "black":
            goto = "analyze_player2" if state_obj.turn == "red" else "player1_move"
            return Command(update=state_obj.model_dump(), goto=goto)
        return self.make_move(state_obj, "black")

    def make_move(self, state: CheckersState, player: str) -> Command:
        """Make a move with error handling and retry logic.

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

        Args:
            state (CheckersState): Current game state
            player (str): Player to make the move ("red" or "black")

        Returns:
            Command: LangGraph command with updated state and next node
        """
        if state.turn != player:
            return Command(update=state.model_dump(), goto=f"analyze_{player}")

        engine = self.engines.get(f"{player}_player")
        if not engine:
            raise ValueError(f"Missing engine for {player}_player")

        # Show thinking animation
        self.ui.show_thinking(player)

        # Retry logic
        max_attempts = 3
        attempt = 0
        previous_error = None

        while attempt < max_attempts:
            attempt += 1

            try:
                # Get legal moves
                legal_moves = self.state_manager.get_legal_moves(state)
                if not legal_moves:
                    # No legal moves means game over
                    winner = "black" if player == "red" else "red"
                    return Command(
                        update={"game_status": "game_over", "winner": winner}, goto=END
                    )

                # Format legal moves for prompt
                formatted_legal_moves = [str(move) for move in legal_moves]

                # Build error context
                error_context = ""
                if previous_error and attempt > 1:
                    error_context = (
                        f"⚠️ PREVIOUS ATTEMPT ERROR: {previous_error}\n"
                        f"Please select a DIFFERENT move from the legal moves list.\n\n"
                    )

                # Prepare context with error info
                context = self.prepare_move_context(state, player)
                context["error_context"] = error_context

                # Get move decision
                move_decision = engine.invoke(context)
                move = self.extract_move(move_decision)

                # Validate the move
                valid_move = None
                for legal_move in legal_moves:
                    if (
                        legal_move.from_position == move.from_position
                        and legal_move.to_position == move.to_position
                    ):
                        valid_move = legal_move
                        break

                if not valid_move:
                    # Try to match by string representation
                    move_str = str(move)
                    valid_move = next(
                        (m for m in legal_moves if str(m) == move_str), None
                    )

                if valid_move:
                    # Show the move
                    self.ui.show_move(valid_move)

                    updated_state = self.state_manager.apply_move(state, valid_move)

                    # Check game status
                    if updated_state.game_status == "game_over" or updated_state.winner:
                        return Command(update=updated_state.model_dump(), goto=END)

                    # Determine next step
                    goto = "analyze_player2" if player == "red" else "analyze_player1"
                    return Command(update=updated_state.model_dump(), goto=goto)
                # Invalid move
                previous_error = (
                    f"Move '{move}' is not in legal moves. "
                    f"Legal moves are: {', '.join(formatted_legal_moves[:10])}"
                    f"{' ...' if len(formatted_legal_moves) > 10 else ''}"
                )

                if attempt < max_attempts:
                    continue
                # Use fallback after max attempts
                print(
                    f"❌ Invalid move after {max_attempts} attempts! Using first legal move."
                )
                # Apply first legal move as fallback
                legal_moves = self.state_manager.get_legal_moves(state)
                if legal_moves:
                    fallback_move = legal_moves[0]
                    self.ui.show_move(fallback_move)
                    updated_state = self.state_manager.apply_move(state, fallback_move)
                    goto = "analyze_player2" if player == "red" else "analyze_player1"
                    return Command(update=updated_state.model_dump(), goto=goto)

            except Exception as e:
                print(f"❌ Error in attempt {attempt}: {e}")
                previous_error = str(e)

                if attempt >= max_attempts:
                    # Use fallback move
                    legal_moves = self.state_manager.get_legal_moves(state)
                    if legal_moves:
                        fallback_move = legal_moves[0]
                        self.ui.show_move(fallback_move)
                        updated_state = self.state_manager.apply_move(
                            state, fallback_move
                        )

                        if (
                            updated_state.game_status == "game_over"
                            or updated_state.winner
                        ):
                            return Command(update=updated_state.model_dump(), goto=END)

                        goto = (
                            "analyze_player2" if player == "red" else "analyze_player1"
                        )
                        return Command(update=updated_state.model_dump(), goto=goto)
                    return Command(update={"game_status": "game_over"}, goto=END)

    def prepare_move_context(self, state: CheckersState, player: str) -> dict[str, Any]:
        """Prepare context for move generation.

        Creates a context dictionary with all necessary information for
        the player engines to make a move decision.

        Args:
            state (CheckersState): Current game state
            player (str): Player to make the move ("red" or "black")

        Returns:
            dict[str, Any]: Context dictionary for move generation
        """
        legal_moves = self.state_manager.get_legal_moves(state)
        formatted_legal_moves = [str(move) for move in legal_moves]

        # Get latest analysis
        player_analysis = None
        if player == "red" and state.red_analysis:
            player_analysis = state.red_analysis[-1]
        elif player == "black" and state.black_analysis:
            player_analysis = state.black_analysis[-1]

        # Format analysis for prompt
        analysis_str = "No previous analysis"
        if player_analysis:
            analysis_str = (
                f"Material: {player_analysis.material_advantage}, "
                f"Center: {player_analysis.control_of_center}, "
                f"Position: {player_analysis.positional_evaluation}"
            )

        return {
            "board": state.board_string,
            "turn": state.turn,
            "color": player,
            "legal_moves": ", ".join(formatted_legal_moves),  # Join as string
            "captured_red": len(state.captured_pieces["red"]),
            "captured_black": len(state.captured_pieces["black"]),
            "move_history": ", ".join(str(m) for m in state.move_history[-50:]),
            "player_analysis": analysis_str,
            "error_context": "",  # Will be filled by retry logic
        }

    def analyze_player1(self, state: dict[str, Any]) -> Command:
        """Analyze the position for player 1 (red).

        Handles position analysis for the red player.

        Args:
            state (dict[str, Any]): Current game state

        Returns:
            Command: LangGraph command with updated state and next node
        """
        state_obj = (
            state if isinstance(state, CheckersState) else CheckersState(**state)
        )
        if state_obj.turn != "red":
            return Command(update=state_obj.model_dump(), goto="player1_move")
        return self.analyze_position(state_obj, "red")

    def analyze_player2(self, state: dict[str, Any]) -> Command:
        """Analyze the position for player 2 (black).

        Handles position analysis for the black player.

        Args:
            state (dict[str, Any]): Current game state

        Returns:
            Command: LangGraph command with updated state and next node
        """
        state_obj = (
            state if isinstance(state, CheckersState) else CheckersState(**state)
        )
        if state_obj.turn != "black":
            return Command(update=state_obj.model_dump(), goto="player2_move")
        return self.analyze_position(state_obj, "black")

    def analyze_position(self, state: CheckersState, player: str) -> Command:
        """Analyze the position for a player.

        Gets a detailed position analysis from the appropriate analyzer engine
        and updates the game state with the analysis.

        Args:
            state (CheckersState): Current game state
            player (str): Player to analyze for ("red" or "black")

        Returns:
            Command: LangGraph command with updated state and next node
        """
        if state.turn != player:
            return Command(update=state.model_dump(), goto=f"{player}_move")

        context = self.prepare_analysis_context(state, player)
        engine = self.engines.get(f"{player}_analyzer")
        if not engine:
            raise ValueError(f"Missing engine for {player}_analyzer")

        try:
            analysis = engine.invoke(context)
            updated_state = self.state_manager.update_analysis(state, analysis, player)
        except Exception as e:
            print(f"Error during analysis: {e}")
            # Create a default analysis to keep the game going
            from haive.games.checkers.models import CheckersAnalysis

            default_analysis = CheckersAnalysis(
                material_advantage="Error occurred during analysis",
                control_of_center="Game continues with default analysis",
                suggested_moves=["Continue play"],
                positional_evaluation="Position unclear due to analysis error",
            )
            updated_state = self.state_manager.update_analysis(
                state, default_analysis, player
            )

        return Command(update=updated_state.model_dump(), goto=f"{player}_move")

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Use the rich UI to visualize the current game state.

        Displays the current board, game info, move history, and other
        visual elements using the rich UI.

        Args:
            state (dict[str, Any]): Current game state
        """
        checker_state = (
            state if isinstance(state, CheckersState) else CheckersState(**state)
        )
        self.ui.display_state(checker_state)

        # Check for game over
        if checker_state.game_status == "game_over":
            self.ui.show_game_over(checker_state)

    def run_game_with_ui(self) -> dict[str, Any]:
        """Run game with beautiful UI visualization.

        Runs a complete checkers game with rich UI visualization,
        streaming the state updates and displaying them in real-time.

        Returns:
            dict[str, Any]: Final game state

        Examples:
            >>> agent = CheckersAgent(CheckersAgentConfig())
            >>> final_state = agent.run_game_with_ui()
            >>> print(f"Winner: {final_state.get('winner')}")
        """
        initial_state = self.state_manager.initialize()

        # Create runnable config with significantly increased recursion limit
        config = {
            "configurable": {"recursion_limit": 10000, "thread_id": "checkers_game"}
        }

        try:
            # Display initial state
            self.ui.display_state(initial_state)
            time.sleep(2)

            for step in self.app.stream(
                initial_state.model_dump(), stream_mode="values", config=config
            ):
                self.visualize_state(step)

            return step
        except Exception as e:
            print(f"Error running game: {e}")
            return {}

    def run_game(self, visualize: bool = True) -> dict[str, Any]:
        """Run the checkers game.

        Runs a complete checkers game with optional visualization.

        Args:
            visualize (bool, optional): Whether to show the UI. Defaults to True.

        Returns:
            dict[str, Any]: Final game state

        Examples:
            >>> agent = CheckersAgent(CheckersAgentConfig())
            >>> # Run with visualization
            >>> final_state = agent.run_game(visualize=True)
            >>> # Run without visualization
            >>> final_state = agent.run_game(visualize=False)
        """
        if visualize:
            return self.run_game_with_ui()
        # Create runnable config with significantly increased recursion limit
        config = {
            "configurable": {"recursion_limit": 10000, "thread_id": "checkers_game"}
        }
        return self.run({}, config=config)

    def setup_workflow(self) -> None:
        """Set up the workflow graph for the checkers game.

        Creates a LangGraph workflow with nodes for initialization, moves,
        and analysis, with appropriate edges between them.

        The graph flow follows this pattern:
        initialize → player1_move → analyze_player2 → player2_move → analyze_player1 → loop
        """
        gb = DynamicGraph(
            components=[self.config], state_schema=self.config.state_schema
        )

        gb.add_node("initialize", self.initialize_game)
        gb.set_entry_point("initialize")
        gb.add_node("player1_move", self.make_player1_move)
        gb.add_node("player2_move", self.make_player2_move)
        gb.add_node("analyze_player1", self.analyze_player1)
        gb.add_node("analyze_player2", self.analyze_player2)
        gb.add_edge("initialize", "player1_move")
        gb.add_edge("player1_move", "analyze_player2")
        gb.add_edge("analyze_player2", "player2_move")
        gb.add_edge("player2_move", "analyze_player1")
        gb.add_edge("analyze_player1", "player1_move")
        self.graph = gb.build()
