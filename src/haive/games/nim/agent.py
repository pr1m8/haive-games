"""Agent for playing Nim.

This module defines the Nim agent, which uses language models
to generate moves and analyze positions in the game.
"""

import logging
import time
from typing import Any

from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langgraph.types import Command

from haive.games.framework.base.agent import GameAgent
from haive.games.nim.config import NimConfig
from haive.games.nim.state import NimState
from haive.games.nim.state_manager import NimStateManager

try:
    from haive.games.nim.ui import RICH_AVAILABLE, NimUI
except ImportError:
    RICH_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def ensure_game_state(
    state_input: dict[str, Any] | NimState | Command,
) -> NimState:
    """Ensure input is converted to NimState.

    This helper function ensures that the input state is properly converted to a NimState
    object, handling various input types (dict, NimState, Command).

    Args:
        state_input: The state to convert, which can be a dictionary, NimState, or Command.

    Returns:
        NimState: The converted state.
    """
    logger.info(f"ensure_game_state: received input of type {type(state_input)}")

    if isinstance(state_input, NimState):
        logger.info("ensure_game_state: Input is already NimState")
        return state_input
    if isinstance(state_input, Command):
        logger.info("ensure_game_state: Input is a Command, extracting state")
        # Attempt to extract state from Command
        if hasattr(state_input, "state") and state_input.state:
            return ensure_game_state(state_input.state)
        logger.error("ensure_game_state: Command does not have state attribute")
        # Initialize a new state as fallback
        return NimStateManager.initialize()
    if isinstance(state_input, dict):
        try:
            logger.info(
                f"ensure_game_state: Converting dict to NimState, keys: {list(state_input.keys())}"
            )
            return NimState.model_validate(state_input)
        except Exception as e:
            logger.error(f"Failed to convert dict to NimState: {e}")
            logger.debug(f"Dict contents: {state_input}")
            # Initialize a new state as fallback rather than crashing
            logger.info("ensure_game_state: Using default state as fallback")
            return NimStateManager.initialize()
    else:
        logger.error(f"Cannot convert {type(state_input)} to NimState")
        # Initialize a new state as fallback rather than crashing
        logger.info("ensure_game_state: Using default state as fallback")
        return NimStateManager.initialize()


