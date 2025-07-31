"""Connect4 rich UI visualization module.

This module provides a visually appealing terminal UI for Connect4 games,
with styled components, animations, and comprehensive game information.

It uses the Rich library to create a console-based UI with:
    - Colorful board display with piece symbols
    - Move history panel
    - Game status and information
    - Position analysis display
    - Move and thinking animations

Example:
    >>> from haive.games.connect4.ui import Connect4UI
    >>> from haive.games.connect4.state import Connect4State
    >>>
    >>> ui = Connect4UI()
    >>> state = Connect4State.initialize()
    >>> ui.display_state(state)  # Display the initial board
    >>>
    >>> # Show thinking animation for player move
    >>> ui.show_thinking("red")
    >>>
    >>> # Display a move
    >>> from haive.games.connect4.models import Connect4Move
    >>> move = Connect4Move(column=3)
    >>> ui.show_move(move, "red")

"""

import time

from rich.align import Align
from rich.box import ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from haive.games.connect4.models import Connect4Move
from haive.games.connect4.state import Connect4State


class Connect4UI:
    """Rich UI for beautiful Connect4 game visualization.

    This class provides a visually appealing terminal UI for Connect4 games,
    with styled components, animations, and comprehensive game information.

    Features:
        - Colorful board display with piece symbols
        - Move history panel
        - Game status and information
        - Position analysis display
        - Move and thinking animations

    Attributes:
        console (Console): Rich console for output
        layout (Layout): Layout manager for UI components
        colors (dict): Color schemes for different UI elements

    Examples:
        >>> ui = Connect4UI()
        >>> state = Connect4State.initialize()
        >>> ui.display_state(state)  # Display the initial board

    """

    def __init__(self):
        """Initialize the Connect4 UI with default settings."""
        self.console = Console()
        self.layout = Layout()

        # Define colors and styles
        self.colors = {
            "red": {"piece": "bright_red", "bg": "on red", "text": "red"},
            "yellow": {"piece": "bright_yellow", "bg": "on yellow", "text": "yellow"},
            "board": "blue",
            "header": "bold cyan",
            "info": "bright_white",
            "success": "green",
            "warning": "bright_yellow",
            "error": "bright_red",
        }

        # Set up the layout
        self._setup_layout()

        # Move history
        self.move_history: list[str] = []
        self.move_count = 0

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
            Layout(name="game_info", size=6),
            Layout(name="analysis", ratio=2),
            Layout(name="move_history", ratio=1),
        )

    def _render_header(self, state: Connect4State) -> Panel:
        """Render the game header with title and status.

        Args:
            state: Current game state

        Returns:
            Panel: Styled header panel

        """
        title = Text("🔴 🟡 CONNECT 4 GAME 🟡 🔴", style=self.colors["header"])
        status = Text(f"Status: {state.game_status.upper()}", style=self.colors["info"])

        if state.game_status == "ongoing":
            turn_text = f"Current Turn: [bold {self.colors[state.turn]['text']}]{state.turn.upper()}[/]"
        else:
            winner_color = (
                self.colors[state.winner]["text"]
                if state.winner
                else self.colors["info"]
            )
            turn_text = f"Winner: [bold {winner_color}]{
                state.winner.upper() if state.winner else 'DRAW'
            }[/]"

        return Panel(
            Align.center(
                Text.assemble(
                    title, "\n", status, "\n", Text(turn_text, justify="center")
                )
            ),
            box=ROUNDED,
            border_style=self.colors["header"],
            padding=(0, 2),
        )

    def _render_board(self, state: Connect4State) -> Panel:
        """Render the Connect4 board with pieces.

        Args:
            state: Current game state

        Returns:
            Panel: Styled board panel

        """
        # Create a table for the board
        board_table = Table(
            show_header=True,
            box=ROUNDED,
            expand=False,
            border_style=self.colors["board"],
        )

        # Add column headers (0-6)
        for col in range(7):
            board_table.add_column(
                f"[bold white]{col}[/]", justify="center", vertical="middle", width=3
            )

        # Add board rows
        for _row_idx, row in enumerate(state.board):
            row_cells = []
            for _col_idx, cell in enumerate(row):
                if cell is None:
                    row_cells.append("⚪")  # Empty cell
                elif cell == "red":
                    row_cells.append(
                        f"[{self.colors['red']['piece']}]🔴[/]"
                    )  # Red piece
                elif cell == "yellow":
                    row_cells.append(
                        f"[{self.colors['yellow']['piece']}]🟡[/]"
                    )  # Yellow piece

            board_table.add_row(*row_cells)

        return Panel(
            Align.center(board_table),
            title="Game Board",
            title_align="center",
            border_style=self.colors["board"],
            padding=(1, 1),
        )

    def _render_game_info(self, state: Connect4State) -> Panel:
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
        info_table.add_row("Game Phase", state.game_status.upper())
        info_table.add_row(
            "Current Turn",
            f"[{self.colors[state.turn]['text']}]{state.turn.upper()}[/]",
        )
        info_table.add_row("Total Moves", str(len(state.move_history)))

        # Add winner information if game is over
        if state.game_status != "ongoing":
            winner_text = state.winner.upper() if state.winner else "DRAW"
            winner_style = (
                self.colors[state.winner]["text"] if state.winner else "white"
            )
            info_table.add_row("Result", f"[bold {winner_style}]{winner_text}[/]")

        return Panel(
            info_table,
            title="Game Info",
            title_align="center",
            border_style="bright_blue",
            padding=(1, 1),
        )

    def _render_analysis(self, state: Connect4State) -> Panel:
        """Render analysis information panel.

        Args:
            state: Current game state

        Returns:
            Panel: Analysis information panel

        """
        # Get the latest analysis for the previous player
        analysis = None
        analysis_player = None

        if state.red_analysis and state.turn == "yellow":
            analysis = state.red_analysis[-1]
            analysis_player = "red"
        elif state.yellow_analysis and state.turn == "red":
            analysis = state.yellow_analysis[-1]
            analysis_player = "yellow"

        if not analysis:
            return Panel(
                "[italic]No analysis available yet[/]",
                title="Position Analysis",
                title_align="center",
                border_style="bright_blue",
                padding=(1, 1),
            )

        # Create analysis table
        analysis_table = Table(
            show_header=False,
            box=None,
            expand=True,
            padding=(0, 1),
        )

        analysis_table.add_column("Metric", style="cyan")
        analysis_table.add_column("Value", style="white")

        # Add analysis data
        player_color = self.colors[analysis_player]["text"]
        analysis_table.add_row(
            "Player", f"[bold {player_color}]{analysis_player.upper()}[/]"
        )

        # Position score
        score = analysis.get("position_score", 0)
        score_style = "green" if score > 0 else "red" if score < 0 else "white"
        analysis_table.add_row("Position Score", f"[{score_style}]{score}[/]")

        # Center control
        center_control = analysis.get("center_control", 5)
        center_style = (
            "green" if center_control > 7 else "yellow" if center_control > 4 else "red"
        )
        analysis_table.add_row(
            "Center Control", f"[{center_style}]{center_control}/10[/]"
        )

        # Winning chances
        winning_chances = analysis.get("winning_chances", 50)
        chances_style = (
            "green"
            if winning_chances > 70
            else "yellow"
            if winning_chances > 40
            else "red"
        )
        analysis_table.add_row(
            "Winning Chances", f"[{chances_style}]{winning_chances}%[/]"
        )

        # Threats
        threats = analysis.get("threats", {})
        winning_moves = threats.get("winning_moves", [])
        blocking_moves = threats.get("blocking_moves", [])

        if winning_moves:
            winning_text = ", ".join(str(col) for col in winning_moves)
            analysis_table.add_row("Winning Moves", f"[bold green]{winning_text}[/]")

        if blocking_moves:
            blocking_text = ", ".join(str(col) for col in blocking_moves)
            analysis_table.add_row("Blocking Needed", f"[bold red]{blocking_text}[/]")

        # Suggested columns
        suggested = analysis.get("suggested_columns", [])
        if suggested:
            suggested_text = ", ".join(str(col) for col in suggested)
            analysis_table.add_row(
                "Suggested Columns", f"[bold cyan]{suggested_text}[/]"
            )

        return Panel(
            analysis_table,
            title="Position Analysis",
            title_align="center",
            border_style="bright_blue",
            padding=(1, 1),
        )

    def _render_move_history(self, state: Connect4State) -> Panel:
        """Render move history panel.

        Args:
            state: Current game state

        Returns:
            Panel: Move history panel

        """
        if not state.move_history:
            return Panel(
                "[italic]No moves yet[/]",
                title="Move History",
                title_align="center",
                border_style="bright_blue",
                padding=(1, 1),
            )

        # Create move history table
        history_table = Table(
            show_header=True,
            box=None,
            expand=True,
            padding=(0, 1),
        )

        history_table.add_column("#", style="dim", width=3)
        history_table.add_column("Player", style="white")
        history_table.add_column("Move", style="white")

        # Display the most recent moves (up to 10)
        for i, move in enumerate(state.move_history[-10:]):
            actual_move_num = len(state.move_history) - 10 + i + 1
            player = "red" if actual_move_num % 2 == 1 else "yellow"
            player_color = self.colors[player]["text"]

            history_table.add_row(
                str(actual_move_num),
                f"[{player_color}]{player.upper()}[/]",
                f"Column {move.column}",
            )

        return Panel(
            history_table,
            title="Recent Moves",
            title_align="center",
            border_style="bright_blue",
            padding=(1, 1),
        )

    def display_state(self, state: Connect4State | dict) -> None:
        """Display the current game state with rich formatting.

        Renders the complete game state including board, game info,
        analysis, and move history in a formatted layout.

        Args:
            state (Union[Connect4State, dict]): Current game state (Connect4State or dict)

        Returns:
            None

        Example:
            >>> ui = Connect4UI()
            >>> state = Connect4State.initialize()
            >>> ui.display_state(state)

        """
        # Convert dict to Connect4State if needed
        if isinstance(state, dict):
            state = Connect4State(**state)

        # Update each component in the layout
        self.layout["header"].update(self._render_header(state))
        self.layout["board"].update(self._render_board(state))
        self.layout["game_info"].update(self._render_game_info(state))
        self.layout["analysis"].update(self._render_analysis(state))
        self.layout["move_history"].update(self._render_move_history(state))

        # Render the complete layout
        self.console.clear()
        self.console.print(self.layout)

    def show_thinking(self, player: str, message: str = "Thinking...") -> None:
        """Display a thinking animation for the current player.

        Shows a spinner animation with player-colored text to indicate
        that the player is thinking about their move.

        Args:
            player (str): Current player ("red" or "yellow")
            message (str, optional): Custom message to display. Defaults to "Thinking...".

        Returns:
            None

        Example:
            >>> ui = Connect4UI()
            >>> ui.show_thinking("red", "Analyzing position...")

        """
        player_color = self.colors[player]["text"]

        with Progress(
            SpinnerColumn(),
            TextColumn(f"[{player_color}]{player.upper()}[/] {message}"),
            console=self.console,
            transient=True,
        ) as progress:
            progress.add_task("thinking", total=None)
            time.sleep(1.0)  # Show thinking animation for 1 second

    def show_move(self, move: Connect4Move, player: str) -> None:
        """Display a move animation.

        Shows a formatted message indicating which player made which move,
        with color-coded player name and piece symbol.

        Args:
            move (Connect4Move): The move being made
            player (str): Player making the move ("red" or "yellow")

        Returns:
            None

        Example:
            >>> ui = Connect4UI()
            >>> move = Connect4Move(column=3)
            >>> ui.show_move(move, "red")

        """
        player_color = self.colors[player]["text"]
        piece_symbol = "🔴" if player == "red" else "🟡"

        self.console.print(
            f"\n[{player_color}]{player.upper()}[/] moves: {piece_symbol} Column {move.column}"
        )
        time.sleep(0.5)  # Brief pause after showing the move

    def show_game_over(self, winner: str | None = None) -> None:
        """Display game over message with result.

        Shows a game over panel with the winner highlighted in their color,
        or indicating a draw if there's no winner.

        Args:
            winner (Optional[str], optional): Winning player or None for a draw. Defaults to None.

        Returns:
            None

        Example:
            >>> ui = Connect4UI()
            >>> ui.show_game_over("red")  # Red player wins
            >>> ui.show_game_over(None)   # Draw

        """
        if winner:
            winner_color = self.colors[winner]["text"]
            message = f"[bold {winner_color}]{winner.upper()}[/] WINS!"
            self.console.print(
                Panel(
                    Align.center(Text(message, justify="center")),
                    title="🏆 GAME OVER 🏆",
                    border_style="bright_green",
                    padding=(1, 2),
                )
            )
        else:
            self.console.print(
                Panel(
                    Align.center(Text("IT'S A DRAW!", justify="center")),
                    title="🏆 GAME OVER 🏆",
                    border_style="bright_yellow",
                    padding=(1, 2),
                )
            )

        time.sleep(1.0)  # Pause to show the game over message
