"""Texas Hold'em Rich UI for live game display.

This module provides a beautiful Rich-based terminal UI for displaying
Texas Hold'em games in real-time, showing:
    - Player positions and chip stacks
    - Community cards and pot
    - Current action and betting
    - Game phase and status
"""

import logging
import time
from typing import Any, Dict, Optional

from rich.align import Align
from rich.box import ROUNDED, SIMPLE
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from haive.games.hold_em.game_agent import HoldemGameAgent
from haive.games.hold_em.state import GamePhase, HoldemState, PlayerState, PlayerStatus

logger = logging.getLogger(__name__)


class HoldemRichUI:
    """Beautiful Rich UI for displaying a live Texas Hold'em game."""

    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        self.state: Optional[Dict[str, Any]] = None
        self.last_action: Optional[Dict[str, Any]] = None
        self._setup_layout()

    def _setup_layout(self):
        """Initialize the layout structure."""
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="body", ratio=1),
            Layout(name="footer", size=4),
        )

        self.layout["body"].split_row(
            Layout(name="left_panel", ratio=1),
            Layout(name="center", ratio=2),
            Layout(name="right_panel", ratio=1),
        )

        self.layout["body"]["left_panel"].split(
            Layout(name="player_info", size=12),
            Layout(name="game_stats"),
        )

        self.layout["body"]["center"].split(
            Layout(name="table", ratio=2),
            Layout(name="community_cards", size=6),
            Layout(name="pot_info", size=4),
        )

        self.layout["body"]["right_panel"].split(
            Layout(name="action_log", size=15),
            Layout(name="hand_history"),
        )

    def render_header(self) -> Panel:
        """Render the header with game title and phase."""
        if not self.state:
            header_text = Text(
                "🃏 Texas Hold'em Arena", justify="center", style="bold white on blue"
            )
            return Panel(header_text, border_style="blue")
        if isinstance(self.state, dict):
            self.state = HoldemState.model_validate(self.state)
        game_state = self.state
        phase_text = game_state.current_phase.value.upper().replace("_", " ")
        hand_num = game_state.hand_number

        header_text = Text()
        header_text.append("🃏 Texas Hold'em Arena  ", style="bold white")
        header_text.append(f"Hand #{hand_num}  ", style="bold yellow")
        header_text.append(f"Phase: {phase_text}", style="bold cyan")

        return Panel(Align.center(header_text), border_style="blue", box=ROUNDED)

    def render_footer(self) -> Panel:
        """Render the footer with controls and current action."""
        controls = [
            ("Q", "Quit"),
            ("P", "Pause"),
            ("R", "Reset"),
            ("S", "Speed"),
        ]

        footer_content = Text()
        for key, desc in controls:
            footer_content.append(f" {key} ", style="black on white")
            footer_content.append(f" {desc}  ", style="white")

        if self.state and self.last_action:
            footer_content.append("\n")
            action_text = self._format_last_action()
            footer_content.append(action_text)

        return Panel(footer_content, title="Controls", border_style="blue", box=SIMPLE)

    def render_table(self) -> Panel:
        """Render the poker table with player positions."""
        if not self.state:
            return Panel(
                "Waiting for game...", title="Poker Table", border_style="green"
            )

        game_state = self.state

        # Create a visual representation of the table
        table_text = Text()

        # Table layout (6-max style)
        positions = [
            ("     [2]     ", 2),  # Top
            ("[1]       [3]", 1, 3),  # Middle sides
            ("     [0]     ", 0),  # Bottom (dealer view)
        ]

        for line_data in positions:
            if len(line_data) == 2:  # Single position
                line_template, pos = line_data
                player = self._get_player_at_position(game_state, pos)
                if player:
                    player_repr = self._format_player_short(player, game_state)
                    line = line_template.replace(f"[{pos}]", player_repr)
                else:
                    line = line_template.replace(f"[{pos}]", "     ")
                table_text.append(line + "\n")

            else:  # Multiple positions
                line_template = line_data[0]
                positions_in_line = line_data[1:]
                line = line_template

                for pos in positions_in_line:
                    player = self._get_player_at_position(game_state, pos)
                    if player:
                        player_repr = self._format_player_short(player, game_state)
                        line = line.replace(f"[{pos}]", player_repr)
                    else:
                        line = line.replace(f"[{pos}]", "     ")
                table_text.append(line + "\n")

        # Add dealer button
        dealer_pos = game_state.dealer_position
        table_text.append(f"\n🔘 Dealer: Position {dealer_pos}")

        return Panel(table_text, title="Poker Table", border_style="green", box=ROUNDED)

    def render_community_cards(self) -> Panel:
        """Render community cards and board."""
        if not self.state:
            return Panel(
                "No cards dealt", title="Community Cards", border_style="yellow"
            )

        game_state = self.state

        if not game_state.community_cards:
            return Panel(
                "No community cards yet", title="Community Cards", border_style="yellow"
            )

        # Format cards with suits
        cards_text = Text()
        cards_text.append("🃏 ", style="bold")

        for i, card in enumerate(game_state.community_cards):
            if i > 0:
                cards_text.append("  ")

            # Color cards by suit
            suit = card[1] if len(card) > 1 else ""
            if suit in ["h", "d"]:  # Hearts, Diamonds
                style = "bold red"
            else:  # Clubs, Spades
                style = "bold white"

            cards_text.append(f"[{card[0]}{self._suit_symbol(suit)}]", style=style)

        # Add phase information
        phase_info = Text()
        if game_state.current_phase == GamePhase.FLOP:
            phase_info.append("\nFlop (3 cards)", style="dim")
        elif game_state.current_phase == GamePhase.TURN:
            phase_info.append("\nTurn (4th card)", style="dim")
        elif game_state.current_phase == GamePhase.RIVER:
            phase_info.append("\nRiver (5th card)", style="dim")

        full_text = Text()
        full_text.append(cards_text)
        full_text.append(phase_info)

        return Panel(
            full_text, title="Community Cards", border_style="yellow", box=ROUNDED
        )

    def render_pot_info(self) -> Panel:
        """Render pot size and betting information."""
        if not self.state:
            return Panel("No pot info", title="Pot", border_style="red")

        game_state = self.state

        pot_text = Text()
        pot_text.append("💰 Main Pot: ", style="bold")
        pot_text.append(f"{game_state.total_pot:,} chips\n", style="bold green")

        if game_state.current_bet > 0:
            pot_text.append("Current Bet: ", style="bold")
            pot_text.append(f"{game_state.current_bet} chips\n", style="bold yellow")

        if game_state.side_pots:
            pot_text.append(f"Side Pots: {len(game_state.side_pots)}\n", style="dim")

        # Add current player to act
        if game_state.current_player:
            pot_text.append("\n🎯 Action on: ", style="bold")
            pot_text.append(f"{game_state.current_player.name}", style="bold cyan")

        return Panel(pot_text, title="Pot Information", border_style="red", box=SIMPLE)

    def render_player_info(self) -> Panel:
        """Render detailed player information."""
        if not self.state:
            return Panel("No players", title="Players", border_style="cyan")

        game_state = self.state

        table = Table(box=SIMPLE, style="dim", show_header=True)
        table.add_column("Player", style="bold", width=8)
        table.add_column("Chips", justify="right", width=8)
        table.add_column("Bet", justify="right", width=6)
        table.add_column("Status", width=8)

        for player in game_state.players:
            # Player name with position indicator
            name = player.name
            if player.is_dealer:
                name += " 🔘"
            elif player.is_small_blind:
                name += " SB"
            elif player.is_big_blind:
                name += " BB"

            # Chip count with color coding
            chips_str = f"{player.chips:,}"
            if player.chips == 0:
                chips_style = "red"
            elif player.chips < game_state.big_blind * 10:
                chips_style = "yellow"
            else:
                chips_style = "green"

            # Current bet
            bet_str = f"{player.current_bet}" if player.current_bet > 0 else "-"

            # Status with color
            status_map = {
                PlayerStatus.ACTIVE: ("Active", "green"),
                PlayerStatus.FOLDED: ("Folded", "red"),
                PlayerStatus.ALL_IN: ("All-in", "yellow"),
                PlayerStatus.OUT: ("Out", "dim red"),
            }
            status_text, status_style = status_map.get(
                player.status, ("Unknown", "white")
            )

            table.add_row(
                name,
                Text(chips_str, style=chips_style),
                bet_str,
                Text(status_text, style=status_style),
            )

        return Panel(table, title="Player Info", border_style="cyan")

    def render_action_log(self) -> Panel:
        """Render recent actions and decisions."""
        if not self.state:
            return Panel("No actions yet", title="Action Log", border_style="magenta")

        game_state = self.state

        if not game_state.actions_this_round:
            return Panel(
                "No actions this round", title="Action Log", border_style="magenta"
            )

        log_text = Text()
        recent_actions = game_state.actions_this_round[-8:]  # Show last 8 actions

        for action in recent_actions:
            player_name = self._get_player_name_by_id(
                game_state, action.get("player_id", "")
            )
            action_type = action.get("action", "unknown")
            amount = action.get("amount", 0)

            # Format action with color
            action_line = Text()
            action_line.append(f"{player_name}: ", style="bold")

            if action_type == "fold":
                action_line.append("folds", style="red")
            elif action_type == "check":
                action_line.append("checks", style="green")
            elif action_type == "call":
                action_line.append(f"calls {amount}", style="blue")
            elif action_type in ["bet", "raise"]:
                action_line.append(f"{action_type}s to {amount}", style="yellow")
            elif action_type == "all_in":
                action_line.append(f"ALL-IN {amount}", style="bold red")
            else:
                action_line.append(f"{action_type} {amount}", style="white")

            log_text.append(action_line)
            log_text.append("\n")

        return Panel(log_text, title="Action Log", border_style="magenta", box=SIMPLE)

    def render_hand_history(self) -> Panel:
        """Render hand history summary."""
        if not self.state:
            return Panel("No history", title="Hand History", border_style="blue")

        game_state = self.state

        if not game_state.hand_history:
            return Panel(
                "No completed hands", title="Hand History", border_style="blue"
            )

        history_text = Text()
        recent_hands = game_state.hand_history[-5:]  # Show last 5 hands

        for hand in recent_hands:
            hand_num = hand.get("hand_number", "?")
            winner = self._get_player_name_by_id(game_state, hand.get("winner", ""))
            pot_size = hand.get("pot_size", 0)

            history_text.append(f"Hand #{hand_num}: ", style="bold")
            history_text.append(f"{winner} wins {pot_size:,}\n", style="green")

        return Panel(
            history_text, title="Recent Hands", border_style="blue", box=SIMPLE
        )

    def render_game_stats(self) -> Panel:
        """Render game statistics."""
        if not self.state:
            return Panel("No stats", title="Game Stats", border_style="white")

        game_state = self.state

        stats_text = Text()
        stats_text.append(f"Hand: {game_state.hand_number}\n", style="bold")
        stats_text.append(f"Players: {len(game_state.players)}\n")
        stats_text.append(f"Active: {len(game_state.active_players)}\n")
        stats_text.append(f"In Hand: {len(game_state.players_in_hand)}\n")

        # Blinds info
        stats_text.append(
            f"\nBlinds: {game_state.small_blind}/{game_state.big_blind}\n",
            style="yellow",
        )

        # Total chips in play
        total_chips = sum(p.chips + p.total_bet for p in game_state.players)
        stats_text.append(f"Total Chips: {total_chips:,}\n", style="dim")

        return Panel(stats_text, title="Game Stats", border_style="white", box=SIMPLE)

    def run(self, agent: HoldemGameAgent, delay: float = 2.0):
        """Run the live UI with the Hold'em agent.

        Args:
            agent: The HoldemGameAgent instance
            delay: Delay between updates for readability
        """
        # Create initial state
        initial_state = self._create_initial_state(agent)

        # Show initial state
        self.state = initial_state
        self._update_layout()

        try:
            with Live(self.layout, refresh_per_second=2) as live:
                last_update_time = time.time()

                for step in agent.app.stream(
                    initial_state,
                    config=agent.runnable_config,
                    debug=True,
                    stream_mode="values",
                ):
                    # Update state
                    self.state = step
                    self.last_action = step.get("last_action")

                    # Throttle UI updates
                    current_time = time.time()
                    if current_time - last_update_time >= delay:
                        self._update_layout()
                        live.refresh()
                        last_update_time = current_time

                    # Check for game end
                    if step.get("game_over") or step.get("error_message"):
                        self._update_layout()
                        live.refresh()
                        time.sleep(2)
                        break

        except Exception as e:
            self.console.print(f"\n[bold red]Error during game: {str(e)}[/bold red]")
            import traceback

            self.console.print(traceback.format_exc())

        self.console.print("\n[bold magenta]🏁 Game Over![/bold magenta]")
        if hasattr(agent, "save_state_history"):
            agent.save_state_history()

    def _update_layout(self):
        """Update all layout components with current state."""
        self.layout["header"].update(self.render_header())
        self.layout["footer"].update(self.render_footer())

        self.layout["body"]["left_panel"]["player_info"].update(
            self.render_player_info()
        )
        self.layout["body"]["left_panel"]["game_stats"].update(self.render_game_stats())

        self.layout["body"]["center"]["table"].update(self.render_table())
        self.layout["body"]["center"]["community_cards"].update(
            self.render_community_cards()
        )
        self.layout["body"]["center"]["pot_info"].update(self.render_pot_info())

        self.layout["body"]["right_panel"]["action_log"].update(
            self.render_action_log()
        )
        self.layout["body"]["right_panel"]["hand_history"].update(
            self.render_hand_history()
        )

    def _create_initial_state(self, agent: HoldemGameAgent) -> HoldemState:
        """Create initial game state from agent config."""
        from haive.games.hold_em.utils import create_standard_deck, shuffle_deck

        players = []
        for i, player_config in enumerate(agent.config.player_configs):
            # FIXED: Ensure player_id matches the expected format and is not empty
            player_id = f"player_{i}"

            # Validate the player_id is not empty
            if not player_id or player_id.strip() == "":
                raise ValueError(
                    f"Empty player_id for player {i} ({player_config.player_name})"
                )

            player = PlayerState(
                player_id=player_id,  # Ensure this is set correctly
                name=player_config.player_name,
                chips=agent.config.starting_chips,
                position=i,
                is_dealer=(i == 0),
                is_small_blind=(
                    (i == 1) if len(agent.config.player_configs) > 2 else (i == 0)
                ),
                is_big_blind=(
                    (i == 2) if len(agent.config.player_configs) > 2 else (i == 1)
                ),
            )

            # Double-check the player_id was set correctly
            if not player.player_id or player.player_id.strip() == "":
                raise ValueError(
                    f"Failed to set player_id for {player_config.player_name}"
                )

            players.append(player)
            logger.info(
                f"✅ Created player: {player.name} with ID: '{player.player_id}'"
            )

        initial_state = HoldemState(
            game_id="ui_test_game",
            players=players,
            max_players=agent.config.max_players,
            small_blind=agent.config.small_blind,
            big_blind=agent.config.big_blind,
            deck=shuffle_deck(create_standard_deck()),
            current_phase=GamePhase.PREFLOP,
            hand_number=1,
        )

        # Validate all players have proper IDs before returning
        for player in initial_state.players:
            if not player.player_id or player.player_id.strip() == "":
                raise ValueError(
                    f"Player {player.name} has empty player_id after state creation"
                )

        return initial_state

    def _suit_symbol(self, suit: str) -> str:
        """Convert suit letter to symbol."""
        symbols = {"h": "♥", "d": "♦", "c": "♣", "s": "♠"}
        return symbols.get(suit, suit)

    def _get_player_at_position(
        self, game_state: HoldemState, position: int
    ) -> Optional[PlayerState]:
        """Get player at specific position."""
        for player in game_state.players:
            if player.position == position:
                return player
        return None

    def _format_player_short(self, player: PlayerState, game_state: HoldemState) -> str:
        """Format player for table display."""
        name = player.name[:5]  # Truncate long names
        f"{player.chips//1000}k" if player.chips >= 1000 else str(player.chips)

        if player.status == PlayerStatus.FOLDED:
            return f"[dim]{name}[/dim]"
        elif player.status == PlayerStatus.ALL_IN:
            return f"[yellow]{name}*[/yellow]"
        elif player == game_state.current_player:
            return f"[bold green]>{name}<[/bold green]"
        else:
            return f"[white]{name}[/white]"

    def _get_player_name_by_id(self, game_state: HoldemState, player_id: str) -> str:
        """Get player name by ID."""
        player = game_state.get_player_by_id(player_id)
        return player.name if player else "Unknown"

    def _format_last_action(self) -> Text:
        """Format the last action for display."""
        if not self.last_action or not self.state:
            return Text("No recent action")

        game_state = self.state
        if isinstance(game_state, dict):
            game_state = HoldemState.model_validate(game_state)
        player_name = self._get_player_name_by_id(
            game_state, self.last_action.get("player_id", "")
        )
        action = self.last_action.get("action", "unknown")
        amount = self.last_action.get("amount", 0)
        reasoning = self.last_action.get("reasoning", "")

        action_text = Text()
        action_text.append("Last Action: ", style="bold")
        action_text.append(f"{player_name} {action}", style="cyan")

        if amount > 0:
            action_text.append(f" {amount}", style="yellow")

        if reasoning:
            # Truncate long reasoning
            short_reasoning = (
                reasoning[:50] + "..." if len(reasoning) > 50 else reasoning
            )
            action_text.append(f" ({short_reasoning})", style="dim")

        return action_text


def main():
    """Main function to run the UI demo."""
    from haive.games.hold_em.config import create_default_holdem_config
    from haive.games.hold_em.game_agent import HoldemGameAgent

    # Create a demo game
    config = create_default_holdem_config(num_players=4, starting_chips=1000)
    agent = HoldemGameAgent(config)

    # Run the UI
    ui = HoldemRichUI()
    ui.run(agent, delay=1.5)


if __name__ == "__main__":
    main()
