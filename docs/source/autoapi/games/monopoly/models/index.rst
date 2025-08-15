games.monopoly.models
=====================

.. py:module:: games.monopoly.models


Classes
-------

.. autoapisummary::

   games.monopoly.models.BuildingDecision
   games.monopoly.models.CardType
   games.monopoly.models.DiceRoll
   games.monopoly.models.GameEvent
   games.monopoly.models.JailDecision
   games.monopoly.models.Player
   games.monopoly.models.PlayerActionType
   games.monopoly.models.PlayerAnalysis
   games.monopoly.models.Property
   games.monopoly.models.PropertyColor
   games.monopoly.models.PropertyDecision
   games.monopoly.models.PropertyType
   games.monopoly.models.TradeOffer
   games.monopoly.models.TradeResponse


Module Contents
---------------

.. py:class:: BuildingDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategic decision model for property development and rental income optimization.

   This model captures the decision-making process for building houses and hotels
   on monopolized properties, including development strategy, cash flow management,
   and rental income optimization considerations.

   The building decision involves:
   - Strategic property development prioritization
   - Cash flow analysis and investment timing
   - Rental income optimization calculations
   - Housing shortage manipulation tactics
   - Long-term portfolio development strategy

   .. attribute:: property_name

      Name of the specific property to develop.
      Must be a property owned by the player in a monopolized color group.

      :type: str

   .. attribute:: action

      Type of development - BUILD_HOUSE for adding
      houses (1-4 per property) or BUILD_HOTEL for hotel upgrade.

      :type: PlayerActionType

   .. attribute:: quantity

      Number of houses to build (1-4) or 1 for hotel.
      Houses must be built evenly across monopoly group.

      :type: int

   .. attribute:: reasoning

      Detailed strategic reasoning for the development decision
      including financial analysis and rental income projections.

      :type: str

   .. rubric:: Examples

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

   .. note::

      Houses must be built evenly across all properties in a monopoly group.
      Hotels require 4 houses to be traded in plus hotel cost.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BuildingDecision
      :collapse:

   .. py:method:: validate_building_action(v: PlayerActionType) -> PlayerActionType
      :classmethod:


      Validate that action is appropriate for building.

      :param v: Action to validate.
      :type v: PlayerActionType

      :returns: Validated action.
      :rtype: PlayerActionType

      :raises ValueError: If action is not valid for building.


      .. autolink-examples:: validate_building_action
         :collapse:


   .. py:method:: validate_quantity(v: int) -> int
      :classmethod:


      Validate building quantity is within game limits.

      :param v: Quantity to validate.
      :type v: int

      :returns: Validated quantity.
      :rtype: int

      :raises ValueError: If quantity is outside valid range.


      .. autolink-examples:: validate_quantity
         :collapse:


   .. py:attribute:: action
      :type:  PlayerActionType
      :value: None



   .. py:property:: is_hotel_upgrade
      :type: bool


      Determine if decision is for hotel upgrade.

      :returns: True if upgrading to hotel, False if building houses.
      :rtype: bool

      .. autolink-examples:: is_hotel_upgrade
         :collapse:


   .. py:attribute:: property_name
      :type:  str
      :value: None



   .. py:attribute:: quantity
      :type:  int
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: CardType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of cards drawn during Monopoly gameplay.

   Represents the two types of cards that players can draw when landing
   on specific board spaces, each with different effects and outcomes.

   Values:
       CHANCE: Orange cards with various effects (movement, payments, etc.)
       COMMUNITY_CHEST: Blue cards typically involving payments or rewards


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CardType
      :collapse:

   .. py:attribute:: CHANCE
      :value: 'chance'



   .. py:attribute:: COMMUNITY_CHEST
      :value: 'community_chest'



