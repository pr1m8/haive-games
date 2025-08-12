"""Example script for running the Flow Free game agent.

This script demonstrates how to configure and run the Flow Free game agent in different
modes and difficulty levels.

"""

import argparse
import sys
import traceback
from pathlib import Path

from rich.console import Console

from haive.games.single_player.base import GameDifficulty, GameMode, PlayerType
from haive.games.single_player.flow_free.agent import FlowFreeAgent
from haive.games.single_player.flow_free.config import FlowFreeConfig
from haive.games.single_player.flow_free.state_manager import FlowFreeStateManager

# Add the package to the path if running directly
if __name__ == "__main__":
    package_root = Path(__file__).parent.parent.parent.parent.parent
    sys.path.insert(0, str(package_root))


def main():
    """Run the Flow Free game."""
    console = Console()

    # Show startup banner
    console.print("[bold cyan]🧩 Flow Free Puzzle Game[/bold cyan]")
    console.print("[dim]Connect the dots without crossing paths[/dim]")
    console.print()

    try:
        # Parse command-line arguments
        args = parse_arguments()

        # Create configuration based on arguments
        config = create_config(args)

        console.print(
            f"[yellow]⚙️ Creating a {
                config.difficulty.value
            } Flow Free puzzle...[/yellow]"
        )
        console.print(f"[yellow]🎮 Game mode: {config.game_mode.value}[/yellow]")
        console.print(f"[yellow]🧮 Grid size: {config.rows}x{config.cols}[/yellow]")

        # Create and run the agent
        agent = FlowFreeAgent(config)
        agent.state_manager = FlowFreeStateManager

        console.print("[green]✅ Setup complete! Starting game...[/green]")
        console.print()

        agent.run_game()

        console.print()
        console.print("[green]🎮 Game completed![/green]")

    except KeyboardInterrupt:
        console.print("\n[yellow]👋 Game interrupted by user. Goodbye![/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Game failed: {e}[/red]")

        console.print(traceback.format_exc())


def parse_arguments():
    """Parse command-line arguments.

    Returns:
        Namespace with parsed arguments.

    """
    parser = argparse.ArgumentParser(description="Flow Free Puzzle Game")

    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard", "expert"],
        default="medium",
        help="Difficulty level of the puzzle",
    )

    parser.add_argument(
        "--mode",
        choices=["auto", "interactive", "assist"],
        default="auto",
        help="Game mode (auto=LLM plays, interactive=human plays, assist=LLM assists human)",
    )

    parser.add_argument(
        "--size",
        choices=["5x5", "6x6", "7x7"],
        default="5x5",
        help="Grid size (rows x columns)",
    )

    parser.add_argument(
        "--flows",
        type=int,
        default=None,
        help="Number of flows to include (default: determined by difficulty)",
    )

    parser.add_argument(
        "--no-visualize", action="store_true", help="Disable visualization"
    )

    return parser.parse_args()


def create_config(args):
    """Create a game configuration based on arguments.

    Args:
        args: Parsed command-line arguments.

    Returns:
        FlowFreeConfig: Game configuration.

    """
    # Parse difficulty
    difficulty_map = {
        "easy": GameDifficulty.EASY,
        "medium": GameDifficulty.MEDIUM,
        "hard": GameDifficulty.HARD,
        "expert": GameDifficulty.EXPERT,
    }
    difficulty = difficulty_map.get(args.difficulty, GameDifficulty.MEDIUM)

    # Parse game mode
    mode_map = {
        "auto": GameMode.AUTO,
        "interactive": GameMode.INTERACTIVE,
        "assist": GameMode.ASSIST,
    }
    game_mode = mode_map.get(args.mode, GameMode.AUTO)

    # Parse player type based on mode
    player_type = PlayerType.LLM if game_mode == GameMode.AUTO else PlayerType.HUMAN
    if game_mode == GameMode.ASSIST:
        player_type = PlayerType.HYBRID

    # Parse grid size
    size_map = {"5x5": (5, 5), "6x6": (6, 6), "7x7": (7, 7)}
    rows, cols = size_map.get(args.size, (5, 5))

    # Create configuration
    return FlowFreeConfig(
        name=f"flow_free_{args.difficulty}_{args.size}",
        player_type=player_type,
        game_mode=game_mode,
        difficulty=difficulty,
        rows=rows,
        cols=cols,
        num_flows=args.flows,
        visualize=not args.no_visualize,
    )


if __name__ == "__main__":
    main()
