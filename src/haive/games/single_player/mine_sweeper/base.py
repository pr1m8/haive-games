from __future__ import annotations

"""Base core module.

This module provides base functionality for the Haive framework.

Classes:
    CellState: CellState implementation.
    MinePiece: MinePiece implementation.
    MinesweeperCell: MinesweeperCell implementation.

Functions:
    can_move_to: Can Move To functionality.
    place_mine: Place Mine functionality.
"""


import random
import uuid
from collections import deque
from enum import Enum

# Import base framework classes
from game_framework_base import GamePiece, GridBoard, GridPosition, GridSpace
from pydantic import BaseModel, Field, model_validator

# ======================================================
# MINESWEEPER COMPONENTS
# ======================================================


class CellState(str, Enum):
    """Possible states of a Minesweeper cell."""

    HIDDEN = "hidden"  # Initial state, not revealed yet
    REVEALED = "revealed"  # Cell has been revealed
    FLAGGED = "flagged"  # Player has flagged as potential mine
    QUESTIONED = "questioned"  # Player has marked with question mark


class MinePiece(GamePiece[GridPosition]):
    """Represents a mine in Minesweeper."""

    def can_move_to(self, position: GridPosition, board: Board) -> bool:
        """Mines can't move in Minesweeper."""
        return False

    def __str__(self) -> str:
        """String representation of a mine."""
        return "*"


class MinesweeperCell(GridSpace[MinePiece]):
    """A cell in the Minesweeper grid."""

    has_mine: bool = False
    state: CellState = CellState.HIDDEN
    adjacent_mines: int = 0

    def place_mine(self) -> None:
        """Place a mine in this cell."""
        self.has_mine = True
        # Create a mine piece for consistency
        self.piece = MinePiece()

    def is_mine(self) -> bool:
        """Check if this cell contains a mine."""
        return self.has_mine

    def is_revealed(self) -> bool:
        """Check if this cell has been revealed."""
        return self.state == CellState.REVEALED

    def is_flagged(self) -> bool:
        """Check if this cell has been flagged."""
        return self.state == CellState.FLAGGED

    def is_questioned(self) -> bool:
        """Check if this cell has been marked with a question."""
        return self.state == CellState.QUESTIONED

    def reveal(self) -> bool:
        """Reveal this cell.

        Returns:
            True if it's a mine (game over), False otherwise
        """
        if self.state != CellState.HIDDEN:
            return False  # Already revealed or flagged

        self.state = CellState.REVEALED
        return self.has_mine

    def toggle_flag(self) -> CellState:
        """Toggle flag state: hidden -> flagged -> questioned -> hidden.

        Returns:
            The new state
        """
        if self.state == CellState.REVEALED:
            return self.state  # Can't flag revealed cells

        # Cycle through states: HIDDEN -> FLAGGED -> QUESTIONED -> HIDDEN
        if self.state == CellState.HIDDEN:
            self.state = CellState.FLAGGED
        elif self.state == CellState.FLAGGED:
            self.state = CellState.QUESTIONED
        elif self.state == CellState.QUESTIONED:
            self.state = CellState.HIDDEN

        return self.state

    def set_adjacent_mines(self, count: int) -> None:
        """Set the number of adjacent mines."""
        self.adjacent_mines = count

    def get_display_value(self) -> str:
        """Get the display value for this cell based on its state."""
        if self.state == CellState.HIDDEN:
            return "·"  # Hidden cell
        if self.state == CellState.FLAGGED:
            return "F"  # Flagged cell
        if self.state == CellState.QUESTIONED:
            return "?"  # Questioned cell
        if self.has_mine:
            return "*"  # Mine
        if self.adjacent_mines == 0:
            return " "  # Empty cell
        return str(self.adjacent_mines)  # Number of adjacent mines


class Difficulty(str, Enum):
    """Difficulty levels for Minesweeper."""

    BEGINNER = "beginner"  # 9x9 grid, 10 mines
    INTERMEDIATE = "intermediate"  # 16x16 grid, 40 mines
    EXPERT = "expert"  # 30x16 grid, 99 mines
    CUSTOM = "custom"  # Custom dimensions and mine count


