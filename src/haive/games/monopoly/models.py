from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, computed_field, field_validator

r"""Comprehensive data models for strategic Monopoly gameplay and real estate
management.

This module provides sophisticated data models for the classic Monopoly board game,
supporting complex property transactions, strategic decision-making, and comprehensive
game state management. The models enable structured data handling throughout the
Monopoly game implementation and provide strong typing for LLM-based components.

The models support:
- Complete property management with development and mortgage systems
- Strategic player decisions with reasoning and financial analysis
- Complex trading mechanisms between players
- Comprehensive game event tracking and transaction logging
- Advanced AI decision-making for strategic gameplay
- Full support for all Monopoly game mechanics

Examples:
    Basic property purchase decision::\n

        decision = PropertyDecision(
            action=PlayerActionType.BUY_PROPERTY,
            reasoning="Strategic acquisition of orange property group for high traffic location",
            max_bid=600
        )

    Complex trade negotiation::\n

        trade = TradeOffer(
            offering_player="Player1",
            receiving_player="Player2",
            offered_properties=["St. James Place", "Tennessee Avenue"],
            offered_money=200,
            requested_properties=["New York Avenue"],
            requested_money=0,
            reasoning="Completing orange monopoly for strong rental income"
        )

    Strategic property development::\n

        building = BuildingDecision(
            property_name="Park Place",
            action=PlayerActionType.BUILD_HOUSE,
            quantity=3,
            reasoning="Developing high-value property for maximum rental income"
        )

    Financial position analysis::\n

        analysis = PlayerAnalysis(
            financial_position="Strong cash position with $1,200 and diversified portfolio",
            property_strategy="Focus on completing color groups for monopoly advantages",
            immediate_goals=["Acquire remaining orange properties", "Develop existing monopolies"],
            threats=["Player2 approaching monopoly completion"],
            opportunities=["Available railroad for transportation monopoly"]
        )

Note:
    All models use Pydantic for validation and support both JSON serialization
    and integration with LLM-based strategic analysis systems for advanced gameplay.
"""


class PropertyType(str, Enum):
    """Enumeration of property types in the Monopoly game.

    Defines the four main categories of board spaces that players can
    interact with, each with distinct gameplay mechanics and rules.

    Values:
        STREET: Standard property that can be developed with houses/hotels
        RAILROAD: Transportation properties with special rent calculation
        UTILITY: Electric Company and Water Works with dice-based rent
        SPECIAL: Non-purchasable spaces like GO, Jail, Free Parking

    """

    STREET = "street"
    RAILROAD = "railroad"
    UTILITY = "utility"
    SPECIAL = "special"


class PropertyColor(str, Enum):
    """Property color groups for monopoly formation and development.

    Represents the color-coded property groups in Monopoly, where owning
    all properties of the same color grants monopoly privileges including
    doubled rent and the ability to build houses and hotels.

    Values:
        BROWN: Mediterranean/Baltic Ave group (lowest rent)
        LIGHT_BLUE: Oriental/Vermont/Connecticut Ave group
        PINK: St. Charles/States/Virginia Ave group
        ORANGE: St. James/Tennessee/New York Ave group (high traffic)
        RED: Kentucky/Indiana/Illinois Ave group
        YELLOW: Atlantic/Ventnor/Marvin Gardens group
        GREEN: Pacific/North Carolina/Pennsylvania Ave group
        DARK_BLUE: Park Place/Boardwalk group (highest rent)
        RAILROAD: All four railroad properties
        UTILITY: Electric Company and Water Works
        SPECIAL: Non-property spaces

    """

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
    """Types of cards drawn during Monopoly gameplay.

    Represents the two types of cards that players can draw when landing
    on specific board spaces, each with different effects and outcomes.

    Values:
        CHANCE: Orange cards with various effects (movement, payments, etc.)
        COMMUNITY_CHEST: Blue cards typically involving payments or rewards

    """

    CHANCE = "chance"
    COMMUNITY_CHEST = "community_chest"


