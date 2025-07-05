"""Mancala game agent.

This module defines the Mancala game agent, which uses language models
to generate moves and analyze positions in the game.
"""

import logging
import time
from typing import Any

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.types import Command

from haive.games.framework.base.agent import GameAgent
from haive.games.mancala.config import MancalaConfig
from haive.games.mancala.models import MancalaMove
from haive.games.mancala.state import MancalaState
from haive.games.mancala.state_manager import MancalaStateManager

# Set up logging
logger = logging.getLogger(__name__)


def ensure_game_state(
    state_input: dict[str, Any] | MancalaState | Command,
) -> MancalaState:
    """Ensure input is converted to MancalaState.

    Args:
        state_input: State input as dict, MancalaState, or Command

    Returns:
        MancalaState instance
    """
    logger.info(f"ensure_game_state: received input of type {type(state_input)}")

    if isinstance(state_input, MancalaState):
        logger.info("ensure_game_state: Input is already MancalaState")
        return state_input
    if isinstance(state_input, Command):
        logger.info("ensure_game_state: Input is a Command, extracting state")
        # Attempt to extract state from Command
        if hasattr(state_input, "state") and state_input.state:
            return ensure_game_state(state_input.state)
        logger.error("ensure_game_state: Command does not have state attribute")
        # Initialize a new state as fallback
        return MancalaState.initialize()
    if isinstance(state_input, dict):
        try:
            logger.info(
                f"ensure_game_state: Converting dict to MancalaState, keys: {list(state_input.keys())}"
            )
            return MancalaState.model_validate(state_input)
        except Exception as e:
            logger.error(f"Failed to convert dict to MancalaState: {e}")
            logger.debug(f"Dict contents: {state_input}")
            # Initialize a new state as fallback rather than crashing
            logger.info("ensure_game_state: Using default state as fallback")
            return MancalaState.initialize()
    else:
        logger.error(f"Cannot convert {type(state_input)} to MancalaState")
        # Initialize a new state as fallback rather than crashing
        logger.info("ensure_game_state: Using default state as fallback")
        return MancalaState.initialize()


