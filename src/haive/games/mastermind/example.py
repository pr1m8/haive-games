#!/usr/bin/env python3
"""Example script for running the Mastermind game.

This script demonstrates how to initialize and run the Mastermind game
with various configuration options.
"""

import argparse
import random
import sys

from .mastermind.agent import MastermindAgent
from .mastermind.config import MastermindConfig


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run the Mastermind game")
    parser.add_argument(
        "--codemaker",
        choices=["player1", "player2"],
        default="player1",
        help="Player who creates the secret code (default: player1)",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=10,
        help="Maximum number of turns (default: 10)",
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        default=True,
        help="Enable visualization (default: True)",
    )
    parser.add_argument(
        "--rich-ui",
        action="store_true",
        default=True,
        help="Use Rich UI if available (default: True)",
    )
    parser.add_argument(
        "--random-code",
        action="store_true",
        default=True,
        help="Use a random secret code (default: True)",
    )
    return parser.parse_args()


def main():
    """Run the Mastermind game with the specified configuration."""
    args = parse_args()

    # Define available colors
    available_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

    # Generate a random secret code or use a fixed one
    if args.random_code:
        secret_code = random.sample(available_colors, 4)
        print(f"Generated random secret code: {secret_code}")
    else:
        # Fixed code for testing
        secret_code = ["red", "blue", "green", "yellow"]
        print(f"Using fixed secret code: {secret_code}")

    # Create config
    config = MastermindConfig(
        codemaker=args.codemaker,
        max_turns=args.max_turns,
        visualize=args.visualize,
        colors=available_colors,
        secret_code=secret_code,
        enable_analysis=True,
    )

    # Create and run agent
    agent = MastermindAgent(config=config)

    # Run with Rich UI if requested
    if args.rich_ui:
        agent.run_game_with_ui()
    else:
        agent.run_game(visualize=args.visualize)

    return 0


if __name__ == "__main__":
    sys.exit(main())
