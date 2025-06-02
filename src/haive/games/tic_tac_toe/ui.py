"""Rich UI Game Runner for Tic Tac Toe.

This module provides a beautiful, interactive UI for running Tic Tac Toe games
using the Rich library for enhanced terminal displays.
"""

import time
from typing import Any, Dict, Optional

from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.models import TicTacToeAnalysis
from haive.games.tic_tac_toe.state import TicTacToeState


class RichTicTacToeRunner:
    """Rich UI runner for Tic Tac Toe games."""

    def __init__(self, agent: TicTacToeAgent):
        """Initialize the Rich UI runner.

        Args:
            agent: The TicTacToe agent to run
        """
        self.agent = agent
        self.console = Console()
        self.current_state: Optional[TicTacToeState] = None

    def create_board_panel(self, state: TicTacToeState) -> Panel:
        """Create a rich panel displaying the game board.

        Args:
            state: Current game state

        Returns:
            Rich Panel with the game board
        """
        # Create a table for the board
        board_table = Table(show_header=False, show_lines=True, box=box.HEAVY)

        # Add columns
        for _ in range(3):
            board_table.add_column(width=3, justify="center")

        # Add rows
        for row in state.board:
            cells = []
            for cell in row:
                if cell is None:
                    cells.append(Text("   ", style="dim"))
                elif cell == "X":
                    cells.append(Text(" X ", style="bold red"))
                else:  # cell == "O"
                    cells.append(Text(" O ", style="bold blue"))
            board_table.add_row(*cells)

        # Determine panel style based on game status
        if state.game_status == "ongoing":
            title = f"🎮 Tic Tac Toe - Turn: {state.turn}"
            border_style = "green"
        elif state.game_status == "draw":
            title = "🤝 Game Draw!"
            border_style = "yellow"
        elif state.winner:
            symbol = state.winner
            player = state.player_X if symbol == "X" else state.player_O
            title = f"🏆 {symbol} ({player}) Wins!"
            border_style = "gold1"
        else:
            title = "🎮 Tic Tac Toe"
            border_style = "white"

        return Panel(
            Align.center(board_table),
            title=title,
            border_style=border_style,
            padding=(1, 2),
        )

    def create_game_info_panel(self, state: TicTacToeState) -> Panel:
        """Create a panel with game information.

        Args:
            state: Current game state

        Returns:
            Rich Panel with game info
        """
        info_table = Table(show_header=False, box=None)
        info_table.add_column("Property", style="cyan")
        info_table.add_column("Value", style="white")

        # Player assignments
        info_table.add_row("Player X:", f"{state.player_X}")
        info_table.add_row("Player O:", f"{state.player_O}")
        info_table.add_row("", "")  # Spacing

        # Current turn info
        if state.game_status == "ongoing":
            current_player = state.current_player_name
            info_table.add_row("Current Turn:", f"{state.turn} ({current_player})")

        # Move history
        if state.move_history:
            last_move = state.move_history[-1]
            info_table.add_row(
                "Last Move:", f"{last_move.player} → ({last_move.row}, {last_move.col})"
            )
            info_table.add_row("Move Count:", str(len(state.move_history)))
        else:
            info_table.add_row("Move Count:", "0")

        # Game status
        info_table.add_row("Game Status:", state.game_status)

        # Error message
        if state.error_message:
            info_table.add_row("", "")
            info_table.add_row("⚠️ Error:", Text(state.error_message, style="bold red"))

        return Panel(
            info_table, title="📊 Game Information", border_style="blue", padding=(1, 1)
        )

    def create_analysis_panel(self, state: TicTacToeState) -> Optional[Panel]:
        """Create a panel showing the latest analysis.

        Args:
            state: Current game state

        Returns:
            Rich Panel with analysis info, or None if no analysis
        """
        # Get the most recent analysis
        analysis = None
        analyzer_player = None

        if state.player1_analysis:
            if not state.player2_analysis or len(state.player1_analysis) > len(
                state.player2_analysis
            ):
                analysis = state.player1_analysis[-1]
                analyzer_player = "player1"
            elif state.player2_analysis:
                analysis = state.player2_analysis[-1]
                analyzer_player = "player2"
        elif state.player2_analysis:
            analysis = state.player2_analysis[-1]
            analyzer_player = "player2"

        if not analysis:
            return None

        # Create analysis table
        analysis_table = Table(show_header=False, box=None)
        analysis_table.add_column("Aspect", style="magenta")
        analysis_table.add_column("Details", style="white")

        analysis_table.add_row("Analyzer:", analyzer_player)
        analysis_table.add_row("Position:", analysis.position_evaluation)

        if analysis.winning_moves:
            moves_str = ", ".join(
                [f"({m['row']}, {m['col']})" for m in analysis.winning_moves]
            )
            analysis_table.add_row("🎯 Winning:", moves_str)

        if analysis.blocking_moves:
            moves_str = ", ".join(
                [f"({m['row']}, {m['col']})" for m in analysis.blocking_moves]
            )
            analysis_table.add_row("🛡️ Blocking:", moves_str)

        if analysis.fork_opportunities:
            moves_str = ", ".join(
                [f"({m['row']}, {m['col']})" for m in analysis.fork_opportunities]
            )
            analysis_table.add_row("🍴 Forks:", moves_str)

        if analysis.recommended_move:
            move = analysis.recommended_move
            analysis_table.add_row("💡 Suggested:", f"({move['row']}, {move['col']})")

        # Strategy (truncated)
        strategy_text = analysis.strategy
        if len(strategy_text) > 100:
            strategy_text = strategy_text[:97] + "..."
        analysis_table.add_row("", "")
        analysis_table.add_row("Strategy:", Text(strategy_text, style="italic"))

        return Panel(
            analysis_table,
            title="🧠 AI Analysis",
            border_style="magenta",
            padding=(1, 1),
        )

    def create_layout(self, state: TicTacToeState) -> Layout:
        """Create the main layout for the game display.

        Args:
            state: Current game state

        Returns:
            Rich Layout object
        """
        layout = Layout()

        # Split into main sections
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3),
        )

        # Header
        title_text = Text("🎯 Haive Tic Tac Toe", style="bold cyan", justify="center")
        layout["header"].update(Panel(title_text, box=box.ROUNDED))

        # Main content
        layout["main"].split_row(
            Layout(name="board", ratio=2), Layout(name="sidebar", ratio=1)
        )

        # Board
        layout["board"].update(self.create_board_panel(state))

        # Sidebar
        sidebar_panels = [self.create_game_info_panel(state)]

        analysis_panel = self.create_analysis_panel(state)
        if analysis_panel:
            sidebar_panels.append(analysis_panel)

        if len(sidebar_panels) == 1:
            layout["sidebar"].update(sidebar_panels[0])
        else:
            layout["sidebar"].split_column(*[Layout() for _ in sidebar_panels])
            for i, panel in enumerate(sidebar_panels):
                layout["sidebar"].children[i].update(panel)

        # Footer
        if state.game_status == "ongoing":
            footer_text = Text(
                "⏳ Waiting for AI move...", style="yellow", justify="center"
            )
        else:
            footer_text = Text(
                "🎉 Game Complete! Press Ctrl+C to exit.",
                style="green",
                justify="center",
            )

        layout["footer"].update(Panel(footer_text, box=box.ROUNDED))

        return layout

    def show_thinking_animation(self, player: str, duration: float = 2.0):
        """Show a thinking animation while AI is processing.

        Args:
            player: The player who is thinking
            duration: How long to show the animation
        """
        with Progress(
            SpinnerColumn(),
            TextColumn(f"[bold blue]{player} is thinking..."),
            console=self.console,
            transient=True,
        ) as progress:
            task = progress.add_task("thinking", total=100)

            start_time = time.time()
            while time.time() - start_time < duration:
                progress.update(task, advance=1)
                time.sleep(duration / 100)

    def run_game(
        self, show_thinking: bool = True, step_delay: float = 1.0, debug: bool = False
    ) -> Dict[str, Any]:
        """Run the Tic Tac Toe game with Rich UI.

        Args:
            show_thinking: Whether to show thinking animations
            step_delay: Delay between moves in seconds
            debug: Whether to show debug information

        Returns:
            Final game state
        """
        self.console.clear()

        # Show initial setup
        with self.console.status("[bold green]Setting up game...", spinner="dots"):
            # Initialize the game
            initial_state = self.agent.state_manager.initialize(
                first_player=self.agent.config.first_player,
                player_X=self.agent.config.player_X,
                player_O=self.agent.config.player_O,
            )

        final_state = None

        try:
            # Convert initial state to dict for consistency
            initial_dict = (
                initial_state.model_dump()
                if hasattr(initial_state, "model_dump")
                else initial_state.dict()
            )
            current_state = TicTacToeState(**initial_dict)

            if debug:
                self.console.print(f"[cyan]DEBUG: Initial state created[/cyan]")
                self.console.print(f"[dim]Board: {current_state.board}[/dim]")
                self.console.print(f"[dim]Turn: {current_state.turn}[/dim]")
                self.console.print(f"[dim]Status: {current_state.game_status}[/dim]")

            # Create live display
            with Live(
                self.create_layout(current_state),
                console=self.console,
                refresh_per_second=4,
            ) as live:

                step_count = 0
                for step in self.agent.stream(initial_dict, stream_mode="values"):
                    step_count += 1

                    if debug:
                        self.console.print(f"[cyan]DEBUG: Step {step_count}[/cyan]")
                        self.console.print(f"[dim]Step type: {type(step)}[/dim]")
                        if isinstance(step, dict):
                            self.console.print(f"[dim]Keys: {list(step.keys())}[/dim]")
                            if "board" in step:
                                self.console.print(f"[dim]Board: {step['board']}[/dim]")
                            if "turn" in step:
                                self.console.print(f"[dim]Turn: {step['turn']}[/dim]")
                            if "move_history" in step:
                                self.console.print(
                                    f"[dim]Moves: {len(step['move_history'])} total[/dim]"
                                )

                    # Ensure step is a dict and create TicTacToeState
                    if isinstance(step, dict):
                        try:
                            self.current_state = TicTacToeState(**step)
                            if debug:
                                self.console.print(
                                    f"[green]DEBUG: State created successfully[/green]"
                                )
                        except Exception as e:
                            self.console.print(
                                f"[red]Error creating state from step: {e}[/red]"
                            )
                            self.console.print(f"[dim]Step data: {step}[/dim]")
                            continue
                    else:
                        self.current_state = step
                        if debug:
                            self.console.print(
                                f"[green]DEBUG: Using step as state directly[/green]"
                            )

                    # Update display
                    live.update(self.create_layout(self.current_state))
                    final_state = step

                    # Add delay between moves for better viewing
                    if self.current_state.game_status == "ongoing":
                        time.sleep(step_delay)
                    else:
                        # Game is over, show final state longer
                        if debug:
                            self.console.print(
                                f"[yellow]DEBUG: Game ended with status: {self.current_state.game_status}[/yellow]"
                            )
                        time.sleep(step_delay * 2)
                        break

        except KeyboardInterrupt:
            self.console.print("\n[yellow]Game interrupted by user[/yellow]")
        except Exception as e:
            self.console.print(f"\n[red]Game error: {e}[/red]")
            import traceback

            self.console.print(f"[dim]{traceback.format_exc()}[/dim]")
            final_state = self.current_state

        return final_state

    def show_game_summary(self, final_state: Dict[str, Any]):
        """Show a summary of the completed game.

        Args:
            final_state: The final state of the game
        """
        if not final_state:
            return

        state = (
            TicTacToeState(**final_state)
            if isinstance(final_state, dict)
            else final_state
        )

        # Create summary table
        summary_table = Table(title="🎯 Game Summary", box=box.ROUNDED)
        summary_table.add_column("Metric", style="cyan")
        summary_table.add_column("Value", style="white")

        # Game outcome
        if state.game_status == "draw":
            summary_table.add_row("Outcome", "Draw")
        elif state.winner:
            winner_player = state.player_X if state.winner == "X" else state.player_O
            summary_table.add_row("Winner", f"{state.winner} ({winner_player})")

        # Game stats
        summary_table.add_row("Total Moves", str(len(state.move_history)))
        summary_table.add_row("Player X", state.player_X)
        summary_table.add_row("Player O", state.player_O)

        # Analysis counts
        if state.player1_analysis:
            summary_table.add_row("Player1 Analyses", str(len(state.player1_analysis)))
        if state.player2_analysis:
            summary_table.add_row("Player2 Analyses", str(len(state.player2_analysis)))

        self.console.print()
        self.console.print(summary_table)

        # Show move history
        if state.move_history:
            self.console.print()
            move_table = Table(title="📝 Move History", box=box.SIMPLE)
            move_table.add_column("Move #", style="cyan")
            move_table.add_column("Player", style="yellow")
            move_table.add_column("Position", style="white")

            for i, move in enumerate(state.move_history, 1):
                move_table.add_row(str(i), move.player, f"({move.row}, {move.col})")

            self.console.print(move_table)
