"""Monopoly game models module.

This module provides data models for the monopoly game, including:
    - Player actions and decisions
    - Property management
    - Game events and transactions
    - Structured output models for LLMs
"""

from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field, field_validator


class PropertyType(str, Enum):
    """Types of properties in Monopoly."""

    STREET = "street"
    RAILROAD = "railroad"
    UTILITY = "utility"
    SPECIAL = "special"  # GO, Jail, etc.


class PropertyColor(str, Enum):
    """Property color groups."""

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


class CardType(str, Enum):
    """Types of cards in Monopoly."""

    CHANCE = "chance"
    COMMUNITY_CHEST = "community_chest"


class PlayerActionType(str, Enum):
    """Types of actions a player can take."""

    BUY_PROPERTY = "buy_property"
    PASS_PROPERTY = "pass_property"
    PAY_RENT = "pay_rent"
    PAY_TAX = "pay_tax"
    DRAW_CARD = "draw_card"
    GO_TO_JAIL = "go_to_jail"
    PAY_JAIL_FINE = "pay_jail_fine"
    ROLL_FOR_JAIL = "roll_for_jail"
    USE_JAIL_CARD = "use_jail_card"
    BUILD_HOUSE = "build_house"
    BUILD_HOTEL = "build_hotel"
    MORTGAGE_PROPERTY = "mortgage_property"
    UNMORTGAGE_PROPERTY = "unmortgage_property"
    TRADE_OFFER = "trade_offer"
    TRADE_ACCEPT = "trade_accept"
    TRADE_DECLINE = "trade_decline"
    DECLARE_BANKRUPTCY = "declare_bankruptcy"


class PropertyDecision(BaseModel):
    """Model for property purchase decisions."""

    action: PlayerActionType = Field(
        description="Whether to buy or pass on the property"
    )

    reasoning: str = Field(description="Explanation for the decision")

    max_bid: Optional[int] = Field(
        default=None, description="Maximum bid if property goes to auction"
    )

    @field_validator("action")
    def validate_property_action(cls, v):
        """Validate that action is appropriate for property decisions."""
        valid_actions = {PlayerActionType.BUY_PROPERTY, PlayerActionType.PASS_PROPERTY}
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v


class JailDecision(BaseModel):
    """Model for jail-related decisions."""

    action: PlayerActionType = Field(description="How to handle being in jail")

    reasoning: str = Field(description="Explanation for the decision")

    @field_validator("action")
    def validate_jail_action(cls, v):
        """Validate that action is appropriate for jail decisions."""
        valid_actions = {
            PlayerActionType.PAY_JAIL_FINE,
            PlayerActionType.ROLL_FOR_JAIL,
            PlayerActionType.USE_JAIL_CARD,
        }
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v


class BuildingDecision(BaseModel):
    """Model for building houses/hotels decisions."""

    property_name: str = Field(description="Name of the property to build on")

    action: PlayerActionType = Field(description="Type of building action")

    quantity: int = Field(
        default=1, description="Number of houses to build (1-4) or 1 hotel"
    )

    reasoning: str = Field(description="Explanation for the building decision")

    @field_validator("action")
    def validate_building_action(cls, v):
        """Validate that action is appropriate for building."""
        valid_actions = {PlayerActionType.BUILD_HOUSE, PlayerActionType.BUILD_HOTEL}
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v

    @field_validator("quantity")
    def validate_quantity(cls, v):
        """Validate building quantity."""
        if v < 1 or v > 4:
            raise ValueError("Quantity must be between 1 and 4")
        return v


class TradeOffer(BaseModel):
    """Model for trade offers between players."""

    offering_player: str = Field(description="Name of player making the offer")

    receiving_player: str = Field(description="Name of player receiving the offer")

    offered_properties: list[str] = Field(
        default_factory=list, description="Properties being offered"
    )

    offered_money: int = Field(default=0, description="Money being offered")

    requested_properties: list[str] = Field(
        default_factory=list, description="Properties being requested"
    )

    requested_money: int = Field(default=0, description="Money being requested")

    reasoning: str = Field(description="Explanation for the trade offer")