class PlayerActionType(str, Enum):
    """Comprehensive enumeration of all possible player actions in Monopoly.

    Defines every action a player can take during their turn or in response
    to game events, enabling structured decision-making and game flow control.

    Values:
        BUY_PROPERTY: Purchase an unowned property at list price
        PASS_PROPERTY: Decline to purchase a property (triggers auction)
        PAY_RENT: Pay rent to another player for landing on their property
        PAY_TAX: Pay tax when landing on tax spaces
        DRAW_CARD: Draw a Chance or Community Chest card
        GO_TO_JAIL: Move directly to jail (do not pass GO)
        PAY_JAIL_FINE: Pay $50 fine to get out of jail
        ROLL_FOR_JAIL: Attempt to roll doubles to get out of jail
        USE_JAIL_CARD: Use "Get Out of Jail Free" card
        BUILD_HOUSE: Construct houses on monopolized properties
        BUILD_HOTEL: Upgrade 4 houses to a hotel
        MORTGAGE_PROPERTY: Mortgage property for immediate cash
        UNMORTGAGE_PROPERTY: Pay to unmortgage a property
        TRADE_OFFER: Propose a trade with another player
        TRADE_ACCEPT: Accept a trade offer
        TRADE_DECLINE: Decline a trade offer
        DECLARE_BANKRUPTCY: Declare bankruptcy and exit the game

    """

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
    r"""Strategic decision model for property purchase and auction scenarios.

    This model captures the decision-making process when a player lands on an
    unowned property, including the choice to purchase at list price or pass
    (triggering an auction), along with strategic reasoning and auction bidding
    parameters.

    The decision process involves:
    - Immediate purchase evaluation at list price
    - Strategic assessment of property value and portfolio fit
    - Auction participation strategy if property is passed
    - Financial risk assessment and cash flow management
    - Long-term strategic planning for monopoly completion

    Attributes:
        action (PlayerActionType): The chosen action - either BUY_PROPERTY to
            purchase at list price or PASS_PROPERTY to trigger auction.
        reasoning (str): Detailed strategic reasoning for the decision including
            financial analysis, portfolio considerations, and strategic value.
        max_bid (Optional[int]): Maximum bid amount if property goes to auction.
            Should be None if purchasing at list price.

    Examples:
        Strategic property purchase::\n

            decision = PropertyDecision(
                action=PlayerActionType.BUY_PROPERTY,
                reasoning="Strategic acquisition of orange property group for high traffic location and monopoly completion",
                max_bid=None
            )

        Auction participation strategy::\n

            decision = PropertyDecision(
                action=PlayerActionType.PASS_PROPERTY,
                reasoning="List price too high for current cash position, but willing to bid competitively at auction",
                max_bid=600
            )

        Conservative financial approach::\n

            decision = PropertyDecision(
                action=PlayerActionType.PASS_PROPERTY,
                reasoning="Preserving cash for existing property development, not participating in auction",
                max_bid=0
            )

    Note:
        When action is BUY_PROPERTY, max_bid should be None. When action is
        PASS_PROPERTY, max_bid determines auction participation level.

    """

    action: PlayerActionType = Field(
        ...,
        description="Whether to buy property at list price or pass to trigger auction",
    )

    reasoning: str = Field(
        ...,
        min_length=10,
        max_length=300,
        description="Detailed strategic reasoning for the decision including financial analysis",
        examples=[
            "Strategic acquisition of orange property group for high traffic location",
            "List price too high for current cash position, but willing to bid at auction",
            "Preserving cash for existing property development opportunities",
        ],
    )

    max_bid: int | None = Field(
        default=None,
        ge=0,
        le=10000,
        description="Maximum bid amount if property goes to auction (None if buying at list price)",
        examples=[None, 0, 400, 600, 800],
    )

    @field_validator("action")
    @classmethod
    def validate_property_action(cls, v: PlayerActionType) -> PlayerActionType:
        """Validate that action is appropriate for property decisions.

        Args:
            v (PlayerActionType): Action to validate.

        Returns:
            PlayerActionType: Validated action.

        Raises:
            ValueError: If action is not valid for property decisions.

        """
        valid_actions = {PlayerActionType.BUY_PROPERTY, PlayerActionType.PASS_PROPERTY}
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v

    @computed_field
    @property
    def is_auction_participant(self) -> bool:
        """Determine if player will participate in auction.

        Returns:
            bool: True if player will bid in auction, False otherwise.

        """
        return self.action == PlayerActionType.PASS_PROPERTY and (self.max_bid or 0) > 0


class JailDecision(BaseModel):
    r"""Strategic decision model for jail escape and turn management.

    This model captures the decision-making process when a player is in jail,
    including the choice of escape method, timing considerations, and strategic
    implications of remaining in jail versus getting out immediately.

    The jail decision involves:
    - Immediate escape via fine payment ($50)
    - Risk-based escape attempt by rolling doubles
    - Using "Get Out of Jail Free" cards if available
    - Strategic evaluation of jail benefits in late game
    - Turn opportunity cost analysis

    Attributes:
        action (PlayerActionType): The chosen escape method - PAY_JAIL_FINE for
            immediate release, ROLL_FOR_JAIL to attempt doubles, or USE_JAIL_CARD
            to use a "Get Out of Jail Free" card.
        reasoning (str): Detailed strategic reasoning for the decision including
            financial considerations, board position analysis, and timing factors.

    Examples:
        Immediate jail escape::\n

            decision = JailDecision(
                action=PlayerActionType.PAY_JAIL_FINE,
                reasoning="Need immediate mobility to complete property trades and avoid losing turn advantage"
            )

        Risk-based escape attempt::\n

            decision = JailDecision(
                action=PlayerActionType.ROLL_FOR_JAIL,
                reasoning="Conserving cash for property development, willing to risk additional jail time"
            )

        Strategic card usage::\n

            decision = JailDecision(
                action=PlayerActionType.USE_JAIL_CARD,
                reasoning="Preserving cash while maintaining mobility for critical property acquisitions"
            )

    Note:
        In late game, staying in jail can be strategically beneficial to avoid
        landing on expensive developed properties while still collecting rent.

    """

    action: PlayerActionType = Field(
        ...,
        description="How to handle being in jail (pay fine, roll for doubles, or use card)",
    )

    reasoning: str = Field(
        ...,
        min_length=10,
        max_length=250,
        description="Detailed strategic reasoning for the jail escape decision",
        examples=[
            "Need immediate mobility to complete property trades and avoid losing turn advantage",
            "Conserving cash for property development, willing to risk additional jail time",
            "Preserving cash while maintaining mobility for critical property acquisitions",
        ],
    )

    @field_validator("action")
    @classmethod
    def validate_jail_action(cls, v: PlayerActionType) -> PlayerActionType:
        """Validate that action is appropriate for jail decisions.

        Args:
            v (PlayerActionType): Action to validate.

        Returns:
            PlayerActionType: Validated action.

        Raises:
            ValueError: If action is not valid for jail decisions.

        """
        valid_actions = {
            PlayerActionType.PAY_JAIL_FINE,
            PlayerActionType.ROLL_FOR_JAIL,
            PlayerActionType.USE_JAIL_CARD,
        }
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v

    @computed_field
    @property
    def has_immediate_cost(self) -> bool:
        """Determine if decision has immediate financial cost.

        Returns:
            bool: True if action requires immediate payment, False otherwise.

        """
        return self.action == PlayerActionType.PAY_JAIL_FINE


