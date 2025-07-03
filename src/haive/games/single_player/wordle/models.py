from typing import Literal

from pydantic import BaseModel, Field, field_validator

from haive.games.framework.base import GameState


class WordConnectionsMove(BaseModel):
    """Represents a move in Word Connections game."""

    words: list[str] = Field(
        ..., description="Set of 4 words that the player believes are connected"
    )
    category_guess: str = Field(
        ..., description="Player's guess about what connects these words"
    )

    @field_validator("words")
    @classmethod
    def validate_words_length(cls, v):
        """Validate that exactly 4 words are provided."""
        if len(v) != 4:
            raise ValueError(f"Must select exactly 4 words, selected {len(v)}")
        return v


class WordConnectionsState(GameState):
    """State for a Word Connections game."""

    # Core game data
    grid: list[str] = Field(..., description="16 words in the grid")
    categories: dict[str, list[str]] = Field(
        ..., description="The correct categories (hidden from player)"
    )
    difficulty_map: dict[str, str] = Field(
        ..., description="Difficulty level for each category"
    )

    # Game progress
    found_categories: dict[str, list[str]] = Field(
        default_factory=dict, description="Categories found so far"
    )
    incorrect_guesses: list[list[str]] = Field(
        default_factory=list, description="Previous incorrect guesses"
    )
    mistakes_remaining: int = Field(
        default=4, description="Mistakes allowed before game over"
    )

    # Game state
    game_status: Literal["playing", "won", "lost"] = Field(default="playing")

    @property
    def remaining_words(self) -> list[str]:
        """Get words not yet correctly categorized."""
        found_words = set()
        for words in self.found_categories.values():
            found_words.update(words)
        return [w for w in self.grid if w not in found_words]

    @property
    def display_grid(self) -> str:
        """Display the current grid state."""
        remaining = self.remaining_words

        if not remaining:
            return "All categories found!"

        # Create 4x4 display
        display = "WORD CONNECTIONS GRID:\n\n"

        # Show remaining words in a grid
        for i in range(0, len(remaining), 4):
            row = remaining[i : i + 4]
            # Pad row if needed
            while len(row) < 4:
                row.append("[SOLVED]")
            display += "  ".join(f"{word:12}" for word in row) + "\n"

        # Show found categories
        if self.found_categories:
            display += "\nFOUND CATEGORIES:\n"
            for category, words in self.found_categories.items():
                difficulty = self.difficulty_map.get(category, "")
                emoji = {
                    "yellow": "🟨",
                    "green": "🟩",
                    "blue": "🟦",
                    "purple": "🟪",
                }.get(difficulty, "")
                display += f"{emoji} {category}: {', '.join(words)}\n"

        # Show mistakes
        display += f"\nMistakes remaining: {self.mistakes_remaining}/4"

        return display
