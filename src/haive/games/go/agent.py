"""Go game agent implementation.

This module provides a Go game agent that supports:
    - Standard Go game rules and mechanics
    - Black and white player moves
    - Optional position analysis
    - Game state tracking and visualization
    - SGF format support via sente library

Example:
    >>> from haive.games.go import GoAgent, GoAgentConfig
    >>>
    >>> # Create a Go agent with analysis enabled
    >>> config = GoAgentConfig(include_analysis=True)
    >>> agent = GoAgent(config)
    >>>
    >>> # Run a game
    >>> run_go_game(agent)
"""

import logging
from typing import Any

from haive.core.engine.agent.agent import Agent, register_agent
from langgraph.constants import END, START
from langgraph.types import Command

from haive.games.go.config import GoAgentConfig
from haive.games.go.state import GoGameState
from haive.games.go.state_manager import GoGameStateManager

logger = logging.getLogger(__name__)

from haive.games.go import go_engine as sente


@register_agent(GoAgentConfig)
class GoAgent(Agent[GoAgentConfig]):
    """Go game agent implementation.

    This class provides the core functionality for playing Go games, including:
        - Move generation for both black and white players
        - Position analysis and evaluation
        - Game state management and validation
        - Workflow control for game progression

    Attributes:
        config (GoAgentConfig): Configuration for the Go agent
        engines (Dict[str, Any]): LLM engines for players and analysis
        graph (StateGraph): Game workflow graph

    Example:
        >>> config = GoAgentConfig(
        ...     include_analysis=True,
        ...     board_size=19
        ... )
        >>> agent = GoAgent(config)
        >>> run_go_game(agent)
    """

    def __init__(self, config: GoAgentConfig):
        """Initialize the Go agent.

        Args:
            config (GoAgentConfig): Configuration for the Go agent.
        """
        super().__init__(config)

    def setup_workflow(self) -> None:
        """Define the Go game workflow.

        Sets up the game flow graph with nodes for:
            - Game initialization
            - Black and white moves
            - Position analysis (if enabled)
            - Game status checks

        The workflow supports two main paths:
            1. Basic: Initialize -> Black Move -> White Move -> Repeat
            2. With Analysis: Initialize -> Black Move -> Black Analysis ->
               White Move -> White Analysis -> Repeat
        """
        self.graph.add_node("initialize_game", self.initialize_game)
        self.graph.add_node("black_move", self.make_black_move)
        self.graph.add_node("white_move", self.make_white_move)
        self.graph.add_node("black_analysis_position", self.analyze_black_position)
        self.graph.add_node("white_analysis_position", self.analyze_white_position)
        self.graph.add_node("check_game_status", self.check_game_status)

        # ✅ Set up initial game state
        self.graph.add_edge(START, "initialize_game")
        self.graph.add_edge("initialize_game", "black_move")

        # ✅ Move Execution with Optional Analysis
        if self.config.include_analysis:
            self.graph.add_edge("black_move", "black_analysis_position")
            self.graph.add_conditional_edges(
                "black_analysis_position",
                self.should_continue_game,
                {True: "white_move", False: END},
            )

            self.graph.add_edge("white_move", "white_analysis_position")
            self.graph.add_conditional_edges(
                "white_analysis_position",
                self.should_continue_game,
                {True: "black_move", False: END},
            )
        else:
            self.graph.add_conditional_edges(
                "black_move",
                self.should_continue_game,
                {True: "white_move", False: END},
            )
            self.graph.add_conditional_edges(
                "white_move",
                self.should_continue_game,
                {True: "black_move", False: END},
            )

    def initialize_game(self, state: GoGameState | None = None) -> Command:
        """Initialize a new game of Go.

        Args:
            state (Optional[GoGameState]): Optional initial state. If None,
                creates a new game with standard settings.

        Returns:
            Command: Command to update the game state with initial settings.
        """
        game_state = GoGameStateManager.initialize()
        return Command(update=game_state.model_dump())

    def make_move(self, state: GoGameState, color: str) -> Command:
        """Execute a move for the given player.

        Args:
            state (GoGameState): Current game state.
            color (str): Player color ("black" or "white").

        Returns:
            Command: Command to update the game state with the new move.

        Raises:
            ValueError: If no LLM engine is found for the player.

        Notes:
            - Provides the last 5 moves as context to the LLM
            - Includes recent position analysis if available
            - Validates moves through the state manager
        """
        player = self.engines.get(f"{color}_player")
        if player is None:
            raise ValueError(f"Missing LLM for {color}_player")

        move_response = player.invoke(
            {
                "board_size": state.board_size,
                "move_history": state.move_history[-5:],  # Last 5 moves
                "color": color,
                "captured_stones": state.captured_stones,
                "player_analysis": (
                    state.black_analysis[-1]
                    if color == "black" and state.black_analysis
                    else (
                        state.white_analysis[-1]
                        if color == "white" and state.white_analysis
                        else "N/A"
                    )
                ),
            }
        )

        move = move_response.move  # Extract move tuple (row, col)
        new_state = GoGameStateManager.apply_move(state, move)

        return Command(update=new_state.model_dump())

    def analyze_position(self, state: GoGameState, color: str) -> Command:
        """Analyze the current position for a player.

        Args:
            state (GoGameState): Current game state.
            color (str): Player color ("black" or "white").

        Returns:
            Command: Command to update the game state with the analysis.

        Raises:
            ValueError: If no LLM engine is found for analysis.

        Notes:
            - Maintains a history of the last 4 analyses
            - Provides territory evaluation and strategic advice
            - Identifies strong and weak positions
        """
        analyzer = self.engines.get(f"{color}_analyzer")
        if analyzer is None:
            raise ValueError(f"Missing LLM for {color}_analyzer")

        analysis = analyzer.invoke(
            {
                "board_size": state.board_size,
                "move_history": state.move_history[-5:],  # Last 5 moves
                "color": color,
                "captured_stones": state.captured_stones,
            }
        )

        if color == "black":
            return Command(
                update={"black_analysis": state.black_analysis[-4:] + [analysis.dict()]}
            )
        return Command(
            update={"white_analysis": state.white_analysis[-4:] + [analysis.dict()]}
        )

    def check_game_status(self, state: GoGameState) -> Command:
        """Check and update the Go game status.

        Args:
            state (GoGameState): Current game state.

        Returns:
            Command: Command to update the game status.

        Notes:
            - Uses sente library to validate game state
            - Detects game end conditions (resignation, passes)
            - Updates status to "ended" when game is complete
        """
        game = sente.sgf.loads(state.board_sgf)

        status = "ongoing"
        if game.is_over():
            status = "ended"

        return Command(update={"game_status": status})

    def should_continue_game(self, state: GoGameState) -> bool:
        """Determine if the game should continue.

        Args:
            state (GoGameState): Current game state.

        Returns:
            bool: True if game is ongoing, False otherwise.
        """
        return state.game_status == "ongoing"

    def make_black_move(self, state: GoGameState) -> Command:
        """Handle black's move in the game.

        Args:
            state (GoGameState): Current game state.

        Returns:
            Command: Command to update the game state with black's move.
        """
        return self.make_move(state, "black")

    def make_white_move(self, state: GoGameState) -> Command:
        """Handle white's move in the game.

        Args:
            state (GoGameState): Current game state.

        Returns:
            Command: Command to update the game state with white's move.
        """
        return self.make_move(state, "white")

    def analyze_black_position(self, state: GoGameState) -> Command:
        """Analyze black's position if analysis is enabled.

        Args:
            state (GoGameState): Current game state.

        Returns:
            Command: Command to update the game state with black's analysis.
        """
        return self.analyze_position(state, "black")

    def analyze_white_position(self, state: GoGameState) -> Command:
        """Analyze white's position if analysis is enabled.

        Args:
            state (GoGameState): Current game state.

        Returns:
            Command: Command to update the game state with white's analysis.
        """
        return self.analyze_position(state, "white")


