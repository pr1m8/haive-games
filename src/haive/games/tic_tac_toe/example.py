"""Rich UI example for Tic Tac Toe agent.

This example demonstrates how to run a Tic Tac Toe game with a beautiful
Rich-based terminal UI that shows the board, game state, and AI analysis
in real-time.
"""

import sys
from pathlib import Path

# Add the package to the path if running directly
if __name__ == "__main__":
    package_root = Path(__file__).parent.parent.parent.parent
    sys.path.insert(0, str(package_root))

from rich.console import Console

from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.ui import RichTicTacToeRunner


def main():
    """Run a Tic Tac Toe game with Rich UI."""
    console = Console()

    # Show startup banner
    console.print("[bold cyan]🎯 Haive Tic Tac Toe[/bold cyan]")
    console.print("[dim]Powered by LangGraph and Rich UI[/dim]")
    console.print()

    try:
        # Create configuration
        console.print("[yellow]⚙️ Setting up game configuration...[/yellow]")
        config = TicTacToeConfig(
            name="rich_tictactoe",
            enable_analysis=True,  # Enable analysis for more interesting gameplay
            visualize=False,  # Disable the built-in visualization since we're using Rich
            first_player="X",
            player_X="player1",
            player_O="player2",
        )

        # Create agent
        console.print("[yellow]🤖 Initializing AI agent...[/yellow]")
        agent = TicTacToeAgent(config)

        # Create Rich UI runner
        console.print("[yellow]🎨 Setting up Rich UI...[/yellow]")
        ui_runner = RichTicTacToeRunner(agent)

        console.print("[green]✅ Setup complete! Starting game...[/green]")
        console.print()

        # Run the game with Rich UI
        final_state = ui_runner.run_game(
            show_thinking=True,  # Show AI thinking animations
            step_delay=1.5,  # 1.5 second delay between moves
        )

        # Show game summary
        if final_state:
            console.print()
            ui_runner.show_game_summary(final_state)
            console.print()
            console.print("[green]🎉 Game completed successfully![/green]")
        else:
            console.print("[yellow]⚠️ Game ended without final state[/yellow]")

    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Game interrupted by user. Goodbye![/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Game failed: {e}[/red]")
        # Show traceback for debugging
        import traceback

        console.print("[dim]Traceback:[/dim]")
        console.print(traceback.format_exc())


def run_simple_game():
    """Run a simpler version without analysis for faster gameplay."""
    console = Console()

    console.print("[bold cyan]🎯 Haive Tic Tac Toe - Simple Mode[/bold cyan]")
    console.print()

    try:
        # Simpler configuration
        config = TicTacToeConfig(
            name="simple_tictactoe",
            enable_analysis=False,  # Disable analysis for faster games
            visualize=False,
            first_player="X",
            player_X="player1",
            player_O="player2",
        )

        agent = TicTacToeAgent(config)
        ui_runner = RichTicTacToeRunner(agent)

        # Run with faster settings
        final_state = ui_runner.run_game(
            show_thinking=False,  # No thinking animations
            step_delay=0.8,  # Faster moves
        )

        if final_state:
            ui_runner.show_game_summary(final_state)
            console.print("[green]🎉 Simple game completed![/green]")

    except Exception as e:
        console.print(f"[red]❌ Simple game failed: {e}[/red]")


def run_analysis_showcase():
    """Run a game specifically to showcase the AI analysis features."""
    console = Console()

    console.print("[bold magenta]🧠 Tic Tac Toe - AI Analysis Showcase[/bold magenta]")
    console.print("[dim]Watch the AI analyze each position in detail[/dim]")
    console.print()

    try:
        # Configuration optimized for showcasing analysis
        config = TicTacToeConfig(
            name="analysis_showcase",
            enable_analysis=True,
            visualize=False,
            first_player="X",
            player_X="player1",
            player_O="player2",
        )

        agent = TicTacToeAgent(config)
        ui_runner = RichTicTacToeRunner(agent)

        # Run with longer delays to see analysis
        final_state = ui_runner.run_game(
            show_thinking=True, step_delay=3.0  # Longer delay to read analysis
        )

        if final_state:
            ui_runner.show_game_summary(final_state)
            console.print("[magenta]🧠 Analysis showcase completed![/magenta]")

    except Exception as e:
        console.print(f"[red]❌ Analysis showcase failed: {e}[/red]")


if __name__ == "__main__":
    # Check for command line arguments
    import sys

    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
        if mode == "simple":
            run_simple_game()
        elif mode == "analysis":
            run_analysis_showcase()
        else:
            print("Usage: python example.py [simple|analysis]")
            print("  simple   - Run a fast game without analysis")
            print("  analysis - Run a slower game showcasing AI analysis")
            print("  (no args) - Run the default game with analysis")
            main()
    else:
        main()