class TradeResponse(BaseModel):
    """Model for responding to trade offers."""

    action: PlayerActionType = Field(description="Accept or decline the trade")

    reasoning: str = Field(description="Explanation for the response")

    counter_offer: Optional[TradeOffer] = Field(
        default=None, description="Optional counter-offer if declining"
    )

    @field_validator("action")
    def validate_trade_action(cls, v):
        """Validate that action is appropriate for trade responses."""
        valid_actions = {PlayerActionType.TRADE_ACCEPT, PlayerActionType.TRADE_DECLINE}
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v


class PlayerAnalysis(BaseModel):
    """Model for player analysis and strategy."""

    financial_position: str = Field(
        description="Assessment of current financial position"
    )

    property_strategy: str = Field(description="Current property acquisition strategy")

    immediate_goals: list[str] = Field(description="Short-term goals and priorities")

    threats: list[str] = Field(
        default_factory=list, description="Threats from other players"
    )

    opportunities: list[str] = Field(
        default_factory=list, description="Current opportunities to pursue"
    )


class GameEvent(BaseModel):
    """Model for game events and transactions."""

    event_type: str = Field(description="Type of event that occurred")

    player: str = Field(description="Player involved in the event")

    description: str = Field(description="Description of what happened")

    money_change: int = Field(
        default=0, description="Money gained or lost (negative for losses)"
    )

    property_involved: Optional[str] = Field(
        default=None, description="Property involved in the event"
    )

    details: dict[str, Any] = Field(
        default_factory=dict, description="Additional event details"
    )


class DiceRoll(BaseModel):
    """Model for dice roll results."""

    die1: int = Field(description="First die result", ge=1, le=6)

    die2: int = Field(description="Second die result", ge=1, le=6)

    @property
    def total(self) -> int:
        """Total of both dice."""
        return self.die1 + self.die2

    @property
    def is_doubles(self) -> bool:
        """Whether the roll is doubles."""
        return self.die1 == self.die2


class Property(BaseModel):
    """Model for a property on the board."""

    name: str = Field(description="Property name")
    position: int = Field(description="Position on board (0-39)")
    property_type: PropertyType = Field(description="Type of property")
    color: PropertyColor = Field(description="Property color group")
    price: int = Field(description="Purchase price")
    rent: list[int] = Field(
        description="Rent amounts [base, 1 house, 2 house, 3 house, 4 house, hotel]"
    )
    house_cost: int = Field(default=0, description="Cost to build a house")
    mortgage_value: int = Field(description="Mortgage value")
    owner: Optional[str] = Field(default=None, description="Current owner")
    houses: int = Field(default=0, description="Number of houses (0-4)")
    hotel: bool = Field(default=False, description="Whether there's a hotel")
    mortgaged: bool = Field(default=False, description="Whether property is mortgaged")

    def current_rent(self) -> int:
        """Calculate current rent based on development."""
        if self.mortgaged or not self.owner:
            return 0

        if self.property_type == PropertyType.RAILROAD:
            # Railroad rent depends on how many railroads owner has
            return self.rent[0]  # Will be calculated by game logic

        if self.property_type == PropertyType.UTILITY:
            # Utility rent depends on dice roll and how many utilities owned
            return self.rent[0]  # Will be calculated by game logic

        if self.hotel:
            return self.rent[5]
        else:
            return self.rent[self.houses]


class Player(BaseModel):
    """Model for a player in the game."""

    name: str = Field(description="Player name")
    money: int = Field(default=1500, description="Current money")
    position: int = Field(default=0, description="Current board position")
    properties: list[str] = Field(default_factory=list, description="Owned properties")
    jail_cards: int = Field(default=0, description="Get out of jail free cards")
    in_jail: bool = Field(default=False, description="Whether player is in jail")
    jail_turns: int = Field(default=0, description="Turns spent in jail")
    doubles_count: int = Field(
        default=0, description="Consecutive doubles rolled this turn"
    )
    bankrupt: bool = Field(default=False, description="Whether player is bankrupt")

    def can_afford(self, amount: int) -> bool:
        """Check if player can afford a given amount."""
        return self.money >= amount

    def net_worth(self, properties_dict: dict[str, Property]) -> int:
        """Calculate player's net worth including properties."""
        total = self.money
        for prop_name in self.properties:
            if prop_name in properties_dict:
                prop = properties_dict[prop_name]
                # Add property value plus development
                total += prop.mortgage_value
                total += prop.houses * prop.house_cost
                if prop.hotel:
                    total += prop.house_cost  # Hotel value
        return total
