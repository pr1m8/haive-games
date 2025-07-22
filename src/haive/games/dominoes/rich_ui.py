"""Enhanced Rich UI module for Dominoes game visualization.

This module provides an enhanced rich console UI for visualizing the Dominoes game,
with better styling, clearer representation of dominoes, and improved game animations.
"""

import logging
import time
from typing import Any

from rich.align import Align
from rich.box import DOUBLE, ROUNDED
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from .dominoes.models import (
    DominoMove,
    DominoTile,
)
from .dominoes.state import DominoesState

logger = logging.getLogger(__name__)


class DominoesRichUI:
    """Enhanced Rich UI for Dominoes game visualization.

    This class provides a visually appealing terminal UI for Dominoes games,
    with styled components, animations, and comprehensive game information.

    Features:
        - Beautiful domino tile visualization with ASCII art
        - Game board with clear indication of playable ends
        - Player hands with pip count and tile organization
        - Game information and score tracking
        - Move history and player analysis
        - Thinking animations and move visualizations

    Attributes:
        console (Console): Rich console for output
        layout (Layout): Layout manager for UI components
        colors (dict): Color schemes for different UI elements

    Examples:
        >>> ui = DominoesRichUI()
        >>> state = DominoesState.initialize()
        >>> ui.display_state(state)  # Display the initial game state
    """

    def __init__(self, console: Console | None = None):
        """Initialize the UI.

        Args:
            console: Optional Rich console instance
        """
        self.console = console or Console()

        # Define colors and styles
        self.colors = {
            "player1": "bright_red",
            "player2": "bright_blue",
            "header": "bold yellow",
            "board": "green",
            "tile": "cyan",
            "double_tile": "bright_magenta",
            "open_end": "bright_green",
            "pip": "bright_white",
            "info": "bright_white",
            "success": "green",
            "warning": "bright_yellow",
            "error": "bright_red",
            "panel_border": "bright_cyan",
        }

    def extract_game_state(self, state_data: Any) -> DominoesState | None:
        """Extract DominoesState from various input formats.

        Args:
            state_data: State data in various formats

        Returns:
            DominoesState instance or None if extraction fails
        """
        try:
            # Handle None input gracefully
            if state_data is None:
                logger.warning("Received None state_data")
                return None

            # If it's already a DominoesState, return it
            if isinstance(state_data, DominoesState):
                return state_data

            # Handle langgraph Command objects
            if hasattr(state_data, "update"):
                command_update = state_data.update

                # Handle Command objects where update is already a DominoesState
                if isinstance(command_update, DominoesState):
                    return command_update

                # Handle Command objects where update is a dict
                if isinstance(command_update, dict):
                    if self._is_valid_game_state_dict(command_update):
                        try:
                            return DominoesState.model_validate(command_update)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create DominoesState from Command.update: {e}"
                            )

            # For direct dict output from langgraph stream
            if isinstance(state_data, dict) and self._is_valid_game_state_dict(
                state_data
            ):
                try:
                    return DominoesState.model_validate(state_data)
                except Exception as e:
                    logger.warning(
                        f"Failed to create DominoesState from direct dict: {e}"
                    )

            # If it's a dict, try to extract from nested structure
            if isinstance(state_data, dict):
                # First check for 'values' key which is used in langgraph stream output
                if "values" in state_data and isinstance(state_data["values"], dict):
                    values_dict = state_data["values"]
                    if self._is_valid_game_state_dict(values_dict):
                        try:
                            return DominoesState.model_validate(values_dict)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create DominoesState from 'values': {e}"
                            )

                # First, try to find a DominoesState object in the dict values
                for key, value in state_data.items():
                    if isinstance(value, DominoesState):
                        return value

                # Next, try to find a dict that can be converted to DominoesState
                for key, value in state_data.items():
                    if isinstance(value, dict) and self._is_valid_game_state_dict(
                        value
                    ):
                        try:
                            return DominoesState.model_validate(value)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create DominoesState from {key}: {e}"
                            )
                            continue

                # Create a minimal game state if nothing else works
                if "hands" in state_data and isinstance(state_data["hands"], dict):
                    try:
                        minimal_state = {
                            "players": list(state_data["hands"].keys()),
                            "hands": state_data["hands"],
                            "board": state_data.get("board", []),
                            "boneyard": state_data.get("boneyard", []),
                            "turn": state_data.get("turn", "player1"),
                            "game_status": state_data.get("game_status", "ongoing"),
                            "move_history": state_data.get("move_history", []),
                            "last_passes": state_data.get("last_passes", 0),
                            "scores": state_data.get("scores", {}),
                        }
                        return DominoesState.model_validate(minimal_state)
                    except Exception as e:
                        logger.warning(f"Failed to create minimal state: {e}")

            # Handle other types
            logger.warning(f"Unsupported state type: {type(state_data)}")
            return None

        except Exception as e:
            logger.error(f"Error extracting game state: {e}", exc_info=True)
            return None

    def _is_valid_game_state_dict(self, data: dict) -> bool:
        """Check if a dict contains the required fields for DominoesState.

        Args:
            data: Dictionary to check

        Returns:
            True if the dict appears to be a valid game state
        """
        required_fields = {
            "players",
            "hands",
            "board",
            "boneyard",
            "turn",
            "game_status",
        }
        return all(field in data for field in required_fields)

    def create_domino_tile_art(self, tile: DominoTile, open_end: bool = False) -> Text:
        """Create ASCII art representation of a domino tile.

        Args:
            tile: The domino tile to represent
            open_end: Whether this tile is at an open end of the board

        Returns:
            Rich Text object with tile representation
        """
        # Determine tile style
        if tile.is_double():
            tile_style = self.colors["double_tile"]
        else:
            tile_style = self.colors["tile"]

        # For open ends, highlight with a different color
        if open_end:
            tile_style = self.colors["open_end"]

        # Create the domino representation
        domino_art = ["┌───┬───┐", f"│ {tile.left} │ {tile.right} │", "└───┴───┘"]

        return Text("\n".join(domino_art), style=tile_style)

    def create_board_panel(self, game_state: DominoesState) -> Panel:
        """Create a visual representation of the dominoes board.

        Args:
            game_state: Current game state

        Returns:
            Rich panel representing the board
        """
        if not game_state.board:
            board_text = Text(
                "🎲 Empty Board - Play the first tile! 🎲",
                style="yellow",
                justify="center",
            )
            return Panel(
                Align.center(board_text),
                title="[bold]Game Board[/bold]",
                border_style=self.colors["board"],
                box=ROUNDED,
                padding=(1, 1),
            )

        # Create a table for the board
        Table(
            show_header=False,
            box=None,
            padding=(0, 1),
            show_edge=False,
            collapse_padding=True,
        )

        # Add the tiles in a row
        tile_arts = []
        for i, tile in enumerate(game_state.board):
            # Check if this is an open end
            is_left_end = i == 0
            is_right_end = i == len(game_state.board) - 1

            # Create the tile art
            if is_left_end or is_right_end:
                tile_art = self.create_domino_tile_art(tile, open_end=True)
            else:
                tile_art = self.create_domino_tile_art(tile)

            tile_arts.append(tile_art)

        # If there are too many tiles to fit, show only first 3 and last 3
        if len(tile_arts) > 8:
            connector = Text("   ...   ", style="bold white")
            displayed_tiles = tile_arts[:3] + [connector] + tile_arts[-3:]
        else:
            displayed_tiles = tile_arts

        # Add connector arrows between tiles
        connected_tiles = []
        for i, tile_art in enumerate(displayed_tiles):
            if i > 0:
                connected_tiles.append(Text(" → ", style="bold white"))
            connected_tiles.append(tile_art)

        # Add to a group for display
        board_group = Group(*connected_tiles)

        # Create the panel
        board_panel = Panel(
            Align.center(board_group),
            title="[bold]Game Board[/bold]",
            border_style=self.colors["board"],
            box=ROUNDED,
            padding=(1, 1),
        )

        return board_panel

    def create_player_hand_panel(self, game_state: DominoesState, player: str) -> Panel:
        """Create a panel showing a player's hand.

        Args:
            game_state: Current game state
            player: Player whose hand to display

        Returns:
            Rich panel with player's hand
        """
        hand = game_state.hands[player]
        player_color = self.colors[player]

        if not hand:
            hand_text = Text("No tiles in hand", style="dim", justify="center")
            return Panel(
                hand_text,
                title=f"[bold {player_color}]{player}'s Hand[/bold {player_color}]",
                border_style=player_color,
                box=ROUNDED,
                padding=(1, 1),
            )

        # Create a table for the tiles
        hand_table = Table(
            show_header=False,
            box=None,
            padding=(0, 1),
            show_edge=False,
        )

        # Add columns
        max_cols = 4  # Maximum tiles per row
        for _ in range(min(max_cols, len(hand))):
            hand_table.add_column(justify="center")

        # Create tiles grouped by rows
        rows = []
        current_row = []

        for tile in sorted(hand, key=lambda t: (t.left, t.right)):
            current_row.append(self.create_domino_tile_art(tile))
            if len(current_row) == max_cols:
                rows.append(current_row)
                current_row = []

        if current_row:
            # Pad the last row if needed
            while len(current_row) < max_cols:
                current_row.append(Text(""))
            rows.append(current_row)

        # Add rows to the table
        for row in rows:
            hand_table.add_row(*row)

        # Calculate pip count
        pip_count = sum(tile.left + tile.right for tile in hand)
        pip_text = Text(f"Total Pip Count: {pip_count}", style="dim")

        # Is it this player's turn?
        is_current = player == game_state.turn
        title_suffix = " [bold green](Current Turn)[/bold green]" if is_current else ""

        # Create the panel
        panel = Panel(
            Group(
                Align.center(hand_table),
                Align.center(pip_text),
            ),
            title=f"[bold {player_color}]{player}'s Hand[/bold {player_color}]{title_suffix}",
            border_style=player_color,
            box=ROUNDED,
            padding=(1, 1),
        )

        return panel

    def create_game_info_panel(self, game_state: DominoesState) -> Panel:
        """Create a panel with game information.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with game info
        """
        # Create a table for the info
        info_table = Table(
            show_header=False,
            box=None,
            show_edge=False,
            padding=(0, 1),
        )

        info_table.add_column("Key", style="bright_blue", width=20)
        info_table.add_column("Value", style="white")

        # Game status
        if game_state.game_status == "ongoing":
            status_text = "[green]Game in Progress[/green]"
        elif "win" in game_state.game_status:
            winner = game_state.winner or game_state.game_status.split("_")[0]
            winner_color = self.colors[winner] if winner in self.colors else "yellow"
            status_text = f"[{winner_color}]{winner} Wins![/{winner_color}]"
        else:
            status_text = f"[yellow]{game_state.game_status}[/yellow]"

        info_table.add_row("Game Status", status_text)

        # Current player
        player_color = self.colors[game_state.turn]
        info_table.add_row(
            "Current Turn",
            f"[bold {player_color}]{game_state.turn}[/bold {player_color}]",
        )

        # Boneyard
        info_table.add_row(
            "Boneyard Tiles", f"[bold]{len(game_state.boneyard)}[/bold] tiles remaining"
        )

        # Consecutive passes
        info_table.add_row(
            "Consecutive Passes", f"[bold]{game_state.last_passes}[/bold]"
        )

        # Add separator
        info_table.add_row("", "")

        # Scores
        info_table.add_row("📊 Scores", "")
        for player, score in game_state.scores.items():
            player_color = self.colors[player] if player in self.colors else "white"
            info_table.add_row(
                f"  {player}",
                f"[bold {player_color}]{score}[/bold {player_color}] points",
            )

        # Open ends if board is not empty
        if game_state.board:
            info_table.add_row("", "")
            info_table.add_row("Open Ends", "")
            if game_state.left_value is not None:
                info_table.add_row(
                    "  Left End",
                    f"[bold {self.colors['open_end']}]{game_state.left_value}[/bold {self.colors['open_end']}]",
                )
            if game_state.right_value is not None:
                info_table.add_row(
                    "  Right End",
                    f"[bold {self.colors['open_end']}]{game_state.right_value}[/bold {self.colors['open_end']}]",
                )

        return Panel(
            info_table,
            title="[bold]Game Information[/bold]",
            border_style="bright_blue",
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_move_history_panel(self, game_state: DominoesState) -> Panel:
        """Create a panel showing move history.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with move history
        """
        if not game_state.move_history:
            history_text = Text(
                "No moves have been made yet", style="dim", justify="center"
            )
            return Panel(
                history_text,
                title="[bold]Move History[/bold]",
                border_style="yellow",
                box=ROUNDED,
                padding=(1, 1),
            )

        # Create a table for the moves
        history_table = Table(
            show_header=True,
            box=None,
            padding=(0, 1),
        )

        history_table.add_column("#", style="dim", width=3)
        history_table.add_column("Player", style="white")
        history_table.add_column("Move", style="white")

        # Show the last 8 moves at most
        start_idx = max(0, len(game_state.move_history) - 8)

        for i, move in enumerate(
            game_state.move_history[start_idx:], start=start_idx + 1
        ):
            # Determine player
            player_idx = (i - 1) % len(game_state.players)
            player = game_state.players[player_idx]
            player_color = self.colors[player] if player in self.colors else "white"

            # Format the move
            if move == "pass":
                move_text = "[yellow]Pass[/yellow]"
            else:
                # It's a DominoMove
                tile_str = f"[{move.tile.left}|{move.tile.right}]"
                if move.tile.is_double():
                    tile_str = f"[{self.colors['double_tile']}]{tile_str}[/{self.colors['double_tile']}]"
                else:
                    tile_str = (
                        f"[{self.colors['tile']}]{tile_str}[/{self.colors['tile']}]"
                    )

                move_text = f"{tile_str} on {move.location} end"

            history_table.add_row(
                str(i), f"[{player_color}]{player}[/{player_color}]", move_text
            )

        return Panel(
            history_table,
            title="[bold]Move History[/bold]",
            border_style="yellow",
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_analysis_panel(self, game_state: DominoesState) -> Panel:
        """Create a panel showing the latest analysis.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with analysis info
        """
        # Create a table for the analysis
        analysis_table = Table(
            show_header=True,
            box=None,
            padding=(0, 1),
        )

        analysis_table.add_column("Player", style="white")
        analysis_table.add_column("Hand Strength", style="white")
        analysis_table.add_column("Strategy", style="white")

        has_analysis = False

        if hasattr(game_state, "player1_analysis") and game_state.player1_analysis:
            has_analysis = True
            latest_analysis = game_state.player1_analysis[-1]

            # Create a strength meter
            strength = latest_analysis.hand_strength
            strength_meter = "█" * strength + "░" * (10 - strength)
            strength_color = (
                "green" if strength >= 7 else "yellow" if strength >= 4 else "red"
            )

            # Get the strategy summary
            strategy = latest_analysis.suggested_strategy[:50]
            if len(latest_analysis.suggested_strategy) > 50:
                strategy += "..."

            analysis_table.add_row(
                f"[{self.colors['player1']}]player1[/{self.colors['player1']}]",
                f"[{strength_color}]{strength}/10 {strength_meter}[/{strength_color}]",
                strategy,
            )

        if hasattr(game_state, "player2_analysis") and game_state.player2_analysis:
            has_analysis = True
            latest_analysis = game_state.player2_analysis[-1]

            # Create a strength meter
            strength = latest_analysis.hand_strength
            strength_meter = "█" * strength + "░" * (10 - strength)
            strength_color = (
                "green" if strength >= 7 else "yellow" if strength >= 4 else "red"
            )

            # Get the strategy summary
            strategy = latest_analysis.suggested_strategy[:50]
            if len(latest_analysis.suggested_strategy) > 50:
                strategy += "..."

            analysis_table.add_row(
                f"[{self.colors['player2']}]player2[/{self.colors['player2']}]",
                f"[{strength_color}]{strength}/10 {strength_meter}[/{strength_color}]",
                strategy,
            )

        if not has_analysis:
            no_analysis_text = Text(
                "No analysis available yet", style="dim", justify="center"
            )
            return Panel(
                no_analysis_text,
                title="[bold]Player Analysis[/bold]",
                border_style="magenta",
                box=ROUNDED,
                padding=(1, 1),
            )

        return Panel(
            analysis_table,
            title="[bold]Player Analysis[/bold]",
            border_style="magenta",
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_layout(self, game_state: DominoesState) -> Layout:
        """Create the complete rich UI layout.

        Args:
            game_state: Current game state

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
            "🎲 DOMINOES GAME 🎲", style=self.colors["header"], justify="center"
        )
        layout["header"].update(
            Panel(header_text, border_style=self.colors["panel_border"], box=ROUNDED)
        )

        # Split main into board and sidebar
        layout["main"].split_row(
            Layout(name="left_column", ratio=3),
            Layout(name="right_column", ratio=2),
        )

        # Left column - split into board and hands
        layout["main"]["left_column"].split(
            Layout(name="board", size=8),
            Layout(name="hands", ratio=1),
            Layout(name="move_history", size=12),
        )

        # Add the board
        layout["main"]["left_column"]["board"].update(
            self.create_board_panel(game_state)
        )

        # Split hands into player1 and player2
        layout["main"]["left_column"]["hands"].split_row(
            Layout(name="player1_hand"),
            Layout(name="player2_hand"),
        )

        # Add player hands
        layout["main"]["left_column"]["hands"]["player1_hand"].update(
            self.create_player_hand_panel(game_state, "player1")
        )
        layout["main"]["left_column"]["hands"]["player2_hand"].update(
            self.create_player_hand_panel(game_state, "player2")
        )

        # Add move history
        layout["main"]["left_column"]["move_history"].update(
            self.create_move_history_panel(game_state)
        )

        # Right column - split into game info and analysis
        layout["main"]["right_column"].split(
            Layout(name="game_info", ratio=3),
            Layout(name="analysis", ratio=2),
        )

        # Add game info and analysis
        layout["main"]["right_column"]["game_info"].update(
            self.create_game_info_panel(game_state)
        )
        layout["main"]["right_column"]["analysis"].update(
            self.create_analysis_panel(game_state)
        )

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

    def show_thinking(self, player: str, message: str = "Thinking...") -> None:
        """Display a thinking animation for the current player.

        Shows a spinner animation with player-colored text to indicate
        that the player is thinking about their move.

        Args:
            player (str): Current player ("player1" or "player2")
            message (str, optional): Custom message to display. Defaults to "Thinking...".

        Returns:
            None
        """
        player_color = self.colors[player]

        with Progress(
            SpinnerColumn(),
            TextColumn(f"[{player_color}]{player.upper()}[/] {message}"),
            console=self.console,
            transient=True,
        ) as progress:
            progress.add_task("thinking", total=None)
            time.sleep(1.0)  # Show thinking animation for 1 second

    def show_move(self, move: DominoMove | str, player: str) -> None:
        """Display a move being made.

        Shows a formatted message indicating which player made which move,
        whether it's playing a tile or passing.

        Args:
            move (Union[DominoMove, str]): The move being made ("pass" or DominoMove)
            player (str): Player making the move ("player1" or "player2")

        Returns:
            None
        """
        player_color = self.colors[player]

        if move == "pass":
            move_panel = Panel(
                f"[{player_color}]{player.upper()}[/] draws a tile or passes their turn",
                title="[bold]Move[/bold]",
                title_align="center",
                border_style=player_color,
                padding=(1, 2),
            )
        else:
            # It's a tile placement
            tile_str = f"[{move.tile.left}|{move.tile.right}]"
            if move.tile.is_double():
                tile_str = f"[{self.colors['double_tile']}]{tile_str}[/{self.colors['double_tile']}]"
            else:
                tile_str = f"[{self.colors['tile']}]{tile_str}[/{self.colors['tile']}]"

            move_panel = Panel(
                f"[{player_color}]{player.upper()}[/] plays {tile_str} on the {move.location} end",
                title="[bold]Move[/bold]",
                title_align="center",
                border_style=player_color,
                padding=(1, 2),
            )

        self.console.print(move_panel)
        time.sleep(0.5)  # Brief pause after showing the move

    def display_welcome(self) -> None:
        """Display welcome message."""
        welcome_text = Text(
            """
🎲 Welcome to Dominoes! 🎲

This is a classic tile-based game where:
• Players take turns placing matching dominoes
• The first player to use all their tiles wins
• If the game is locked, the player with the lowest pip count wins
• Strategic tile placement is key to victory

The game will be played by AI agents with real-time visualization!
        """.strip(),
            style="bold cyan",
        )

        self.console.print(
            Panel(
                welcome_text,
                title="[bold yellow]🎮 DOMINOES GAME 🎮[/bold yellow]",
                border_style="bright_green",
                box=DOUBLE,
                padding=(1, 2),
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

            # Calculate final pip counts
            pip_counts = {}
            for player, hand in game_state.hands.items():
                pip_counts[player] = sum(tile.left + tile.right for tile in hand)

            # Create results table
            results_table = Table(show_header=True, box=ROUNDED)
            results_table.add_column("Player", style="white")
            results_table.add_column("Tiles Left", style="white")
            results_table.add_column("Pip Count", style="white")
            results_table.add_column("Score", style="white")

            for player in game_state.players:
                player_color = self.colors[player] if player in self.colors else "white"
                tiles_left = len(game_state.hands[player])
                pip_count = pip_counts[player]
                score = game_state.scores.get(player, 0)

                results_table.add_row(
                    f"[{player_color}]{player}[/{player_color}]",
                    str(tiles_left),
                    str(pip_count),
                    f"[bold]{score}[/bold]",
                )

            # Create title based on result
            if game_state.game_status == "draw":
                title = "[bold yellow]Game Ended in a Draw![/bold yellow]"
                border_style = "yellow"
            elif game_state.winner:
                winner = game_state.winner
                winner_color = self.colors[winner] if winner in self.colors else "green"
                title = f"[bold {winner_color}]{winner} Wins the Game![/bold {winner_color}]"
                border_style = winner_color
            else:
                title = "[bold]Game Complete[/bold]"
                border_style = "green"

            self.console.print()
            self.console.print("=" * 50)
            self.console.print(
                Panel(
                    Group(
                        Align.center(Text("🏆 Final Results 🏆", style="bold yellow")),
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
        state_before: DominoesState,
        state_after: DominoesState,
        delay: float = 0.5,
    ) -> None:
        """Animate a move being made.

        Shows a smooth transition between the before and after states with
        visual indicators of what changed.

        Args:
            state_before: Game state before the move
            state_after: Game state after the move
            delay: Delay in seconds for the animation

        Returns:
            None
        """
        # Get the last move
        if not state_after.move_history:
            return

        last_move = state_after.move_history[-1]
        current_player = state_before.turn

        # Clear the screen for the animation
        self.console.clear()

        # Show the pre-move state
        self.console.print(self.create_layout(state_before))
        time.sleep(delay)

        # Show the thinking animation
        self.show_thinking(current_player)

        # Show the move being made
        self.show_move(last_move, current_player)

        # Show the post-move state
        self.console.print(self.create_layout(state_after))

    def display_game_with_animation(
        self, state_sequence: list[DominoesState], delay: float = 1.0
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

    def run_game_with_ui(self, agent, delay: float = 1.0) -> DominoesState:
        """Run a complete game with UI visualization.

        This method handles the entire game flow, including initialization,
        move animation, and final results display.

        Args:
            agent: The game agent that manages the game logic
            delay: Delay in seconds between game states

        Returns:
            Final game state
        """
        # Display welcome
        self.display_welcome()
        time.sleep(delay)

        # Initialize the game
        initial_state = agent.initialize_game()
        self.display_state(initial_state)
        time.sleep(delay)

        # Run the game with state tracking
        state_sequence = agent.run_game_with_state_tracking()

        # Animate through the state sequence
        self.display_game_with_animation(state_sequence, delay=delay)

        return state_sequence[-1] if state_sequence else initial_state
