#!/usr/bin/env python3
"""Example of playing a Mancala game.

This script demonstrates how to initialize and run a Mancala game
with the Haive framework.
"""

import logging
import time

from rich.console import Console
from rich.panel import Panel

# Set up logging
logging.basicConfig(level=logging.INFO)

# Import the MancalaAgent
from haive.games.mancala.agent import MancalaAgent
from haive.games.mancala.config import MancalaConfig

# Create a console for rich output
console = Console()

console.print(
    Panel.fit(
        "[bold cyan]Mancala Game Demo[/bold cyan]\n"
        "An ancient board game of strategy and counting",
        border_style="cyan",
    )
)

# Initialize the agent with configuration
config = MancalaConfig(stones_per_pit=4)
agent = MancalaAgent(config)

try:
    # Run the game with visualization
    final_state = agent.run_game(visualize=True, debug=True)

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

except Exception as e:
    console.print(
        Panel.fit(
            f"[bold red]Error running game:[/bold red]\n{str(e)}", border_style="red"
        )
    )
    import traceback

    traceback.print_exc()
