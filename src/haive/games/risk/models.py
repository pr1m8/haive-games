"""Pydantic models for Risk game components.

This module defines comprehensive data models for the Risk strategy game,
including territories, continents, players, cards, moves, and game analysis.
All models use Pydantic for validation with extensive documentation and examples.

The Risk implementation supports classic world domination gameplay with
AI-powered strategic analysis, multi-phase turns, and complex territorial
control mechanics.

Examples:
    Creating a territory::

        territory = Territory(
            name="Eastern Australia",
            continent="Australia",
            owner="player_1",
            armies=5,
            adjacent=["Western Australia", "New Guinea"]
        )

    Setting up a player::

        player = Player(
            name="General Smith",
            cards=[Card(card_type=CardType.INFANTRY, territory_name="Alaska")],
            unplaced_armies=3
        )

    Creating an attack move::

        attack = RiskMove(
            move_type=MoveType.ATTACK,
            player="player_1",
            from_territory="Ukraine",
            to_territory="Middle East",
            attack_dice=3
        )
"""

from enum import Enum

from pydantic import BaseModel, Field, computed_field, field_validator


class CardType(str, Enum):
    """Types of Risk cards for army reinforcement trading.

    Risk cards are collected by conquering territories and can be traded
    in sets for additional armies. The four card types correspond to
    different military units and provide strategic options for players.

    Attributes:
        INFANTRY: Basic ground unit card, most common type.
        CAVALRY: Mobile unit card, medium rarity.
        ARTILLERY: Heavy weapon card, provides firepower bonus.
        WILD: Special card that can substitute for any other type.

    Examples:
        Standard card types::

            infantry_card = CardType.INFANTRY
            cavalry_card = CardType.CAVALRY
            artillery_card = CardType.ARTILLERY

        Special wild card::

            wild_card = CardType.WILD  # Can be used as any type

        Trading combinations::

            # Valid trading sets:
            # - 3 of same type (3 infantry, 3 cavalry, 3 artillery)
            # - 1 of each type (1 infantry, 1 cavalry, 1 artillery)
            # - Any combination with wild cards

    Note:
        Card trading values typically increase each time cards are traded,
        starting at 4 armies for the first trade and increasing by 2 each time.
    """

    INFANTRY = "infantry"  #: Basic ground unit, represents foot soldiers
    CAVALRY = "cavalry"  #: Mobile unit, represents mounted troops
    ARTILLERY = "artillery"  #: Heavy weapons, represents cannons and siege equipment
    WILD = "wild"  #: Special card that can substitute for any type


class Card(BaseModel):
    """A Risk card that can be traded for army reinforcements.

    Risk cards are earned by conquering at least one territory per turn
    and can be accumulated and traded in strategic sets for additional
    armies. Each card typically shows a territory and has a unit type.

    The card system adds strategic depth by encouraging aggressive play
    (to earn cards) while providing timing decisions about when to trade
    for maximum advantage.

    Attributes:
        card_type (CardType): The military unit type shown on the card.
        territory_name (Optional[str]): Territory depicted on the card, if any.

    Examples:
        Territory-specific card::

            alaska_card = Card(
                card_type=CardType.INFANTRY,
                territory_name="Alaska"
            )

        Generic unit card::

            cavalry_card = Card(
                card_type=CardType.CAVALRY
                # No specific territory
            )

        Wild card::

            wild_card = Card(
                card_type=CardType.WILD,
                territory_name="Special"
            )

    Note:
        Territory names on cards are typically for thematic purposes
        and don't affect trading value, but may provide strategic
        information about board state.
    """

    card_type: CardType = Field(
        ...,
        description="The military unit type represented by this card",
        examples=[
            CardType.INFANTRY,
            CardType.CAVALRY,
            CardType.ARTILLERY,
            CardType.WILD,
        ],
    )

    territory_name: str | None = Field(
        None,
        max_length=50,
        description="Name of the territory depicted on the card, if any",
        examples=["Alaska", "Brazil", "China", "Egypt", "Ukraine", None],
    )

    def __str__(self) -> str:
        """String representation of the card.

        Returns:
            str: Human-readable card description.

        Examples:
            >>> card = Card(card_type=CardType.INFANTRY, territory_name="Alaska")
            >>> str(card)
            "Infantry (Alaska)"
            >>> card = Card(card_type=CardType.WILD)
            >>> str(card)
            "Wild"
        """
        if self.territory_name:
            return f"{self.card_type.value.capitalize()} ({self.territory_name})"
        return f"{self.card_type.value.capitalize()}"

    @computed_field
    @property
    def is_wild(self) -> bool:
        """Check if this is a wild card.

        Returns:
            bool: True if this is a wild card that can substitute for any type.

        Examples:
            >>> wild_card = Card(card_type=CardType.WILD)
            >>> wild_card.is_wild
            True
            >>> infantry_card = Card(card_type=CardType.INFANTRY)
            >>> infantry_card.is_wild
            False
        """
        return self.card_type == CardType.WILD


