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

from rich import box
from rich.align import Align
from rich.box import DOUBLE, HEAVY, ROUNDED
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
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
        self.game_log: list[str] = []
        self.move_count = 0
        self.start_time = datetime.now()

        # Color schemes
        self.colors = {
            "red_piece": "bold bright_red",
            "red_king": "bold bright_red on yellow3",
            "black_piece": "bold bright_white on grey39",
            "black_king": "bold bright_white on yellow3",
            "dark_square": "on grey19",
            "light_square": "on grey27",
            "highlight": "bold green",
            "last_move": "on bright_blue",
            "last_move_red": "bold bright_red on bright_blue",
            "last_move_black": "bold bright_white on bright_blue",
            "captured": "dim red",
            "board_border": "bold cyan",
            "player_red": "bold bright_red",
            "player_black": "bold bright_white",
        }

        # Unicode pieces
        self.pieces = {
            "red": "●",
            "red_king": "◆",  # Diamond for red king
            "black": "○",
            "black_king": "◇",  # Diamond outline for black king
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
        self, state: CheckersState, last_move: CheckersMove | None = None
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
                is_last_move_highlight = ""

                if (row, col) == last_from or (row, col) == last_to:
                    square_style = self.colors["last_move"]

                    # We'll set a flag to apply special styling to the piece later
                    if last_move and (row, col) == last_to:
                        is_last_move_highlight = last_move.player

                # Get piece at this position
                piece_value = state.board[row][col]
                piece_display = self._get_piece_display(
                    piece_value, is_last_move_highlight
                )

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

    def _get_piece_display(self, piece_value: int, last_move_player: str = "") -> str:
        """Get styled piece display.

        Converts a numeric piece value to a styled Unicode symbol.

        Args:
            piece_value (int): Piece value (0-4)
            last_move_player (str, optional): Player color for last move highlighting.
                Defaults to "".

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

        # Special highlight for pieces that were just moved
        if last_move_player == "red" and piece_value in [1, 2]:
            # Red piece that was just moved
            if piece_value == 1:  # Regular piece
                return f"[{self.colors['last_move_red']}]{self.pieces['red']}[/{self.colors['last_move_red']}]"
            # King
            return f"[{self.colors['last_move_red']}]{self.pieces['red_king']}[/{self.colors['last_move_red']}]"
        if last_move_player == "black" and piece_value in [3, 4]:
            # Black piece that was just moved
            if piece_value == 3:  # Regular piece
                return f"[{self.colors['last_move_black']}]{self.pieces['black']}[/{self.colors['last_move_black']}]"
            # King
            return f"[{self.colors['last_move_black']}]{self.pieces['black_king']}[/{self.colors['last_move_black']}]"

        # Normal piece styling
        if piece_value == 1:  # Red piece
            return f"[{self.colors['red_piece']}]{self.pieces['red']}[/{self.colors['red_piece']}]"
        if piece_value == 2:  # Red king
            return f"[{self.colors['red_king']}]{self.pieces['red_king']}[/{self.colors['red_king']}]"
        if piece_value == 3:  # Black piece
            return f"[{self.colors['black_piece']}]{self.pieces['black']}[/{self.colors['black_piece']}]"
        if piece_value == 4:  # Black king
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
        header_text.append("♔ ", style="bold bright_red")
        header_text.append("ROYAL CHECKERS", style="bold bright_yellow")
        header_text.append(" ♚", style="bold bright_white")

        # More prominent current turn display
        turn_indicator = "\n🎮 CURRENT TURN: "
        if current_player == "RED":
            piece_symbol = self.pieces["red"]
            header_text.append(turn_indicator, style="dim")
            header_text.append(
                f"{piece_symbol} {current_player} {piece_symbol}",
                style=f"bold {player_color}",
            )
        else:
            piece_symbol = self.pieces["black"]
            header_text.append(turn_indicator, style="dim")
            header_text.append(
                f"{piece_symbol} {current_player} {piece_symbol}",
                style=f"bold {player_color}",
            )

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

        # Piece count with detailed breakdown
        red_regular = sum(1 for row in state.board for cell in row if cell == 1)
        red_kings = sum(1 for row in state.board for cell in row if cell == 2)
        red_pieces = red_regular + red_kings

        black_regular = sum(1 for row in state.board for cell in row if cell == 3)
        black_kings = sum(1 for row in state.board for cell in row if cell == 4)
        black_pieces = black_regular + black_kings

        table.add_row("", "")

        # Show pieces with their actual symbols
        red_info = f"{red_pieces} pieces"
        if red_kings > 0:
            red_info += f" ({red_kings} {self.pieces['red_king']})"

        black_info = f"{black_pieces} pieces"
        if black_kings > 0:
            black_info += f" ({black_kings} {self.pieces['black_king']})"

        table.add_row(
            f"🔴 Red [{self.pieces['red']}]:", red_info, style=self.colors["player_red"]
        )
        table.add_row(
            f"⚫ Black [{self.pieces['black']}]:",
            black_info,
            style=self.colors["player_black"],
        )

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

        # Red captures with visual representation
        captured_text.append("🔴 Red captured: ", style=self.colors["player_red"])
        red_caps = len(state.captured_pieces.get("red", []))
        captured_text.append(f"{red_caps} pieces", style=self.colors["player_red"])

        # Add visual representation of captured pieces
        if red_caps > 0:
            captured_text.append("\n")
            for _ in range(min(red_caps, 8)):  # Show up to 8 pieces visually
                captured_text.append(
                    f"{self.pieces['black']} ", style=self.colors["player_black"]
                )
            if red_caps > 8:
                captured_text.append(f"+{red_caps - 8} more", style="dim")

        captured_text.append("\n\n")

        # Black captures
        captured_text.append("⚫ Black captured: ", style=self.colors["player_black"])
        black_caps = len(state.captured_pieces.get("black", []))
        captured_text.append(f"{black_caps} pieces", style=self.colors["player_black"])

        # Add visual representation of captured pieces
        if black_caps > 0:
            captured_text.append("\n")
            for _ in range(min(black_caps, 8)):  # Show up to 8 pieces visually
                captured_text.append(
                    f"{self.pieces['red']} ", style=self.colors["player_red"]
                )
            if black_caps > 8:
                captured_text.append(f"+{black_caps - 8} more", style="dim")

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
        # Use a table for better formatting
        if not state.move_history:
            history_text = Text("No moves yet", style="dim")
        else:
            # Create a table for better formatting
            history_table = Table(show_header=True, box=box.SIMPLE)
            history_table.add_column("Move", style="dim", width=4)
            history_table.add_column("Red", style=self.colors["player_red"], width=8)
            history_table.add_column(
                "Black", style=self.colors["player_black"], width=8
            )

            # Process moves in pairs (Red & Black)
            moves = state.move_history
            total_pairs = (len(moves) + 1) // 2  # Round up to include incomplete pairs

            # Show last 8 move pairs (16 moves) at most
            start_pair = max(0, total_pairs - 8)
            for pair_idx in range(start_pair, total_pairs):
                move_num = pair_idx + 1
                red_idx = pair_idx * 2
                black_idx = red_idx + 1

                red_move = str(moves[red_idx]) if red_idx < len(moves) else ""
                black_move = str(moves[black_idx]) if black_idx < len(moves) else ""

                # Style the most recent moves differently
                red_style = "bold bright_red" if red_idx == len(moves) - 1 else ""
                black_style = "bold bright_white" if black_idx == len(moves) - 1 else ""

                # Add the row
                history_table.add_row(
                    str(move_num),
                    f"[{red_style}]{red_move}[/{red_style}]" if red_style else red_move,
                    (
                        f"[{black_style}]{black_move}[/{black_style}]"
                        if black_style
                        else black_move
                    ),
                )

            history_text = history_table

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
            progress.add_task(
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
            # Create a much more impressive game over screen
            winner_text = Text()

            # Trophy decorations
            trophy_line = "🏆 " * 7
            winner_text.append(f"{trophy_line}\n\n", style="bold bright_yellow")

            # Game over text
            winner_text.append(
                "G A M E   O V E R !\n\n", style="bold bright_cyan underline"
            )

            # Winner announcement with piece symbol
            if state.winner == "red":
                piece_symbol = self.pieces["red"]
                crown_symbol = self.pieces["red_king"]
                winner_text.append(
                    f"{crown_symbol} {piece_symbol} ",
                    style=self.colors[f"player_{state.winner}"],
                )
                winner_text.append(
                    f"{state.winner.upper()} WINS!",
                    style=f"bold {self.colors[f'player_{state.winner}']}",
                )
                winner_text.append(
                    f" {piece_symbol} {crown_symbol}",
                    style=self.colors[f"player_{state.winner}"],
                )
            else:
                piece_symbol = self.pieces["black"]
                crown_symbol = self.pieces["black_king"]
                winner_text.append(
                    f"{crown_symbol} {piece_symbol} ",
                    style=self.colors[f"player_{state.winner}"],
                )
                winner_text.append(
                    f"{state.winner.upper()} WINS!",
                    style=f"bold {self.colors[f'player_{state.winner}']}",
                )
                winner_text.append(
                    f" {piece_symbol} {crown_symbol}",
                    style=self.colors[f"player_{state.winner}"],
                )

            # Move stats
            winner_text.append(
                f"\n\nTotal Moves: {len(state.move_history)}", style="bright_green"
            )

            # Trophy line at bottom
            winner_text.append(f"\n\n{trophy_line}", style="bold bright_yellow")

            panel = Panel(
                Align.center(winner_text),
                border_style="bright_yellow",
                box=DOUBLE,
                padding=(2, 8),
            )

            self.console.print("\n")
            self.console.print(panel)
            self.console.print("\n")
