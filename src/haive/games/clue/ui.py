"""Clue rich UI visualization module.

This module provides a visually appealing terminal UI for Clue games,
with styled components, animations, and comprehensive game information.

It uses the Rich library to create a console-based UI with:
    - Game board visualization with players, suspects, weapons, and rooms
    - Guess history with detailed responses
    - Player cards and deduction notes
    - Game status and information
    - Thinking animations and guess visualization

Example:
    >>> from haive.games.clue.ui import ClueUI
    >>> from haive.games.clue.state import ClueState
    >>>
    >>> ui = ClueUI()
    >>> state = ClueState.initialize()
    >>> ui.display_state(state)  # Display the initial game state
    >>>
    >>> # Show thinking animation for player
    >>> ui.show_thinking("player1")
    >>>
    >>> # Display a guess
    >>> from haive.games.clue.models import ClueGuess, ValidSuspect, ValidWeapon, ValidRoom
    >>> guess = ClueGuess(
    >>>     suspect=ValidSuspect.COLONEL_MUSTARD,
    >>>     weapon=ValidWeapon.KNIFE,
    >>>     room=ValidRoom.KITCHEN
    >>> )
    >>> ui.show_guess(guess, "player1")
"""

import time
from typing import Any, Dict, List, Optional, Union

from rich.align import Align
from rich.box import DOUBLE, ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from haive.games.clue.models import (
    CardType,
    ClueCard,
    ClueGuess,
    ClueResponse,
    ClueSolution,
    ValidRoom,
    ValidSuspect,
    ValidWeapon,
)
from haive.games.clue.state import ClueState


