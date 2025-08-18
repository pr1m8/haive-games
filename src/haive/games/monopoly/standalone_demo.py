"""Standalone Monopoly demo with minimal dependencies.

This script provides a self-contained demonstration of the Monopoly game
without relying on external dependencies like langchain.

Usage:
    python standalone_demo.py

"""

import random
import time
import traceback
from dataclasses import dataclass, field
from enum import Enum


# Define enums for property types and colors
class PropertyType(str, Enum):
    STREET = "street"
    RAILROAD = "railroad"
    UTILITY = "utility"
    SPECIAL = "special"


class PropertyColor(str, Enum):
    BROWN = "brown"
    LIGHT_BLUE = "light_blue"
    PINK = "pink"
    ORANGE = "orange"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    DARK_BLUE = "dark_blue"
    RAILROAD = "railroad"
    UTILITY = "utility"
    SPECIAL = "special"


# Define basic data models
@dataclass
class Property:
    name: str
    position: int
    property_type: PropertyType
    color: PropertyColor
    price: int
    rent: list[int]
    house_cost: int = 0
    mortgage_value: int = 0
    owner: str | None = None
    houses: int = 0
    hotel: bool = False
    mortgaged: bool = False


@dataclass
class Player:
    name: str
    money: int = 1500
    position: int = 0
    properties: list[str] = field(default_factory=list)
    jail_cards: int = 0
    in_jail: bool = False
    jail_turns: int = 0
    doubles_count: int = 0
    bankrupt: bool = False

    def can_afford(self, amount: int) -> bool:
        """Can Afford.

Args:
    amount: [TODO: Add description]

Returns:
    [TODO: Add return description]
"""
        return self.money >= amount


@dataclass
class DiceRoll:
    die1: int
    die2: int

    @property
    def total(self) -> int:
        """Total.

Returns:
    [TODO: Add return description]
"""
        return self.die1 + self.die2

    @property
    def is_doubles(self) -> bool:
        """Is Doubles.

Returns:
    [TODO: Add return description]
"""
        return self.die1 == self.die2


@dataclass
class GameEvent:
    event_type: str
    player: str
    description: str
    money_change: int = 0
    property_involved: str | None = None
    details: dict = field(default_factory=dict)


@dataclass
class GameState:
    players: list[Player]
    properties: dict[str, Property]
    current_player_index: int = 0
    turn_number: int = 1
    game_events: list[GameEvent] = field(default_factory=list)
    last_roll: DiceRoll | None = None

    @property
    def current_player(self) -> Player:
        """Current Player.

Returns:
    [TODO: Add return description]
"""
        if not self.players:
            return Player(name="Unknown")
        if 0 <= self.current_player_index < len(self.players):
            return self.players[self.current_player_index]
        return self.players[0] if self.players else Player(name="Unknown")

    @property
    def active_players(self) -> list[Player]:
        """Active Players.

Returns:
    [TODO: Add return description]
"""
        return [p for p in self.players if not p.bankrupt]

    def next_player(self) -> None:
        """Next Player.

Returns:
    [TODO: Add return description]
"""
        if len(self.active_players) <= 1:
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

        self.turn_number += 1


