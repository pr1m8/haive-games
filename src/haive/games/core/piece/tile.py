class Tile(GamePiece[P]):
    """A tile used in tile-based games (Scrabble, Mahjong, etc.)."""

    face_up: bool = True
    value: int = 0

    def flip(self) -> None:
        """Flip the tile's face."""
        self.face_up = not self.face_up

    def can_move_to(self, position: P, board: "Board") -> bool:
        """Check if this tile can be placed at the specified position."""
        space = board.get_space_at_position(position)
        if not space:
            return False
        # Default implementation: can place if space is empty
        return not space.is_occupied()
