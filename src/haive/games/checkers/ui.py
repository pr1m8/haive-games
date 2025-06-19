"""Checkers game UI module.

This module provides a rich text-based UI for the checkers game, including:
    - Beautiful board visualization with colors
    - Game information display
    - Move history tracking
    - Captured pieces visualization
    - Position analysis display
    - Game status and winner announcements
    - Move and thinking animations

The UI uses the rich library to create a visually appealing terminal interface
that makes the game more engaging and easier to follow.
"""

import time
from datetime import datetime
from typing import Any, Dict, List, Optional

from rich import box
from rich.align import Align
from rich.box import DOUBLE, HEAVY, ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.style import Style
from rich.table import Table
from rich.text import Text

from haive.games.checkers.models import CheckersMove
from haive.games.checkers.state import CheckersState


class CheckersUI:
    """Rich UI for beautiful checkers game visualization.

    This class provides a visually appealing terminal UI for checkers games,
    with styled components, animations, and comprehensive game information.

    Features:
        - Colorful board display with piece symbols
        - Move history panel
        - Captured pieces tracking
        - Game status and information
        - Position analysis display
        - Move and thinking animations
        - Game over screen

    Attributes:
        console (Console): Rich console for output
        layout (Layout): Layout manager for UI components
        colors (dict): Color schemes for different UI elements
        pieces (dict): Unicode symbols for different piece types
        game_log (List[str]): Log of game events
        move_count (int): Counter for moves
        start_time (datetime): Game start time

    Examples:
        >>> ui = CheckersUI()
        >>> state = CheckersState.initialize()
        >>> ui.display_state(state)  # Display the initial board
        >>>
        >>> # Show thinking animation during move generation
        >>> ui.show_thinking("red")
        >>>
        >>> # Display a move
        >>> move = CheckersMove(from_position="a3", to_position="b4", player="red")
        >>> ui.show_move(move)
    """

    def __init__(self):
        """Initialize the checkers UI.

        Sets up the console, layout, color schemes, piece symbols, and
        tracking variables for the UI.
        """
        self.console = Console()
        self.layout = Layout()
        self.game_log: List[str] = []
        self.move_count = 0
        self.start_time = datetime.now()

        # Color schemes
        self.colors = {
            "red_piece": "bold red",
            "red_king": "bold red on yellow",
            "black_piece": "bold black on white",
            "black_king": "bold black on yellow",
            "dark_square": "on grey23",
            "light_square": "on grey35",
            "highlight": "bold green",
            "last_move": "bold cyan",
            "captured": "dim red",
            "board_border": "bold blue",
            "player_red": "bold red",
            "player_black": "bold white",
        }

        # Unicode pieces
        self.pieces = {
            "red": "●",
            "red_king": "♔",
            "black": "○",
            "black_king": "♚",
            "empty": " ",
        }

        self._setup_layout()

    def _setup_layout(self):
        """Setup the main layout structure.

        Creates a layout with the following components:
        - Header: Game title and current turn
        - Main area: Board and sidebars
        - Footer: Status messages and controls
        - Left sidebar: Game info and captured pieces
        - Right sidebar: Analysis and move history
        """
        self.layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3),
        )

        self.layout["main"].split_row(
            Layout(name="sidebar_left", size=30),
            Layout(name="board", size=60),
            Layout(name="sidebar_right", size=40),
        )

        self.layout["sidebar_left"].split_column(
            Layout(name="game_info", size=15),
            Layout(name="captured", size=10),
            Layout(name="controls"),
        )

        self.layout["sidebar_right"].split_column(
            Layout(name="analysis", size=20), Layout(name="move_history")
        )

    def _create_board_display(
        self, state: CheckersState, last_move: Optional[CheckersMove] = None
    ) -> Panel:
        """Create a beautiful board visualization.

        Generates a rich Panel containing the styled checkers board with
        pieces, coordinates, and optional highlighting for the last move.

        Args:
            state (CheckersState): Current game state
            last_move (Optional[CheckersMove], optional): Last move to highlight.
                Defaults to None.

        Returns:
            Panel: A styled panel containing the board visualization
        """
        board_lines = []

        # Column headers with style
        col_header = "     " + "  ".join(
            f"[bold cyan]{chr(97+i)}[/bold cyan]" for i in range(8)
        )
        board_lines.append(col_header)
        board_lines.append("   " + "─" * 33)

        # Convert last move positions to indices if available
        last_from = last_to = None
        if last_move:
            last_from = self._notation_to_index(last_move.from_position)
            last_to = self._notation_to_index(last_move.to_position)

        # Build board rows
        for row in range(8):
            row_display = f"[bold cyan]{8-row}[/bold cyan] │"

            for col in range(8):
                # Determine square color
                is_dark = (row + col) % 2 == 1
                square_style = (
                    self.colors["dark_square"]
                    if is_dark
                    else self.colors["light_square"]
                )

                # Check if this square was part of the last move
                is_last_move = (row, col) == last_from or (row, col) == last_to
                if is_last_move:
                    square_style = "on blue"

                # Get piece at this position
                piece_value = state.board[row][col]
                piece_display = self._get_piece_display(piece_value)

                # Add spacing and style
                cell = f" {piece_display} "
                styled_cell = f"[{square_style}]{cell}[/{square_style}]"
                row_display += styled_cell

            row_display += f" │ [bold cyan]{8-row}[/bold cyan]"
            board_lines.append(row_display)

        # Bottom border and column labels
        board_lines.append("   " + "─" * 33)
        board_lines.append(col_header)

        # Create panel with fancy border
        board_text = "\n".join(board_lines)
        return Panel(
            board_text,
            title="♔ CHECKERS BOARD ♚",
            title_align="center",
            border_style=self.colors["board_border"],
            box=DOUBLE,
            padding=(1, 2),
        )

    def _get_piece_display(self, piece_value: int) -> str:
        """Get styled piece display.

        Converts a numeric piece value to a styled Unicode symbol.

        Args:
            piece_value (int): Piece value (0-4)

        Returns:
            str: Styled Unicode representation of the piece

        Note:
            Piece values:
            - 0: Empty square
            - 1: Red piece
            - 2: Red king
            - 3: Black piece
            - 4: Black king
        """
        if piece_value == 0:
            return self.pieces["empty"]
        elif piece_value == 1:  # Red piece
            return f"[{self.colors['red_piece']}]{self.pieces['red']}[/{self.colors['red_piece']}]"
        elif piece_value == 2:  # Red king
            return f"[{self.colors['red_king']}]{self.pieces['red_king']}[/{self.colors['red_king']}]"
        elif piece_value == 3:  # Black piece
            return f"[{self.colors['black_piece']}]{self.pieces['black']}[/{self.colors['black_piece']}]"
        elif piece_value == 4:  # Black king
            return f"[{self.colors['black_king']}]{self.pieces['black_king']}[/{self.colors['black_king']}]"
        return " "

    def _notation_to_index(self, notation: str) -> tuple[int, int]:
        """Convert algebraic notation to board indices.

        Converts algebraic notation (e.g., "a3") to zero-based row and column indices.

        Args:
            notation (str): Position in algebraic notation (e.g., "a3")

        Returns:
            tuple[int, int]: (row, col) indices

        Examples:
            >>> ui = CheckersUI()
            >>> ui._notation_to_index("a8")
            (0, 0)
            >>> ui._notation_to_index("h1")
            (7, 7)
        """
        col = ord(notation[0]) - 97
        row = 8 - int(notation[1])
        return row, col

    def _create_header(self, state: CheckersState) -> Panel:
        """Create the header panel.

        Creates a styled header with the game title, current turn, and elapsed time.

        Args:
            state (CheckersState): Current game state

        Returns:
            Panel: A styled panel for the header
        """
        current_player = state.turn.upper()
        player_color = self.colors[f"player_{state.turn}"]

        elapsed = datetime.now() - self.start_time
        elapsed_str = f"{elapsed.seconds // 60:02d}:{elapsed.seconds % 60:02d}"

        header_text = Text()
        header_text.append("♔ ", style="bold red")
        header_text.append("ROYAL CHECKERS", style="bold yellow")
        header_text.append(" ♚", style="bold white")
        header_text.append(f"\n🎮 Current Turn: ", style="dim")
        header_text.append(f"{current_player}", style=player_color)
        header_text.append(f"  ⏱️  Time: {elapsed_str}", style="dim cyan")

        return Panel(Align.center(header_text), border_style="bright_blue", box=HEAVY)

    def _create_game_info(self, state: CheckersState) -> Panel:
        """Create game information panel.

        Creates a panel with game status, move count, winner (if any),
        and piece counts.

        Args:
            state (CheckersState): Current game state

        Returns:
            Panel: A styled panel with game information
        """
        table = Table(show_header=False, box=None, padding=0)
        table.add_column(style="bold cyan")
        table.add_column()

        table.add_row("📊 Status:", state.game_status.replace("_", " ").title())
        table.add_row("🎯 Moves:", str(self.move_count))

        if state.winner:
            winner_color = self.colors[f"player_{state.winner}"]
            table.add_row(
                "🏆 Winner:", f"[{winner_color}]{state.winner.upper()}[/{winner_color}]"
            )

        # Piece count
        red_pieces = sum(1 for row in state.board for cell in row if cell in [1, 2])
        black_pieces = sum(1 for row in state.board for cell in row if cell in [3, 4])

        table.add_row("", "")
        table.add_row("🔴 Red:", f"{red_pieces} pieces")
        table.add_row("⚫ Black:", f"{black_pieces} pieces")

        return Panel(
            table,
            title="Game Info",
            title_align="left",
            border_style="blue",
            box=ROUNDED,
        )

    def _create_captured_pieces(self, state: CheckersState) -> Panel:
        """Create captured pieces display.

        Creates a panel showing pieces captured by each player.

        Args:
            state (CheckersState): Current game state

        Returns:
            Panel: A styled panel showing captured pieces
        """
        captured_text = Text()

        # Red captures
        captured_text.append("🔴 Red captured: ", style="bold red")
        red_caps = len(state.captured_pieces.get("red", []))
        captured_text.append(f"{red_caps} pieces\n", style="red")

        # Black captures
        captured_text.append("⚫ Black captured: ", style="bold white")
        black_caps = len(state.captured_pieces.get("black", []))
        captured_text.append(f"{black_caps} pieces", style="white")

        return Panel(
            captured_text,
            title="Captured Pieces",
            title_align="left",
            border_style="red",
            box=ROUNDED,
        )

    def _create_analysis_panel(self, state: CheckersState) -> Panel:
        """Create analysis panel showing latest analysis.

        Creates a panel with the latest position analysis for the current player,
        including material advantage, center control, and suggested moves.

        Args:
            state (CheckersState): Current game state

        Returns:
            Panel: A styled panel with position analysis
        """
        analysis_text = Text()

        # Get latest analysis for current player
        if state.turn == "red" and state.red_analysis:
            analysis = state.red_analysis[-1]
            analysis_text.append("🔴 Red's Analysis\n\n", style="bold red")
        elif state.turn == "black" and state.black_analysis:
            analysis = state.black_analysis[-1]
            analysis_text.append("⚫ Black's Analysis\n\n", style="bold white")
        else:
            analysis_text.append("No analysis available yet", style="dim")
            return Panel(
                analysis_text,
                title="Position Analysis",
                title_align="left",
                border_style="yellow",
                box=ROUNDED,
            )

        # Format analysis
        if hasattr(analysis, "material_advantage"):
            analysis_text.append("📊 Material: ", style="bold")
            analysis_text.append(f"{analysis.material_advantage}\n\n")

            analysis_text.append("🎯 Center Control: ", style="bold")
            analysis_text.append(f"{analysis.control_of_center}\n\n")

            analysis_text.append("💡 Evaluation: ", style="bold")
            analysis_text.append(f"{analysis.positional_evaluation}\n\n")

            if analysis.suggested_moves:
                analysis_text.append("🎲 Suggested Moves:\n", style="bold")
                for move in analysis.suggested_moves[:3]:
                    analysis_text.append(f"  • {move}\n", style="cyan")

        return Panel(
            analysis_text,
            title="Position Analysis",
            title_align="left",
            border_style="yellow",
            box=ROUNDED,
        )

    def _create_move_history(self, state: CheckersState) -> Panel:
        """Create move history panel.

        Creates a panel showing the recent moves made in the game.

        Args:
            state (CheckersState): Current game state

        Returns:
            Panel: A styled panel with move history
        """
        history_text = Text()

        if not state.move_history:
            history_text.append("No moves yet", style="dim")
        else:
            # Show last 10 moves
            recent_moves = state.move_history[-10:]
            for i, move in enumerate(recent_moves, 1):
                move_num = len(state.move_history) - len(recent_moves) + i
                player_style = self.colors[f"player_{move.player}"]

                history_text.append(f"{move_num:3d}. ", style="dim")
                history_text.append(
                    f"{move.player.capitalize():5s} ", style=player_style
                )
                history_text.append(f"{str(move)}\n", style="bold")

        return Panel(
            history_text,
            title="Move History",
            title_align="left",
            border_style="green",
            box=ROUNDED,
        )

    def _create_footer(self, message: str = "") -> Panel:
        """Create footer with status message.

        Creates a footer panel with a status message or default controls.

        Args:
            message (str, optional): Custom message to display. Defaults to "".

        Returns:
            Panel: A styled footer panel
        """
        footer_text = Text()

        if message:
            footer_text.append(message, style="bold yellow")
        else:
            footer_text.append("🎮 ", style="bold")
            footer_text.append("Use arrow keys to navigate • ", style="dim")
            footer_text.append("SPACE ", style="bold cyan")
            footer_text.append("to select • ", style="dim")
            footer_text.append("Q ", style="bold red")
            footer_text.append("to quit", style="dim")

        return Panel(
            Align.center(footer_text), border_style="bright_blue", box=box.MINIMAL
        )

    def display_state(self, state: CheckersState, message: str = ""):
        """Display the complete game state.

        Updates and displays all UI components with the current game state.

        Args:
            state (CheckersState): Current game state
            message (str, optional): Custom message for the footer. Defaults to "".

        Examples:
            >>> ui = CheckersUI()
            >>> state = CheckersState.initialize()
            >>> ui.display_state(state)
            >>>
            >>> # Display with a custom message
            >>> ui.display_state(state, "Red is thinking...")
        """
        # Get last move if available
        last_move = state.move_history[-1] if state.move_history else None

        # Update all panels
        self.layout["header"].update(self._create_header(state))
        self.layout["board"].update(self._create_board_display(state, last_move))
        self.layout["game_info"].update(self._create_game_info(state))
        self.layout["captured"].update(self._create_captured_pieces(state))
        self.layout["analysis"].update(self._create_analysis_panel(state))
        self.layout["move_history"].update(self._create_move_history(state))
        self.layout["footer"].update(self._create_footer(message))

        # Update move count
        self.move_count = len(state.move_history)

        # Clear and print
        self.console.clear()
        self.console.print(self.layout)

    def show_thinking(self, player: str):
        """Show thinking animation.

        Displays a spinner animation while a player is thinking about a move.

        Args:
            player (str): Player who is thinking ("red" or "black")

        Examples:
            >>> ui = CheckersUI()
            >>> ui.show_thinking("red")  # Shows a spinner for red's thinking
        """
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=self.console,
            transient=True,
        ) as progress:
            task = progress.add_task(
                f"[{self.colors[f'player_{player}']}]{player.capitalize()} is thinking...",
                total=None,
            )
            time.sleep(0.5)

    def show_move(self, move: CheckersMove):
        """Show move animation.

        Displays a brief animation/message when a move is made.

        Args:
            move (CheckersMove): The move that was made

        Examples:
            >>> ui = CheckersUI()
            >>> move = CheckersMove(from_position="a3", to_position="b4", player="red")
            >>> ui.show_move(move)  # Shows move message
        """
        move_text = Text()
        move_text.append("➜ ", style="bold green")
        move_text.append(
            f"{move.player.capitalize()} ", style=self.colors[f"player_{move.player}"]
        )
        move_text.append("plays: ", style="dim")
        move_text.append(str(move), style="bold yellow")

        panel = Panel(Align.center(move_text), border_style="green", box=box.MINIMAL)

        self.console.print(panel)
        time.sleep(1)

    def show_game_over(self, state: CheckersState):
        """Show game over screen.

        Displays a game over message with the winner when the game ends.

        Args:
            state (CheckersState): Final game state

        Examples:
            >>> ui = CheckersUI()
            >>> state = CheckersState(game_status="game_over", winner="red")
            >>> ui.show_game_over(state)  # Shows "RED WINS!" message
        """
        if state.winner:
            winner_text = Text()
            winner_text.append("🏆 GAME OVER! 🏆\n\n", style="bold yellow")
            winner_text.append(
                f"{state.winner.upper()} ", style=self.colors[f"player_{state.winner}"]
            )
            winner_text.append("WINS!", style="bold yellow")

            panel = Panel(
                Align.center(winner_text),
                border_style="yellow",
                box=DOUBLE,
                padding=(2, 4),
            )

            self.console.print("\n")
            self.console.print(panel)
            self.console.print("\n")
