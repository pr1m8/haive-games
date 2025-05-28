#!/usr/bin/env python3
"""Simple runner for Fox and Geese game."""

import logging
import time
import uuid
from typing import Optional

from rich.console import Console
from rich.panel import Panel

from haive.games.fox_and_geese.agent import FoxAndGeeseAgent
from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.state import FoxAndGeeseState

# Set up logging - uncomment to see detailed debug logs
# logging.basicConfig(level=logging.DEBUG)


def run_fox_and_geese_game(agent: FoxAndGeeseAgent, thread_id: Optional[str] = None):
    """Run a Fox and Geese game using agent.run()."""
    console = Console()

    # Generate or use thread_id for persistence
    thread_id = thread_id or f"fox_geese_thread_{uuid.uuid4().hex[:8]}"
    console.print(f"🧵 Using thread_id: [cyan]{thread_id}[/cyan]")

    # Initialize the game state
    initial_state = agent.state_manager.initialize()
    console.print(
        Panel(
            f"🦊 Fox at position: {initial_state.fox_position}\n"
            f"🪿 {initial_state.num_geese} geese on the board",
            title="🎮 Starting Fox and Geese game",
            border_style="green",
        )
    )

    try:
        # Run the full agent workflow until END
        final_state = agent.run(initial_state, thread_id=thread_id)

        # Display final game outcome
        console.print("\n")
        console.print(
            Panel(
                f"🎯 Winner: [bold]{final_state.winner or 'None'}[/bold]\n"
                f"📊 Game Status: [bold]{final_state.game_status}[/bold]\n"
                f"🔢 Total moves: [bold]{len(final_state.move_history)}[/bold]\n"
                f"🪿 Geese remaining: [bold]{final_state.num_geese}[/bold]",
                title="🏁 Game Over!",
                border_style="yellow",
            )
        )

        # Display last few moves
        if final_state.move_history:
            moves_text = "\n".join(
                [f"   - {move}" for move in final_state.move_history[-5:]]
            )
            console.print(
                Panel(moves_text, title="📜 Recent moves", border_style="blue")
            )

        # Display analyses if available
        if hasattr(final_state, "fox_analysis") and final_state.fox_analysis:
            console.print(
                Panel(
                    final_state.fox_analysis[-1],
                    title="🦊 Fox Analysis",
                    border_style="red",
                )
            )

        if hasattr(final_state, "geese_analysis") and final_state.geese_analysis:
            console.print(
                Panel(
                    final_state.geese_analysis[-1],
                    title="🪿 Geese Analysis",
                    border_style="cyan",
                )
            )

        return final_state

    except Exception as e:
        console.print(f"[bold red]Error running game: {e}[/bold red]")
        return None


def run_fox_and_geese_with_ui(agent: FoxAndGeeseAgent, delay: float = 2.0):
    """Run a Fox and Geese game with UI visualization."""
    console = Console()
    console.print(
        Panel(
            "Starting Fox and Geese game with Rich UI",
            title="🎮 Fox and Geese",
            border_style="cyan",
        )
    )

    try:
        # Run the game with UI
        final_state = agent.run_game_with_ui(delay=delay)

        console.print("\n")
        console.print(
            Panel("Game has completed!", title="🏁 Game Complete", border_style="green")
        )
        return final_state

    except Exception as e:
        console.print(f"[bold red]Error running game with UI: {e}[/bold red]")
        return None


# Entry point
if __name__ == "__main__":
    console = Console()

    try:
        # Create agent config
        config = FoxAndGeeseConfig(
            name="fox_and_geese_game",
            enable_analysis=True,
            visualize=True,
            runnable_config={
                "configurable": {
                    "thread_id": uuid.uuid4().hex[:8],
                    "recursion_limit": 100,
                }
            },
        )

        # Create agent
        agent = FoxAndGeeseAgent(config)

        # Choose run mode
        console.print(
            Panel(
                "1. Run with Rich UI (recommended)\n" "2. Run in console mode",
                title="🎮 Fox and Geese Game Options",
                border_style="cyan",
            )
        )

        choice = input("Enter choice (1 or 2): ").strip()

        if choice == "1":
            run_fox_and_geese_with_ui(agent, delay=1.5)
        else:
            run_fox_and_geese_game(agent)

    except Exception as e:
        console.print(f"[bold red]Critical error: {e}[/bold red]")
        import traceback

        console.print(
            Panel(traceback.format_exc(), title="Error Details", border_style="red")
        )
