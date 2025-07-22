from __future__ import annotations

import uuid
from enum import Enum
from typing import (
    Literal,
)

# Import from our base framework
from game_framework_base import (
    Game,
    GridPosition,
    GridSpace,
)
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator

# ======================================================
# CROSSWORD TYPES AND CONSTANTS
# ======================================================


class Direction(str, Enum):
    """Direction of a word in a crossword."""

    ACROSS = "across"
    DOWN = "down"


CellType = Literal["letter", "block", "empty"]

# ======================================================
# CROSSWORD POSITIONS AND PIECES
# ======================================================


# ======================================================
# CROSSWORD SPACES
# ======================================================


class CrosswordCell(GridSpace[CrosswordLetter]):
    """A cell in a crossword puzzle."""

    cell_type: CellType = "empty"
    number: int | None = None  # Clue number, if any

    @computed_field
    @property
    def is_block(self) -> bool:
        """Check if this cell is a block (black square)."""
        return self.cell_type == "block"

    @computed_field
    @property
    def is_letter_cell(self) -> bool:
        """Check if this cell can contain a letter."""
        return self.cell_type == "letter"

    @computed_field
    @property
    def current_letter(self) -> str | None:
        """Get the current letter in this cell, if any."""
        if self.is_occupied() and isinstance(self.piece, CrosswordLetter):
            return self.piece.letter
        return None

    @computed_field
    @property
    def is_filled(self) -> bool:
        """Check if this cell has been filled by the player."""
        if self.is_occupied() and isinstance(self.piece, CrosswordLetter):
            return self.piece.is_filled
        return False


# ======================================================
# CROSSWORD CLUE AND WORD
# ======================================================


class CrosswordClue(BaseModel):
    """A clue in a crossword puzzle."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    number: int
    direction: Direction
    text: str
    answer: str
    start_position: GridPosition
    length: int

    @field_validator("answer")
    @classmethod
    def validate_answer(cls, v: str) -> str:
        """Ensure answer contains only letters and matches the length."""
        if not v.isalpha():
            raise ValueError("Answer must contain only letters")
        return v.upper()

    @computed_field
    @property
    def end_position(self) -> GridPosition:
        """Calculate the ending position of the word."""
        if self.direction == Direction.ACROSS:
            return GridPosition(
                row=self.start_position.row,
                col=self.start_position.col + self.length - 1,
            )
        # DOWN
        return GridPosition(
            row=self.start_position.row + self.length - 1,
            col=self.start_position.col,
        )


class CrosswordWord(BaseModel):
    """A word placement in a crossword puzzle."""

    clue: CrosswordClue
    positions: list[GridPosition]  # Positions of each letter
    letters: list[str]  # Letters of the word

    @model_validator(mode="after")
    @classmethod
    def validate_word(cls) -> CrosswordWord:
        """Ensure the word's length matches positions and letters."""
        if (
            len(self.positions) != len(self.letters)
            or len(self.positions) != self.clue.length
        ):
            raise ValueError("Word length must match positions and clue length")

        # Ensure all letters are uppercase
        self.letters = [letter.upper() for letter in self.letters]

        return self


# ======================================================
# CROSSWORD BOARD
# ======================================================


class CrosswordMove(BaseModel):
    """A move in a crossword puzzle."""

    position: GridPosition
    letter: str


