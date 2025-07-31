"""Rich UI module for Dominoes game visualization.

This module provides rich console UI components for visualizing the Dominoes game.

"""

import logging
from typing import Any

from rich.align import Align
from rich.box import ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from haive.games.dominoes.state import DominoesState

logger = logging.getLogger(__name__)


class DominoesUI:
    """Rich UI for Dominoes game visualization."""

    def __init__(self, console: Console | None = None):
        """Initialize the UI.

        Args:
            console: Optional Rich console instance

        """
        self.console = console or Console()

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
                logger.debug("State is already DominoesState")
                return state_data

            # Handle langgraph Command objects
            if hasattr(state_data, "update"):
                logger.debug("State appears to be a Command object")
                command_update = state_data.update

                # Handle Command objects where update is already a
                # DominoesState
                if isinstance(command_update, DominoesState):
                    logger.debug("Command.update is already a DominoesState")
                    return command_update

                # Handle Command objects where update is a dict
                if isinstance(command_update, dict):
                    if self._is_valid_game_state_dict(command_update):
                        try:
                            logger.debug(
                                "Creating DominoesState from Command.update dict"
                            )
                            return DominoesState.model_validate(command_update)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create DominoesState from Command.update: {e}"
                            )
                    else:
                        logger.debug(
                            f"Command.update dict doesn't have required fields: {
                                list(command_update.keys())
                            }"
                        )

            # For direct dict output from langgraph stream - simple dict from
            # command.update
            if isinstance(state_data, dict) and self._is_valid_game_state_dict(
                state_data
            ):
                logger.debug("Direct dict is a valid game state")
                try:
                    return DominoesState.model_validate(state_data)
                except Exception as e:
                    logger.warning(
                        f"Failed to create DominoesState from direct dict: {e}"
                    )

            # If it's a dict, try to extract from nested structure
            if isinstance(state_data, dict):
                logger.debug(f"State is dict with keys: {list(state_data.keys())}")

                # First check for 'values' key which is used in langgraph
                # stream output
                if "values" in state_data and isinstance(state_data["values"], dict):
                    values_dict = state_data["values"]
                    if self._is_valid_game_state_dict(values_dict):
                        logger.debug("Found valid game state in 'values' key")
                        try:
                            return DominoesState.model_validate(values_dict)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create DominoesState from 'values': {e}"
                            )
                    else:
                        logger.debug(
                            f"'values' dict doesn't have required fields: {
                                list(values_dict.keys())
                            }"
                        )

                # First, try to find a DominoesState object in the dict values
                for key, value in state_data.items():
                    if isinstance(value, DominoesState):
                        logger.debug(f"Found DominoesState in key: {key}")
                        return value

                # Next, try to find a dict that can be converted to
                # DominoesState
                for key, value in state_data.items():
                    if isinstance(value, dict) and self._is_valid_game_state_dict(
                        value
                    ):
                        logger.debug(f"Found state dict in key: {key}")
                        try:
                            return DominoesState.model_validate(value)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create DominoesState from {key}: {e}"
                            )
                            continue

                # If all else fails, try to get at least some state dict we can
                # work with
                logger.warning(
                    f"Could not find valid game state in dict with keys: {
                        list(state_data.keys())
                    }"
                )

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
                        logger.debug("Created minimal state from partial data")
                        return DominoesState.model_validate(minimal_state)
                    except Exception as e:
                        logger.warning(f"Failed to create minimal state: {e}")

                return None

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

    def create_board_panel(self, game_state: DominoesState) -> Panel:
        """Create a visual representation of the dominoes board.

        Args:
            game_state: Current game state

        Returns:
            Rich panel representing the board

        """
        if not game_state.board:
            board_text = Text("🀱 Empty Board - Play the first tile! 🀱", style="yellow")
            return Panel(
                Align.center(board_text),
                title="[bold]Game Board[/bold]",
                border_style="blue",
                box=ROUNDED,
            )

        # Create a visual representation of the dominoes
        board_tiles = []
        for tile in game_state.board:
            tile_str = f"[{tile.left}|{tile.right}]"
            # Add color based on the tile values
            if tile.is_double():
                board_tiles.append(f"[bold magenta]{tile_str}[/bold magenta]")
            else:
                board_tiles.append(f"[cyan]{tile_str}[/cyan]")

        # Join the tiles with connectors
        board_display = " - ".join(board_tiles)

        # Highlight the open ends
        if game_state.left_value is not None:
            board_display = (
                f"[bold green]{game_state.left_value}[/bold green] << " + board_display
            )
        if game_state.right_value is not None:
            board_display = (
                board_display + f" >> [bold green]{game_state.right_value}[/bold green]"
            )

        # Create panel
        return Panel(
            Align.center(Text(board_display)),
            title="[bold]Game Board[/bold]",
            border_style="blue",
            box=ROUNDED,
        )

    def create_player_hand_panel(self, game_state: DominoesState, player: str) -> Panel:
        """Create a panel showing a player's hand.

        Args:
            game_state: Current game state
            player: Player whose hand to display

        Returns:
            Rich panel with player's hand

        """
        hand = game_state.hands[player]

        if not hand:
            hand_text = "[dim]No tiles in hand[/dim]"
            return Panel(
                hand_text,
                title=f"[bold]{player}'s Hand[/bold]",
                border_style="red" if player == "player1" else "blue",
                box=ROUNDED,
            )

        # Create a table for the tiles
        hand_table = Table(show_header=False, box=None, padding=1)

        # Calculate tiles per row
        tiles_per_row = 5

        # Create formatted tile strings
        tile_strs = []
        for tile in hand:
            # Color doubles differently
            if tile.is_double():
                tile_strs.append(
                    f"[bold magenta][{tile.left}|{tile.right}][/bold magenta]"
                )
            else:
                tile_strs.append(f"[cyan][{tile.left}|{tile.right}][/cyan]")

        # Add rows to the table
        for i in range(0, len(tile_strs), tiles_per_row):
            row_tiles = tile_strs[i : i + tiles_per_row]
            hand_table.add_row(*row_tiles)

        # Add pip count
        pip_count = sum(tile.left + tile.right for tile in hand)
        pip_text = Text(f"\nTotal Pip Count: {pip_count}", style="dim")

        # Create the panel
        panel_style = "red" if player == "player1" else "blue"
        is_current = player == game_state.turn
        title = f"[bold]{player}'s Hand[/bold]" + (
            " [bold green](Current Turn)[/bold green]" if is_current else ""
        )

        return Panel(
            Layout(
                renderable=hand_table,
                size=len(hand_table.rows) + 1,  # Adjust size based on content
            ).split(Layout(pip_text)),
            title=title,
            border_style=panel_style,
            box=ROUNDED,
        )

    def create_game_info_panel(self, game_state: DominoesState) -> Panel:
        """Create a panel with game information.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with game info

        """
        # Current player indicator
        current_player = f"🎮 {game_state.turn}'s Turn"
        player_color = "red" if game_state.turn == "player1" else "blue"

        # Game status
        if game_state.game_status == "ongoing":
            status_text = "[green]Game in Progress[/green]"
        elif "win" in game_state.game_status:
            winner = game_state.winner or game_state.game_status.split("_")[0]
            status_text = f"[yellow]{winner} Wins![/yellow]"
        else:
            status_text = f"[yellow]{game_state.game_status}[/yellow]"

        # Boneyard count
        boneyard_text = f"🎲 Boneyard: [bold]{len(game_state.boneyard)}[/bold] tiles"

        # Last passes
        passes_text = f"⏭️ Consecutive Passes: [bold]{game_state.last_passes}[/bold]"

        # Scores
        scores_text = "📊 Scores:"
        for player, score in game_state.scores.items():
            color = "red" if player == "player1" else "blue"
            scores_text += f"\n  [{color}]{player}[/{color}]: [bold]{score}[/bold]"

        info_text = f"""[bold {player_color}]{current_player}[/bold {player_color}]

{status_text}

{boneyard_text}
{passes_text}

{scores_text}"""

        return Panel(
            info_text, title="[bold]Game Info[/bold]", border_style="green", box=ROUNDED
        )

    def create_last_move_panel(self, game_state: DominoesState) -> Panel:
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
            if last_move == "pass":
                last_move_text = "[yellow]Pass[/yellow]"
            else:
                player_idx = (game_state.players.index(game_state.turn) - 1) % len(
                    game_state.players
                )
                last_player = game_state.players[player_idx]
                color = "red" if last_player == "player1" else "blue"

                tile_str = f"[{last_move.tile.left}|{last_move.tile.right}]"
                if last_move.tile.is_double():
                    tile_str = f"[bold magenta]{tile_str}[/bold magenta]"
                else:
                    tile_str = f"[cyan]{tile_str}[/cyan]"

                last_move_text = f"[{color}]{last_player}[/{color}] played {tile_str} on the {last_move.location} end"

        return Panel(
            last_move_text,
            title="[bold]Last Move[/bold]",
            border_style="yellow",
            box=ROUNDED,
        )

    def create_analysis_panel(self, game_state: DominoesState) -> Panel:
        """Create a panel showing the latest analysis.

        Args:
            game_state: Current game state

        Returns:
            Rich panel with analysis info

        """
        analysis_text = ""

        if hasattr(game_state, "player1_analysis") and game_state.player1_analysis:
            latest_analysis = game_state.player1_analysis[-1]
            summary = f"Hand Strength: {latest_analysis.hand_strength}/10"
            if hasattr(latest_analysis, "suggested_strategy"):
                summary += f"\nStrategy: {latest_analysis.suggested_strategy}"
            analysis_text += f"[red]Player1 Analysis:[/red]\n{summary}\n\n"

        if hasattr(game_state, "player2_analysis") and game_state.player2_analysis:
            latest_analysis = game_state.player2_analysis[-1]
            summary = f"Hand Strength: {latest_analysis.hand_strength}/10"
            if hasattr(latest_analysis, "suggested_strategy"):
                summary += f"\nStrategy: {latest_analysis.suggested_strategy}"
            analysis_text += f"[blue]Player2 Analysis:[/blue]\n{summary}"

        if not analysis_text:
            analysis_text = "[dim]No analysis yet[/dim]"

        return Panel(
            analysis_text,
            title="[bold]Latest Analysis[/bold]",
            border_style="magenta",
            box=ROUNDED,
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
        layout.split_column(Layout(name="header", size=3), Layout(name="body"))

        # Header
        title = Text("🎲 Dominoes Game 🎲", style="bold magenta", justify="center")
        layout["header"].update(Panel(title, box=ROUNDED))

        # Split body into sections
        layout["body"].split_column(
            Layout(name="board", size=5),
            Layout(name="hands"),
            Layout(name="info", size=15),
        )

        # Board section
        layout["body"]["board"].update(self.create_board_panel(game_state))

        # Hands section - split into player hands
        layout["body"]["hands"].split_row(
            Layout(name="player1_hand"),
            Layout(name="player2_hand"),
        )
        layout["body"]["hands"]["player1_hand"].update(
            self.create_player_hand_panel(game_state, "player1")
        )
        layout["body"]["hands"]["player2_hand"].update(
            self.create_player_hand_panel(game_state, "player2")
        )

        # Info section - split into game info, last move, and analysis
        layout["body"]["info"].split_row(
            Layout(name="game_info"),
            Layout(name="last_move"),
            Layout(name="analysis"),
        )
        layout["body"]["info"]["game_info"].update(
            self.create_game_info_panel(game_state)
        )
        layout["body"]["info"]["last_move"].update(
            self.create_last_move_panel(game_state)
        )
        layout["body"]["info"]["analysis"].update(
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
            style="bold blue",
        )

        self.console.print(
            Panel(
                welcome_text,
                title="[bold magenta]🎮 Dominoes Game 🎮[/bold magenta]",
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

            # Calculate final pip counts
            pip_counts = {}
            for player, hand in game_state.hands.items():
                pip_counts[player] = sum(tile.left + tile.right for tile in hand)

            # Create result text
            if "win" in status:
                player_color = "red" if winner == "player1" else "blue"
                result_text = (
                    f"[bold {player_color}]{winner} Wins![/bold {player_color}] 🎉\n"
                )
                result_text += f"Final Score: {game_state.scores.get(winner, 0)}\n"
            else:
                result_text = "[bold yellow]Game ended in a draw![/bold yellow]\n"

            result_text += "\nFinal Pip Counts:"
            for player, count in pip_counts.items():
                player_color = "red" if player == "player1" else "blue"
                result_text += f"\n[{player_color}]{player}[/{player_color}]: {count}"

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
        elif isinstance(state_data, DominoesState):
            logger.debug(
                f"Game state - Turn: {state_data.turn}, Status: {state_data.game_status}"
            )
            logger.debug(f"Board: {state_data.board_string}")
            logger.debug(f"Hands: {len(state_data.hands)}")
            for player, hand in state_data.hands.items():
                logger.debug(f"  {player}: {[str(tile) for tile in hand]}")
        else:
            logger.debug(f"Raw value: {str(state_data)[:200]}")

        logger.debug("=== END DEBUG INFO ===")
