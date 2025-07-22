"""Mancala game agent.

This module defines the Mancala game agent, which uses language models
to generate moves and analyze positions in the game.
"""

import json
import logging
import traceback
from typing import Any

from haive.core.engine.agent.agent import register_agent
from haive.core.graph.dynamic_graph_builder import DynamicGraph
from langchain_core.messages import AIMessage
from langgraph.types import Command

from haive.games.framework.base.agent import GameAgent
from haive.games.mancala.config import MancalaConfig
from haive.games.mancala.models import MancalaAnalysis, MancalaMove
from haive.games.mancala.state import MancalaState
from haive.games.mancala.state_manager import MancalaStateManager

# Set up logging
logger = logging.getLogger(__name__)


def ensure_game_state(
    state_input: dict[str, Any] | MancalaState | Command,
) -> MancalaState:
    """Ensure input is converted to MancalaState.

    Args:
        state_input: Input that could be a dict, MancalaState, or Command.

    Returns:
        MancalaState: Properly typed game state.
    """
    if isinstance(state_input, MancalaState):
        return state_input
    if isinstance(state_input, dict):
        return MancalaState(**state_input)
    if isinstance(state_input, Command):
        # For Commands, we assume the update contains the state
        if hasattr(state_input, "update") and state_input.update:
            return MancalaState(**state_input.update)
        return MancalaState()
    return MancalaState()


def extract_data_from_response(
    response: Any, data_type: str = "move"
) -> dict[str, Any] | None:
    """Extract move or analysis data from an LLM response.

    Args:
        response: The response from the LLM.
        data_type: Type of data to extract ('move' or 'analysis').

    Returns:
        Extracted data dictionary or None.
    """
    # If it's already a dict with the expected fields
    if isinstance(response, dict) and (
        (data_type == "move" and "pit_index" in response)
        or (data_type == "analysis" and "position_evaluation" in response)
    ):
        return response

    # If it's an AIMessage, try to extract from tool calls
    if isinstance(response, AIMessage):
        if hasattr(response, "tool_calls") and response.tool_calls:
            for tool_call in response.tool_calls:
                if "args" in tool_call:
                    return tool_call["args"]

        # Also check additional_kwargs
        if hasattr(response, "additional_kwargs"):
            tool_calls = response.additional_kwargs.get("tool_calls", [])
            if tool_calls and len(tool_calls) > 0:
                tool_call = tool_calls[0]
                if "function" in tool_call and "arguments" in tool_call["function"]:
                    try:
                        args = json.loads(tool_call["function"]["arguments"])
                        return args
                    except json.JSONDecodeError as e:
                        logger.exception(f"Failed to parse JSON: {e}")

    # For other message types with tool_calls
    if hasattr(response, "tool_calls") and response.tool_calls:
        for tool_call in response.tool_calls:
            if isinstance(tool_call, dict) and "args" in tool_call:
                return tool_call["args"]

    return None


