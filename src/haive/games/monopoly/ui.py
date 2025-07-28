"""Rich UI for displaying a live Monopoly game with proper error handling.

This module provides a beautiful terminal interface for watching
Monopoly games unfold in real-time using Rich, with fixes for the
validation error.
"""

import time

from rich.align import Align
from rich.box import SIMPLE
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from haive.games.monopoly.config import MonopolyGameAgentConfig
from haive.games.monopoly.main_agent import MonopolyAgent
from haive.games.monopoly.state import MonopolyState


class MonopolyRichUI:
    """Beautiful Rich UI for displaying a live Monopoly game."""

    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        self.state: MonopolyState | None = None
        self._setup_layout()

    def _setup_layout(self):
        """Initialize the layout structure."""
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=4),
        )

        self.layout["body"].split_row(
            Layout(name="board", ratio=2),
            Layout(name="right_panel", ratio=1),
        )

        self.layout["right_panel"].split(
            Layout(name="current_player", size=8),
            Layout(name="players", ratio=1),
            Layout(name="recent_events", ratio=1),
        )

    def render_header(self) -> Panel:
        """Render the game header."""
        if not self.state:
            header_text = Text(
                "🏠 Monopoly Game - Initializing...",
                justify="center",
                style="bold white on blue",
            )
        else:
            # state = MonopolyState.model_validate(self.state)
            if hasattr(self.state, "model_dump"):
                self.state = self.state.model_dump()
            status_color = (
                "green" if self.state["game_status"] == "playing" else "yellow"
            )
            header_text = Text(
                f"🏠 Monopoly Game - Turn {self.state["turn_numbef"]} - {self.state["game_status"].title()}",
                justify="center",
                style=f"bold white on {status_color}",
            )

        return Panel(header_text, border_style="blue")

    def render_footer(self) -> Panel:
        """Render the footer with controls and game info."""
        footer_text = Text()  # Initialize footer_text at the beginning

        if not self.state:
            footer_text.append("Waiting for game to start...", style="italic")
        else:
            if isinstance(self.state, dict):
                state = MonopolyState.model_validate(self.state)
            else:
                state = self.state

            footer_text.append(f"Round: {state.round_number} ", style="bold")
            footer_text.append(
                f"• Active Players: {len(state.active_players)} ", style="green"
            )

            if state.bankrupt_players:
                footer_text.append(
                    f"• Bankrupt: {len(state.bankrupt_players)} ", style="red"
                )

            if state.winner:
                footer_text.append(f"• WINNER: {state.winner} ", style="bold gold1")

        # Add controls
        controls = Text("\n")
        control_items = [("Q", "Quit"), ("P", "Pause"), ("S", "Save"), ("R", "Restart")]
        for key, desc in control_items:
            controls.append(f" {key} ", style="black on white")
            controls.append(f" {desc}  ", style="white")

        footer_text.append(controls)
        return Panel(Align.center(footer_text), border_style="blue")

    def render_board(self) -> Panel:
        """Render a simplified board view."""
        if not self.state:
            return Panel(
                "Waiting for game state...", title="Board", border_style="magenta"
            )

        # Create a simple grid representation of the board
        board_text = Text()

        # Top row (positions 20-30)
        board_text.append("FREE  ", style="yellow")
        for pos in range(21, 30):
            if isinstance(self.state, dict):
                state = MonopolyState.model_validate(self.state)
                prop = state.get_property_by_position(pos)
            else:
                prop = self.state.get_property_by_position(pos)
                if prop and prop.owner:
                    style = self._get_player_color(prop.owner)
                    board_text.append(f"{prop.name[:5]:<5} ", style=style)
                else:
                    board_text.append("-----  ", style="dim")
        board_text.append("JAIL\n", style="red")

        # Middle sections (simplified)
        for _row in range(3):
            board_text.append("│    " + " " * 60 + "    │\n", style="dim")

        # Bottom row (positions 10-0)
        board_text.append("VISIT ", style="cyan")
        for pos in range(9, 0, -1):
            if isinstance(self.state, dict):
                state = MonopolyState.model_validate(self.state)
                prop = state.get_property_by_position(pos)
            else:
                prop = self.state.get_property_by_position(pos)
            if prop and prop.owner:
                style = self._get_player_color(prop.owner)
                board_text.append(f"{prop.name[:5]:<5} ", style=style)
            else:
                board_text.append("-----  ", style="dim")
        board_text.append("  GO\n", style="green bold")

        # Show player positions
        board_text.append("\nPlayer Positions:\n", style="bold underline")
        if isinstance(self.state, dict):
            state = MonopolyState.model_validate(self.state)
            players = state.players
        else:
            players = self.state.players
        for player in players:
            if not player.bankrupt:
                pos_info = self._get_position_name(player.position)
                style = self._get_player_color(player.name)
                board_text.append(f"• {player.name}: {pos_info}\n", style=style)

        return Panel(board_text, title="Board", border_style="magenta")

    def render_current_player(self) -> Panel:
        """Render current player information."""
        if not self.state:
            return Panel("No current player", title="Current Turn", border_style="cyan")

        if isinstance(self.state, dict):
            state = MonopolyState.model_validate(self.state)
            current = state.current_player
        else:
            current = self.state.current_player
        style = self._get_player_color(current.name)

        player_text = Text()
        player_text.append(f"{current.name}\n", style=f"bold {style}")
        player_text.append(f"💰 Money: ${current.money:,}\n")
        player_text.append(
            f"📍 Position: {self._get_position_name(current.position)}\n"
        )
        player_text.append(f"🏠 Properties: {len(current.properties)}\n")

        if current.in_jail:
            player_text.append(
                f"🔒 In Jail (Turn {current.jail_turns}/3)\n", style="red"
            )

        if current.jail_cards > 0:
            player_text.append(f"🎫 Jail Cards: {current.jail_cards}\n", style="yellow")
        if isinstance(self.state, dict):
            state = MonopolyState.model_validate(self.state)
            last_roll = state.last_roll
        else:
            last_roll = self.state.last_roll
        if last_roll:
            roll = last_roll
            roll_style = "bold green" if roll.is_doubles else "white"
            player_text.append(
                f"🎲 Last Roll: {roll.die1}+{roll.die2}={roll.total}", style=roll_style
            )
            if roll.is_doubles:
                player_text.append(" (DOUBLES!)", style="bold yellow")

        return Panel(player_text, title="Current Turn", border_style="cyan")

    def render_players(self) -> Panel:
        """Render all players summary."""
        if not self.state:
            return Panel("No players", title="Players", border_style="green")

        table = Table(box=SIMPLE, show_header=True, header_style="bold")
        table.add_column("Player", style="bold")
        table.add_column("Money", justify="right")
        table.add_column("Props", justify="center")
        table.add_column("Status")

        if isinstance(self.state, dict):
            state = MonopolyState.model_validate(self.state)
            players = state.players
        else:
            players = self.state.players
        for player in players:
            if player.bankrupt:
                table.add_row(player.name, "💥", "0", "Bankrupt", style="red dim")
            else:
                status = "🔒 Jail" if player.in_jail else "Active"
                style = self._get_player_color(player.name)
                if isinstance(self.state, dict):
                    state = MonopolyState.model_validate(self.state)
                    current_player = state.current_player
                else:
                    current_player = self.state.current_player
                if player.name == current_player.name:
                    style += " bold"

                table.add_row(
                    player.name,
                    f"${player.money:,}",
                    str(len(player.properties)),
                    status,
                    style=style,
                )

        return Panel(table, title="Players", border_style="green")

    def render_recent_events(self) -> Panel:
        """Render recent game events."""
        if isinstance(self.state, dict):
            state = MonopolyState.model_validate(self.state)
            recent_events = state.get_recent_events(8)
        else:
            recent_events = self.state.get_recent_events(8)
        if not self.state or not recent_events:
            return Panel("No events yet", title="Recent Events", border_style="yellow")

        events_text = Text()

        for event in recent_events:
            # Style based on event type
            if event.event_type in ["property_purchase", "rent_payment"]:
                style = "green"
            elif event.event_type in ["bankruptcy", "go_to_jail"]:
                style = "red"
            elif event.event_type == "dice_roll":
                style = "cyan"
            else:
                style = "white"

            # Money indicator
            money_indicator = ""
            if event.money_change > 0:
                money_indicator = f" (+${event.money_change})"
            elif event.money_change < 0:
                money_indicator = f" (${event.money_change})"

            events_text.append(
                f"• {event.player}: {event.description}{money_indicator}\n", style=style
            )

        return Panel(events_text, title="Recent Events", border_style="yellow")

    def _get_player_color(self, player_name: str) -> str:
        """Get color for a player based on their name."""
        colors = {
            0: "red",
            1: "blue",
            2: "green",
            3: "magenta",
            4: "cyan",
            5: "yellow",
            6: "bright_red",
            7: "bright_blue",
        }

        if not self.state:
            return "white"

        if isinstance(self.state, dict):
            state = MonopolyState.model_validate(self.state)
            players = state.players
        else:
            players = self.state.players
        for i, player in enumerate(players):
            if player.name == player_name:
                return colors.get(i, "white")

        return "white"

    def _get_position_name(self, position: int) -> str:
        """Get the name of a board position."""
        from haive.games.monopoly.utils import get_property_at_position

        pos_data = get_property_at_position(position)
        if pos_data:
            return f"{pos_data['name']} ({position})"
        return f"Position {position}"

    def run(self, agent: MonopolyAgent, delay: float = 2.0):
        """Run the live UI with the Monopoly agent.

        Args:
            agent: The Monopoly agent to run
            delay: Delay between updates for readability
        """
        # CRITICAL FIX: Ensure initial state has messages field
        initial_state = agent.initial_state

        # Show initial state
        self.state = agent.initial_state
        self._update_layout()

        try:
            with Live(self.layout, refresh_per_second=2) as live:
                last_update_time = time.time()

                for step in agent.app.stream(
                    initial_state, config=agent.runnable_config, stream_mode="values"
                ):
                    # Update state
                    self.state = step

                    # Only update UI periodically to prevent flickering
                    current_time = time.time()
                    if current_time - last_update_time >= delay:
                        self._update_layout()
                        live.refresh()
                        last_update_time = current_time

                    # Check for game end
                    if step.get("error_message"):
                        self.console.print(
                            f"\n[bold red]Error: {step['error_message']}[/bold red]"
                        )
                        time.sleep(1)
                        break

                    if step.get("game_status") == "finished":
                        self._update_layout()
                        live.refresh()
                        time.sleep(3)
                        break

        except Exception as e:
            self.console.print(f"\n[bold red]Error during game: {e!s}[/bold red]")
            import traceback

            self.console.print(traceback.format_exc())

        self.console.print("\n[bold magenta]🏁 Game Over![/bold magenta]")

        # Save game history
        try:
            agent.save_game_history()
        except Exception as e:
            self.console.print(f"Could not save game history: {e}")

    def _update_layout(self):
        """Update all layout components with current state."""
        self.layout["header"].update(self.render_header())
        self.layout["footer"].update(self.render_footer())

        self.layout["body"]["board"].update(self.render_board())
        self.layout["body"]["right_panel"]["current_player"].update(
            self.render_current_player()
        )
        self.layout["body"]["right_panel"]["players"].update(self.render_players())
        self.layout["body"]["right_panel"]["recent_events"].update(
            self.render_recent_events()
        )


def main():
    """Run a Monopoly game with the Rich UI."""
    # Create game configuration
    config = MonopolyGameAgentConfig(
        player_names=["Alice", "Bob", "Charlie", "Diana"],
        max_turns=500,
        enable_trading=False,  # Disable for simpler initial version
        enable_building=False,
    )

    # Create agent
    agent = MonopolyAgent(config)

    # Create and run UI
    ui = MonopolyRichUI()
    ui.run(agent, delay=1.5)


if __name__ == "__main__":
    main()
