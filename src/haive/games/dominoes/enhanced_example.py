#!/usr/bin/env python3
"""Example runner for Dominoes game with enhanced Rich UI visualization."""

import argparse
import time
import traceback
import uuid

from rich.console import Console
from rich.panel import Panel

from haive.games.dominoes.agent import DominoesAgent
from haive.games.dominoes.config import DominoesAgentConfig
from haive.games.dominoes.models import DominoMove, DominoTile
from haive.games.dominoes.rich_ui import DominoesRichUI
from haive.games.dominoes.state import DominoesState
from haive.games.dominoes.ui import DominoesUI

# Set up logging - uncomment to see detailed debug logs
# logging.basicConfig(level=logging.DEBUG)


def run_dominoes_game(
    agent: DominoesAgent, delay: float = 1.2, use_rich_ui: bool = True
):
    """Run a Dominoes game with visualization.

    Args:
        agent: Configured DominoesAgent
        delay: Delay between moves in seconds
        use_rich_ui: Whether to use the enhanced Rich UI (vs. the basic UI)

    Returns:
        The final game state
    """
    console = Console()
    console.print(
        Panel(
            f"Starting Dominoes game with {
                'Enhanced' if use_rich_ui else 'Basic'
            } Rich UI visualization",
            title="🎲 Dominoes Game 🎲",
            border_style="magenta",
        )
    )

    try:
        # Create the appropriate UI
        if use_rich_ui:
            ui = DominoesRichUI(console=console)
        else:
            ui = DominoesUI(console=console)

        # Display welcome message
        ui.display_welcome()
        time.sleep(delay)

        # Run the game with UI
        if use_rich_ui and hasattr(ui, "run_game_with_ui"):
            # The enhanced UI has its own game running method
            final_state = ui.run_game_with_ui(agent, delay=delay)
        else:
            # Use the agent's method for the basic UI
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


def demo_ui_features(delay: float = 0.5):
    """Demonstrate UI features with a sample game state.

    Args:
        delay: Delay between demonstrations in seconds
    """
    console = Console()
    ui = DominoesRichUI(console=console)

    # Create a sample game state
    game_state = DominoesState.initialize()

    # Show the welcome message
    console.print(
        Panel(
            "UI Feature Demonstration",
            title="🎲 Dominoes UI Demo 🎲",
            border_style="magenta",
        )
    )
    time.sleep(delay)

    # Show the welcome screen
    ui.display_welcome()
    time.sleep(delay * 2)

    # Show the initial state
    console.print(Panel("Initial Game State", title="Demo", border_style="cyan"))
    ui.display_state(game_state)
    time.sleep(delay * 2)

    # Show thinking animation
    console.print(Panel("Thinking Animation", title="Demo", border_style="cyan"))
    ui.show_thinking("player1", "Considering my move...")
    time.sleep(delay)
    ui.show_thinking("player2", "Planning my strategy...")
    time.sleep(delay * 2)

    # Create some sample moves

    move1 = DominoMove(tile=DominoTile(left=6, right=6), location="left")
    move2 = DominoMove(tile=DominoTile(left=6, right=3), location="right")

    # Show move animations
    console.print(Panel("Move Animations", title="Demo", border_style="cyan"))
    ui.show_move(move1, "player1")
    time.sleep(delay)
    ui.show_move(move2, "player2")
    time.sleep(delay)
    ui.show_move("pass", "player1")
    time.sleep(delay * 2)

    # Create a more advanced game state
    game_state.board = [DominoTile(left=6, right=6), DominoTile(left=6, right=3)]
    game_state.move_history = [move1, move2]

    # Show the updated state
    console.print(Panel("Game in Progress", title="Demo", border_style="cyan"))
    ui.display_state(game_state)
    time.sleep(delay * 2)

    # Show final results
    game_state.game_status = "player1_win"
    game_state.winner = "player1"
    game_state.scores = {"player1": 50, "player2": 25}

    console.print(Panel("Final Results", title="Demo", border_style="cyan"))
    ui.display_final_results(game_state)


# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Dominoes game with Rich UI")
    parser.add_argument("--demo", action="store_true", help="Run a UI demonstration")
    parser.add_argument(
        "--basic-ui",
        action="store_true",
        help="Use the basic UI instead of enhanced UI",
    )
    parser.add_argument(
        "--delay", type=float, default=1.2, help="Delay between moves in seconds"
    )
    args = parser.parse_args()

    console = Console()

    try:
        if args.demo:
            # Run the UI demo
            demo_ui_features(delay=args.delay)
        else:
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
            run_dominoes_game(agent, delay=args.delay, use_rich_ui=not args.basic_ui)

    except Exception as e:
        console.print(f"[bold red]Critical error: {e}[/bold red]")

        console.print(
            Panel(
                traceback.format_exc(),
                title="Error Details",
                border_style="red",
            )
        )
