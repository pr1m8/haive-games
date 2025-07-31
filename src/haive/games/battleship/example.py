"""Main script to run the Battleship game.

This module provides a standalone command-line interface for running
the Battleship game with LLM-powered agents. It features:
    - Rich text-based visualization of game boards and states
    - Command-line options for customizing game behavior
    - Progress tracking and game statistics
    - Error handling and graceful termination

Run this script directly to start a Battleship game:
    python -m haive.games.battleship.example

Command-line options:
    --no-visual: Disable board visualization
    --no-analysis: Disable strategic analysis
    --debug: Enable debug mode with detailed logs
    --delay: Set delay between game steps (default: 0.5s)

"""

import argparse
import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table

from haive.games.battleship.agent import BattleshipAgent
from haive.games.battleship.config import BattleshipAgentConfig
from haive.games.battleship.models import GamePhase
from haive.games.battleship.utils import visualize_board

# Import battleship components

# Create console for rich output
console = Console()


def run_game(visualize=True, debug=False, analysis=True, delay=0.5):
    """Run a Battleship game with rich visualization.

    Creates and runs a complete Battleship game with the specified configuration
    options. Displays game progress, board states, and strategic analysis in
    the terminal using rich text formatting.

    Args:
        visualize: Whether to visualize the game boards
        debug: Whether to enable debug mode with verbose logging
        analysis: Whether to enable strategic analysis by LLM agents
        delay: Delay between steps in seconds (controls game speed)

    Returns:
        None

    Raises:
        KeyboardInterrupt: If the game is interrupted by the user
        Exception: For any unexpected errors during gameplay

    Examples:
        >>> run_game(visualize=True, debug=False, analysis=True, delay=0.5)
        # Displays an interactive game in the terminal

        >>> run_game(visualize=False, debug=True, analysis=False)
        # Runs a game with debug logging but no visualization or analysis

    """
    console.print(
        Panel.fit(
            "🚢 [bold blue]Battleship Game[/bold blue] 🚢",
            border_style="bold blue",
        ),
    )

    # Create configuration
    config = BattleshipAgentConfig(
        enable_analysis=analysis,
        visualize_board=visualize,
        debug=debug,
    )

    # Create and initialize agent
    with Progress(transient=True) as progress:
        task = progress.add_task("[cyan]Initializing game...", total=100)
        progress.update(task, advance=30)

        agent = BattleshipAgent(config)
        progress.update(task, advance=70)

    console.print("[green]Game initialized![/green]")

    # Run the game
    try:
        step_counter = 0
        game_over = False
        final_state = None

        console.print("[cyan]Starting game...[/cyan]")

        for step in agent.app.stream(
            {},
            stream_mode="values",
            debug=debug,
            config=agent.runnable_config,
        ):
            step_counter += 1
            current_player = step.get("current_player")
            phase = step.get("game_phase")
            winner = step.get("winner")
            error = step.get("error_message")

            # Display game information
            console.rule(f"[bold blue]Step {step_counter}")
            console.print(f"Turn: [bold]{current_player}[/bold]")
            console.print(f"Phase: [bold]{phase}[/bold]")

            # Show error if any
            if error:
                console.print(
                    Panel(f"[bold red]ERROR:[/bold red] {error}", border_style="red"),
                )

            # Show boards if in playing phase and visualization is enabled
            if visualize and phase == GamePhase.PLAYING:
                # Get player states
                player1_state = step.get("player1_state", {})
                player2_state = step.get("player2_state", {})

                # Create tables for boards
                table = Table(title="Game Boards")
                table.add_column("Player 1 Board")
                table.add_column("Player 2 Board")

                # Visualize boards
                p1_board = visualize_board(
                    player1_state.get("board", {}),
                    is_opponent=False,
                )
                p2_board = visualize_board(
                    player2_state.get("board", {}),
                    is_opponent=True,
                )

                table.add_row(p1_board, p2_board)
                console.print(table)

                # Show latest analysis if available
                if analysis:
                    p1_analysis = player1_state.get("strategic_analysis", [])
                    p2_analysis = player2_state.get("strategic_analysis", [])

                    if p1_analysis and current_player == "player1":
                        console.print(
                            Panel(
                                p1_analysis[-1],
                                title="Player 1 Analysis",
                                border_style="cyan",
                            ),
                        )
                    elif p2_analysis and current_player == "player2":
                        console.print(
                            Panel(
                                p2_analysis[-1],
                                title="Player 2 Analysis",
                                border_style="cyan",
                            ),
                        )

            # Check if game is over
            if phase == GamePhase.ENDED:
                game_over = True
                final_state = step
                console.print(f"[bold green]Game Over! Winner: {winner}[/bold green]")
                break

            # Add delay between steps
            time.sleep(delay)

        # Final game summary
        if game_over and final_state:
            console.rule("[bold green]Game Summary")

            # Show winner
            winner = final_state.get("winner")
            console.print(f"Winner: [bold green]{winner}[/bold green]")

            # Show move count
            move_history = final_state.get("move_history", [])
            console.print(f"Total Moves: {len(move_history)}")

            # Show hit statistics
            p1_hits = len(
                final_state.get("player1_state", {})
                .get("board", {})
                .get("successful_hits", []),
            )
            p2_hits = len(
                final_state.get("player2_state", {})
                .get("board", {})
                .get("successful_hits", []),
            )
            console.print(f"Player 1 Hits: {p1_hits}")
            console.print(f"Player 2 Hits: {p2_hits}")

            # Show final boards
            if visualize:
                # Get player states
                player1_state = final_state.get("player1_state", {})
                player2_state = final_state.get("player2_state", {})

                # Create tables for boards
                table = Table(title="Final Game Boards")
                table.add_column("Player 1 Board")
                table.add_column("Player 2 Board")
                # Visualize final boards
                p1_board = visualize_board(
                    player1_state.get("board", {}),
                    is_opponent=False,
                )
                p2_board = visualize_board(
                    player2_state.get("board", {}),
                    is_opponent=False,
                )
                table.add_row(p1_board, p2_board)
                console.print(table)

    except KeyboardInterrupt:
        console.print("[bold red]Game interrupted by user.[/bold red]")
    except Exception as e:
        console.print(
            Panel(f"[bold red]Unexpected error:[/bold red] {e}", border_style="red"),
        )


def main():
    """Parse command-line arguments and run the Battleship game.

    This function handles command-line argument parsing and launches
    the Battleship game with the specified configuration options.

    Command-line arguments:
        --no-visual: Disable board visualization
        --no-analysis: Disable strategic analysis
        --debug: Enable debug mode with detailed logs
        --delay: Set delay between game steps (default: 0.5s)

    Returns:
        None

    """
    parser = argparse.ArgumentParser(description="Run a Battleship LLM agent match.")
    parser.add_argument(
        "--no-visual",
        action="store_true",
        help="Disable board visualization.",
    )
    parser.add_argument(
        "--no-analysis",
        action="store_true",
        help="Disable strategic analysis.",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between steps (default: 0.5s)",
    )

    args = parser.parse_args()

    run_game(
        visualize=not args.no_visual,
        debug=args.debug,
        analysis=not args.no_analysis,
        delay=args.delay,
    )


if __name__ == "__main__":
    main()
