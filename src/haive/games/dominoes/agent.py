import json
import logging
import time
from typing import Any, Literal

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.graph import END
from langgraph.types import Command
from rich.console import Console
from rich.live import Live

from haive.games.dominoes.config import DominoesAgentConfig
from haive.games.dominoes.models import (
    DominoesAnalysis,
    DominoesPlayerDecision,
    DominoMove,
)
from haive.games.dominoes.state import DominoesState
from haive.games.dominoes.state_manager import DominoesStateManager
from haive.games.dominoes.ui import DominoesUI
from haive.games.framework.base.agent import GameAgent

# Import the UI module
try:
    UI_AVAILABLE = True
except ImportError:
    UI_AVAILABLE = False

logger = logging.getLogger(__name__)


@register_agent(DominoesAgentConfig)
class DominoesAgent(GameAgent[DominoesAgentConfig]):
    """Agent for playing dominoes."""

    def __init__(self, config: DominoesAgentConfig | None = None):
        # Use default config if not provided
        if config is None:
            config = DominoesAgentConfig()

        # Set state manager
        self.state_manager = DominoesStateManager
        super().__init__(config)

        # Initialize UI if available
        self.console = Console()
        self.ui = DominoesUI(self.console) if UI_AVAILABLE else None
        if not UI_AVAILABLE:
            logger.warning("Rich UI not available - falling back to text output")

    def initialize_game(self, state: dict[str, Any]) -> Command:
        """Initialize a new Dominoes game.

        Args:
            state (Dict[str, Any]): The initial state.

        Returns:
            Command: Command with updated state.

        """
        game_state = self.state_manager.initialize()
        return Command(update=game_state, goto="player1_move")

    def prepare_move_context(self, state: DominoesState, player: str) -> dict[str, Any]:
        """Prepare context for move generation."""
        legal_moves = self.state_manager.get_legal_moves(state)
        formatted_legal_moves = [str(move) for move in legal_moves]

        hand = state.hands[player]
        formatted_hand = [str(tile) for tile in hand]

        player_analysis = None
        if player == "player1" and state.player1_analysis:
            player_analysis = state.player1_analysis[-1]
        elif player == "player2" and state.player2_analysis:
            player_analysis = state.player2_analysis[-1]

        pip_count = sum(tile.left + tile.right for tile in hand)

        return {
            "player": player,
            "hand": formatted_hand,
            "pip_count": pip_count,
            "board": state.board_string,
            "open_ends": [state.left_value, state.right_value] if state.board else [],
            "legal_moves": formatted_legal_moves,
            "boneyard_count": len(state.boneyard),
            "opponent_count": {
                p: len(state.hands[p]) for p in state.players if p != player
            },
            "move_history": state.move_history[-5:],
            "player_analysis": player_analysis,
        }

    def make_player1_move(self, state: DominoesState) -> Command:
        """Make a move for player1.

        Args:
            state (DominoesState): The current game state.

        Returns:
            Command: Command with updated state.

        """
        # Ensure we have a DominoesState object
        if isinstance(state, dict):
            try:
                state = DominoesState.model_validate(state)
            except Exception as e:
                logger.exception(f"Error converting dict to DominoesState: {e}")
                # Return a minimal Command to avoid crashing
                return Command(update=state, goto="player2_move")

        # Only make a move if it's player1's turn
        if state.turn != "player1":
            # If it's not player1's turn, just pass through the state
            goto = "analyze_player1" if state.turn == "player2" else "player2_move"
            return Command(update=state, goto=goto)

        return self.make_move(state, "player1")

    def make_player2_move(self, state: DominoesState) -> Command:
        """Make a move for player2.

        Args:
            state (DominoesState): The current game state.

        Returns:
            Command: Command with updated state.

        """
        # Ensure we have a DominoesState object
        if isinstance(state, dict):
            try:
                state = DominoesState.model_validate(state)
            except Exception as e:
                logger.exception(f"Error converting dict to DominoesState: {e}")
                # Return a minimal Command to avoid crashing
                return Command(update=state, goto="player1_move")

        # Only make a move if it's player2's turn
        if state.turn != "player2":
            # If it's not player2's turn, just pass through the state
            goto = "analyze_player2" if state.turn == "player1" else "player1_move"
            return Command(update=state, goto=goto)

        return self.make_move(state, "player2")

    def make_move(self, state: DominoesState, player: str) -> Command:
        """Make a move for the specified player.

        Args:
            state (DominoesState): The current game state.
            player (str): The player to make the move for.

        Returns:
            Command: Command with updated state.

        """
        # Ensure we have a DominoesState object
        if isinstance(state, dict):
            try:
                state = DominoesState.model_validate(state)
            except Exception as e:
                logger.exception(
                    f"Error converting dict to DominoesState in make_move: {e}"
                )
                # Return a minimal Command to avoid crashing
                goto = "analyze_player2" if player == "player1" else "analyze_player1"
                return Command(update=state, goto=goto)

        # Make sure it's the player's turn
        if state.turn != player:
            # If it's not this player's turn, just pass through to the
            # appropriate next node
            goto = f"analyze_{player}"
            return Command(update=state, goto=goto)

        # Prepare context for the move
        context = self.prepare_move_context(state, player)

        # Select the appropriate engine
        engine_key = f"{player}_player"
        engine = self.engines[engine_key]

        # Generate move
        try:
            move_decision = engine.invoke(context)
            move = self.extract_move(move_decision)

            # Validate the move
            legal_moves = self.state_manager.get_legal_moves(state)

            # If move is "pass", it's always valid if returned by
            # get_legal_moves
            if move == "pass" and "pass" in legal_moves:
                updated_state = self.state_manager.apply_move(state, move)
            # Otherwise, need to find a matching legal move
            elif move != "pass":
                # Find matching legal move
                valid_move = None
                for legal_move in legal_moves:
                    if legal_move == "pass":
                        continue

                    # Check if tiles match (regardless of orientation)
                    if (
                        (
                            legal_move.tile.left == move.tile.left
                            and legal_move.tile.right == move.tile.right
                        )
                        or (
                            legal_move.tile.left == move.tile.right
                            and legal_move.tile.right == move.tile.left
                        )
                    ) and legal_move.location == move.location:
                        valid_move = legal_move
                        break

                if valid_move:
                    updated_state = self.state_manager.apply_move(state, valid_move)
                else:
                    # If no valid move found, use the first legal move
                    fallback_move = legal_moves[0]
                    updated_state = self.state_manager.apply_move(state, fallback_move)
            else:
                # If an invalid move was provided, use the first legal move
                fallback_move = legal_moves[0]
                updated_state = self.state_manager.apply_move(state, fallback_move)

        except Exception as e:
            # If any error occurs, log it and use a fallback move
            logger.exception(f"Error making move: {e}")
            legal_moves = self.state_manager.get_legal_moves(state)
            fallback_move = legal_moves[0]
            updated_state = self.state_manager.apply_move(state, fallback_move)

        # Return the updated state with conditional goto
        if (
            updated_state.game_status == "game_over"
            or "win" in updated_state.game_status
        ):
            return Command(update=updated_state, goto=END)

        # Determine next node based on player
        goto = "analyze_player2" if player == "player1" else "analyze_player1"
        return Command(update=updated_state, goto=goto)

    def extract_move(self, response: Any) -> DominoMove | Literal["pass"]:
        """Extract move from engine response."""

        # If the response is already a DominoesPlayerDecision
        if isinstance(response, DominoesPlayerDecision):
            if response.pass_turn:
                return "pass"
            return response.move

        # Handle AIMessage with content
        if hasattr(response, "content"):
            if isinstance(response.content, DominoesPlayerDecision):
                if response.content.pass_turn:
                    return "pass"
                return response.content.move
            if isinstance(response.content, dict):
                try:
                    decision = DominoesPlayerDecision.model_validate(response.content)
                    if decision.pass_turn:
                        return "pass"
                    return decision.move
                except Exception as e:
                    logger.warning(f"Failed to parse decision from content dict: {e}")

        # Handle tool calls in response
        if hasattr(response, "tool_calls") and response.tool_calls:
            tool_call = response.tool_calls[0]
            if hasattr(tool_call, "args") and isinstance(tool_call.args, dict):
                try:
                    decision = DominoesPlayerDecision.model_validate(tool_call.args)
                    if decision.pass_turn:
                        return "pass"
                    return decision.move
                except Exception as e:
                    logger.warning(f"Failed to parse decision from tool_call args: {e}")
            elif hasattr(tool_call, "function") and "arguments" in tool_call.function:
                try:
                    args = json.loads(tool_call.function["arguments"])
                    decision = DominoesPlayerDecision.model_validate(args)
                    if decision.pass_turn:
                        return "pass"
                    return decision.move
                except Exception as e:
                    logger.warning(f"Failed to parse tool call arguments: {e}")

        # Handle tool calls in additional_kwargs
        if (
            hasattr(response, "additional_kwargs")
            and "tool_calls" in response.additional_kwargs
        ):
            tool_calls = response.additional_kwargs["tool_calls"]
            if tool_calls and len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call and "arguments" in tool_call["function"]:
                    try:
                        args = json.loads(tool_call["function"]["arguments"])
                        decision = DominoesPlayerDecision.model_validate(args)
                        if decision.pass_turn:
                            return "pass"
                        return decision.move
                    except Exception as e:
                        logger.warning(
                            "Failed to parse tool call arguments from "
                            f"additional_kwargs: {e}"
                        )

        # Handle raw dict
        if isinstance(response, dict):
            try:
                decision = DominoesPlayerDecision.model_validate(response)
                if decision.pass_turn:
                    return "pass"
                return decision.move
            except Exception as e:
                logger.warning(f"Failed to parse decision from dict: {e}")

        # Fallback to pass if we can't extract a valid move
        logger.warning(
            f"Could not extract valid move from response type: {type(response)}"
        )
        return "pass"

    def prepare_analysis_context(
        self, state: DominoesState, player: str
    ) -> dict[str, Any]:
        """Prepare context for position analysis."""
        hand = state.hands[player]
        formatted_hand = [str(tile) for tile in hand]

        pip_count = sum(tile.left + tile.right for tile in hand)

        value_counts = {}
        for i in range(7):  # Values 0-6
            value_counts[i] = sum(1 for tile in hand if i in (tile.left, tile.right))

        return {
            "player": player,
            "hand": formatted_hand,
            "pip_count": pip_count,
            "value_counts": value_counts,
            "board": state.board_string,
            "open_ends": [state.left_value, state.right_value] if state.board else [],
            "boneyard_count": len(state.boneyard),
            "opponent_count": {
                p: len(state.hands[p]) for p in state.players if p != player
            },
            "move_history": state.move_history[-5:],  # Last 5 moves
        }

    def analyze_player1(self, state: DominoesState) -> Command:
        """Analyze position for player1.

        Args:
            state (DominoesState): The current game state.

        Returns:
            Command: Command with updated state.

        """
        # Ensure we have a DominoesState object
        if isinstance(state, dict):
            try:
                state = DominoesState.model_validate(state)
            except Exception as e:
                logger.exception(
                    f"Error converting dict to DominoesState in analyze_player1: {e}"
                )
                # Return a minimal Command to avoid crashing
                return Command(update=state, goto="player1_move")

        # Always analyze for player1, even if it's not their turn
        # This ensures analysis is ready before their move
        return self.analyze_position(state, "player1")

    def analyze_player2(self, state: DominoesState) -> Command:
        """Analyze position for player2.

        Args:
            state (DominoesState): The current game state.

        Returns:
            Command: Command with updated state.

        """
        # Ensure we have a DominoesState object
        if isinstance(state, dict):
            try:
                state = DominoesState.model_validate(state)
            except Exception as e:
                logger.exception(
                    f"Error converting dict to DominoesState in analyze_player2: {e}"
                )
                # Return a minimal Command to avoid crashing
                return Command(update=state, goto="player2_move")

        # Always analyze for player2, even if it's not their turn
        # This ensures analysis is ready before their move
        return self.analyze_position(state, "player2")

    def analyze_position(self, state: DominoesState, player: str) -> Command:
        """Analyze the current position for the specified player.

        Args:
            state (DominoesState): The current game state.
            player (str): The player to analyze the position for.

        Returns:
            Command: Command with updated state.

        """
        # Ensure we have a DominoesState object
        if isinstance(state, dict):
            try:
                state = DominoesState.model_validate(state)
            except Exception as e:
                logger.exception(
                    f"Error converting dict to DominoesState in analyze_position: {e}"
                )
                # Return a minimal Command to avoid crashing
                goto = f"{player}_move"
                return Command(update=state, goto=goto)

        # Get the player's context for analysis
        # We analyze their position even if it's not their turn
        context = self.prepare_analysis_context(state, player)

        # Select the appropriate engine
        engine_key = f"{player}_analyzer"

        try:
            engine = self.engines[engine_key]

            # Generate analysis
            analysis_response = engine.invoke(context)
            analysis = self._extract_analysis(analysis_response)

            # Update state with analysis
            updated_state = self.state_manager.update_analysis(state, analysis, player)
        except Exception as e:
            # If any error occurs, log it and skip analysis
            logger.exception(f"Error during analysis: {e}")
            updated_state = state

        # Return the updated state
        goto = f"{player}_move"
        return Command(update=updated_state, goto=goto)

    def _extract_analysis(self, response: Any) -> DominoesAnalysis:
        """Extract analysis from engine response."""

        # If the response is already a DominoesAnalysis
        if isinstance(response, DominoesAnalysis):
            return response

        # Handle AIMessage with content
        if hasattr(response, "content"):
            if isinstance(response.content, DominoesAnalysis):
                return response.content
            if isinstance(response.content, dict):
                try:
                    return DominoesAnalysis.model_validate(response.content)
                except Exception as e:
                    logger.warning(f"Failed to parse analysis from content dict: {e}")

        # Handle tool calls in response
        if hasattr(response, "tool_calls") and response.tool_calls:
            tool_call = response.tool_calls[0]
            if hasattr(tool_call, "args") and isinstance(tool_call.args, dict):
                try:
                    return DominoesAnalysis.model_validate(tool_call.args)
                except Exception as e:
                    logger.warning(f"Failed to parse analysis from tool_call args: {e}")
            elif hasattr(tool_call, "function") and "arguments" in tool_call.function:
                try:
                    args = json.loads(tool_call.function["arguments"])
                    return DominoesAnalysis.model_validate(args)
                except Exception as e:
                    logger.warning(f"Failed to parse tool call arguments: {e}")

        # Handle tool calls in additional_kwargs
        if (
            hasattr(response, "additional_kwargs")
            and "tool_calls" in response.additional_kwargs
        ):
            tool_calls = response.additional_kwargs["tool_calls"]
            if tool_calls and len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call and "arguments" in tool_call["function"]:
                    try:
                        args = json.loads(tool_call["function"]["arguments"])
                        return DominoesAnalysis.model_validate(args)
                    except Exception as e:
                        logger.warning(
                            "Failed to parse tool call arguments from "
                            f"additional_kwargs: {e}"
                        )

        # Handle raw dict
        if isinstance(response, dict):
            try:
                return DominoesAnalysis.model_validate(response)
            except Exception as e:
                logger.warning(f"Failed to parse analysis from dict: {e}")

        # Create a fallback analysis if we can't extract a valid one
        logger.warning(
            f"Creating fallback analysis for response type: {type(response)}"
        )
        return DominoesAnalysis(
            hand_strength=5,
            pip_count_assessment="Unknown",
            open_ends=["Unknown"],
            missing_values=[],
            suggested_strategy="Play strategically",
            blocking_potential="Unknown",
            reasoning="Fallback analysis - could not extract from response",
        )

    def check_game_status(self, state: DominoesState) -> str:
        """Check if the game is over.

        Args:
            state (DominoesState): The current game state.

        Returns:
            str: Next node to go to.

        """
        if state.game_status == "game_over" or "win" in state.game_status:
            return END

        # Determine next node based on turn
        return "player1_move" if state.turn == "player1" else "player2_move"

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Visualize the current game state."""
        if self.ui:
            self.ui.display_state(state)
        else:
            # Fallback to text-based visualization
            # Create a DominoesState from the dict
            try:
                domino_state = DominoesState(**state)

                logger.info("\n" + "=" * 50)
                logger.info(f"🎮 Current Player: {domino_state.turn}")
                logger.info(f"📌 Game Status: {domino_state.game_status}")
                logger.info("=" * 50)

                # Show the board
                logger.info("\n" + domino_state.board_string)

                # Print player hands
                for player in domino_state.players:
                    hand = domino_state.hands[player]
                    formatted_hand = [str(tile) for tile in hand]
                    hand_info = (
                        f"\n{player}'s hand: {', '.join(formatted_hand)} "
                        f"(Pip count: {sum(tile.left + tile.right for tile in hand)})"
                    )
                    logger.info(hand_info)

                # Log boneyard
                logger.info(f"\nBoneyard: {len(domino_state.boneyard)} remaining tiles")

                # Log last move if available
                if domino_state.move_history:
                    logger.info(f"\nLast move: {domino_state.move_history[-1]}")

                # Print analysis if available
                if (
                    hasattr(domino_state, "player1_analysis")
                    and domino_state.player1_analysis
                    and domino_state.turn == "player1"
                ):
                    logger.info(
                        f"\nPlayer 1 Analysis: {domino_state.player1_analysis[-1]}"
                    )
                if (
                    hasattr(domino_state, "player2_analysis")
                    and domino_state.player2_analysis
                    and domino_state.turn == "player2"
                ):
                    logger.info(
                        f"\nPlayer 2 Analysis: {domino_state.player2_analysis[-1]}"
                    )
            except Exception as e:
                logger.exception(f"Error in text visualization: {e}")
                logger.exception(f"Error visualizing state: {e}")

    def run_game(self, visualize: bool = True) -> dict[str, Any]:
        """Run the full game, optionally visualizing each step."""
        if not visualize:
            return self.run({})

        # Check if UI is available and use it if requested
        if visualize and UI_AVAILABLE and self.ui:
            return self.run_game_with_ui()

        # Fallback to terminal-based visualization
        initial_state = self.state_manager.initialize()
        try:
            for step in self.app.stream(
                initial_state,
                stream_mode="values",
                debug=True,
                config=self.runnable_config,
            ):
                self.visualize_state(step)
                time.sleep(1)  # Add delay for better visualization
            return step
        except Exception as e:
            logger.exception(f"Error running game: {e}")
            return {}

    def run_game_with_ui(self, delay: float = 1.5) -> dict[str, Any]:
        """Run the full game with Rich UI visualization.

        Args:
            delay: Delay between moves in seconds

        Returns:
            Final game state

        """
        if not self.ui:
            logger.error("UI not available - falling back to regular run")
            return self.run_game(visualize=False)

        logger.info("Starting Dominoes game with UI")

        # Display welcome
        self.ui.display_welcome()
        time.sleep(1.5)

        # Initialize game state
        initial_state = self.state_manager.initialize()

        # Create live display
        with Live(refresh_per_second=4) as live:
            final_state = initial_state

            try:
                # Run the game using agent.stream()
                logger.debug(
                    f"Starting stream with initial state type: {type(initial_state)}"
                )

                # Display initial state
                layout = self.ui.create_layout(initial_state)
                live.update(layout)
                time.sleep(delay)

                step_count = 0
                try:
                    for state_update in self.app.stream(
                        initial_state,
                        stream_mode="values",
                        debug=True,
                        config=self.runnable_config,
                    ):
                        step_count += 1
                        logger.debug(f"Stream step {step_count}: Received state update")

                        # Handle None state from stream
                        if state_update is None:
                            logger.warning("Received None state from stream, skipping")
                            continue

                        # Extract the game state and update display
                        game_state = self.ui.extract_game_state(state_update)
                        if game_state:
                            # Update the live display
                            layout = self.ui.create_layout(game_state)
                            live.update(layout)
                            final_state = game_state

                            # Check if game is over
                            if game_state.game_status != "ongoing":
                                logger.info(
                                    f"Game completed with status: {
                                        game_state.game_status
                                    }"
                                )
                                time.sleep(delay * 2)  # Show final state longer
                                break

                            # Delay between moves
                            time.sleep(delay)
                        else:
                            logger.warning(
                                "Could not extract game state from stream update"
                            )
                except Exception as e:
                    logger.error(f"Error during stream processing: {e}", exc_info=True)
                    self.console.print(f"[red]Stream error: {e}[/red]")

                logger.info(f"Stream completed after {step_count} steps")

            except Exception as e:
                logger.error(f"Error during game execution: {e}", exc_info=True)
                self.console.print(f"[red]Error during game: {e}[/red]")

        # Display final results
        if final_state and self.ui:
            self.ui.display_final_results(final_state)

        return final_state

    def setup_workflow(self) -> None:
        """Set up the game workflow."""
        # Create the graph builder with the state schema
        gb = DynamicGraph(
            name=self.config.name,
            components=[self.config],
            state_schema=self.config.state_schema,
        )

        # Add nodes for the main game flow
        gb.add_node("initialize", self.initialize_game)
        gb.set_entry_point("initialize")
        gb.add_node("player1_move", self.make_player1_move)
        gb.add_node("player2_move", self.make_player2_move)
        gb.add_node("analyze_player1", self.analyze_player1)
        gb.add_node("analyze_player2", self.analyze_player2)

        # Create a strictly sequential flow to avoid concurrent updates
        # 1. Start with initialize
        gb.add_edge("initialize", "analyze_player1")

        # 2. Player 1's turn: analyze -> move
        gb.add_edge("analyze_player1", "player1_move")

        # 3. After player 1 moves, go to player 2's analysis
        gb.add_edge("player1_move", "analyze_player2")

        # 4. Player 2's turn: analyze -> move
        gb.add_edge("analyze_player2", "player2_move")

        # 5. After player 2 moves, back to player 1's analysis
        gb.add_edge("player2_move", "analyze_player1")

        # Add conditional edges to handle game ending
        gb.add_conditional_edges(
            "player1_move",
            lambda state: state.game_status == "ongoing",
            {True: "analyze_player2", False: END},
        )

        gb.add_conditional_edges(
            "player2_move",
            lambda state: state.game_status == "ongoing",
            {True: "analyze_player1", False: END},
        )

        # Build the graph
        self.graph = gb.build()

        # Compile the app for later use in run_game
        self._app = self.graph.compile()


# For direct script execution
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Create and run the game agent
    agent = DominoesAgent()
    agent.run_game(visualize=True)
