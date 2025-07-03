# ======================================================
# SUDOKU BOARD
# ======================================================

from haive.games.core.board.base import GridBoard
from haive.games.core.position.base import GridPosition
from haive.games.single_player.sudoku.game.cell import SudokuCell
from haive.games.single_player.sudoku.game.piece import SudokuDigit


class SudokuBoard(GridBoard[SudokuCell, GridPosition, SudokuDigit]):
    """The Sudoku game board with validation logic."""

    rows: int = 9
    cols: int = 9
    box_size: int = 3  # Size of the 3x3 sub-boxes

    def initialize_board(self) -> None:
        """Initialize an empty 9x9 Sudoku grid."""
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)
                cell = SudokuCell(position=position)
                self.add_space(cell)

                # Connect to cells in same row, column, and box
                for r in range(self.rows):
                    for c in range(self.cols):
                        # Skip self or cells that aren't in same row, column, or box
                        if r == row and c == col:
                            continue

                        # Connect if in same row, column, or box
                        if (
                            r == row
                            or c == col
                            or (
                                r // self.box_size == row // self.box_size
                                and c // self.box_size == col // self.box_size
                            )
                        ):

                            adj_pos = GridPosition(row=r, col=c)
                            adj_cell = self.get_space_at_position(adj_pos)
                            if adj_cell:
                                self.connect_spaces(cell.id, adj_cell.id)

    def load_puzzle(self, puzzle: list[list[int]]) -> None:
        """Load a puzzle into the board.

        Args:
            puzzle: 9x9 grid with digits (0 for empty cells)
        """
        if len(puzzle) != 9 or any(len(row) != 9 for row in puzzle):
            raise ValueError("Puzzle must be a 9x9 grid")

        # Clear any existing digits
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell:
                    cell.remove_piece()

        # Set values from puzzle
        for row in range(self.rows):
            for col in range(self.cols):
                value = puzzle[row][col]
                if 1 <= value <= 9:
                    cell = self.get_space_at(row, col)
                    if cell:
                        cell.set_value(value, fixed=True)

        # Update candidates for all cells
        self.update_all_candidates()

    def get_row_values(self, row: int) -> list[int]:
        """Get all values in a row."""
        values = []
        for col in range(self.cols):
            cell = self.get_space_at(row, col)
            if cell and cell.is_occupied():
                values.append(cell.value)
        return values

    def get_column_values(self, col: int) -> list[int]:
        """Get all values in a column."""
        values = []
        for row in range(self.rows):
            cell = self.get_space_at(row, col)
            if cell and cell.is_occupied():
                values.append(cell.value)
        return values

    def get_box_values(self, box_row: int, box_col: int) -> list[int]:
        """Get all values in a 3x3 box."""
        values = []
        start_row = box_row * self.box_size
        start_col = box_col * self.box_size

        for r in range(start_row, start_row + self.box_size):
            for c in range(start_col, start_col + self.box_size):
                cell = self.get_space_at(r, c)
                if cell and cell.is_occupied():
                    values.append(cell.value)
        return values

    def is_valid_placement(self, row: int, col: int, value: int) -> bool:
        """Check if placing a value at a position would be valid."""
        # Check row
        if value in self.get_row_values(row):
            return False

        # Check column
        if value in self.get_column_values(col):
            return False

        # Check box
        box_row = row // self.box_size
        box_col = col // self.box_size
        if value in self.get_box_values(box_row, box_col):
            return False

        return True

    def update_candidates(self, row: int, col: int) -> None:
        """Update candidates for a specific cell."""
        cell = self.get_space_at(row, col)
        if not cell or cell.is_occupied():
            return

        # Collect values in row, column, and box
        invalid_values = set()
        invalid_values.update(self.get_row_values(row))
        invalid_values.update(self.get_column_values(col))

        box_row = row // self.box_size
        box_col = col // self.box_size
        invalid_values.update(self.get_box_values(box_row, box_col))

        # Update cell's candidates
        cell.update_candidates(invalid_values)

    def update_all_candidates(self) -> None:
        """Update candidates for all cells."""
        for row in range(self.rows):
            for col in range(self.cols):
                self.update_candidates(row, col)

    def set_value(self, row: int, col: int, value: int) -> bool:
        """Set a value at the specified position."""
        if not 1 <= value <= 9:
            return False

        cell = self.get_space_at(row, col)
        if not cell or cell.is_fixed():
            return False

        # Check if the placement is valid
        if not self.is_valid_placement(row, col, value):
            return False

        # Set the value
        if cell.set_value(value):
            # Update candidates for all affected cells
            self.update_candidates_for_related_cells(row, col)
            return True

        return False

    def clear_cell(self, row: int, col: int) -> bool:
        """Clear a cell at the specified position."""
        cell = self.get_space_at(row, col)
        if not cell or cell.is_fixed():
            return False

        if cell.clear():
            # Update candidates for this cell and related cells
            self.update_candidates(row, col)
            self.update_candidates_for_related_cells(row, col)
            return True

        return False

    def update_candidates_for_related_cells(self, row: int, col: int) -> None:
        """Update candidates for all cells related to the specified position."""
        # Update cells in the same row
        for c in range(self.cols):
            if c != col:
                self.update_candidates(row, c)

        # Update cells in the same column
        for r in range(self.rows):
            if r != row:
                self.update_candidates(r, col)

        # Update cells in the same box
        box_row = row // self.box_size
        box_col = col // self.box_size
        for r in range(box_row * self.box_size, (box_row + 1) * self.box_size):
            for c in range(box_col * self.box_size, (box_col + 1) * self.box_size):
                if r != row or c != col:
                    self.update_candidates(r, c)

    def is_complete(self) -> bool:
        """Check if the puzzle is complete (all cells filled)."""
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if not cell or not cell.is_occupied():
                    return False
        return True

    def is_valid(self) -> bool:
        """Check if the current board state is valid."""
        # Check rows
        for row in range(self.rows):
            values = self.get_row_values(row)
            if len(values) != len(set(values)):
                return False  # Duplicate values in row

        # Check columns
        for col in range(self.cols):
            values = self.get_column_values(col)
            if len(values) != len(set(values)):
                return False  # Duplicate values in column

        # Check boxes
        for box_row in range(3):
            for box_col in range(3):
                values = self.get_box_values(box_row, box_col)
                if len(values) != len(set(values)):
                    return False  # Duplicate values in box

        return True

    def is_solved(self) -> bool:
        """Check if the puzzle is correctly solved."""
        return self.is_complete() and self.is_valid()

    def get_puzzle_state(self) -> list[list[int]]:
        """Get the current puzzle state as a 2D array."""
        state = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell and cell.is_occupied():
                    state[row][col] = cell.value
        return state

    def get_candidates_state(self) -> dict[tuple[int, int], set[int]]:
        """Get the current candidates state."""
        state = {}
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell and not cell.is_occupied() and cell.candidates:
                    state[(row, col)] = cell.candidates
        return state

    def autosolve_step(self) -> bool:
        """Perform one step of automatic solving using basic strategies.

        Returns:
            True if a cell was filled, False otherwise
        """
        # Strategy 1: Naked Singles - cells with only one candidate
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell and not cell.is_occupied() and len(cell.candidates) == 1:
                    value = next(iter(cell.candidates))
                    if self.set_value(row, col, value):
                        return True

        # Strategy 2: Hidden Singles - only one cell in a unit can have a certain value
        # Check rows
        for row in range(self.rows):
            for value in range(1, 10):
                valid_cols = []
                for col in range(self.cols):
                    cell = self.get_space_at(row, col)
                    if cell and not cell.is_occupied() and value in cell.candidates:
                        valid_cols.append(col)
                if len(valid_cols) == 1:
                    if self.set_value(row, valid_cols[0], value):
                        return True

        # Check columns
        for col in range(self.cols):
            for value in range(1, 10):
                valid_rows = []
                for row in range(self.rows):
                    cell = self.get_space_at(row, col)
                    if cell and not cell.is_occupied() and value in cell.candidates:
                        valid_rows.append(row)
                if len(valid_rows) == 1:
                    if self.set_value(valid_rows[0], col, value):
                        return True

        # Check boxes
        for box_row in range(3):
            for box_col in range(3):
                for value in range(1, 10):
                    valid_positions = []
                    for r in range(box_row * 3, (box_row + 1) * 3):
                        for c in range(box_col * 3, (box_col + 1) * 3):
                            cell = self.get_space_at(r, c)
                            if (
                                cell
                                and not cell.is_occupied()
                                and value in cell.candidates
                            ):
                                valid_positions.append((r, c))
                    if len(valid_positions) == 1:
                        r, c = valid_positions[0]
                        if self.set_value(r, c, value):
                            return True

        return False  # No progress made