.. py:class:: DiceRoll(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for dice roll results and movement calculation in Monopoly.

   This model captures the outcome of rolling two six-sided dice, which is
   fundamental to Monopoly gameplay for determining player movement, jail
   escape attempts, and various game mechanics.

   The dice roll model includes:
   - Individual die results for transparency
   - Total movement calculation
   - Doubles detection for special rules
   - Statistical analysis capabilities
   - Integration with game event logging

   .. attribute:: die1

      Result of the first die (1-6).

      :type: int

   .. attribute:: die2

      Result of the second die (1-6).

      :type: int

   .. rubric:: Examples

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

   .. note::

      Rolling doubles three times in a row sends the player to jail.
      Doubles allow extra turns but also carry strategic risks.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: DiceRoll
      :collapse:

   .. py:attribute:: die1
      :type:  int
      :value: None



   .. py:attribute:: die2
      :type:  int
      :value: None



   .. py:property:: is_doubles
      :type: bool


      Determine if the roll is doubles.

      :returns: True if both dice show the same value, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_doubles
         :collapse:


   .. py:property:: roll_description
      :type: str


      Generate human-readable description of the roll.

      :returns: Descriptive text of the dice roll result.
      :rtype: str

      .. autolink-examples:: roll_description
         :collapse:


   .. py:property:: total
      :type: int


      Calculate total movement from both dice.

      :returns: Sum of both dice (2-12).
      :rtype: int

      .. autolink-examples:: total
         :collapse:


.. py:class:: GameEvent(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive model for game events, transactions, and state changes.

   This model captures all significant events that occur during Monopoly gameplay,
   including transactions, property changes, card draws, and strategic actions.
   It provides detailed logging and tracking for game analysis and replay capabilities.

   The event model supports:
   - Complete transaction logging with financial impacts
   - Property-related events and ownership changes
   - Player actions and strategic decisions
   - Random events from cards and dice rolls
   - Detailed metadata for analysis and debugging

   .. attribute:: event_type

      Classification of the event type for categorization
      and analysis (e.g., "property_purchase", "rent_payment", "card_draw").

      :type: str

   .. attribute:: player

      Name of the player primarily involved in the event.
      Must be a valid player currently in the game.

      :type: str

   .. attribute:: description

      Human-readable description of what occurred
      during the event for logging and display purposes.

      :type: str

   .. attribute:: money_change

      Financial impact of the event on the involved player.
      Positive values indicate money gained, negative indicate money lost.

      :type: int

   .. attribute:: property_involved

      Name of the property involved in the
      event, if applicable (e.g., for purchases, rent, development).

      :type: Optional[str]

   .. attribute:: details

      Additional structured data about the event
      including game state changes, transaction details, and metadata.

      :type: Dict[str, Any]

   .. rubric:: Examples

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

   .. note::

      Events should be logged chronologically to maintain complete game history.
      The details field can contain any additional structured data relevant to the event.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameEvent
      :collapse:

   .. py:attribute:: description
      :type:  str
      :value: None



   .. py:attribute:: details
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: event_type
      :type:  str
      :value: None



   .. py:property:: is_financial_event
      :type: bool


      Determine if event has financial impact.

      :returns: True if event involves money change, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_financial_event
         :collapse:


   .. py:property:: is_property_event
      :type: bool


      Determine if event involves a property.

      :returns: True if event involves a property, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_property_event
         :collapse:


   .. py:attribute:: money_change
      :type:  int
      :value: None



   .. py:attribute:: player
      :type:  str
      :value: None



   .. py:attribute:: property_involved
      :type:  str | None
      :value: None



.. py:class:: JailDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategic decision model for jail escape and turn management.

   This model captures the decision-making process when a player is in jail,
   including the choice of escape method, timing considerations, and strategic
   implications of remaining in jail versus getting out immediately.

   The jail decision involves:
   - Immediate escape via fine payment ($50)
   - Risk-based escape attempt by rolling doubles
   - Using "Get Out of Jail Free" cards if available
   - Strategic evaluation of jail benefits in late game
   - Turn opportunity cost analysis

   .. attribute:: action

      The chosen escape method - PAY_JAIL_FINE for
      immediate release, ROLL_FOR_JAIL to attempt doubles, or USE_JAIL_CARD
      to use a "Get Out of Jail Free" card.

      :type: PlayerActionType

   .. attribute:: reasoning

      Detailed strategic reasoning for the decision including
      financial considerations, board position analysis, and timing factors.

      :type: str

   .. rubric:: Examples

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

   .. note::

      In late game, staying in jail can be strategically beneficial to avoid
      landing on expensive developed properties while still collecting rent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: JailDecision
      :collapse:

   .. py:method:: validate_jail_action(v: PlayerActionType) -> PlayerActionType
      :classmethod:


      Validate that action is appropriate for jail decisions.

      :param v: Action to validate.
      :type v: PlayerActionType

      :returns: Validated action.
      :rtype: PlayerActionType

      :raises ValueError: If action is not valid for jail decisions.


      .. autolink-examples:: validate_jail_action
         :collapse:


   .. py:attribute:: action
      :type:  PlayerActionType
      :value: None



   .. py:property:: has_immediate_cost
      :type: bool


      Determine if decision has immediate financial cost.

      :returns: True if action requires immediate payment, False otherwise.
      :rtype: bool

      .. autolink-examples:: has_immediate_cost
         :collapse:


   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: Player(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive model for individual players in Monopoly with complete state.
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

   .. attribute:: name

      Unique player identifier and display name.

      :type: str

   .. attribute:: money

      Current cash holdings available for purchases and payments.

      :type: int

   .. attribute:: position

      Current board position (0-39) for movement and location.

      :type: int

   .. attribute:: properties

      List of owned property names for portfolio tracking.

      :type: List[str]

   .. attribute:: jail_cards

      Number of "Get Out of Jail Free" cards held.

      :type: int

   .. attribute:: in_jail

      Whether player is currently in jail.

      :type: bool

   .. attribute:: jail_turns

      Number of turns spent in jail (max 3).

      :type: int

   .. attribute:: doubles_count

      Consecutive doubles rolled this turn (max 3).

      :type: int

   .. attribute:: bankrupt

      Whether player has declared bankruptcy and is eliminated.

      :type: bool

   .. rubric:: Examples

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

   .. note::

      Players are eliminated from the game when they declare bankruptcy.
      The game ends when only one player remains solvent.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Player
      :collapse:

   .. py:method:: can_afford(amount: int) -> bool

      Check if player can afford a given amount with current cash.

      :param amount: Amount to check affordability for.
      :type amount: int

      :returns: True if player has sufficient cash, False otherwise.
      :rtype: bool


      .. autolink-examples:: can_afford
         :collapse:


   .. py:method:: net_worth(properties_dict: dict[str, Property]) -> int

      Calculate player's total net worth including properties and development.

      :param properties_dict: Dictionary of all properties by name.
      :type properties_dict: Dict[str, Property]

      :returns: Total net worth including cash, properties, and development.
      :rtype: int


      .. autolink-examples:: net_worth
         :collapse:


   .. py:attribute:: bankrupt
      :type:  bool
      :value: None



   .. py:attribute:: doubles_count
      :type:  int
      :value: None



   .. py:attribute:: in_jail
      :type:  bool
      :value: None



   .. py:property:: is_active
      :type: bool


      Determine if player is still active in the game.

      :returns: True if player is not bankrupt, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_active
         :collapse:


   .. py:attribute:: jail_cards
      :type:  int
      :value: None



   .. py:property:: jail_status
      :type: str


      Get current jail status description.

      :returns: Description of current jail status.
      :rtype: str

      .. autolink-examples:: jail_status
         :collapse:


   .. py:attribute:: jail_turns
      :type:  int
      :value: None



   .. py:property:: liquidity_ratio
      :type: float


      Calculate ratio of cash to total assets (liquidity measure).

      :returns: Ratio of cash to total net worth (0.0 to 1.0).
      :rtype: float

      .. autolink-examples:: liquidity_ratio
         :collapse:


   .. py:attribute:: money
      :type:  int
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: position
      :type:  int
      :value: None



   .. py:attribute:: properties
      :type:  list[str]
      :value: None



   .. py:property:: property_count
      :type: int


      Get total number of properties owned.

      :returns: Count of owned properties.
      :rtype: int

      .. autolink-examples:: property_count
         :collapse:


.. py:class:: PlayerActionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Comprehensive enumeration of all possible player actions in Monopoly.

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


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerActionType
      :collapse:

   .. py:attribute:: BUILD_HOTEL
      :value: 'build_hotel'



   .. py:attribute:: BUILD_HOUSE
      :value: 'build_house'



   .. py:attribute:: BUY_PROPERTY
      :value: 'buy_property'



   .. py:attribute:: DECLARE_BANKRUPTCY
      :value: 'declare_bankruptcy'



   .. py:attribute:: DRAW_CARD
      :value: 'draw_card'



   .. py:attribute:: GO_TO_JAIL
      :value: 'go_to_jail'



   .. py:attribute:: MORTGAGE_PROPERTY
      :value: 'mortgage_property'



   .. py:attribute:: PASS_PROPERTY
      :value: 'pass_property'



   .. py:attribute:: PAY_JAIL_FINE
      :value: 'pay_jail_fine'



   .. py:attribute:: PAY_RENT
      :value: 'pay_rent'



   .. py:attribute:: PAY_TAX
      :value: 'pay_tax'



   .. py:attribute:: ROLL_FOR_JAIL
      :value: 'roll_for_jail'



   .. py:attribute:: TRADE_ACCEPT
      :value: 'trade_accept'



   .. py:attribute:: TRADE_DECLINE
      :value: 'trade_decline'



   .. py:attribute:: TRADE_OFFER
      :value: 'trade_offer'



   .. py:attribute:: UNMORTGAGE_PROPERTY
      :value: 'unmortgage_property'



   .. py:attribute:: USE_JAIL_CARD
      :value: 'use_jail_card'



.. py:class:: PlayerAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive strategic analysis model for player position and game state.
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

   .. attribute:: financial_position

      Comprehensive assessment of current financial
      position including cash, assets, income potential, and liquidity.

      :type: str

   .. attribute:: property_strategy

      Current property acquisition and development
      strategy including monopoly targets and portfolio optimization.

      :type: str

   .. attribute:: immediate_goals

      Short-term tactical goals and priorities
      for the next few turns.

      :type: List[str]

   .. attribute:: threats

      Identified threats from other players including
      potential monopolies, competitive advantages, and strategic risks.

      :type: List[str]

   .. attribute:: opportunities

      Current opportunities available for strategic
      advancement and competitive positioning.

      :type: List[str]

   .. rubric:: Examples

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

   .. note::

      Analysis should be updated regularly as game state changes and new
      information becomes available through player actions and market dynamics.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerAnalysis
      :collapse:

   .. py:attribute:: financial_position
      :type:  str
      :value: None



   .. py:attribute:: immediate_goals
      :type:  list[str]
      :value: None



   .. py:attribute:: opportunities
      :type:  list[str]
      :value: None



   .. py:attribute:: property_strategy
      :type:  str
      :value: None



   .. py:property:: strategic_outlook
      :type: str


      Generate overall strategic outlook based on analysis.

      :returns: Overall strategic position assessment.
      :rtype: str

      .. autolink-examples:: strategic_outlook
         :collapse:


   .. py:attribute:: threats
      :type:  list[str]
      :value: None



.. py:class:: Property(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive model for Monopoly board properties with development and ownership.
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

   .. attribute:: name

      Official property name as displayed on the board.

      :type: str

   .. attribute:: position

      Board position (0-39) for movement and location tracking.

      :type: int

   .. attribute:: property_type

      Category of property (street, railroad, utility, special).

      :type: PropertyType

   .. attribute:: color

      Color group for monopoly formation and development.

      :type: PropertyColor

   .. attribute:: price

      Base purchase price of the property.

      :type: int

   .. attribute:: rent

      Rent schedule [base, 1 house, 2 house, 3 house, 4 house, hotel].

      :type: List[int]

   .. attribute:: house_cost

      Cost to build each house on the property.

      :type: int

   .. attribute:: mortgage_value

      Cash value when mortgaged (typically half of purchase price).

      :type: int

   .. attribute:: owner

      Name of current owner, None if unowned.

      :type: Optional[str]

   .. attribute:: houses

      Number of houses currently built (0-4).

      :type: int

   .. attribute:: hotel

      Whether property has a hotel (replaces 4 houses).

      :type: bool

   .. attribute:: mortgaged

      Whether property is currently mortgaged.

      :type: bool

   .. rubric:: Examples

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

   .. note::

      Properties can only be developed when the owner has a complete color group monopoly.
      Houses must be built evenly across all properties in a monopoly group.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Property
      :collapse:

   .. py:method:: current_rent() -> int

      Calculate current rent based on development level and ownership.

      :returns: Current rent amount based on houses/hotel and property type.
      :rtype: int


      .. autolink-examples:: current_rent
         :collapse:


   .. py:attribute:: color
      :type:  PropertyColor
      :value: None



   .. py:property:: development_cost
      :type: int


      Calculate total cost invested in development.

      :returns: Total amount spent on houses and hotels.
      :rtype: int

      .. autolink-examples:: development_cost
         :collapse:


   .. py:attribute:: hotel
      :type:  bool
      :value: None



   .. py:attribute:: house_cost
      :type:  int
      :value: None



   .. py:attribute:: houses
      :type:  int
      :value: None



   .. py:property:: is_developed
      :type: bool


      Determine if property has any development.

      :returns: True if property has houses or hotel, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_developed
         :collapse:


   .. py:attribute:: mortgage_value
      :type:  int
      :value: None



   .. py:attribute:: mortgaged
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: owner
      :type:  str | None
      :value: None



   .. py:attribute:: position
      :type:  int
      :value: None



   .. py:attribute:: price
      :type:  int
      :value: None



   .. py:attribute:: property_type
      :type:  PropertyType
      :value: None



   .. py:attribute:: rent
      :type:  list[int]
      :value: None



   .. py:property:: total_investment
      :type: int


      Calculate total investment in property including purchase and development.

      :returns: Total amount invested in property.
      :rtype: int

      .. autolink-examples:: total_investment
         :collapse:


.. py:class:: PropertyColor

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Property color groups for monopoly formation and development.

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


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyColor
      :collapse:

   .. py:attribute:: BROWN
      :value: 'brown'



   .. py:attribute:: DARK_BLUE
      :value: 'dark_blue'



   .. py:attribute:: GREEN
      :value: 'green'



   .. py:attribute:: LIGHT_BLUE
      :value: 'light_blue'



   .. py:attribute:: ORANGE
      :value: 'orange'



   .. py:attribute:: PINK
      :value: 'pink'



   .. py:attribute:: RAILROAD
      :value: 'railroad'



   .. py:attribute:: RED
      :value: 'red'



   .. py:attribute:: SPECIAL
      :value: 'special'



   .. py:attribute:: UTILITY
      :value: 'utility'



   .. py:attribute:: YELLOW
      :value: 'yellow'



.. py:class:: PropertyDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategic decision model for property purchase and auction scenarios.

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

   .. attribute:: action

      The chosen action - either BUY_PROPERTY to
      purchase at list price or PASS_PROPERTY to trigger auction.

      :type: PlayerActionType

   .. attribute:: reasoning

      Detailed strategic reasoning for the decision including
      financial analysis, portfolio considerations, and strategic value.

      :type: str

   .. attribute:: max_bid

      Maximum bid amount if property goes to auction.
      Should be None if purchasing at list price.

      :type: Optional[int]

   .. rubric:: Examples

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

   .. note::

      When action is BUY_PROPERTY, max_bid should be None. When action is
      PASS_PROPERTY, max_bid determines auction participation level.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyDecision
      :collapse:

   .. py:method:: validate_property_action(v: PlayerActionType) -> PlayerActionType
      :classmethod:


      Validate that action is appropriate for property decisions.

      :param v: Action to validate.
      :type v: PlayerActionType

      :returns: Validated action.
      :rtype: PlayerActionType

      :raises ValueError: If action is not valid for property decisions.


      .. autolink-examples:: validate_property_action
         :collapse:


   .. py:attribute:: action
      :type:  PlayerActionType
      :value: None



   .. py:property:: is_auction_participant
      :type: bool


      Determine if player will participate in auction.

      :returns: True if player will bid in auction, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_auction_participant
         :collapse:


   .. py:attribute:: max_bid
      :type:  int | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: PropertyType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Enumeration of property types in the Monopoly game.

   Defines the four main categories of board spaces that players can
   interact with, each with distinct gameplay mechanics and rules.

   Values:
       STREET: Standard property that can be developed with houses/hotels
       RAILROAD: Transportation properties with special rent calculation
       UTILITY: Electric Company and Water Works with dice-based rent
       SPECIAL: Non-purchasable spaces like GO, Jail, Free Parking


   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PropertyType
      :collapse:

   .. py:attribute:: RAILROAD
      :value: 'railroad'



   .. py:attribute:: SPECIAL
      :value: 'special'



   .. py:attribute:: STREET
      :value: 'street'



   .. py:attribute:: UTILITY
      :value: 'utility'



.. py:class:: TradeOffer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive model for inter-player trade negotiations and strategic exchanges.

   This model captures complex trade offers between players, including property
   exchanges, cash considerations, and strategic reasoning. It supports multi-asset
   trades that are essential for monopoly completion and strategic positioning.

   The trade offer includes:
   - Multi-property exchange capabilities
   - Cash consideration balancing
   - Strategic reasoning and negotiation context
   - Fair value assessment and win-win scenarios
   - Monopoly completion and blocking strategies

   .. attribute:: offering_player

      Name of the player initiating the trade offer.
      Must be a valid player currently in the game.

      :type: str

   .. attribute:: receiving_player

      Name of the player receiving the trade offer.
      Must be a different player than the offering player.

      :type: str

   .. attribute:: offered_properties

      List of property names being offered.
      Properties must be owned by the offering player.

      :type: List[str]

   .. attribute:: offered_money

      Cash amount being offered as part of the trade.
      Must be less than or equal to offering player's available cash.

      :type: int

   .. attribute:: requested_properties

      List of property names being requested.
      Properties must be owned by the receiving player.

      :type: List[str]

   .. attribute:: requested_money

      Cash amount being requested as part of the trade.
      Must be less than or equal to receiving player's available cash.

      :type: int

   .. attribute:: reasoning

      Detailed explanation for the trade offer including
      strategic benefits, fair value justification, and mutual advantages.

      :type: str

   .. rubric:: Examples

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

   .. note::

      Trade offers should be mutually beneficial or strategically justified.
      Players cannot trade mortgaged properties or properties with buildings.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TradeOffer
      :collapse:

   .. py:method:: validate_different_players(v: str, info) -> str
      :classmethod:


      Validate that receiving player is different from offering player.

      :param v: Receiving player name to validate.
      :type v: str
      :param info: Validation info containing other field values.

      :returns: Validated receiving player name.
      :rtype: str

      :raises ValueError: If receiving player is the same as offering player.


      .. autolink-examples:: validate_different_players
         :collapse:


   .. py:property:: net_cash_flow
      :type: int


      Calculate net cash flow for the offering player.

      :returns: Net cash change for offering player (negative = paying out, positive = receiving).
      :rtype: int

      .. autolink-examples:: net_cash_flow
         :collapse:


   .. py:attribute:: offered_money
      :type:  int
      :value: None



   .. py:attribute:: offered_properties
      :type:  list[str]
      :value: None



   .. py:attribute:: offering_player
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: receiving_player
      :type:  str
      :value: None



   .. py:attribute:: requested_money
      :type:  int
      :value: None



   .. py:attribute:: requested_properties
      :type:  list[str]
      :value: None



   .. py:property:: total_assets_offered
      :type: int


      Calculate total number of assets being offered.

      :returns: Total count of properties and cash being offered.
      :rtype: int

      .. autolink-examples:: total_assets_offered
         :collapse:


   .. py:property:: total_assets_requested
      :type: int


      Calculate total number of assets being requested.

      :returns: Total count of properties and cash being requested.
      :rtype: int

      .. autolink-examples:: total_assets_requested
         :collapse:


.. py:class:: TradeResponse(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategic response model for trade offer evaluation and negotiation.

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

   .. attribute:: action

      Response decision - TRADE_ACCEPT to accept
      the offer as presented, or TRADE_DECLINE to reject.

      :type: PlayerActionType

   .. attribute:: reasoning

      Detailed explanation for the response decision
      including strategic analysis and value assessment.

      :type: str

   .. attribute:: counter_offer

      Alternative trade proposal if
      declining the original offer. Enables continued negotiation.

      :type: Optional[TradeOffer]

   .. rubric:: Examples

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

   .. note::

      Counter-offers should only be provided when declining. When accepting,
      counter_offer should be None.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TradeResponse
      :collapse:

   .. py:method:: validate_trade_action(v: PlayerActionType) -> PlayerActionType
      :classmethod:


      Validate that action is appropriate for trade responses.

      :param v: Action to validate.
      :type v: PlayerActionType

      :returns: Validated action.
      :rtype: PlayerActionType

      :raises ValueError: If action is not valid for trade responses.


      .. autolink-examples:: validate_trade_action
         :collapse:


   .. py:attribute:: action
      :type:  PlayerActionType
      :value: None



   .. py:attribute:: counter_offer
      :type:  TradeOffer | None
      :value: None



   .. py:property:: is_negotiation_continuing
      :type: bool


      Determine if negotiation continues with counter-offer.

      :returns: True if declining with counter-offer, False otherwise.
      :rtype: bool

      .. autolink-examples:: is_negotiation_continuing
         :collapse:


   .. py:attribute:: reasoning
      :type:  str
      :value: None



