"""Standalone Monopoly demo with minimal dependencies.

This script provides a self-contained demonstration of the Monopoly game
without relying on external dependencies like langchain.

Usage:
    python standalone_demo.py
"""

import random
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
        return self.money >= amount


@dataclass
class DiceRoll:
    die1: int
    die2: int

    @property
    def total(self) -> int:
        return self.die1 + self.die2

    @property
    def is_doubles(self) -> bool:
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
        if not self.players:
            return Player(name="Unknown")
        if 0 <= self.current_player_index < len(self.players):
            return self.players[self.current_player_index]
        return self.players[0] if self.players else Player(name="Unknown")

    @property
    def active_players(self) -> list[Player]:
        return [p for p in self.players if not p.bankrupt]

    def next_player(self) -> None:
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
                rent=prop_data.get("rent", [0]),
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
                rent=[0],
                house_cost=0,
                mortgage_value=0,
            )

    print(f"Created {len(properties)} properties")
    print(f"Properties include 'Vermont Avenue': {'Vermont Avenue' in properties}")

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
    print(Color.CYAN + "=" * 80 + Color.RESET)


def print_property(property_obj: Property):
    """Print property details."""
    if property_obj.property_type == PropertyType.SPECIAL:
        print(f"{Color.BOLD}{property_obj.name}{Color.RESET} (Special)")
        return

    owner_text = f"Owned by {property_obj.owner}" if property_obj.owner else "Unowned"

    print(
        f"{Color.BOLD}{property_obj.name}{Color.RESET} - Price: ${property_obj.price} - {owner_text}"
    )
    print(f"  Rent: ${property_obj.rent[0]}")

    if property_obj.mortgaged:
        print(f"  {Color.RED}MORTGAGED{Color.RESET} for ${property_obj.mortgage_value}")
    elif property_obj.hotel:
        print(
            f"  {Color.RED}{Color.BOLD}HOTEL{Color.RESET} - Rent: ${property_obj.rent[5]}"
        )
    elif property_obj.houses > 0:
        houses = "■ " * property_obj.houses
        print(
            f"  {Color.GREEN}{houses}{Color.RESET} - Rent: ${property_obj.rent[property_obj.houses]}"
        )


def print_player_status(state: GameState):
    """Print current status of all players."""
    print("\n" + Color.BOLD + "Player Status:" + Color.RESET)

    table = state.players.copy()
    # Sort so current player is first
    if state.current_player_index < len(table):
        current = table[state.current_player_index]
        table.pop(state.current_player_index)
        table.insert(0, current)

    for player in table:
        is_current = player.name == state.current_player.name
        name_style = f"{Color.GREEN}{Color.BOLD}" if is_current else Color.BOLD

        print(f"{name_style}{player.name}{Color.RESET} - ${player.money}")

        if player.properties:
            property_text = ", ".join(player.properties)
            print(f"  Properties: {property_text}")

        if player.in_jail:
            print(f"  {Color.RED}IN JAIL{Color.RESET} (Turn {player.jail_turns}/3)")

        if player.bankrupt:
            print(f"  {Color.RED}BANKRUPT{Color.RESET}")

        # Print current position name
        position = player.position
        position_data = get_property_at_position(position)
        if position_data:
            print(f"  Position: {position_data['name']} ({position})")
        else:
            print(f"  Position: {position}")

        print("")


def print_recent_events(events: list[GameEvent], count: int = 5):
    """Print recent game events."""
    if not events:
        return

    recent = events[-count:]
    print("\n" + Color.BOLD + "Recent Events:" + Color.RESET)

    for event in reversed(recent):
        # Style based on event type
        if event.event_type in ["property_purchase", "rent_payment"]:
            style = Color.GREEN
        elif event.event_type in ["bankruptcy", "go_to_jail"]:
            style = Color.RED
        elif event.event_type == "dice_roll":
            style = Color.CYAN
        else:
            style = ""

        # Money indicator
        money_indicator = ""
        if event.money_change > 0:
            money_indicator = f" {Color.GREEN}(+${event.money_change}){Color.RESET}"
        elif event.money_change < 0:
            money_indicator = f" {Color.RED}(${event.money_change}){Color.RESET}"

        print(
            f"• {Color.BOLD}{event.player}{Color.RESET}: {style}{event.description}{Color.RESET}{money_indicator}"
        )


