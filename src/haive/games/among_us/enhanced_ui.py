"""Enhanced Rich UI module for Among Us game visualization.

This module provides an enhanced rich console UI for visualizing the Among Us game, with
better styling, animated visualizations, and improved game information display.

"""

import logging
import time
from typing import Any

from rich.box import DOUBLE, ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from haive.games.among_us.models import AmongUsGamePhase, PlayerRole, TaskStatus
from haive.games.among_us.state import AmongUsState

logger = logging.getLogger(__name__)


class EnhancedAmongUsUI:
    """Enhanced UI for Among Us game with rich terminal graphics.

    This class provides a visually appealing terminal UI for Among Us games,
    with styled components, animations, and comprehensive game information.

    Features:
        - Beautiful game map visualization with colored squares
        - Animated transitions between game states
        - Detailed player status display
        - Vent and sabotage system visualization
        - Meeting and voting interfaces
        - Game over screens with detailed statistics

    """

    def __init__(self, console: Console | None = None):
        """Initialize the UI.

        Args:
            console: Optional Rich console instance

        """
        self.console = console or Console()

        # Define colors and styles
        self.colors = {
            "crewmate": "bright_green",
            "impostor": "bright_red",
            "dead": "dim red",
            "highlight": "bright_yellow",
            "warning": "bright_yellow",
            "danger": "bright_red",
            "info": "bright_cyan",
            "success": "bright_green",
            "header": "bright_magenta",
            "panel_border": "cyan",
            "task": "bright_yellow",
            "cafeteria": "bright_white",
            "electrical": "bright_yellow",
            "security": "bright_magenta",
            "medbay": "bright_green",
            "storage": "bright_blue",
            "weapons": "bright_red",
            "o2": "bright_cyan",
            "navigation": "bright_blue",
            "admin": "bright_magenta",
            "shields": "bright_yellow",
            "communications": "bright_green",
            "reactor": "bright_red",
            "upper_engine": "bright_blue",
            "lower_engine": "bright_blue",
        }

        # Symbols for UI elements
        self.symbols = {
            "crewmate": "👤",
            "impostor": "👤",  # Same symbol for secrecy
            "dead_body": "💀",
            "task_incomplete": "◻️",
            "task_complete": "✅",
            "vent": "↕️",
            "meeting": "🔔",
            "emergency": "🚨",
            "sabotage": "⚠️",
            "vote": "✓",
        }

        # Map element symbols
        self.map_symbols = {
            "room": "□",
            "current_room": "■",
            "vent": "⊛",
            "player": "●",
            "task": "✧",
            "dead_body": "☠",
            "connection": "─",
            "vertical_connection": "│",
            "diagonal_up": "╱",
            "diagonal_down": "╲",
            "corner_topleft": "┌",
            "corner_topright": "┐",
            "corner_bottomleft": "└",
            "corner_bottomright": "┘",
            "t_up": "┴",
            "t_down": "┬",
            "t_left": "┤",
            "t_right": "├",
            "cross": "┼",
        }

    def extract_game_state(self, state_data: Any) -> AmongUsState | None:
        """Extract AmongUsState from various input formats.

        Args:
            state_data: State data in various formats

        Returns:
            AmongUsState instance or None if extraction fails

        """
        try:
            # Handle None input gracefully
            if state_data is None:
                logger.warning("Received None state_data")
                return None

            # If it's already a AmongUsState, return it
            if isinstance(state_data, AmongUsState):
                return state_data

            # Handle langgraph Command objects
            if hasattr(state_data, "update"):
                command_update = state_data.update

                # Handle Command objects where update is already a AmongUsState
                if isinstance(command_update, AmongUsState):
                    return command_update

                # Handle Command objects where update is a dict
                if isinstance(command_update, dict):
                    if self._is_valid_game_state_dict(command_update):
                        try:
                            return AmongUsState.model_validate(command_update)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create AmongUsState from Command.update: {e}"
                            )

            # For direct dict output from langgraph stream
            if isinstance(state_data, dict) and self._is_valid_game_state_dict(
                state_data
            ):
                try:
                    return AmongUsState.model_validate(state_data)
                except Exception as e:
                    logger.warning(
                        f"Failed to create AmongUsState from direct dict: {e}"
                    )

            # If it's a dict, try to extract from nested structure
            if isinstance(state_data, dict):
                # First check for 'values' key which is used in langgraph
                # stream output
                if "values" in state_data and isinstance(state_data["values"], dict):
                    values_dict = state_data["values"]
                    if self._is_valid_game_state_dict(values_dict):
                        try:
                            return AmongUsState.model_validate(values_dict)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create AmongUsState from 'values': {e}"
                            )

                # First, try to find a AmongUsState object in the dict values
                for key, value in state_data.items():
                    if isinstance(value, AmongUsState):
                        return value

                # Next, try to find a dict that can be converted to
                # AmongUsState
                for key, value in state_data.items():
                    if isinstance(value, dict) and self._is_valid_game_state_dict(
                        value
                    ):
                        try:
                            return AmongUsState.model_validate(value)
                        except Exception as e:
                            logger.warning(
                                f"Failed to create AmongUsState from {key}: {e}"
                            )
                            continue

            # Handle other types
            logger.warning(f"Unsupported state type: {type(state_data)}")
            return None

        except Exception as e:
            logger.error(f"Error extracting game state: {e}", exc_info=True)
            return None

    def _is_valid_game_state_dict(self, data: dict) -> bool:
        """Check if a dict contains the required fields for AmongUsState.

        Args:
            data: Dictionary to check

        Returns:
            True if the dict appears to be a valid game state

        """
        required_fields = {"player_states", "game_phase", "map_name"}
        return all(field in data for field in required_fields)

    def create_map_visualization(
        self, state: AmongUsState, player_id: str | None = None
    ) -> Panel:
        """Create a visual representation of the map with rooms, vents, and players.

        Args:
            state: Current game state
            player_id: Optional ID of the player whose perspective to show

        Returns:
            Rich panel containing the map visualization

        """
        # Get the current player's state if provided
        player_state = None
        if player_id and player_id in state.player_states:
            player_state = state.player_states[player_id]

        # Create a grid-based map representation
        map_name = state.map_name.capitalize()

        # Create map table
        map_table = Table(
            show_header=False, box=None, padding=(0, 1), collapse_padding=True
        )

        # Set up the map grid based on the map name
        if state.map_name.lower() == "skeld":
            # Create a simplified Skeld map layout
            # This is a simplified representation - adjust as needed
            grid = [
                ["", "weapons", "o2", "navigation"],
                ["cafeteria", "", "shields", ""],
                ["", "admin", "communications", ""],
                ["medbay", "", "storage", ""],
                ["upper_engine", "security", "electrical", ""],
                ["reactor", "", "lower_engine", ""],
            ]

            # Add columns to the table
            for _ in range(len(grid[0])):
                map_table.add_column(justify="center", no_wrap=True)

            # Process each row in the grid
            for row in grid:
                table_row = []
                for room_id in row:
                    if not room_id:
                        table_row.append("")
                        continue

                    room = state.get_room(room_id)
                    if not room:
                        table_row.append(f"[dim]{room_id}[/dim]")
                        continue

                    # Determine if this is the current player's location
                    is_current = player_state and player_state.location == room_id

                    # Count players in this room
                    players_in_room = [
                        pid
                        for pid, pstate in state.player_states.items()
                        if pstate.is_alive and pstate.location == room_id
                    ]

                    # Count dead bodies in this room
                    bodies_in_room = [
                        pid
                        for pid, pstate in state.player_states.items()
                        if not pstate.is_alive and pstate.location == room_id
                    ]

                    # Check if room has vents
                    has_vents = len(room.vents) > 0

                    # Generate room cell
                    room_style = self.colors.get(room_id, "white")
                    room_symbol = (
                        self.map_symbols["current_room"]
                        if is_current
                        else self.map_symbols["room"]
                    )

                    cell_content = (
                        f"[{room_style}]{room_symbol} {room.name}[/{room_style}]"
                    )

                    # Add player indicators
                    if players_in_room:
                        player_count = len(players_in_room)
                        cell_content += f"\n[{self.colors['info']}]{
                            self.map_symbols['player']
                        } {player_count} player{'s' if player_count > 1 else ''}[/{
                            self.colors['info']
                        }]"

                    # Add dead body indicators
                    if bodies_in_room:
                        body_count = len(bodies_in_room)
                        cell_content += f"\n[{self.colors['dead']}]{
                            self.map_symbols['dead_body']
                        } {body_count} bod{'ies' if body_count > 1 else 'y'}[/{
                            self.colors['dead']
                        }]"

                    # Add vent indicator
                    if has_vents:
                        cell_content += f"\n[dim]{self.map_symbols['vent']} vent[/dim]"

                    table_row.append(cell_content)

                map_table.add_row(*table_row)

        else:
            # For other maps, create a simple list of rooms
            map_table.add_column("Room", style="cyan")
            map_table.add_column("Players", style="white")
            map_table.add_column("Bodies", style="red")
            map_table.add_column("Vents", style="dim")

            for room_id, room in state.rooms.items():
                # Count players in this room
                players_in_room = [
                    pid
                    for pid, pstate in state.player_states.items()
                    if pstate.is_alive and pstate.location == room_id
                ]

                # Count dead bodies in this room
                bodies_in_room = [
                    pid
                    for pid, pstate in state.player_states.items()
                    if not pstate.is_alive and pstate.location == room_id
                ]

                # Check if room has vents
                has_vents = len(room.vents) > 0

                # Determine if this is the current player's location
                is_current = player_state and player_state.location == room_id
                room_style = (
                    "bold " + self.colors.get(room_id, "white")
                    if is_current
                    else self.colors.get(room_id, "white")
                )

                map_table.add_row(
                    f"[{room_style}]{room.name}[/{room_style}]",
                    f"{len(players_in_room)}" if players_in_room else "0",
                    (
                        f"[{self.colors['dead']}]{len(bodies_in_room)}[/{self.colors['dead']}]"
                        if bodies_in_room
                        else "0"
                    ),
                    "Yes" if has_vents else "No",
                )

        # Create the panel with the map
        return Panel(
            map_table,
            title=f"[bold]{map_name} Map[/bold]",
            border_style=self.colors["panel_border"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_player_info_panel(self, state: AmongUsState, player_id: str) -> Panel:
        """Create a panel with detailed information about the player.

        Args:
            state: Current game state
            player_id: ID of the player to show info for

        Returns:
            Rich panel containing player information

        """
        if player_id not in state.player_states:
            return Panel("Player not found", title="Player Info")

        player_state = state.player_states[player_id]

        # Create player info layout
        player_info = Layout()
        player_info.split(
            Layout(name="header"),
            Layout(name="tasks"),
            Layout(name="observations"),
        )

        # Player header
        role_color = (
            self.colors["impostor"]
            if player_state.is_impostor()
            else self.colors["crewmate"]
        )
        role_text = "IMPOSTOR" if player_state.is_impostor() else "CREWMATE"
        status_color = (
            self.colors["success"] if player_state.is_alive else self.colors["dead"]
        )
        status_text = "ALIVE" if player_state.is_alive else "DEAD"

        header_table = Table(
            show_header=False, box=None, show_edge=False, padding=(0, 1)
        )
        header_table.add_column("Key", style="bright_blue", width=10)
        header_table.add_column("Value", style="white")

        header_table.add_row("Name", f"[bold]{player_id}[/bold]")
        header_table.add_row("Role", f"[{role_color}]{role_text}[/{role_color}]")
        header_table.add_row(
            "Status", f"[{status_color}]{status_text}[/{status_color}]"
        )
        header_table.add_row(
            "Location",
            f"[{self.colors.get(player_state.location, 'white')}]{
                player_state.location.capitalize()
            }[/{self.colors.get(player_state.location, 'white')}]",
        )

        if player_state.in_vent:
            header_table.add_row(
                "In Vent",
                f"[{self.colors['warning']}]YES - {player_state.current_vent}[/{self.colors['warning']}]",
            )

        if player_state.is_impostor():
            kill_cooldown = state.get_player_cooldown(player_id)
            header_table.add_row(
                "Kill Cooldown",
                f"{kill_cooldown}s" if kill_cooldown > 0 else "[green]READY[/green]",
            )

        player_info["header"].update(header_table)

        # Player tasks
        tasks_table = Table(show_header=True, box=None, show_edge=False, padding=(0, 1))
        tasks_table.add_column("Status", style="white", width=4)
        tasks_table.add_column("Task", style="white")
        tasks_table.add_column("Location", style="white")

        for task in player_state.tasks:
            status_symbol = (
                self.symbols["task_complete"]
                if task.status == TaskStatus.COMPLETED
                else self.symbols["task_incomplete"]
            )
            status_color = (
                self.colors["success"]
                if task.status == TaskStatus.COMPLETED
                else self.colors["task"]
            )

            # Highlight current location tasks
            location_style = "bold " if task.location == player_state.location else ""
            location_style += self.colors.get(task.location, "white")

            tasks_table.add_row(
                f"[{status_color}]{status_symbol}[/{status_color}]",
                task.description,
                f"[{location_style}]{task.location.capitalize()}[/{location_style}]",
            )

        tasks_panel = Panel(
            tasks_table,
            title=f"[bold]Tasks ({sum(1 for t in player_state.tasks if t.status == TaskStatus.COMPLETED)}/{len(player_state.tasks)})[/bold]",
            border_style=self.colors["task"],
            box=ROUNDED,
            padding=(0, 1),
        )
        player_info["tasks"].update(tasks_panel)

        # Recent observations
        if player_state.observations:
            obs_text = ""
            # Show last 5 observations
            for obs in player_state.observations[-5:]:
                obs_text += f"• {obs}\n"

            observations_panel = Panel(
                Text(obs_text, style="italic"),
                title="[bold]Recent Observations[/bold]",
                border_style=self.colors["info"],
                box=ROUNDED,
                padding=(0, 1),
            )
        else:
            observations_panel = Panel(
                "No observations yet",
                title="[bold]Recent Observations[/bold]",
                border_style=self.colors["info"],
                box=ROUNDED,
                padding=(0, 1),
            )

        player_info["observations"].update(observations_panel)

        # Create the main panel
        return Panel(
            player_info,
            title=f"[bold]{player_id}'s Information[/bold]",
            border_style=role_color,
            box=ROUNDED,
            padding=(0, 0),
        )

    def create_game_info_panel(self, state: AmongUsState) -> Panel:
        """Create a panel with general game information.

        Args:
            state: Current game state

        Returns:
            Rich panel containing game information

        """
        # Create info table
        info_table = Table(show_header=False, box=None, show_edge=False, padding=(0, 1))
        info_table.add_column("Key", style="bright_blue", width=16)
        info_table.add_column("Value", style="white")

        # Game phase
        phase_color = {
            AmongUsGamePhase.TASKS: self.colors["task"],
            AmongUsGamePhase.MEETING: self.colors["warning"],
            AmongUsGamePhase.VOTING: self.colors["info"],
            AmongUsGamePhase.GAME_OVER: self.colors["danger"],
        }.get(state.game_phase, "white")

        info_table.add_row(
            "Game Phase",
            f"[{phase_color}]{state.game_phase.capitalize()}[/{phase_color}]",
        )
        info_table.add_row("Map", f"{state.map_name.capitalize()}")
        info_table.add_row("Round", f"{state.round_number}")

        # Player counts
        info_table.add_row("", "")
        info_table.add_row("Players", f"[bold]{len(state.player_states)}[/bold]")

        alive_players = sum(
            1 for pid, pstate in state.player_states.items() if pstate.is_alive
        )
        dead_players = sum(
            1 for pid, pstate in state.player_states.items() if not pstate.is_alive
        )

        info_table.add_row(
            "Alive",
            f"[{self.colors['success']}]{alive_players}[/{self.colors['success']}]",
        )
        info_table.add_row(
            "Dead", f"[{self.colors['dead']}]{dead_players}[/{self.colors['dead']}]"
        )

        # Task completion
        info_table.add_row("", "")
        info_table.add_row(
            "Task Completion",
            f"[{self.colors['task']}]{state.get_task_completion_percentage():.1f}%[/{self.colors['task']}]",
        )

        # Task progress bar
        task_percent = state.get_task_completion_percentage() / 100
        task_bar_width = 20
        completed_cells = int(task_percent * task_bar_width)
        task_bar = "█" * completed_cells + "░" * (task_bar_width - completed_cells)

        info_table.add_row(
            "Progress", f"[{self.colors['task']}]{task_bar}[/{self.colors['task']}]"
        )

        # Active sabotage
        active_sabotage = state.get_active_sabotage()
        if active_sabotage:
            info_table.add_row("", "")
            info_table.add_row(
                "Active Sabotage",
                f"[{self.colors['danger']}]{active_sabotage.type.upper()}[/{self.colors['danger']}]",
            )
            info_table.add_row("Time Remaining", f"{active_sabotage.timer}s")

            # Show resolution points
            for i, point in enumerate(active_sabotage.resolution_points):
                status = (
                    "[green]FIXED[/green]" if point.resolved else "[red]NOT FIXED[/red]"
                )
                info_table.add_row(
                    f"Fix Point {i + 1}", f"{point.location.capitalize()} - {status}"
                )

        # Create the panel
        return Panel(
            info_table,
            title="[bold]Game Information[/bold]",
            border_style=self.colors["panel_border"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_other_players_panel(self, state: AmongUsState, player_id: str) -> Panel:
        """Create a panel showing information about other players.

        Args:
            state: Current game state
            player_id: ID of the current player

        Returns:
            Rich panel containing other player information

        """
        if player_id not in state.player_states:
            return Panel("Player not found", title="Other Players")

        current_player = state.player_states[player_id]

        # Create table for other players
        players_table = Table(show_header=True, box=None, padding=(0, 1))
        players_table.add_column("Player", style="cyan")
        players_table.add_column("Status", style="white")
        players_table.add_column("Location", style="white")

        # Add role column for impostors
        if current_player.is_impostor():
            players_table.add_column("Role", style="red")

        # Add each player
        for pid, pstate in state.player_states.items():
            if pid == player_id:
                continue

            # Status with color
            status_color = (
                self.colors["success"] if pstate.is_alive else self.colors["dead"]
            )
            status_text = "ALIVE" if pstate.is_alive else "DEAD"

            # Location (only shown if in same room or during meeting)
            location_text = "Unknown"
            if (
                pstate.location == current_player.location
                or state.game_phase
                in [AmongUsGamePhase.MEETING, AmongUsGamePhase.VOTING]
                or current_player.is_impostor()
            ):
                location_text = pstate.location.capitalize()

            row_data = [
                pid,
                f"[{status_color}]{status_text}[/{status_color}]",
                location_text,
            ]

            # Add role for impostors
            if current_player.is_impostor():
                role_text = "IMPOSTOR" if pstate.is_impostor() else "CREWMATE"
                role_color = (
                    self.colors["impostor"]
                    if pstate.is_impostor()
                    else self.colors["crewmate"]
                )
                row_data.append(f"[{role_color}]{role_text}[/{role_color}]")

            players_table.add_row(*row_data)

        # Create panel
        return Panel(
            players_table,
            title="[bold]Other Players[/bold]",
            border_style=self.colors["info"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_meeting_panel(self, state: AmongUsState) -> Panel:
        """Create a panel for the meeting phase.

        Args:
            state: Current game state

        Returns:
            Rich panel for the meeting

        """
        if state.game_phase not in [AmongUsGamePhase.MEETING, AmongUsGamePhase.VOTING]:
            return Panel("No meeting in progress", title="Meeting")

        # Meeting layout
        meeting_layout = Layout()
        meeting_layout.split(
            Layout(name="header"),
            Layout(name="discussion", ratio=2),
            Layout(
                name="voting", visible=(state.game_phase == AmongUsGamePhase.VOTING)
            ),
        )

        # Meeting header
        header_text = ""
        if state.reported_body:
            header_text = f"[{self.colors['danger']}]{self.symbols['dead_body']} {state.meeting_caller} reported {state.reported_body}'s body[/{self.colors['danger']}]"
        else:
            header_text = f"[{self.colors['warning']}]{self.symbols['meeting']} {state.meeting_caller} called an emergency meeting[/{self.colors['warning']}]"

        meeting_layout["header"].update(
            Panel(
                Text(header_text, justify="center"),
                border_style=self.colors["panel_border"],
                box=ROUNDED,
                padding=(1, 1),
            )
        )

        # Discussion history
        if state.discussion_history:
            discussion_table = Table(
                show_header=False, box=None, show_edge=False, padding=(0, 1)
            )
            discussion_table.add_column("Player", style="cyan", width=10)
            discussion_table.add_column("Message", style="white")

            for msg in state.discussion_history[-10:]:  # Show last 10 messages
                player_id = msg.get("player_id", "Unknown")
                message = msg.get("message", "")

                # Color based on player status
                player_style = "cyan"
                if player_id in state.player_states:
                    player_style = (
                        self.colors["impostor"]
                        if state.player_states[player_id].is_impostor()
                        else self.colors["crewmate"]
                    )

                discussion_table.add_row(
                    f"[{player_style}]{player_id}:[/{player_style}]",
                    Text(message, style="italic"),
                )

            meeting_layout["discussion"].update(
                Panel(
                    discussion_table,
                    title="[bold]Discussion[/bold]",
                    border_style=self.colors["info"],
                    box=ROUNDED,
                    padding=(1, 1),
                )
            )
        else:
            meeting_layout["discussion"].update(
                Panel(
                    "No discussion yet",
                    title="[bold]Discussion[/bold]",
                    border_style=self.colors["info"],
                    box=ROUNDED,
                    padding=(1, 1),
                )
            )

        # Voting section
        if state.game_phase == AmongUsGamePhase.VOTING:
            voting_table = Table(
                show_header=False, box=None, show_edge=False, padding=(0, 1)
            )
            voting_table.add_column("Player", style="cyan", width=10)
            voting_table.add_column("Status", style="white")

            for pid, pstate in state.player_states.items():
                if not pstate.is_alive:
                    continue

                voted = pid in state.votes
                vote_status = (
                    f"[{self.colors['success']}]Voted[/{self.colors['success']}]"
                    if voted
                    else "Not voted"
                )

                voting_table.add_row(pid, vote_status)

            # Add skip vote option
            voting_table.add_row("[dim]Skip vote[/dim]", "")

            meeting_layout["voting"].update(
                Panel(
                    voting_table,
                    title="[bold]Voting[/bold]",
                    border_style=self.colors["warning"],
                    box=ROUNDED,
                    padding=(1, 1),
                )
            )

        # Create the main panel
        return Panel(
            meeting_layout,
            title=f"[bold]{state.game_phase.capitalize()} Phase[/bold]",
            border_style=self.colors["panel_border"],
            box=DOUBLE,
            padding=(1, 1),
        )

    def create_game_over_panel(self, state: AmongUsState) -> Panel:
        """Create a panel for the game over screen.

        Args:
            state: Current game state

        Returns:
            Rich panel for game over

        """
        if state.game_phase != AmongUsGamePhase.GAME_OVER:
            return Panel("Game not over", title="Game Status")

        # Game over layout
        game_over_layout = Layout()
        game_over_layout.split(
            Layout(name="header"),
            Layout(name="results"),
            Layout(name="players"),
        )

        # Winner header
        winner = getattr(state, "winner", None)
        winner_text = "Unknown"
        winner_color = "white"

        if winner == "crewmates":
            winner_text = "CREWMATES WIN!"
            winner_color = self.colors["crewmate"]
        elif winner == "impostors":
            winner_text = "IMPOSTORS WIN!"
            winner_color = self.colors["impostor"]

        header_text = Text(winner_text, style=f"bold {winner_color}", justify="center")

        reason_text = ""
        if winner == "crewmates":
            if state.get_task_completion_percentage() >= 100:
                reason_text = "All tasks completed successfully!"
            else:
                reason_text = "All impostors were eliminated!"
        elif winner == "impostors":
            if state.crewmate_count == 0:
                reason_text = "All crewmates were eliminated!"
            else:
                reason_text = "Impostors have outnumbered the remaining crewmates!"

        if reason_text:
            header_text.append("\n\n")
            header_text.append(reason_text, style=f"{winner_color}")

        game_over_layout["header"].update(
            Panel(
                header_text,
                border_style=winner_color,
                box=DOUBLE,
                padding=(1, 2),
            )
        )

        # Game statistics
        stats_table = Table(show_header=True, box=None, padding=(0, 1))
        stats_table.add_column("Statistic", style="cyan")
        stats_table.add_column("Value", style="white")

        stats_table.add_row("Rounds Played", str(state.round_number))
        stats_table.add_row(
            "Tasks Completed", f"{state.get_task_completion_percentage():.1f}%"
        )
        stats_table.add_row(
            "Meeting Count",
            str(
                len(state.discussion_history) // len(state.player_states)
                if state.discussion_history
                else 0
            ),
        )
        stats_table.add_row(
            "Eliminated Players",
            ", ".join(state.eliminated_players) if state.eliminated_players else "None",
        )

        game_over_layout["results"].update(
            Panel(
                stats_table,
                title="[bold]Game Statistics[/bold]",
                border_style=self.colors["info"],
                box=ROUNDED,
                padding=(1, 1),
            )
        )

        # Player results
        players_table = Table(show_header=True, box=None, padding=(0, 1))
        players_table.add_column("Player", style="cyan")
        players_table.add_column("Role", style="white")
        players_table.add_column("Status", style="white")
        players_table.add_column("Tasks", style="white")

        for pid, pstate in state.player_states.items():
            role_text = "CREWMATE" if pstate.role == PlayerRole.CREWMATE else "IMPOSTOR"
            role_color = (
                self.colors["crewmate"]
                if pstate.role == PlayerRole.CREWMATE
                else self.colors["impostor"]
            )

            status_text = "ALIVE" if pstate.is_alive else "DEAD"
            status_color = (
                self.colors["success"] if pstate.is_alive else self.colors["dead"]
            )

            # Calculate task completion for player
            completed_tasks = sum(
                1 for task in pstate.tasks if task.status == TaskStatus.COMPLETED
            )
            task_text = f"{completed_tasks}/{len(pstate.tasks)}"

            players_table.add_row(
                pid,
                f"[{role_color}]{role_text}[/{role_color}]",
                f"[{status_color}]{status_text}[/{status_color}]",
                task_text,
            )

        game_over_layout["players"].update(
            Panel(
                players_table,
                title="[bold]Player Results[/bold]",
                border_style=self.colors["panel_border"],
                box=ROUNDED,
                padding=(1, 1),
            )
        )

        # Create the main panel
        return Panel(
            game_over_layout,
            title="[bold]GAME OVER[/bold]",
            border_style="bright_magenta",
            box=DOUBLE,
            padding=(1, 1),
        )

    def create_sabotage_panel(
        self, state: AmongUsState, player_id: str | None = None
    ) -> Panel | None:
        """Create a panel showing active sabotage information if any.

        Args:
            state: Current game state
            player_id: Optional ID of the current player

        Returns:
            Rich panel for sabotage or None if no active sabotage

        """
        active_sabotage = state.get_active_sabotage()
        if not active_sabotage:
            return None

        sabotage_layout = Layout()
        sabotage_layout.split(
            Layout(name="header"),
            Layout(name="details"),
        )

        # Sabotage header
        is_critical = active_sabotage.is_critical()
        header_style = self.colors["danger"] if is_critical else self.colors["warning"]
        sabotage_title = f"{active_sabotage.type.upper()} SABOTAGE"

        if is_critical:
            sabotage_title = f"CRITICAL {sabotage_title}"

        header_text = Text(
            f"{self.symbols['sabotage']} {sabotage_title}",
            style=f"bold {header_style}",
            justify="center",
        )
        header_text.append(
            f"\nTime Remaining: {active_sabotage.timer} seconds", style=header_style
        )

        # Progress bar for timer
        max_timer = 45 if is_critical else 90  # Estimate based on sabotage type
        progress_width = 30
        remaining_progress = int((active_sabotage.timer / max_timer) * progress_width)
        timer_bar = "█" * remaining_progress + "░" * (
            progress_width - remaining_progress
        )

        header_text.append(f"\n[{header_style}]{timer_bar}[/{header_style}]")

        sabotage_layout["header"].update(
            Panel(
                header_text,
                border_style=header_style,
                box=ROUNDED,
                padding=(1, 1),
            )
        )

        # Sabotage details
        if active_sabotage.resolution_points:
            resolution_table = Table(show_header=True, box=None, padding=(0, 1))
            resolution_table.add_column("Location", style="cyan")
            resolution_table.add_column("Description", style="white")
            resolution_table.add_column("Status", style="white")

            for point in active_sabotage.resolution_points:
                status_text = "RESOLVED" if point.resolved else "NOT RESOLVED"
                status_color = (
                    self.colors["success"] if point.resolved else self.colors["danger"]
                )

                # Highlight if player is in the right location to resolve
                location_style = (
                    "bold cyan"
                    if (
                        player_id
                        and state.player_states[player_id].location == point.location
                    )
                    else "cyan"
                )

                resolution_table.add_row(
                    f"[{location_style}]{point.location.capitalize()}[/{location_style}]",
                    point.description,
                    f"[{status_color}]{status_text}[/{status_color}]",
                )

            sabotage_layout["details"].update(
                Panel(
                    resolution_table,
                    title="[bold]Resolution Points[/bold]",
                    border_style=self.colors["info"],
                    box=ROUNDED,
                    padding=(1, 1),
                )
            )
        else:
            # For door locks or other sabotages without resolution points
            effects_text = ""
            if active_sabotage.type == "doors":
                effects_text = f"The doors to {
                    active_sabotage.location.capitalize()
                } have been locked.\n\nDoors will automatically unlock after the timer expires."
            elif active_sabotage.type == "lights":
                effects_text = "Lights have been sabotaged. Crewmate vision is reduced.\n\nFix the lights panel in Electrical to restore vision."
            elif active_sabotage.type == "comms":
                effects_text = "Communications have been sabotaged. Task list is unavailable.\n\nFix the communications panel to restore functionality."

            sabotage_layout["details"].update(
                Panel(
                    Text(effects_text, justify="center"),
                    title="[bold]Effects[/bold]",
                    border_style=self.colors["info"],
                    box=ROUNDED,
                    padding=(1, 1),
                )
            )

        # Create the main panel
        return Panel(
            sabotage_layout,
            title="[bold]SABOTAGE ALERT[/bold]",
            border_style=header_style,
            box=DOUBLE,
            padding=(1, 1),
        )

    def create_legal_moves_panel(self, legal_moves: list[dict[str, Any]]) -> Panel:
        """Create a panel showing legal moves.

        Args:
            legal_moves: List of legal moves for the player

        Returns:
            Rich panel showing legal moves

        """
        if not legal_moves:
            return Panel("No legal moves available", title="Legal Moves")

        # Group moves by type
        move_groups = {}
        for move in legal_moves:
            action_type = move.get("action", "unknown")
            if action_type not in move_groups:
                move_groups[action_type] = []
            move_groups[action_type].append(move)

        # Create table
        moves_table = Table(show_header=True, box=None, padding=(0, 1))
        moves_table.add_column("Action", style="cyan")
        moves_table.add_column("Details", style="white")

        # Add rows for each action type
        for action_type, moves in sorted(move_groups.items()):
            if action_type == "move":
                locations = [move.get("location") for move in moves]
                if len(locations) > 3:  # If many locations, summarize
                    details = (
                        f"{len(locations)} locations: {', '.join(locations[:3])}..."
                    )
                else:
                    details = f"{len(locations)} locations: {', '.join(locations)}"
                moves_table.add_row("Move", details)

            elif action_type == "complete_task":
                task_count = len(moves)
                details = f"{task_count} task(s) available in current location"
                moves_table.add_row("Complete Task", details)

            elif action_type == "kill":
                targets = [move.get("target_id") for move in moves]
                details = f"{len(targets)} potential target(s): {', '.join(targets)}"
                moves_table.add_row(
                    f"[{self.colors['danger']}]Kill[/{self.colors['danger']}]", details
                )

            elif action_type == "report_body":
                moves_table.add_row(
                    f"[{self.colors['warning']}]Report Body[/{self.colors['warning']}]",
                    "Report dead body in current location",
                )

            elif action_type == "call_emergency_meeting":
                moves_table.add_row(
                    f"[{self.colors['warning']}]Emergency Meeting[/{self.colors['warning']}]",
                    "Call emergency meeting",
                )

            elif action_type == "discuss":
                moves_table.add_row("Discuss", "Contribute to meeting discussion")

            elif action_type == "vote":
                vote_targets = [move.get("vote_for") for move in moves]
                [t for t in vote_targets if t == "skip"]
                players = [t for t in vote_targets if t != "skip"]
                details = f"Vote for one of {len(players)} players or skip"
                moves_table.add_row("Vote", details)

            elif action_type == "sabotage":
                sabotage_types = {move.get("sabotage_type") for move in moves}
                details = f"Types: {', '.join(sabotage_types)}"
                moves_table.add_row(
                    f"[{self.colors['danger']}]Sabotage[/{self.colors['danger']}]",
                    details,
                )

            elif action_type == "resolve_sabotage":
                moves_table.add_row(
                    f"[{self.colors['success']}]Resolve Sabotage[/{self.colors['success']}]",
                    "Fix sabotage in current location",
                )

            elif action_type == "vent":
                vent_ids = [move.get("vent_id") for move in moves]
                details = f"{len(vent_ids)} vent(s) available"
                moves_table.add_row("Use Vent", details)

            elif action_type == "exit_vent":
                moves_table.add_row("Exit Vent", "Exit current vent")

            else:
                moves_table.add_row(action_type.capitalize(), f"{len(moves)} option(s)")

        # Create panel
        return Panel(
            moves_table,
            title="[bold]Available Actions[/bold]",
            border_style=self.colors["panel_border"],
            box=ROUNDED,
            padding=(1, 1),
        )

    def create_layout(
        self,
        state: AmongUsState,
        player_id: str | None = None,
        legal_moves: list[dict[str, Any]] | None = None,
    ) -> Layout:
        """Create the complete layout for the game UI.

        Args:
            state: Current game state
            player_id: Optional ID of the current player's perspective
            legal_moves: Optional list of legal moves for the player

        Returns:
            Complete rich layout

        """
        # Create main layout
        layout = Layout()

        # Split into header and body
        layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
        )

        # Header with game title and phase
        phase_info = f"PHASE: {state.game_phase.upper()} - ROUND: {state.round_number}"
        header_text = Text(
            "AMONG US", style=f"bold {self.colors['header']}", justify="center"
        )
        header_text.append(f"\n{phase_info}", style=self.colors["info"])

        layout["header"].update(
            Panel(header_text, border_style=self.colors["panel_border"], box=ROUNDED)
        )

        # Main section layout depends on game phase
        if state.game_phase == AmongUsGamePhase.GAME_OVER:
            # Game over screen
            layout["main"].update(self.create_game_over_panel(state))

        elif state.game_phase in [AmongUsGamePhase.MEETING, AmongUsGamePhase.VOTING]:
            # Meeting phase layout
            layout["main"].split_row(
                Layout(name="meeting", ratio=2),
                Layout(name="info", ratio=1),
            )

            # Meeting panel
            layout["main"]["meeting"].update(self.create_meeting_panel(state))

            # Info column
            layout["main"]["info"].split(
                Layout(name="player_info"),
                Layout(name="game_info"),
            )

            if player_id and player_id in state.player_states:
                layout["main"]["info"]["player_info"].update(
                    self.create_player_info_panel(state, player_id)
                )

            layout["main"]["info"]["game_info"].update(
                self.create_game_info_panel(state)
            )

        else:
            # Normal gameplay layout
            layout["main"].split_row(
                Layout(name="left_column", ratio=2),
                Layout(name="right_column", ratio=1),
            )

            # Left column - map and active sabotage
            layout["main"]["left_column"].split(
                Layout(name="map", ratio=2),
                Layout(
                    name="sabotage",
                    size=10,
                    visible=state.get_active_sabotage() is not None,
                ),
                Layout(name="legal_moves", size=10, visible=legal_moves is not None),
            )

            # Map
            layout["main"]["left_column"]["map"].update(
                self.create_map_visualization(state, player_id)
            )

            # Sabotage alert if active
            sabotage_panel = self.create_sabotage_panel(state, player_id)
            if sabotage_panel:
                layout["main"]["left_column"]["sabotage"].update(sabotage_panel)
                layout["main"]["left_column"]["sabotage"].visible = True
            else:
                layout["main"]["left_column"]["sabotage"].visible = False

            # Legal moves if provided
            if legal_moves:
                layout["main"]["left_column"]["legal_moves"].update(
                    self.create_legal_moves_panel(legal_moves)
                )
                layout["main"]["left_column"]["legal_moves"].visible = True
            else:
                layout["main"]["left_column"]["legal_moves"].visible = False

            # Right column - player info, game info, other players
            layout["main"]["right_column"].split(
                Layout(name="player_info"),
                Layout(name="game_info"),
                Layout(name="other_players"),
            )

            # Player info if specified
            if player_id and player_id in state.player_states:
                layout["main"]["right_column"]["player_info"].update(
                    self.create_player_info_panel(state, player_id)
                )
            else:
                # If no player specified, show general game info
                layout["main"]["right_column"]["player_info"].update(
                    Panel(
                        "No player perspective selected",
                        title="[bold]Player Info[/bold]",
                        border_style=self.colors["panel_border"],
                        box=ROUNDED,
                    )
                )

            # Game info
            layout["main"]["right_column"]["game_info"].update(
                self.create_game_info_panel(state)
            )

            # Other players info
            if player_id and player_id in state.player_states:
                layout["main"]["right_column"]["other_players"].update(
                    self.create_other_players_panel(state, player_id)
                )
            else:
                # If no player specified, hide this section
                layout["main"]["right_column"]["other_players"].visible = False

        return layout

    def display_state(
        self,
        state_data: Any,
        player_id: str | None = None,
        legal_moves: list[dict[str, Any]] | None = None,
    ) -> bool:
        """Display the game state using enhanced rich UI.

        Args:
            state_data: State data in various formats
            player_id: Optional ID of the player whose perspective to show
            legal_moves: Optional list of legal moves for the player

        Returns:
            True if display was successful, False otherwise

        """
        try:
            game_state = self.extract_game_state(state_data)
            if game_state is None:
                logger.error("Could not extract valid game state for display")
                return False

            layout = self.create_layout(game_state, player_id, legal_moves)
            self.console.print(layout)
            return True

        except Exception as e:
            logger.error(f"Error displaying state: {e}", exc_info=True)
            return False

    def show_thinking(self, player_id: str, message: str = "Thinking...") -> None:
        """Display a thinking animation for the player.

        Args:
            player_id: ID of the player who is thinking
            message: Message to display during thinking

        Returns:
            None

        """
        with Progress(
            SpinnerColumn(),
            TextColumn(f"[cyan]{player_id}[/cyan] {message}"),
            console=self.console,
            transient=True,
        ) as progress:
            progress.add_task("thinking", total=None)
            time.sleep(1.0)  # Show thinking animation for 1 second

    def display_welcome(self) -> None:
        """Display welcome message and game introduction.

        Returns:
            None

        """
        welcome_text = Text(
            """
🚀 Welcome to Among Us! 🚀

This is a social deduction game where:
• Crewmates try to complete tasks and identify the impostors
• Impostors try to sabotage the ship and eliminate crewmates
• Crewmates win by completing all tasks or eliminating all impostors
• Impostors win by eliminating enough crewmates to outnumber them

The game is played across various rooms on a spaceship where players
can move around, complete tasks, report bodies, and call emergency meetings.

Impostors have special abilities like killing crewmates, venting between
rooms, and sabotaging ship systems.

The game will be played by AI agents with enhanced visualization!
            """.strip(),
            style="cyan",
        )

        self.console.print(
            Panel(
                welcome_text,
                title="[bold yellow]🎮 AMONG US GAME 🎮[/bold yellow]",
                border_style="bright_green",
                box=DOUBLE,
                padding=(1, 2),
            )
        )

    def display_final_results(self, final_state: Any) -> None:
        """Display enhanced final game results.

        Args:
            final_state: Final game state

        Returns:
            None

        """
        game_state = self.extract_game_state(final_state)
        if game_state is None:
            self.console.print("[red]Could not extract final game state[/red]")
            return

        # Display the game over panel
        self.console.print(self.create_game_over_panel(game_state))

    def animate_move(
        self,
        move: dict[str, Any],
        state_before: AmongUsState,
        state_after: AmongUsState,
        player_id: str,
        delay: float = 0.5,
    ) -> None:
        """Animate a move being made.

        Args:
            move: Move details
            state_before: State before the move
            state_after: State after the move
            player_id: ID of the player making the move
            delay: Delay for animation

        Returns:
            None

        """
        action_type = move.get("action", "unknown")

        # Show thinking animation
        self.show_thinking(player_id, f"Performing {action_type}...")

        # Create a formatted description of the move
        move_text = self._format_move_description(move, player_id, state_before)

        # Show the move panel
        self.console.print(
            Panel(
                Text(move_text, justify="center"),
                title=f"[bold]{player_id}'s Move[/bold]",
                border_style=self.colors["info"],
                box=ROUNDED,
                padding=(1, 2),
            )
        )

        # Show the final state
        self.display_state(state_after, player_id)

    def _format_move_description(
        self, move: dict[str, Any], player_id: str, state: AmongUsState
    ) -> str:
        """Format a move description for display.

        Args:
            move: Move details
            player_id: ID of the player making the move
            state: Current game state

        Returns:
            Formatted move description

        """
        action_type = move.get("action", "unknown")
        player_role = (
            "IMPOSTOR" if state.player_states[player_id].is_impostor() else "CREWMATE"
        )
        role_color = (
            self.colors["impostor"]
            if state.player_states[player_id].is_impostor()
            else self.colors["crewmate"]
        )

        description = f"[{role_color}]{player_id} ({player_role})[/{role_color}] "

        if action_type == "move":
            location = move.get("location", "unknown")
            description += f"moved to [{self.colors.get(location, 'white')}]{
                location.capitalize()
            }[/{self.colors.get(location, 'white')}]"

        elif action_type == "complete_task":
            task_id = move.get("task_id", "unknown")
            task = next(
                (t for t in state.player_states[player_id].tasks if t.id == task_id),
                None,
            )
            if task:
                description += f"completed task: [{self.colors['task']}]{
                    task.description
                }[/{self.colors['task']}] in {task.location.capitalize()}"
            else:
                description += f"completed task ID: {task_id}"

        elif action_type == "kill":
            target_id = move.get("target_id", "unknown")
            description += (
                f"[{self.colors['danger']}]killed {target_id}[/{self.colors['danger']}]"
            )

        elif action_type == "report_body":
            description += f"[{self.colors['warning']}]reported a dead body[/{self.colors['warning']}]"

        elif action_type == "call_emergency_meeting":
            description += f"[{self.colors['warning']}]called an emergency meeting[/{self.colors['warning']}]"

        elif action_type == "discuss":
            message = move.get("message", "")
            description += f'said: [italic]"{message}"[/italic]'

        elif action_type == "vote":
            target = move.get("vote_for", "unknown")
            if target == "skip":
                description += (
                    f"voted to [{self.colors['info']}]skip[/{self.colors['info']}]"
                )
            else:
                description += (
                    f"voted for [{self.colors['info']}]{target}[/{self.colors['info']}]"
                )

        elif action_type == "sabotage":
            sabotage_type = move.get("sabotage_type", "unknown")
            location = move.get("location", sabotage_type)
            description += f"[{self.colors['danger']}]sabotaged {sabotage_type.upper()}[/{self.colors['danger']}]"
            if sabotage_type == "doors":
                description += f" in {location.capitalize()}"

        elif action_type == "resolve_sabotage":
            sabotage_id = move.get("sabotage_id", "unknown")
            resolution_point_id = move.get("resolution_point_id", "unknown")
            description += f"[{self.colors['success']}]resolved {sabotage_id.upper()} sabotage[/{self.colors['success']}] ({resolution_point_id})"

        elif action_type == "vent":
            vent_id = move.get("vent_id", "unknown")
            description += f"used vent: {vent_id}"

        elif action_type == "exit_vent":
            description += "exited vent"

        else:
            description += f"performed unknown action: {action_type}"

        return description

    def run_among_us_game(self, agent, delay: float = 1.0) -> AmongUsState:
        """Run a complete Among Us game with UI visualization.

        Args:
            agent: The game agent that manages the game logic
            delay: Delay between game states

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
        initial_state = agent.initialize()
        self.display_state(initial_state)
        time.sleep(delay)

        # Run the game with state tracking
        final_state = agent.run_game_with_ui(delay=delay)

        # Show final results
        self.display_final_results(final_state)

        return final_state
