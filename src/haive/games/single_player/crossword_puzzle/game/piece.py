"""Piece core module.

This module provides piece functionality for the Haive framework.

Classes:
    CrosswordLetter: CrosswordLetter implementation.

Functions:
    validate_letter: Validate Letter functionality.
    can_move_to: Can Move To functionality.
"""

from pydantic import field_validator

from haive.games.core.piece.base import GamePiece
from haive.games.core.position.base import GridPosition
from haive.games.single_player.crossword_puzzle.game.board import CrosswordBoard
from haive.games.single_player.crossword_puzzle.game.cell import CrosswordCell


class CrosswordLetter(GamePiece[GridPosition]):
    """A letter in a cross puzzle."""

    letter: str
    is_filled: bool = False  # Whether it's been filled by player

    @field_validator("letter")
    @classmethod
    def validate_letter(cls, v: str) -> str:
        """Ensure letter is a single uppercase character."""
        if not v.isalpha() or len(v) != 1:
            raise ValueError("Letter must be a single alphabetic character")
        return v.upper()

    def can_move_to(self, position: GridPosition, board: "CrosswordBoard") -> bool:
        """Check if this letter can be placed at this position."""
        space = board.get_space_at_position(position)
        if not space:
            return False

        # Can only place on empty letter cells
        if not isinstance(space, CrosswordCell) or space.cell_type != "letter":
            return False

        # If space has a letter, it must match
        if space.is_occupied():
            existing_letter = space.piece
            if (
                isinstance(existing_letter, CrosswordLetter)
                and existing_letter.letter != self.letter
            ):
                return False

        return True
