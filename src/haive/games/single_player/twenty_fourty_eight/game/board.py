class TwentyFortyEightBoard(
    GridBoard[TwentyFortyEightSquare, GridPosition, NumberTile]
):
    """The 2048 game board with sliding and merging mechanics."""

    rows: int = 4
    cols: int = 4
    score: int = 0

    def initialize_board(self) -> None:
        """Initialize an empty 4x4 grid."""
        for row in range(self.rows):
            for col in range(self.cols):
                position = GridPosition(row=row, col=col)
                square = TwentyFortyEightSquare(position=position)
                self.add_space(square)

    def spawn_random_tile(self) -> Optional[NumberTile]:
        """Spawn a new tile (2 or 4) in a random empty space."""
        # Find all empty spaces
        empty_spaces = []
        for row in range(self.rows):
            for col in range(self.cols):
                square = self.get_space_at(row, col)
                if square and not square.is_occupied():
                    empty_spaces.append(square)

        if not empty_spaces:
            return None  # No empty spaces

        # Choose random empty space
        square = random.choice(empty_spaces)

        # Create new tile (90% chance of 2, 10% chance of 4)
        value = 4 if random.random() < 0.1 else 2
        tile = NumberTile(value=value)

        # Place tile
        if square.place_piece(tile):
            tile.position = square.position
            return tile

        return None

    def move_tiles(self, direction: Direction) -> bool:
        """
        Move all tiles in the specified direction, merging where possible.

        Returns:
            True if any tiles moved, False otherwise
        """
        # Reset merge status on all tiles
        for space in self.spaces.values():
            if space.is_occupied() and isinstance(space.piece, NumberTile):
                space.piece.reset_merge_status()

        # Track if anything moved
        moved = False

        # Process tiles in the right order based on direction
        if direction == Direction.UP:
            # Process column by column, starting from top
            for col in range(self.cols):
                for row in range(1, self.rows):
                    moved |= self._move_tile(row, col, -1, 0)

        elif direction == Direction.DOWN:
            # Process column by column, starting from bottom
            for col in range(self.cols):
                for row in range(self.rows - 2, -1, -1):
                    moved |= self._move_tile(row, col, 1, 0)

        elif direction == Direction.LEFT:
            # Process row by row, starting from left
            for row in range(self.rows):
                for col in range(1, self.cols):
                    moved |= self._move_tile(row, col, 0, -1)

        elif direction == Direction.RIGHT:
            # Process row by row, starting from right
            for row in range(self.rows):
                for col in range(self.cols - 2, -1, -1):
                    moved |= self._move_tile(row, col, 0, 1)

        return moved

    def _move_tile(self, row: int, col: int, dr: int, dc: int) -> bool:
        """
        Try to move a tile from (row, col) in direction (dr, dc).

        Returns:
            True if the tile moved, False otherwise
        """
        # Check if there's a tile at this position
        source = self.get_space_at(row, col)
        if not source or not source.is_occupied():
            return False

        tile = source.piece
        if not isinstance(tile, NumberTile):
            return False

        # Find the furthest position the tile can move to
        r, c = row, col
        next_r, next_c = r + dr, c + dc

        # Keep moving until we hit a boundary or an occupied space
        while 0 <= next_r < self.rows and 0 <= next_c < self.cols:
            target = self.get_space_at(next_r, next_c)
            if not target:
                break

            # If target space is empty, keep moving
            if not target.is_occupied():
                r, c = next_r, next_c
                next_r, next_c = r + dr, c + dc
                continue

            # If target has a tile that can be merged with ours, merge and stop
            target_tile = target.piece
            if (
                isinstance(target_tile, NumberTile)
                and target_tile.value == tile.value
                and not target_tile.merged_this_turn
            ):

                r, c = next_r, next_c
                break

            # Otherwise, can't move further
            break

        # If we didn't move, return False
        if r == row and c == col:
            return False

        # Remove tile from source
        removed_tile = source.remove_piece()
        if not removed_tile:
            return False

        # Get the target space
        target = self.get_space_at(r, c)
        if not target:
            # This shouldn't happen, but just in case
            source.place_piece(removed_tile)
            return False

        # Place tile in target (this will handle merging if needed)
        if target.place_tile(removed_tile):
            # If merge happened, update score
            if target.is_occupied() and target.piece.value > removed_tile.value:
                self.score += target.piece.value
            return True

        # If placement failed, put tile back
        source.place_piece(removed_tile)
        return False

    def has_valid_moves(self) -> bool:
        """Check if there are any valid moves remaining."""
        # Check for empty spaces
        for row in range(self.rows):
            for col in range(self.cols):
                square = self.get_space_at(row, col)
                if square and not square.is_occupied():
                    return True

        # Check for possible merges
        for row in range(self.rows):
            for col in range(self.cols):
                square = self.get_space_at(row, col)
                if not square or not square.is_occupied():
                    continue

                tile = square.piece
                if not isinstance(tile, NumberTile):
                    continue

                # Check adjacent squares for same value
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    adj_row, adj_col = row + dr, col + dc
                    if not (0 <= adj_row < self.rows and 0 <= adj_col < self.cols):
                        continue

                    adj_square = self.get_space_at(adj_row, adj_col)
                    if not adj_square or not adj_square.is_occupied():
                        continue

                    adj_tile = adj_square.piece
                    if (
                        isinstance(adj_tile, NumberTile)
                        and adj_tile.value == tile.value
                    ):
                        return True

        return False

    def has_winning_tile(self, target: int = 2048) -> bool:
        """Check if the target tile value has been reached."""
        for space in self.spaces.values():
            if space.is_occupied() and isinstance(space.piece, NumberTile):
                if space.piece.value >= target:
                    return True
        return False

    def get_max_tile(self) -> int:
        """Get the highest tile value on the board."""
        max_value = 0
        for space in self.spaces.values():
            if space.is_occupied() and isinstance(space.piece, NumberTile):
                max_value = max(max_value, space.piece.value)
        return max_value

    def clear(self) -> None:
        """Clear all tiles from the board."""
        for space in self.spaces.values():
            space.remove_piece()
        self.score = 0

    def get_board_state(self) -> List[List[int]]:
        """Get the current board state as a 2D array of values."""
        state = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                square = self.get_space_at(row, col)
                if (
                    square
                    and square.is_occupied()
                    and isinstance(square.piece, NumberTile)
                ):
                    state[row][col] = square.piece.value
        return state