def handle_property_landing(state: GameState, position: int) -> list[GameEvent]:
    """Handle a player landing on a property."""
    events = []
    current_player = state.current_player

    # Get position data
    position_data = get_property_at_position(position)
    if not position_data:
        print(f"{Color.RED}Error: Invalid position {position}{Color.RESET}")
        return events

    property_name = position_data["name"]
    print(
        f"\n{Color.BOLD}🎯 {current_player.name} landed on {property_name}{Color.RESET}"
    )

    # Handle special positions
    if position_data["type"] == PropertyType.SPECIAL:
        if property_name == "Income Tax":
            tax = 200
            current_player.money -= tax
            print(f"{Color.RED}Paid ${tax} in Income Tax{Color.RESET}")
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
            print(f"{Color.RED}Paid ${tax} in Luxury Tax{Color.RESET}")
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
            print(f"{Color.RED}Go to Jail! Moving to Jail...{Color.RESET}")
            events.append(
                GameEvent(
                    event_type="go_to_jail",
                    player=current_player.name,
                    description="Sent to Jail",
                )
            )
        elif property_name in ["Chance", "Community Chest"]:
            print(
                f"{Color.YELLOW}Draw a {property_name} card (not implemented in demo){Color.RESET}"
            )
        else:
            print(f"{Color.BLUE}On {property_name} - no action needed{Color.RESET}")

        return events

    # Handle regular property
    property_obj = state.properties.get(property_name)

    if not property_obj:
        print(
            f"{Color.RED}Warning: Property '{property_name}' not found in state.{Color.RESET}"
        )
        print("Creating property from board data...")

        # Create property from board data
        property_obj = Property(
            name=property_name,
            position=position,
            property_type=PropertyType(position_data["type"]),
            color=PropertyColor(position_data["color"]),
            price=position_data.get("price", 0),
            rent=position_data.get("rent", [0]),
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
            print(
                f"\n{Color.GREEN}Buying {property_name} for ${property_obj.price}{Color.RESET}"
            )
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
            print(
                f"\n{Color.RED}Cannot afford {property_name} (${property_obj.price}){Color.RESET}"
            )
            events.append(
                GameEvent(
                    event_type="property_pass",
                    player=current_player.name,
                    description=f"Could not afford {property_name}",
                    property_involved=property_name,
                )
            )
    elif property_obj.owner == current_player.name:
        print(f"\n{Color.BLUE}You own this property - no action needed{Color.RESET}")
    else:
        # Pay rent to owner
        owner = None
        for player in state.players:
            if player.name == property_obj.owner:
                owner = player
                break

        if not owner:
            print(
                f"{Color.RED}Error: Owner '{property_obj.owner}' not found{Color.RESET}"
            )
            return events

        # Calculate rent
        dice_total = state.last_roll.total if state.last_roll else 0
        rent = calculate_rent(property_obj, state, dice_total)

        if rent <= 0:
            print(
                f"\n{Color.BLUE}No rent due (property mortgaged or special circumstances){Color.RESET}"
            )
            return events

        print(
            f"\n{Color.YELLOW}Property owned by {owner.name} - rent: ${rent}{Color.RESET}"
        )

        # Pay rent
        if current_player.money >= rent:
            current_player.money -= rent
            owner.money += rent

            print(f"{Color.RED}Paid ${rent} in rent to {owner.name}{Color.RESET}")

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
            print(
                f"{Color.RED}{Color.BOLD}Cannot afford ${rent} rent - {current_player.name} goes BANKRUPT!{Color.RESET}"
            )
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
        print("WARNING: Vermont Avenue not in properties!")
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

    print(f"{Color.GREEN}{Color.BOLD}🎮 MONOPOLY DEMO{Color.RESET}")
    print("A simplified demonstration of the Monopoly game\n")

    # Show initial state
    print_player_status(state)

    # Game loop
    for turn in range(1, turns + 1):
        if len(state.active_players) <= 1:
            print(
                f"{Color.RED}{Color.BOLD}Game over - only one player remains!{Color.RESET}"
            )
            break

        current_player = state.current_player

        if current_player.bankrupt:
            print(
                f"{Color.RED}{current_player.name} is bankrupt - skipping turn{Color.RESET}"
            )
            state.next_player()
            continue

        print_divider()
        print(f"{Color.BOLD}Turn {turn}: {current_player.name}'s turn{Color.RESET}")

        # Roll dice
        dice = roll_dice()
        state.last_roll = dice

        print(
            f"\n🎲 {Color.BOLD}{current_player.name}{Color.RESET} rolls: {dice.die1} + {dice.die2} = {dice.total}"
        )
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
                print(f"{Color.GREEN}Rolled doubles! Out of jail!{Color.RESET}")
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
                        print(
                            f"{Color.YELLOW}Paid $50 to get out of jail after 3 turns{Color.RESET}"
                        )
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
                        print(
                            f"{Color.RED}{Color.BOLD}Cannot afford jail fine - goes BANKRUPT!{Color.RESET}"
                        )
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
                    print(
                        f"{Color.RED}Stays in jail (turn {current_player.jail_turns}/3){Color.RESET}"
                    )
                    state.game_events.append(
                        GameEvent(
                            event_type="jail_stay",
                            player=current_player.name,
                            description=f"Stays in jail (turn {current_player.jail_turns}/3)",
                        )
                    )
                    state.next_player()
                    continue

        # Move player
        old_position = current_player.position
        new_position, passed_go = move_player(current_player, dice)

        print(f"\n🚶 Moves from {old_position} to {new_position}")

        # Handle passing GO
        if passed_go:
            current_player.money += 200
            print(f"{Color.GREEN}Passed GO! Collect $200{Color.RESET}")
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
        print("\n...Next turn in 1 second...")
        import time

        time.sleep(1)

    # Game summary
    print_divider()
    print(f"{Color.GREEN}{Color.BOLD}🏁 Game Summary{Color.RESET}")

    # Determine winner
    active_players = state.active_players
    if len(active_players) == 1:
        winner = active_players[0]
        print(
            f"{Color.GREEN}{Color.BOLD}Winner: {winner.name} with ${winner.money}{Color.RESET}"
        )
    else:
        # Find player with highest money (simplified)
        best_player = None
        best_money = -1

        for player in active_players:
            if player.money > best_money:
                best_money = player.money
                best_player = player

        if best_player:
            print(
                f"{Color.GREEN}{Color.BOLD}Highest money: {best_player.name} with ${best_money}{Color.RESET}"
            )

    # Print final player status
    print_player_status(state)

    # Print statistics
    property_owners = {}
    for prop_name, prop in state.properties.items():
        if prop.owner:
            if prop.owner not in property_owners:
                property_owners[prop.owner] = []
            property_owners[prop.owner].append(prop_name)

    print(f"\n{Color.BOLD}Property Ownership:{Color.RESET}")
    for owner, props in property_owners.items():
        print(f"{Color.BOLD}{owner}{Color.RESET}: {len(props)} properties")
        for prop in props:
            print(f"  • {prop}")


if __name__ == "__main__":
    print("Starting Monopoly standalone demo...")
    try:
        run_demo(10)
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback

        traceback.print_exc()
    finally:
        print("\nThanks for playing!")