class BuildingDecision(BaseModel):
    r"""Strategic decision model for property development and rental income optimization.

    This model captures the decision-making process for building houses and hotels
    on monopolized properties, including development strategy, cash flow management,
    and rental income optimization considerations.

    The building decision involves:
    - Strategic property development prioritization
    - Cash flow analysis and investment timing
    - Rental income optimization calculations
    - Housing shortage manipulation tactics
    - Long-term portfolio development strategy

    Attributes:
        property_name (str): Name of the specific property to develop.
            Must be a property owned by the player in a monopolized color group.
        action (PlayerActionType): Type of development - BUILD_HOUSE for adding
            houses (1-4 per property) or BUILD_HOTEL for hotel upgrade.
        quantity (int): Number of houses to build (1-4) or 1 for hotel.
            Houses must be built evenly across monopoly group.
        reasoning (str): Detailed strategic reasoning for the development decision
            including financial analysis and rental income projections.

    Examples:
        Strategic house development::\n

            decision = BuildingDecision(
                property_name="St. James Place",
                action=PlayerActionType.BUILD_HOUSE,
                quantity=2,
                reasoning="Developing orange monopoly to 2 houses for optimal rent-to-investment ratio"
            )

        Hotel upgrade for maximum income::\n

            decision = BuildingDecision(
                property_name="Boardwalk",
                action=PlayerActionType.BUILD_HOTEL,
                quantity=1,
                reasoning="Upgrading to hotel for maximum rental income on premium property"
            )

        Even development strategy::\n

            decision = BuildingDecision(
                property_name="Indiana Avenue",
                action=PlayerActionType.BUILD_HOUSE,
                quantity=1,
                reasoning="Maintaining even development across red monopoly for efficient housing use"
            )

    Note:
        Houses must be built evenly across all properties in a monopoly group.
        Hotels require 4 houses to be traded in plus hotel cost.

    """

    property_name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Name of the property to develop (must be in monopolized color group)",
        examples=["St. James Place", "Boardwalk", "Indiana Avenue", "Park Place"],
    )

    action: PlayerActionType = Field(
        ..., description="Type of development action (build houses or upgrade to hotel)"
    )

    quantity: int = Field(
        default=1,
        ge=1,
        le=4,
        description="Number of houses to build (1-4) or 1 for hotel upgrade",
        examples=[1, 2, 3, 4],
    )

    reasoning: str = Field(
        ...,
        min_length=15,
        max_length=300,
        description="Detailed strategic reasoning for the development decision",
        examples=[
            "Developing orange monopoly to 2 houses for optimal rent-to-investment ratio",
            "Upgrading to hotel for maximum rental income on premium property",
            "Maintaining even development across red monopoly for efficient housing use",
        ],
    )

    @field_validator("action")
    @classmethod
    def validate_building_action(cls, v: PlayerActionType) -> PlayerActionType:
        """Validate that action is appropriate for building.

        Args:
            v (PlayerActionType): Action to validate.

        Returns:
            PlayerActionType: Validated action.

        Raises:
            ValueError: If action is not valid for building.

        """
        valid_actions = {PlayerActionType.BUILD_HOUSE, PlayerActionType.BUILD_HOTEL}
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v

    @field_validator("quantity")
    @classmethod
    def validate_quantity(cls, v: int) -> int:
        """Validate building quantity is within game limits.

        Args:
            v (int): Quantity to validate.

        Returns:
            int: Validated quantity.

        Raises:
            ValueError: If quantity is outside valid range.

        """
        if v < 1 or v > 4:
            raise ValueError("Quantity must be between 1 and 4")
        return v

    @computed_field
    @property
    def is_hotel_upgrade(self) -> bool:
        """Determine if decision is for hotel upgrade.

        Returns:
            bool: True if upgrading to hotel, False if building houses.

        """
        return self.action == PlayerActionType.BUILD_HOTEL