class Territory(BaseModel):
    """A territory on the Risk game board.

    Territories are the fundamental units of control in Risk. Each territory
    belongs to a continent, can be owned by a player, contains armies for
    defense, and connects to adjacent territories for movement and attack.

    The territorial system forms the core of Risk strategy, as players
    must control territories to earn reinforcements and achieve victory
    conditions (total world domination or objective completion).

    Attributes:
        name (str): Unique identifier and display name for the territory.
        continent (str): The continent this territory belongs to.
        owner (Optional[str]): The player who currently controls this territory.
        armies (int): Number of armies stationed in this territory for defense.
        adjacent (List[str]): Names of territories that border this one.

    Examples:
        Strategic territory setup::

            ukraine = Territory(
                name="Ukraine",
                continent="Europe",
                owner="player_1",
                armies=8,
                adjacent=["Scandinavia", "Northern Europe", "Southern Europe",
                         "Ural", "Afghanistan", "Middle East"]
            )

        Neutral territory::

            greenland = Territory(
                name="Greenland",
                continent="North America",
                # No owner initially
                armies=2,
                adjacent=["Northwest Territory", "Ontario", "Quebec", "Iceland"]
            )

        Fortified position::

            egypt = Territory(
                name="Egypt",
                continent="Africa",
                owner="player_2",
                armies=12,  # Heavily fortified
                adjacent=["Libya", "East Africa", "Middle East"]
            )

    Note:
        Territory adjacency defines the game's strategic geography.
        Control of key chokepoints and continental borders often
        determines game outcomes.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="Unique name identifying this territory on the game board",
        examples=["Alaska", "Brazil", "China", "Egypt", "Ukraine", "Madagascar"],
    )

    continent: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Name of the continent this territory belongs to",
        examples=[
            "North America",
            "South America",
            "Europe",
            "Africa",
            "Asia",
            "Australia",
        ],
    )

    owner: str | None = Field(
        None,
        description="Player ID who currently controls this territory",
        examples=["player_1", "player_2", "red_player", "blue_player", None],
    )

    armies: int = Field(
        default=0,
        ge=0,
        le=100,
        description="Number of armies stationed in this territory (0-100)",
        examples=[1, 5, 12, 25, 3],
    )

    adjacent: list[str] = Field(
        default_factory=list,
        description="List of territory names that border this territory",
        examples=[
            ["Western Europe", "Northern Europe", "Southern Europe"],
            ["Quebec", "Ontario", "Western United States"],
            ["China", "India", "Ural"],
        ],
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        """Validate territory name is properly formatted.

        Args:
            v (str): Territory name to validate.

        Returns:
            str: Cleaned and validated territory name.

        Raises:
            ValueError: If name is empty or contains invalid characters.
        """
        name = v.strip()
        if not name:
            raise ValueError("Territory name cannot be empty")
        return name

    @field_validator("armies")
    @classmethod
    def validate_armies(cls, v: int) -> int:
        """Validate army count is reasonable.

        Args:
            v (int): Army count to validate.

        Returns:
            int: Validated army count.

        Raises:
            ValueError: If army count is negative.
        """
        if v < 0:
            raise ValueError("Army count cannot be negative")
        return v

    def __str__(self) -> str:
        """String representation of the territory.

        Returns:
            str: Human-readable territory description.

        Examples:
            >>> territory = Territory(name="Alaska", continent="North America",
            ...                      owner="player_1", armies=3)
            >>> str(territory)
            "Alaska (player_1, 3 armies)"
        """
        owner_str = f"{self.owner}" if self.owner else "Unoccupied"
        return f"{self.name} ({owner_str}, {self.armies} armies)"

    @computed_field
    @property
    def is_occupied(self) -> bool:
        """Check if territory is currently occupied by a player.

        Returns:
            bool: True if territory has an owner, False if neutral.
        """
        return self.owner is not None

    @computed_field
    @property
    def defense_strength(self) -> int:
        """Calculate defensive strength of this territory.

        Returns:
            int: Maximum dice this territory can roll in defense (1-2).

        Note:
            Territories with 1 army can defend with 1 die,
            territories with 2+ armies can defend with 2 dice.
        """
        return min(2, max(1, self.armies))


class Continent(BaseModel):
    """A continent grouping of territories with bonus reinforcements.

    Continents provide structure to the Risk board and offer strategic
    objectives. Players who control all territories in a continent
    receive bonus armies each turn, creating natural strategic goals.

    Continental control is often the key to victory in Risk, as the
    bonus armies compound over time and provide significant advantages
    in the lengthy conquest campaigns.

    Attributes:
        name (str): The name of the continent.
        bonus (int): Bonus armies awarded for complete continental control.
        territories (List[str]): Names of all territories in this continent.

    Examples:
        High-value continent::

            asia = Continent(
                name="Asia",
                bonus=7,  # Highest bonus but hardest to hold
                territories=[
                    "Ural", "Siberia", "Yakutsk", "Kamchatka", "Irkutsk",
                    "Mongolia", "China", "Siam", "India", "Middle East",
                    "Afghanistan", "Japan"
                ]
            )

        Balanced continent::

            europe = Continent(
                name="Europe",
                bonus=5,
                territories=[
                    "Iceland", "Scandinavia", "Ukraine", "Great Britain",
                    "Northern Europe", "Western Europe", "Southern Europe"
                ]
            )

        Easy-to-defend continent::

            australia = Continent(
                name="Australia",
                bonus=2,  # Small but defensible
                territories=["Indonesia", "New Guinea", "Western Australia", "Eastern Australia"]
            )

    Note:
        Continent bonuses create risk-reward tradeoffs. Larger continents
        offer bigger bonuses but are harder to conquer and defend.
        Australia is traditionally the easiest to defend but offers
        the smallest bonus.
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=20,
        description="Name of the continent",
        examples=[
            "North America",
            "South America",
            "Europe",
            "Africa",
            "Asia",
            "Australia",
        ],
    )

    bonus: int = Field(
        ...,
        ge=1,
        le=10,
        description="Number of bonus armies awarded for controlling all territories (1-10)",
        examples=[2, 3, 5, 7],  # Australia=2, Europe=5, Asia=7
    )

    territories: list[str] = Field(
        default_factory=list,
        min_length=1,
        description="Names of all territories that belong to this continent",
        examples=[
            [
                "Alaska",
                "Northwest Territory",
                "Greenland",
                "Alberta",
                "Ontario",
                "Quebec",
                "Western United States",
                "Eastern United States",
                "Central America",
            ],
            ["Venezuela", "Brazil", "Peru", "Argentina"],
            ["Indonesia", "New Guinea", "Western Australia", "Eastern Australia"],
        ],
    )

    @field_validator("territories")
    @classmethod
    def validate_territories(cls, v: list[str]) -> list[str]:
        """Validate territory list is not empty and contains valid names.

        Args:
            v (List[str]): Territory names to validate.

        Returns:
            List[str]: Validated territory list.

        Raises:
            ValueError: If territory list is empty or contains invalid names.
        """
        if not v:
            raise ValueError("Continent must contain at least one territory")

        # Remove empty territory names
        valid_territories = [t.strip() for t in v if t.strip()]
        if not valid_territories:
            raise ValueError("Continent must contain valid territory names")

        return valid_territories

    def __str__(self) -> str:
        """String representation of the continent.

        Returns:
            str: Human-readable continent description.

        Examples:
            >>> continent = Continent(name="Europe", bonus=5, territories=["..."])
            >>> str(continent)
            "Europe (Bonus: 5)"
        """
        return f"{self.name} (Bonus: {self.bonus})"

    @computed_field
    @property
    def territory_count(self) -> int:
        """Get the number of territories in this continent.

        Returns:
            int: Count of territories in the continent.
        """
        return len(self.territories)

    @computed_field
    @property
    def bonus_per_territory(self) -> float:
        """Calculate bonus armies per territory in this continent.

        Returns:
            float: Bonus efficiency ratio for strategic evaluation.

        Note:
            Higher ratios indicate more efficient continents to control.
            Australia typically has the highest ratio (0.5), while
            Asia has a lower ratio (0.58) despite its large bonus.
        """
        return self.bonus / max(1, len(self.territories))


