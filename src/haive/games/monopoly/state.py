"""Fixed Monopoly game state with proper BaseModel consistency and state conversion.

This module provides the corrected MonopolyState class that ensures:
    - Proper BaseModel usage throughout
    - Consistent state conversion methods
    - Proper reducer handling for LangGraph Command updates
    - Fixed update_player method to avoid IndexError
"""

import operator
from datetime import datetime
from enum import Enum
from typing import Annotated, Any, Dict, List, Optional, Union

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field, computed_field

from haive.games.monopoly.models import (
    DiceRoll,
    GameEvent,
    Player,
    PlayerActionType,
    Property,
)


def add_events(left: List[GameEvent], right: List[GameEvent]) -> List[GameEvent]:
    """Custom reducer for game events - always append new events."""
    if not left:
        return right
    if not right:
        return left
    return left + right


def add_strings(left: List[str], right: List[str]) -> List[str]:
    """Custom reducer for string lists."""
    if not left:
        return right
    if not right:
        return left
    return left + right


class MonopolyState(BaseModel):
    """State for the Monopoly game with proper reducers and BaseModel consistency.

    This class represents the complete game state including:
        - Players and their states
        - Properties and ownership
        - Game flow and turn management
        - Event history with reducers
        - Dice rolls and movement
    """

    # Core game data
    players: List[Player] = Field(
        default_factory=list, description="All players in the game"
    )
    properties: Dict[str, Property] = Field(
        default_factory=dict, description="All properties on the board"
    )

    # Game flow state
    current_player_index: int = Field(default=0, description="Index of current player")
    turn_number: int = Field(default=1, description="Current turn number")
    round_number: int = Field(default=1, description="Current round number")
    game_status: str = Field(default="waiting", description="Current game status")

    # Dice and movement
    last_roll: Optional[DiceRoll] = Field(default=None, description="Last dice roll")
    doubles_rolled: bool = Field(
        default=False, description="Whether doubles were rolled this turn"
    )

    # Cards
    chance_cards: List[str] = Field(
        default_factory=list, description="Shuffled chance cards"
    )
    community_chest_cards: List[str] = Field(
        default_factory=list, description="Shuffled community chest cards"
    )

    # Game events with proper reducer for Command updates
    game_events: Annotated[List[GameEvent], add_events] = Field(
        default_factory=list, description="History of game events"
    )

    # Game end state
    winner: Optional[str] = Field(default=None, description="Winner of the game")
    error_message: Optional[str] = Field(
        default=None, description="Error message if any"
    )

    # Optional messages field for LLM compatibility - but not required
    messages: Optional[List[BaseMessage]] = Field(
        default_factory=list,
        description="Optional conversation messages for LLM compatibility",
    )

    # Computed properties with proper bounds checking
    @computed_field
    @property
    def current_player(self) -> Player:
        """Get the current player with proper bounds checking."""
        if not self.players:
            # Return a default player if no players exist
            return Player(name="Unknown")

        # Ensure index is within bounds
        if 0 <= self.current_player_index < len(self.players):
            return self.players[self.current_player_index]

        # If index is out of bounds, reset to 0 and return first player
        # This is a defensive measure to prevent crashes
        if self.players:
            return self.players[0]

        return Player(name="Unknown")

    @computed_field
    @property
    def active_players(self) -> List[Player]:
        """Get list of active (non-bankrupt) players."""
        return [p for p in self.players if not p.bankrupt]

    @computed_field
    @property
    def bankrupt_players(self) -> List[Player]:
        """Get list of bankrupt players."""
        return [p for p in self.players if p.bankrupt]

    def get_player_by_name(self, name: str) -> Optional[Player]:
        """Get player by name."""
        return next((p for p in self.players if p.name == name), None)

    def get_property_by_name(self, name: str) -> Optional[Property]:
        """Get property by name."""
        return self.properties.get(name)

    def get_property_by_position(self, position: int) -> Optional[Property]:
        """Get property at a specific board position."""
        return next(
            (prop for prop in self.properties.values() if prop.position == position),
            None,
        )

    def get_properties_owned_by_player(self, player_name: str) -> List[Property]:
        """Get all properties owned by a player."""
        return [prop for prop in self.properties.values() if prop.owner == player_name]

    def player_owns_monopoly(self, player_name: str, color: str) -> bool:
        """Check if player owns all properties of a color group."""
        from .utils import get_properties_by_color

        color_group = get_properties_by_color(color)
        owned_in_group = [
            prop.name
            for prop in self.properties.values()
            if prop.owner == player_name and prop.name in color_group
        ]

        return len(owned_in_group) == len(color_group)

    def get_rent_amount(self, property_name: str, dice_roll: int = 0) -> int:
        """Calculate rent amount for a property."""
        from .utils import calculate_rent

        property_obj = self.get_property_by_name(property_name)
        if not property_obj:
            return 0

        return calculate_rent(property_obj, self, dice_roll)

    def next_player(self) -> None:
        """Move to the next player's turn with proper bounds checking."""
        active = self.active_players
        if len(active) <= 1:
            return

        if not self.players:
            return

        # Find next active player
        start_index = self.current_player_index
        for i in range(len(self.players)):
            next_index = (start_index + 1 + i) % len(self.players)
            if next_index < len(self.players) and not self.players[next_index].bankrupt:
                self.current_player_index = next_index
                break

        # If we're back to player 0, increment round
        if self.current_player_index == 0:
            self.round_number += 1

        self.turn_number += 1

    def get_recent_events(self, count: int = 10) -> List[GameEvent]:
        """Get the most recent game events."""
        return self.game_events[-count:] if self.game_events else []

    def add_event(self, event: GameEvent) -> None:
        """Add a single event to the game history."""
        # This will work with the reducer when using Command updates
        self.game_events.append(event)

    @classmethod
    def from_state_object(
        cls, state: Union["MonopolyState", BaseModel, Dict[str, Any]]
    ) -> "MonopolyState":
        """Convert any state object to MonopolyState.

        This is the primary method for ensuring consistency across all state handling.
        """
        if isinstance(state, cls):
            return state
        elif isinstance(state, dict):
            return cls.from_dict(state)
        elif isinstance(state, BaseModel):
            # Convert BaseModel to dict then to MonopolyState
            return cls.from_dict(state.model_dump())
        else:
            raise ValueError(f"Cannot convert {type(state)} to MonopolyState")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MonopolyState":
        """Create state from dictionary with proper nested object handling."""
        # Create a copy to avoid modifying the original
        data = data.copy()

        # Handle nested Player objects
        if "players" in data and isinstance(data["players"], list):
            data["players"] = [
                Player.model_validate(p) if isinstance(p, dict) else p
                for p in data["players"]
            ]

        # Handle nested Property objects
        if "properties" in data and isinstance(data["properties"], dict):
            data["properties"] = {
                name: Property.model_validate(prop) if isinstance(prop, dict) else prop
                for name, prop in data["properties"].items()
            }

        # Handle nested GameEvent objects
        if "game_events" in data and isinstance(data["game_events"], list):
            data["game_events"] = [
                GameEvent.model_validate(event) if isinstance(event, dict) else event
                for event in data["game_events"]
            ]

        # Handle DiceRoll object
        if "last_roll" in data and data["last_roll"]:
            if isinstance(data["last_roll"], dict):
                data["last_roll"] = DiceRoll.model_validate(data["last_roll"])

        # Ensure messages field exists and is empty list if not provided
        if "messages" not in data:
            data["messages"] = []

        # Validate current_player_index bounds
        if "current_player_index" in data and "players" in data:
            players_count = len(data["players"])
            if players_count > 0:
                data["current_player_index"] = max(
                    0, min(data["current_player_index"], players_count - 1)
                )
            else:
                data["current_player_index"] = 0

        return cls.model_validate(data)

    def to_dict(self) -> Dict[str, Any]:
        """Convert state to dictionary for serialization."""
        # Use model_dump for Pydantic v2 compliance
        result = self.model_dump()

        # Add computed properties
        result["current_player"] = self.current_player.model_dump()
        result["active_players"] = [p.model_dump() for p in self.active_players]
        result["bankrupt_players"] = [p.model_dump() for p in self.bankrupt_players]

        return result

    def update_player(self, player_index: int, player: Player) -> "MonopolyState":
        """Update a player and return a new state instance with proper bounds checking."""
        # Validate player_index bounds
        if not self.players:
            raise ValueError("No players in the game to update")

        if player_index < 0 or player_index >= len(self.players):
            raise ValueError(
                f"Player index {player_index} out of bounds (0-{len(self.players)-1})"
            )

        # Create a copy of the players list
        new_players = self.players.copy()
        new_players[player_index] = player

        return self.model_copy(update={"players": new_players})

    def update_property(
        self, property_name: str, property_obj: Property
    ) -> "MonopolyState":
        """Update a property and return a new state instance."""
        new_properties = self.properties.copy()
        new_properties[property_name] = property_obj

        return self.model_copy(update={"properties": new_properties})

    def add_events_and_update(
        self, events: List[GameEvent], **updates
    ) -> Dict[str, Any]:
        """Add events and other updates for Command usage."""
        update_dict = {"game_events": events}
        update_dict.update(updates)
        return update_dict

    def validate_state_consistency(self) -> List[str]:
        """Validate the state for consistency and return any issues found."""
        issues = []

        # Check current_player_index bounds
        if self.players:
            if self.current_player_index < 0 or self.current_player_index >= len(
                self.players
            ):
                issues.append(
                    f"current_player_index {self.current_player_index} out of bounds (0-{len(self.players)-1})"
                )
        else:
            if self.current_player_index != 0:
                issues.append(f"current_player_index should be 0 when no players exist")

        # Check for duplicate player names
        player_names = [p.name for p in self.players]
        if len(player_names) != len(set(player_names)):
            issues.append("Duplicate player names found")

        # Check property ownership consistency
        for property_name, property_obj in self.properties.items():
            if property_obj.owner:
                owner_player = self.get_player_by_name(property_obj.owner)
                if not owner_player:
                    issues.append(
                        f"Property {property_name} owned by non-existent player {property_obj.owner}"
                    )
                elif property_name not in owner_player.properties:
                    issues.append(
                        f"Property {property_name} not in owner's property list"
                    )

        return issues

    class Config:
        """Pydantic configuration."""

        arbitrary_types_allowed = True
