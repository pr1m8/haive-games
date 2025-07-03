import time

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table
from rich.text import Text

from haive.games.single_player.towers_of_hanoi.agent import HanoiAgent
from haive.games.single_player.towers_of_hanoi.config import HanoiAgentConfig
from haive.games.single_player.towers_of_hanoi.game import HanoiGame

console = Console()


class HanoiUI:
    """Rich UI for Tower of Hanoi game."""

    def __init__(self):
        self.game: HanoiGame | None = None
        self.agent: HanoiAgent | None = None
        self.state = {}

    def run(self):
        """Run the interactive UI."""
        console.clear()
        console.print("[bold cyan]Tower of Hanoi - AI Player[/bold cyan]\n")

        # Get game configuration
        num_disks = IntPrompt.ask(
            "Number of disks", default=3, choices=["2", "3", "4", "5"]
        )
        num_pegs = IntPrompt.ask("Number of pegs", default=3, choices=["3", "4", "5"])

        # Initialize game
        self.game = HanoiGame(num_disks=num_disks, num_pegs=num_pegs)
        self.game.initialize()

        # Initialize agent
        config = HanoiAgentConfig()
        self.agent = HanoiAgent(config)

        # Initialize state
        self.state = {"game": self.game}

        # Game loop
        self.play_game()

    def play_game(self):
        """Main game loop."""
        with Live(self.create_display(), refresh_per_second=1) as live:
            while not self.game.is_solved:
                # Update display
                live.update(self.create_display())

                # Get user choice
                console.print("\n[yellow]Options:[/yellow]")
                console.print("1. Let AI make next move")
                console.print("2. Make manual move")
                console.print("3. Auto-play to completion")
                console.print("4. Quit")

                choice = Prompt.ask("Choice", choices=["1", "2", "3", "4"])

                if choice == "1":
                    self.ai_move()
                    time.sleep(1)  # Pause to see move
                elif choice == "2":
                    self.manual_move()
                elif choice == "3":
                    self.auto_play(live)
                    break
                elif choice == "4":
                    break

                # Update display
                live.update(self.create_display())

        if self.game.is_solved:
            console.print("\n[bold green]🎉 Puzzle Solved! 🎉[/bold green]")
            console.print(f"Total moves: {len(self.game.moves)}")
            console.print(f"Optimal moves: {self.game.optimal_moves}")
            efficiency = (self.game.optimal_moves / len(self.game.moves)) * 100
            console.print(f"Efficiency: {efficiency:.1f}%")

    def create_display(self) -> Panel:
        """Create the game display."""
        layout = Layout()
        layout.split_column(
            Layout(name="board", size=10),
            Layout(name="info", size=6),
            Layout(name="moves", size=10),
        )

        # Board display
        board_text = Text(self.game.format_board_state(), justify="center")
        board_panel = Panel(board_text, title="Game Board", border_style="cyan")
        layout["board"].update(board_panel)

        # Info display
        info_table = Table(show_header=False, box=None)
        info_table.add_column("Label", style="dim")
        info_table.add_column("Value", style="bold")

        info_table.add_row("Disks:", str(self.game.num_disks))
        info_table.add_row("Pegs:", str(self.game.num_pegs))
        info_table.add_row("Moves:", str(len(self.game.moves)))
        info_table.add_row("Optimal:", str(self.game.optimal_moves))

        if self.game.moves:
            efficiency = (self.game.optimal_moves / len(self.game.moves)) * 100
            info_table.add_row("Efficiency:", f"{efficiency:.1f}%")

        info_panel = Panel(info_table, title="Game Info", border_style="green")
        layout["info"].update(info_panel)

        # Moves display
        moves_text = self.format_moves()
        moves_panel = Panel(moves_text, title="Recent Moves", border_style="yellow")
        layout["moves"].update(moves_panel)

        return Panel(layout, title="Tower of Hanoi", border_style="bold")

    def format_moves(self) -> str:
        """Format recent moves for display."""
        if not self.game.moves:
            return "No moves yet"

        lines = []
        for i, move in enumerate(self.game.moves[-5:], 1):
            move_num = len(self.game.moves) - 5 + i
            lines.append(
                f"{move_num}. Move disk {move['disk']} from peg {move['from_peg']} to peg {move['to_peg']}"
            )

        return "\n".join(lines)

    def ai_move(self):
        """Let AI make a move."""
        console.print("\n[cyan]AI is thinking...[/cyan]")

        # Run through agent workflow
        result = self.agent.invoke(self.state)

        # Display analysis if available
        if result.get("analysis"):
            console.print("\n[bold]AI Analysis:[/bold]")
            console.print(Panel(result["analysis"], border_style="dim"))

        # The move should already be applied
        console.print("[green]AI made its move![/green]")

    def manual_move(self):
        """Allow manual move input."""
        valid_moves = self.game.get_valid_moves()

        console.print("\n[yellow]Valid moves:[/yellow]")
        for i, move in enumerate(valid_moves, 1):
            console.print(
                f"{i}. Move disk {move['disk']} from peg {move['from_peg']} to peg {move['to_peg']}"
            )

        choice = IntPrompt.ask(
            "Select move", choices=[str(i) for i in range(1, len(valid_moves) + 1)]
        )
        selected = valid_moves[choice - 1]

        self.game.make_move(selected["from_peg"], selected["to_peg"])
        console.print("[green]Move made![/green]")

    def auto_play(self, live):
        """Auto-play to completion."""
        console.print("\n[cyan]Auto-playing to completion...[/cyan]")

        while not self.game.is_solved:
            # AI move
            self.agent.invoke(self.state)

            # Update display
            live.update(self.create_display())
            time.sleep(0.5)  # Pause between moves


def main():
    """Run the Tower of Hanoi UI."""
    ui = HanoiUI()
    ui.run()


if __name__ == "__main__":
    main()
