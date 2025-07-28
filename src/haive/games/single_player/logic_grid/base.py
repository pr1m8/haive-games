"""Base core module.

This module provides base functionality for the Haive framework.

Classes:
    MarkType: MarkType implementation.
    LogicGridPosition: LogicGridPosition implementation.
    LogicGridMark: LogicGridMark implementation.

Functions:
    validate_indices: Validate Indices functionality.
"""

from __future__ import annotations

import uuid
from enum import Enum

# Import from our base framework
from game_framework_base import Board, Game, GamePiece, Position, Space
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator

# ======================================================
# LOGIC GRID TYPES AND CONSTANTS
# ======================================================


class MarkType(str, Enum):
    """Types of marks in a logic grid."""

    NONE = "none"  # Empty cell
    NO = "no"  # Not possible (X)
    YES = "yes"  # Confirmed match (O)


# ======================================================
# LOGIC GRID POSITION
# ======================================================


class LogicGridPosition(Position):
    """Position in a logic grid."""

    category1_index: int  # Index of item in first category
    category2_index: int  # Index of item in second category

    @field_validator("category1_index", "category2_index")
    @classmethod
    def validate_indices(cls, v: int) -> int:
        """Ensure indices are non-negative."""
        if v < 0:
            raise ValueError("Category indices must be non-negative")
        return v

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LogicGridPosition):
            return False
        return (
            self.category1_index == other.category1_index
            and self.category2_index == other.category2_index
        )

    def __hash__(self) -> int:
        return hash((self.category1_index, self.category2_index))

    @computed_field
    @property
    def display_coords(self) -> str:
        """Return human-readable coordinates."""
        return f"({self.category1_index}, {self.category2_index})"


# ======================================================
# LOGIC GRID MARK
# ======================================================


class LogicGridMark(GamePiece[LogicGridPosition]):
    """A mark in a logic grid."""

    mark_type: MarkType = MarkType.NONE

    def can_move_to(self, position: LogicGridPosition, board: Board) -> bool:
        """Marks can be placed on any empty space."""
        space = board.get_space_at_position(position)
        if not space:
            return False

        # Can place if space is empty or we're changing an existing mark
        return not space.is_occupied() or (
            isinstance(space.piece, LogicGridMark)
            and space.piece.mark_type != self.mark_type
        )


# ======================================================
# LOGIC GRID SPACE
# ======================================================


class LogicGridSpace(Space[LogicGridPosition, LogicGridMark]):
    """A cell in a logic grid."""

    position: LogicGridPosition

    @computed_field
    @property
    def mark_type(self) -> MarkType:
        """Get the type of mark in this space."""
        if not self.is_occupied() or not isinstance(self.piece, LogicGridMark):
            return MarkType.NONE
        return self.piece.mark_type


# ======================================================
# LOGIC GRID CLUE
# ======================================================


class ClueType(str, Enum):
    """Types of clues in a logic grid puzzle."""

    DIRECT_MATCH = "direct_match"  # A is B
    DIRECT_NONMATCH = "direct_nonmatch"  # A is not B
    RELATIVE = "relative"  # A is next to B
    ORDERING = "ordering"  # A comes before B
    CUSTOM = "custom"  # Custom logic