class MinesweeperBoard(GridBoard[MinesweeperCell, GridPosition, MinePiece]):
    """The Minesweeper game board."""

    revealed_count: int = 0
    flagged_count: int = 0
    total_mines: int = 0
    first_move_made: bool = False

    # Constants for difficulty levels
    DIFFICULTY_SETTINGS = {
        Difficulty.BEGINNER: {"rows": 9, "cols": 9, "mines": 10},
        Difficulty.INTERMEDIATE: {"rows": 16, "cols": 16, "mines": 40},
        Difficulty.EXPERT: {"rows": 16, "cols": 30, "mines": 99},
    }

    def initialize_board(
        self,
        difficulty: Difficulty = Difficulty.BEGINNER,
        custom_rows: int | None = None,
        custom_cols: int | None = None,
        custom_mines: int | None = None,
    ) -> None:
        """Initialize the Minesweeper board based on difficulty."""
        # Set dimensions and mine count based on difficulty
        if difficulty == Difficulty.CUSTOM:
            if custom_rows is None or custom_cols is None or custom_mines is None:
                raise ValueError("Custom difficulty requires rows, cols, and mines")
            self.rows = custom_rows
            self.cols = custom_cols
            self.total_mines = custom_mines
        else:
            settings = self.DIFFICULTY_SETTINGS[difficulty]
            self.rows = settings["rows"]
            self.cols = settings["cols"]
            self.total_mines = settings["mines"]

        # Sanity check on mine count
        max_mines = (
            self.rows * self.cols - 9
        )  # Ensuring first click has 8 safe neighbors + itself
        if self.total_mines > max_mines:
            raise ValueError(f"Too many mines for grid size. Maximum is {max_mines}")

        # Create empty grid
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)
                cell = MinesweeperCell(position=position)
                self.add_space(cell)

                # Connect cells (including diagonals for Minesweeper)
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue  # Skip self

                        adj_row, adj_col = row + dr, col + dc
                        if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                            adj_cell = self.get_space_at(adj_row, adj_col)
                            if adj_cell:
                                self.connect_spaces(cell.id, adj_cell.id)

        # Reset counters
        self.revealed_count = 0
        self.flagged_count = 0
        self.first_move_made = False

    def place_mines(self, first_click_row: int, first_click_col: int) -> None:
        """Place mines randomly, ensuring the first click is safe.

        Args:
            first_click_row: Row of first click
            first_click_col: Column of first click
        """
        # Determine safe cells (first click and its 8 neighbors)
        safe_cells = set()
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                r, c = first_click_row + dr, first_click_col + dc
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    safe_cells.add((r, c))

        # Get all possible mine positions (excluding safe cells)
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        valid_positions = [pos for pos in all_positions if pos not in safe_cells]

        # Ensure we have enough valid positions
        if len(valid_positions) < self.total_mines:
            raise ValueError("Not enough valid positions for mines")

        # Place mines randomly
        mine_positions = random.sample(valid_positions, self.total_mines)
        for row, col in mine_positions:
            cell = self.get_space_at(row, col)
            if cell:
                cell.place_mine()

        # Calculate adjacent mines for all cells
        self._calculate_adjacent_mines()

        # Mark first move as made
        self.first_move_made = True

    def _calculate_adjacent_mines(self) -> None:
        """Calculate the number of adjacent mines for each cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell and not cell.is_mine():
                    # Count adjacent mines
                    adjacent_mines = 0
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if dr == 0 and dc == 0:
                                continue  # Skip self

                            adj_row, adj_col = row + dr, col + dc
                            if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                                adj_cell = self.get_space_at(adj_row, adj_col)
                                if adj_cell and adj_cell.is_mine():
                                    adjacent_mines += 1

                    cell.set_adjacent_mines(adjacent_mines)

    def reveal_cell(self, row: int, col: int) -> tuple[bool, int]:
        """Reveal a cell at the specified position.

        Args:
            row: Row to reveal
            col: Column to reveal

        Returns:
            Tuple of (hit_mine, cells_revealed)
        """
        # Check if it's the first move
        if not self.first_move_made:
            self.place_mines(row, col)

        cell = self.get_space_at(row, col)
        if not cell or cell.is_revealed() or cell.is_flagged():
            return False, 0  # Cell already revealed or flagged

        # Reveal the cell
        hit_mine = cell.reveal()
        revealed_count = 1
        self.revealed_count += 1

        # If it's a mine, game over
        if hit_mine:
            return True, revealed_count

        # If it's an empty cell (0 adjacent mines), reveal neighbors recursively
        if cell.adjacent_mines == 0:
            # Use breadth-first search to reveal connected empty cells
            queue = deque([(row, col)])
            visited = {(row, col)}

            while queue:
                r, c = queue.popleft()

                # Check all 8 adjacent cells
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue  # Skip self

                        adj_row, adj_col = r + dr, c + dc
                        if (adj_row, adj_col) in visited:
                            continue

                        if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                            adj_cell = self.get_space_at(adj_row, adj_col)
                            if (
                                adj_cell
                                and not adj_cell.is_revealed()
                                and not adj_cell.is_flagged()
                            ):
                                adj_cell.reveal()
                                self.revealed_count += 1
                                revealed_count += 1
                                visited.add((adj_row, adj_col))

                                # If it's also an empty cell, add to queue
                                if adj_cell.adjacent_mines == 0:
                                    queue.append((adj_row, adj_col))

        return hit_mine, revealed_count

    def toggle_flag(self, row: int, col: int) -> bool:
        """Toggle the flag state of a cell.

        Args:
            row: Row to toggle
            col: Column to toggle

        Returns:
            True if flag was placed, False if removed or state is questioned
        """
        cell = self.get_space_at(row, col)
        if not cell or cell.is_revealed():
            return False  # Can't flag revealed cells

        previous_state = cell.state
        new_state = cell.toggle_flag()

        # Update flag count
        if previous_state == CellState.FLAGGED:
            self.flagged_count -= 1
        if new_state == CellState.FLAGGED:
            self.flagged_count += 1

        return new_state == CellState.FLAGGED

    def chord(self, row: int, col: int) -> tuple[bool, int]:
        """Perform a chord (middle-click) to reveal all unflagged neighbors.
        Only works if the number of flagged neighbors equals the cell's value.

        Args:
            row: Row to chord
            col: Column to chord

        Returns:
            Tuple of (hit_mine, cells_revealed)
        """
        cell = self.get_space_at(row, col)
        if not cell or not cell.is_revealed() or cell.adjacent_mines == 0:
            return False, 0  # Can't chord on unrevealed or 0-value cells

        # Count flagged neighbors
        flagged_neighbors = 0
        neighbors = []
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue  # Skip self

                adj_row, adj_col = row + dr, col + dc
                if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                    adj_cell = self.get_space_at(adj_row, adj_col)
                    if adj_cell:
                        if adj_cell.is_flagged():
                            flagged_neighbors += 1
                        elif not adj_cell.is_revealed():
                            neighbors.append((adj_row, adj_col))

        # If flagged neighbors equals the cell's value, reveal all unflagged neighbors
        if flagged_neighbors == cell.adjacent_mines:
            hit_mine = False
            revealed_count = 0

            for adj_row, adj_col in neighbors:
                mine_hit, cells_revealed = self.reveal_cell(adj_row, adj_col)
                hit_mine = hit_mine or mine_hit
                revealed_count += cells_revealed

                if hit_mine:
                    break  # Game over if a mine is hit

            return hit_mine, revealed_count

        return False, 0  # No action taken

    def is_game_won(self) -> bool:
        """Check if the game has been won (all non-mine cells revealed)."""
        total_cells = self.rows * self.cols
        return self.revealed_count == total_cells - self.total_mines

    def get_board_state(self) -> list[list[str]]:
        """Get the current visible board state as a 2D array."""
        state = [["" for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell:
                    state[row][col] = cell.get_display_value()
        return state

    def get_mine_locations(self) -> list[tuple[int, int]]:
        """Get the locations of all mines."""
        mines = []
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell and cell.is_mine():
                    mines.append((row, col))
        return mines

    def reveal_all_mines(self) -> None:
        """Reveal all mines (for game over)."""
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.get_space_at(row, col)
                if cell and cell.is_mine():
                    cell.reveal()

    def get_remaining_mines(self) -> int:
        """Get the number of unflagged mines (for display)."""
        return self.total_mines - self.flagged_count


class MinesweeperGame(BaseModel):
    """Model for managing a Minesweeper game."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    board: MinesweeperBoard
    difficulty: Difficulty = Difficulty.BEGINNER
    game_over: bool = False
    win: bool = False
    start_time: float | None = None
    end_time: float | None = None

    @model_validator(mode="after")
    @classmethod
    def validate_game(cls) -> MinesweeperGame:
        """Ensure game has valid components."""
        return self

    @classmethod
    def new_game(
        cls,
        difficulty: Difficulty = Difficulty.BEGINNER,
        custom_rows: int | None = None,
        custom_cols: int | None = None,
        custom_mines: int | None = None,
    ) -> MinesweeperGame:
        """Create a new Minesweeper game with the specified difficulty."""
        # Create board
        board = MinesweeperBoard(name="Minesweeper Board")
        board.initialize_board(
            difficulty=difficulty,
            custom_rows=custom_rows,
            custom_cols=custom_cols,
            custom_mines=custom_mines,
        )

        # Create game
        game = cls(board=board, difficulty=difficulty)

        # Set start time
        import time

        game.start_time = time.time()

        return game

    def make_move(self, row: int, col: int) -> tuple[bool, bool, int]:
        """Make a move by revealing a cell.

        Args:
            row: Row to reveal
            col: Column to reveal

        Returns:
            Tuple of (success, hit_mine, cells_revealed)
        """
        if self.game_over:
            return False, False, 0

        # Reveal the cell
        hit_mine, cells_revealed = self.board.reveal_cell(row, col)

        # Check for game over
        if hit_mine:
            self.game_over = True
            self.board.reveal_all_mines()

            # Set end time
            import time

            self.end_time = time.time()

            return True, True, cells_revealed

        # Check for win
        if self.board.is_game_won():
            self.game_over = True
            self.win = True

            # Set end time
            import time

            self.end_time = time.time()

        return True, False, cells_revealed

    def toggle_flag(self, row: int, col: int) -> bool:
        """Toggle flag on a cell.

        Args:
            row: Row to toggle
            col: Column to toggle

        Returns:
            True if successful, False otherwise
        """
        if self.game_over:
            return False

        return self.board.toggle_flag(row, col)

    def chord(self, row: int, col: int) -> tuple[bool, bool, int]:
        """Perform a chord action.

        Args:
            row: Row to chord
            col: Column to chord

        Returns:
            Tuple of (success, hit_mine, cells_revealed)
        """
        if self.game_over:
            return False, False, 0

        hit_mine, cells_revealed = self.board.chord(row, col)

        # Check for game over
        if hit_mine:
            self.game_over = True
            self.board.reveal_all_mines()

            # Set end time
            import time

            self.end_time = time.time()

            return True, True, cells_revealed

        # Check for win
        if self.board.is_game_won():
            self.game_over = True
            self.win = True

            # Set end time
            import time

            self.end_time = time.time()

        return True, False, cells_revealed

    def restart(self) -> None:
        """Restart the game with the same settings."""
        # Reinitialize board with same settings
        self.board.initialize_board(
            difficulty=self.difficulty,
            custom_rows=(
                self.board.rows if self.difficulty == Difficulty.CUSTOM else None
            ),
            custom_cols=(
                self.board.cols if self.difficulty == Difficulty.CUSTOM else None
            ),
            custom_mines=(
                self.board.total_mines if self.difficulty == Difficulty.CUSTOM else None
            ),
        )

        # Reset game state
        self.game_over = False
        self.win = False

        # Reset times
        import time

        self.start_time = time.time()
        self.end_time = None

    def get_elapsed_time(self) -> int:
        """Get the elapsed time in seconds."""
        import time

        if self.start_time is None:
            return 0

        end = self.end_time if self.end_time is not None else time.time()
        return int(end - self.start_time)

    def get_status(self) -> dict[str, Any]:
        """Get the current game status."""
        return {
            "difficulty": self.difficulty,
            "rows": self.board.rows,
            "cols": self.board.cols,
            "total_mines": self.board.total_mines,
            "remaining_mines": self.board.get_remaining_mines(),
            "revealed_count": self.board.revealed_count,
            "flagged_count": self.board.flagged_count,
            "game_over": self.game_over,
            "win": self.win,
            "elapsed_time": self.get_elapsed_time(),
            "board": self.board.get_board_state(),
        }

    def __str__(self) -> str:
        """String representation of the game."""
        result = []
        result.append(
            f"Minesweeper ({self.difficulty.value}) - "
            f"Mines remaining: {self.board.get_remaining_mines()}"
        )
        result.append(f"Time: {self.get_elapsed_time()} seconds")

        # Board representation
        for row in range(self.board.rows):
            row_str = []
            for col in range(self.board.cols):
                cell = self.board.get_space_at(row, col)
                if cell:
                    row_str.append(cell.get_display_value())
            result.append("|" + "|".join(row_str) + "|")

        if self.win:
            result.append("Congratulations! You won!")
        elif self.game_over:
            result.append("Game Over! You hit a mine!")

        return "\n".join(result)