class TradeOffer(BaseModel):
    r"""Comprehensive model for inter-player trade negotiations and strategic exchanges.

    This model captures complex trade offers between players, including property
    exchanges, cash considerations, and strategic reasoning. It supports multi-asset
    trades that are essential for monopoly completion and strategic positioning.

    The trade offer includes:
    - Multi-property exchange capabilities
    - Cash consideration balancing
    - Strategic reasoning and negotiation context
    - Fair value assessment and win-win scenarios
    - Monopoly completion and blocking strategies

    Attributes:
        offering_player (str): Name of the player initiating the trade offer.
            Must be a valid player currently in the game.
        receiving_player (str): Name of the player receiving the trade offer.
            Must be a different player than the offering player.
        offered_properties (List[str]): List of property names being offered.
            Properties must be owned by the offering player.
        offered_money (int): Cash amount being offered as part of the trade.
            Must be less than or equal to offering player's available cash.
        requested_properties (List[str]): List of property names being requested.
            Properties must be owned by the receiving player.
        requested_money (int): Cash amount being requested as part of the trade.
            Must be less than or equal to receiving player's available cash.
        reasoning (str): Detailed explanation for the trade offer including
            strategic benefits, fair value justification, and mutual advantages.

    Examples:
        Monopoly completion trade::\n

            trade = TradeOffer(
                offering_player="Player1",
                receiving_player="Player2",
                offered_properties=["St. James Place", "Tennessee Avenue"],
                offered_money=200,
                requested_properties=["New York Avenue"],
                requested_money=0,
                reasoning="Completing orange monopoly for high-traffic rental income, offering premium for strategic value"
            )

        Balanced property exchange::\n

            trade = TradeOffer(
                offering_player="Player2",
                receiving_player="Player3",
                offered_properties=["Reading Railroad"],
                offered_money=0,
                requested_properties=["Water Works"],
                requested_money=100,
                reasoning="Exchanging railroad for utility plus cash to diversify portfolio and improve liquidity"
            )

        Cash-heavy acquisition::\n

            trade = TradeOffer(
                offering_player="Player3",
                receiving_player="Player1",
                offered_properties=[],
                offered_money=800,
                requested_properties=["Boardwalk"],
                requested_money=0,
                reasoning="Premium cash offer for Boardwalk to prevent opponent monopoly completion"
            )

    Note:
        Trade offers should be mutually beneficial or strategically justified.
        Players cannot trade mortgaged properties or properties with buildings.

    """

    offering_player: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Name of the player initiating the trade offer",
        examples=["Player1", "Alice", "Strategic_AI", "Human_Player"],
    )

    receiving_player: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Name of the player receiving the trade offer",
        examples=["Player2", "Bob", "Tactical_AI", "Computer_Opponent"],
    )

    offered_properties: list[str] = Field(
        default_factory=list,
        description="List of property names being offered by the offering player",
        examples=[
            ["St. James Place", "Tennessee Avenue"],
            ["Reading Railroad"],
            ["Mediterranean Avenue", "Baltic Avenue"],
        ],
    )

    offered_money: int = Field(
        default=0,
        ge=0,
        le=20000,
        description="Cash amount being offered as part of the trade",
        examples=[0, 100, 200, 500, 800],
    )

    requested_properties: list[str] = Field(
        default_factory=list,
        description="List of property names being requested from the receiving player",
        examples=[["New York Avenue"], ["Water Works"], ["Boardwalk"]],
    )

    requested_money: int = Field(
        default=0,
        ge=0,
        le=20000,
        description="Cash amount being requested as part of the trade",
        examples=[0, 50, 100, 300, 600],
    )

    reasoning: str = Field(
        ...,
        min_length=20,
        max_length=400,
        description="Detailed explanation for the trade offer including strategic benefits and fair value justification",
        examples=[
            "Completing orange monopoly for high-traffic rental income, offering premium for strategic value",
            "Exchanging railroad for utility plus cash to diversify portfolio and improve liquidity",
            "Premium cash offer for Boardwalk to prevent opponent monopoly completion",
        ],
    )

    @field_validator("receiving_player")
    @classmethod
    def validate_different_players(cls, v: str, info) -> str:
        """Validate that receiving player is different from offering player.

        Args:
            v (str): Receiving player name to validate.
            info: Validation info containing other field values.

        Returns:
            str: Validated receiving player name.

        Raises:
            ValueError: If receiving player is the same as offering player.

        """
        if hasattr(info, "data") and info.data.get("offering_player") == v:
            raise ValueError("Receiving player must be different from offering player")
        return v

    @computed_field
    @property
    def net_cash_flow(self) -> int:
        """Calculate net cash flow for the offering player.

        Returns:
            int: Net cash change for offering player (negative = paying out, positive = receiving).

        """
        return self.requested_money - self.offered_money

    @computed_field
    @property
    def total_assets_offered(self) -> int:
        """Calculate total number of assets being offered.

        Returns:
            int: Total count of properties and cash being offered.

        """
        return len(self.offered_properties) + (1 if self.offered_money > 0 else 0)

    @computed_field
    @property
    def total_assets_requested(self) -> int:
        """Calculate total number of assets being requested.

        Returns:
            int: Total count of properties and cash being requested.

        """
        return len(self.requested_properties) + (1 if self.requested_money > 0 else 0)


class TradeResponse(BaseModel):
    """Strategic response model for trade offer evaluation and negotiation.

    This model captures the decision-making process when responding to trade
    offers, including acceptance, rejection, and counter-offer negotiations.
    It supports complex multi-round trading scenarios essential for strategic
    Monopoly gameplay.

    The trade response includes:
    - Accept/decline decision with strategic reasoning
    - Counter-offer capabilities for continued negotiation
    - Risk assessment and strategic value evaluation
    - Alternative proposal generation for win-win scenarios
    - Negotiation tactics and positioning strategies

    Attributes:
        action (PlayerActionType): Response decision - TRADE_ACCEPT to accept
            the offer as presented, or TRADE_DECLINE to reject.
        reasoning (str): Detailed explanation for the response decision
            including strategic analysis and value assessment.
        counter_offer (Optional[TradeOffer]): Alternative trade proposal if
            declining the original offer. Enables continued negotiation.

    Examples:
        Accepting a favorable trade::

            response = TradeResponse(
                action=PlayerActionType.TRADE_ACCEPT,
                reasoning="Excellent value for monopoly completion, strategic advantage outweighs asset loss",
                counter_offer=None
            )

        Declining with counter-offer::

            response = TradeResponse(
                action=PlayerActionType.TRADE_DECLINE,
                reasoning="Original offer undervalues my assets, proposing adjusted terms",
                counter_offer=TradeOffer(
                    offering_player="Player2",
                    receiving_player="Player1",
                    offered_properties=["Reading Railroad"],
                    offered_money=100,
                    requested_properties=["New York Avenue"],
                    requested_money=0,
                    reasoning="Counter-proposal with additional cash for fair value"
                )
            )

        Outright rejection::

            response = TradeResponse(
                action=PlayerActionType.TRADE_DECLINE,
                reasoning="Trade would strengthen opponent's position too significantly without adequate compensation",
                counter_offer=None
            )

    Note:
        Counter-offers should only be provided when declining. When accepting,
        counter_offer should be None.

    """

    action: PlayerActionType = Field(
        ..., description="Response decision (accept or decline the trade offer)"
    )

    reasoning: str = Field(
        ...,
        min_length=15,
        max_length=300,
        description="Detailed explanation for the response decision including strategic analysis",
        examples=[
            "Excellent value for monopoly completion, strategic advantage outweighs asset loss",
            "Original offer undervalues my assets, proposing adjusted terms",
            "Trade would strengthen opponent's position too significantly without adequate compensation",
        ],
    )

    counter_offer: TradeOffer | None = Field(
        default=None,
        description="Optional alternative trade proposal if declining the original offer",
    )

    @field_validator("action")
    @classmethod
    def validate_trade_action(cls, v: PlayerActionType) -> PlayerActionType:
        """Validate that action is appropriate for trade responses.

        Args:
            v (PlayerActionType): Action to validate.

        Returns:
            PlayerActionType: Validated action.

        Raises:
            ValueError: If action is not valid for trade responses.

        """
        valid_actions = {PlayerActionType.TRADE_ACCEPT, PlayerActionType.TRADE_DECLINE}
        if v not in valid_actions:
            raise ValueError(f"Action must be one of {valid_actions}")
        return v

    @computed_field
    @property
    def is_negotiation_continuing(self) -> bool:
        """Determine if negotiation continues with counter-offer.

        Returns:
            bool: True if declining with counter-offer, False otherwise.

        """
        return (
            self.action == PlayerActionType.TRADE_DECLINE
            and self.counter_offer is not None
        )


