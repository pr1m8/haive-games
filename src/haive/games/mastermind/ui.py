"""Rich UI for the Mastermind game.

This module provides a rich terminal UI for the Mastermind game using
the Rich library. It displays the game board, guesses, feedback, and
analysis in a visually appealing way.
"""

from typing import Any

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from haive.games.mastermind.state import MastermindState


class MastermindUI:
    """Rich terminal UI for the Mastermind game.

    This class provides methods for displaying the Mastermind game state
    in a visually appealing way using the Rich library.
    """

    # Color emoji mappings
    COLOR_EMOJIS = {
        "red": "🔴",
        "blue": "🔵",
        "green": "🟢",
        "yellow": "🟡",
        "purple": "🟣",
        "orange": "🟠",
        "white": "⚪",
        "black": "⚫",
    }

    # Color style mappings
    COLOR_STYLES = {
        "red": "red",
        "blue": "blue",
        "green": "green",
        "yellow": "yellow",
        "purple": "magenta",
        "orange": "orange1",
        "white": "white",
        "black": "black",
    }

    def __init__(self, console: Console | None = None):
        """Initialize the UI with a Rich console.

        Args:
            console: Optional Rich console to use. If not provided, a new one is created.
        """
        self.console = console or Console()

    def display_welcome(self):
        """Display a welcome message for the Mastermind game."""
        title = Text("🎮 MASTERMIND 🎮", style="bold yellow")
        panel = Panel(
            Text(
                "Try to guess the secret code in 10 turns or less!\n"
                "🎯 Black pegs indicate correct color and position\n"
                "🔄 White pegs indicate correct color but wrong position\n\n"
                "Available colors: 🔴 red, 🔵 blue, 🟢 green, 🟡 yellow, 🟣 purple, 🟠 orange",
                justify="center",
            ),
            title=title,
            border_style="yellow",
        )
        self.console.print(panel)

    def color_to_styled_text(self, color: str) -> Text:
        """Convert a color name to a styled text object.

        Args:
            color: The name of the color.

        Returns:
            A Rich Text object with appropriate styling for the color.
        """
        emoji = self.COLOR_EMOJIS.get(color, "❓")
        style = self.COLOR_STYLES.get(color, "white")
        return Text(f"{emoji} {color}", style=style)

    def create_guesses_table(self, state: MastermindState) -> Table:
        """Create a table displaying all guesses and their feedback.

        Args:
            state: The current game state.

        Returns:
            A Rich Table object containing the guesses and feedback.
        """
        table = Table(show_header=True, header_style="bold")
        table.add_column("Turn", style="dim", width=6)
        table.add_column("Guess", width=40)
        table.add_column("Feedback", width=20)

        if not state.guesses:
            table.add_row("--", "No guesses yet", "--")
            return table

        for i, (guess, feedback) in enumerate(
            zip(state.guesses, state.feedback, strict=False)
        ):
            # Create styled color texts for the guess
            color_texts = [self.color_to_styled_text(color) for color in guess.colors]

            # Create feedback text
            feedback_text = Text()
            feedback_text.append(f"🎯 {feedback.correct_position} ", style="bold green")
            feedback_text.append(f"🔄 {feedback.correct_color}", style="bold blue")

            # Add the row
            table.add_row(
                str(i + 1),
                Text(" ").join(color_texts),
                feedback_text,
            )

        return table

    def create_info_panel(self, state: MastermindState) -> Panel:
        """Create a panel with game information.

        Args:
            state: The current game state.

        Returns:
            A Rich Panel object containing game information.
        """
        info_text = Text()
        info_text.append(
            f"Turn: {state.current_turn_number}/{state.max_turns}\n", style="bold cyan"
        )
        info_text.append(f"Codemaker: {state.codemaker}\n", style="bold yellow")
        info_text.append(
            f"Codebreaker: {'player2' if state.codemaker == 'player1' else 'player1'}\n",
            style="bold green",
        )
        info_text.append(f"Game Status: {state.game_status}\n", style="bold magenta")

        # Only show secret code if game is over
        if state.game_status != "ongoing":
            secret_code_text = Text("Secret Code: ", style="bold red")
            color_texts = [
                self.color_to_styled_text(color) for color in state.secret_code
            ]
            secret_code_text.append(Text(" ").join(color_texts))
            info_text.append("\n")
            info_text.append(secret_code_text)

        return Panel(info_text, title="Game Info", border_style="cyan")

    def create_analysis_panel(self, state: MastermindState) -> Panel | None:
        """Create a panel with the most recent analysis if available.

        Args:
            state: The current game state.

        Returns:
            A Rich Panel object containing analysis information, or None if no analysis available.
        """
        codebreaker = "player2" if state.codemaker == "player1" else "player1"
        analysis = None

        if codebreaker == "player1" and state.player1_analysis:
            analysis = state.player1_analysis[-1]
        elif codebreaker == "player2" and state.player2_analysis:
            analysis = state.player2_analysis[-1]

        if not analysis:
            return None

        analysis_text = Text()

        try:
            # Handle both dict and MastermindAnalysis object formats
            if isinstance(analysis, dict):
                analysis_text.append(
                    f"Possible combinations: {analysis['possible_combinations']}\n",
                    style="bold cyan",
                )

                high_prob_colors = analysis.get("high_probability_colors", [])
                if high_prob_colors:
                    analysis_text.append(
                        "High probability colors: ", style="bold green"
                    )
                    color_texts = [
                        self.color_to_styled_text(color) for color in high_prob_colors
                    ]
                    analysis_text.append(Text(" ").join(color_texts))
                    analysis_text.append("\n")

                analysis_text.append(
                    f"Strategy: {analysis.get('strategy', 'Unknown')}\n",
                    style="bold magenta",
                )
                analysis_text.append(
                    f"Confidence: {analysis.get('confidence', '?')}/10",
                    style="bold yellow",
                )
            else:
                # Handle MastermindAnalysis object
                analysis_text.append(
                    f"Possible combinations: {analysis.possible_combinations}\n",
                    style="bold cyan",
                )

                if analysis.high_probability_colors:
                    analysis_text.append(
                        "High probability colors: ", style="bold green"
                    )
                    color_texts = [
                        self.color_to_styled_text(color)
                        for color in analysis.high_probability_colors
                    ]
                    analysis_text.append(Text(" ").join(color_texts))
                    analysis_text.append("\n")

                analysis_text.append(
                    f"Strategy: {analysis.strategy}\n", style="bold magenta"
                )
                analysis_text.append(
                    f"Confidence: {analysis.confidence}/10", style="bold yellow"
                )
        except Exception as e:
            analysis_text = Text(f"Error displaying analysis: {e}", style="bold red")

        return Panel(analysis_text, title="🔍 Analysis", border_style="green")

    def create_layout(self, state: MastermindState) -> Layout:
        """Create a complete layout for the game state.

        Args:
            state: The current game state.

        Returns:
            A Rich Layout object containing all game UI components.
        """
        layout = Layout()
        layout.split(
            Layout(self.create_info_panel(state), name="info", size=8),
            Layout(name="main"),
        )

        # Add analysis panel if available
        analysis_panel = self.create_analysis_panel(state)
        if analysis_panel:
            layout["main"].split(
                Layout(self.create_guesses_table(state), name="guesses"),
                Layout(analysis_panel, name="analysis", size=8),
            )
        else:
            layout["main"].update(self.create_guesses_table(state))

        return layout

    def display_game_state(self, state: MastermindState):
        """Display the current game state.

        Args:
            state: The current game state.
        """
        self.console.clear()
        self.console.print(self.create_layout(state))

    def display_final_results(self, state: MastermindState):
        """Display the final results of the game.

        Args:
            state: The final game state.
        """
        winner = state.winner or "None"
        result_text = Text()

        if state.game_status == "ongoing":
            result_text.append("Game not completed!", style="bold yellow")
        elif winner == state.codemaker:
            result_text.append(
                f"🏆 Codemaker ({state.codemaker}) wins!", style="bold red"
            )
            result_text.append(
                "\nThe codebreaker couldn't guess the secret code in time."
            )
        else:
            result_text.append(f"🏆 Codebreaker ({winner}) wins!", style="bold green")
            result_text.append(
                f"\nThe secret code was guessed in {len(state.guesses)} turns!"
            )

        # Show the secret code
        result_text.append("\n\n")
        result_text.append("Secret Code: ", style="bold")
        color_texts = [self.color_to_styled_text(color) for color in state.secret_code]
        result_text.append(Text(" ").join(color_texts))

        # Add statistics
        result_text.append("\n\n")
        result_text.append(
            f"Total turns: {len(state.guesses)}/{state.max_turns}\n", style="cyan"
        )

        panel = Panel(result_text, title="🎮 Game Over", border_style="yellow")
        self.console.print(panel)

    def extract_game_state(self, state_dict: dict[str, Any]) -> MastermindState | None:
        """Extract a MastermindState from a state dictionary.

        Args:
            state_dict: The state dictionary to convert.

        Returns:
            A MastermindState object, or None if conversion fails.
        """
        try:
            return MastermindState(**state_dict)
        except Exception as e:
            self.console.print(f"[bold red]Error extracting game state: {e}[/bold red]")
            return None

    def print_debug_info(self, data: Any, label: str = "Debug"):
        """Print debug information.

        Args:
            data: The data to print.
            label: A label for the debug panel.
        """
        debug_text = str(data)
        panel = Panel(debug_text, title=f"🐞 {label}", border_style="red")
        self.console.print(panel)
