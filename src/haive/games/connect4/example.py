"""Connect4 example module.

This module provides an example of running a Connect4 game with LLM agents
using the rich UI visualization.

It demonstrates how to:
    - Configure and initialize the Connect4 agent
    - Set up the game state
    - Visualize the game with the rich UI
    - Stream and process game steps
    - Handle game over conditions

The module uses a standard CLI interface with argument parsing
to allow customization of game behavior.

Example:
    Run this script directly to start a Connect4 game:
        python -m haive.games.connect4.example

    Command-line options:
        --debug: Enable debug mode with detailed logging
        --analysis: Enable position analysis
        --delay: Set delay between moves in seconds (default: 1.0)
"""

import argparse
import logging
import random
import time
import traceback
import uuid

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.models import (
    Connect4Analysis,
    Connect4Move,
    Connect4PlayerDecision,
)
from haive.games.connect4.state_manager import Connect4StateManager
from haive.games.connect4.ui import Connect4UI

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_connect4_game(
    debug: bool = False, enable_analysis: bool = False, delay: float = 1.0
):
    """Run a Connect4 game with rich UI visualization.

    This function sets up and runs a Connect4 game using mock moves (for testing)
    with rich terminal visualization. It handles a simplified game flow with
    a few predetermined moves for UI testing.

    Args:
        debug (bool): Enable debug mode with detailed logging
        enable_analysis (bool): Enable position analysis during gameplay
        delay (float): Delay between moves in seconds for better readability

    Returns:
        None

    Example:
        >>> run_connect4_game(debug=True, enable_analysis=True, delay=0.5)
        # Runs a test game with debug logging, position analysis, and 0.5s delay
    """
    # Create the UI
    ui = Connect4UI()

    try:
        # Initialize game state
        state = Connect4StateManager.initialize()

        # Display initial state
        ui.display_state(state)
        time.sleep(delay)

        # Predefined moves for testing (red plays odd-indexed moves, yellow plays even-indexed)
        test_moves = [
            Connect4Move(column=3, explanation="Control the center"),  # Red's move
            Connect4Move(column=4, explanation="Block center control"),  # Yellow's move
            Connect4Move(column=3, explanation="Build up in center"),  # Red's move
            Connect4Move(
                column=2, explanation="Prepare diagonal threat"
            ),  # Yellow's move
            Connect4Move(column=3, explanation="Continue center stack"),  # Red's move
        ]

        # Make sample analysis for testing
        sample_analysis = {
            "red": Connect4Analysis(
                position_score=0.5,
                center_control=7,
                threats={"winning_moves": [], "blocking_moves": [4]},
                suggested_columns=[3, 2, 4],
                winning_chances=65,
            ),
            "yellow": Connect4Analysis(
                position_score=-0.2,
                center_control=3,
                threats={"winning_moves": [], "blocking_moves": [3]},
                suggested_columns=[4, 2, 5],
                winning_chances=40,
            ),
        }

        # Play each move in sequence
        for i, move in enumerate(test_moves):
            # Determine current player
            player = "red" if i % 2 == 0 else "yellow"

            # Show thinking animation
            ui.show_thinking(player)
            time.sleep(delay * 0.5)

            # Apply the move
            state = Connect4StateManager.apply_move(state, move)

            # If analysis is enabled, add analysis to state
            if enable_analysis:
                if player == "red":
                    state.red_analysis.append(sample_analysis["red"].model_dump())
                else:
                    state.yellow_analysis.append(sample_analysis["yellow"].model_dump())

            # Show the move being made
            ui.show_move(move, player)
            time.sleep(delay * 0.5)

            # Display updated state
            ui.display_state(state)
            time.sleep(delay)

        # Show game end (example: declare red as winner for testing)
        state.game_status = "red_win"
        state.winner = "red"
        ui.display_state(state)
        ui.show_game_over("red")

    except Exception as e:
        logger.error(f"Setup error: {e}")
        traceback.print_exc()

    logger.info("Game complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Connect4 game with rich UI")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument(
        "--analysis", action="store_true", help="Enable position analysis"
    )
    parser.add_argument(
        "--delay", type=float, default=1.0, help="Delay between moves (seconds)"
    )

    args = parser.parse_args()

    # Set logging level based on debug flag
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    # Run the game
    run_connect4_game(debug=args.debug, enable_analysis=args.analysis, delay=args.delay)
