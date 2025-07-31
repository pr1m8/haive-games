#!/usr/bin/env python3
"""Example runner for Dominoes game with rich UI visualization."""

import traceback
import uuid

from rich.console import Console
from rich.panel import Panel

from haive.games.dominoes.agent import DominoesAgent
from haive.games.dominoes.config import DominoesAgentConfig

# Set up logging - uncomment to see detailed debug logs
# logging.basicConfig(level=logging.DEBUG)


def run_dominoes_game(agent: DominoesAgent, delay: float = 1.5):
    """Run a Dominoes game with visualization.

    Args:
        agent: Configured DominoesAgent
        delay: Delay between moves in seconds

    """
    console = Console()
    console.print(
        Panel(
            "Starting Dominoes game with Rich UI visualization",
            title="🎲 Dominoes Game 🎲",
            border_style="magenta",
        )
    )

    try:
        # Run the game with UI
        final_state = agent.run_game_with_ui(delay=delay)

        # Print final message
        console.print("\n")
        console.print(
            Panel(
                "Game has completed! Thanks for playing!",
                title="🎲 Game Complete 🎲",
                border_style="green",
            )
        )
        return final_state

    except Exception as e:
        console.print(f"[bold red]Error running game: {e}[/bold red]")

        console.print(
            Panel(
                traceback.format_exc(),
                title="Error Details",
                border_style="red",
            )
        )
        return None


# Entry point
if __name__ == "__main__":
    console = Console()

    try:
        # Create agent config with a unique ID for the session
        config = DominoesAgentConfig(
            name="dominoes_game",
            runnable_config={
                "configurable": {
                    "thread_id": uuid.uuid4().hex[:8],
                    "recursion_limit": 400,
                }
            },
        )

        # Create agent
        agent = DominoesAgent(config)

        # Run the game
        run_dominoes_game(agent, delay=1.2)

    except Exception as e:
        console.print(f"[bold red]Critical error: {e}[/bold red]")

        console.print(
            Panel(
                traceback.format_exc(),
                title="Error Details",
                border_style="red",
            )
        )
