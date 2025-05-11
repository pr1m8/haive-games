from __future__ import annotations

import random
import re
import uuid
from collections import defaultdict
from enum import Enum, auto
from typing import (
    Annotated,
    ClassVar,
    Dict,
    FrozenSet,
    List,
    Literal,
    Optional,
    Set,
    Tuple,
    Union,
)

# Import from our base framework
from game_framework_base import (
    Board,
    Game,
    GamePiece,
    GridBoard,
    GridPosition,
    GridSpace,
    Position,
    Space,
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


class CrosswordLetter(GamePiece[GridPosition]):
    """A letter in a crossword puzzle."""

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


# ======================================================
# CROSSWORD SPACES
# ======================================================


class CrosswordCell(GridSpace[CrosswordLetter]):
    """A cell in a crossword puzzle."""

    cell_type: CellType = "empty"
    number: Optional[int] = None  # Clue number, if any

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
    def current_letter(self) -> Optional[str]:
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
        else:  # DOWN
            return GridPosition(
                row=self.start_position.row + self.length - 1,
                col=self.start_position.col,
            )


class CrosswordWord(BaseModel):
    """A word placement in a crossword puzzle."""

    clue: CrosswordClue
    positions: List[GridPosition]  # Positions of each letter
    letters: List[str]  # Letters of the word

    @model_validator(mode="after")
    def validate_word(self) -> "CrosswordWord":
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


class CrosswordBoard(
    GridBoard[CrosswordCell[CrosswordLetter], GridPosition, CrosswordLetter]
):
    """A crossword puzzle board."""

    words: Dict[str, CrosswordWord] = Field(default_factory=dict)
    clues: Dict[str, CrosswordClue] = Field(default_factory=dict)

    def initialize_grid(self) -> None:
        """Initialize an empty crossword grid."""
        # Create empty cells for each position
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)
                cell = CrosswordCell[CrosswordLetter](position=position)
                self.add_space(cell)

                # Connect to adjacent cells
                for dr, dc in [
                    (0, 1),
                    (1, 0),
                    (0, -1),
                    (-1, 0),
                ]:  # right, down, left, up
                    adj_row, adj_col = row + dr, col + dc
                    if 0 <= adj_row < self.rows and 0 <= adj_col < self.cols:
                        adj_cell = self.get_space_at(adj_row, adj_col)
                        if adj_cell:
                            self.connect_spaces(cell.id, adj_cell.id)

    def set_cell_type(self, position: GridPosition, cell_type: CellType) -> bool:
        """Set the type of a cell."""
        cell = self.get_space_at_position(position)
        if not cell:
            return False

        cell.cell_type = cell_type

        # If changing to a block, remove any letter
        if cell_type == "block" and cell.is_occupied():
            cell.remove_piece()

        return True

    def add_clue(
        self,
        number: int,
        direction: Direction,
        text: str,
        answer: str,
        start_position: GridPosition,
    ) -> Optional[str]:
        """Add a clue to the crossword."""
        # Check if the clue can be placed on the board
        if not self._validate_word_placement(answer, start_position, direction):
            return None

        # Create the clue
        clue = CrosswordClue(
            number=number,
            direction=direction,
            text=text,
            answer=answer,
            start_position=start_position,
            length=len(answer),
        )

        # Store the clue
        self.clues[clue.id] = clue

        # Create the word placement
        positions = self._get_word_positions(answer, start_position, direction)
        word = CrosswordWord(clue=clue, positions=positions, letters=list(answer))

        # Store the word
        self.words[clue.id] = word

        # Mark letter cells and set clue number
        for pos in positions:
            cell = self.get_space_at_position(pos)
            if cell:
                cell.cell_type = "letter"

        # Set the clue number on the starting cell
        start_cell = self.get_space_at_position(start_position)
        if start_cell:
            start_cell.number = number

        return clue.id

    def enter_letter(
        self, position: GridPosition, letter: str, is_filled: bool = True
    ) -> bool:
        """Enter a letter in a cell."""
        cell = self.get_space_at_position(position)
        if not cell or not cell.is_letter_cell:
            return False

        # Create letter piece
        letter_piece = CrosswordLetter(
            letter=letter, is_filled=is_filled, position=position
        )

        # Remove existing letter if present
        if cell.is_occupied():
            cell.remove_piece()

        # Place the new letter
        return cell.place_piece(letter_piece)

    def check_letter(self, position: GridPosition) -> bool:
        """Check if the letter at a position is correct."""
        cell = self.get_space_at_position(position)
        if (
            not cell
            or not cell.is_occupied()
            or not isinstance(cell.piece, CrosswordLetter)
        ):
            return False

        # Find the correct letter from any word that contains this position
        correct_letter = None
        for word in self.words.values():
            try:
                # Get the index of this position in the word
                idx = word.positions.index(position)
                # Get the corresponding letter
                correct_letter = word.letters[idx]
                break
            except ValueError:
                continue

        if not correct_letter:
            return False

        # Compare with the entered letter
        return cell.piece.letter == correct_letter

    def _validate_word_placement(
        self, word: str, start_position: GridPosition, direction: Direction
    ) -> bool:
        """Check if a word can be placed at the specified position."""
        # Calculate positions for each letter
        positions = self._get_word_positions(word, start_position, direction)

        # Check if all positions are within the grid
        for pos in positions:
            if not (0 <= pos.row < self.rows and 0 <= pos.col < self.cols):
                return False

            # Get the cell at this position
            cell = self.get_space_at_position(pos)
            if not cell:
                return False

            # Cell must not be a block
            if cell.is_block:
                return False

            # If cell already has a letter from another word, it must match
            if cell.is_letter_cell and cell.is_occupied():
                if isinstance(cell.piece, CrosswordLetter):
                    idx = positions.index(pos)
                    if cell.piece.letter != word[idx].upper():
                        return False

        return True

    def _get_word_positions(
        self, word: str, start_position: GridPosition, direction: Direction
    ) -> List[GridPosition]:
        """Calculate the positions for each letter of a word."""
        positions = []

        for i in range(len(word)):
            if direction == Direction.ACROSS:
                pos = GridPosition(row=start_position.row, col=start_position.col + i)
            else:  # DOWN
                pos = GridPosition(row=start_position.row + i, col=start_position.col)

            positions.append(pos)

        return positions

    @computed_field
    @property
    def is_complete(self) -> bool:
        """Check if the crossword is complete and correct."""
        # Check each letter cell has a letter
        for space in self.spaces.values():
            if isinstance(space, CrosswordCell) and space.is_letter_cell:
                if not space.is_occupied() or not isinstance(
                    space.piece, CrosswordLetter
                ):
                    return False

                # Check the letter is correct
                if not self.check_letter(space.position):
                    return False

        return True


# ======================================================
# CROSSWORD GAME
# ======================================================


class CrosswordMove(BaseModel):
    """A move in a crossword puzzle."""

    position: GridPosition
    letter: str


class CrosswordGame(Game[GridPosition, CrosswordLetter]):
    """Crossword puzzle game controller."""

    board: CrosswordBoard
    selected_position: Optional[GridPosition] = None
    check_as_you_type: bool = False

    def start_game(self) -> None:
        """Start the game."""
        super().start_game()
        self.board.initialize_grid()

    def is_valid_move(self, move: Union[CrosswordMove, Dict[str, any]]) -> bool:
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
        if not move.letter.isalpha() or len(move.letter) != 1:
            return False

        return True

    def make_move(self, move: Union[CrosswordMove, Dict[str, any]]) -> bool:
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
        for i, pos in enumerate(word.positions):
            if not self.board.check_letter(pos):
                return False

        return True

    def check_all(self) -> Dict[str, bool]:
        """Check all filled letters against the solution."""
        results = {}

        for clue_id, word in self.board.words.items():
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
    block_positions: List[Tuple[int, int]]  # (row, col) for each black cell
    clues: List[Dict[str, any]]  # Clue definitions

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