class NimAgent(GameAgent[NimConfig]):
    """Agent for playing Nim."""

    def __init__(self, config: NimConfig = NimConfig()):
        """Initialize the Nim agent.

        Args:
            config (NimConfig): The configuration for the game.
        """
        self.state_manager = NimStateManager
        self.ui = NimUI() if RICH_AVAILABLE else None
        super().__init__(config)

    def initialize_game(self, state: dict[str, Any] | NimState | Command) -> Command:
        """Initialize a new Nim game with configured pile sizes.

        Args:
            state: The initial state of the game.

        Returns:
            Command: The command to initialize the game.
        """
        logger.info("Initializing new Nim game")

        # Initialize with configured pile sizes and misere mode
        game_state = self.state_manager.initialize(
            pile_sizes=self.config.pile_sizes, misere_mode=self.config.misere_mode
        )

        logger.info(
            f"Initialized game with pile sizes {game_state.piles} and misere_mode={game_state.misere_mode}"
        )

        return Command(
            update=(
                game_state.model_dump()
                if hasattr(game_state, "model_dump")
                else game_state.dict()
            )
        )

    def prepare_move_context(self, state: NimState, player: str) -> dict[str, Any]:
        """Prepare context for move generation.

        Args:
            state (NimState): The current game state.
            player (str): The player to prepare the context for.

        Returns:
            Dict[str, Any]: The context for the move generation.
        """
        # Format legal moves for display
        formatted_legal_moves = "\n".join(
            [
                f"Take {move.stones_taken} stones from pile {move.pile_index} (current size: {state.piles[move.pile_index]})"
                for move in self.state_manager.get_legal_moves(state)
            ]
        )

        # Get recent move history
        recent_moves = []
        for move in state.move_history[-5:]:
            recent_moves.append(str(move))

        # Prepare the context
        return {
            "board_string": state.board_string,
            "player": player,
            "legal_moves": formatted_legal_moves,
            "move_history": "\n".join(recent_moves),
            "misere_mode": state.misere_mode,
        }

    def extract_move(self, response: Any) -> Any:
        """Extract move from engine response.

        Args:
            response (Any): The response from the engine.

        Returns:
            Any: The move from the engine.
        """
        # The response should already be a NimMove object
        return response

    def make_player1_move(self, state: NimState) -> Command:
        """Make a move for player1.

        Args:
            state (NimState): The current game state.

        Returns:
            Command: The command to make the move.
        """
        return self.make_move(state, "player1")

    def make_player2_move(self, state: NimState) -> Command:
        """Make a move for player2.

        Args:
            state (NimState): The current game state.

        Returns:
            Command: The command to make the move.
        """
        return self.make_move(state, "player2")

    def make_move(
        self, state: NimState | dict[str, Any] | Command, player: str
    ) -> Command:
        """Make a move for the specified player.

        Args:
            state: The current game state.
            player: The player to make the move for.

        Returns:
            Command: The command to make the move.
        """
        # Ensure state is a NimState
        game_state = ensure_game_state(state)

        # Check if it's the player's turn
        if game_state.turn != player:
            logger.warning(f"Not {player}'s turn, but was asked to make a move")

        # Prepare context for the move
        context = self.prepare_move_context(game_state, player)

        # Select the appropriate engine
        engine_key = f"{player}_player"
        engine = self.engines[engine_key]

        # Generate move
        move = engine.invoke(context)

        # Apply the move
        new_state = self.state_manager.apply_move(game_state, move)

        # Return the updated state
        return Command(
            update=(
                new_state.model_dump()
                if hasattr(new_state, "model_dump")
                else new_state.dict()
            )
        )

    def prepare_analysis_context(self, state: NimState, player: str) -> dict[str, Any]:
        """Prepare context for position analysis.

        Args:
            state (NimState): The current game state.
            player (str): The player to prepare the context for.

        Returns:
            Dict[str, Any]: The context for the position analysis.
        """
        return {
            "board_string": state.board_string,
            "player": player,
            "move_history": [str(move) for move in state.move_history[-5:]],
            "misere_mode": state.misere_mode,
            "nim_sum": state.nim_sum,
        }

    def analyze_player1(self, state: NimState) -> Command:
        """Analyze position for player1.

        Args:
            state (NimState): The current game state.

        Returns:
            Command: The command to analyze the position.
        """
        return self.analyze_position(state, "player1")

    def analyze_player2(self, state: NimState) -> Command:
        """Analyze position for player2.

        Args:
            state (NimState): The current game state.

        Returns:
            Command: The command to analyze the position.
        """
        return self.analyze_position(state, "player2")

    def analyze_position(
        self, state: NimState | dict[str, Any] | Command, player: str
    ) -> Command:
        """Analyze the current position for the specified player.

        Args:
            state: The current game state.
            player: The player to analyze the position for.

        Returns:
            Command: The command to analyze the position.
        """
        # Ensure state is a NimState
        game_state = ensure_game_state(state)

        if not self.config.enable_analysis:
            return Command(
                update=(
                    game_state.model_dump()
                    if hasattr(game_state, "model_dump")
                    else game_state.dict()
                )
            )

        # Prepare context for analysis
        context = self.prepare_analysis_context(game_state, player)

        # Select the appropriate engine
        engine_key = f"{player}_analyzer"
        engine = self.engines[engine_key]

        # Generate analysis
        analysis = engine.invoke(context)

        # Update state with analysis
        new_state = self.state_manager.add_analysis(game_state, player, analysis)

        # Return the updated state
        return Command(
            update=(
                new_state.model_dump()
                if hasattr(new_state, "model_dump")
                else new_state.dict()
            )
        )

    def run_game(self, visualize: bool = True) -> dict[str, Any]:
        """Run a complete Nim game with optional visualization.

        Args:
            visualize (bool): Whether to visualize each game state.

        Returns:
            Dict[str, Any]: The final game state.
        """
        # Initialize the game state
        initial_state = self.state_manager.initialize(
            pile_sizes=self.config.pile_sizes, misere_mode=self.config.misere_mode
        )

        # Run the game with visualization
        if visualize:
            for step in self.stream(initial_state, stream_mode="values"):
                self.visualize_state(step)
            return step  # final state
        return super().run(initial_state)

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Visualize the current game state.

        Args:
            state (Dict[str, Any]): The current game state.
        """
        # Use Rich UI if available
        if RICH_AVAILABLE and self.ui:
            self.ui.display_game_state(state)
        else:
            # Fallback to basic text UI
            # Create a NimState from the dict
            game_state = ensure_game_state(state)

            print("\n" + "=" * 50)
            print(f"🎮 Current Player: {game_state.turn}")
            print(f"📌 Game Status: {game_state.game_status}")
            print(
                f"🎲 Game Mode: {'Misere (last takes loses)' if game_state.misere_mode else 'Standard (last takes wins)'}"
            )
            print("=" * 50)

            # Print the board
            print("\n" + game_state.board_string)

            # Print last move if available
            if game_state.move_history:
                last_move = game_state.move_history[-1]
                print(f"\n📝 Last Move: {last_move!s}")

            # Print analyses if available
            if (
                hasattr(game_state, "player1_analysis")
                and game_state.player1_analysis
                and game_state.turn == "player2"
            ):
                last_analysis = game_state.player1_analysis[-1]
                print("\n🔍 Player 1's Analysis:")
                print(f"Position Evaluation: {last_analysis.position_evaluation}")
                print(f"Explanation: {last_analysis.explanation}")

            if (
                hasattr(game_state, "player2_analysis")
                and game_state.player2_analysis
                and game_state.turn == "player1"
            ):
                last_analysis = game_state.player2_analysis[-1]
                print("\n🔍 Player 2's Analysis:")
                print(f"Position Evaluation: {last_analysis.position_evaluation}")
                print(f"Explanation: {last_analysis.explanation}")

        # Add a delay for readability (use the UI's delay if available)
        delay = self.ui.delay if hasattr(self, "ui") and self.ui else 0.5
        time.sleep(delay)

    def run_game_with_ui(self, show_analysis: bool = True) -> dict[str, Any]:
        """Run a complete Nim game with Rich UI.

        This method runs a Nim game with Rich UI visualization, showing
        the game state after each move. It optionally includes analysis.

        Args:
            show_analysis: Whether to include analysis in the game.

        Returns:
            Dict[str, Any]: The final game state.
        """
        # Check if Rich UI is available
        if not RICH_AVAILABLE:
            logger.warning("Rich UI not available. Using standard visualization.")
            return self.run_game(visualize=True)

        logger.info("Starting Nim game with Rich UI")

        # Initialize the game state
        initial_state = self.state_manager.initialize(
            pile_sizes=self.config.pile_sizes, misere_mode=self.config.misere_mode
        )

        # Set enable_analysis based on parameter
        old_enable_analysis = self.config.enable_analysis
        self.config.enable_analysis = show_analysis

        try:
            # Run the game with visualization
            for step in self.stream(initial_state, stream_mode="values"):
                self.visualize_state(step)

            # Return final state
            return step
        finally:
            # Restore original analysis setting
            self.config.enable_analysis = old_enable_analysis

    def setup_workflow(self) -> None:
        """Set up the game workflow.

        Returns:
            None
        """
        # Create a graph builder
        builder = DynamicGraph(state_schema=self.state_schema)

        # Add nodes for the main game flow
        builder.add_node("initialize", self.initialize_game)
        builder.add_node("player1_move", self.make_player1_move)
        builder.add_node("player2_move", self.make_player2_move)
        builder.add_node("analyze_player1", self.analyze_player1)
        builder.add_node("analyze_player2", self.analyze_player2)

        # Set up the game flow
        from langgraph.constants import START  # Import the START constant

        # Add START edge to initialize
        builder.add_edge(START, "initialize")

        # Set up the main game flow
        builder.add_edge("initialize", "player1_move")  # Start with player1
        builder.add_edge("player1_move", "analyze_player1")
        builder.add_edge("analyze_player1", "player2_move")
        builder.add_edge("player2_move", "analyze_player2")
        builder.add_edge("analyze_player2", "player1_move")  # Complete the cycle

        # Build the graph
        self.graph = builder.build()


# a=NimAgent()
# a.run_game(visualize=True)
