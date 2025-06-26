"""Enhanced Rich UI module for Fox and Geese game visualization.

This module provides an enhanced rich console UI for visualizing the Fox and Geese game,
with better styling, animated piece movements, and improved game information display.
"""

import logging
import time
from typing import Any, List, Optional, Set

from rich.align import Align
from rich.box import DOUBLE, ROUNDED
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.fox_and_geese.state import FoxAndGeeseState

logger = logging.getLogger(__name__)


class FoxAndGeeseRichUI:
    """Enhanced Rich UI for Fox and Geese game visualization.

    This class provides a visually appealing terminal UI for Fox and Geese games,
    with styled components, animations, and comprehensive game information.

    Features:
        - Beautiful game board visualization with colored squares
        - Animated piece movements for fox and geese
        - Detailed game statistics and turn information
        - Move history tracking with visual indicators
        - Analysis visualization for both fox and geese strategies
        - Thinking animations and move highlights

    Attributes:
        console (Console): Rich console for output
        colors (dict): Color schemes for different UI elements
    """

    def __init__(self, console: Optional[Console] = None):
        """Initialize the UI.

        Args:
            console: Optional Rich console instance
        """
        self.console = console or Console()

        # Define colors and styles
        self.colors = {
            "fox": "bright_red",
            "geese": "bright_blue",
            "board_light": "bright_white",
            "board_dark": "dim",
            "highlight": "bright_yellow",
            "capture": "bright_red",
            "header": "bright_magenta",
            "info": "bright_green",
            "move": "bright_cyan",
            "panel_border": "cyan",
            "success": "green",
            "warning": "yellow",
            "error": "red",
        }

        # Board representation constants
        self.board_symbols = {
            "fox": "🦊",
            "goose": "🪿",
            "empty_light": "⬜",
            "empty_dark": "⬛",
            "highlight": "🟨",
            "capture": "🟥",
        }

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
                return state_data

            # Handle langgraph Command objects
            if hasattr(state_data, "update"):
                command_update = state_data.update

                # Handle Command objects where update is already a FoxAndGeeseState
                if isinstance(command_update, FoxAndGeeseState):
                    return command_update

                # Handle Command objects where update is a dict
                elif isinstance(command_update, dict):
                    if self._is_valid_game_state_dict(command_update):
                        try:
                            return FoxAndGeeseState.model_validate(command_update)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create FoxAndGeeseState from Command.update: {e}"
                            )

            # For direct dict output from langgraph stream
            if isinstance(state_data, dict) and self._is_valid_game_state_dict(
                state_data
            ):
                try:
                    return FoxAndGeeseState.model_validate(state_data)
                except Exception as e:
                    logger.warning(
                        f"Failed to create FoxAndGeeseState from direct dict: {e}"
                    )

            # If it's a dict, try to extract from nested structure
            if isinstance(state_data, dict):
                # First check for 'values' key which is used in langgraph stream output
                if "values" in state_data and isinstance(state_data["values"], dict):
                    values_dict = state_data["values"]
                    if self._is_valid_game_state_dict(values_dict):
                        try:
                            return FoxAndGeeseState.model_validate(values_dict)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create FoxAndGeeseState from 'values': {e}"
                            )

                # First, try to find a FoxAndGeeseState object in the dict values
                for key, value in state_data.items():
                    if isinstance(value, FoxAndGeeseState):
                        return value

                # Next, try to find a dict that can be converted to FoxAndGeeseState
                for key, value in state_data.items():
                    if isinstance(value, dict) and self._is_valid_game_state_dict(
                        value
                    ):
                        try:
                            return FoxAndGeeseState.model_validate(value)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create FoxAndGeeseState from {key}: {e}"
                            )
                            continue

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

    def create_board_table(
        self,
        game_state: FoxAndGeeseState,
        highlight_positions: Optional[Set[FoxAndGeesePosition]] = None,
        capture_position: Optional[FoxAndGeesePosition] = None,
    ) -> Table:
        """Create an enhanced visual representation of the board.

        Args:
            game_state: Current game state
            highlight_positions: Optional positions to highlight (for showing moves)
            capture_position: Optional position to highlight as a capture

        Returns:
            Rich table representing the board
        """
        # Create board table with nicer styling
        board_table = Table(
            show_header=False,
            show_edge=False,
            padding=(0, 1),
            box=None,
            collapse_padding=True,
        )

        # Add columns for the board
        for _ in range(8):  # 7 columns + 1 for row numbers
            board_table.add_column(justify="center", width=3)

        # Prepare highlight and capture positions as sets for efficient lookups
        highlight_positions = highlight_positions or set()

        # Create the board representation
        board = [
            [self._get_square_symbol(row, col) for col in range(7)] for row in range(7)
        ]

        # Place the fox
        if game_state.fox_position:
            row, col = game_state.fox_position.row, game_state.fox_position.col
            board[row][
                col
            ] = f"[{self.colors['fox']}]{self.board_symbols['fox']}[/{self.colors['fox']}]"

        # Place the geese
        for goose in game_state.geese_positions:
            row, col = goose.row, goose.col
            board[row][
                col
            ] = f"[{self.colors['geese']}]{self.board_symbols['goose']}[/{self.colors['geese']}]"

        # Apply highlights for possible moves
        for pos in highlight_positions:
            if 0 <= pos.row < 7 and 0 <= pos.col < 7:  # Ensure position is valid
                board[pos.row][
                    pos.col
                ] = f"[{self.colors['highlight']}]{self.board_symbols['highlight']}[/{self.colors['highlight']}]"

        # Apply highlight for capture
        if (
            capture_position
            and 0 <= capture_position.row < 7
            and 0 <= capture_position.col < 7
        ):
            board[capture_position.row][
                capture_position.col
            ] = f"[{self.colors['capture']}]{self.board_symbols['capture']}[/{self.colors['capture']}]"

        # Add header row with column numbers
        header_row = [""] + [f"[bold blue]{i}[/bold blue]" for i in range(7)]
        board_table.add_row(*header_row)

        # Add board rows with row numbers and styled squares
        for i, row in enumerate(board):
            display_row = [f"[bold blue]{i}[/bold blue]"] + row
            board_table.add_row(*display_row)

        return board_table

    def _get_square_symbol(self, row: int, col: int) -> str:
        """Get the symbol for a board square based on its position.

        In Fox and Geese, pieces can move on any square but we use a checkered pattern
        to make the board more visually appealing.

        Args:
            row: Row index
            col: Column index

        Returns:
            Symbol for the square
        """
        # Create a checkered pattern for better visibility
        if (row + col) % 2 == 0:
            return f"[{self.colors['board_dark']}]{self.board_symbols['empty_dark']}[/{self.colors['board_dark']}]"
        else:
            return f"[{self.colors['board_light']}]{self.board_symbols['empty_light']}[/{self.colors['board_light']}]"

    def create_game_info_panel(self, game_state: FoxAndGeeseState) -> Panel:
        """Create an enhanced panel with game information.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with detailed game info
        """
        # Create a table for the game info
        info_table = Table(show_header=False, box=None, show_edge=False, padding=(0, 1))
        info_table.add_column("Key", style="bright_blue", width=16)
        info_table.add_column("Value", style="white")

        # Current player
        if game_state.turn == "fox":
            current_turn = f"[{self.colors['fox']}]🦊 Fox's Turn[/{self.colors['fox']}]"
        else:
            current_turn = (
                f"[{self.colors['geese']}]🪿 Geese's Turn[/{self.colors['geese']}]"
            )
        info_table.add_row("Current Turn", current_turn)

        # Game status
        if game_state.game_status == "ongoing":
            status = (
                f"[{self.colors['success']}]Game in Progress[/{self.colors['success']}]"
            )
        elif game_state.game_status == "fox_win":
            status = f"[{self.colors['fox']}]🦊 Fox Wins![/{self.colors['fox']}]"
        elif game_state.game_status == "geese_win":
            status = f"[{self.colors['geese']}]🪿 Geese Win![/{self.colors['geese']}]"
        else:
            status = f"[{self.colors['warning']}]{game_state.game_status}[/{self.colors['warning']}]"
        info_table.add_row("Game Status", status)

        # Fox position
        fox_pos = f"({game_state.fox_position.row}, {game_state.fox_position.col})"
        info_table.add_row(
            "Fox Position", f"[{self.colors['fox']}]{fox_pos}[/{self.colors['fox']}]"
        )

        # Geese remaining
        info_table.add_row(
            "Geese Remaining", f"[bold]{game_state.num_geese}[/bold] / 8"
        )

        # Geese percentage
        geese_percent = (game_state.num_geese / 8) * 100
        geese_bar = "█" * int(geese_percent / 10) + "░" * (10 - int(geese_percent / 10))
        info_table.add_row(
            "Geese Health",
            f"[{self.colors['geese']}]{geese_bar} {geese_percent:.1f}%[/{self.colors['geese']}]",
        )

        # Move count
        info_table.add_row("Move Count", f"[bold]{len(game_state.move_history)}[/bold]")

        # Victory conditions
        info_table.add_row("", "")
        info_table.add_row("Victory Conditions", "")
        info_table.add_row("Fox Wins", f"When fewer than [bold]{4}[/bold] geese remain")
        info_table.add_row("Geese Win", "When fox has no legal moves")

        # Create the panel
        return Panel(
            info_table,
            title="[bold]Game Information[/bold]",
            border_style=self.colors["panel_border"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_move_history_panel(self, game_state: FoxAndGeeseState) -> Panel:
        """Create an enhanced panel showing move history.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with detailed move history
        """
        if not game_state.move_history:
            history_text = Text(
                "No moves have been made yet", style="dim", justify="center"
            )
            return Panel(
                history_text,
                title="[bold]Move History[/bold]",
                border_style=self.colors["move"],
                box=ROUNDED,
                padding=(1, 1),
            )

        # Create a table for the moves
        history_table = Table(
            show_header=True,
            box=None,
            padding=(0, 1),
            title="Recent Moves",
            title_style="bold",
        )

        history_table.add_column("#", style="dim", width=3)
        history_table.add_column("Piece", style="white", width=6)
        history_table.add_column("From", style="white", width=6)
        history_table.add_column("To", style="white", width=6)
        history_table.add_column("Capture", style="white", width=8)

        # Show the last 8 moves at most
        start_idx = max(0, len(game_state.move_history) - 8)

        for i, move in enumerate(
            game_state.move_history[start_idx:], start=start_idx + 1
        ):
            # Format piece with appropriate color
            if move.piece_type == "fox":
                piece_text = f"[{self.colors['fox']}]🦊 Fox[/{self.colors['fox']}]"
            else:
                piece_text = (
                    f"[{self.colors['geese']}]🪿 Goose[/{self.colors['geese']}]"
                )

            # Format positions
            from_text = f"({move.from_pos.row},{move.from_pos.col})"
            to_text = f"({move.to_pos.row},{move.to_pos.col})"

            # Format capture information
            if move.capture:
                capture_text = (
                    f"[{self.colors['capture']}]Yes![/{self.colors['capture']}]"
                )
            else:
                capture_text = "No"

            history_table.add_row(str(i), piece_text, from_text, to_text, capture_text)

        return Panel(
            history_table,
            title="[bold]Move History[/bold]",
            border_style=self.colors["move"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_analysis_panel(self, game_state: FoxAndGeeseState) -> Panel:
        """Create an enhanced panel showing the latest analysis.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with detailed analysis
        """
        # Create a table for the analysis
        analysis_table = Table(
            show_header=False,
            box=None,
            show_edge=False,
            padding=(0, 1),
        )

        analysis_table.add_column("Key", style="bright_magenta", width=8)
        analysis_table.add_column("Value", style="white")

        has_analysis = False

        # Fox analysis
        if hasattr(game_state, "fox_analysis") and game_state.fox_analysis:
            has_analysis = True
            fox_analysis = game_state.fox_analysis[-1]

            # Truncate if needed
            if len(fox_analysis) > 200:
                fox_text = fox_analysis[:200] + "..."
            else:
                fox_text = fox_analysis

            analysis_table.add_row(
                f"[{self.colors['fox']}]🦊 Fox[/{self.colors['fox']}]", fox_text
            )

        # Geese analysis
        if hasattr(game_state, "geese_analysis") and game_state.geese_analysis:
            has_analysis = True
            geese_analysis = game_state.geese_analysis[-1]

            # Truncate if needed
            if len(geese_analysis) > 200:
                geese_text = geese_analysis[:200] + "..."
            else:
                geese_text = geese_analysis

            analysis_table.add_row(
                f"[{self.colors['geese']}]🪿 Geese[/{self.colors['geese']}]", geese_text
            )

        if not has_analysis:
            no_analysis_text = Text(
                "No analysis available yet", style="dim", justify="center"
            )
            return Panel(
                no_analysis_text,
                title="[bold]Game Analysis[/bold]",
                border_style="magenta",
                box=ROUNDED,
                padding=(1, 1),
            )

        return Panel(
            analysis_table,
            title="[bold]Game Analysis[/bold]",
            border_style="magenta",
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_legal_moves_panel(
        self,
        game_state: FoxAndGeeseState,
        legal_moves: Optional[List[FoxAndGeeseMove]] = None,
    ) -> Panel:
        """Create a panel showing legal moves for the current player.

        Args:
            game_state: Current game state
            legal_moves: Optional list of legal moves

        Returns:
            Rich panel with legal moves info
        """
        # If no legal moves are provided, use an empty list
        if legal_moves is None:
            legal_moves = []

        # If the list is empty, show a message
        if len(legal_moves) == 0:
            moves_text = Text(
                f"No legal moves for {game_state.turn}", style="dim", justify="center"
            )

            # Set title based on whose turn it is
            if game_state.turn == "fox":
                title = f"[bold {self.colors['fox']}]Legal Moves for Fox[/bold {self.colors['fox']}]"
            else:
                title = f"[bold {self.colors['geese']}]Legal Moves for Geese[/bold {self.colors['geese']}]"

            return Panel(
                moves_text,
                title=title,
                border_style=self.colors["info"],
                box=ROUNDED,
                padding=(1, 1),
            )

        # Create a table for moves
        moves_table = Table(
            show_header=True,
            box=None,
            padding=(0, 1),
        )

        moves_table.add_column("#", style="dim", width=3)
        moves_table.add_column("From", style="white", width=6)
        moves_table.add_column("To", style="white", width=6)
        moves_table.add_column("Capture", style="white", width=8)

        # Show at most 6 moves
        display_moves = legal_moves[:6]

        for i, move in enumerate(display_moves, start=1):
            # Format positions
            from_text = f"({move.from_pos.row},{move.from_pos.col})"
            to_text = f"({move.to_pos.row},{move.to_pos.col})"

            # Format capture
            if move.capture:
                capture_text = (
                    f"[{self.colors['capture']}]Yes![/{self.colors['capture']}]"
                )
            else:
                capture_text = "No"

            moves_table.add_row(str(i), from_text, to_text, capture_text)

        # Add count of additional moves if needed
        if len(legal_moves) > 6:
            remaining = len(legal_moves) - 6
            moves_table.add_row("...", f"[dim]+{remaining} more moves[/dim]", "", "")

        # Set the title based on whose turn it is
        if game_state.turn == "fox":
            title = f"[bold {self.colors['fox']}]Legal Moves for Fox[/bold {self.colors['fox']}]"
        else:
            title = f"[bold {self.colors['geese']}]Legal Moves for Geese[/bold {self.colors['geese']}]"

        return Panel(
            moves_table,
            title=title,
            border_style=self.colors["info"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_layout(
        self,
        game_state: FoxAndGeeseState,
        highlight_positions: Optional[Set[FoxAndGeesePosition]] = None,
        capture_position: Optional[FoxAndGeesePosition] = None,
        legal_moves: Optional[List[FoxAndGeeseMove]] = None,
    ) -> Layout:
        """Create the enhanced complete rich UI layout.

        Args:
            game_state: Current game state
            highlight_positions: Optional positions to highlight
            capture_position: Optional position being captured
            legal_moves: Optional list of legal moves

        Returns:
            Complete rich layout
        """
        # Create layout
        layout = Layout()

        # Split into header and body
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
        )

        # Header with game title
        header_text = Text(
            "🦊 FOX AND GEESE GAME 🪿", style=self.colors["header"], justify="center"
        )
        layout["header"].update(
            Panel(header_text, border_style=self.colors["panel_border"], box=ROUNDED)
        )

        # Split main into board and sidebar
        layout["main"].split_row(
            Layout(name="left_column", ratio=6),
            Layout(name="right_column", ratio=4),
        )

        # Left column - split into board and history
        layout["main"]["left_column"].split(
            Layout(name="board", ratio=3),
            Layout(name="move_history", ratio=1),
        )

        # Add the board
        board_table = self.create_board_table(
            game_state,
            highlight_positions=highlight_positions,
            capture_position=capture_position,
        )
        layout["main"]["left_column"]["board"].update(
            Panel(
                Align.center(board_table),
                title="[bold]Game Board[/bold]",
                border_style=self.colors["board_light"],
                box=ROUNDED,
                padding=(1, 1),
            )
        )

        # Add move history
        layout["main"]["left_column"]["move_history"].update(
            self.create_move_history_panel(game_state)
        )

        # Right column - split into game info, legal moves, and analysis
        layout["main"]["right_column"].split(
            Layout(name="game_info", ratio=3),
            Layout(name="legal_moves", ratio=2),
            Layout(name="analysis", ratio=3),
        )

        # Add game info, legal moves, and analysis
        layout["main"]["right_column"]["game_info"].update(
            self.create_game_info_panel(game_state)
        )
        layout["main"]["right_column"]["legal_moves"].update(
            self.create_legal_moves_panel(game_state, legal_moves)
        )
        layout["main"]["right_column"]["analysis"].update(
            self.create_analysis_panel(game_state)
        )

        return layout

    def display_state(
        self,
        state_data: Any,
        highlight_positions: Optional[Set[FoxAndGeesePosition]] = None,
        capture_position: Optional[FoxAndGeesePosition] = None,
        legal_moves: Optional[List[FoxAndGeeseMove]] = None,
    ) -> bool:
        """Display the game state using enhanced rich UI.

        Args:
            state_data: State data in various formats
            highlight_positions: Optional positions to highlight
            capture_position: Optional position being captured
            legal_moves: Optional list of legal moves

        Returns:
            True if display was successful, False otherwise
        """
        try:
            game_state = self.extract_game_state(state_data)
            if game_state is None:
                logger.error("Could not extract valid game state for display")
                return False

            layout = self.create_layout(
                game_state,
                highlight_positions=highlight_positions,
                capture_position=capture_position,
                legal_moves=legal_moves,
            )
            self.console.print(layout)
            return True

        except Exception as e:
            logger.error(f"Error displaying state: {e}", exc_info=True)
            return False

    def show_thinking(self, player: str, message: str = "Thinking...") -> None:
        """Display a thinking animation for the current player.

        Shows a spinner animation with player-colored text to indicate
        that the player is thinking about their move.

        Args:
            player (str): Current player ("fox" or "geese")
            message (str, optional): Custom message to display. Defaults to "Thinking...".

        Returns:
            None
        """
        player_color = self.colors[player]
        player_display = "🦊 Fox" if player == "fox" else "🪿 Geese"

        with Progress(
            SpinnerColumn(),
            TextColumn(f"[{player_color}]{player_display}[/] {message}"),
            console=self.console,
            transient=True,
        ) as progress:
            progress.add_task("thinking", total=None)
            time.sleep(1.0)  # Show thinking animation for 1 second

    def show_move(
        self,
        move: FoxAndGeeseMove,
        state_before: FoxAndGeeseState,
        state_after: FoxAndGeeseState,
    ) -> None:
        """Display an animated move being made.

        Shows the move with highlighting of the relevant positions.

        Args:
            move: The move being made
            state_before: State before the move
            state_after: State after the move

        Returns:
            None
        """
        # Highlight the source and destination squares
        highlight_positions = {move.from_pos, move.to_pos}

        # Determine if this is a capture move
        capture_position = move.capture

        # Show the board with the move highlighted
        move_panel = Panel(
            f"[{self.colors[move.piece_type]}]{self.board_symbols['fox'] if move.piece_type == 'fox' else self.board_symbols['goose']} "
            f"{move.piece_type.capitalize()}[/{self.colors[move.piece_type]}] moves from "
            f"({move.from_pos.row},{move.from_pos.col}) to ({move.to_pos.row},{move.to_pos.col})"
            + (
                f"\n[{self.colors['capture']}]Capturing goose at ({capture_position.row},{capture_position.col})![/{self.colors['capture']}]"
                if capture_position
                else ""
            ),
            title="[bold]Move[/bold]",
            title_align="center",
            border_style=self.colors[move.piece_type],
            padding=(1, 2),
        )

        # Display the move
        self.console.print(move_panel)

        # Show the board with highlighted positions
        self.display_state(state_after, highlight_positions, capture_position)

        # Short pause to let the user see the move
        time.sleep(0.8)

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

The game is played on a cross-shaped board with the fox starting in the center
and the geese at the top. The fox can move in any direction along the lines,
while geese can only move forward or sideways.

The fox can capture geese by jumping over them into an empty space.

The game will be played by AI agents with real-time visualization!
            """.strip(),
            style="bold cyan",
        )

        self.console.print(
            Panel(
                welcome_text,
                title="[bold yellow]🎮 FOX AND GEESE GAME 🎮[/bold yellow]",
                border_style="bright_green",
                box=DOUBLE,
                padding=(1, 2),
            )
        )

    def display_final_results(self, final_state: Any) -> None:
        """Display enhanced final game results.

        Args:
            final_state: Final game state
        """
        try:
            game_state = self.extract_game_state(final_state)
            if game_state is None:
                self.console.print("[red]Could not extract final game state[/red]")
                return

            # Calculate game stats
            move_count = len(game_state.move_history)
            geese_remaining = game_state.num_geese
            capture_count = sum(
                1 for move in game_state.move_history if move.capture is not None
            )

            # Create results table
            results_table = Table(show_header=True, box=ROUNDED)
            results_table.add_column("Statistic", style="white")
            results_table.add_column("Value", style="white")

            results_table.add_row("Total Moves", f"[bold]{move_count}[/bold]")
            results_table.add_row(
                "Geese Remaining", f"[bold]{geese_remaining}[/bold] / 8"
            )
            results_table.add_row("Captures", f"[bold]{capture_count}[/bold]")

            # Create title based on result
            if game_state.game_status == "fox_win":
                title = f"[bold {self.colors['fox']}]🦊 Fox Wins the Game! 🦊[/bold {self.colors['fox']}]"
                border_style = self.colors["fox"]
                winner_text = Text(
                    "The fox has captured enough geese to secure victory!",
                    style=self.colors["fox"],
                    justify="center",
                )
            elif game_state.game_status == "geese_win":
                title = f"[bold {self.colors['geese']}]🪿 Geese Win the Game! 🪿[/bold {self.colors['geese']}]"
                border_style = self.colors["geese"]
                winner_text = Text(
                    "The geese have successfully trapped the fox!",
                    style=self.colors["geese"],
                    justify="center",
                )
            else:
                title = "[bold]Game Complete[/bold]"
                border_style = "green"
                winner_text = Text(
                    "The game has ended.", style="green", justify="center"
                )

            self.console.print()
            self.console.print("=" * 50)
            self.console.print(
                Panel(
                    Group(
                        winner_text,
                        Align.center(results_table),
                    ),
                    title=title,
                    border_style=border_style,
                    box=DOUBLE,
                    padding=(1, 2),
                )
            )

        except Exception as e:
            logger.error(f"Error displaying final results: {e}", exc_info=True)
            self.console.print(f"[red]Error displaying final results: {e}[/red]")

    def animate_move(
        self,
        state_before: FoxAndGeeseState,
        state_after: FoxAndGeeseState,
        delay: float = 0.5,
    ) -> None:
        """Animate a move being made.

        Shows a smooth transition between the before and after states with
        visual indicators of what changed.

        Args:
            state_before: Game state before the move
            state_after: State after the move
            delay: Delay in seconds for the animation

        Returns:
            None
        """
        # Get the last move
        if not state_after.move_history:
            return

        last_move = state_after.move_history[-1]

        # Show the thinking animation
        self.show_thinking(last_move.piece_type)

        # Show the move being made
        self.show_move(last_move, state_before, state_after)

        # Show the final state
        self.display_state(state_after)

    def display_game_with_animation(
        self, state_sequence: List[FoxAndGeeseState], delay: float = 1.0
    ) -> None:
        """Display a sequence of game states with smooth transitions.

        This is useful for replaying a game or showing a sequence of moves with
        visual transitions between states.

        Args:
            state_sequence: List of game states in sequence
            delay: Delay in seconds between states

        Returns:
            None
        """
        if not state_sequence:
            return

        # Display welcome message
        self.display_welcome()
        time.sleep(delay)

        # Display initial state
        self.display_state(state_sequence[0])
        time.sleep(delay)

        # Animate through the sequence
        for i in range(1, len(state_sequence)):
            state_before = state_sequence[i - 1]
            state_after = state_sequence[i]

            # Animate the transition
            self.animate_move(state_before, state_after, delay=delay)
            time.sleep(delay)

        # Show final results
        self.display_final_results(state_sequence[-1])

    def run_fox_and_geese_game(self, agent, delay: float = 1.0) -> FoxAndGeeseState:
        """Run a complete Fox and Geese game with UI visualization.

        This method handles the entire game flow, including initialization,
        move animation, and final results display.

        Args:
            agent: The game agent that manages the game logic
            delay: Delay in seconds between game states

        Returns:
            Final game state
        """
        # Set the UI on the agent if possible
        if hasattr(agent, "ui"):
            agent.ui = self

        # Display welcome
        self.display_welcome()
        time.sleep(delay)

        # Initialize the game
        initial_state = agent.state_manager.initialize()
        self.display_state(initial_state)
        time.sleep(delay)

        # Run the game with state tracking
        final_state = agent.run_game_with_ui(delay=delay)

        # Show final results
        self.display_final_results(final_state)

        return final_state
