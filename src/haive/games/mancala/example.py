#!/usr/bin/env python3
"""Example of playing a Mancala game.

This script demonstrates how to initialize and run a Mancala game
with the Haive framework. It provides a rich terminal UI and handles
various configuration options.

Usage:
    python example.py [--stones=4] [--no-analysis] [--no-visual] [--debug]

Options:
    --stones=N       Set the number of stones per pit (default: 4)
    --no-analysis    Disable position analysis
    --no-visual      Disable visualization
    --debug          Enable debug output

"""

import argparse
import logging
import traceback
import uuid

from haive.core.config.runnable import RunnableConfigManager
from rich.console import Console
from rich.panel import Panel

from haive.games.mancala.agent import MancalaAgent
from haive.games.mancala.config import MancalaConfig


def main():
    """Run the Mancala game demo."""
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run a Mancala game demo")
    parser.add_argument(
        "--stones", type=int, default=4, help="Number of stones per pit"
    )
    parser.add_argument(
        "--no-analysis", action="store_true", help="Disable position analysis"
    )
    parser.add_argument(
        "--no-visual", action="store_true", help="Disable visualization"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    # Set up logging
    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=log_level)
    logger = logging.getLogger("mancala_demo")

    # Create a console for rich output
    console = Console()

    # Display header
    console.print(
        Panel.fit(
            "[bold cyan]Mancala Game Demo[/bold cyan]\n"
            "An ancient board game of strategy and counting",
            border_style="cyan",
        )
    )

    try:
        # Import the MancalaAgent

        # Display configuration
        console.print("[bold]Game Configuration:[/bold]")
        console.print(f"• Stones per pit: {args.stones}")
        console.print(
            f"• Position analysis: {'disabled' if args.no_analysis else 'enabled'}"
        )
        console.print(f"• Visualization: {'disabled' if args.no_visual else 'enabled'}")
        console.print(f"• Debug mode: {'enabled' if args.debug else 'disabled'}")
        console.print()

        # Initialize the agent with configuration and increased recursion limit

        # Create a runnable config with higher recursion limit
        runnable_config = RunnableConfigManager.create(
            thread_id=str(uuid.uuid4()),
            recursion_limit=200,  # Increase from default 25 to avoid recursion limit errors
        )

        config = MancalaConfig(
            stones_per_pit=args.stones,
            enable_analysis=not args.no_analysis,
            visualize=not args.no_visual,
            runnable_config=runnable_config,
        )
        agent = MancalaAgent(config)

        console.print("[bold yellow]Starting game...[/bold yellow]")
        console.print("(This may take a moment to initialize the LLM engines)")
        console.print()

        # Run the game
        final_state = agent.run({"initialize": {"stones_per_pit": args.stones}})

        # Display final result
        if final_state:
            console.print(
                Panel.fit(
                    f"[bold green]Game Complete![/bold green]\n"
                    f"Final Score: Player 1: {final_state.player1_score}, Player 2: {final_state.player2_score}\n"
                    f"Winner: {final_state.winner or 'Draw'}",
                    border_style="green",
                )
            )
        else:
            console.print(
                Panel.fit(
                    "[bold yellow]Game ended without returning a final state[/bold yellow]\n"
                    "This might happen if an error occurred during gameplay.",
                    border_style="yellow",
                )
            )

    except ModuleNotFoundError as e:
        console.print(
            Panel.fit(
                "[bold red]Error: Required module not found[/bold red]\n"
                f"{e!s}\n\n"
                "This example requires the Haive framework and its dependencies.\n"
                "If you want to test the core Mancala logic without these dependencies,\n"
                "try running 'minimal_test.py' instead.",
                border_style="red",
            )
        )

    except Exception as e:
        console.print(
            Panel.fit(
                f"[bold red]Error running game:[/bold red]\n{e!s}",
                border_style="red",
            )
        )
        if args.debug:
            traceback.print_exc()
        else:
            console.print("Run with --debug flag for detailed error information.")


if __name__ == "__main__":
    main()