class Player(BaseModel):
    """A player in the Risk game.

    Players are the strategic decision-makers in Risk, controlling
    territories, managing armies, and executing complex multi-turn
    plans for world domination. Each player maintains their own
    hand of cards and army reserves.

    Player management includes tracking eliminated status, which
    occurs when a player loses all territories, transferring their
    cards to the conquering player and removing them from play.

    Attributes:
        name (str): The player's identifier and display name.
        cards (List[Card]): Risk cards in the player's hand for trading.
        unplaced_armies (int): Armies available for placement but not yet deployed.
        eliminated (bool): Whether this player has been defeated.

    Examples:
        Active player with resources::

            player = Player(
                name="General Patton",
                cards=[
                    Card(card_type=CardType.INFANTRY, territory_name="Alaska"),
                    Card(card_type=CardType.CAVALRY, territory_name="Brazil"),
                    Card(card_type=CardType.ARTILLERY, territory_name="Egypt")
                ],
                unplaced_armies=5
            )

        Starting player::

            new_player = Player(
                name="Commander Lee",
                unplaced_armies=20  # Initial army allocation
            )

        Eliminated player::

            defeated_player = Player(
                name="Admiral Nelson",
                eliminated=True
                # Cards transferred to conquering player
            )

    Note:
        Card accumulation is crucial for late-game army generation.
        Players must balance aggressive expansion (to earn cards)
        with defensive positioning (to avoid elimination).
    """

    name: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="Player's name or identifier",
        examples=[
            "General Patton",
            "Commander Lee",
            "Admiral Nelson",
            "player_1",
            "red_player",
        ],
    )

    cards: list[Card] = Field(
        default_factory=list,
        description="Risk cards in the player's hand available for trading",
        examples=[
            [],  # No cards
            [Card(card_type=CardType.INFANTRY)],  # Single card
            [  # Trading set
                Card(card_type=CardType.INFANTRY, territory_name="Alaska"),
                Card(card_type=CardType.CAVALRY, territory_name="Brazil"),
                Card(card_type=CardType.ARTILLERY, territory_name="Egypt"),
            ],
        ],
    )

    unplaced_armies: int = Field(
        default=0,
        ge=0,
        le=200,
        description="Number of armies available for placement but not yet deployed (0-200)",
        examples=[0, 3, 5, 12, 25],
    )

    eliminated: bool = Field(
        default=False,
        description="Whether this player has been eliminated from the game",
        examples=[False, True],
    )

    @field_validator("unplaced_armies")
    @classmethod
    def validate_unplaced_armies(cls, v: int) -> int:
        """Validate unplaced army count is reasonable.

        Args:
            v (int): Unplaced army count to validate.

        Returns:
            int: Validated army count.

        Raises:
            ValueError: If army count is negative.
        """
        if v < 0:
            raise ValueError("Unplaced armies cannot be negative")
        return v

    def __str__(self) -> str:
        """String representation of the player.

        Returns:
            str: Human-readable player description.

        Examples:
            >>> player = Player(name="General Patton", unplaced_armies=5,
            ...                cards=[Card(card_type=CardType.INFANTRY)])
            >>> str(player)
            "General Patton (Active, 5 unplaced armies, 1 cards)"
        """
        status = "Eliminated" if self.eliminated else "Active"
        return f"{self.name} ({status}, {self.unplaced_armies} unplaced armies, {len(self.cards)} cards)"

    @computed_field
    @property
    def can_trade_cards(self) -> bool:
        """Check if player has enough cards to make a trade.

        Returns:
            bool: True if player has 3+ cards (minimum for trading).

        Note:
            Players with 5+ cards must trade at the start of their turn.
            Trading with exactly 3 cards is optional but often strategic.
        """
        return len(self.cards) >= 3

    @computed_field
    @property
    def must_trade_cards(self) -> bool:
        """Check if player is forced to trade cards.

        Returns:
            bool: True if player has 5+ cards and must trade before placing armies.

        Note:
            This rule prevents card hoarding and maintains game flow.
        """
        return len(self.cards) >= 5