# Board properties definitions
BOARD_PROPERTIES = {
    0: {"name": "GO", "type": PropertyType.SPECIAL, "color": PropertyColor.SPECIAL},
    1: {
        "name": "Mediterranean Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.BROWN,
        "price": 60,
        "rent": [2, 10, 30, 90, 160, 250],
        "house_cost": 50,
        "mortgage_value": 30,
    },
    2: {
        "name": "Community Chest",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    3: {
        "name": "Baltic Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.BROWN,
        "price": 60,
        "rent": [4, 20, 60, 180, 320, 450],
        "house_cost": 50,
        "mortgage_value": 30,
    },
    4: {
        "name": "Income Tax",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    5: {
        "name": "Reading Railroad",
        "type": PropertyType.RAILROAD,
        "color": PropertyColor.RAILROAD,
        "price": 200,
        "rent": [25, 50, 100, 200],
        "mortgage_value": 100,
    },
    6: {
        "name": "Oriental Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.LIGHT_BLUE,
        "price": 100,
        "rent": [6, 30, 90, 270, 400, 550],
        "house_cost": 50,
        "mortgage_value": 50,
    },
    7: {"name": "Chance", "type": PropertyType.SPECIAL, "color": PropertyColor.SPECIAL},
    8: {
        "name": "Vermont Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.LIGHT_BLUE,
        "price": 100,
        "rent": [6, 30, 90, 270, 400, 550],
        "house_cost": 50,
        "mortgage_value": 50,
    },
    9: {
        "name": "Connecticut Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.LIGHT_BLUE,
        "price": 120,
        "rent": [8, 40, 100, 300, 450, 600],
        "house_cost": 50,
        "mortgage_value": 60,
    },
    10: {"name": "Jail", "type": PropertyType.SPECIAL, "color": PropertyColor.SPECIAL},
    11: {
        "name": "St. Charles Place",
        "type": PropertyType.STREET,
        "color": PropertyColor.PINK,
        "price": 140,
        "rent": [10, 50, 150, 450, 625, 750],
        "house_cost": 100,
        "mortgage_value": 70,
    },
    12: {
        "name": "Electric Company",
        "type": PropertyType.UTILITY,
        "color": PropertyColor.UTILITY,
        "price": 150,
        "rent": [4, 10],
        "mortgage_value": 75,
    },
    # Rest of the board properties...
    # (Adding key properties for brevity, full board would have positions 0-39)
    20: {
        "name": "Free Parking",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    30: {
        "name": "Go To Jail",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    38: {
        "name": "Luxury Tax",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    39: {
        "name": "Boardwalk",
        "type": PropertyType.STREET,
        "color": PropertyColor.DARK_BLUE,
        "price": 400,
        "rent": [50, 200, 600, 1400, 1700, 2000],
        "house_cost": 200,
        "mortgage_value": 200,
    },
}


# Helper functions
def create_board() -> dict[str, Property]:
    """Create the initial board with all properties."""
    properties = {}

    for position, prop_data in BOARD_PROPERTIES.items():
        # Create ALL properties, including special ones
        property_type = PropertyType(prop_data["type"])

        # For regular properties, include all details
        if property_type != PropertyType.SPECIAL:
            properties[prop_data["name"]] = Property(
                name=prop_data["name"],
                position=position,
                property_type=property_type,
                color=PropertyColor(prop_data["color"]),
                price=prop_data.get("price", 0),
                rent=prop_data.get("rent", [0, 0, 0, 0, 0, 0]),
                house_cost=prop_data.get("house_cost", 0),
                mortgage_value=prop_data.get("mortgage_value", 0),
            )
        # For special properties, create minimal Property objects
        else:
            properties[prop_data["name"]] = Property(
                name=prop_data["name"],
                position=position,
                property_type=property_type,
                color=PropertyColor(prop_data["color"]),
                price=0,
                rent=[0, 0, 0, 0, 0, 0],
                house_cost=0,
                mortgage_value=0,
            )

    return properties


def create_players(player_names: list[str]) -> list[Player]:
    """Create initial players."""
    return [Player(name=name) for name in player_names]


def roll_dice() -> DiceRoll:
    """Roll two dice."""
    return DiceRoll(die1=random.randint(1, 6), die2=random.randint(1, 6))


def move_player(player: Player, dice_roll: DiceRoll) -> tuple[int, bool]:
    """Move a player based on dice roll."""
    old_position = player.position
    new_position = (old_position + dice_roll.total) % 40
    passed_go = new_position < old_position and new_position != 0

    player.position = new_position
    return new_position, passed_go


def get_property_at_position(position: int) -> dict | None:
    """Get property information at a board position."""
    return BOARD_PROPERTIES.get(position)


def calculate_rent(
    property_obj: Property, state: GameState, dice_roll: int | None = None
) -> int:
    """Calculate rent for a property."""
    if not property_obj.owner or property_obj.mortgaged:
        return 0

    if property_obj.property_type == PropertyType.RAILROAD:
        # Count railroads owned by the same player
        railroads_owned = sum(
            1
            for prop in state.properties.values()
            if (
                prop.property_type == PropertyType.RAILROAD
                and prop.owner == property_obj.owner
                and not prop.mortgaged
            )
        )
        return property_obj.rent[min(railroads_owned - 1, 3)]

    if property_obj.property_type == PropertyType.UTILITY:
        if dice_roll is None:
            return 0

        # Count utilities owned by the same player
        utilities_owned = sum(
            1
            for prop in state.properties.values()
            if (
                prop.property_type == PropertyType.UTILITY
                and prop.owner == property_obj.owner
                and not prop.mortgaged
            )
        )

        multiplier = (
            property_obj.rent[0] if utilities_owned == 1 else property_obj.rent[1]
        )
        return dice_roll * multiplier

    if property_obj.property_type == PropertyType.STREET:
        if property_obj.hotel:
            return property_obj.rent[5]
        if property_obj.houses > 0:
            return property_obj.rent[property_obj.houses]
        return property_obj.rent[0]

    return 0


# ANSI color codes for terminal output
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


# UI helper functions
def print_divider():
    """Print a divider line."""


def print_property(property_obj: Property):
    """Print property details."""
    if property_obj.property_type == PropertyType.SPECIAL:
        return

    if property_obj.mortgaged or property_obj.hotel:
        pass
    elif property_obj.houses > 0:
        "■ " * property_obj.houses


def print_player_status(state: GameState):
    """Print current status of all players."""
    table = state.players.copy()
    # Sort so current player is first
    if state.current_player_index < len(table):
        current = table[state.current_player_index]
        table.pop(state.current_player_index)
        table.insert(0, current)

    for player in table:
        if player.properties:
            ", ".join(player.properties)

        if player.in_jail:
            pass

        if player.bankrupt:
            pass

        # Print current position name
        position = player.position
        position_data = get_property_at_position(position)
        if position_data:
            pass
        else:
            pass


def print_recent_events(events: list[GameEvent], count: int = 5):
    """Print recent game events."""
    if not events:
        return

    recent = events[-count:]

    for event in reversed(recent):
        # Style based on event type
        if (
            event.event_type in ["property_purchase", "rent_payment"]
            or event.event_type in ["bankruptcy", "go_to_jail"]
            or event.event_type == "dice_roll"
        ):
            pass
        else:
            pass

        # Money indicator
        if event.money_change > 0 or event.money_change < 0:
            pass


def handle_property_landing(state: GameState, position: int) -> list[GameEvent]:
    """Handle a player landing on a property."""
    events = []
    current_player = state.current_player

    # Get position data
    position_data = get_property_at_position(position)
    if not position_data:
        return events

    property_name = position_data["name"]

    # Handle special positions
    if position_data["type"] == PropertyType.SPECIAL:
        if property_name == "Income Tax":
            tax = 200
            current_player.money -= tax
            events.append(
                GameEvent(
                    event_type="tax_payment",
                    player=current_player.name,
                    description=f"Paid ${tax} Income Tax",
                    money_change=-tax,
                )
            )
        elif property_name == "Luxury Tax":
            tax = 75
            current_player.money -= tax
            events.append(
                GameEvent(
                    event_type="tax_payment",
                    player=current_player.name,
                    description=f"Paid ${tax} Luxury Tax",
                    money_change=-tax,
                )
            )
        elif property_name == "Go To Jail":
            current_player.position = 10  # Jail position
            current_player.in_jail = True
            events.append(
                GameEvent(
                    event_type="go_to_jail",
                    player=current_player.name,
                    description="Sent to Jail",
                )
            )
        elif property_name in ["Chance", "Community Chest"]:
            pass
        else:
            pass

        return events

    # Handle regular property
    property_obj = state.properties.get(property_name)

    if not property_obj:
        # Create property from board data
        property_obj = Property(
            name=property_name,
            position=position,
            property_type=PropertyType(position_data["type"]),
            color=PropertyColor(position_data["color"]),
            price=position_data.get("price", 0),
            rent=position_data.get("rent", [0, 0, 0, 0, 0, 0]),
            house_cost=position_data.get("house_cost", 0),
            mortgage_value=position_data.get("mortgage_value", 0),
        )

        # Add to state
        state.properties[property_name] = property_obj

        events.append(
            GameEvent(
                event_type="property_added",
                player=current_player.name,
                description=f"Property {property_name} added to game",
                property_involved=property_name,
            )
        )

    print_property(property_obj)

    # Check if property is owned
    if property_obj.owner is None:
        # Property is unowned - offer to buy
        if property_obj.price <= current_player.money:
            # In this demo, always buy if can afford
            current_player.money -= property_obj.price
            current_player.properties.append(property_name)
            property_obj.owner = current_player.name

            events.append(
                GameEvent(
                    event_type="property_purchase",
                    player=current_player.name,
                    description=f"Purchased {property_name}",
                    money_change=-property_obj.price,
                    property_involved=property_name,
                )
            )
        else:
            events.append(
                GameEvent(
                    event_type="property_pass",
                    player=current_player.name,
                    description=f"Could not afford {property_name}",
                    property_involved=property_name,
                )
            )
    elif property_obj.owner == current_player.name:
        pass
    else:
        # Pay rent to owner
        owner = None
        for player in state.players:
            if player.name == property_obj.owner:
                owner = player
                break

        if not owner:
            return events

        # Calculate rent
        dice_total = state.last_roll.total if state.last_roll else 0
        rent = calculate_rent(property_obj, state, dice_total)

        if rent <= 0:
            return events

        # Pay rent
        if current_player.money >= rent:
            current_player.money -= rent
            owner.money += rent

            events.append(
                GameEvent(
                    event_type="rent_payment",
                    player=current_player.name,
                    description=f"Paid ${rent} rent to {owner.name}",
                    money_change=-rent,
                    property_involved=property_name,
                )
            )
        else:
            # Simplified bankruptcy
            current_player.bankrupt = True

            events.append(
                GameEvent(
                    event_type="bankruptcy",
                    player=current_player.name,
                    description=f"Went bankrupt owing ${rent} rent to {owner.name}",
                    property_involved=property_name,
                )
            )

    return events


def run_demo(turns: int = 10):
    """Run a simple Monopoly game demo."""
    # Initialize game state
    players = create_players(["Alice", "Bob", "Charlie"])
    properties = create_board()

    # Ensure Vermont Avenue exists in properties
    if "Vermont Avenue" not in properties:
        # Get position 8 (Vermont Avenue)
        vermont_data = get_property_at_position(8)
        if vermont_data:
            properties["Vermont Avenue"] = Property(
                name="Vermont Avenue",
                position=8,
                property_type=PropertyType.STREET,
                color=PropertyColor.LIGHT_BLUE,
                price=100,
                rent=[6, 30, 90, 270, 400, 550],
                house_cost=50,
                mortgage_value=50,
            )

    state = GameState(
        players=players,
        properties=properties,
        current_player_index=0,
        turn_number=1,
        game_events=[],
    )

    # Show initial state
    print_player_status(state)

    # Game loop
    for _turn in range(1, turns + 1):
        if len(state.active_players) <= 1:
            break

        current_player = state.current_player

        if current_player.bankrupt:
            state.next_player()
            continue

        print_divider()

        # Roll dice
        dice = roll_dice()
        state.last_roll = dice

        state.game_events.append(
            GameEvent(
                event_type="dice_roll",
                player=current_player.name,
                description=f"Rolled {dice.die1} and {dice.die2} for {dice.total}",
                details={"dice": [dice.die1, dice.die2]},
            )
        )

        # Handle jail
        if current_player.in_jail:
            if dice.is_doubles:
                current_player.in_jail = False
                state.game_events.append(
                    GameEvent(
                        event_type="jail_release",
                        player=current_player.name,
                        description="Got out of jail by rolling doubles",
                    )
                )
            else:
                current_player.jail_turns += 1
                if current_player.jail_turns >= 3:
                    # Must pay to get out after 3 turns
                    if current_player.money >= 50:
                        current_player.money -= 50
                        current_player.in_jail = False
                        state.game_events.append(
                            GameEvent(
                                event_type="jail_release",
                                player=current_player.name,
                                description="Paid $50 to get out of jail after 3 turns",
                                money_change=-50,
                            )
                        )
                    else:
                        # Simplified bankruptcy
                        current_player.bankrupt = True
                        state.game_events.append(
                            GameEvent(
                                event_type="bankruptcy",
                                player=current_player.name,
                                description="Went bankrupt unable to pay jail fine",
                            )
                        )
                        state.next_player()
                        continue
                else:
                    state.game_events.append(
                        GameEvent(
                            event_type="jail_stay",
                            player=current_player.name,
                            description=f"Stays in jail (turn {
                                current_player.jail_turns
                            }/3)",
                        )
                    )
                    state.next_player()
                    continue

        # Move player
        new_position, passed_go = move_player(current_player, dice)

        # Handle passing GO
        if passed_go:
            current_player.money += 200
            state.game_events.append(
                GameEvent(
                    event_type="pass_go",
                    player=current_player.name,
                    description="Passed GO and collected $200",
                    money_change=200,
                )
            )

        # Handle landing on property
        events = handle_property_landing(state, new_position)
        state.game_events.extend(events)

        # Print recent events and status
        print_recent_events(state.game_events)
        print_player_status(state)

        # Next player
        state.next_player()

        # Brief pause between turns for readability

        time.sleep(1)

    # Game summary
    print_divider()

    # Determine winner
    active_players = state.active_players
    if len(active_players) == 1:
        active_players[0]
    else:
        # Find player with highest money (simplified)
        best_player = None
        best_money = -1

        for player in active_players:
            if player.money > best_money:
                best_money = player.money
                best_player = player

        if best_player:
            pass

    # Print final player status
    print_player_status(state)

    # Print statistics
    property_owners = {}
    for prop_name, prop in state.properties.items():
        if prop.owner:
            if prop.owner not in property_owners:
                property_owners[prop.owner] = []
            property_owners[prop.owner].append(prop_name)

    for _owner, props in property_owners.items():
        for prop in props:
            pass


if __name__ == "__main__":
    try:
        run_demo(10)
    except KeyboardInterrupt:
        pass
    except Exception:
        traceback.print_exc()
    finally:
        pass