class ClueUI:
    """Rich UI for beautiful Clue game visualization.

    This class provides a visually appealing terminal UI for Clue games,
    with styled components, animations, and comprehensive game information.

    Features:
        - Game board visualization with suspects, weapons, and rooms
        - Guess history with detailed responses
        - Player cards and deduction notes
        - Game status and information
        - Thinking animations and guess visualization

    Attributes:
        console (Console): Rich console for output
        layout (Layout): Layout manager for UI components
        colors (dict): Color schemes for different UI elements

    Examples:
        >>> ui = ClueUI()
        >>> state = ClueState.initialize()
        >>> ui.display_state(state)  # Display the initial game state
    """

    def __init__(self):
        """Initialize the Clue UI with default settings."""
        self.console = Console()
        self.layout = Layout()

        # Define colors and styles
        self.colors = {
            "player1": "bright_green",
            "player2": "bright_blue",
            "header": "bold magenta",
            "info": "bright_white",
            "success": "green",
            "warning": "bright_yellow",
            "error": "bright_red",
            "suspect": "bright_cyan",
            "weapon": "bright_red",
            "room": "bright_green",
            "border": "bright_magenta",
            "title": "bold yellow",
        }

        # Set up the layout
        self._setup_layout()

    def _setup_layout(self):
        """Set up the layout structure for the UI."""
        # Main layout with header, board, and sidebar
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main", ratio=1),
        )

        # Split main area into board and sidebar
        self.layout["main"].split_row(
            Layout(name="board", ratio=3),
            Layout(name="sidebar", ratio=2),
        )

        # Split sidebar into sections
        self.layout["sidebar"].split(
            Layout(name="game_info", size=7),
            Layout(name="player_cards", ratio=1),
            Layout(name="deductions", ratio=2),
        )

        # Split board into sections
        self.layout["board"].split(
            Layout(name="suspects_weapons", size=12),
            Layout(name="guess_history", ratio=1),
        )

        # Split suspects_weapons into two columns
        self.layout["suspects_weapons"].split_row(
            Layout(name="suspects", ratio=1),
            Layout(name="weapons_rooms", ratio=1),
        )

        # Split weapons_rooms into two rows
        self.layout["weapons_rooms"].split(
            Layout(name="weapons", ratio=1),
            Layout(name="rooms", ratio=1),
        )

    def _render_header(self, state: ClueState) -> Panel:
        """Render the game header with title and status.

        Args:
            state: Current game state

        Returns:
            Panel: Styled header panel
        """
        title = Text("🕵️ CLUE DETECTIVE GAME 🕵️", style=self.colors["header"])

        if state.game_status == "ongoing":
            status_text = (
                f"Status: ONGOING | Turn: {state.current_turn_number}/{state.max_turns}"
            )
            turn_text = f"Current Player: [bold {self.colors[state.current_player]}]{state.current_player.upper()}[/]"
        else:
            status_text = f"Status: GAME OVER"
            turn_text = (
                f"Winner: [bold {self.colors[state.winner]}]{state.winner.upper()}[/]"
                if state.winner
                else "No Winner"
            )

        status = Text(status_text, style=self.colors["info"])

        return Panel(
            Align.center(
                Text.assemble(
                    title, "\n", status, "\n", Text(turn_text, justify="center")
                )
            ),
            box=ROUNDED,
            border_style=self.colors["border"],
            padding=(0, 2),
        )

    def _render_suspects(self, state: ClueState) -> Panel:
        """Render the suspects panel.

        Args:
            state: Current game state

        Returns:
            Panel: Suspects panel
        """
        suspects_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=True,
            border_style=self.colors["suspect"],
        )

        suspects_table.add_column("Suspect", style="bold cyan")
        suspects_table.add_column("Status", style="white")

        # Get all suspects
        all_suspects = [suspect.value for suspect in ValidSuspect]

        # Get suspects from player cards (if in hand, they're not the murderer)
        player1_cards = set(state.player1_cards)
        player2_cards = set(state.player2_cards)

        for suspect in all_suspects:
            status = ""
            if suspect == state.solution.suspect and state.game_status != "ongoing":
                status = "[bold red]MURDERER[/]"
            elif suspect in player1_cards:
                status = f"[{self.colors['player1']}]Player 1's Card[/]"
            elif suspect in player2_cards:
                status = f"[{self.colors['player2']}]Player 2's Card[/]"

            suspects_table.add_row(suspect, status)

        return Panel(
            suspects_table,
            title="Suspects",
            title_align="center",
            border_style=self.colors["suspect"],
            padding=(0, 1),
        )

    def _render_weapons(self, state: ClueState) -> Panel:
        """Render the weapons panel.

        Args:
            state: Current game state

        Returns:
            Panel: Weapons panel
        """
        weapons_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=True,
            border_style=self.colors["weapon"],
        )

        weapons_table.add_column("Weapon", style="bold red")
        weapons_table.add_column("Status", style="white")

        # Get all weapons
        all_weapons = [weapon.value for weapon in ValidWeapon]

        # Get weapons from player cards (if in hand, they're not the murder weapon)
        player1_cards = set(state.player1_cards)
        player2_cards = set(state.player2_cards)

        for weapon in all_weapons:
            status = ""
            if weapon == state.solution.weapon and state.game_status != "ongoing":
                status = "[bold red]MURDER WEAPON[/]"
            elif weapon in player1_cards:
                status = f"[{self.colors['player1']}]Player 1's Card[/]"
            elif weapon in player2_cards:
                status = f"[{self.colors['player2']}]Player 2's Card[/]"

            weapons_table.add_row(weapon, status)

        return Panel(
            weapons_table,
            title="Weapons",
            title_align="center",
            border_style=self.colors["weapon"],
            padding=(0, 1),
        )

    def _render_rooms(self, state: ClueState) -> Panel:
        """Render the rooms panel.

        Args:
            state: Current game state

        Returns:
            Panel: Rooms panel
        """
        rooms_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=True,
            border_style=self.colors["room"],
        )

        rooms_table.add_column("Room", style="bold green")
        rooms_table.add_column("Status", style="white")

        # Get all rooms
        all_rooms = [room.value for room in ValidRoom]

        # Get rooms from player cards (if in hand, they're not the murder room)
        player1_cards = set(state.player1_cards)
        player2_cards = set(state.player2_cards)

        for room in all_rooms:
            status = ""
            if room == state.solution.room and state.game_status != "ongoing":
                status = "[bold red]CRIME SCENE[/]"
            elif room in player1_cards:
                status = f"[{self.colors['player1']}]Player 1's Card[/]"
            elif room in player2_cards:
                status = f"[{self.colors['player2']}]Player 2's Card[/]"

            rooms_table.add_row(room, status)

        return Panel(
            rooms_table,
            title="Rooms",
            title_align="center",
            border_style=self.colors["room"],
            padding=(0, 1),
        )

    def _render_guess_history(self, state: ClueState) -> Panel:
        """Render the guess history panel.

        Args:
            state: Current game state

        Returns:
            Panel: Guess history panel
        """
        if not state.guesses:
            return Panel(
                "[italic]No guesses have been made yet[/]",
                title="Guess History",
                title_align="center",
                border_style=self.colors["border"],
                padding=(1, 1),
            )

        history_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=True,
            border_style=self.colors["border"],
        )

        history_table.add_column("#", style="dim", width=3)
        history_table.add_column("Player", style="white")
        history_table.add_column("Suspect", style=self.colors["suspect"])
        history_table.add_column("Weapon", style=self.colors["weapon"])
        history_table.add_column("Room", style=self.colors["room"])
        history_table.add_column("Response", style="white")

        for i, (guess, response) in enumerate(
            zip(state.guesses, state.responses, strict=False)
        ):
            player = "Player 1" if i % 2 == 0 else "Player 2"
            player_color = (
                self.colors["player1"] if i % 2 == 0 else self.colors["player2"]
            )

            response_text = ""
            if response.is_correct:
                response_text = "[bold green]CORRECT![/]"
            elif response.responding_player:
                response_text = f"Refuted by [bold]{response.responding_player}[/]"
                if response.refuting_card:
                    card_type_color = {
                        "Suspect": self.colors["suspect"],
                        "Weapon": self.colors["weapon"],
                        "Room": self.colors["room"],
                    }.get(response.refuting_card.card_type.value, "white")
                    response_text += (
                        f" with [{card_type_color}]{response.refuting_card.name}[/]"
                    )
            else:
                response_text = "[italic]No one could refute[/]"

            history_table.add_row(
                str(i + 1),
                f"[{player_color}]{player}[/]",
                guess.suspect.value,
                guess.weapon.value,
                guess.room.value,
                response_text,
            )

        return Panel(
            history_table,
            title="Guess History",
            title_align="center",
            border_style=self.colors["border"],
            padding=(0, 1),
        )

    def _render_game_info(self, state: ClueState) -> Panel:
        """Render game information panel.

        Args:
            state: Current game state

        Returns:
            Panel: Game information panel
        """
        info_table = Table(
            show_header=False,
            box=None,
            expand=True,
            padding=(0, 1),
        )

        info_table.add_column("Key", style="bright_blue")
        info_table.add_column("Value", style="white")

        # Add game information
        info_table.add_row("Game Status", state.game_status.upper())
        info_table.add_row(
            "Current Turn", f"{state.current_turn_number}/{state.max_turns}"
        )
        info_table.add_row(
            "Current Player",
            f"[{self.colors[state.current_player]}]{state.current_player.upper()}[/]",
        )

        # Add solution information if game is over
        if state.game_status != "ongoing":
            # Get the clean string values from enum values or handle as is
            suspect_value = (
                state.solution.suspect.value
                if hasattr(state.solution.suspect, "value")
                else str(state.solution.suspect)
            )
            weapon_value = (
                state.solution.weapon.value
                if hasattr(state.solution.weapon, "value")
                else str(state.solution.weapon)
            )
            room_value = (
                state.solution.room.value
                if hasattr(state.solution.room, "value")
                else str(state.solution.room)
            )

            info_table.add_row(
                "Solution",
                f"[{self.colors['suspect']}]{suspect_value}[/], "
                f"[{self.colors['weapon']}]{weapon_value}[/], "
                f"[{self.colors['room']}]{room_value}[/]",
            )

            if state.winner:
                winner_color = (
                    self.colors["player1"]
                    if state.winner == "player1"
                    else self.colors["player2"]
                )
                info_table.add_row(
                    "Winner", f"[bold {winner_color}]{state.winner.upper()}[/]"
                )
            else:
                info_table.add_row("Winner", "[italic]No winner (game ended)[/]")

        return Panel(
            info_table,
            title="Game Info",
            title_align="center",
            border_style="bright_blue",
            padding=(0, 1),
        )

    def _render_player_cards(self, state: ClueState) -> Panel:
        """Render player cards panel.

        Args:
            state: Current game state

        Returns:
            Panel: Player cards panel
        """
        cards_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=True,
            border_style=self.colors["border"],
        )

        cards_table.add_column("Player", style="white")
        cards_table.add_column("Cards", style="white")

        # Format player 1's cards
        player1_cards_text = ""
        for card in state.player1_cards:
            card_type = (
                "suspect"
                if card in [s.value for s in ValidSuspect]
                else "weapon" if card in [w.value for w in ValidWeapon] else "room"
            )
            player1_cards_text += f"[{self.colors[card_type]}]{card}[/], "
        player1_cards_text = player1_cards_text.rstrip(", ")

        # Format player 2's cards
        player2_cards_text = ""
        for card in state.player2_cards:
            card_type = (
                "suspect"
                if card in [s.value for s in ValidSuspect]
                else "weapon" if card in [w.value for w in ValidWeapon] else "room"
            )
            player2_cards_text += f"[{self.colors[card_type]}]{card}[/], "
        player2_cards_text = player2_cards_text.rstrip(", ")

        cards_table.add_row(
            f"[{self.colors['player1']}]Player 1[/]",
            player1_cards_text or "[italic]No cards[/]",
        )
        cards_table.add_row(
            f"[{self.colors['player2']}]Player 2[/]",
            player2_cards_text or "[italic]No cards[/]",
        )

        return Panel(
            cards_table,
            title="Player Cards",
            title_align="center",
            border_style=self.colors["border"],
            padding=(0, 1),
        )

    def _render_deductions(self, state: ClueState) -> Panel:
        """Render deductions and analysis panel.

        Args:
            state: Current game state

        Returns:
            Panel: Deductions panel
        """
        if not state.player1_hypotheses and not state.player2_hypotheses:
            return Panel(
                "[italic]No deductions have been made yet[/]",
                title="Deductions",
                title_align="center",
                border_style=self.colors["border"],
                padding=(1, 1),
            )

        deduction_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=True,
            border_style=self.colors["border"],
        )

        deduction_table.add_column("Player", style="white")
        deduction_table.add_column("Suspect", style=self.colors["suspect"])
        deduction_table.add_column("Weapon", style=self.colors["weapon"])
        deduction_table.add_column("Room", style=self.colors["room"])
        deduction_table.add_column("Confidence", style="white")

        # Player 1 hypotheses
        for hypothesis in state.player1_hypotheses[
            -3:
        ]:  # Show only the last 3 hypotheses
            deduction_table.add_row(
                f"[{self.colors['player1']}]Player 1[/]",
                hypothesis.get("prime_suspect", "Unknown"),
                hypothesis.get("prime_weapon", "Unknown"),
                hypothesis.get("prime_room", "Unknown"),
                f"{hypothesis.get('confidence', 0.0) * 100:.0f}%",
            )

        # Player 2 hypotheses
        for hypothesis in state.player2_hypotheses[
            -3:
        ]:  # Show only the last 3 hypotheses
            deduction_table.add_row(
                f"[{self.colors['player2']}]Player 2[/]",
                hypothesis.get("prime_suspect", "Unknown"),
                hypothesis.get("prime_weapon", "Unknown"),
                hypothesis.get("prime_room", "Unknown"),
                f"{hypothesis.get('confidence', 0.0) * 100:.0f}%",
            )

        return Panel(
            deduction_table,
            title="Deductions",
            title_align="center",
            border_style=self.colors["border"],
            padding=(0, 1),
        )

    def display_state(self, state: Union[ClueState, Dict[str, Any]]) -> None:
        """Display the current game state with rich formatting.

        Renders the complete game state including suspects, weapons, rooms,
        guess history, player cards, and game information in a formatted layout.

        Args:
            state (Union[ClueState, Dict[str, Any]]): Current game state

        Returns:
            None

        Example:
            >>> ui = ClueUI()
            >>> state = ClueState.initialize()
            >>> ui.display_state(state)
        """
        # Convert dict to ClueState if needed
        if isinstance(state, dict):
            state = ClueState(**state)

        # Update each component in the layout
        self.layout["header"].update(self._render_header(state))
        self.layout["suspects"].update(self._render_suspects(state))
        self.layout["weapons"].update(self._render_weapons(state))
        self.layout["rooms"].update(self._render_rooms(state))
        self.layout["guess_history"].update(self._render_guess_history(state))
        self.layout["game_info"].update(self._render_game_info(state))
        self.layout["player_cards"].update(self._render_player_cards(state))
        self.layout["deductions"].update(self._render_deductions(state))

        # Render the complete layout
        self.console.clear()
        self.console.print(self.layout)

    def show_thinking(self, player: str, message: str = "Thinking...") -> None:
        """Display a thinking animation for the current player.

        Shows a spinner animation with player-colored text to indicate
        that the player is thinking about their guess.

        Args:
            player (str): Current player ("player1" or "player2")
            message (str, optional): Custom message to display. Defaults to "Thinking...".

        Returns:
            None

        Example:
            >>> ui = ClueUI()
            >>> ui.show_thinking("player1", "Analyzing clues...")
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

    def show_guess(self, guess: ClueGuess, player: str) -> None:
        """Display a guess being made.

        Shows a formatted message indicating which player made a guess,
        including the suspect, weapon, and room.

        Args:
            guess (ClueGuess): The guess being made
            player (str): Player making the guess ("player1" or "player2")

        Returns:
            None

        Example:
            >>> ui = ClueUI()
            >>> guess = ClueGuess(
            ...     suspect=ValidSuspect.COLONEL_MUSTARD,
            ...     weapon=ValidWeapon.KNIFE,
            ...     room=ValidRoom.KITCHEN
            ... )
            >>> ui.show_guess(guess, "player1")
        """
        player_color = self.colors[player]

        guess_panel = Panel(
            f"[{player_color}]{player.upper()}[/] guesses:\n\n"
            f"[{self.colors['suspect']}]Suspect:[/] {guess.suspect.value}\n"
            f"[{self.colors['weapon']}]Weapon:[/] {guess.weapon.value}\n"
            f"[{self.colors['room']}]Room:[/] {guess.room.value}",
            title="New Guess",
            title_align="center",
            border_style=player_color,
            padding=(1, 2),
        )

        self.console.print(guess_panel)
        time.sleep(1.0)  # Brief pause after showing the guess

    def show_response(self, response: ClueResponse, player: str) -> None:
        """Display a response to a guess.

        Shows a formatted message indicating the response to a guess,
        including which player responded and what card was shown.

        Args:
            response (ClueResponse): The response to the guess
            player (str): Player who made the guess ("player1" or "player2")

        Returns:
            None

        Example:
            >>> ui = ClueUI()
            >>> response = ClueResponse(
            ...     is_correct=False,
            ...     responding_player="player2",
            ...     refuting_card=ClueCard(name="Knife", card_type=CardType.WEAPON)
            ... )
            >>> ui.show_response(response, "player1")
        """
        player_color = self.colors[player]

        if response.is_correct:
            response_panel = Panel(
                f"[bold green]CORRECT GUESS![/]\n\n"
                f"[{player_color}]{player.upper()}[/] has solved the mystery!",
                title="Response",
                title_align="center",
                border_style="green",
                padding=(1, 2),
            )
        elif response.responding_player:
            responding_color = (
                self.colors["player1"]
                if response.responding_player == "player1"
                else self.colors["player2"]
            )

            response_text = f"[{responding_color}]{response.responding_player.upper()}[/] refutes the guess"

            if response.refuting_card:
                card_type_color = {
                    "Suspect": self.colors["suspect"],
                    "Weapon": self.colors["weapon"],
                    "Room": self.colors["room"],
                }.get(response.refuting_card.card_type.value, "white")

                response_text += f" by showing:\n\n[{card_type_color}]{response.refuting_card.name}[/]"

            response_panel = Panel(
                response_text,
                title="Response",
                title_align="center",
                border_style=responding_color,
                padding=(1, 2),
            )
        else:
            response_panel = Panel(
                "No player could refute this guess!",
                title="Response",
                title_align="center",
                border_style="yellow",
                padding=(1, 2),
            )

        self.console.print(response_panel)
        time.sleep(1.0)  # Brief pause after showing the response

    def show_game_over(self, state: ClueState) -> None:
        """Display game over message with result.

        Shows a game over panel with the winner highlighted in their color,
        and reveals the solution.

        Args:
            state (ClueState): Final game state

        Returns:
            None

        Example:
            >>> ui = ClueUI()
            >>> state = ClueState.initialize()
            >>> state.game_status = "player1_win"
            >>> state.winner = "player1"
            >>> ui.show_game_over(state)
        """
        # Get the clean string values from enum values or handle as is
        suspect_value = (
            state.solution.suspect.value
            if hasattr(state.solution.suspect, "value")
            else str(state.solution.suspect)
        )
        weapon_value = (
            state.solution.weapon.value
            if hasattr(state.solution.weapon, "value")
            else str(state.solution.weapon)
        )
        room_value = (
            state.solution.room.value
            if hasattr(state.solution.room, "value")
            else str(state.solution.room)
        )

        if state.winner:
            winner_color = self.colors[state.winner]

            game_over_panel = Panel(
                f"[bold {winner_color}]{state.winner.upper()}[/] wins!\n\n"
                f"The solution was:\n"
                f"[{self.colors['suspect']}]Suspect:[/] {suspect_value}\n"
                f"[{self.colors['weapon']}]Weapon:[/] {weapon_value}\n"
                f"[{self.colors['room']}]Room:[/] {room_value}",
                title="🏆 GAME OVER 🏆",
                title_align="center",
                border_style="bright_green",
                padding=(1, 2),
                box=DOUBLE,
            )
        else:
            game_over_panel = Panel(
                f"Game over! Maximum turns reached.\n\n"
                f"The solution was:\n"
                f"[{self.colors['suspect']}]Suspect:[/] {suspect_value}\n"
                f"[{self.colors['weapon']}]Weapon:[/] {weapon_value}\n"
                f"[{self.colors['room']}]Room:[/] {room_value}",
                title="🏆 GAME OVER 🏆",
                title_align="center",
                border_style="bright_yellow",
                padding=(1, 2),
                box=DOUBLE,
            )

        self.console.print(game_over_panel)
        time.sleep(1.0)  # Pause to show the game over message