class PlayerAnalysis(BaseModel):
    """Comprehensive strategic analysis model for player position and game state
    evaluation.

    This model provides detailed analysis of a player's current position in the game,
    including financial assessment, strategic planning, opportunity identification,
    and threat evaluation. It supports advanced AI decision-making and strategic
    planning for optimal Monopoly gameplay.

    The analysis includes:
    - Complete financial position assessment
    - Strategic property acquisition planning
    - Short-term and long-term goal identification
    - Competitive threat analysis and countermeasures
    - Opportunity recognition and exploitation strategies

    Attributes:
        financial_position (str): Comprehensive assessment of current financial
            position including cash, assets, income potential, and liquidity.
        property_strategy (str): Current property acquisition and development
            strategy including monopoly targets and portfolio optimization.
        immediate_goals (List[str]): Short-term tactical goals and priorities
            for the next few turns.
        threats (List[str]): Identified threats from other players including
            potential monopolies, competitive advantages, and strategic risks.
        opportunities (List[str]): Current opportunities available for strategic
            advancement and competitive positioning.

    Examples:
        Mid-game strategic analysis::

            analysis = PlayerAnalysis(
                financial_position="Strong cash position with $1,200 and diversified property portfolio generating $400/turn",
                property_strategy="Focus on completing orange monopoly while preventing opponent's railroad monopoly",
                immediate_goals=[
                    "Acquire New York Avenue to complete orange monopoly",
                    "Develop existing properties to 2-house level",
                    "Maintain $800 cash reserve for opportunities"
                ],
                threats=[
                    "Player2 owns 3 railroads, one away from transportation monopoly",
                    "Player3 has strong cash position for competitive bidding"
                ],
                opportunities=[
                    "Boardwalk available for acquisition",
                    "Player4 in financial difficulty, potential trade partner"
                ]
            )

        Early-game analysis::

            analysis = PlayerAnalysis(
                financial_position="Healthy starting position with $1,100 after initial purchases",
                property_strategy="Acquire diverse properties for trading leverage and rental income",
                immediate_goals=[
                    "Target orange or red properties for high-traffic locations",
                    "Avoid expensive blue properties in early game"
                ],
                threats=[
                    "No immediate threats, all players in development phase"
                ],
                opportunities=[
                    "Multiple property groups still available",
                    "Good trading positions developing"
                ]
            )

    Note:
        Analysis should be updated regularly as game state changes and new
        information becomes available through player actions and market dynamics.

    """

    financial_position: str = Field(
        ...,
        min_length=20,
        max_length=300,
        description="Comprehensive assessment of current financial position including cash, assets, and income",
        examples=[
            "Strong cash position with $1,200 and diversified property portfolio generating $400/turn",
            "Healthy starting position with $1,100 after initial purchases",
            "Tight cash flow with $300 but high-income potential from developed properties",
        ],
    )

    property_strategy: str = Field(
        ...,
        min_length=15,
        max_length=250,
        description="Current property acquisition and development strategy including monopoly targets",
        examples=[
            "Focus on completing orange monopoly while preventing opponent's railroad monopoly",
            "Acquire diverse properties for trading leverage and rental income",
            "Develop existing monopolies to maximum rental potential",
        ],
    )

    immediate_goals: list[str] = Field(
        ...,
        min_length=1,
        max_length=5,
        description="Short-term tactical goals and priorities for the next few turns",
        examples=[
            [
                "Acquire New York Avenue to complete orange monopoly",
                "Develop existing properties to 2-house level",
            ],
            ["Target orange or red properties for high-traffic locations"],
            ["Raise cash through strategic property mortgaging"],
        ],
    )

    threats: list[str] = Field(
        default_factory=list,
        description="Identified threats from other players including potential monopolies and competitive risks",
        examples=[
            ["Player2 owns 3 railroads, one away from transportation monopoly"],
            ["Player3 has strong cash position for competitive bidding"],
            ["No immediate threats, all players in development phase"],
        ],
    )

    opportunities: list[str] = Field(
        default_factory=list,
        description="Current opportunities available for strategic advancement and competitive positioning",
        examples=[
            [
                "Boardwalk available for acquisition",
                "Player4 in financial difficulty, potential trade partner",
            ],
            ["Multiple property groups still available"],
            ["Opportunity to corner housing market through strategic development"],
        ],
    )

    @computed_field
    @property
    def strategic_outlook(self) -> str:
        """Generate overall strategic outlook based on analysis.

        Returns:
            str: Overall strategic position assessment.

        """
        threat_count = len(self.threats)
        opportunity_count = len(self.opportunities)

        if opportunity_count > threat_count:
            return "Favorable - More opportunities than threats"
        if threat_count > opportunity_count:
            return "Challenging - More threats than opportunities"
        return "Balanced - Equal opportunities and threats"


