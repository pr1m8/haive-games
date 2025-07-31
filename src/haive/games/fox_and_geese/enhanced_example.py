#!/usr/bin/env python3
"""Enhanced example runner for Fox and Geese game with Rich UI
visualization."""

import argparse
import time
import uuid

from rich.console import Console
from rich.panel import Panel

from haive.games.fox_and_geese.agent import FoxAndGeeseAgent
from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.fox_and_geese.rich_ui import FoxAndGeeseRichUI
from haive.games.fox_and_geese.state import FoxAndGeeseState
from haive.games.fox_and_geese.ui import FoxAndGeeseUI

# Set up logging - uncomment to see detailed debug logs
# logging.basicConfig(level=logging.DEBUG)


def run_fox_and_geese_game(
    agent: FoxAndGeeseAgent, delay: float = 1.5, use_rich_ui: bool = True
):
    """Run a Fox and Geese game with visualization.

    Args:
        agent: Configured FoxAndGeeseAgent
        delay: Delay between moves in seconds
        use_rich_ui: Whether to use the enhanced Rich UI (vs. the basic UI)

    Returns:
        The final game state
    """
    console = Console()
    console.print(
        Panel(
            f"Starting Fox and Geese game with {
                'Enhanced' if use_rich_ui else 'Basic'
            } Rich UI visualization",
            title="🦊 Fox and Geese Game 🪿",
            border_style="magenta",
        )
    )

    try:
        # Create the appropriate UI
        if use_rich_ui:
            ui = FoxAndGeeseRichUI(console=console)
        else:
            ui = FoxAndGeeseUI(console=console)

        # Display welcome message
        ui.display_welcome()
        time.sleep(delay)

        # Run the game with UI
        if use_rich_ui and hasattr(ui, "run_fox_and_geese_game"):
            # The enhanced UI has its own game running method
            final_state = ui.run_fox_and_geese_game(agent, delay=delay)
        else:
            # Use the agent's method for the basic UI
            if hasattr(agent, "ui"):
                agent.ui = ui
            final_state = agent.run_game_with_ui(delay=delay)

        # Print final message
        console.print("\n")
        console.print(
            Panel(
                "Game has completed! Thanks for playing!",
                title="🎮 Game Complete 🎮",
                border_style="green",
            )
        )
        return final_state

    except Exception as e:
        console.print(f"[bold red]Error running game: {e}[/bold red]")
        import traceback

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
    ui = FoxAndGeeseRichUI(console=console)

    # Create a sample game state
    game_state = FoxAndGeeseState.initialize()

    # Show the welcome message
    console.print(
        Panel(
            "UI Feature Demonstration",
            title="🦊 Fox and Geese UI Demo 🪿",
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
    ui.show_thinking("fox", "Considering my move...")
    time.sleep(delay)
    ui.show_thinking("geese", "Planning our strategy...")
    time.sleep(delay * 2)

    # Create some sample moves and positions to highlight
    fox_pos = FoxAndGeesePosition(row=3, col=3)
    move1 = FoxAndGeeseMove(
        from_pos=fox_pos,
        to_pos=FoxAndGeesePosition(row=2, col=2),
        piece_type="fox",
        capture=None,
    )

    # Add a sample move to the history
    game_state.move_history.append(move1)

    # Update the fox position
    game_state.fox_position = move1.to_pos

    # Create sample legal moves
    legal_moves = [
        FoxAndGeeseMove(
            from_pos=game_state.fox_position,
            to_pos=FoxAndGeesePosition(row=1, col=1),
            piece_type="fox",
            capture=None,
        ),
        FoxAndGeeseMove(
            from_pos=game_state.fox_position,
            to_pos=FoxAndGeesePosition(row=3, col=1),
            piece_type="fox",
            capture=None,
        ),
        FoxAndGeeseMove(
            from_pos=game_state.fox_position,
            to_pos=FoxAndGeesePosition(row=1, col=3),
            piece_type="fox",
            capture=None,
        ),
    ]

    # Show the state with highlighted positions
    console.print(Panel("Highlighted Positions", title="Demo", border_style="cyan"))
    highlight_positions = {
        FoxAndGeesePosition(row=1, col=1),
        FoxAndGeesePosition(row=3, col=1),
    }
    ui.display_state(
        game_state, highlight_positions=highlight_positions, legal_moves=legal_moves
    )
    time.sleep(delay * 2)

    # Create a capture move
    capture_move = FoxAndGeeseMove(
        from_pos=game_state.fox_position,
        to_pos=FoxAndGeesePosition(row=0, col=0),
        piece_type="fox",
        capture=FoxAndGeesePosition(row=1, col=1),
    )

    # Show capture animation
    console.print(Panel("Capture Animation", title="Demo", border_style="cyan"))
    ui.show_move(capture_move, game_state, game_state)
    time.sleep(delay * 2)

    # Update game state to simulate game progress
    game_state.fox_position = capture_move.to_pos
    game_state.move_history.append(capture_move)
    game_state.num_geese -= 1

    # Remove a captured goose
    if capture_move.capture in game_state.geese_positions:
        game_state.geese_positions.remove(capture_move.capture)

    # Show game in progress
    console.print(Panel("Game in Progress", title="Demo", border_style="cyan"))
    ui.display_state(game_state)
    time.sleep(delay * 2)

    # Show final results
    game_state.game_status = "fox_win"
    game_state.winner = "fox"

    console.print(Panel("Final Results", title="Demo", border_style="cyan"))
    ui.display_final_results(game_state)


# Entry point
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the Fox and Geese game with Rich UI"
    )
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
            # Create agent config
            config = FoxAndGeeseConfig(
                name="fox_and_geese_game",
                enable_analysis=True,
                visualize=True,
                runnable_config={
                    "configurable": {
                        "thread_id": uuid.uuid4().hex[:8],
                        "recursion_limit": 400,
                    }
                },
            )

            # Create agent
            agent = FoxAndGeeseAgent(config)

            try:
                # Run the game in basic UI mode only for now
                run_fox_and_geese_game(agent, delay=args.delay, use_rich_ui=False)
            except Exception as e:
                console.print(f"[bold red]Error running game: {e}[/bold red]")
                traceback.print_exc()

    except Exception as e:
        console.print(f"[bold red]Critical error: {e}[/bold red]")
        import traceback

        console.print(
            Panel(
                traceback.format_exc(),
                title="Error Details",
                border_style="red",
            )
        )

import traceback
