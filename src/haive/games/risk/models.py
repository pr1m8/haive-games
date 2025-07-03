"""Models for the Risk game.

This module defines the core data structures for the Risk game, including
territories, continents, cards, players, and moves.
"""

from enum import Enum

from pydantic import BaseModel, Field


class CardType(str, Enum):
    """Types of Risk cards.

    Represents the different types of cards that can be collected and traded
    for armies in the Risk game.
    """

    INFANTRY = "infantry"
    CAVALRY = "cavalry"
    ARTILLERY = "artillery"
    WILD = "wild"


class Card(BaseModel):
    """A Risk card that can be traded for armies.

    Attributes:
        card_type: The type of the card (infantry, cavalry, artillery, wild).
        territory_name: Optional name of territory shown on the card.
    """

    card_type: CardType
    territory_name: str | None = None

    def __str__(self) -> str:
        """String representation of the card."""
        if self.territory_name:
            return f"{self.card_type.value.capitalize()} ({self.territory_name})"
        return f"{self.card_type.value.capitalize()}"


class Territory(BaseModel):
    """A territory on the Risk board.

    Attributes:
        name: The name of the territory.
        continent: The name of the continent this territory belongs to.
        owner: The player who controls this territory.
        armies: The number of armies on this territory.
        adjacent: List of territory names that are adjacent to this one.
    """

    name: str
    continent: str
    owner: str | None = None
    armies: int = 0
    adjacent: list[str] = Field(default_factory=list)

    def __str__(self) -> str:
        """String representation of the territory."""
        owner_str = f"{self.owner}" if self.owner else "Unoccupied"
        return f"{self.name} ({owner_str}, {self.armies} armies)"


class Continent(BaseModel):
    """A continent on the Risk board.

    Attributes:
        name: The name of the continent.
        bonus: The number of bonus armies awarded for controlling all territories.
        territories: The names of all territories in this continent.
    """

    name: str
    bonus: int
    territories: list[str] = Field(default_factory=list)

    def __str__(self) -> str:
        """String representation of the continent."""
        return f"{self.name} (Bonus: {self.bonus})"


class Player(BaseModel):
    """A player in the Risk game.

    Attributes:
        name: The player's name.
        cards: The cards in the player's hand.
        unplaced_armies: The number of armies the player has not yet placed.
        eliminated: Whether the player has been eliminated from the game.
    """

    name: str
    cards: list[Card] = Field(default_factory=list)
    unplaced_armies: int = 0
    eliminated: bool = False

    def __str__(self) -> str:
        """String representation of the player."""
        status = "Eliminated" if self.eliminated else "Active"
        return f"{self.name} ({status}, {self.unplaced_armies} unplaced armies, {len(self.cards)} cards)"


class MoveType(str, Enum):
    """Types of moves in Risk.

    Represents the different types of actions a player can take during their turn.
    """

    PLACE_ARMIES = "place_armies"
    ATTACK = "attack"
    FORTIFY = "fortify"
    TRADE_CARDS = "trade_cards"


class RiskMove(BaseModel):
    """A move in the Risk game.

    Attributes:
        move_type: The type of move (place armies, attack, fortify, trade cards).
        player: The player making the move.
        from_territory: The territory to move armies from (for attack/fortify).
        to_territory: The territory to move armies to (for attack/fortify/place).
        armies: The number of armies to place or move.
        cards: The cards to trade in (for trade_cards move).
        attack_dice: The number of dice to use in an attack.
    """

    move_type: MoveType
    player: str
    from_territory: str | None = None
    to_territory: str | None = None
    armies: int | None = None
    cards: list[Card] | None = None
    attack_dice: int | None = None

    def __str__(self) -> str:
        """String representation of the move."""
        if self.move_type == MoveType.PLACE_ARMIES:
            return f"{self.player} places {self.armies} armies on {self.to_territory}"
        if self.move_type == MoveType.ATTACK:
            return f"{self.player} attacks from {self.from_territory} to {self.to_territory} with {self.attack_dice} dice"
        if self.move_type == MoveType.FORTIFY:
            return f"{self.player} fortifies {self.to_territory} with {self.armies} armies from {self.from_territory}"
        if self.move_type == MoveType.TRADE_CARDS:
            cards_str = (
                ", ".join(str(card) for card in self.cards)
                if self.cards
                else "no cards"
            )
            return f"{self.player} trades in cards: {cards_str}"
        return f"Unknown move: {self.move_type}"


class PhaseType(str, Enum):
    """Game phases in Risk.

    Represents the different phases of a Risk game turn.
    """

    SETUP = "setup"
    REINFORCE = "reinforce"
    ATTACK = "attack"
    FORTIFY = "fortify"
    GAME_OVER = "game_over"


class GameStatus(str, Enum):
    """Status of the Risk game.

    Indicates whether the game is still being played or has concluded.
    """

    IN_PROGRESS = "in_progress"
    FINISHED = "finished"


class RiskAnalysis(BaseModel):
    """Analysis of a Risk position.

    Attributes:
        player: The player the analysis is for.
        controlled_continents: List of continents controlled by the player.
        controlled_territories: Number of territories controlled by the player.
        total_armies: Total number of armies controlled by the player.
        position_evaluation: Assessment of the player's position.
        recommended_move: The recommended move for the player.
        explanation: Explanation of the analysis.
    """

    player: str
    controlled_continents: list[str] = Field(default_factory=list)
    controlled_territories: int
    total_armies: int
    position_evaluation: str  # winning, losing, or neutral
    recommended_move: RiskMove
    explanation: str

    def __str__(self) -> str:
        """String representation of the analysis."""
        continents_str = (
            ", ".join(self.controlled_continents)
            if self.controlled_continents
            else "None"
        )
        return (
            f"Analysis for {self.player}:\n"
            f"Controlled continents: {continents_str}\n"
            f"Controlled territories: {self.controlled_territories}\n"
            f"Total armies: {self.total_armies}\n"
            f"Position evaluation: {self.position_evaluation}\n"
            f"Recommended move: {self.recommended_move}\n"
            f"Explanation: {self.explanation}"
        )