@register_agent(MancalaConfig)
class MancalaAgent(GameAgent[MancalaConfig]):
    """Agent for playing Mancala using language models.

    This agent uses LLMs to generate moves and analyze positions
    in the Mancala game. It builds a dynamic graph for game flow
    and uses structured outputs for reliable move generation.

    Attributes:
        config: Configuration for the Mancala game.
        graph_builder: Dynamic graph builder for game flow.
        state_manager: Manager for game state transitions.
    """

    def __init__(self, config: MancalaConfig) -> None:
        """Initialize the Mancala agent.

        Args:
            config: Configuration for the Mancala game.
        """
        super().__init__(config)
        self.state_manager = MancalaStateManager()
        self._build_graph()

    def _build_graph(self) -> None:
        """Build the game flow graph."""
        try:
            self.graph_builder = self._create_graph_structure()
            self._app = self.graph_builder.build()
        except Exception as e:
            logger.exception(f"Failed to build graph: {e}")
            # Fall back to a simple structure
            self.graph_builder = self._create_simple_graph()
            self._app = self.graph_builder.build()

    def _create_graph_structure(self) -> DynamicGraph:
        """Create the full graph structure for the game.

        Returns:
            DynamicGraph configured for Mancala gameplay.
        """
        graph_builder = DynamicGraph(state_schema=MancalaState)

        # Add conditional edges
        graph_builder.add_conditional_edges(
            "check_game_over",
            lambda x: "end" if x.game_status == "ended" else "continue",
            {"end": "__end__", "continue": "player_turn"},
        )

        graph_builder.add_conditional_edges(
            "player_turn",
            lambda x: x.turn,
            {"player1": "player1_turn", "player2": "player2_turn"},
        )

        graph_builder.add_conditional_edges(
            "after_move",
            lambda x: "extra_turn" if x.free_turn else "normal",
            {"extra_turn": "player_turn", "normal": "check_game_over"},
        )

        # Set entry point
        graph_builder.set_entry_point("check_game_over")

        # Add nodes
        graph_builder.add_node("check_game_over", self.check_game_over)
        graph_builder.add_node("player_turn", lambda x: x)
        graph_builder.add_node("player1_turn", self.player1_turn)
        graph_builder.add_node("player2_turn", self.player2_turn)
        graph_builder.add_node("after_move", lambda x: x)

        # Add edges
        graph_builder.add_edge("player1_turn", "after_move")
        graph_builder.add_edge("player2_turn", "after_move")

        return graph_builder

    def _create_simple_graph(self) -> DynamicGraph:
        """Create a simplified graph structure as fallback.

        Returns:
            Simplified DynamicGraph for basic gameplay.
        """
        graph_builder = DynamicGraph(state_schema=MancalaState)
        graph_builder.set_entry_point("play")
        graph_builder.add_node("play", self.simple_play)
        graph_builder.set_finish_point("play")
        return graph_builder

    def simple_play(self, state: MancalaState) -> MancalaState:
        """Simple play logic for fallback mode.

        Args:
            state: Current game state.

        Returns:
            Updated game state.
        """
        state = ensure_game_state(state)
        if state.game_status == "ended":
            return state

        # Make move based on current turn
        state = (
            self.player1_turn(state)
            if state.turn == "player1"
            else self.player2_turn(state)
        )

        # Check game over
        return self.check_game_over(state)

    def check_game_over(self, state: MancalaState) -> MancalaState:
        """Check if the game is over and update state accordingly.

        Args:
            state: Current game state.

        Returns:
            Updated game state.
        """
        state = ensure_game_state(state)
        if state.is_game_over():
            state.game_status = "ended"
            state.winner = state.determine_winner()
        return state

    def player1_turn(self, state: MancalaState) -> MancalaState:
        """Execute player 1's turn.

        Args:
            state: Current game state.

        Returns:
            Updated game state after player 1's move.
        """
        state = ensure_game_state(state)
        return self.make_move(state, "player1")

    def player2_turn(self, state: MancalaState) -> MancalaState:
        """Execute player 2's turn.

        Args:
            state: Current game state.

        Returns:
            Updated game state after player 2's move.
        """
        state = ensure_game_state(state)
        return self.make_move(state, "player2")

    def make_move(self, state: MancalaState, player: str) -> MancalaState:
        """Make a move for the specified player.

        This method handles move generation, validation, and state updates.
        It includes retry logic for invalid moves and fallback to random
        valid moves if the LLM fails.

        Args:
            state: Current game state.
            player: Player making the move ('player1' or 'player2').

        Returns:
            Updated game state after the move.
        """
        state = ensure_game_state(state)
        valid_moves = state.get_valid_moves(player)

        if not valid_moves:
            logger.warning(f"No valid moves for {player}")
            return state

        # Get the engine for this player
        engine = self.engines.get(player)
        if not engine:
            logger.error(f"No engine configured for {player}")
            # Fallback to first valid move
            move = MancalaMove(pit_index=valid_moves[0], player=player)
            return self._apply_move(state, move)

        # Prepare the prompt
        prompt_data = self._prepare_move_prompt(state, player, valid_moves)

        # Try to get a valid move from the LLM
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                logger.info(f"Attempt {attempt + 1} for {player}")
                response = engine.invoke(prompt_data)

                # Extract move from response
                move_data = extract_data_from_response(response, "move")

                if move_data and "pit_index" in move_data:
                    pit_index = move_data["pit_index"]

                    # Validate the move
                    if pit_index in valid_moves:
                        move = MancalaMove(pit_index=pit_index, player=player)
                        return self._apply_move(state, move)
                    logger.warning(f"Invalid move {pit_index} not in {valid_moves}")
                else:
                    logger.warning("Could not extract move from response")

            except Exception as e:
                logger.exception(f"Error in attempt {attempt + 1}: {e}")
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(traceback.format_exc())

        # Fallback to first valid move
        logger.warning(f"All attempts failed for {player}, using fallback")
        move = MancalaMove(pit_index=valid_moves[0], player=player)
        return self._apply_move(state, move)

    def _prepare_move_prompt(
        self, state: MancalaState, player: str, valid_moves: list[int]
    ) -> dict[str, Any]:
        """Prepare the prompt data for move generation.

        Args:
            state: Current game state.
            player: Player making the move.
            valid_moves: List of valid move indices.

        Returns:
            Dictionary with prompt data for the LLM.
        """
        return {
            "board_state": state.display_board(),
            "current_player": player,
            "valid_moves": valid_moves,
            "scores": state.get_scores(),
            "move_history": [
                f"{m.player}: pit {m.pit_index}" for m in state.move_history[-5:]
            ],
        }

    def _apply_move(self, state: MancalaState, move: MancalaMove) -> MancalaState:
        """Apply a move to the game state.

        Args:
            state: Current game state.
            move: Move to apply.

        Returns:
            Updated game state.
        """
        try:
            # Apply the move using state manager
            new_state = self.state_manager.apply_move(state, move)

            # Analyze position if enabled
            if self.config.enable_analysis:
                new_state = self._analyze_position(new_state, move.player)

            return new_state

        except Exception as e:
            logger.exception(f"Failed to apply move: {e}")
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(traceback.format_exc())
            return state

    def _analyze_position(self, state: MancalaState, player: str) -> MancalaState:
        """Analyze the current position for the specified player.

        Args:
            state: Current game state.
            player: Player to analyze for.

        Returns:
            State with analysis added.
        """
        engine = self.engines.get(player)
        if not engine:
            return state

        try:
            prompt_data = {
                "board_state": state.display_board(),
                "current_player": player,
                "scores": state.get_scores(),
                "game_status": state.game_status,
            }

            response = engine.invoke(prompt_data)
            analysis_data = extract_data_from_response(response, "analysis")

            if analysis_data:
                analysis = MancalaAnalysis(**analysis_data)
                if player == "player1":
                    state.player1_analysis.append(analysis)
                else:
                    state.player2_analysis.append(analysis)

        except Exception as e:
            logger.exception(f"Failed to analyze position: {e}")

        return state