@register_agent(MancalaConfig)
class MancalaAgent(GameAgent[MancalaConfig]):
    """Agent for playing Mancala.

    This class implements the Mancala game agent, which uses language models
    to generate moves and analyze positions in the game.
    """

    def __init__(self, config: MancalaConfig = MancalaConfig()):
        """Initialize the Mancala agent.

        Args:
            config (MancalaConfig): The configuration for the Mancala game.
        """
        super().__init__(config)
        self.state_manager = MancalaStateManager
        self.engines = config.aug_llm_configs

    def initialize_game(self, state: dict[str, Any]) -> Command:
        """Initialize a new Mancala game with configured stones per pit.

        Args:
            state (Dict[str, Any]): Initial state dictionary (unused here but required for interface).

        Returns:
            Command: Initialization command containing the new game state fields.
        """
        game_state = self.state_manager.initialize(
            stones_per_pit=self.config.stones_per_pit
        )

        return Command(
            update={
                "board": game_state.board,
                "turn": game_state.turn,
                "game_status": game_state.game_status,
                "move_history": game_state.move_history,
                "free_turn": game_state.free_turn,
                "winner": game_state.winner,
                "player1_analysis": game_state.player1_analysis,
                "player2_analysis": game_state.player2_analysis,
                "error_message": None,
            }
        )

    def prepare_move_context(self, state: MancalaState, player: str) -> dict[str, Any]:
        """Prepare context for move generation.

        Args:
            state (MancalaState): Current game state.
            player (str): The player making the move ('player1' or 'player2').

        Returns:
            Dict[str, Any]: Context dictionary for move generation.
        """
        try:
            # Ensure we have a proper MancalaState
            game_state = ensure_game_state(state)

            # Get legal moves
            legal_moves = self.state_manager.get_legal_moves(game_state)

            # Format legal moves for display
            formatted_legal_moves = "\n".join(
                [
                    f"Pit {move.pit_index}: {game_state.board[move.pit_index if player == 'player1' else move.pit_index + 7]} stones"
                    for move in legal_moves
                ]
            )

            # Get recent move history
            recent_moves = []
            for move in game_state.move_history[-5:]:
                recent_moves.append(str(move))

            # Get player's analysis if available
            player_analysis = None
            if hasattr(game_state, f"{player}_analysis") and getattr(
                game_state, f"{player}_analysis"
            ):
                player_analysis = getattr(game_state, f"{player}_analysis")[-1]
            else:
                player_analysis = "No previous analysis available."

            # Prepare the context
            return {
                "board_string": game_state.board_string,
                "turn": game_state.turn,
                "legal_moves": formatted_legal_moves,
                "move_history": "\n".join(recent_moves),
                "player_analysis": player_analysis,
            }

        except Exception as e:
            logger.error(f"Error preparing move context: {e}")
            # Return a minimal context to avoid crashing
            return {
                "board_string": "Error preparing context",
                "turn": player,
                "legal_moves": "No legal moves available due to error",
                "move_history": "",
                "player_analysis": "No analysis available due to error",
            }

    def prepare_analysis_context(
        self, state: MancalaState, player: str
    ) -> dict[str, Any]:
        """Prepare context for position analysis.

        Args:
            state (MancalaState): Current game state.
            player (str): The player making the analysis ('player1' or 'player2').

        Returns:
            Dict[str, Any]: Context dictionary for position analysis.
        """
        try:
            # Ensure we have a proper MancalaState
            game_state = ensure_game_state(state)

            # Get recent move history
            recent_moves = []
            for move in game_state.move_history[-5:]:
                recent_moves.append(str(move))

            # Get pit stones for each player
            player1_pits = game_state.board[0:6]
            player2_pits = game_state.board[7:13]

            # Prepare the context
            return {
                "board_string": game_state.board_string,
                "player": player,
                "player1_score": game_state.player1_score,
                "player2_score": game_state.player2_score,
                "player1_pits": player1_pits,
                "player2_pits": player2_pits,
                "move_history": "\n".join(recent_moves),
            }

        except Exception as e:
            logger.error(f"Error preparing analysis context: {e}")
            # Return a minimal context to avoid crashing
            return {
                "board_string": "Error preparing context",
                "player": player,
                "player1_score": 0,
                "player2_score": 0,
                "player1_pits": [0, 0, 0, 0, 0, 0],
                "player2_pits": [0, 0, 0, 0, 0, 0],
                "move_history": "",
            }

    def extract_move(self, response: Any) -> MancalaMove:
        """Extract move from engine response.

        Args:
            response (Any): Response from the engine.

        Returns:
            MancalaMove: Parsed move object.
        """
        # Handle different response types
        import json

        from langchain_core.messages import AIMessage

        # If it's an AIMessage (from LLM tool call)
        if isinstance(response, AIMessage):
            # Check for tool_calls in the message's tool_calls attribute
            if hasattr(response, "tool_calls") and response.tool_calls:
                # Extract the first tool call
                tool_call = response.tool_calls[0]
                # Extract the args from the tool call
                if hasattr(tool_call, "args"):
                    # Some versions of LangChain have parsed args
                    args = tool_call.args
                    return MancalaMove(
                        pit_index=args.get("pit_index"), player=args.get("player")
                    )

            # Check additional_kwargs for tool_calls (this is the common pattern)
            if (
                hasattr(response, "additional_kwargs")
                and "tool_calls" in response.additional_kwargs
            ):
                tool_calls = response.additional_kwargs["tool_calls"]
                if tool_calls and len(tool_calls) > 0:
                    # Get the first tool call
                    tool_call = tool_calls[0]
                    # Parse the arguments from the function
                    if "function" in tool_call and "arguments" in tool_call["function"]:
                        # Parse the JSON string in arguments
                        args = json.loads(tool_call["function"]["arguments"])
                        return MancalaMove(
                            pit_index=args.get("pit_index"), player=args.get("player")
                        )

        # If it's already a MancalaMove, return it
        if isinstance(response, MancalaMove):
            return response

        # If it's a dict, convert to MancalaMove
        if isinstance(response, dict) and "pit_index" in response:
            return MancalaMove(
                pit_index=response.get("pit_index"), player=response.get("player", "")
            )

        # If we got here, we couldn't extract a valid move
        raise ValueError(f"Could not extract move from response: {response}")

    def make_player1_move(self, state: MancalaState) -> Command:
        """Make a move for player1.

        Args:
            state (MancalaState): Current game state.

        Returns:
            Command: Updated game state after the move.
        """
        return self.make_move(state, "player1")

    def make_player2_move(self, state: MancalaState) -> Command:
        """Make a move for player2.

        Args:
            state (MancalaState): Current game state.

        Returns:
            Command: Updated game state after the move.
        """
        return self.make_move(state, "player2")

    def make_move(self, state: MancalaState, player: str) -> Command:
        """Make a move for the specified player.

        Args:
            state (MancalaState): Current game state.
            player (str): The player making the move ('player1' or 'player2').

        Returns:
            Command: Updated game state after the move.
        """
        try:
            # Ensure we have a proper MancalaState
            game_state = ensure_game_state(state)

            # Log state conversion
            logger.info(f"make_move: state type before conversion: {type(state)}")
            logger.info(f"make_move: state type after conversion: {type(game_state)}")

            # Check if it's the correct player's turn
            if game_state.turn != player:
                return Command(
                    update={"game_status": game_state.game_status}
                )  # Pass through game status to help terminate recursion

            # Check if game is over
            if game_state.game_status != "ongoing":
                return Command(stop=True)  # Stop the graph execution if game is over

            try:
                # Prepare context for the move
                context = self.prepare_move_context(game_state, player)

                # Select the appropriate engine
                engine_key = f"{player}_player"
                engine = self.engines[engine_key].create_runnable()

                # Generate move
                response = engine.invoke(context)

                # Extract the move from the response
                try:
                    move = self.extract_move(response)
                    # Ensure the move has the correct player
                    if not hasattr(move, "player") or not move.player:
                        # Set the player attribute explicitly
                        move.player = player
                except Exception as extract_error:
                    logger.error(f"Failed to extract move: {extract_error}")
                    return Command(
                        update={
                            "error_message": f"Failed to extract move: {extract_error!s}\nResponse: {response}"
                        }
                    )

                # Apply the move
                new_state = self.state_manager.apply_move(game_state, move)

                # Return only the fields that changed
                return Command(
                    update={
                        "board": new_state.board,
                        "turn": new_state.turn,
                        "game_status": new_state.game_status,
                        "move_history": new_state.move_history,
                        "free_turn": new_state.free_turn,
                        "winner": new_state.winner,
                        "error_message": None,
                    }
                )

            except Exception as e:
                logger.error(f"Error generating move: {e}")
                # Return error without changing other state
                return Command(update={"error_message": str(e)})

        except Exception as e:
            logger.error(f"Critical error in make_move: {e}", exc_info=True)
            # Return error without changing other state
            return Command(update={"error_message": f"Critical error: {e!s}"})

    def extract_analysis(self, response: Any) -> Any:
        """Extract analysis from engine response.

        Args:
            response (Any): Response from the engine.

        Returns:
            Any: Parsed analysis object.
        """
        # Handle different response types
        import json

        from langchain_core.messages import AIMessage

        from haive.games.mancala.models import MancalaAnalysis

        # If it's an AIMessage (from LLM tool call)
        if isinstance(response, AIMessage):
            # Extract the MancalaAnalysis data from the tool call
            if hasattr(response, "tool_calls") and response.tool_calls:
                # Extract the first tool call
                tool_call = response.tool_calls[0]
                # Parse the args if available
                if hasattr(tool_call, "args"):
                    return MancalaAnalysis(**tool_call.args)

            # Check additional_kwargs for tool_calls
            if (
                hasattr(response, "additional_kwargs")
                and "tool_calls" in response.additional_kwargs
            ):
                tool_calls = response.additional_kwargs["tool_calls"]
                if tool_calls and len(tool_calls) > 0:
                    # Get the first tool call
                    tool_call = tool_calls[0]
                    # Parse the arguments from the function
                    if "function" in tool_call and "arguments" in tool_call["function"]:
                        # Parse the JSON string in arguments
                        try:
                            args = json.loads(tool_call["function"]["arguments"])
                            return MancalaAnalysis(**args)
                        except Exception as e:
                            raise ValueError(
                                f"Failed to parse tool call arguments: {e}"
                            )

        # If it's already an analysis object, return it
        if isinstance(response, MancalaAnalysis):
            return response

        # If it's a dict with analysis fields, try to convert it
        if isinstance(response, dict) and "position_evaluation" in response:
            try:
                return MancalaAnalysis(**response)
            except Exception as e:
                raise ValueError(f"Could not convert dict to MancalaAnalysis: {e}")

        # If we couldn't parse the response
        raise ValueError(f"Could not extract analysis from response: {response}")

    def analyze_player1(self, state: MancalaState) -> Command:
        """Analyze position for player1.

        Args:
            state (MancalaState): Current game state.

        Returns:
            Command: Updated game state after the analysis.
        """
        return self.analyze_position(state, "player1")

    def analyze_player2(self, state: MancalaState) -> Command:
        """Analyze position for player2.

        Args:
            state (MancalaState): Current game state.

        Returns:
            Command: Updated game state after the analysis.
        """
        return self.analyze_position(state, "player2")

    def analyze_position(self, state: MancalaState, player: str) -> Command:
        """Analyze the current position for the specified player.

        Args:
            state (MancalaState): Current game state.
            player (str): The player making the analysis ('player1' or 'player2').

        Returns:
            Command: Updated game state after the analysis.
        """
        try:
            # Ensure we have a proper MancalaState
            game_state = ensure_game_state(state)

            # Log state conversion
            logger.info(
                f"analyze_position: state type before conversion: {type(state)}"
            )
            logger.info(
                f"analyze_position: state type after conversion: {type(game_state)}"
            )

            # Skip analysis if disabled
            if not self.config.enable_analysis:
                return Command(update={})  # No changes

            # Stop graph execution if game is over
            if game_state.game_status != "ongoing":
                return Command(stop=True)  # Stop the graph execution if game is over

            try:
                # Prepare context for analysis
                context = self.prepare_analysis_context(game_state, player)

                # Select the appropriate engine
                engine_key = f"{player}_analyzer"
                engine = self.engines[engine_key].create_runnable()

                # Generate analysis
                try:
                    response = engine.invoke(context)
                    analysis = self.extract_analysis(response)
                except Exception as extract_error:
                    logger.error(f"Failed to extract analysis: {extract_error}")
                    return Command(
                        update={
                            "error_message": f"Failed to extract analysis: {extract_error!s}\nResponse: {response}"
                        }
                    )

                # Update state with analysis
                new_state = self.state_manager.add_analysis(
                    game_state, player, analysis
                )

                # Return only the analysis field that changed
                return Command(
                    update={
                        f"{player}_analysis": getattr(new_state, f"{player}_analysis")
                    }
                )

            except Exception as e:
                logger.error(f"Error generating analysis: {e}")
                # Return error without changing other state
                return Command(update={"error_message": str(e)})

        except Exception as e:
            logger.error(f"Critical error in analyze_position: {e}", exc_info=True)
            # Return empty Command to avoid errors
            return Command(update={"error_message": f"Critical error: {e!s}"})

    def visualize_state(self, state):
        """Visualize the current game state.

        Args:
            state: Either a MancalaState object or a dictionary with state data
        """
        try:
            # Use our helper function to ensure we have a proper MancalaState
            game_state = ensure_game_state(state)

            print("\n" + "=" * 50)
            print(f"🎮 Current Player: {game_state.turn}")
            print(f"📌 Game Status: {game_state.game_status}")
            if game_state.free_turn:
                print("🎲 Free Turn: Yes")
            print("=" * 50)
            print()

            # Display the board using the board_string property
            print(game_state.board_string)
            print()

            # Show move history if available
            if game_state.move_history:
                print("📜 Recent moves:")
                for i, move in enumerate(
                    game_state.move_history[-3:], 1
                ):  # Show last 3 moves
                    print(f"  {i}. {move}")
                print()

            # Show game over information
            if game_state.is_game_over():
                winner = game_state.get_winner()
                if winner == "draw":
                    print("🤝 Game ended in a draw!")
                elif winner:
                    print(f"🏆 {winner.title()} wins!")
                print()

        except Exception as e:
            logger.error(f"Error visualizing state: {e}")
            print(f"\nError visualizing state: {e}")

    def setup_workflow(self) -> None:
        """Set up the game workflow.

        Creates a dynamic graph with nodes for game initialization, move making,
        and analysis. Adds edges between nodes based on the current player's turn.
        """
        # Create a graph builder
        builder = DynamicGraph(state_schema=self.state_schema)

        # Add nodes for the main game flow
        builder.add_node("initialize", self.initialize_game)
        builder.set_entry_point("initialize")
        builder.add_node("player1_move", self.make_player1_move)
        builder.add_node("player2_move", self.make_player2_move)
        builder.add_node("analyze_player1", self.analyze_player1)
        builder.add_node("analyze_player2", self.analyze_player2)

        # Set up the game flow
        builder.add_edge("initialize", "player1_move")  # Start with player1
        builder.add_edge("player1_move", "analyze_player1")
        builder.add_edge("analyze_player1", "player2_move")
        builder.add_edge("player2_move", "analyze_player2")
        builder.add_edge("analyze_player2", "player1_move")  # Complete the cycle

        # Build the graph
        self.graph = builder.build()

    def run_game(self, visualize: bool = True, debug: bool = False) -> MancalaState:
        """Run a full Mancala game loop with optional visualization.

        Args:
            visualize (bool): Whether to visualize the game state.
            debug (bool): Whether to run in debug mode.

        Returns:
            MancalaState: Final game state after completion.
        """
        # Initialize game state
        initial_state = MancalaStateManager.initialize(
            stones_per_pit=self.config.stones_per_pit
        )

        # Run the game
        if visualize:
            try:
                final_state = None
                for step in self.app.stream(
                    initial_state,
                    stream_mode="values",
                    debug=debug,
                    config=self.runnable_config,
                ):
                    # Store the last step as the final state
                    final_state = step

                    # Visualize current state
                    self.visualize_state(step)
                    time.sleep(1)

                # Return the final state
                return final_state
            except Exception as e:
                import traceback

                print(f"Error during game execution: {e!s}")
                traceback.print_exc()

                # Try to run without streaming as a fallback
                try:
                    print("Attempting to run game without streaming...")
                    return super().run(initial_state, debug=debug)
                except Exception as fallback_error:
                    print(f"Fallback also failed: {fallback_error!s}")
                    return initial_state  # Return initial state as fallback
        else:
            # Run without visualization
            try:
                return super().run(initial_state, debug=debug)
            except Exception as e:
                import traceback

                print(f"Error running game: {e!s}")
                traceback.print_exc()
                return initial_state  # Return initial state as fallback
