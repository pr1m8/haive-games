"""Rich UI module for Fox and Geese game visualization.

This module provides rich console UI components for visualizing the Fox and Geese game.
"""

import logging
from typing import Any, Dict, Optional, Union

from rich.align import Align
from rich.box import ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from haive.games.fox_and_geese.state import FoxAndGeeseState

logger = logging.getLogger(__name__)


class FoxAndGeeseUI:
    """Rich UI for Fox and Geese game visualization."""

    def __init__(self, console: Optional[Console] = None):
        """Initialize the UI.

        Args:
            console: Optional Rich console instance
        """
        self.console = console or Console()

    def extract_game_state(self, state_data: Any) -> Optional[FoxAndGeeseState]:
        """Extract FoxAndGeeseState from various input formats.

        Args:
            state_data: State data in various formats

        Returns:
            FoxAndGeeseState instance or None if extraction fails
        """
        try:
            # Handle None input gracefully
            if state_data is None:
                logger.warning("Received None state_data")
                return None

            # If it's already a FoxAndGeeseState, return it
            if isinstance(state_data, FoxAndGeeseState):
                logger.debug("State is already FoxAndGeeseState")
                return state_data

            # Handle langgraph Command objects
            if hasattr(state_data, "update") and callable(
                getattr(state_data, "update", None)
            ):
                logger.debug("State is a Command object with update field")
                command_update = state_data.update
                if isinstance(command_update, dict):
                    if self._is_valid_game_state_dict(command_update):
                        try:
                            return FoxAndGeeseState.model_validate(command_update)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create FoxAndGeeseState from Command.update: {e}"
                            )

            # If it's a dict, try to extract from nested structure
            if isinstance(state_data, dict):
                logger.debug(f"State is dict with keys: {list(state_data.keys())}")

                # First check for 'values' key which is used in langgraph stream output
                if "values" in state_data and isinstance(state_data["values"], dict):
                    values_dict = state_data["values"]
                    if self._is_valid_game_state_dict(values_dict):
                        logger.debug("Found valid game state in 'values' key")
                        try:
                            return FoxAndGeeseState.model_validate(values_dict)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create FoxAndGeeseState from 'values': {e}"
                            )

                # First, try to find a FoxAndGeeseState object in the dict values
                for key, value in state_data.items():
                    if isinstance(value, FoxAndGeeseState):
                        logger.debug(f"Found FoxAndGeeseState in key: {key}")
                        return value

                # Next, try to find a dict that can be converted to FoxAndGeeseState
                for key, value in state_data.items():
                    if isinstance(value, dict) and self._is_valid_game_state_dict(
                        value
                    ):
                        logger.debug(
                            f"Found state dict in key: {key}, attempting to create FoxAndGeeseState"
                        )
                        try:
                            return FoxAndGeeseState.model_validate(value)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create FoxAndGeeseState from {key}: {e}"
                            )
                            continue

                # Try to create directly from the dict if it has the right structure
                if self._is_valid_game_state_dict(state_data):
                    logger.debug(
                        "Attempting to create FoxAndGeeseState directly from dict"
                    )
                    try:
                        return FoxAndGeeseState.model_validate(state_data)
                    except Exception as e:
                        logger.warning(
                            f"Failed to create FoxAndGeeseState directly: {e}"
                        )

                logger.warning(
                    f"Could not find valid game state in dict with keys: {list(state_data.keys())}"
                )
                return None

            # Handle other types
            logger.warning(f"Unsupported state type: {type(state_data)}")
            return None

        except Exception as e:
            logger.error(f"Error extracting game state: {e}", exc_info=True)
            return None

    def _is_valid_game_state_dict(self, data: dict) -> bool:
        """Check if a dict contains the required fields for FoxAndGeeseState.

        Args:
            data: Dictionary to check

        Returns:
            True if the dict appears to be a valid game state
        """
        required_fields = {"fox_position", "geese_positions", "turn", "game_status"}
        return all(field in data for field in required_fields)

    def create_board_table(self, game_state: FoxAndGeeseState) -> Table:
        """Create a rich visual representation of the board.

        Args:
            game_state: Current game state

        Returns:
            Rich table representing the board
        """
        # Create board table
        board_table = Table(show_header=False, show_edge=False, padding=(0, 1))

        # Add columns for the board
        for _ in range(8):  # 7 columns + 1 for row numbers
            board_table.add_column(justify="center", width=3)

        # Create the board representation
        board = [["⬜" for _ in range(7)] for _ in range(7)]

        # Place the fox
        if game_state.fox_position:
            board[game_state.fox_position.row][game_state.fox_position.col] = "🦊"

        # Place the geese
        for goose in game_state.geese_positions:
            board[goose.row][goose.col] = "🪿"

        # Add header row with column numbers
        header_row = [""] + [str(i) for i in range(7)]
        board_table.add_row(*header_row, style="bold blue")

        # Add board rows
        for i, row in enumerate(board):
            display_row = [str(i)] + row
            board_table.add_row(*display_row)

        return board_table

    def create_game_info_panel(self, game_state: FoxAndGeeseState) -> Panel:
        """Create a panel with game information.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with game info
        """
        # Current player indicator
        if game_state.turn == "fox":
            current_player = "🦊 Fox's Turn"
            player_color = "red"
        else:
            current_player = "🪿 Geese's Turn"
            player_color = "blue"

        # Game status
        if game_state.game_status == "ongoing":
            status_text = "[green]Game in Progress[/green]"
        elif game_state.game_status == "fox_win":
            status_text = "[red]🦊 Fox Wins![/red]"
        elif game_state.game_status == "geese_win":
            status_text = "[blue]🪿 Geese Win![/blue]"
        else:
            status_text = f"[yellow]{game_state.game_status}[/yellow]"

        info_text = f"""[bold {player_color}]{current_player}[/bold {player_color}]

{status_text}

🪿 Geese Remaining: [bold]{game_state.num_geese}[/bold]
📝 Move Count: [bold]{len(game_state.move_history)}[/bold]"""

        return Panel(
            info_text, title="[bold]Game Info[/bold]", border_style="green", box=ROUNDED
        )

    def create_last_move_panel(self, game_state: FoxAndGeeseState) -> Panel:
        """Create a panel showing the last move.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with last move info
        """
        if not game_state.move_history:
            last_move_text = "[dim]No moves yet[/dim]"
        else:
            last_move = game_state.move_history[-1]
            if last_move.piece_type == "fox":
                piece_emoji = "🦊"
                color = "red"
            else:
                piece_emoji = "🪿"
                color = "blue"

            move_text = f"[{color}]{piece_emoji} {last_move.piece_type.title()}[/{color}]: {last_move.from_pos} → {last_move.to_pos}"

            if last_move.capture:
                move_text += f"\n[yellow]Captured goose at {last_move.capture}[/yellow]"

            last_move_text = move_text

        return Panel(
            last_move_text,
            title="[bold]Last Move[/bold]",
            border_style="yellow",
            box=ROUNDED,
        )

    def create_analysis_panel(self, game_state: FoxAndGeeseState) -> Panel:
        """Create a panel showing the latest analysis.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with analysis info
        """
        analysis_text = ""

        if hasattr(game_state, "fox_analysis") and game_state.fox_analysis:
            latest_fox = game_state.fox_analysis[-1]
            if len(latest_fox) > 200:
                latest_fox = latest_fox[:200] + "..."
            analysis_text += f"[red]🦊 Fox Analysis:[/red]\n{latest_fox}\n\n"

        if hasattr(game_state, "geese_analysis") and game_state.geese_analysis:
            latest_geese = game_state.geese_analysis[-1]
            if len(latest_geese) > 200:
                latest_geese = latest_geese[:200] + "..."
            analysis_text += f"[blue]🪿 Geese Analysis:[/blue]\n{latest_geese}"

        if not analysis_text:
            analysis_text = "[dim]No analysis yet[/dim]"

        return Panel(
            analysis_text,
            title="[bold]Latest Analysis[/bold]",
            border_style="magenta",
            box=ROUNDED,
        )

    def create_layout(self, game_state: FoxAndGeeseState) -> Layout:
        """Create the complete rich UI layout.

        Args:
            game_state: Current game state

        Returns:
            Complete rich layout
        """
        # Create layout
        layout = Layout()

        # Split into header and body
        layout.split_column(Layout(name="header", size=3), Layout(name="body"))

        # Header
        title = Text("🦊 Fox and Geese Game 🪿", style="bold magenta", justify="center")
        layout["header"].update(Panel(title, box=ROUNDED))

        # Split body into left and right
        layout["body"].split_row(
            Layout(name="left", ratio=2), Layout(name="right", ratio=1)
        )

        # Left side: board
        board_table = self.create_board_table(game_state)
        layout["left"].update(
            Panel(
                Align.center(board_table),
                title="[bold]Game Board[/bold]",
                border_style="blue",
                box=ROUNDED,
            )
        )

        # Right side: split into info panels
        layout["right"].split_column(
            Layout(name="info"), Layout(name="last_move"), Layout(name="analysis")
        )

        # Info panels
        layout["right"]["info"].update(self.create_game_info_panel(game_state))
        layout["right"]["last_move"].update(self.create_last_move_panel(game_state))
        layout["right"]["analysis"].update(self.create_analysis_panel(game_state))

        return layout

    def display_state(self, state_data: Any) -> bool:
        """Display the game state using rich UI.

        Args:
            state_data: State data in various formats

        Returns:
            True if display was successful, False otherwise
        """
        try:
            game_state = self.extract_game_state(state_data)
            if game_state is None:
                logger.error("Could not extract valid game state for display")
                return False

            layout = self.create_layout(game_state)
            self.console.print(layout)
            return True

        except Exception as e:
            logger.error(f"Error displaying state: {e}", exc_info=True)
            return False

    def display_welcome(self) -> None:
        """Display welcome message."""
        welcome_text = Text(
            """
🦊 Welcome to Fox and Geese! 🪿

This is a classic board game where:
• The Fox (🦊) tries to capture enough geese to win
• The Geese (🪿) try to trap the fox so it cannot move
• The fox wins by reducing geese to fewer than 4
• The geese win by trapping the fox with no legal moves

The game will be played by AI agents with real-time visualization!
        """.strip(),
            style="bold blue",
        )

        self.console.print(
            Panel(
                welcome_text,
                title="[bold magenta]🎮 Fox and Geese Game 🎮[/bold magenta]",
                border_style="green",
            )
        )

    def display_final_results(self, final_state: Any) -> None:
        """Display final game results.

        Args:
            final_state: Final game state
        """
        try:
            game_state = self.extract_game_state(final_state)
            if game_state is None:
                self.console.print("[red]Could not extract final game state[/red]")
                return

            self.console.print("\n" + "=" * 60)
            self.console.print("[bold green]🎮 Game Complete! 🎮[/bold green]")

            status = game_state.game_status
            winner = game_state.winner
            moves = len(game_state.move_history)
            geese_remaining = game_state.num_geese

            if status == "fox_win":
                result_text = f"🦊 [bold red]Fox Wins![/bold red] 🎉\nGeese remaining: {geese_remaining}\nTotal moves: {moves}"
            elif status == "geese_win":
                result_text = f"🪿 [bold blue]Geese Win![/bold blue] 🎉\nFox was trapped!\nTotal moves: {moves}"
            else:
                result_text = f"Game ended with status: {status}\nTotal moves: {moves}"

            self.console.print(
                Panel(
                    result_text,
                    title="[bold]Final Results[/bold]",
                    border_style="yellow",
                )
            )

        except Exception as e:
            logger.error(f"Error displaying final results: {e}", exc_info=True)
            self.console.print(f"[red]Error displaying final results: {e}[/red]")

    def print_debug_info(self, state_data: Any, context: str = "") -> None:
        """Print debug information about the state.

        Args:
            state_data: State data to debug
            context: Context string for debugging
        """
        logger.debug(f"=== DEBUG INFO {context} ===")
        logger.debug(f"State type: {type(state_data)}")

        if state_data is None:
            logger.debug("State data is None")
        elif isinstance(state_data, dict):
            logger.debug(f"Dict keys: {list(state_data.keys())}")
            for key, value in state_data.items():
                logger.debug(f"  {key}: {type(value)}")
                if isinstance(value, dict) and len(value) < 10:
                    logger.debug(f"    Value: {value}")
        elif isinstance(state_data, FoxAndGeeseState):
            logger.debug(
                f"Game state - Turn: {state_data.turn}, Status: {state_data.game_status}"
            )
            logger.debug(f"Fox position: {state_data.fox_position}")
            logger.debug(f"Geese count: {state_data.num_geese}")
        else:
            logger.debug(f"Raw value: {str(state_data)[:200]}")

        logger.debug("=== END DEBUG INFO ===")