class CrosswordGame(Game[GridPosition, CrosswordLetter]):
    """Crossword puzzle game controller."""

    board: CrosswordBoard
    selected_position: GridPosition | None = None
    check_as_you_type: bool = False

    def start_game(self) -> None:
        """Start the game."""
        super().start_game()
        self.board.initialize_grid()

    def is_valid_move(self, move: CrosswordMove | dict[str, any]) -> bool:
        """Check if a move is valid."""
        # Convert dict to CrosswordMove if needed
        if isinstance(move, dict):
            try:
                move = CrosswordMove(
                    position=GridPosition(
                        row=move["position"]["row"], col=move["position"]["col"]
                    ),
                    letter=move["letter"],
                )
            except (KeyError, ValueError):
                return False

        # Check if position is valid
        cell = self.board.get_space_at_position(move.position)
        if not cell or not cell.is_letter_cell:
            return False

        # Letter must be alphabetic
        return not (not move.letter.isalpha() or len(move.letter) != 1)

    def make_move(self, move: CrosswordMove | dict[str, any]) -> bool:
        """Make a move in the game."""
        if self.status != "in_progress":
            return False

        # Convert dict to CrosswordMove if needed
        if isinstance(move, dict):
            try:
                move = CrosswordMove(
                    position=GridPosition(
                        row=move["position"]["row"], col=move["position"]["col"]
                    ),
                    letter=move["letter"],
                )
            except (KeyError, ValueError):
                return False

        if not self.is_valid_move(move):
            return False

        # Enter the letter
        result = self.board.enter_letter(move.position, move.letter)

        if result:
            # Record the move
            self.moves.append(move.model_dump())

            # Set selected position to the next cell if appropriate
            if self.selected_position is not None:
                # Calculate next position based on typical typing behavior
                # Default to moving right (ACROSS mode)
                next_row, next_col = move.position.row, move.position.col + 1

                # If at edge, move to next row
                if next_col >= self.board.cols:
                    next_row += 1
                    next_col = 0

                # If still in bounds, select next cell
                if next_row < self.board.rows:
                    next_position = GridPosition(row=next_row, col=next_col)
                    next_cell = self.board.get_space_at_position(next_position)
                    if next_cell and next_cell.is_letter_cell:
                        self.selected_position = next_position

            # Check for completion
            if self.board.is_complete:
                self.status = "completed"

        return result

    def select_cell(self, position: GridPosition) -> bool:
        """Select a cell."""
        cell = self.board.get_space_at_position(position)
        if not cell or not cell.is_letter_cell:
            return False

        self.selected_position = position
        return True

    def check_word(self, clue_id: str) -> bool:
        """Check if a word is filled in correctly."""
        if clue_id not in self.board.words:
            return False

        word = self.board.words[clue_id]

        # Check each letter
        return all(
            self.board.check_letter(pos) for _i, pos in enumerate(word.positions)
        )

    def check_all(self) -> dict[str, bool]:
        """Check all filled letters against the solution."""
        results = {}

        for clue_id, _word in self.board.words.items():
            results[clue_id] = self.check_word(clue_id)

        return results

    def reveal_letter(self, position: GridPosition) -> bool:
        """Reveal the correct letter at a position."""
        cell = self.board.get_space_at_position(position)
        if not cell or not cell.is_letter_cell:
            return False

        # Find the correct letter
        correct_letter = None
        for word in self.board.words.values():
            try:
                idx = word.positions.index(position)
                correct_letter = word.letters[idx]
                break
            except ValueError:
                continue

        if not correct_letter:
            return False

        # Enter the correct letter, but mark it as not filled by the player
        return self.board.enter_letter(position, correct_letter, is_filled=False)

    def reveal_word(self, clue_id: str) -> bool:
        """Reveal all letters in a word."""
        if clue_id not in self.board.words:
            return False

        word = self.board.words[clue_id]

        # Reveal each letter
        for i, pos in enumerate(word.positions):
            self.board.enter_letter(pos, word.letters[i], is_filled=False)

        return True

    def reset(self) -> None:
        """Reset the game."""
        super().reset()

        # Remove all letters but keep the grid structure
        for space in self.board.spaces.values():
            if (
                isinstance(space, CrosswordCell)
                and space.is_letter_cell
                and space.is_occupied()
            ):
                space.remove_piece()

        self.selected_position = None


# ======================================================
# CROSSWORD GENERATOR
# ======================================================


class CrosswordTemplate(BaseModel):
    """A pre-defined crossword template."""

    name: str
    rows: int
    cols: int
    block_positions: list[tuple[int, int]]  # (row, col) for each black cell
    clues: list[dict[str, any]]  # Clue definitions

    def create_game(self) -> CrosswordGame:
        """Create a game from this template."""
        # Create the board
        board = CrosswordBoard(name=self.name, rows=self.rows, cols=self.cols)
        board.initialize_grid()

        # Set block positions
        for row, col in self.block_positions:
            board.set_cell_type(GridPosition(row=row, col=col), "block")

        # Create the game
        game = CrosswordGame(name=self.name, board=board)
        game.start_game()

        # Add clues
        for clue_data in self.clues:
            start_pos = GridPosition(
                row=clue_data["start_row"], col=clue_data["start_col"]
            )

            board.add_clue(
                number=clue_data["number"],
                direction=clue_data["direction"],
                text=clue_data["text"],
                answer=clue_data["answer"],
                start_position=start_pos,
            )

        return game
