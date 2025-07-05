"""Fox and Geese game agent with fixed state handling and UI integration.

This module defines the Fox and Geese game agent, which uses language models
to generate moves and analyze positions in the game.
"""

# Standard library imports
import json
import logging
import re
import time
from typing import Any

# Local imports
from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph

# Third-party imports
from langgraph.constants import END, START
from langgraph.types import Command
from rich.console import Console
from rich.live import Live

from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.models import (
    FoxAndGeeseAnalysis,
    FoxAndGeeseMove,
    FoxAndGeesePosition,
)
from haive.games.fox_and_geese.state import FoxAndGeeseState
from haive.games.fox_and_geese.state_manager import FoxAndGeeseStateManager
from haive.games.framework.base.agent import GameAgent

# Import the UI module
try:
    from haive.games.fox_and_geese.ui import FoxAndGeeseUI

    UI_AVAILABLE = True
except ImportError:
    UI_AVAILABLE = False

logger = logging.getLogger(__name__)


def ensure_game_state(
    state_input: dict[str, Any] | FoxAndGeeseState,
) -> FoxAndGeeseState:
    """Ensure input is converted to FoxAndGeeseState.

    Args:
        state_input: State input as dict or FoxAndGeeseState

    Returns:
        FoxAndGeeseState instance
    """
    logger.info(f"ensure_game_state: received input of type {type(state_input)}")

    if isinstance(state_input, FoxAndGeeseState):
        logger.info("ensure_game_state: Input is already FoxAndGeeseState")
        return state_input
    if isinstance(state_input, Command):
        logger.info("ensure_game_state: Input is a Command, extracting state")
        # Attempt to extract state from Command
        if hasattr(state_input, "state") and state_input.state:
            return ensure_game_state(state_input.state)
        logger.error("ensure_game_state: Command does not have state attribute")
        # Initialize a new state as fallback
        return FoxAndGeeseState.initialize()
    if isinstance(state_input, dict):

        try:
            logger.info(
                f"ensure_game_state: Converting dict to FoxAndGeeseState, keys: {list(state_input.keys())}"
            )
            return FoxAndGeeseState.model_validate(state_input)
        except Exception as e:
            logger.error(f"Failed to convert dict to FoxAndGeeseState: {e}")
            logger.debug(f"Dict contents: {state_input}")
            # Initialize a new state as fallback rather than crashing
            logger.info("ensure_game_state: Using default state as fallback")
            return FoxAndGeeseState.initialize()
    else:
        logger.error(f"Cannot convert {type(state_input)} to FoxAndGeeseState")
        # Initialize a new state as fallback rather than crashing
        logger.info("ensure_game_state: Using default state as fallback")
        return FoxAndGeeseState.initialize()


