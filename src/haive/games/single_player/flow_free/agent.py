"""Flow Free game agent implementation.

This module implements the agent for the Flow Free puzzle game,
handling move generation, analysis, and game flow.
"""

import time
from typing import Any

from haive.core.engine.agent.agent import register_agent
from langgraph.types import Command
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from haive.games.single_player.base import SinglePlayerGameAgent
from haive.games.single_player.flow_free.config import FlowFreeConfig
from haive.games.single_player.flow_free.models import FlowFreeMove, Position
from haive.games.single_player.flow_free.state import FlowFreeState
from haive.games.single_player.flow_free.state_manager import FlowFreeStateManager


@register_agent(FlowFreeConfig)
class FlowFreeAgent(SinglePlayerGameAgent):
    """Agent for playing Flow Free puzzle game."""

    def __init__(self, config: FlowFreeConfig = FlowFreeConfig()):
        """Initialize the Flow Free agent.

        Args:
            config: Configuration for the agent.
        """
        self.console = Console()
        self.state_manager = FlowFreeStateManager
        super().__init__(config)

    def initialize_game(self, state: dict[str, Any]) -> Command:
        """Initialize a new Flow Free game.

        Args:
            state: Initial state.

        Returns:
            Command with the initialized game state.
        """
        game_state = self.state_manager.initialize(
            difficulty=self.config.difficulty,
            player_type=self.config.player_type,
            rows=self.config.rows,
            cols=self.config.cols,
            num_flows=self.config.num_flows,
        )

        # Convert to dict for Command
        state_dict = (
            game_state.model_dump()
            if hasattr(game_state, "model_dump")
            else game_state.dict()
        )
        return Command(update=state_dict)

    def prepare_move_context(self, state: FlowFreeState) -> dict[str, Any]:
        """Prepare context for move generation.

        Args:
            state: Current game state.

        Returns:
            Context for the move generation engine.
        """
        # Generate board display
        board_display = state.to_display_string()

        # Get flow status
        flow_status = []
        for _flow_id, flow in state.flows.items():
            status = "✓" if flow.completed else " "
            path_length = len(flow.path)
            flow_status.append(
                f"{status} {flow.color}: {flow.start.position} → {flow.end.position} "
                f"(Path length: {path_length})"
            )

        # Get valid moves
        valid_moves = self.state_manager.get_legal_moves(state)
        formatted_moves = []
        for move in valid_moves:
            flow = state.flows.get(move.flow_id)
            if flow:
                formatted_moves.append(
                    f"- Flow '{flow.color}' to position {move.position}"
                )

        return {
            "board_display": board_display,
            "move_count": state.move_count,
            "completed_flows_count": sum(
                1 for flow in state.flows.values() if flow.completed
            ),
            "total_flows": len(state.flows),
            "board_fill_percentage": state.board_fill_percentage,
            "flow_status": "\n".join(flow_status),
            "valid_moves": (
                "\n".join(formatted_moves)
                if formatted_moves
                else "No valid moves available."
            ),
        }

    def prepare_analysis_context(self, state: FlowFreeState) -> dict[str, Any]:
        """Prepare context for position analysis.

        Args:
            state: Current game state.

        Returns:
            Context for the analysis engine.
        """
        # Generate board display
        board_display = state.to_display_string()

        # Get flow status
        flow_status = []
        for _flow_id, flow in state.flows.items():
            status = "✓" if flow.completed else " "
            path_length = len(flow.path)
            flow_status.append(
                f"{status} {flow.color}: {flow.start.position} → {flow.end.position} "
                f"(Path length: {path_length})"
            )

        # Include hint request if needed
        hint_request = ""
        if "hint_request" in self.runnable_config.get("configurable", {}):
            hint_request = "Please provide a hint for the next move."

        return {
            "board_display": board_display,
            "move_count": state.move_count,
            "completed_flows_count": sum(
                1 for flow in state.flows.values() if flow.completed
            ),
            "total_flows": len(state.flows),
            "board_fill_percentage": state.board_fill_percentage,
            "flow_status": "\n".join(flow_status),
            "hint_request": hint_request,
        }

    def extract_move(self, response: Any) -> FlowFreeMove:
        """Extract a move from the engine response.

        Args:
            response: Response from the engine.

        Returns:
            Extracted FlowFreeMove.
        """
        # If the response is already a FlowFreeMove object, return it
        if isinstance(response, FlowFreeMove):
            return response

        # Otherwise, extract from dict-like structure
        if hasattr(response, "flow_id") and hasattr(response, "position"):
            position = response.position
            if isinstance(position, dict):
                position = Position(row=position["row"], col=position["col"])

            return FlowFreeMove(flow_id=response.flow_id, position=position)

        # If we can't extract, raise an error
        raise ValueError(f"Could not extract move from response: {response}")

    def visualize_state(self, state: dict[str, Any]) -> None:
        """Visualize the current game state.

        Args:
            state: Current game state.
        """
        if not self.config.visualize:
            return

        try:
            # Convert to FlowFreeState if needed
            if isinstance(state, dict):
                game_state = FlowFreeState(**state)
            else:
                game_state = state

            # Create a colorful representation of the board
            table = Table(show_header=True, header_style="bold")

            # Add column headers (0, 1, 2, ...)
            table.add_column(" ", style="dim")
            for c in range(game_state.cols):
                table.add_column(str(c))

            # Add rows
            for r in range(game_state.rows):
                row_cells = [str(r)]

                for c in range(game_state.cols):
                    cell = game_state.get_cell(Position(row=r, col=c))
                    if cell and cell.flow_id is not None:
                        flow = game_state.flows.get(cell.flow_id)
                        if flow:
                            color = flow.color.lower()
                            # Map colors to Rich styles
                            style_map = {
                                "red": "red",
                                "green": "green",
                                "blue": "blue",
                                "yellow": "yellow",
                                "orange": "orange3",
                                "purple": "purple",
                                "cyan": "cyan",
                                "pink": "magenta",
                                "brown": "yellow4",
                                "gray": "gray",
                            }
                            style = style_map.get(color, "white")

                            if cell.is_endpoint:
                                cell_text = "●"  # Endpoint
                            # Pipe segment
                            elif cell.pipe_direction == "up":
                                cell_text = "↑"
                            elif cell.pipe_direction == "down":
                                cell_text = "↓"
                            elif cell.pipe_direction == "left":
                                cell_text = "←"
                            elif cell.pipe_direction == "right":
                                cell_text = "→"
                            else:
                                cell_text = "■"  # Generic pipe segment

                            row_cells.append(
                                f"[bold {style}]{cell_text}[/bold {style}]"
                            )
                        else:
                            row_cells.append("?")
                    else:
                        row_cells.append(" ")

                table.add_row(*row_cells)

            # Create a panel for the board
            board_panel = Panel(
                table,
                title=f"Flow Free [{game_state.rows}x{game_state.cols}]",
                subtitle=f"Moves: {game_state.move_count} | Hints: {game_state.hint_count}",
                border_style="green" if game_state.game_status == "victory" else "blue",
            )

            # Print the board
            self.console.print("\n")
            self.console.print(board_panel)

            # Show flow status
            flow_table = Table(show_header=True, header_style="bold")
            flow_table.add_column("Color", style="bold")
            flow_table.add_column("Status")
            flow_table.add_column("Start", justify="center")
            flow_table.add_column("End", justify="center")
            flow_table.add_column("Path Length", justify="right")

            for _flow_id, flow in game_state.flows.items():
                color = flow.color.lower()
                style_map = {
                    "red": "red",
                    "green": "green",
                    "blue": "blue",
                    "yellow": "yellow",
                    "orange": "orange3",
                    "purple": "purple",
                    "cyan": "cyan",
                    "pink": "magenta",
                    "brown": "yellow4",
                    "gray": "gray",
                }
                style = style_map.get(color, "white")

                status = "[green]✓[/green]" if flow.completed else "[gray]○[/gray]"
                flow_table.add_row(
                    f"[{style}]{flow.color}[/{style}]",
                    status,
                    str(flow.start.position),
                    str(flow.end.position),
                    str(len(flow.path)),
                )

            flow_panel = Panel(flow_table, title="Flows", border_style="blue")

            self.console.print(flow_panel)

            # Show error message if any
            if game_state.error_message:
                self.console.print(
                    f"[bold red]Message:[/bold red] {game_state.error_message}"
                )

            # Show game status
            if game_state.game_status == "victory":
                self.console.print("[bold green]🎉 Puzzle Solved![/bold green]")

            time.sleep(0.5)  # Short delay for better viewing

        except Exception as e:
            self.console.print(f"[bold red]Error in visualization: {e}[/bold red]")

    def run_game(self, debug: bool = False) -> dict[str, Any]:
        """Run a complete Flow Free game.

        Args:
            debug: Whether to show debug information.

        Returns:
            Final game state.
        """
        # Initialize the game
        initial_state = self.state_manager.initialize(
            difficulty=self.config.difficulty,
            player_type=self.config.player_type,
            rows=self.config.rows,
            cols=self.config.cols,
            num_flows=self.config.num_flows,
        )

        # Set up a minimal demo game that simulates the real gameplay
        # This is a simplified version for demonstration purposes
        current_state = initial_state

        # Heading
        self.console.print("\n[bold cyan]Flow Free Puzzle Game[/bold cyan]")
        self.console.print(
            f"[dim]Difficulty: {self.config.difficulty.value.capitalize()}[/dim]"
        )
        self.console.print()

        # Display initial state
        if self.config.visualize:
            self.visualize_state(current_state)

        # Play up to 20 moves (arbitrary limit for demo)
        for _ in range(20):
            # Get legal moves
            legal_moves = self.state_manager.get_legal_moves(current_state)

            # If no legal moves or puzzle solved, we're done
            if not legal_moves or current_state.is_solved:
                break

            # For demo, just take the first legal move
            move = legal_moves[0]

            # Apply the move
            try:
                current_state = self.state_manager.apply_move(current_state, move)

                # Display updated state
                if self.config.visualize:
                    self.console.print(f"\n[dim]Move: {move}[/dim]")
                    self.visualize_state(current_state)
            except Exception as e:
                self.console.print(f"[bold red]Error applying move: {e}[/bold red]")
                break

        # Show final status
        if current_state.is_solved:
            self.console.print("[bold green]🎉 Puzzle Solved![/bold green]")
        else:
            self.console.print("[yellow]Puzzle not completed in demo mode[/yellow]")

        return (
            current_state.model_dump()
            if hasattr(current_state, "model_dump")
            else current_state.dict()
        )
