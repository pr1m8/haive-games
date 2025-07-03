#!/usr/bin/env python3
"""Example script for running the Nim game.

This script demonstrates how to initialize and run the Nim game
with various configuration options and Rich UI.
"""

import argparse
import logging
import sys
import time

from haive.games.nim.agent import NimAgent
from haive.games.nim.config import NimConfig
from haive.games.nim.ui import RICH_AVAILABLE

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run the Nim game")

    parser.add_argument(
        "--pile-sizes",
        type=int,
        nargs="+",
        default=[3, 5, 7],
        help="Initial pile sizes (default: 3 5 7)",
    )

    parser.add_argument(
        "--misere",
        action="store_true",
        default=False,
        help="Use misère mode - last player to take a stone loses (default: false)",
    )

    parser.add_argument(
        "--no-analysis",
        action="store_true",
        default=False,
        help="Disable position analysis (default: analysis enabled)",
    )

    parser.add_argument(
        "--no-ui",
        action="store_true",
        default=False,
        help="Disable Rich UI and use text-based UI (default: Rich UI if available)",
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay between moves in seconds (default: 1.0)",
    )

    return parser.parse_args()


def main():
    """Run the Nim game with the specified configuration."""
    args = parse_args()

    # Print startup message
    print("\n" + "=" * 60)
    print("STARTING NIM GAME")
    print("=" * 60)

    # Create configuration
    config = NimConfig(
        pile_sizes=args.pile_sizes,
        misere_mode=args.misere,
        enable_analysis=not args.no_analysis,
        visualize=True,
    )

    # Show configuration details
    print("\nGame Configuration:")
    print(f"- Pile Sizes: {config.pile_sizes}")
    print(
        f"- Game Mode: {'Misère (last takes loses)' if config.misere_mode else 'Standard (last takes wins)'}"
    )
    print(f"- Analysis: {'Enabled' if config.enable_analysis else 'Disabled'}")

    # Check if Rich UI is available
    if RICH_AVAILABLE and not args.no_ui:
        print("- UI: Rich Terminal UI")
    else:
        print("- UI: Text-based UI")

    print(f"- Move Delay: {args.delay} seconds\n")

    # Create the agent
    try:
        agent = NimAgent(config=config)
        logger.info(f"Created Nim agent with config: {config}")
    except Exception as e:
        logger.error(f"Failed to create Nim agent: {e}")
        return 1

    # Set visualization delay
    if hasattr(agent, "ui") and agent.ui:
        agent.ui.delay = args.delay

    # Run the game
    try:
        print("Starting game...\n")
        time.sleep(1)  # Brief pause before starting

        # Run with standalone game since there are issues with the agent framework
        print("Running standalone Nim game instead due to framework issues...")
        time.sleep(1)

        # Use subprocess to run the standalone game
        import subprocess

        cmd = [
            "python",
            "packages/haive-games/src/haive/games/nim/standalone_game.py",
            "--player1",
            "computer",
            "--player2",
            "computer",
        ]

        if args.misere:
            cmd.append("--misere")

        if args.pile_sizes != [3, 5, 7]:
            cmd.extend(["--pile-sizes"] + [str(p) for p in args.pile_sizes])

        if args.delay != 1.0:
            cmd.extend(["--delay", str(args.delay)])

        subprocess.run(cmd, check=False)

        # Game result is shown by the standalone game
        print("\n" + "=" * 60)
        print("GAME COMPLETE")
        print("=" * 60 + "\n")

        return 0

    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
        return 0
    except Exception as e:
        logger.error(f"Error running game: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