class LogicGridClue(BaseModel):
    """A clue in a logic grid puzzle."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    clue_type: ClueType
    text: str
    categories: list[str]
    items: list[list[int]]  # Indices of items involved in the clue

    @model_validator(mode="after")
    @classmethod
    def validate_clue(cls) -> LogicGridClue:
        """Validate the clue based on its type."""
        if self.clue_type in (ClueType.DIRECT_MATCH, ClueType.DIRECT_NONMATCH):
            # Should have 2 categories and 1 item per category
            if (
                len(self.categories) != 2
                or len(self.items) != 2
                or len(self.items[0]) != 1
                or len(self.items[1]) != 1
            ):
                raise ValueError(
                    f"{self.clue_type} clue must have 2 categories with 1 item each"
                )

        elif self.clue_type in (ClueType.RELATIVE, ClueType.ORDERING):
            # Should have 2 categories and at least 1 item per category
            if len(self.categories) != 2 or len(self.items) != 2:
                raise ValueError(f"{self.clue_type} clue must have 2 categories")

        return self

    def apply_to_grid(self, grid: LogicGrid) -> bool:
        """Apply this clue to the grid."""
        if self.clue_type == ClueType.DIRECT_MATCH:
            # Mark a direct match between two items
            cat1, cat2 = self.categories
            item1, item2 = self.items[0][0], self.items[1][0]

            # Get the category indices
            cat1_idx = grid.get_category_index(cat1)
            cat2_idx = grid.get_category_index(cat2)

            if cat1_idx == -1 or cat2_idx == -1:
                return False

            # Mark the direct match as YES
            pos = LogicGridPosition(category1_index=item1, category2_index=item2)
            grid.set_mark(pos, MarkType.YES)

            # Mark all other positions in the same row and column as NO
            for i in range(grid.category_sizes[cat1_idx]):
                if i != item1:
                    pos = LogicGridPosition(category1_index=i, category2_index=item2)
                    grid.set_mark(pos, MarkType.NO)

            for j in range(grid.category_sizes[cat2_idx]):
                if j != item2:
                    pos = LogicGridPosition(category1_index=item1, category2_index=j)
                    grid.set_mark(pos, MarkType.NO)

            return True

        if self.clue_type == ClueType.DIRECT_NONMATCH:
            # Mark that two items don't match
            cat1, cat2 = self.categories
            item1, item2 = self.items[0][0], self.items[1][0]

            # Get the category indices
            cat1_idx = grid.get_category_index(cat1)
            cat2_idx = grid.get_category_index(cat2)

            if cat1_idx == -1 or cat2_idx == -1:
                return False

            # Mark the cell as NO
            pos = LogicGridPosition(category1_index=item1, category2_index=item2)
            grid.set_mark(pos, MarkType.NO)

            return True

        # Additional clue types would be handled similarly

        return False


# ======================================================
# LOGIC GRID BOARD
# ======================================================


class LogicGrid(Board[LogicGridSpace[LogicGridMark], LogicGridPosition, LogicGridMark]):
    """A logic grid board."""

    categories: list[str]
    category_items: list[list[str]]
    category_sizes: list[int]
    relations: dict[str, dict[str, list[LogicGridSpace[LogicGridMark]]]] = Field(
        default_factory=dict
    )

    def get_space_at_position(
        self, position: LogicGridPosition
    ) -> LogicGridSpace[LogicGridMark] | None:
        """Get the space at the specified position."""
        for space in self.spaces.values():
            if (
                isinstance(space.position, LogicGridPosition)
                and space.position.category1_index == position.category1_index
                and space.position.category2_index == position.category2_index
            ):
                return space
        return None

    def initialize_grid(self) -> None:
        """Initialize the grid with empty spaces."""
        # Create spaces for each combination of items
        for i, category1 in enumerate(self.categories):
            for j, category2 in enumerate(self.categories):
                if i < j:  # Only create grids for unique category pairs
                    # Create spaces for all combinations of items in these categories
                    for item1_idx in range(len(self.category_items[i])):
                        for item2_idx in range(len(self.category_items[j])):
                            position = LogicGridPosition(
                                category1_index=item1_idx, category2_index=item2_idx
                            )
                            space = LogicGridSpace[LogicGridMark](position=position)
                            self.add_space(space)

                            # Store in relations for easy lookup
                            if category1 not in self.relations:
                                self.relations[category1] = {}
                            if category2 not in self.relations[category1]:
                                self.relations[category1][category2] = []

                            self.relations[category1][category2].append(space)

    def set_mark(self, position: LogicGridPosition, mark_type: MarkType) -> bool:
        """Set a mark at the specified position."""
        space = self.get_space_at_position(position)
        if not space:
            return False

        # Create a new mark or update existing
        if space.is_occupied() and isinstance(space.piece, LogicGridMark):
            space.piece.mark_type = mark_type
        else:
            mark = LogicGridMark(mark_type=mark_type, position=position)
            space.place_piece(mark)

        return True

    def get_category_index(self, category: str) -> int:
        """Get the index of a category."""
        try:
            return self.categories.index(category)
        except ValueError:
            return -1

    def get_grid_for_categories(
        self, category1: str, category2: str
    ) -> list[list[MarkType]]:
        """Get the grid of marks for a pair of categories."""
        if (
            category1 not in self.relations
            or category2 not in self.relations[category1]
        ):
            return []

        # Get category indices and sizes
        cat1_idx = self.get_category_index(category1)
        cat2_idx = self.get_category_index(category2)

        if cat1_idx == -1 or cat2_idx == -1:
            return []

        cat1_size = len(self.category_items[cat1_idx])
        cat2_size = len(self.category_items[cat2_idx])

        # Create empty grid
        grid = [[MarkType.NONE for _ in range(cat2_size)] for _ in range(cat1_size)]

        # Fill in the grid
        for space in self.relations[category1][category2]:
            pos = space.position
            grid[pos.category1_index][pos.category2_index] = space.mark_type

        return grid

    @computed_field
    @property
    def is_solved(self) -> bool:
        """Check if the puzzle is solved."""
        # A logic grid is solved when each item in each category
        # has exactly one YES mark in each relation grid

        for i, category1 in enumerate(self.categories):
            for j, category2 in enumerate(self.categories):
                if i < j:  # Check each unique pair of categories
                    # Get the grid for this pair
                    grid = self.get_grid_for_categories(category1, category2)

                    # Check each row has exactly one YES
                    for row in grid:
                        if row.count(MarkType.YES) != 1:
                            return False

                    # Check each column has exactly one YES
                    for col_idx in range(len(grid[0])):
                        col = [row[col_idx] for row in grid]
                        if col.count(MarkType.YES) != 1:
                            return False

        return True


# ======================================================
# LOGIC GRID PUZZLE GAME
# ======================================================


class LogicGridMove(BaseModel):
    """A move in a Logic Grid puzzle."""

    position: LogicGridPosition
    mark_type: MarkType


class LogicGridPuzzle(Game[LogicGridPosition, LogicGridMark]):
    """Logic Grid puzzle game controller."""

    board: LogicGrid
    clues: list[LogicGridClue] = Field(default_factory=list)

    def start_game(self) -> None:
        """Start the game."""
        super().start_game()
        self.board.initialize_grid()

    def add_clue(self, clue: LogicGridClue) -> None:
        """Add a clue to the puzzle."""
        self.clues.append(clue)

    def apply_clues(self) -> None:
        """Apply all clues to the grid."""
        for clue in self.clues:
            clue.apply_to_grid(self.board)

    def is_valid_move(self, move: LogicGridMove) -> bool:
        """Check if a move is valid."""
        # Get the space at the position
        space = self.board.get_space_at_position(move.position)
        if not space:
            return False

        # Can set any mark to any valid space
        return True

    def make_move(self, move: LogicGridMove) -> bool:
        """Make a move in the game."""
        if self.status != "in_progress":
            return False

        if not self.is_valid_move(move):
            return False

        # Set the mark
        result = self.board.set_mark(move.position, move.mark_type)

        if result:
            # Record the move
            self.moves.append(move.model_dump())

            # Check if the puzzle is solved
            if self.board.is_solved:
                self.status = "completed"

        return result

    def propagate_constraints(self) -> int:
        """Propagate constraints from currently placed marks."""
        # This would implement basic constraint propagation for logic grids
        # For example, if a cell is marked YES, all other cells in its row and column should be NO

        changes = 0

        # Check each pair of categories
        for i, category1 in enumerate(self.board.categories):
            for j, category2 in enumerate(self.board.categories):
                if i < j:  # For each unique pair
                    grid = self.board.get_grid_for_categories(category1, category2)

                    # Propagate row constraints
                    for row_idx, row in enumerate(grid):
                        if MarkType.YES in row:
                            yes_col = row.index(MarkType.YES)
                            # Mark all other cells in this row as NO
                            for col_idx, mark in enumerate(row):
                                if col_idx != yes_col and mark == MarkType.NONE:
                                    pos = LogicGridPosition(
                                        category1_index=row_idx, category2_index=col_idx
                                    )
                                    if self.board.set_mark(pos, MarkType.NO):
                                        changes += 1

                    # Propagate column constraints
                    for col_idx in range(len(grid[0])):
                        col = [row[col_idx] for row in grid]
                        if MarkType.YES in col:
                            yes_row = col.index(MarkType.YES)
                            # Mark all other cells in this column as NO
                            for row_idx, mark in enumerate(col):
                                if row_idx != yes_row and mark == MarkType.NONE:
                                    pos = LogicGridPosition(
                                        category1_index=row_idx, category2_index=col_idx
                                    )
                                    if self.board.set_mark(pos, MarkType.NO):
                                        changes += 1

        return changes

    def reset(self) -> None:
        """Reset the game."""
        super().reset()
        self.board.initialize_grid()


# ======================================================
# LOGIC GRID PUZZLE GENERATOR
# ======================================================


class LogicGridPuzzleDefinition(BaseModel):
    """Definition of a logic grid puzzle."""

    name: str
    categories: list[str]
    category_items: list[list[str]]
    clues: list[dict[str, any]]

    def create_game(self) -> LogicGridPuzzle:
        """Create a game from this definition."""
        # Create the grid
        board = LogicGrid(
            name=self.name,
            categories=self.categories,
            category_items=self.category_items,
            category_sizes=[len(items) for items in self.category_items],
        )

        # Create the game
        game = LogicGridPuzzle(name=self.name, board=board)

        # Add clues
        for clue_data in self.clues:
            clue = LogicGridClue(
                clue_type=clue_data["type"],
                text=clue_data["text"],
                categories=clue_data["categories"],
                items=clue_data["items"],
            )
            game.add_clue(clue)

        # Start the game
        game.start_game()

        # Apply clues
        game.apply_clues()

        return game