class MoveType(str, Enum):
    """Types of moves available in Risk gameplay.

    Risk turns are structured around specific move types that correspond
    to different phases of play. Each move type has distinct rules,
    timing requirements, and strategic implications.

    The move type system ensures proper game flow and enables the AI
    to understand and plan appropriate actions for each phase.

    Attributes:
        PLACE_ARMIES: Deploy reinforcement armies to controlled territories.
        ATTACK: Launch military attacks against adjacent enemy territories.
        FORTIFY: Transfer armies between connected friendly territories.
        TRADE_CARDS: Exchange card sets for additional armies.

    Examples:
        Turn phase progression::

            # 1. Start of turn - reinforcement phase
            trade_move = MoveType.TRADE_CARDS  # If required/desired
            place_move = MoveType.PLACE_ARMIES

            # 2. Combat phase
            attack_moves = [MoveType.ATTACK, MoveType.ATTACK, ...]

            # 3. End of turn - reorganization
            fortify_move = MoveType.FORTIFY  # Optional

        Strategic move sequencing::

            # Aggressive expansion turn
            moves = [
                MoveType.PLACE_ARMIES,  # Strengthen attack position
                MoveType.ATTACK,        # Primary assault
                MoveType.ATTACK,        # Follow-up attack
                MoveType.FORTIFY        # Consolidate gains
            ]

    Note:
        Move types correspond to Risk's traditional turn structure:
        reinforcement → attack → fortification. Card trading can
        occur at the start if the player has 3+ cards.
    """

    PLACE_ARMIES = "place_armies"  #: Deploy reinforcement armies to territories
    ATTACK = "attack"  #: Launch attacks against enemy territories
    FORTIFY = "fortify"  #: Move armies between friendly territories
    TRADE_CARDS = "trade_cards"  #: Exchange card sets for bonus armies


