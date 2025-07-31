from enum import Enum
from typing import Annotated, Any, Union

from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field, computed_field, field_validator

from haive.games.monopoly.models import (
    DiceRoll,
    GameEvent,
    Player,
    Property,
    PropertyColor,
    PropertyType,
)
from haive.games.monopoly.utils import calculate_rent, get_properties_by_color

r"""Comprehensive state management system for Monopoly gameplay and real estate
economics.

This module provides sophisticated state models for Monopoly games with complete
support for game mechanics, economic transactions, strategic analysis, and
distributed gameplay. The state system maintains both game rules and economic
context for advanced AI decision-making and tournament play.

The state system supports:
- Complete game state tracking with property ownership and development
- Economic transaction logging with detailed financial analysis
- Strategic analysis integration for AI decision-making
- Multi-player state synchronization for distributed gameplay
- Comprehensive validation and consistency checking
- LangGraph integration with proper state reducers

Examples:
    Creating a new game state::\n

        state = MonopolyState.initialize_game(
            player_names=["Alice", "Bob", "Charlie"],
            starting_money=1500
        )

    Managing property transactions::\n

        # Purchase property
        state = state.purchase_property("Alice", "Boardwalk", 400)

        # Build development
        state = state.build_houses("Alice", "Boardwalk", 2)

        # Calculate rent
        rent = state.get_rent_amount("Boardwalk", dice_roll=7)

    Tracking game progression::\n

        # Move to next player
        state.next_player()

        # Add game events
        event = GameEvent(
            type="property_purchase",
            player="Alice",
            details="Purchased Boardwalk for $400"
        )
        state.add_event(event)

        # Check game completion
        if state.is_game_over():
            winner = state.winner

    Economic analysis::\n

        # Financial metrics
        metrics = state.economic_metrics

        # Property distribution
        distribution = state.property_distribution

        # Player rankings
        rankings = state.player_rankings

Note:
    All state models use Pydantic for validation and support both JSON serialization
    and integration with LangGraph for distributed tournament systems.
"""


class GameStatus(str, Enum):
    """Enumeration of game status states.

    Defines the different states a Monopoly game can be in,
    affecting which actions are valid and how the game progresses.

    Values:
        WAITING: Game is waiting to start
        PLAYING: Game is actively in progress
        PAUSED: Game is temporarily paused
        FINISHED: Game has completed with a winner
        ABANDONED: Game was abandoned before completion
    """

    WAITING = "waiting"
    PLAYING = "playing"
    PAUSED = "paused"
    FINISHED = "finished"
    ABANDONED = "abandoned"


def add_events(left: list[GameEvent], right: list[GameEvent]) -> list[GameEvent]:
    """Custom reducer for game events - always append new events.

    This reducer ensures that when state updates occur through LangGraph Commands,
    game events are properly accumulated rather than replaced.

    Args:
        left (List[GameEvent]): Existing events in the state.
        right (List[GameEvent]): New events to add.

    Returns:
        List[GameEvent]: Combined list of events.
    """
    if not left:
        return right
    if not right:
        return left
    return left + right


def add_strings(left: list[str], right: list[str]) -> list[str]:
    """Custom reducer for string lists.

    Generic reducer for accumulating string lists in LangGraph state updates.

    Args:
        left (List[str]): Existing strings in the state.
        right (List[str]): New strings to add.

    Returns:
        List[str]: Combined list of strings.
    """
    if not left:
        return right
    if not right:
        return left
    return left + right


