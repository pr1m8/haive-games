"""Board core module.

This module provides board functionality for the Haive framework.

Classes:
    CrosswordBoard: CrosswordBoard implementation.

Functions:
    initialize_grid: Initialize Grid functionality.
    set_cell_type: Set Cell Type functionality.
    add_clue: Add Clue functionality.
"""


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