def run_go_game(agent: GoAgent) -> None:
    """Run a Go game with visualization and structured output.

    This function manages the game loop and provides rich visualization
    of the game state, including:
        - Board visualization using ASCII art
        - Move history tracking
        - Position analysis display
        - Captured stones counting
        - Game status updates

    Args:
        agent (GoAgent): The Go agent to run the game with.

    Example:
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
    """
    # ✅ Initialize the game state
    initial_state = {
        "board_size": 19,
        "board_sgf": sente.sgf.dumps(sente.Game(19)),  # Start with an empty board
        "turn": "black",
        "move_history": [],
        "captured_stones": {"black": 0, "white": 0},
        "passes": 0,  # Track consecutive passes
        "game_status": "ongoing",
        "black_analysis": [],
        "white_analysis": [],
        "error_message": None,
    }

    # ✅ Stream the game loop
    for step in agent.app.stream(
        initial_state, config=agent.runnable_config, debug=True, stream_mode="values"
    ):
        # Check if step has board_sgf
        if hasattr(step, "board_sgf"):
            board_sgf = step.board_sgf
        elif isinstance(step, dict) and "board_sgf" in step:
            board_sgf = step["board_sgf"]
        else:
            # Skip steps without board_sgf
            continue

        # Load the game from SGF
        try:
            game = sente.sgf.loads(board_sgf)
        except Exception as e:
            logger.warning(f"Failed to load SGF: {e}")
            continue

        # 🎯 **Game Board Visualization**
        logger.info("\n🔷 Current Board Position:")
        logger.info(str(game))

        # 🎯 **Game State Information**
        turn = (
            step.get("turn", "unknown")
            if isinstance(step, dict)
            else getattr(step, "turn", "unknown")
        )
        game_status = (
            step.get("game_status", "unknown")
            if isinstance(step, dict)
            else getattr(step, "game_status", "unknown")
        )
        logger.info(f"\n🎮 Current Player: {turn.capitalize()}")
        logger.info(f"📌 Game Status: {game_status}")
        logger.info("-" * 50)

        # ✅ **Display Last Move**
        move_history = (
            step.get("move_history", [])
            if isinstance(step, dict)
            else getattr(step, "move_history", [])
        )
        if move_history:
            last_move = move_history[-1]
            logger.info(
                f"📝 Last Move: {last_move[0].capitalize()} played at {last_move[1]}"
            )

        # ✅ **Handle Black's Analysis Safely**
        black_analysis = (
            step.get("black_analysis", [])
            if isinstance(step, dict)
            else getattr(step, "black_analysis", [])
        )
        if black_analysis:
            last_black_analysis = black_analysis[-1]
            if isinstance(last_black_analysis, dict):
                logger.info("\n🔍 Black's Analysis:")
                logger.info(
                    f"   - Territory Estimate: {last_black_analysis.get('territory_evaluation', 'N/A')}"
                )
                logger.info(
                    f"   - Strong Positions: {last_black_analysis.get('strong_positions', 'N/A')}"
                )
                logger.info(
                    f"   - Weak Positions: {last_black_analysis.get('weak_positions', 'N/A')}"
                )
                logger.info(
                    f"   - Strategic Advice: {', '.join(last_black_analysis.get('strategic_advice', []))}"
                )

        # ✅ **Handle White's Analysis Safely**
        white_analysis = (
            step.get("white_analysis", [])
            if isinstance(step, dict)
            else getattr(step, "white_analysis", [])
        )
        if white_analysis:
            last_white_analysis = white_analysis[-1]
            if isinstance(last_white_analysis, dict):
                logger.info("\n🔍 White's Analysis:")
                logger.info(
                    f"   - Territory Estimate: {last_white_analysis.get('territory_evaluation', 'N/A')}"
                )
                logger.info(
                    f"   - Strong Positions: {last_white_analysis.get('strong_positions', 'N/A')}"
                )
                logger.info(
                    f"   - Weak Positions: {last_white_analysis.get('weak_positions', 'N/A')}"
                )
                logger.info(
                    f"   - Strategic Advice: {', '.join(last_white_analysis.get('strategic_advice', []))}"
                )

        # ✅ **Captured Stones**
        captured_stones = (
            step.get("captured_stones", {})
            if isinstance(step, dict)
            else getattr(step, "captured_stones", {})
        )
        if captured_stones:
            logger.info("\n🔻 Captured Stones:")
            logger.info(f"   - Black Captured: {captured_stones.get('black', 0)}")
            logger.info(f"   - White Captured: {captured_stones.get('white', 0)}")

        logger.info("\n" + "-" * 60)  # Divider for clarity
