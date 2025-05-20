from __future__ import annotations

import math
import random
import uuid
from collections import Counter, defaultdict
from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union

# Import base framework classes
from game_framework_base import GamePiece, GridBoard, GridPosition, GridSpace
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator


class Difficulty(str, Enum):
    """Difficulty levels for Sudoku."""

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


class SudokuGame(BaseModel):
    """Model for managing a Sudoku game."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    board: SudokuBoard
    difficulty: Difficulty = Difficulty.EASY
    original_puzzle: List[List[int]] = Field(
        default_factory=lambda: [[0 for _ in range(9)] for _ in range(9)]
    )
    moves: List[Dict[str, Any]] = Field(default_factory=list)
    hint_count: int = 0
    show_candidates: bool = True
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    solved: bool = False

    @model_validator(mode="after")
    def validate_game(self) -> "SudokuGame":
        """Ensure game has valid components."""
        # Initialize board if not done already
        if self.board and not self.board.spaces:
            self.board.initialize_board()
        return self

    @classmethod
    def new_game(
        cls,
        difficulty: Difficulty = Difficulty.EASY,
        puzzle: Optional[List[List[int]]] = None,
    ) -> "SudokuGame":
        """Create a new Sudoku game with the specified difficulty."""
        # Create board
        board = SudokuBoard(name="Sudoku Board")
        board.initialize_board()

        # Create game
        game = cls(board=board, difficulty=difficulty)

        # Load puzzle if provided, otherwise generate one
        if puzzle:
            game.original_puzzle = [row[:] for row in puzzle]  # Deep copy
            board.load_puzzle(puzzle)
        else:
            # In a real implementation, we would generate a puzzle based on difficulty
            # Here, we'll provide a simple built-in puzzle for demonstration
            game.original_puzzle = game._get_sample_puzzle(difficulty)
            board.load_puzzle(game.original_puzzle)

        # Set start time
        import time

        game.start_time = time.time()

        return game

    def _get_sample_puzzle(self, difficulty: Difficulty) -> List[List[int]]:
        """Get a sample puzzle for the specified difficulty."""
        # These are just examples; a real implementation would have many puzzles
        # or generate them dynamically
        puzzles = {
            Difficulty.EASY: [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9],
            ],
            Difficulty.MEDIUM: [
                [0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0],
            ],
            Difficulty.HARD: [
                [0, 0, 0, 6, 0, 0, 4, 0, 0],
                [7, 0, 0, 0, 0, 3, 6, 0, 0],
                [0, 0, 0, 0, 9, 1, 0, 8, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 5, 0, 1, 8, 0, 0, 0, 3],
                [0, 0, 0, 3, 0, 6, 0, 4, 5],
                [0, 4, 0, 2, 0, 0, 0, 6, 0],
                [9, 0, 3, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 1, 0, 0],
            ],
            Difficulty.EXPERT: [
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 6, 0, 0, 0, 0, 3],
                [0, 7, 4, 0, 8, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 3, 0, 0, 2],
                [0, 8, 0, 0, 4, 0, 0, 1, 0],
                [6, 0, 0, 5, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 7, 8, 0],
                [5, 0, 0, 0, 0, 9, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 4, 0],
            ],
        }

        return puzzles.get(difficulty, puzzles[Difficulty.EASY])

    def make_move(self, row: int, col: int, value: int) -> bool:
        """
        Make a move by placing a value in a cell.

        Args:
            row: Row to place value
            col: Column to place value
            value: Value to place (1-9, or 0 to clear)

        Returns:
            True if successful, False otherwise
        """
        if self.solved:
            return False

        if value == 0:
            # Clear the cell
            success = self.board.clear_cell(row, col)
        else:
            # Set a value
            success = self.board.set_value(row, col, value)

        if success:
            # Record the move
            self.moves.append(
                {
                    "type": "set" if value > 0 else "clear",
                    "row": row,
                    "col": col,
                    "value": value,
                }
            )

            # Check if the puzzle is solved
            if self.board.is_solved():
                self.solved = True

                # Set end time
                import time

                self.end_time = time.time()

        return success

    def get_hint(self) -> Optional[Tuple[int, int, int]]:
        """
        Get a hint for the next move.

        Returns:
            Tuple of (row, col, value) if a hint is available, None otherwise
        """
        # Try to solve one step
        if self.board.autosolve_step():
            self.hint_count += 1

            # Find the changed cell
            for row in range(9):
                for col in range(9):
                    cell = self.board.get_space_at(row, col)
                    if cell and cell.is_occupied() and not cell.is_fixed():
                        # Check if this cell was just filled
                        is_new = True
                        for move in reversed(self.moves):
                            if move["row"] == row and move["col"] == col:
                                is_new = False
                                break

                        if is_new:
                            # Record the hint move
                            self.moves.append(
                                {
                                    "type": "hint",
                                    "row": row,
                                    "col": col,
                                    "value": cell.value,
                                }
                            )

                            # Check if the puzzle is solved
                            if self.board.is_solved():
                                self.solved = True

                                # Set end time
                                import time

                                self.end_time = time.time()

                            return (row, col, cell.value)

        return None

    def toggle_candidates(self) -> None:
        """Toggle whether to show candidates."""
        self.show_candidates = not self.show_candidates

    def restart(self) -> None:
        """Restart the game with the same puzzle."""
        # Reload the original puzzle
        self.board.load_puzzle(self.original_puzzle)

        # Reset game state
        self.moves = []
        self.hint_count = 0
        self.solved = False

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

    def get_status(self) -> Dict[str, Any]:
        """Get the current game status."""
        candidates = {}
        if self.show_candidates:
            candidates = self.board.get_candidates_state()

        return {
            "difficulty": self.difficulty,
            "moves": len(self.moves),
            "hint_count": self.hint_count,
            "elapsed_time": self.get_elapsed_time(),
            "solved": self.solved,
            "board": self.board.get_puzzle_state(),
            "candidates": candidates,
            "show_candidates": self.show_candidates,
        }

    def undo_move(self) -> bool:
        """
        Undo the last move.

        Returns:
            True if successful, False if no moves to undo
        """
        if not self.moves:
            return False

        # Remove last move from history
        last_move = self.moves.pop()

        # Set the cell back to its previous state
        row, col = last_move["row"], last_move["col"]

        # Find the previous value for this cell
        prev_value = 0  # Default to empty
        for move in reversed(self.moves):
            if move["row"] == row and move["col"] == col:
                prev_value = move["value"]
                break

        # Apply the previous state
        if prev_value == 0:
            self.board.clear_cell(row, col)
        else:
            self.board.set_value(row, col, prev_value)

        # Update all candidates
        self.board.update_all_candidates()

        # Reset solved state
        self.solved = False
        self.end_time = None

        return True

    def __str__(self) -> str:
        """String representation of the game."""
        result = []
        result.append(
            f"Sudoku ({self.difficulty.value}) - "
            f"Moves: {len(self.moves)}, Hints: {self.hint_count}"
        )
        result.append(f"Time: {self.get_elapsed_time()} seconds")

        # Board representation
        for row in range(9):
            if row % 3 == 0 and row > 0:
                result.append("-" * 25)  # Horizontal divider

            row_str = ""
            for col in range(9):
                if col % 3 == 0 and col > 0:
                    row_str += "| "  # Vertical divider

                cell = self.board.get_space_at(row, col)
                if cell and cell.is_occupied():
                    # Bold for fixed values
                    value = cell.value
                    if cell.is_fixed():
                        row_str += f"{value} "
                    else:
                        row_str += f"{value} "
                else:
                    row_str += ". "
            result.append(row_str)

        if self.solved:
            result.append("Congratulations! You solved the puzzle!")

        return "\n".join(result)
