from pydantic import computed_field, field_validator

from haive.games.framework.core.position import Position


class PegPosition(Position):
    """Position on a Tower of Hanoi peg."""

    peg: PegNumber  # Which peg (1, 2, or 3)
    level: int  # Position in stack (0 = bottom)

    @field_validator("level")
    @classmethod
    def validate_level(cls, v: int) -> int:
        """Ensure level is valid."""
        if v < 0:
            raise ValueError("Level must be non-negative")
        return v

    def __eq__(self, other: object) -> bool:
        """  Eq  .

Args:
    other: [TODO: Add description]

Returns:
    [TODO: Add return description]
"""
        if not isinstance(other, PegPosition):
            return False
        return self.peg == other.peg and self.level == other.level

    def __hash__(self) -> int:
        """  Hash  .

Returns:
    [TODO: Add return description]
"""
        return hash((self.peg, self.level))

    @computed_field
    @property
    def display_coords(self) -> str:
        """Return human-readable coordinates."""
        return f"Peg {self.peg}, Level {self.level}"
