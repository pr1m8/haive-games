"""State model for Flow Free game.

This module defines the game state for Flow Free, tracking the board,
flows, and game progress.
"""

from uuid import uuid4

from pydantic import BaseModel, Field, computed_field

from haive.games.single_player.base import SinglePlayerGameState
from haive.games.single_player.flow_free.models import PipeDirection, Position


class FlowEndpoint(BaseModel):
    """An endpoint (colored dot) in Flow Free.

    Attributes:
        position: Position of the endpoint on the board.
        is_start: Whether this is the start endpoint (otherwise it's the end).
    """

    position: Position
    is_start: bool = True


class Flow(BaseModel):
    """A flow in Flow Free, consisting of two endpoints and a path of pipes.

    Attributes:
        id: Unique identifier for the flow.
        color: Color of the flow.
        start: Starting endpoint.
        end: Ending endpoint.
        path: List of positions forming the path between endpoints.
        completed: Whether the flow is complete (endpoints connected).
    """

    id: str = Field(default_factory=lambda: str(uuid4()))
    color: str
    start: FlowEndpoint
    end: FlowEndpoint
    path: list[Position] = Field(default_factory=list)
    completed: bool = False


class Cell(BaseModel):
    """A cell on the Flow Free board.

    Attributes:
        position: Position of the cell.
        flow_id: ID of the flow occupying this cell, if any.
        is_endpoint: Whether this cell contains an endpoint.
        pipe_direction: Direction of the pipe in this cell, if any.
    """

    position: Position
    flow_id: str | None = None
    is_endpoint: bool = False
    pipe_direction: PipeDirection | None = None


class FlowFreeState(SinglePlayerGameState):
    """State for the Flow Free game.

    Attributes:
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.
        grid: 2D grid of cells.
        flows: Dictionary of flows by ID.
        current_flow_id: ID of the currently selected flow.
        puzzle_id: Identifier for the current puzzle.
        hints_used: Number of hints used.
    """

    rows: int = Field(default=5, description="Number of rows in the grid")
    cols: int = Field(default=5, description="Number of columns in the grid")
    grid: list[list[Cell]] = Field(default_factory=list, description="2D grid of cells")
    flows: dict[str, Flow] = Field(
        default_factory=dict, description="Dictionary of flows by ID"
    )
    current_flow_id: str | None = Field(
        default=None, description="ID of the currently selected flow"
    )
    puzzle_id: str = Field(
        default_factory=lambda: str(uuid4()),
        description="Identifier for the current puzzle",
    )

    @computed_field
    @property
    def is_solved(self) -> bool:
        """Check if the puzzle is solved.

        The puzzle is solved when all flows are completed and all cells
        are filled.
        """
        # Check if all flows are completed
        if not all(flow.completed for flow in self.flows.values()):
            return False

        # Check if all cells are filled
        for row in self.grid:
            for cell in row:
                if cell.flow_id is None:
                    return False

        return True

    @computed_field
    @property
    def completion_percentage(self) -> float:
        """Calculate the percentage of flows completed."""
        if not self.flows:
            return 0.0
        return (
            sum(1 for flow in self.flows.values() if flow.completed)
            / len(self.flows)
            * 100.0
        )

    @computed_field
    @property
    def total_cells(self) -> int:
        """Calculate the total number of cells on the board."""
        return self.rows * self.cols

    @computed_field
    @property
    def filled_cells(self) -> int:
        """Calculate the number of filled cells on the board."""
        return sum(1 for row in self.grid for cell in row if cell.flow_id is not None)

    @computed_field
    @property
    def board_fill_percentage(self) -> float:
        """Calculate the percentage of the board that is filled."""
        if self.total_cells == 0:
            return 0.0
        return self.filled_cells / self.total_cells * 100.0

    def get_cell(self, position: Position) -> Cell | None:
        """Get the cell at the specified position.

        Args:
            position: Position to get the cell for.

        Returns:
            The cell at the position, or None if out of bounds.
        """
        if 0 <= position.row < self.rows and 0 <= position.col < self.cols:
            return self.grid[position.row][position.col]
        return None

    def is_cell_empty(self, position: Position) -> bool:
        """Check if a cell is empty.

        Args:
            position: Position to check.

        Returns:
            True if the cell is empty, False otherwise.
        """
        cell = self.get_cell(position)
        return cell is not None and cell.flow_id is None

    def is_cell_endpoint(self, position: Position) -> bool:
        """Check if a cell contains an endpoint.

        Args:
            position: Position to check.

        Returns:
            True if the cell contains an endpoint, False otherwise.
        """
        cell = self.get_cell(position)
        return cell is not None and cell.is_endpoint

    def get_adjacent_positions(self, position: Position) -> list[Position]:
        """Get all valid adjacent positions.

        Args:
            position: Position to get adjacent positions for.

        Returns:
            List of adjacent positions.
        """
        adjacent = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
            new_row, new_col = position.row + dr, position.col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                adjacent.append(Position(row=new_row, col=new_col))
        return adjacent

    def to_display_string(self) -> str:
        """Generate a string representation of the board for display.

        Returns:
            A formatted string representation of the board.
        """
        result = []

        # Header row
        header = "   " + " ".join(str(i) for i in range(self.cols))
        result.append(header)

        # Separator
        separator = "  +" + "-" * (2 * self.cols - 1) + "+"
        result.append(separator)

        # Board rows
        for r in range(self.rows):
            row_str = f"{r} |"
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell.is_endpoint:
                    row_str += "O"
                elif cell.flow_id is not None:
                    row_str += "#"
                else:
                    row_str += " "

                if c < self.cols - 1:
                    row_str += " "

            row_str += "|"
            result.append(row_str)

        # Bottom separator
        result.append(separator)

        # Flow information
        result.append("\nFlows:")
        for _flow_id, flow in self.flows.items():
            status = "✓" if flow.completed else " "
            result.append(
                f" {status} {flow.color}: {flow.start.position} → {flow.end.position}"
            )

        return "\n".join(result)
