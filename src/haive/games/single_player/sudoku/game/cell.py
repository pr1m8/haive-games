from typing import Optional, Set

from pydantic import Field, computed_field

from haive.games.core.position.base import GridSpace
from haive.games.single_player.sudoku.game.piece import SudokuDigit


class SudokuCell(GridSpace[SudokuDigit]):
    """A cell in the Sudoku grid."""

    # Track candidate digits for solving assistance
    candidates: Set[int] = Field(default_factory=lambda: set(range(1, 10)))

    @computed_field
    @property
    def value(self) -> Optional[int]:
        """Get the current value of this cell."""
        return self.piece.value if self.is_occupied() else None

    @computed_field
    @property
    def is_fixed(self) -> bool:
        """Check if this cell has a fixed value."""
        return self.is_occupied() and self.piece.fixed

    def place_digit(self, digit: SudokuDigit) -> bool:
        """Place a digit in this cell."""
        if self.is_fixed():
            return False  # Can't change fixed cells

        success = super().place_piece(digit)
        if success:
            # Update digit's position
            digit.position = self.position
            # Clear candidates when a digit is placed
            self.candidates = set()
        return success

    def set_value(self, value: int, fixed: bool = False) -> bool:
        """Set a value in this cell."""
        if self.is_fixed():
            return False  # Can't change fixed cells

        # Remove existing digit if any
        self.remove_piece()

        # Create new digit
        digit = SudokuDigit(value=value, fixed=fixed)
        return self.place_digit(digit)

    def clear(self) -> bool:
        """Clear this cell."""
        if self.is_fixed():
            return False  # Can't clear fixed cells

        if self.is_occupied():
            self.remove_piece()
            # Reset candidates
            self.candidates = set(range(1, 10))
            return True
        return False

    def update_candidates(self, invalid_values: Set[int]) -> None:
        """Update candidate values by removing invalid options."""
        if self.is_occupied():
            self.candidates = set()  # No candidates for filled cells
        else:
            self.candidates = {n for n in range(1, 10) if n not in invalid_values}
