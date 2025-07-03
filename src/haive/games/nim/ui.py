"""Rich UI implementation for the Nim game.

This module provides a Rich-based UI for visualizing and interacting with the Nim game.
It includes a NimUI class that handles visualization of the game state, piles, and game information.
"""

import logging
from typing import Any

# Import Rich components
try:
    from rich import box
    from rich.console import Console
    from rich.layout import Layout
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text

    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    logging.warning("Rich library not available. Using fallback text UI.")

# Import the game models
from haive.games.nim.models import NimMove
from haive.games.nim.state import NimState

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger(__name__)


class NimUI:
    """Rich terminal UI for the Nim game.

    This class provides methods for visualizing the Nim game state using the Rich library.
    It includes methods for displaying the game board, piles, game information, and analysis.
    """

    # Stone representation
    STONE_SYMBOL = "🔵"  # Blue circle
    EMPTY_SYMBOL = "⚫"  # Black circle (for visualization spacing)

    # Game status emoji
    STATUS_EMOJIS = {
        "in_progress": "🎮",
        "player1_win": "🏆",
        "player2_win": "🏆",
    }

    def __init__(self):
        """Initialize the UI with a Rich console if available."""
        if RICH_AVAILABLE:
            self.console = Console()
        else:
            self.console = None
            logger.warning("Rich UI not available. Using fallback text UI.")

        # Default delay between displays (for animation effect)
        self.delay = 0.5

    def create_header(self, state: NimState) -> Panel:
        """Create header panel with game info.

        Args:
            state: The current game state.

        Returns:
            Panel: A Rich panel containing the game header information.
        """
        # Determine game status text and style
        if state.game_status == "in_progress":
            status_text = f"[bold blue]Game in Progress - {state.turn}'s Turn[/]"
        elif state.game_status == "player1_win":
            status_text = "[bold green]Game Over - Player 1 Wins![/]"
        elif state.game_status == "player2_win":
            status_text = "[bold green]Game Over - Player 2 Wins![/]"
        else:
            status_text = f"[bold yellow]Game Status: {state.game_status}[/]"

        # Game mode info
        game_mode = (
            "[bold red]Misère Mode[/]"
            if state.misere_mode
            else "[bold blue]Standard Mode[/]"
        )

        # Create the header content
        header_content = Text.from_markup(
            f"{status_text}\n"
            f"Game Mode: {game_mode} - "
            f"{'Last player to take a stone loses' if state.misere_mode else 'Last player to take a stone wins'}"
        )

        return Panel(
            header_content,
            title="[bold cyan]Nim Game[/]",
            border_style="cyan",
            box=box.DOUBLE,
        )

    def create_piles_panel(self, state: NimState) -> Panel:
        """Create a panel showing the piles of stones.

        Args:
            state: The current game state.

        Returns:
            Panel: A Rich panel containing visualizations of the piles.
        """
        pile_lines = []

        # Generate visual representation for each pile
        for i, pile_size in enumerate(state.piles):
            stones = self.STONE_SYMBOL * pile_size
            pile_line = f"[bold white]Pile {i}[/] ({pile_size}): {stones}"
            pile_lines.append(pile_line)

        # Create the panel with pile visualizations
        return Panel(
            Text.from_markup("\n".join(pile_lines)),
            title="[bold blue]Piles[/]",
            border_style="blue",
        )

    def create_moves_table(self, state: NimState) -> Table:
        """Create a table showing move history.

        Args:
            state: The current game state.

        Returns:
            Table: A Rich table containing the move history.
        """
        table = Table(title="Move History", box=box.SIMPLE)

        # Define columns
        table.add_column("Turn", style="cyan", justify="center")
        table.add_column("Player", style="green", justify="center")
        table.add_column("Move", justify="left")

        # Add move history rows
        for i, move in enumerate(state.move_history):
            player = "Player 1" if i % 2 == 0 else "Player 2"
            move_text = f"Took {move.stones_taken} stone(s) from pile {move.pile_index}"
            table.add_row(str(i + 1), player, move_text)

        return table

    def create_analysis_panel(self, state: NimState) -> Panel | None:
        """Create a panel showing the latest analysis if available.

        Args:
            state: The current game state.

        Returns:
            Optional[Panel]: A Rich panel containing analysis information, or None if no analysis.
        """
        # Get the latest analysis, if any
        latest_analysis = None

        if state.turn == "player1" and state.player2_analysis:
            latest_analysis = state.player2_analysis[-1]
            player = "Player 2"
        elif state.turn == "player2" and state.player1_analysis:
            latest_analysis = state.player1_analysis[-1]
            player = "Player 1"

        if not latest_analysis:
            return None

        # Create content based on latest analysis
        evaluation_color = {
            "winning": "green",
            "losing": "red",
            "unclear": "yellow",
        }.get(latest_analysis.position_evaluation, "white")

        analysis_text = Text.from_markup(
            f"[bold]Player:[/] {player}\n"
            f"[bold]Nim Sum:[/] {latest_analysis.nim_sum}\n"
            f"[bold]Evaluation:[/] [{evaluation_color}]{latest_analysis.position_evaluation}[/]\n"
            f"[bold]Recommended Move:[/] Take {latest_analysis.recommended_move.stones_taken} "
            f"stone(s) from pile {latest_analysis.recommended_move.pile_index}\n\n"
            f"[bold]Explanation:[/] {latest_analysis.explanation}"
        )

        return Panel(
            analysis_text,
            title="[bold magenta]Latest Analysis[/]",
            border_style="magenta",
        )

    def create_layout(self, state: NimState) -> Layout:
        """Create the complete layout for the game display.

        Args:
            state: The current game state.

        Returns:
            Layout: A Rich layout for the complete game display.
        """
        # Create main layout
        layout = Layout()

        # Split into header and body
        layout.split(Layout(name="header", size=4), Layout(name="body"))

        # Add header
        layout["header"].update(self.create_header(state))

        # Split body into game and info
        layout["body"].split_row(
            Layout(name="game", ratio=3), Layout(name="info", ratio=2)
        )

        # Update game section with piles
        layout["game"].update(self.create_piles_panel(state))

        # Split info into analysis and moves
        layout["info"].split(Layout(name="analysis"), Layout(name="moves"))

        # Add analysis if available
        analysis_panel = self.create_analysis_panel(state)
        if analysis_panel:
            layout["info"]["analysis"].update(analysis_panel)
        else:
            # Hide analysis section if no analysis
            layout["info"]["analysis"].visible = False

        # Add moves
        layout["info"]["moves"].update(self.create_moves_table(state))

        return layout

    def display_game_state(self, state: NimState | dict[str, Any]):
        """Display the current game state using Rich UI or fallback text UI.

        Args:
            state: The current game state as a NimState object or dict.
        """
        # Convert dict to NimState if needed
        if isinstance(state, dict):
            state = NimState(**state)

        if RICH_AVAILABLE and self.console:
            # Rich UI display
            self.console.clear()
            layout = self.create_layout(state)
            self.console.print(layout)
        else:
            # Fallback text UI
            self._display_text_ui(state)

    def _display_text_ui(self, state: NimState):
        """Display a text-based UI for the game state when Rich is not available.

        Args:
            state: The current game state.
        """
        # Header
        print("\n" + "=" * 50)
        print(f"NIM GAME - {state.turn}'s Turn")
        print(f"Game Status: {state.game_status}")
        print(f"Game Mode: {'Misère' if state.misere_mode else 'Standard'}")
        print("=" * 50)

        # Print piles
        print("\nPiles:")
        for i, pile_size in enumerate(state.piles):
            print(f"Pile {i} ({pile_size}): " + "O " * pile_size)

        # Print move history
        if state.move_history:
            print("\nRecent Moves:")
            for i, move in enumerate(state.move_history[-5:]):
                player = (
                    "Player 1"
                    if (len(state.move_history) - 5 + i) % 2 == 0
                    else "Player 2"
                )
                print(
                    f"- {player}: Took {move.stones_taken} stone(s) from pile {move.pile_index}"
                )

        # Print latest analysis
        latest_analysis = None
        if state.turn == "player1" and state.player2_analysis:
            latest_analysis = state.player2_analysis[-1]
            player = "Player 2"
        elif state.turn == "player2" and state.player1_analysis:
            latest_analysis = state.player1_analysis[-1]
            player = "Player 1"

        if latest_analysis:
            print(f"\n{player}'s Analysis:")
            print(f"Nim Sum: {latest_analysis.nim_sum}")
            print(f"Evaluation: {latest_analysis.position_evaluation}")
            print(
                f"Recommended Move: Take {latest_analysis.recommended_move.stones_taken} "
                f"stone(s) from pile {latest_analysis.recommended_move.pile_index}"
            )
            print(f"Explanation: {latest_analysis.explanation}")

    def prompt_for_move(self, state: NimState) -> NimMove:
        """Prompt the user to input a move.

        Args:
            state: The current game state.

        Returns:
            NimMove: The move chosen by the user.
        """
        # Display current state
        self.display_game_state(state)

        while True:
            try:
                # Prompt for pile index
                if RICH_AVAILABLE and self.console:
                    pile_idx = int(
                        self.console.input("[bold cyan]Enter pile index: [/]")
                    )
                else:
                    pile_idx = int(input("Enter pile index: "))

                # Validate pile index
                if pile_idx < 0 or pile_idx >= len(state.piles):
                    print(
                        f"Invalid pile index. Please choose between 0 and {len(state.piles)-1}."
                    )
                    continue

                # Check if pile is empty
                if state.piles[pile_idx] == 0:
                    print("This pile is empty. Please choose a non-empty pile.")
                    continue

                # Prompt for stones to take
                if RICH_AVAILABLE and self.console:
                    stones = int(
                        self.console.input(
                            f"[bold cyan]Enter stones to take (1-{state.piles[pile_idx]}): [/]"
                        )
                    )
                else:
                    stones = int(
                        input(f"Enter stones to take (1-{state.piles[pile_idx]}): ")
                    )

                # Validate stones
                if stones < 1 or stones > state.piles[pile_idx]:
                    print(
                        f"Invalid number of stones. Please choose between 1 and {state.piles[pile_idx]}."
                    )
                    continue

                # Return valid move
                return NimMove(pile_index=pile_idx, stones_taken=stones)

            except ValueError:
                print("Please enter a valid number.")
