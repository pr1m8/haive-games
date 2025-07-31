#!/usr/bin/env python3
"""Fixed runner for Fox and Geese game without LangGraph streaming issues."""

import argparse
import logging
import time
import traceback
import uuid

from rich.console import Console
from rich.live import Live
from rich.panel import Panel

from haive.games.fox_and_geese.agent import FoxAndGeeseAgent
from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.state import FoxAndGeeseState
from haive.games.fox_and_geese.ui import FoxAndGeeseUI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FixedFoxAndGeeseAgent(FoxAndGeeseAgent):
    """Fixed Fox and Geese agent that handles state directly."""

    def run_fixed_game(
        self, delay: float = 1.0, max_moves: int = 100
    ) -> FoxAndGeeseState:
        """Run the Fox and Geese game step by step, managing state directly.

        This bypasses LangGraph's stream method, which can have issues with certain state types.

        Args:
            delay: Time delay between moves for better visualization
            max_moves: Maximum number of moves before forcing a draw

        Returns:
            Final game state
        """
        console = Console()
        console.print(
            Panel("Starting Fox and Geese Game with Fixed Runner", border_style="green")
        )

        # Initialize UI
        ui = FoxAndGeeseUI(console)
        ui.display_welcome()
        time.sleep(1)

        # Initialize game state
        state = self.state_manager.initialize()

        # Create a live display for the board
        with Live(ui.create_layout(state), refresh_per_second=4) as live:
            move_count = 0

            while state.game_status == "ongoing" and move_count < max_moves:
                # Update the display
                live.update(ui.create_layout(state))
                time.sleep(delay)

                # Make the next move based on the current turn
                if state.turn == "fox":
                    console.print("[bold red]🦊 Fox's turn...[/bold red]")
                    # First run analysis if enabled
                    if self.config.enable_analysis:
                        analysis_command = self.analyze_player1(state)
                        if (
                            hasattr(analysis_command, "update")
                            and analysis_command.update
                        ):
                            # Extract fox_analysis from the command and update
                            # state
                            if "fox_analysis" in analysis_command.update:
                                state = state.model_copy(deep=True)
                                state.fox_analysis = analysis_command.update[
                                    "fox_analysis"
                                ]

                    # Now make the move
                    new_state = self.make_fox_move(state)
                    state = new_state

                else:  # geese's turn
                    console.print("[bold blue]🪿 Geese's turn...[/bold blue]")
                    # First run analysis if enabled
                    if self.config.enable_analysis:
                        analysis_command = self.analyze_player2(state)
                        if (
                            hasattr(analysis_command, "update")
                            and analysis_command.update
                        ):
                            # Extract geese_analysis from the command and
                            # update state
                            if "geese_analysis" in analysis_command.update:
                                state = state.model_copy(deep=True)
                                state.geese_analysis = analysis_command.update[
                                    "geese_analysis"
                                ]

                    # Now make the move
                    new_state = self.make_geese_move(state)
                    state = new_state

                move_count += 1

                # Update the display after the move
                live.update(ui.create_layout(state))
                time.sleep(delay)

                # Check if the game is over
                if state.game_status != "ongoing":
                    break

            # If we reached max moves, set as a draw
            if state.game_status == "ongoing" and move_count >= max_moves:
                state = state.model_copy(deep=True)
                state.game_status = "draw"
                state.winner = "none"
                live.update(ui.create_layout(state))
                time.sleep(delay)

        # Display final results
        ui.display_final_results(state)

        return state


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Run Fox and Geese game with fixed state handling"
    )
    parser.add_argument(
        "--delay", type=float, default=1.0, help="Delay between moves (seconds)"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    parser.add_argument(
        "--no-analysis", action="store_true", help="Disable position analysis"
    )
    parser.add_argument(
        "--max-moves", type=int, default=100, help="Maximum number of moves"
    )
    return parser.parse_args()


def main():
    """Run the Fox and Geese game with the fixed runner."""
    args = parse_arguments()

    # Configure logging
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    console = Console()

    try:
        # Create config with unique ID
        config = FoxAndGeeseConfig(
            name="fox_and_geese_fixed",
            enable_analysis=not args.no_analysis,
            visualize=True,
            runnable_config={
                "configurable": {
                    "thread_id": uuid.uuid4().hex[:8],
                    "recursion_limit": 400,
                }
            },
        )

        # Create agent with the fixed implementation
        agent = FixedFoxAndGeeseAgent(config)

        console.print(
            Panel(
                "Running Fox and Geese with fixed state handling\n"
                f"Delay between moves: {args.delay} seconds\n"
                f"Analysis enabled: {not args.no_analysis}\n"
                f"Maximum moves: {args.max_moves}",
                title="🎮 Fox and Geese Fixed Game",
                border_style="cyan",
            )
        )

        # Run the game with the fixed step-by-step approach
        agent.run_fixed_game(delay=args.delay, max_moves=args.max_moves)

    except Exception as e:
        console.print(f"[bold red]Error running game: {e}[/bold red]")

        console.print(
            Panel(traceback.format_exc(), title="Error Details", border_style="red")
        )


if __name__ == "__main__":
    main()
