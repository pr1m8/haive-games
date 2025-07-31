# ======================================================
# SUDOKU COMPONENTS
# ======================================================

from pydantic import Field, field_validator

from haive.games.core.piece.base import GamePiece
from haive.games.core.position.base import GridPosition


class SudokuDigit(GamePiece[GridPosition]):
    """A digit in a Sudoku puzzle."""

    value: int = Field(le=9, ge=1, description="The value of the digit")
    fixed: bool = False  # Whether this is part of the initial puzzle

    # Unsure if this is neeeded due to the above
    @field_validator("value")
    @classmethod
    def validate_value(cls, v: int) -> int:
        """Ensure value is between 1 and 9."""
        if not 1 <= v <= 9:
            raise ValueError("Sudoku digits must be between 1 and 9")
        return v

    def can_move_to(self, position: GridPosition, board: "Board") -> bool:
        """Check if this digit can be placed at the specified position."""
        if self.fixed:
            return False  # Fixed digits can't be moved

        space = board.get_space_at_position(position)
        if not space:
            return False

        # Can place in empty cell
        if not space.is_occupied():
            return True

        return False

    def __str__(self) -> str:
        """String representation of the digit."""
        return str(self.value)
