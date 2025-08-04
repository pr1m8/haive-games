"""Monopoly game utilities and board logic.

This module provides utility functions for the monopoly game, including:
    - Board setup and property definitions
    - Game logic calculations
    - Card definitions and handling
    - Rent calculations

"""

import random
from typing import TYPE_CHECKING, Any

from haive.games.monopoly.models import (
    DiceRoll,
    Player,
    Property,
    PropertyColor,
    PropertyType,
)

if TYPE_CHECKING:
    from haive.games.monopoly.state import MonopolyState

# Board positions and property definitions
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
        "rent": [4, 10],  # 4x dice if own 1, 10x dice if own both
        "mortgage_value": 75,
    },
    13: {
        "name": "States Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.PINK,
        "price": 140,
        "rent": [10, 50, 150, 450, 625, 750],
        "house_cost": 100,
        "mortgage_value": 70,
    },
    14: {
        "name": "Virginia Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.PINK,
        "price": 160,
        "rent": [12, 60, 180, 500, 700, 900],
        "house_cost": 100,
        "mortgage_value": 80,
    },
    15: {
        "name": "Pennsylvania Railroad",
        "type": PropertyType.RAILROAD,
        "color": PropertyColor.RAILROAD,
        "price": 200,
        "rent": [25, 50, 100, 200],
        "mortgage_value": 100,
    },
    16: {
        "name": "St. James Place",
        "type": PropertyType.STREET,
        "color": PropertyColor.ORANGE,
        "price": 180,
        "rent": [14, 70, 200, 550, 750, 950],
        "house_cost": 100,
        "mortgage_value": 90,
    },
    17: {
        "name": "Community Chest",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    18: {
        "name": "Tennessee Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.ORANGE,
        "price": 180,
        "rent": [14, 70, 200, 550, 750, 950],
        "house_cost": 100,
        "mortgage_value": 90,
    },
    19: {
        "name": "New York Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.ORANGE,
        "price": 200,
        "rent": [16, 80, 220, 600, 800, 1000],
        "house_cost": 100,
        "mortgage_value": 100,
    },
    20: {
        "name": "Free Parking",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    21: {
        "name": "Kentucky Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.RED,
        "price": 220,
        "rent": [18, 90, 250, 700, 875, 1050],
        "house_cost": 150,
        "mortgage_value": 110,
    },
    22: {
        "name": "Chance",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    23: {
        "name": "Indiana Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.RED,
        "price": 220,
        "rent": [18, 90, 250, 700, 875, 1050],
        "house_cost": 150,
        "mortgage_value": 110,
    },
    24: {
        "name": "Illinois Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.RED,
        "price": 240,
        "rent": [20, 100, 300, 750, 925, 1100],
        "house_cost": 150,
        "mortgage_value": 120,
    },
    25: {
        "name": "B&O Railroad",
        "type": PropertyType.RAILROAD,
        "color": PropertyColor.RAILROAD,
        "price": 200,
        "rent": [25, 50, 100, 200],
        "mortgage_value": 100,
    },
    26: {
        "name": "Atlantic Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.YELLOW,
        "price": 260,
        "rent": [22, 110, 330, 800, 975, 1150],
        "house_cost": 150,
        "mortgage_value": 130,
    },
    27: {
        "name": "Ventnor Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.YELLOW,
        "price": 260,
        "rent": [22, 110, 330, 800, 975, 1150],
        "house_cost": 150,
        "mortgage_value": 130,
    },
    28: {
        "name": "Water Works",
        "type": PropertyType.UTILITY,
        "color": PropertyColor.UTILITY,
        "price": 150,
        "rent": [4, 10],  # 4x dice if own 1, 10x dice if own both
        "mortgage_value": 75,
    },
    29: {
        "name": "Marvin Gardens",
        "type": PropertyType.STREET,
        "color": PropertyColor.YELLOW,
        "price": 280,
        "rent": [24, 120, 360, 850, 1025, 1200],
        "house_cost": 150,
        "mortgage_value": 140,
    },
    30: {
        "name": "Go To Jail",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    31: {
        "name": "Pacific Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.GREEN,
        "price": 300,
        "rent": [26, 130, 390, 900, 1100, 1275],
        "house_cost": 200,
        "mortgage_value": 150,
    },
    32: {
        "name": "North Carolina Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.GREEN,
        "price": 300,
        "rent": [26, 130, 390, 900, 1100, 1275],
        "house_cost": 200,
        "mortgage_value": 150,
    },
    33: {
        "name": "Community Chest",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    34: {
        "name": "Pennsylvania Avenue",
        "type": PropertyType.STREET,
        "color": PropertyColor.GREEN,
        "price": 320,
        "rent": [28, 150, 450, 1000, 1200, 1400],
        "house_cost": 200,
        "mortgage_value": 160,
    },
    35: {
        "name": "Short Line",
        "type": PropertyType.RAILROAD,
        "color": PropertyColor.RAILROAD,
        "price": 200,
        "rent": [25, 50, 100, 200],
        "mortgage_value": 100,
    },
    36: {
        "name": "Chance",
        "type": PropertyType.SPECIAL,
        "color": PropertyColor.SPECIAL,
    },
    37: {
        "name": "Park Place",
        "type": PropertyType.STREET,
        "color": PropertyColor.DARK_BLUE,
        "price": 350,
        "rent": [35, 175, 500, 1100, 1300, 1500],
        "house_cost": 200,
        "mortgage_value": 175,
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

# Color group mappings
COLOR_GROUPS = {
    PropertyColor.BROWN: ["Mediterranean Avenue", "Baltic Avenue"],
    PropertyColor.LIGHT_BLUE: [
        "Oriental Avenue",
        "Vermont Avenue",
        "Connecticut Avenue",
    ],
    PropertyColor.PINK: ["St. Charles Place", "States Avenue", "Virginia Avenue"],
    PropertyColor.ORANGE: ["St. James Place", "Tennessee Avenue", "New York Avenue"],
    PropertyColor.RED: ["Kentucky Avenue", "Indiana Avenue", "Illinois Avenue"],
    PropertyColor.YELLOW: ["Atlantic Avenue", "Ventnor Avenue", "Marvin Gardens"],
    PropertyColor.GREEN: [
        "Pacific Avenue",
        "North Carolina Avenue",
        "Pennsylvania Avenue",
    ],
    PropertyColor.DARK_BLUE: ["Park Place", "Boardwalk"],
    PropertyColor.RAILROAD: [
        "Reading Railroad",
        "Pennsylvania Railroad",
        "B&O Railroad",
        "Short Line",
    ],
    PropertyColor.UTILITY: ["Electric Company", "Water Works"],
}

# Chance cards
CHANCE_CARDS = [
    "Advance to GO (Collect $200)",
    "Advance to Illinois Avenue",
    "Advance to St. Charles Place",
    "Advance token to nearest Utility",
    "Advance token to nearest Railroad",
    "Bank pays you dividend of $50",
    "Get Out of Jail Free",
    "Go Back 3 Spaces",
    "Go to Jail",
    "Make general repairs on all your property",
    "Pay poor tax of $15",
    "Take a trip to Reading Railroad",
    "Take a walk on the Boardwalk",
    "You have been elected Chairman of the Board",
    "Your building and loan matures",
    "You have won a crossword competition",
]

# Community Chest cards
COMMUNITY_CHEST_CARDS = [
    "Advance to GO (Collect $200)",
    "Bank error in your favor",
    "Doctor's fee",
    "From sale of stock you get $50",
    "Get Out of Jail Free",
    "Go to Jail",
    "Holiday fund matures",
    "Income tax refund",
    "It is your birthday",
    "Life insurance matures",
    "Pay hospital fees of $100",
    "Pay school fees of $50",
    "Receive $25 consultancy fee",
    "You are assessed for street repairs",
    "You have won second prize in a beauty contest",
    "You inherit $100",
]


def create_board() -> dict[str, Property]:
    """Create the initial board with all properties."""
    properties = {}

    for position, prop_data in BOARD_PROPERTIES.items():
        # Create ALL properties, including special ones
        # This ensures positions like Vermont Avenue are properly mapped
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

    # Debug print to verify all properties were created

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
    passed_go = new_position < old_position

    player.position = new_position
    return new_position, passed_go


def get_properties_by_color(color: PropertyColor) -> list[str]:
    """Get all property names for a color group."""
    return COLOR_GROUPS.get(color, [])


def calculate_rent(
    property: Property, state: "MonopolyState", dice_roll: int | None = None
) -> int:
    """Calculate rent for a property."""
    if not property.owner or property.mortgaged:
        return 0

    if property.property_type == PropertyType.RAILROAD:
        # Count railroads owned by the same player
        railroads_owned = sum(
            1
            for prop in state.properties.values()
            if (
                prop.property_type == PropertyType.RAILROAD
                and prop.owner == property.owner
                and not prop.mortgaged
            )
        )
        return property.rent[min(railroads_owned - 1, 3)]

    if property.property_type == PropertyType.UTILITY:
        if dice_roll is None:
            return 0

        # Count utilities owned by the same player
        utilities_owned = sum(
            1
            for prop in state.properties.values()
            if (
                prop.property_type == PropertyType.UTILITY
                and prop.owner == property.owner
                and not prop.mortgaged
            )
        )

        multiplier = property.rent[0] if utilities_owned == 1 else property.rent[1]
        return dice_roll * multiplier

    if property.property_type == PropertyType.STREET:
        # Check if owner has monopoly
        has_monopoly = state.player_owns_monopoly(property.owner, property.color.value)

        if property.hotel:
            return property.rent[5]
        if property.houses > 0:
            return property.rent[property.houses]
        if has_monopoly:
            # Double rent if monopoly but no houses
            return property.rent[0] * 2
        return property.rent[0]

    return 0


def get_property_at_position(position: int) -> dict[str, Any] | None:
    """Get property information at a board position."""
    return BOARD_PROPERTIES.get(position)


def shuffle_cards() -> tuple[list[str], list[str]]:
    """Shuffle and return chance and community chest cards."""
    chance = CHANCE_CARDS.copy()
    community_chest = COMMUNITY_CHEST_CARDS.copy()
    random.shuffle(chance)
    random.shuffle(community_chest)
    return chance, community_chest


def handle_special_position(
    position: int, player: Player, state: "MonopolyState"
) -> str:
    """Handle special board positions like GO, Jail, etc."""
    position_data = get_property_at_position(position)
    if not position_data:
        return "unknown_position"

    position_name = position_data["name"]

    if position_name == "GO":
        return "collect_go_money"
    if position_name == "Jail":
        return "visiting_jail"
    if position_name == "Go To Jail":
        return "go_to_jail"
    if position_name == "Free Parking":
        return "free_parking"
    if position_name == "Income Tax":
        return "pay_income_tax"
    if position_name == "Luxury Tax":
        return "pay_luxury_tax"
    if position_name == "Chance":
        return "draw_chance"
    if position_name == "Community Chest":
        return "draw_community_chest"

    return "no_action"


def check_game_end(state: "MonopolyState") -> tuple[bool, str | None]:
    """Check if the game should end."""
    active_players = state.active_players

    # Game ends if only one player remains
    if len(active_players) <= 1:
        winner = active_players[0].name if active_players else None
        return True, winner

    # Could add other end conditions (time limit, etc.)
    return False, None


def get_building_cost(
    property: Property, buildings: int, is_hotel: bool = False
) -> int:
    """Calculate cost to build houses or hotel."""
    if is_hotel:
        return property.house_cost  # Hotel costs same as one house
    return property.house_cost * buildings


def can_trade_properties(
    prop1: Property, prop2: Property, state: "MonopolyState"
) -> bool:
    """Check if two properties can be traded."""
    # Can't trade mortgaged properties
    if prop1.mortgaged or prop2.mortgaged:
        return False

    # Can't trade properties with buildings
    return not (prop1.houses > 0 or prop1.hotel or prop2.houses > 0 or prop2.hotel)