class RiskMove(BaseModel):
    """A move action in the Risk game.

    Risk moves represent all player actions during gameplay, from army
    placement and attacks to strategic repositioning. Each move contains
    all necessary information for validation and execution.

    The flexible move structure accommodates Risk's varied action types
    while providing clear validation rules and strategic context for
    AI decision-making systems.

    Attributes:
        move_type (MoveType): The category of action being performed.
        player (str): The player executing this move.
        from_territory (Optional[str]): Source territory for attacks and fortifications.
        to_territory (Optional[str]): Target territory for all move types.
        armies (Optional[int]): Number of armies to deploy, attack with, or transfer.
        cards (Optional[List[Card]]): Cards to trade for army bonuses.
        attack_dice (Optional[int]): Number of dice to use in attack (1-3).

    Examples:
        Army placement move::

            place_move = RiskMove(
                move_type=MoveType.PLACE_ARMIES,
                player="player_1",
                to_territory="Ukraine",
                armies=5
            )

        Attack move::

            attack_move = RiskMove(
                move_type=MoveType.ATTACK,
                player="player_1",
                from_territory="Ukraine",
                to_territory="Middle East",
                armies=6,  # Attacking with 6 armies (max 3 dice)
                attack_dice=3
            )

        Fortification move::

            fortify_move = RiskMove(
                move_type=MoveType.FORTIFY,
                player="player_1",
                from_territory="Siberia",
                to_territory="China",
                armies=4
            )

        Card trading move::

            trade_move = RiskMove(
                move_type=MoveType.TRADE_CARDS,
                player="player_1",
                cards=[
                    Card(card_type=CardType.INFANTRY),
                    Card(card_type=CardType.CAVALRY),
                    Card(card_type=CardType.ARTILLERY)
                ]
            )

    Note:
        Move validation depends on game state, including territory
        ownership, army counts, and adjacency relationships.
        Invalid moves should be rejected with clear error messages.
    """

    move_type: MoveType = Field(
        ...,
        description="The type of action being performed",
        examples=[
            MoveType.PLACE_ARMIES,
            MoveType.ATTACK,
            MoveType.FORTIFY,
            MoveType.TRADE_CARDS,
        ],
    )

    player: str = Field(
        ...,
        min_length=1,
        description="Identifier of the player making this move",
        examples=["player_1", "player_2", "red_player", "General Patton"],
    )

    from_territory: str | None = Field(
        None,
        description="Source territory for attacks and fortifications",
        examples=["Ukraine", "Alaska", "Brazil", "Egypt", None],
    )

    to_territory: str | None = Field(
        None,
        description="Target territory for army placement, attacks, and fortifications",
        examples=["Middle East", "Greenland", "Argentina", "Libya", None],
    )

    armies: int | None = Field(
        None,
        ge=1,
        le=100,
        description="Number of armies to place, attack with, or transfer (1-100)",
        examples=[1, 3, 5, 8, 12, None],
    )

    cards: list[Card] | None = Field(
        None,
        min_length=3,
        max_length=5,
        description="Cards to trade in for bonus armies (must be 3-5 cards)",
        examples=[
            None,
            [
                Card(card_type=CardType.INFANTRY),
                Card(card_type=CardType.CAVALRY),
                Card(card_type=CardType.ARTILLERY),
            ],
        ],
    )

    attack_dice: int | None = Field(
        None,
        ge=1,
        le=3,
        description="Number of dice to use in attack (1-3, limited by attacking armies)",
        examples=[1, 2, 3, None],
    )

    @field_validator("armies")
    @classmethod
    def validate_armies(cls, v: int | None) -> int | None:
        """Validate army count is positive if provided.

        Args:
            v (Optional[int]): Army count to validate.

        Returns:
            Optional[int]: Validated army count or None.

        Raises:
            ValueError: If army count is not positive.
        """
        if v is not None and v <= 0:
            raise ValueError("Army count must be positive")
        return v

    @field_validator("attack_dice")
    @classmethod
    def validate_attack_dice(cls, v: int | None) -> int | None:
        """Validate attack dice count is within valid range.

        Args:
            v (Optional[int]): Dice count to validate.

        Returns:
            Optional[int]: Validated dice count or None.

        Raises:
            ValueError: If dice count is not 1-3.
        """
        if v is not None and not (1 <= v <= 3):
            raise ValueError("Attack dice must be between 1 and 3")
        return v

    def __str__(self) -> str:
        """String representation of the move.

        Returns:
            str: Human-readable move description.

        Examples:
            >>> move = RiskMove(move_type=MoveType.ATTACK, player="player_1",
            ...                from_territory="Ukraine", to_territory="Middle East",
            ...                attack_dice=3)
            >>> str(move)
            "player_1 attacks from Ukraine to Middle East with 3 dice"
        """
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

    @computed_field
    @property
    def is_aggressive(self) -> bool:
        """Determine if this move is aggressive (attack or large army
        placement).

        Returns:
            bool: True if move represents aggressive action.

        Note:
            Used for AI personality and strategic analysis.
        """
        if self.move_type == MoveType.ATTACK:
            return True
        if self.move_type == MoveType.PLACE_ARMIES and self.armies and self.armies >= 3:
            return True
        return False


