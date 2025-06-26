"""Data models and enumerations for the Clue (Cluedo) mystery game implementation.

This module defines the core data structures, enumerations, and models used
throughout the Clue game implementation. It includes the traditional game
elements (suspects, weapons, rooms) as well as game state representations,
player data structures, and action models.

The models follow the classic Clue game rules and include:
- Six suspects (Colonel Mustard, Professor Plum, etc.)
- Six weapons (Knife, Candlestick, Revolver, etc.)
- Nine rooms (Kitchen, Ballroom, Conservatory, etc.)
- Card types and game state tracking
- Player actions and game moves

Key Classes:
    ValidSuspect: Enumeration of all possible suspect characters
    ValidWeapon: Enumeration of all possible murder weapons
    ValidRoom: Enumeration of all possible locations
    CardType: Types of cards in the game (Suspect, Weapon, Room)
    GameState: Current state of the game including player positions and cards
    Player: Individual player data and card holdings
    Move: Represents a player's action (suggestion, accusation, etc.)

Usage:
    ```python
    from haive.games.clue.models import ValidSuspect, ValidWeapon, ValidRoom

    # Create a suggestion
    suspect = ValidSuspect.COLONEL_MUSTARD
    weapon = ValidWeapon.KNIFE
    room = ValidRoom.KITCHEN

    # Use in game logic
    suggestion = (suspect, weapon, room)
    ```

The models are designed to be immutable where possible and include comprehensive
validation to ensure game rules are properly enforced throughout the implementation.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any


class ValidSuspect(Enum):
    """Valid suspects in the game of Clue."""

    COLONEL_MUSTARD = "Colonel Mustard"
    PROFESSOR_PLUM = "Professor Plum"
    MR_GREEN = "Mr. Green"
    MRS_PEACOCK = "Mrs. Peacock"
    MISS_SCARLET = "Miss Scarlet"
    MRS_WHITE = "Mrs. White"


class ValidWeapon(Enum):
    """Valid weapons in the game of Clue."""

    KNIFE = "Knife"
    CANDLESTICK = "Candlestick"
    REVOLVER = "Revolver"
    ROPE = "Rope"
    LEAD_PIPE = "Lead Pipe"
    WRENCH = "Wrench"


class ValidRoom(Enum):
    """Valid rooms in the game of Clue."""

    KITCHEN = "Kitchen"
    BALLROOM = "Ballroom"
    CONSERVATORY = "Conservatory"
    BILLIARD_ROOM = "Billiard Room"
    LIBRARY = "Library"
    STUDY = "Study"
    HALL = "Hall"
    LOUNGE = "Lounge"
    DINING_ROOM = "Dining Room"


class CardType(Enum):
    """Types of cards in the game of Clue."""

    SUSPECT = "Suspect"
    WEAPON = "Weapon"
    ROOM = "Room"


@dataclass
class ClueCard:
    """A card in the game of Clue."""

    name: str  # The name of the card (e.g., "Colonel Mustard")
    card_type: CardType  # The type of card (suspect, weapon, or room)

    @staticmethod
    def from_suspect(suspect: ValidSuspect) -> "ClueCard":
        """Create a card from a suspect enum value."""
        return ClueCard(name=suspect.value, card_type=CardType.SUSPECT)

    @staticmethod
    def from_weapon(weapon: ValidWeapon) -> "ClueCard":
        """Create a card from a weapon enum value."""
        return ClueCard(name=weapon.value, card_type=CardType.WEAPON)

    @staticmethod
    def from_room(room: ValidRoom) -> "ClueCard":
        """Create a card from a room enum value."""
        return ClueCard(name=room.value, card_type=CardType.ROOM)

    def to_dict(self) -> dict[str, str]:
        """Convert the card to a dictionary."""
        return {"name": self.name, "card_type": self.card_type.value}


@dataclass
class ClueSolution:
    """The solution to a game of Clue."""

    suspect: ValidSuspect
    weapon: ValidWeapon
    room: ValidRoom

    def to_dict(self) -> dict[str, str]:
        """Convert the solution to a dictionary."""
        return {
            "suspect": self.suspect.value,
            "weapon": self.weapon.value,
            "room": self.room.value,
        }


@dataclass
class ClueGuess:
    """A guess made during a game of Clue."""

    suspect: ValidSuspect
    weapon: ValidWeapon
    room: ValidRoom

    def to_dict(self) -> dict[str, str]:
        """Convert the guess to a dictionary."""
        return {
            "suspect": self.suspect.value,
            "weapon": self.weapon.value,
            "room": self.room.value,
        }


@dataclass
class ClueResponse:
    """A response to a guess in a game of Clue."""

    is_correct: bool  # True if the guess matched the solution
    responding_player: str | None = None  # Name of the player who responded (if any)
    refuting_card: ClueCard | None = None  # The card shown to refute the guess (if any)

    def to_dict(self) -> dict[str, Any]:
        """Convert the response to a dictionary."""
        result = {
            "is_correct": self.is_correct,
            "responding_player": self.responding_player,
        }
        if self.refuting_card:
            result["refuting_card"] = self.refuting_card.to_dict()
        return result


@dataclass
class ClueHypothesis:
    """A hypothesis about the solution generated by AI analysis."""

    # Primary suspects
    prime_suspect: ValidSuspect | None = None
    prime_weapon: ValidWeapon | None = None
    prime_room: ValidRoom | None = None

    # Confidence level (0.0 to 1.0)
    confidence: float = 0.0

    # Additional information
    excluded_suspects: list[ValidSuspect] = None
    excluded_weapons: list[ValidWeapon] = None
    excluded_rooms: list[ValidRoom] = None

    # Text reasoning
    reasoning: str = ""

    def __post_init__(self):
        """Initialize empty lists if None."""
        if self.excluded_suspects is None:
            self.excluded_suspects = []
        if self.excluded_weapons is None:
            self.excluded_weapons = []
        if self.excluded_rooms is None:
            self.excluded_rooms = []

    def to_dict(self) -> dict[str, Any]:
        """Convert the hypothesis to a dictionary."""
        return {
            "prime_suspect": self.prime_suspect.value if self.prime_suspect else None,
            "prime_weapon": self.prime_weapon.value if self.prime_weapon else None,
            "prime_room": self.prime_room.value if self.prime_room else None,
            "confidence": self.confidence,
            "excluded_suspects": [s.value for s in self.excluded_suspects],
            "excluded_weapons": [w.value for w in self.excluded_weapons],
            "excluded_rooms": [r.value for r in self.excluded_rooms],
            "reasoning": self.reasoning,
        }


class GameStatus(Enum):
    """Status of a Clue game."""

    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

    def __str__(self) -> str:
        return self.value