class MonopolyState(BaseModel):
    r"""Comprehensive state model for Monopoly gameplay with economic analysis
    and strategic context.

    This class provides complete state management for Monopoly games, supporting
    both traditional gameplay mechanics and advanced economic simulation. The state
    system maintains game rules, property ownership, financial transactions, and
    strategic context for AI decision-making and tournament play.

    The state system supports:
    - Complete game state tracking with property ownership and development
    - Economic transaction logging with detailed financial analysis
    - Strategic analysis integration for AI decision-making capabilities
    - Multi-player state synchronization for distributed gameplay
    - Comprehensive validation and consistency checking
    - LangGraph integration with proper state reducers and command updates

    Attributes:
        players (List[Player]): All players in the game with complete financial profiles.
        properties (Dict[str, Property]): All properties on the board with ownership details.
        current_player_index (int): Index of the player whose turn it currently is.
        turn_number (int): Current turn number for tracking game progression.
        round_number (int): Current round number (completed cycles through all players).
        game_status (GameStatus): Current status of the game (waiting, playing, finished, etc.).
        last_roll (Optional[DiceRoll]): Most recent dice roll with movement information.
        doubles_rolled (bool): Whether doubles were rolled this turn (affects extra turns).
        doubles_count (int): Number of consecutive doubles rolled (jail on 3).
        chance_cards (List[str]): Shuffled deck of Chance cards.
        community_chest_cards (List[str]): Shuffled deck of Community Chest cards.
        game_events (List[GameEvent]): Complete history of all game events and transactions.
        winner (Optional[str]): Name of the winning player if game is complete.
        error_message (Optional[str]): Error message if any operation failed.
        messages (Optional[List[BaseMessage]]): Optional conversation messages for LLM compatibility.
        houses_remaining (int): Number of houses available for purchase (scarcity rule).
        hotels_remaining (int): Number of hotels available for purchase (scarcity rule).
        free_parking_money (int): Money accumulated on Free Parking (house rule).
        jail_get_out_free_cards (Dict[str, int]): Get Out of Jail Free cards held by players.

    Examples:
        Creating a new game state::\n

            state = MonopolyState.initialize_game(
                player_names=["Alice", "Bob", "Charlie"],
                starting_money=1500
            )
            assert len(state.players) == 3
            assert state.current_player_index == 0
            assert state.turn_number == 1

        Managing property transactions::\n

            # Purchase property
            state = state.purchase_property("Alice", "Boardwalk", 400)
            alice = state.get_player_by_name("Alice")
            assert "Boardwalk" in alice.properties
            assert alice.money == 1100  # 1500 - 400

            # Build development
            state = state.build_houses("Alice", "Boardwalk", 2)
            boardwalk = state.get_property_by_name("Boardwalk")
            assert boardwalk.houses == 2

            # Calculate rent with development
            rent = state.get_rent_amount("Boardwalk", dice_roll=7)
            assert rent > 50  # Base rent plus houses

        Tracking game progression::\n

            # Move to next player
            initial_player = state.current_player.name
            state.next_player()
            assert state.current_player.name != initial_player

            # Add game events
            event = GameEvent(
                type=PlayerActionType.BUY_PROPERTY,
                player="Alice",
                details="Purchased Boardwalk for $400",
                turn_number=state.turn_number
            )
            state.add_event(event)
            assert len(state.game_events) == 1

            # Check game completion
            if state.is_game_over():
                winner = state.winner
                final_rankings = state.player_rankings

        Economic analysis and strategic context::\n

            # Financial metrics
            metrics = state.economic_metrics
            assert "total_money_in_game" in metrics
            assert "average_player_wealth" in metrics

            # Property distribution analysis
            distribution = state.property_distribution
            assert "monopolies" in distribution
            assert "undeveloped_properties" in distribution

            # Player rankings by net worth
            rankings = state.player_rankings
            assert len(rankings) == len(state.players)

            # Strategic position analysis
            for player in state.players:
                position = state.get_player_strategic_position(player.name)
                assert "net_worth" in position
                assert "monopolies_owned" in position
                assert "development_potential" in position

        Advanced state operations::\n

            # Validate state consistency
            issues = state.validate_state_consistency()
            assert len(issues) == 0  # No validation errors

            # Convert for distributed gameplay
            state_dict = state.to_dict()
            restored_state = MonopolyState.from_dict(state_dict)
            assert restored_state.turn_number == state.turn_number

            # Create secure public view for AI
            public_view = state.get_public_view_for_player("Alice")
            assert "current_player" in public_view
            assert "properties" in public_view
            # Opponent private information is hidden

    Note:
        The state uses Pydantic for validation and supports both JSON serialization
        and integration with LangGraph for distributed tournament systems.
    """

    # Core game data with comprehensive player and property management
    players: list[Player] = Field(
        default_factory=list,
        description="All players in the game with complete financial profiles and strategic context",
    )

    properties: dict[str, Property] = Field(
        default_factory=dict,
        description="All properties on the board with ownership details and development status",
    )

    # Game flow state with turn and round management
    current_player_index: int = Field(
        default=0,
        ge=0,
        description="Index of the player whose turn it currently is (0-based)",
    )

    turn_number: int = Field(
        default=1, ge=1, description="Current turn number for tracking game progression"
    )

    round_number: int = Field(
        default=1,
        ge=1,
        description="Current round number (completed cycles through all players)",
    )

    game_status: GameStatus = Field(
        default=GameStatus.WAITING,
        description="Current status of the game (waiting, playing, finished, etc.)",
    )

    # Dice and movement mechanics
    last_roll: DiceRoll | None = Field(
        default=None, description="Most recent dice roll with movement information"
    )

    doubles_rolled: bool = Field(
        default=False,
        description="Whether doubles were rolled this turn (affects extra turns)",
    )

    doubles_count: int = Field(
        default=0,
        ge=0,
        le=3,
        description="Number of consecutive doubles rolled (jail on 3)",
    )

    # Card deck management
    chance_cards: list[str] = Field(
        default_factory=list, description="Shuffled deck of Chance cards"
    )

    community_chest_cards: list[str] = Field(
        default_factory=list, description="Shuffled deck of Community Chest cards"
    )

    # Game events with proper reducer for Command updates
    game_events: Annotated[list[GameEvent], add_events] = Field(
        default_factory=list,
        description="Complete history of all game events and transactions",
    )

    # Game end state
    winner: str | None = Field(
        default=None, description="Name of the winning player if game is complete"
    )

    error_message: str | None = Field(
        default=None, description="Error message if any operation failed"
    )

    # Optional messages field for LLM compatibility
    messages: list[BaseMessage] | None = Field(
        default_factory=list,
        description="Optional conversation messages for LLM compatibility",
    )

    # Resource scarcity rules (house/hotel limitations)
    houses_remaining: int = Field(
        default=32,
        ge=0,
        le=32,
        description="Number of houses available for purchase (scarcity rule)",
    )

    hotels_remaining: int = Field(
        default=12,
        ge=0,
        le=12,
        description="Number of hotels available for purchase (scarcity rule)",
    )

    # House rules and special mechanics
    free_parking_money: int = Field(
        default=0, ge=0, description="Money accumulated on Free Parking (house rule)"
    )

    jail_get_out_free_cards: dict[str, int] = Field(
        default_factory=dict, description="Get Out of Jail Free cards held by players"
    )

    @field_validator("current_player_index")
    @classmethod
    def validate_current_player_index(cls, v: int, values) -> int:
        """Validate current player index is within bounds.

        Args:
            v (int): Current player index to validate.
            values: Other field values for validation context.

        Returns:
            int: Validated current player index.
        """
        players = values.get("players", [])
        if players and v >= len(players):
            return 0  # Reset to first player if out of bounds
        return v

    @field_validator("doubles_count")
    @classmethod
    def validate_doubles_count(cls, v: int) -> int:
        """Validate doubles count doesn't exceed 3.

        Args:
            v (int): Doubles count to validate.

        Returns:
            int: Validated doubles count.
        """
        return min(v, 3)  # Maximum 3 doubles before jail

    # Computed properties with comprehensive game state analysis
    @computed_field
    @property
    def current_player(self) -> Player:
        """Get the current player with comprehensive bounds checking and
        validation.

        Returns:
            Player: The player whose turn it currently is, with defensive fallbacks.
        """
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
    def active_players(self) -> list[Player]:
        """Get list of active (non-bankrupt) players.

        Returns:
            List[Player]: All players who are still actively playing the game.
        """
        return [p for p in self.players if not p.bankrupt]

    @computed_field
    @property
    def bankrupt_players(self) -> list[Player]:
        """Get list of bankrupt players.

        Returns:
            List[Player]: All players who have been eliminated from the game.
        """
        return [p for p in self.players if p.bankrupt]

    @computed_field
    @property
    def is_game_over(self) -> bool:
        """Check if the game has reached a terminal state.

        Returns:
            bool: True if the game is over, False if gameplay should continue.
        """
        return (
            self.game_status == GameStatus.FINISHED
            or len(self.active_players) <= 1
            or self.winner is not None
        )

    @computed_field
    @property
    def economic_metrics(self) -> dict[str, int | float]:
        """Calculate comprehensive economic metrics for the game.

        Returns:
            Dict[str, Union[int, float]]: Economic analysis including money supply,
                wealth distribution, and market concentration.
        """
        if not self.players:
            return {
                "total_money_in_game": 0,
                "average_player_wealth": 0,
                "wealth_inequality": 0,
                "properties_owned": 0,
                "monopolies_count": 0,
            }

        # Calculate basic financial metrics
        total_money = sum(p.money for p in self.players)
        total_assets = sum(p.net_worth for p in self.players)

        # Wealth distribution analysis
        wealth_values = [p.net_worth for p in self.players]
        wealth_values.sort()

        # Calculate Gini coefficient for wealth inequality
        n = len(wealth_values)
        if n > 1:
            cumulative_wealth = []
            running_sum = 0
            for wealth in wealth_values:
                running_sum += wealth
                cumulative_wealth.append(running_sum)

            # Gini coefficient calculation
            gini = 0
            for i, wealth in enumerate(wealth_values):
                gini += (2 * i - n + 1) * wealth
            gini = gini / (n * sum(wealth_values)) if sum(wealth_values) > 0 else 0
        else:
            gini = 0

        # Property ownership analysis
        properties_owned = sum(len(p.properties) for p in self.players)
        monopolies_count = sum(
            1 for p in self.players for _ in self._get_player_monopolies(p.name)
        )

        return {
            "total_money_in_game": total_money,
            "total_assets_in_game": total_assets,
            "average_player_wealth": total_assets / len(self.players),
            "wealth_inequality": gini,
            "properties_owned": properties_owned,
            "properties_available": len(self.properties) - properties_owned,
            "monopolies_count": monopolies_count,
            "economic_activity_level": len(self.game_events) / max(self.turn_number, 1),
        }

    @computed_field
    @property
    def property_distribution(self) -> dict[str, Any]:
        """Analyze property distribution and development across players.

        Returns:
            Dict[str, Any]: Property distribution analysis including monopolies,
                development patterns, and strategic positions.
        """
        analysis = {
            "monopolies": {},
            "undeveloped_properties": [],
            "developed_properties": [],
            "most_valuable_properties": [],
            "strategic_positions": {},
        }

        # Analyze monopolies
        for player in self.players:
            monopolies = self._get_player_monopolies(player.name)
            if monopolies:
                analysis["monopolies"][player.name] = monopolies

        # Analyze development
        for prop_name, prop in self.properties.items():
            if prop.owner:
                if prop.houses > 0 or prop.hotels > 0:
                    analysis["developed_properties"].append(
                        {
                            "name": prop_name,
                            "owner": prop.owner,
                            "houses": prop.houses,
                            "hotels": prop.hotels,
                            "rent_value": self.get_rent_amount(prop_name),
                        }
                    )
                else:
                    analysis["undeveloped_properties"].append(
                        {
                            "name": prop_name,
                            "owner": prop.owner,
                            "development_potential": prop.type == PropertyType.STREET,
                        }
                    )

        # Find most valuable properties
        valuable_props = []
        for prop_name, prop in self.properties.items():
            if prop.owner:
                rent = self.get_rent_amount(prop_name)
                valuable_props.append(
                    {
                        "name": prop_name,
                        "owner": prop.owner,
                        "rent_value": rent,
                        "purchase_price": prop.price,
                    }
                )

        valuable_props.sort(key=lambda x: x["rent_value"], reverse=True)
        analysis["most_valuable_properties"] = valuable_props[:10]

        return analysis

    @computed_field
    @property
    def player_rankings(self) -> list[dict[str, Any]]:
        """Generate player rankings by net worth and strategic position.

        Returns:
            List[Dict[str, Any]]: Players ranked by net worth with strategic metrics.
        """
        rankings = []

        for player in self.players:
            player_data = {
                "name": player.name,
                "net_worth": player.net_worth,
                "cash": player.money,
                "properties_owned": len(player.properties),
                "monopolies_count": len(self._get_player_monopolies(player.name)),
                "bankrupt": player.bankrupt,
                "position": player.position,
                "in_jail": player.in_jail,
                "strategic_score": self._calculate_strategic_score(player.name),
            }
            rankings.append(player_data)

        # Sort by net worth descending
        rankings.sort(key=lambda x: x["net_worth"], reverse=True)

        # Add rank numbers
        for i, player_data in enumerate(rankings):
            player_data["rank"] = i + 1

        return rankings

    @computed_field
    @property
    def game_statistics(self) -> dict[str, int | float | str]:
        """Generate comprehensive game statistics and metrics.

        Returns:
            Dict[str, Union[int, float, str]]: Game statistics including duration,
                activity levels, and strategic metrics.
        """
        return {
            "turn_number": self.turn_number,
            "round_number": self.round_number,
            "game_status": self.game_status.value,
            "active_players": len(self.active_players),
            "bankrupt_players": len(self.bankrupt_players),
            "total_events": len(self.game_events),
            "properties_owned": sum(len(p.properties) for p in self.players),
            "total_properties": len(self.properties),
            "monopolies_formed": sum(
                len(self._get_player_monopolies(p.name)) for p in self.players
            ),
            "houses_built": 32 - self.houses_remaining,
            "hotels_built": 12 - self.hotels_remaining,
            "average_turns_per_round": self.turn_number / max(self.round_number, 1),
            # Normalized progress
            "game_progression": min(self.turn_number / 100, 1.0),
            "economic_activity": len(self.game_events) / max(self.turn_number, 1),
        }

    def get_player_by_name(self, name: str) -> Player | None:
        """Get player by name."""
        return next((p for p in self.players if p.name == name), None)

    def get_property_by_name(self, name: str) -> Property | None:
        """Get property by name."""
        return self.properties.get(name)

    def get_property_by_position(self, position: int) -> Property | None:
        """Get property at a specific board position."""
        return next(
            (prop for prop in self.properties.values() if prop.position == position),
            None,
        )

    def get_properties_owned_by_player(self, player_name: str) -> list[Property]:
        """Get all properties owned by a player."""
        return [prop for prop in self.properties.values() if prop.owner == player_name]

    def player_owns_monopoly(self, player_name: str, color: str) -> bool:
        """Check if player owns all properties of a color group."""

        color_group = get_properties_by_color(color)
        owned_in_group = [
            prop.name
            for prop in self.properties.values()
            if prop.owner == player_name and prop.name in color_group
        ]

        return len(owned_in_group) == len(color_group)

    def get_rent_amount(self, property_name: str, dice_roll: int = 0) -> int:
        """Calculate rent amount for a property."""

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

    def get_recent_events(self, count: int = 10) -> list[GameEvent]:
        """Get the most recent game events."""
        return self.game_events[-count:] if self.game_events else []

    def add_event(self, event: GameEvent) -> None:
        """Add a single event to the game history."""
        # This will work with the reducer when using Command updates
        self.game_events.append(event)

    @classmethod
    def from_state_object(
        cls, state: Union["MonopolyState", BaseModel, dict[str, Any]]
    ) -> "MonopolyState":
        """Convert any state object to MonopolyState.

        This is the primary method for ensuring consistency across all
        state handling.
        """
        if isinstance(state, cls):
            return state
        if isinstance(state, dict):
            return cls.from_dict(state)
        if isinstance(state, BaseModel):
            # Convert BaseModel to dict then to MonopolyState
            return cls.from_dict(state.model_dump())
        raise TypeError(f"Cannot convert {type(state)} to MonopolyState")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "MonopolyState":
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
        if data.get("last_roll") and isinstance(data["last_roll"], dict):
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

    def to_dict(self) -> dict[str, Any]:
        """Convert state to dictionary for serialization."""
        # Use model_dump for Pydantic v2 compliance
        result = self.model_dump()

        # Add computed properties
        result["current_player"] = self.current_player.model_dump()
        result["active_players"] = [p.model_dump() for p in self.active_players]
        result["bankrupt_players"] = [p.model_dump() for p in self.bankrupt_players]

        return result

    def update_player(self, player_index: int, player: Player) -> "MonopolyState":
        """Update a player and return a new state instance with proper bounds
        checking.
        """
        # Validate player_index bounds
        if not self.players:
            raise ValueError("No players in the game to update")

        if player_index < 0 or player_index >= len(self.players):
            raise ValueError(
                f"Player index {player_index} out of bounds (0-{len(self.players) - 1})"
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
        self, events: list[GameEvent], **updates
    ) -> dict[str, Any]:
        """Add events and other updates for Command usage."""
        update_dict = {"game_events": events}
        update_dict.update(updates)
        return update_dict

    def validate_state_consistency(self) -> list[str]:
        """Validate the state for consistency and return any issues found."""
        issues = []

        # Check current_player_index bounds
        if self.players:
            if self.current_player_index < 0 or self.current_player_index >= len(
                self.players
            ):
                issues.append(
                    f"current_player_index {self.current_player_index} out of bounds (0-{len(self.players) - 1})"
                )
        elif self.current_player_index != 0:
            issues.append("current_player_index should be 0 when no players exist")

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

    def _get_player_monopolies(self, player_name: str) -> list[str]:
        """Get list of color groups where player has monopoly.

        Args:
            player_name (str): Name of the player to check.

        Returns:
            List[str]: List of color groups where player owns all properties.
        """
        monopolies = []
        for color in PropertyColor:
            if self.player_owns_monopoly(player_name, color.value):
                monopolies.append(color.value)
        return monopolies

    def _calculate_strategic_score(self, player_name: str) -> float:
        """Calculate strategic score for a player.

        Args:
            player_name (str): Name of the player.

        Returns:
            float: Strategic score based on net worth, monopolies, and position.
        """
        player = self.get_player_by_name(player_name)
        if not player:
            return 0.0

        # Base score from net worth
        score = player.net_worth

        # Bonus for monopolies
        monopolies = len(self._get_player_monopolies(player_name))
        score += monopolies * 500

        # Penalty for being in jail
        if player.in_jail:
            score -= 100

        # Bonus for development potential
        developable_props = sum(
            1
            for prop_name in player.properties
            if self.properties.get(prop_name, Property()).type == PropertyType.STREET
        )
        score += developable_props * 50

        return score

    def get_player_strategic_position(self, player_name: str) -> dict[str, Any]:
        """Get comprehensive strategic position analysis for a player.

        Args:
            player_name (str): Name of the player to analyze.

        Returns:
            Dict[str, Any]: Strategic position analysis including strengths and weaknesses.
        """
        player = self.get_player_by_name(player_name)
        if not player:
            return {}

        monopolies = self._get_player_monopolies(player_name)
        properties_owned = len(player.properties)

        # Calculate development potential
        developable_props = [
            prop_name
            for prop_name in player.properties
            if self.properties.get(prop_name, Property()).type == PropertyType.STREET
        ]

        # Assess financial position
        financial_strength = (
            "Strong"
            if player.money > 500
            else "Weak" if player.money < 200 else "Moderate"
        )

        return {
            "player_name": player_name,
            "net_worth": player.net_worth,
            "cash_position": player.money,
            "properties_owned": properties_owned,
            "monopolies_owned": monopolies,
            "monopoly_count": len(monopolies),
            "development_potential": len(developable_props),
            "financial_strength": financial_strength,
            "strategic_score": self._calculate_strategic_score(player_name),
            "position_on_board": player.position,
            "in_jail": player.in_jail,
            "bankrupt": player.bankrupt,
        }

    def get_public_view_for_player(self, player_name: str) -> dict[str, Any]:
        """Generate a secure public view of the game state for a specific
        player.

        This method creates a view that contains all information a player should
        legitimately know while hiding private information from other players.

        Args:
            player_name (str): Name of the player requesting the view.

        Returns:
            Dict[str, Any]: Public state information for the player.
        """
        public_view = {
            "game_status": self.game_status.value,
            "turn_number": self.turn_number,
            "round_number": self.round_number,
            "current_player": self.current_player.name,
            "is_your_turn": self.current_player.name == player_name,
            "last_roll": self.last_roll.model_dump() if self.last_roll else None,
            "doubles_rolled": self.doubles_rolled,
            "houses_remaining": self.houses_remaining,
            "hotels_remaining": self.hotels_remaining,
            "free_parking_money": self.free_parking_money,
            "winner": self.winner,
            "game_over": self.is_game_over,
        }

        # Add all players' public information
        public_view["players"] = []
        for player in self.players:
            player_info = {
                "name": player.name,
                "money": player.money,
                "position": player.position,
                "in_jail": player.in_jail,
                "bankrupt": player.bankrupt,
                "properties_owned": len(player.properties),
                "net_worth": player.net_worth,
            }

            # Add detailed information for the requesting player
            if player.name == player_name:
                player_info["properties"] = player.properties
                player_info["jail_turns"] = player.jail_turns
                player_info["get_out_of_jail_free_cards"] = (
                    self.jail_get_out_free_cards.get(player.name, 0)
                )

            public_view["players"].append(player_info)

        # Add property information
        public_view["properties"] = {}
        for prop_name, prop in self.properties.items():
            public_view["properties"][prop_name] = {
                "name": prop.name,
                "price": prop.price,
                "owner": prop.owner,
                "houses": prop.houses,
                "hotels": prop.hotels,
                "mortgaged": prop.mortgaged,
                "type": prop.type.value if prop.type else None,
                "color": prop.color.value if prop.color else None,
                "rent": self.get_rent_amount(prop_name),
            }

        # Add recent game events
        public_view["recent_events"] = [
            event.model_dump() for event in self.get_recent_events(10)
        ]

        # Add economic metrics
        public_view["economic_metrics"] = self.economic_metrics

        return public_view

    model_config = {"arbitrary_types_allowed": True}