class PhaseType(str, Enum):
    """Game phases in Risk turn structure.

    Risk gameplay follows a structured turn sequence with distinct phases
    that determine available actions and strategic timing. Understanding
    phase transitions is crucial for AI planning and move validation.

    The phase system provides clear game flow while allowing for strategic
    flexibility within each phase's constraints.

    Attributes:
        SETUP: Initial game setup with territory allocation and army placement.
        REINFORCE: Army reinforcement and card trading phase.
        ATTACK: Combat phase with territorial conquest attempts.
        FORTIFY: End-of-turn army repositioning and consolidation.
        GAME_OVER: Game completion with victory conditions met.

    Examples:
        Standard turn progression::

            turn_phases = [
                PhaseType.REINFORCE,  # Get armies, place them
                PhaseType.ATTACK,     # Optional combat
                PhaseType.FORTIFY     # Optional repositioning
            ]

        Game lifecycle::

            game_phases = [
                PhaseType.SETUP,      # Initial setup
                # ... many turns of REINFORCE → ATTACK → FORTIFY
                PhaseType.GAME_OVER   # Victory achieved
            ]

    Note:
        Phase enforcement ensures proper Risk rule compliance and
        provides structure for AI decision-making algorithms.
    """

    SETUP = "setup"  #: Initial game setup and territory allocation
    REINFORCE = "reinforce"  #: Army reinforcement and card trading phase
    ATTACK = "attack"  #: Combat and territorial conquest phase
    FORTIFY = "fortify"  #: End-of-turn army movement and positioning
    GAME_OVER = "game_over"  #: Game completion with victory achieved