class GameEvent(BaseModel):
    """Comprehensive model for game events, transactions, and state changes.

    This model captures all significant events that occur during Monopoly gameplay,
    including transactions, property changes, card draws, and strategic actions.
    It provides detailed logging and tracking for game analysis and replay capabilities.

    The event model supports:
    - Complete transaction logging with financial impacts
    - Property-related events and ownership changes
    - Player actions and strategic decisions
    - Random events from cards and dice rolls
    - Detailed metadata for analysis and debugging

    Attributes:
        event_type (str): Classification of the event type for categorization
            and analysis (e.g., "property_purchase", "rent_payment", "card_draw").
        player (str): Name of the player primarily involved in the event.
            Must be a valid player currently in the game.
        description (str): Human-readable description of what occurred
            during the event for logging and display purposes.
        money_change (int): Financial impact of the event on the involved player.
            Positive values indicate money gained, negative indicate money lost.
        property_involved (Optional[str]): Name of the property involved in the
            event, if applicable (e.g., for purchases, rent, development).
        details (Dict[str, Any]): Additional structured data about the event
            including game state changes, transaction details, and metadata.

    Examples:
        Property purchase event::

            event = GameEvent(
                event_type="property_purchase",
                player="Player1",
                description="Player1 purchased St. James Place for $180",
                money_change=-180,
                property_involved="St. James Place",
                details={"property_color": "orange", "purchase_price": 180}
            )

        Rent payment event::

            event = GameEvent(
                event_type="rent_payment",
                player="Player2",
                description="Player2 paid $350 rent to Player1 for landing on developed St. James Place",
                money_change=-350,
                property_involved="St. James Place",
                details={"rent_amount": 350, "house_count": 2, "recipient": "Player1"}
            )

        Card draw event::

            event = GameEvent(
                event_type="card_draw",
                player="Player3",
                description="Player3 drew Chance card: Advance to Boardwalk",
                money_change=0,
                property_involved=None,
                details={"card_type": "chance", "card_text": "Advance to Boardwalk", "movement": "Boardwalk"}
            )

    Note:
        Events should be logged chronologically to maintain complete game history.
        The details field can contain any additional structured data relevant to the event.

    """

    event_type: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Classification of the event type for categorization and analysis",
        examples=[
            "property_purchase",
            "rent_payment",
            "card_draw",
            "jail_escape",
            "house_construction",
            "trade_completed",
            "bankruptcy_declared",
        ],
    )

    player: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Name of the player primarily involved in the event",
        examples=["Player1", "Alice", "Strategic_AI", "Human_Player"],
    )

    description: str = Field(
        ...,
        min_length=10,
        max_length=200,
        description="Human-readable description of what occurred during the event",
        examples=[
            "Player1 purchased St. James Place for $180",
            "Player2 paid $350 rent to Player1 for landing on developed St. James Place",
            "Player3 drew Chance card: Advance to Boardwalk",
        ],
    )

    money_change: int = Field(
        default=0,
        ge=-20000,
        le=20000,
        description="Financial impact of the event on the involved player (negative for losses)",
        examples=[0, -180, -350, 200, 1500, -50],
    )

    property_involved: str | None = Field(
        default=None,
        min_length=3,
        max_length=30,
        description="Name of the property involved in the event, if applicable",
        examples=[
            "St. James Place",
            "Boardwalk",
            "Reading Railroad",
            "Electric Company",
        ],
    )

    details: dict[str, Any] = Field(
        default_factory=dict,
        description="Additional structured data about the event including game state changes and metadata",
        examples=[
            {"property_color": "orange", "purchase_price": 180},
            {"rent_amount": 350, "house_count": 2, "recipient": "Player1"},
            {
                "card_type": "chance",
                "card_text": "Advance to Boardwalk",
                "movement": "Boardwalk",
            },
        ],
    )

    @computed_field
    @property
    def is_financial_event(self) -> bool:
        """Determine if event has financial impact.

        Returns:
            bool: True if event involves money change, False otherwise.

        """
        return self.money_change != 0

    @computed_field
    @property
    def is_property_event(self) -> bool:
        """Determine if event involves a property.

        Returns:
            bool: True if event involves a property, False otherwise.

        """
        return self.property_involved is not None


class DiceRoll(BaseModel):
    """Model for dice roll results and movement calculation in Monopoly.

    This model captures the outcome of rolling two six-sided dice, which is
    fundamental to Monopoly gameplay for determining player movement, jail
    escape attempts, and various game mechanics.

    The dice roll model includes:
    - Individual die results for transparency
    - Total movement calculation
    - Doubles detection for special rules
    - Statistical analysis capabilities
    - Integration with game event logging

    Attributes:
        die1 (int): Result of the first die (1-6).
        die2 (int): Result of the second die (1-6).

    Examples:
        Regular movement roll::

            roll = DiceRoll(die1=3, die2=5)
            print(f"Rolled {roll.total}, move {roll.total} spaces")
            # Output: "Rolled 8, move 8 spaces"

        Doubles roll for extra turn::

            roll = DiceRoll(die1=4, die2=4)
            if roll.is_doubles:
                print(f"Rolled doubles ({roll.die1}s), take another turn!")
            # Output: "Rolled doubles (4s), take another turn!"

        Jail escape attempt::

            roll = DiceRoll(die1=2, die2=6)
            if roll.is_doubles:
                print("Rolled doubles, escaped jail!")
            else:
                print("No doubles, remain in jail")
            # Output: "No doubles, remain in jail"

    Note:
        Rolling doubles three times in a row sends the player to jail.
        Doubles allow extra turns but also carry strategic risks.

    """

    die1: int = Field(
        ...,
        ge=1,
        le=6,
        description="Result of the first die (1-6)",
        examples=[1, 2, 3, 4, 5, 6],
    )

    die2: int = Field(
        ...,
        ge=1,
        le=6,
        description="Result of the second die (1-6)",
        examples=[1, 2, 3, 4, 5, 6],
    )

    @computed_field
    @property
    def total(self) -> int:
        """Calculate total movement from both dice.

        Returns:
            int: Sum of both dice (2-12).

        """
        return self.die1 + self.die2

    @computed_field
    @property
    def is_doubles(self) -> bool:
        """Determine if the roll is doubles.

        Returns:
            bool: True if both dice show the same value, False otherwise.

        """
        return self.die1 == self.die2

    @computed_field
    @property
    def roll_description(self) -> str:
        """Generate human-readable description of the roll.

        Returns:
            str: Descriptive text of the dice roll result.

        """
        if self.is_doubles:
            return f"Rolled doubles {self.die1}s (total: {self.total})"
        return f"Rolled {self.die1} and {self.die2} (total: {self.total})"