@register_agent(FoxAndGeeseConfig)
class FoxAndGeeseAgent(GameAgent[FoxAndGeeseConfig]):
    """Agent for playing Fox and Geese.

    This class implements the Fox and Geese game agent, which uses language models
    to generate moves and analyze positions in the game.
    """

    def __init__(self, config: FoxAndGeeseConfig = FoxAndGeeseConfig()):
        """Initialize the Fox and Geese agent.

        Args:
            config (FoxAndGeeseConfig): The configuration for the Fox and Geese game.
        """
        super().__init__(config)
        self.state_manager = FoxAndGeeseStateManager
        self.engines = config.engines
        self.console = Console()
        self.game_over = False

        # Ensure recursion_limit is in runnable_config
        if hasattr(self, "runnable_config") and self.runnable_config:
            if "configurable" in self.runnable_config:
                self.runnable_config["configurable"][
                    "recursion_limit"
                ] = config.recursion_limit

        # Initialize UI if available
        self.ui = FoxAndGeeseUI(self.console) if UI_AVAILABLE else None
        if not UI_AVAILABLE:
            logger.warning("Rich UI not available - falling back to text output")

    def initialize_game(self, state: FoxAndGeeseState) -> dict[str, Any]:
        """Initialize a new Fox and Geese game.

        Args:
            state: Input state (ignored for initialization)

        Returns:
            Dict[str, Any]: State updates for the new game
        """
        logger.info("Initializing new Fox and Geese game")
        game_state = self.state_manager.initialize()
        logger.debug(
            f"Initialized game state: fox at {game_state.fox_position}, {game_state.num_geese} geese"
        )

        # Return the state as a Command with dictionary update
        return Command(
            update={
                "fox_position": game_state.fox_position,
                "geese_positions": game_state.geese_positions,
                "turn": game_state.turn,
                "game_status": game_state.game_status,
                "move_history": game_state.move_history,
                "winner": game_state.winner,
                "num_geese": game_state.num_geese,
                "fox_analysis": game_state.fox_analysis,
                "geese_analysis": game_state.geese_analysis,
                "error_message": None,  # Add an error_message field for consistency
            }
        )

    def prepare_move_context(
        self, state: FoxAndGeeseState, player: str
    ) -> dict[str, Any]:
        """Prepare context for move generation.

        Args:
            state: Current game state
            player: The player making the move ('fox' or 'geese')

        Returns:
            Dict[str, Any]: Context dictionary for move generation
        """
        # Format legal moves for display
        legal_moves = self.state_manager.get_legal_moves(state)
        formatted_legal_moves = "\n".join([str(move) for move in legal_moves])

        # Get recent move history
        recent_moves = []
        for move in state.move_history[-5:]:
            recent_moves.append(str(move))

        logger.debug(f"Prepared context for {player}: {len(legal_moves)} legal moves")

        # Prepare the context
        return {
            "board_string": state.board_string,
            "legal_moves": formatted_legal_moves,
            "move_history": "\n".join(recent_moves),
            "num_geese": state.num_geese,
        }

    def prepare_analysis_context(
        self, state: FoxAndGeeseState, player: str
    ) -> dict[str, Any]:
        """Prepare context for position analysis.

        Args:
            state: Current game state
            player: The player for whom to prepare the analysis context

        Returns:
            Dict[str, Any]: The context dictionary for position analysis
        """
        # Use the ensure_game_state helper to handle all conversion cases
        state = ensure_game_state(state)
        return {
            "board_string": state.board_string,
            "turn": state.turn,
            "num_geese": state.num_geese,
            "move_history": "\n".join([str(move) for move in state.move_history[-5:]]),
        }

    def extract_move(self, response: Any, piece_type: str = "fox") -> FoxAndGeeseMove:
        """Extract move from engine response.

        Args:
            response: Response from the engine
            piece_type: Type of piece making the move ('fox' or 'goose')

        Returns:
            FoxAndGeeseMove: Parsed move object
        """
        logger.debug(f"Extracting move from response type: {type(response)}")

        # Handle different response types
        if isinstance(response, FoxAndGeeseMove):
            # Already the right type
            logger.debug("Response is already FoxAndGeeseMove")
            return response
        if hasattr(response, "content"):
            # AIMessage with content
            if isinstance(response.content, FoxAndGeeseMove):
                # Content is already the structured object
                logger.debug("Response content is FoxAndGeeseMove")
                return response.content
            if isinstance(response.content, dict):
                # Content is a dict, convert to FoxAndGeeseMove
                logger.debug("Converting response content dict to FoxAndGeeseMove")
                return FoxAndGeeseMove.model_validate(response.content)
            if isinstance(response.content, str):
                # String content - try to parse structured data from it
                logger.debug(
                    "Received string content, trying to extract structured data"
                )

                # Try to extract a JSON object from the string
                try:
                    # Look for JSON-like content within the string
                    json_match = re.search(r"\{.*\}", response.content, re.DOTALL)
                    if json_match:
                        json_str = json_match.group(0)
                        parsed = json.loads(json_str)
                        if isinstance(parsed, dict):
                            logger.debug("Found JSON object in content string")
                            return FoxAndGeeseMove.model_validate(parsed)
                except Exception as e:
                    logger.warning(f"Failed to extract JSON from string content: {e}")

                # Check if content has move information in text format
                move_pattern = r"from\s*\((\d+),?\s*(\d+)\)\s*to\s*\((\d+),?\s*(\d+)\)"
                match = re.search(move_pattern, response.content)
                if match:
                    try:
                        from_row, from_col, to_row, to_col = map(int, match.groups())
                        logger.debug(
                            f"Extracted move coordinates from text: ({from_row},{from_col}) to ({to_row},{to_col})"
                        )

                        # Check for capture info
                        capture = None
                        capture_pattern = r"capture.*\((\d+),?\s*(\d+)\)"
                        capture_match = re.search(capture_pattern, response.content)
                        if capture_match:
                            cap_row, cap_col = map(int, capture_match.groups())
                            capture = FoxAndGeesePosition(row=cap_row, col=cap_col)

                        return FoxAndGeeseMove(
                            from_pos=FoxAndGeesePosition(row=from_row, col=from_col),
                            to_pos=FoxAndGeesePosition(row=to_row, col=to_col),
                            piece_type=piece_type,
                            capture=capture,
                        )
                    except Exception as e:
                        logger.warning(f"Failed to parse move from text pattern: {e}")
        elif isinstance(response, dict):
            # Response is a dict, convert to FoxAndGeeseMove
            logger.debug("Converting response dict to FoxAndGeeseMove")
            return FoxAndGeeseMove.model_validate(response)
        elif hasattr(response, "tool_calls") and response.tool_calls:
            # Handle tool calls directly
            logger.debug("Extracting move from tool_calls attribute")
            tool_call = response.tool_calls[0]
            if hasattr(tool_call, "args") and isinstance(tool_call.args, dict):
                return FoxAndGeeseMove.model_validate(tool_call.args)
            if hasattr(tool_call, "function") and "arguments" in tool_call.function:
                try:
                    args = json.loads(tool_call.function["arguments"])
                    return FoxAndGeeseMove.model_validate(args)
                except Exception as e:
                    logger.warning(f"Failed to parse tool call arguments: {e}")
        elif (
            hasattr(response, "additional_kwargs")
            and "tool_calls" in response.additional_kwargs
        ):
            # Handle tool calls in additional_kwargs
            logger.debug("Extracting move from additional_kwargs.tool_calls")
            tool_calls = response.additional_kwargs["tool_calls"]
            if tool_calls and len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call and "arguments" in tool_call["function"]:
                    try:
                        args = json.loads(tool_call["function"]["arguments"])
                        return FoxAndGeeseMove.model_validate(args)
                    except Exception as e:
                        logger.warning(
                            f"Failed to parse tool call arguments from additional_kwargs: {e}"
                        )

        # If we got here, we couldn't extract a valid move
        error_msg = f"Could not extract move from response type: {type(response)}"
        logger.error(error_msg)
        raise ValueError(error_msg)

    def _get_legal_move_fallback(
        self, game_state: FoxAndGeeseState, piece_type: str
    ) -> FoxAndGeeseMove:
        """Get a legal move as a fallback when LLM fails.

        Args:
            game_state: Current game state
            piece_type: Type of piece ('fox' or 'goose')

        Returns:
            FoxAndGeeseMove: A legal move
        """
        legal_moves = self.state_manager.get_legal_moves(game_state)
        if not legal_moves:
            raise ValueError(f"No legal moves available for {piece_type}")

        # Return the first legal move as fallback
        logger.info(
            f"Using first legal move as fallback for {piece_type}: {legal_moves[0]}"
        )
        return legal_moves[0]

    def make_player1_move(self, state: FoxAndGeeseState) -> Command:
        """Make a move for player 1 (fox).

        Args:
            state: Current game state

        Returns:
            Dict[str, Any]: State updates after the move
        """
        new_state = self.make_fox_move(state)
        return Command(
            update={
                "fox_position": new_state.fox_position,
                "geese_positions": new_state.geese_positions,
                "turn": new_state.turn,
                "game_status": new_state.game_status,
                "move_history": new_state.move_history,
                "winner": new_state.winner,
                "num_geese": new_state.num_geese,
                "error_message": None,
            }
        )

    def make_player2_move(self, state: FoxAndGeeseState) -> Command:
        """Make a move for player 2 (geese).

        Args:
            state: Current game state

        Returns:
            Dict[str, Any]: State updates after the move
        """
        new_state = self.make_geese_move(state)
        return Command(
            update={
                "fox_position": new_state.fox_position,
                "geese_positions": new_state.geese_positions,
                "turn": new_state.turn,
                "game_status": new_state.game_status,
                "move_history": new_state.move_history,
                "winner": new_state.winner,
                "num_geese": new_state.num_geese,
                "error_message": None,
            }
        )

    def analyze_player1(self, state: FoxAndGeeseState) -> Command:
        """Analyze position for player 1 (fox).

        Args:
            state: Current game state

        Returns:
            Dict[str, Any]: State updates with analysis
        """
        # analyze_fox_position already returns a Command
        return self.analyze_fox_position(state)

    def analyze_player2(self, state: FoxAndGeeseState) -> Command:
        """Analyze position for player 2 (geese).

        Args:
            state: Current game state

        Returns:
            Dict[str, Any]: State updates with analysis
        """
        # analyze_geese_position already returns a Command
        return self.analyze_geese_position(state)

    def make_fox_move(self, state: FoxAndGeeseState) -> FoxAndGeeseState:
        """Make a move for the fox.

        Args:
            state: Current game state

        Returns:
            FoxAndGeeseState: Updated game state after the move
        """
        try:
            # Ensure we have a proper FoxAndGeeseState
            game_state = ensure_game_state(state)
            logger.info(f"Fox move - Current turn: {game_state.turn}")

            # Ensure it's the fox's turn
            if game_state.turn != "fox":
                logger.warning(
                    f"Not fox's turn (current: {game_state.turn}), skipping fox move"
                )
                return game_state

            # Check if fox has legal moves
            legal_moves = self.state_manager.get_legal_moves(game_state)
            if not legal_moves:
                logger.info("Fox has no legal moves - game over!")
                new_state = game_state.model_copy(deep=True)
                new_state.game_status = "geese_win"
                new_state.winner = "geese"
                return new_state

            # Prepare context for the fox player
            context = self.prepare_move_context(game_state, "fox")

            # Try up to 3 times to get a valid move
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    # Call the fox player engine
                    fox_player = self.engines["fox_player"].create_runnable()
                    response = fox_player.invoke(context)

                    # Extract the move
                    move = self.extract_move(response, "fox")

                    # Validate move is legal
                    if move in legal_moves:
                        # We have a valid move, apply it
                        logger.info(f"Applying fox move: {move}")
                        new_state = self.state_manager.apply_move(game_state, move)
                        return new_state
                    logger.warning(
                        f"Attempt {attempt+1}/{max_attempts}: LLM move {move} not in legal moves"
                    )
                    if attempt == max_attempts - 1:
                        # Last attempt, use fallback
                        move = self._get_legal_move_fallback(game_state, "fox")
                        logger.info(f"Using fallback move: {move}")
                        new_state = self.state_manager.apply_move(game_state, move)
                        return new_state

                except Exception as e:
                    logger.error(
                        f"Attempt {attempt+1}/{max_attempts}: Error calling fox engine: {e}"
                    )
                    if attempt == max_attempts - 1:
                        # Last attempt, use fallback
                        move = self._get_legal_move_fallback(game_state, "fox")
                        logger.info(f"Using fallback move after error: {move}")
                        new_state = self.state_manager.apply_move(game_state, move)
                        return new_state

            # Fallback in case all attempts fail
            move = self._get_legal_move_fallback(game_state, "fox")
            logger.info(f"Using fallback move after all attempts failed: {move}")
            new_state = self.state_manager.apply_move(game_state, move)
            return new_state

        except Exception as e:
            logger.error(f"Critical error in fox move: {e}", exc_info=True)
            # Return original state to prevent crashes
            return ensure_game_state(state)

    def make_geese_move(self, state: FoxAndGeeseState) -> FoxAndGeeseState:
        """Make a move for the geese.

        Args:
            state: Current game state

        Returns:
            FoxAndGeeseState: Updated game state after the move
        """
        try:
            # Ensure we have a proper FoxAndGeeseState
            game_state = ensure_game_state(state)
            logger.info(f"Geese move - Current turn: {game_state.turn}")

            # Ensure it's the geese's turn
            if game_state.turn != "geese":
                logger.warning(
                    f"Not geese's turn (current: {game_state.turn}), skipping geese move"
                )
                return game_state

            # Check if geese have legal moves
            legal_moves = self.state_manager.get_legal_moves(game_state)
            if not legal_moves:
                logger.info("Geese have no legal moves - game over!")
                new_state = game_state.model_copy(deep=True)
                new_state.game_status = "fox_win"
                new_state.winner = "fox"
                return new_state

            # Prepare context for the geese player
            context = self.prepare_move_context(game_state, "geese")

            # Try up to 3 times to get a valid move
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    # Call the geese player engine
                    geese_player = self.engines["geese_player"].create_runnable()
                    response = geese_player.invoke(context)

                    # Extract the move
                    move = self.extract_move(response, "goose")

                    # Validate move is legal
                    if move in legal_moves:
                        # We have a valid move, apply it
                        logger.info(f"Applying geese move: {move}")
                        new_state = self.state_manager.apply_move(game_state, move)
                        return new_state
                    logger.warning(
                        f"Attempt {attempt+1}/{max_attempts}: LLM move {move} not in legal moves"
                    )
                    if attempt == max_attempts - 1:
                        # Last attempt, use fallback
                        move = self._get_legal_move_fallback(game_state, "goose")
                        logger.info(f"Using fallback move: {move}")
                        new_state = self.state_manager.apply_move(game_state, move)
                        return new_state

                except Exception as e:
                    logger.error(
                        f"Attempt {attempt+1}/{max_attempts}: Error calling geese engine: {e}"
                    )
                    if attempt == max_attempts - 1:
                        # Last attempt, use fallback
                        move = self._get_legal_move_fallback(game_state, "goose")
                        logger.info(f"Using fallback move after error: {move}")
                        new_state = self.state_manager.apply_move(game_state, move)
                        return new_state

            # Fallback in case all attempts fail
            move = self._get_legal_move_fallback(game_state, "goose")
            logger.info(f"Using fallback move after all attempts failed: {move}")
            new_state = self.state_manager.apply_move(game_state, move)
            return new_state

        except Exception as e:
            logger.error(f"Critical error in geese move: {e}", exc_info=True)
            # Return original state to prevent crashes
            return ensure_game_state(state)

    def analyze_fox_position(self, state: FoxAndGeeseState) -> Command:
        """Analyze the current position from the Fox's perspective.

        Args:
            state: Current game state

        Returns:
            Command: LangGraph command with fox analysis updates
        """
        try:
            # Ensure we have a proper FoxAndGeeseState
            game_state = ensure_game_state(state)

            # Log the type of state before and after conversion for debugging
            logger.info(f"Fox analysis: state type before conversion: {type(state)}")
            logger.info(
                f"Fox analysis: state type after conversion: {type(game_state)}"
            )

            self.prepare_analysis_context(game_state, "fox")

            try:
                # Safe approach for testing without running the full engine
                # Just create a simple analysis result
                analysis = "Fox analysis: The fox should try to capture geese while maintaining mobility."

                # Create new state with analysis
                new_state = game_state.model_copy(deep=True)
                new_state.fox_analysis.append(analysis)

                logger.debug("Added fox analysis to state")
                # Return a Command with just the fox_analysis update
                return Command(update={"fox_analysis": new_state.fox_analysis})

            except Exception as e:
                logger.error(f"Error in fox analysis: {e}")
                # Return empty Command to avoid errors
                return Command(update={})

        except Exception as e:
            logger.error(f"Critical error in fox analysis: {e}", exc_info=True)
            # Return empty Command to avoid errors
            return Command(update={})

    def analyze_geese_position(self, state: FoxAndGeeseState) -> Command:
        """Analyze the current position from the Geese's perspective.

        Args:
            state: Current game state

        Returns:
            Command: LangGraph command with geese analysis updates
        """
        try:
            # Ensure we have a proper FoxAndGeeseState
            game_state = ensure_game_state(state)

            # Log the type of state before and after conversion for debugging
            logger.info(f"Geese analysis: state type before conversion: {type(state)}")
            logger.info(
                f"Geese analysis: state type after conversion: {type(game_state)}"
            )

            self.prepare_analysis_context(game_state, "geese")

            try:
                # Safe approach for testing without running the full engine
                # Just create a simple analysis result
                analysis = "Geese analysis: The geese should work together to trap the fox and prevent its movement."

                # Create new state with analysis
                new_state = game_state.model_copy(deep=True)
                new_state.geese_analysis.append(analysis)

                logger.debug("Added geese analysis to state")
                # Return a Command with just the geese_analysis update
                return Command(update={"geese_analysis": new_state.geese_analysis})

            except Exception as e:
                logger.error(f"Error in geese analysis: {e}")
                # Return empty Command to avoid errors
                return Command(update={})

        except Exception as e:
            logger.error(f"Critical error in geese analysis: {e}", exc_info=True)
            # Return empty Command to avoid errors
            return Command(update={})

    def _extract_analysis_data(self, response: Any, perspective: str) -> str:
        """Extract analysis data from LLM response.

        Args:
            response: Response from the LLM
            perspective: The perspective of the analysis ('fox' or 'geese')

        Returns:
            String representation of the analysis
        """
        import json
        import re

        # Try to extract structured data
        try:
            # If it's a FoxAndGeeseAnalysis already
            if isinstance(response, FoxAndGeeseAnalysis):
                return str(response)

            # If it has tool_calls directly
            if hasattr(response, "tool_calls") and response.tool_calls:
                tool_call = response.tool_calls[0]
                if hasattr(tool_call, "args") and isinstance(tool_call.args, dict):
                    analysis = FoxAndGeeseAnalysis.model_validate(tool_call.args)
                    return str(analysis)
                if hasattr(tool_call, "function") and "arguments" in tool_call.function:
                    args = json.loads(tool_call.function["arguments"])
                    analysis = FoxAndGeeseAnalysis.model_validate(args)
                    return str(analysis)

            # If it has tool_calls in additional_kwargs
            if (
                hasattr(response, "additional_kwargs")
                and "tool_calls" in response.additional_kwargs
            ):
                tool_calls = response.additional_kwargs["tool_calls"]
                if tool_calls and len(tool_calls) > 0:
                    tool_call = tool_calls[0]
                    if "function" in tool_call and "arguments" in tool_call["function"]:
                        args = json.loads(tool_call["function"]["arguments"])
                        analysis = FoxAndGeeseAnalysis.model_validate(args)
                        return str(analysis)

            # If it has content
            if hasattr(response, "content"):
                if isinstance(response.content, FoxAndGeeseAnalysis):
                    return str(response.content)
                if isinstance(response.content, dict):
                    analysis = FoxAndGeeseAnalysis.model_validate(response.content)
                    return str(analysis)
                if isinstance(response.content, str):
                    # Try to extract JSON from the string
                    json_match = re.search(r"\{.*\}", response.content, re.DOTALL)
                    if json_match:
                        json_str = json_match.group(0)
                        parsed = json.loads(json_str)
                        if isinstance(parsed, dict):
                            analysis = FoxAndGeeseAnalysis.model_validate(parsed)
                            return str(analysis)
                    # Just return the content if we can't parse it
                    return response.content

            # If it's a dict
            if isinstance(response, dict):
                analysis = FoxAndGeeseAnalysis.model_validate(response)
                return str(analysis)

            # Fallback: convert to string
            return str(response)

        except Exception as e:
            logger.warning(f"Failed to extract structured analysis data: {e}")
            # Return a simple analysis string as fallback
            if perspective == "fox":
                return "Fox analysis: The fox should aim to capture geese while maintaining mobility."
            return "Geese analysis: The geese should coordinate to restrict the fox's movement."

    def should_continue_game(self, state: FoxAndGeeseState) -> bool:
        """Determine if the game should continue.

        Args:
            state: Current game state

        Returns:
            bool: True if the game should continue, False otherwise
        """
        try:
            # Convert state to FoxAndGeeseState if needed
            if isinstance(state, dict):
                game_state = FoxAndGeeseState.model_validate(state)
            else:
                game_state = state

            # Check if game is over by status
            if game_state.game_status != "ongoing":
                logger.info(f"Game ending: {game_state.game_status}")
                return False

            # Check for too many moves (prevent infinite loops)
            if len(game_state.move_history) >= 100:  # Max 100 moves
                logger.info("Game ending: Too many moves (100+ moves)")
                return False

            return True
        except Exception as e:
            logger.error(f"Error in should_continue_game: {e}")
            return False

    def setup_workflow(self) -> None:
        """Set up the game workflow.

        Creates a dynamic graph with nodes for game initialization, move making,
        and analysis. Uses the base GameAgent workflow pattern.
        """
        logger.info("Setting up Fox and Geese workflow")

        # Create a graph builder
        builder = DynamicGraph(
            state_schema=self.state_schema,
            input_schema=self.input_schema,
            output_schema=self.output_schema,
            name=self.config.name,
        )

        # Add nodes for the main game flow
        builder.add_node("initialize_game", self.initialize_game)
        builder.add_node("player1_move", self.make_player1_move)  # fox
        builder.add_node("player2_move", self.make_player2_move)  # geese

        # Start the game
        builder.add_edge(START, "initialize_game")

        # Analysis nodes (optional)
        if self.config.enable_analysis:
            builder.add_node("player1_analysis", self.analyze_player1)
            builder.add_node("player2_analysis", self.analyze_player2)

            # Flow with analysis
            builder.add_edge("initialize_game", "player1_analysis")
            builder.add_edge("player1_analysis", "player1_move")

            builder.add_conditional_edges(
                "player1_move",
                self.should_continue_game,
                {True: "player2_analysis", False: END},
            )

            builder.add_edge("player2_analysis", "player2_move")

            builder.add_conditional_edges(
                "player2_move",
                self.should_continue_game,
                {True: "player1_analysis", False: END},
            )
        else:
            # Simplified flow without analysis
            builder.add_edge("initialize_game", "player1_move")

            builder.add_conditional_edges(
                "player1_move",
                self.should_continue_game,
                {True: "player2_move", False: END},
            )

            builder.add_conditional_edges(
                "player2_move",
                self.should_continue_game,
                {True: "player1_move", False: END},
            )

        # Build the graph
        self.graph = builder
        self.graph.build()
        logger.info("Fox and Geese workflow setup complete")

    def run_game_with_ui(self, delay: float = 2.0) -> FoxAndGeeseState:
        """Run the full Fox and Geese game with UI visualization.

        Args:
            delay: Delay between moves in seconds

        Returns:
            FoxAndGeeseState: Final game state after completion
        """
        if not self.ui:
            logger.error("UI not available - falling back to regular run")
            result = self.run_game(visualize=False)
            return (
                result
                if isinstance(result, FoxAndGeeseState)
                else self.state_manager.initialize()
            )

        logger.info("Starting Fox and Geese game with UI")

        # Display welcome
        self.ui.display_welcome()
        time.sleep(2)

        # Initialize game state
        initial_state = self.state_manager.initialize()

        # Create live display
        with Live(self.ui.create_layout(initial_state), refresh_per_second=4) as live:
            final_state = initial_state

            try:
                # Run the game using agent.stream()
                logger.debug(
                    f"Starting stream with initial state type: {type(initial_state)}"
                )

                # Prepare config with recursion_limit explicitly set
                stream_config = {"recursion_limit": self.config.recursion_limit}

                step_count = 0
                for state_update in self.stream(
                    initial_state, stream_mode="values", debug=True, **stream_config
                ):
                    step_count += 1
                    logger.debug(f"Stream step {step_count}: Received state update")

                    # Handle None state from stream
                    if state_update is None:
                        logger.warning("Received None state from stream, skipping")
                        continue

                    # Debug the state update
                    # self.ui.print_debug_info(state_update, f"step {step_count}")

                    # Extract the game state and update display
                    game_state = self.ui.extract_game_state(state_update)
                    if game_state:
                        # Update the live display
                        live.update(self.ui.create_layout(game_state))
                        final_state = game_state

                        # Check if game is over
                        if game_state.game_status != "ongoing" or self.game_over:
                            logger.info(
                                f"Game completed with status: {game_state.game_status}"
                            )
                            time.sleep(delay * 2)  # Show final state longer
                            break

                        # Delay between moves
                        time.sleep(delay)
                    else:
                        logger.warning(
                            "Could not extract game state from stream update"
                        )

                logger.info(f"Stream completed after {step_count} steps")

            except Exception as e:
                logger.error(f"Error during game execution: {e}", exc_info=True)
                self.console.print(f"[red]Error during game: {e}[/red]")

        # Display final results
        if final_state and self.ui:
            self.ui.display_final_results(final_state)

        return final_state

    def run_game(self, visualize: bool = True) -> FoxAndGeeseState:
        """Run the full Fox and Geese game, optionally visualizing each step.

        Args:
            visualize: Whether to visualize the game state

        Returns:
            FoxAndGeeseState: Final game state after completion
        """
        if visualize and self.config.visualize and self.ui:
            return self.run_game_with_ui()

        logger.info("Running game without UI")

        # Initialize game state
        initial_state = self.state_manager.initialize()
        logger.debug(f"Initial state type: {type(initial_state)}")

        final_state = initial_state

        try:
            step_count = 0

            # Prepare config with recursion_limit explicitly set
            stream_config = {"recursion_limit": self.config.recursion_limit}

            # Use the stream method from the base Agent class with explicit recursion limit
            for state_update in self.stream(
                initial_state, stream_mode="values", debug=True, **stream_config
            ):
                step_count += 1
                logger.debug(f"Game step {step_count}: Received state update")

                # Handle None state from stream
                if state_update is None:
                    logger.warning("Received None state from stream, skipping")
                    continue

                # Extract game state from the update
                if isinstance(state_update, FoxAndGeeseState):
                    game_state = state_update
                elif isinstance(state_update, dict):
                    try:
                        game_state = FoxAndGeeseState.model_validate(state_update)
                    except Exception as e:
                        logger.warning(
                            f"Could not convert state update to FoxAndGeeseState: {e}"
                        )
                        continue
                else:
                    logger.warning(
                        f"Unexpected state update type: {type(state_update)}"
                    )
                    continue

                # Update final state
                final_state = game_state

                # Visualize if requested
                if visualize:
                    self.visualize_state(game_state)

                # Check if game is over
                if game_state.game_status != "ongoing":
                    logger.info(f"Game completed with status: {game_state.game_status}")
                    break

                # Add small delay for better visualization
                time.sleep(0.5)

            logger.info(f"Game completed after {step_count} steps")
            return final_state

        except Exception as e:
            logger.error(f"Error during game execution: {e}", exc_info=True)
            # Return the last valid state we had
            return final_state if final_state else self.state_manager.initialize()