class GameStatus(str, Enum):
    """Overall status of the Risk game.

    Tracks the high-level state of the game to determine whether
    play should continue or if victory conditions have been met.

    Attributes:
        IN_PROGRESS: Game is actively being played.
        FINISHED: Game has ended with a clear victory.

    Examples:
        Active game::

            status = GameStatus.IN_PROGRESS
            # Players continue taking turns

        Completed game::

            status = GameStatus.FINISHED
            # Victory conditions met, declare winner
    """

    IN_PROGRESS = "in_progress"  #: Game is actively being played
    FINISHED = "finished"  #: Game has ended with victory achieved


class RiskAnalysis(BaseModel):
    """Comprehensive analysis of a player's Risk position.

    Strategic analysis is crucial for AI decision-making in Risk's
    complex, multi-turn gameplay. This model provides structured
    evaluation of territorial control, military strength, and
    strategic positioning.

    The analysis system enables sophisticated AI that can evaluate
    long-term strategic positions beyond immediate tactical moves,
    considering continental bonuses, defensive positioning, and
    overall game progression.

    Attributes:
        player (str): The player being analyzed.
        controlled_continents (List[str]): Continents fully controlled by the player.
        controlled_territories (int): Total number of territories owned.
        total_armies (int): Sum of all armies across all territories.
        position_evaluation (str): Overall strategic assessment.
        recommended_move (RiskMove): Suggested optimal move.
        explanation (str): Detailed reasoning for the analysis and recommendation.

    Examples:
        Strong position analysis::

            analysis = RiskAnalysis(
                player="player_1",
                controlled_continents=["Australia", "South America"],
                controlled_territories=18,
                total_armies=45,
                position_evaluation="winning",
                recommended_move=RiskMove(
                    move_type=MoveType.ATTACK,
                    player="player_1",
                    from_territory="Brazil",
                    to_territory="North Africa",
                    attack_dice=3
                ),
                explanation="Player controls two continents providing 5 bonus armies per turn. Should continue aggressive expansion into Africa while maintaining defensive positions."
            )

        Defensive position analysis::

            analysis = RiskAnalysis(
                player="player_2",
                controlled_continents=[],
                controlled_territories=8,
                total_armies=12,
                position_evaluation="losing",
                recommended_move=RiskMove(
                    move_type=MoveType.FORTIFY,
                    player="player_2",
                    from_territory="Greenland",
                    to_territory="Quebec",
                    armies=3
                ),
                explanation="Player is behind in territory count and lacks continental bonuses. Should consolidate forces and defend key chokepoints to survive."
            )

    Note:
        Analysis quality directly impacts AI performance. Sophisticated
        evaluation considers not just current position but also trajectory,
        opponent threats, and multi-turn strategic opportunities.
    """

    player: str = Field(
        ...,
        description="Identifier of the player being analyzed",
        examples=["player_1", "player_2", "red_player", "General Patton"],
    )

    controlled_continents: list[str] = Field(
        default_factory=list,
        description="Names of continents fully controlled by this player",
        examples=[
            [],  # No continents
            ["Australia"],  # Single continent
            ["Australia", "South America", "Europe"],  # Multiple continents
        ],
    )

    controlled_territories: int = Field(
        ...,
        ge=0,
        le=42,  # Maximum territories on standard board
        description="Total number of territories controlled by this player (0-42)",
        examples=[5, 12, 18, 25, 35],
    )

    total_armies: int = Field(
        ...,
        ge=0,
        le=500,
        description="Sum of all armies across all controlled territories (0-500)",
        examples=[8, 25, 45, 78, 120],
    )

    position_evaluation: str = Field(
        ...,
        description="Overall strategic assessment of the player's position",
        examples=[
            "winning",
            "favorable",
            "neutral",
            "unfavorable",
            "losing",
            "critical",
        ],
    )

    recommended_move: RiskMove = Field(
        ..., description="Strategically optimal move for the current position"
    )

    explanation: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Detailed reasoning behind the analysis and move recommendation",
        examples=[
            "Player controls Australia providing defensive bonus. Should expand into Asia while maintaining territorial integrity.",
            "Critical position requires immediate consolidation. Recommend fortifying chokepoints and avoiding risky attacks.",
            "Strong continental control provides sustained army advantage. Aggressive expansion recommended to capitalize on momentum.",
        ],
    )

    @field_validator("position_evaluation")
    @classmethod
    def validate_position_evaluation(cls, v: str) -> str:
        """Validate position evaluation uses standard terminology.

        Args:
            v (str): Position evaluation to validate.

        Returns:
            str: Validated evaluation string.

        Raises:
            ValueError: If evaluation is not recognized.
        """
        valid_evaluations = {
            "winning",
            "favorable",
            "neutral",
            "unfavorable",
            "losing",
            "critical",
        }
        evaluation = v.strip().lower()
        if evaluation not in valid_evaluations:
            raise ValueError(
                f"Position evaluation must be one of: {', '.join(valid_evaluations)}"
            )
        return evaluation

    def __str__(self) -> str:
        """String representation of the analysis.

        Returns:
            str: Comprehensive analysis summary.

        Examples:
            >>> analysis = RiskAnalysis(player="player_1", controlled_continents=["Australia"],
            ...                        controlled_territories=12, total_armies=25,
            ...                        position_evaluation="favorable", ...)
            >>> str(analysis)
            "Analysis for player_1:
            Controlled continents: Australia
            Controlled territories: 12
            Total armies: 25
            Position evaluation: favorable
            ..."
        """
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

    @computed_field
    @property
    def continent_bonus(self) -> int:
        """Calculate total bonus armies from controlled continents.

        Returns:
            int: Total bonus armies per turn from continental control.

        Note:
            This is a simplified calculation. Real implementation would
            need access to continent definitions with their bonus values.
        """
        # Simplified continent bonuses (would normally reference game data)
        continent_bonuses = {
            "Australia": 2,
            "South America": 2,
            "Africa": 3,
            "North America": 5,
            "Europe": 5,
            "Asia": 7,
        }
        return sum(
            continent_bonuses.get(continent, 0)
            for continent in self.controlled_continents
        )

    @computed_field
    @property
    def average_armies_per_territory(self) -> float:
        """Calculate average army strength per territory.

        Returns:
            float: Average armies per territory for strategic assessment.

        Note:
            Higher ratios indicate stronger defensive positions or
            preparation for major offensives.
        """
        return self.total_armies / max(1, self.controlled_territories)