class Property(BaseModel):
    """Comprehensive model for Monopoly board properties with development and ownership
    tracking.

    This model represents individual properties on the Monopoly board, including
    streets, railroads, utilities, and special spaces. It tracks ownership,
    development level, mortgage status, and rent calculation for complete
    property management.

    The property model supports:
    - Complete ownership and development tracking
    - Dynamic rent calculation based on development
    - Mortgage and unmortgage functionality
    - Property group and monopoly detection
    - Financial analysis and investment metrics

    Attributes:
        name (str): Official property name as displayed on the board.
        position (int): Board position (0-39) for movement and location tracking.
        property_type (PropertyType): Category of property (street, railroad, utility, special).
        color (PropertyColor): Color group for monopoly formation and development.
        price (int): Base purchase price of the property.
        rent (List[int]): Rent schedule [base, 1 house, 2 house, 3 house, 4 house, hotel].
        house_cost (int): Cost to build each house on the property.
        mortgage_value (int): Cash value when mortgaged (typically half of purchase price).
        owner (Optional[str]): Name of current owner, None if unowned.
        houses (int): Number of houses currently built (0-4).
        hotel (bool): Whether property has a hotel (replaces 4 houses).
        mortgaged (bool): Whether property is currently mortgaged.

    Examples:
        Undeveloped street property::

            property = Property(
                name="St. James Place",
                position=16,
                property_type=PropertyType.STREET,
                color=PropertyColor.ORANGE,
                price=180,
                rent=[14, 70, 200, 550, 750, 950],
                house_cost=100,
                mortgage_value=90,
                owner="Player1",
                houses=0,
                hotel=False,
                mortgaged=False
            )

        Developed property with houses::

            property = Property(
                name="Boardwalk",
                position=39,
                property_type=PropertyType.STREET,
                color=PropertyColor.DARK_BLUE,
                price=400,
                rent=[50, 200, 600, 1400, 1700, 2000],
                house_cost=200,
                mortgage_value=200,
                owner="Player2",
                houses=3,
                hotel=False,
                mortgaged=False
            )

        Railroad property::

            property = Property(
                name="Reading Railroad",
                position=5,
                property_type=PropertyType.RAILROAD,
                color=PropertyColor.RAILROAD,
                price=200,
                rent=[25, 50, 100, 200, 0, 0],  # Rent depends on railroads owned
                house_cost=0,
                mortgage_value=100,
                owner="Player3",
                houses=0,
                hotel=False,
                mortgaged=False
            )

    Note:
        Properties can only be developed when the owner has a complete color group monopoly.
        Houses must be built evenly across all properties in a monopoly group.

    """

    name: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Official property name as displayed on the board",
        examples=[
            "St. James Place",
            "Boardwalk",
            "Reading Railroad",
            "Electric Company",
        ],
    )

    position: int = Field(
        ...,
        ge=0,
        le=39,
        description="Board position (0-39) for movement and location tracking",
        # GO, Reading Railroad, St. James Place, Boardwalk
        examples=[0, 5, 16, 39],
    )

    property_type: PropertyType = Field(
        ..., description="Category of property (street, railroad, utility, special)"
    )

    color: PropertyColor = Field(
        ..., description="Color group for monopoly formation and development"
    )

    price: int = Field(
        ...,
        ge=0,
        le=1000,
        description="Base purchase price of the property",
        # Mediterranean, St. James, Railroad, Boardwalk
        examples=[60, 180, 200, 400],
    )

    rent: list[int] = Field(
        ...,
        min_length=6,
        max_length=6,
        description="Rent schedule [base, 1 house, 2 house, 3 house, 4 house, hotel]",
        examples=[
            [14, 70, 200, 550, 750, 950],  # St. James Place
            [50, 200, 600, 1400, 1700, 2000],  # Boardwalk
            [25, 50, 100, 200, 0, 0],  # Railroad
        ],
    )

    house_cost: int = Field(
        default=0,
        ge=0,
        le=200,
        description="Cost to build each house on the property",
        examples=[0, 50, 100, 150, 200],
    )

    mortgage_value: int = Field(
        ...,
        ge=0,
        le=500,
        description="Cash value when mortgaged (typically half of purchase price)",
        examples=[30, 90, 100, 200],  # Half of property prices
    )

    owner: str | None = Field(
        default=None,
        min_length=1,
        max_length=20,
        description="Name of current owner, None if unowned",
        examples=[None, "Player1", "Alice", "Strategic_AI"],
    )

    houses: int = Field(
        default=0,
        ge=0,
        le=4,
        description="Number of houses currently built (0-4)",
        examples=[0, 1, 2, 3, 4],
    )

    hotel: bool = Field(
        default=False, description="Whether property has a hotel (replaces 4 houses)"
    )

    mortgaged: bool = Field(
        default=False, description="Whether property is currently mortgaged"
    )

    def current_rent(self) -> int:
        """Calculate current rent based on development level and ownership.

        Returns:
            int: Current rent amount based on houses/hotel and property type.

        """
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
        return self.rent[self.houses]

    @computed_field
    @property
    def is_developed(self) -> bool:
        """Determine if property has any development.

        Returns:
            bool: True if property has houses or hotel, False otherwise.

        """
        return self.houses > 0 or self.hotel

    @computed_field
    @property
    def development_cost(self) -> int:
        """Calculate total cost invested in development.

        Returns:
            int: Total amount spent on houses and hotels.

        """
        cost = self.houses * self.house_cost
        if self.hotel:
            cost += self.house_cost  # Hotel costs same as house
        return cost

    @computed_field
    @property
    def total_investment(self) -> int:
        """Calculate total investment in property including purchase and development.

        Returns:
            int: Total amount invested in property.

        """
        return self.price + self.development_cost


class Player(BaseModel):
    r"""Comprehensive model for individual players in Monopoly with complete state
    tracking.

    This model represents a player's complete state in the Monopoly game, including
    financial position, property ownership, location, jail status, and strategic
    metrics. It supports advanced player management and strategic analysis.

    The player model includes:
    - Complete financial tracking with cash and asset management
    - Property ownership and portfolio management
    - Board position and movement tracking
    - Jail status and escape mechanics
    - Strategic metrics and performance analysis
    - Bankruptcy detection and game elimination

    Attributes:
        name (str): Unique player identifier and display name.
        money (int): Current cash holdings available for purchases and payments.
        position (int): Current board position (0-39) for movement and location.
        properties (List[str]): List of owned property names for portfolio tracking.
        jail_cards (int): Number of "Get Out of Jail Free" cards held.
        in_jail (bool): Whether player is currently in jail.
        jail_turns (int): Number of turns spent in jail (max 3).
        doubles_count (int): Consecutive doubles rolled this turn (max 3).
        bankrupt (bool): Whether player has declared bankruptcy and is eliminated.

    Examples:
        Starting player state::\n

            player = Player(
                name="Player1",
                money=1500,
                position=0,
                properties=[],
                jail_cards=0,
                in_jail=False,
                jail_turns=0,
                doubles_count=0,
                bankrupt=False
            )

        Mid-game player with properties::\n

            player = Player(
                name="Strategic_AI",
                money=800,
                position=16,
                properties=["St. James Place", "Tennessee Avenue", "Reading Railroad"],
                jail_cards=1,
                in_jail=False,
                jail_turns=0,
                doubles_count=0,
                bankrupt=False
            )

        Player in jail::\n

            player = Player(
                name="Player2",
                money=200,
                position=10,  # Jail position
                properties=["Mediterranean Avenue", "Baltic Avenue"],
                jail_cards=0,
                in_jail=True,
                jail_turns=2,
                doubles_count=0,
                bankrupt=False
            )

    Note:
        Players are eliminated from the game when they declare bankruptcy.
        The game ends when only one player remains solvent.

    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Unique player identifier and display name",
        examples=["Player1", "Alice", "Strategic_AI", "Human_Player"],
    )

    money: int = Field(
        default=1500,
        ge=0,
        le=50000,
        description="Current cash holdings available for purchases and payments",
        examples=[1500, 800, 200, 2500, 0],
    )

    position: int = Field(
        default=0,
        ge=0,
        le=39,
        description="Current board position (0-39) for movement and location tracking",
        # GO, Railroad, Jail, St. James, Boardwalk
        examples=[0, 5, 10, 16, 39],
    )

    properties: list[str] = Field(
        default_factory=list,
        description="List of owned property names for portfolio tracking",
        examples=[
            [],
            ["St. James Place", "Tennessee Avenue"],
            ["Reading Railroad", "Pennsylvania Railroad"],
            ["Mediterranean Avenue", "Baltic Avenue", "Electric Company"],
        ],
    )

    jail_cards: int = Field(
        default=0,
        ge=0,
        le=2,
        description="Number of 'Get Out of Jail Free' cards held",
        examples=[0, 1, 2],
    )

    in_jail: bool = Field(
        default=False, description="Whether player is currently in jail"
    )

    jail_turns: int = Field(
        default=0,
        ge=0,
        le=3,
        description="Number of turns spent in jail (max 3 before forced payment)",
        examples=[0, 1, 2, 3],
    )

    doubles_count: int = Field(
        default=0,
        ge=0,
        le=3,
        description="Consecutive doubles rolled this turn (3 doubles = go to jail)",
        examples=[0, 1, 2, 3],
    )

    bankrupt: bool = Field(
        default=False,
        description="Whether player has declared bankruptcy and is eliminated",
    )

    def can_afford(self, amount: int) -> bool:
        """Check if player can afford a given amount with current cash.

        Args:
            amount (int): Amount to check affordability for.

        Returns:
            bool: True if player has sufficient cash, False otherwise.

        """
        return self.money >= amount

    def net_worth(self, properties_dict: dict[str, Property]) -> int:
        """Calculate player's total net worth including properties and development.

        Args:
            properties_dict (Dict[str, Property]): Dictionary of all properties by name.

        Returns:
            int: Total net worth including cash, properties, and development.

        """
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

    @computed_field
    @property
    def is_active(self) -> bool:
        """Determine if player is still active in the game.

        Returns:
            bool: True if player is not bankrupt, False otherwise.

        """
        return not self.bankrupt

    @computed_field
    @property
    def property_count(self) -> int:
        """Get total number of properties owned.

        Returns:
            int: Count of owned properties.

        """
        return len(self.properties)

    @computed_field
    @property
    def liquidity_ratio(self) -> float:
        """Calculate ratio of cash to total assets (liquidity measure).

        Returns:
            float: Ratio of cash to total net worth (0.0 to 1.0).

        """
        if self.money == 0:
            return 0.0
        # Simple approximation without full property dictionary
        estimated_asset_value = self.money + (
            len(self.properties) * 150
        )  # Rough estimate
        return self.money / max(estimated_asset_value, 1)

    @computed_field
    @property
    def jail_status(self) -> str:
        """Get current jail status description.

        Returns:
            str: Description of current jail status.

        """
        if not self.in_jail:
            return "Free"
        if self.jail_turns == 0:
            return "Just jailed"
        if self.jail_turns < 3:
            return f"In jail ({self.jail_turns} turns)"
        return "Must pay fine"
