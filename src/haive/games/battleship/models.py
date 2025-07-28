"""Pydantic models for Battleship naval strategy game components.

This module defines comprehensive data models for the classic Battleship game,
including ships, coordinates, attacks, board state, and strategic analysis.
All models use Pydantic for validation with extensive documentation and examples.

The Battleship implementation supports classic naval combat gameplay with
AI-powered strategic targeting, ship placement validation, and sophisticated
probability-based attack algorithms.

Examples:
    Creating ship coordinates::

        coordinates = Coordinates(row=3, col=5)
        print(f"Targeting {coordinates}")  # Targeting (3, 5)

    Placing a ship::

        destroyer_placement = ShipPlacement(
            ship_type=ShipType.DESTROYER,
            coordinates=[
                Coordinates(row=2, col=3),
                Coordinates(row=2, col=4)
            ]
        )

    Executing an attack::

        attack = MoveCommand(row=4, col=6)
        outcome = board.receive_attack(attack.row, attack.col)
        print(f"Attack result: {outcome}")
"""

from enum import Enum

from pydantic import BaseModel, Field, computed_field, field_validator, model_validator


class ShipType(str, Enum):
    """Naval ship types in Battleship with varying sizes and strategic roles.

    Each ship type represents a different class of naval vessel with unique
    characteristics. Ship variety adds strategic depth through different
    target profiles and placement considerations.

    The traditional Battleship fleet composition balances large, valuable
    targets (carriers, battleships) with smaller, harder-to-find vessels
    (destroyers, submarines).

    Attributes:
        CARRIER: Largest ship, primary strategic target (5 squares).
        BATTLESHIP: Heavy combat vessel, major threat (4 squares).
        CRUISER: Balanced warship, versatile platform (3 squares).
        SUBMARINE: Stealth vessel, hard to detect (3 squares).
        DESTROYER: Fast escort ship, smallest target (2 squares).

    Examples:
        Fleet composition analysis::

            fleet = [ShipType.CARRIER, ShipType.BATTLESHIP, ShipType.CRUISER,
                    ShipType.SUBMARINE, ShipType.DESTROYER]
            total_squares = sum(SHIP_SIZES[ship] for ship in fleet)  # 17 squares

        Strategic targeting priority::

            high_value_targets = [ShipType.CARRIER, ShipType.BATTLESHIP]
            stealth_targets = [ShipType.SUBMARINE]
            quick_targets = [ShipType.DESTROYER]

    Note:
        Ship types follow traditional naval classifications and provide
        different strategic value in terms of size, placement difficulty,
        and target priority for AI decision-making.
    """

    CARRIER = "Carrier"  #: Aircraft carrier, largest ship (5 squares)
    BATTLESHIP = "Battleship"  #: Heavy battleship, major combat vessel (4 squares)
    CRUISER = "Cruiser"  #: Medium cruiser, balanced warship (3 squares)
    SUBMARINE = "Submarine"  #: Submarine, stealth vessel (3 squares)
    DESTROYER = "Destroyef"  #: Destroyer, smallest escort ship (2 squares)


# Ship sizes by type for validation and game logic
SHIP_SIZES: dict[ShipType, int] = {
    ShipType.CARRIER: 5,  # Aircraft carrier - 5 squares
    ShipType.BATTLESHIP: 4,  # Battleship - 4 squares
    ShipType.CRUISER: 3,  # Cruiser - 3 squares
    ShipType.SUBMARINE: 3,  # Submarine - 3 squares
    ShipType.DESTROYER: 2,  # Destroyer - 2 squares
}


class Coordinates(BaseModel):
    """Represents a coordinate position on the Battleship game board.

    Coordinates use a standard (row, col) system with 0-based indexing
    for a 10x10 grid. This provides precise targeting for naval combat
    and supports conversion between different coordinate representations.

    The coordinate system enables strategic analysis, pattern recognition,
    and systematic search algorithms for AI targeting systems.

    Attributes:
        row (int): Row index from 0-9 (top to bottom).
        col (int): Column index from 0-9 (left to right).

    Examples:
        Basic coordinate creation::

            target = Coordinates(row=3, col=7)
            print(f"Targeting {target}")  # Targeting (3, 7)

        Coordinate arithmetic for search patterns::

            center = Coordinates(row=5, col=5)
            adjacent = [
                Coordinates(row=center.row-1, col=center.col),  # North
                Coordinates(row=center.row+1, col=center.col),  # South
                Coordinates(row=center.row, col=center.col-1),  # West
                Coordinates(row=center.row, col=center.col+1),  # East
            ]

        Grid traversal::

            all_coordinates = [
                Coordinates(row=r, col=c)
                for r in range(10) for c in range(10)
            ]

    Note:
        Standard naval notation (A1, B2, etc.) can be converted to/from
        this coordinate system for human-readable game interfaces.
    """

    row: int = Field(
        ...,
        ge=0,
        le=9,
        description="Row index on the game board (0-9, top to bottom)",
        examples=[0, 3, 5, 7, 9],
    )

    col: int = Field(
        ...,
        ge=0,
        le=9,
        description="Column index on the game board (0-9, left to right)",
        examples=[0, 2, 4, 6, 9],
    )

    def to_tuple(self) -> tuple[int, int]:
        """Convert coordinates to tuple representation.

        Returns:
            Tuple[int, int]: (row, col) tuple for easy comparison and hashing.

        Examples:
            >>> coord = Coordinates(row=3, col=5)
            >>> coord.to_tuple()
            (3, 5)
            >>> coord_set = {coord.to_tuple() for coord in coordinates_list}
        """
        return (self.row, self.col)

    def __str__(self) -> str:
        """String representation of coordinates.

        Returns:
            str: Human-readable coordinate description.

        Examples:
            >>> coord = Coordinates(row=3, col=5)
            >>> str(coord)
            "(3, 5)"
        """
        return f"({self.row}, {self.col})"

    def __hash__(self) -> int:
        """Hash implementation for set operations and dictionary keys.

        Returns:
            int: Hash value based on coordinate tuple.
        """
        return hash(self.to_tuple())

    def __eq__(self, other) -> bool:
        """Equality comparison for coordinates.

        Args:
            other: Another Coordinates instance or compatible object.

        Returns:
            bool: True if coordinates are equal.
        """
        if isinstance(other, Coordinates):
            return self.to_tuple() == other.to_tuple()
        return False

    @computed_field
    @property
    def is_corner(self) -> bool:
        """Check if coordinate is in a corner of the board.

        Returns:
            bool: True if coordinate is at (0,0), (0,9), (9,0), or (9,9).

        Note:
            Corner positions have unique strategic properties for ship
            placement and targeting algorithms.
        """
        return (self.row, self.col) in [(0, 0), (0, 9), (9, 0), (9, 9)]

    @computed_field
    @property
    def is_edge(self) -> bool:
        """Check if coordinate is on the edge of the board.

        Returns:
            bool: True if coordinate is on any board edge.

        Note:
            Edge positions limit ship placement options and affect
            AI search patterns.
        """
        return self.row in [0, 9] or self.col in [0, 9]


class Ship(BaseModel):
    """Represents a naval vessel on the Battleship game board.

    Ships are the primary game entities, each with a specific type, size,
    position, and damage state. Ship management includes placement validation,
    hit tracking, and sunk status determination.

    The ship model supports sophisticated damage tracking and strategic
    analysis for AI decision-making, including damage assessment and
    targeting priority calculations.

    Attributes:
        ship_type (ShipType): The class of naval vessel.
        size (int): Number of grid squares occupied by the ship.
        coordinates (List[Coordinates]): All positions occupied by the ship.
        hits (int): Number of successful attacks against this ship.

    Examples:
        Creating a horizontal destroyer::

            destroyer = Ship(
                ship_type=ShipType.DESTROYER,
                size=2,
                coordinates=[
                    Coordinates(row=3, col=4),
                    Coordinates(row=3, col=5)
                ]
            )

        Vertical aircraft carrier placement::

            carrier = Ship(
                ship_type=ShipType.CARRIER,
                size=5,
                coordinates=[
                    Coordinates(row=2, col=1),
                    Coordinates(row=3, col=1),
                    Coordinates(row=4, col=1),
                    Coordinates(row=5, col=1),
                    Coordinates(row=6, col=1)
                ]
            )

        Damage tracking::

            ship.hits = 2
            if ship.is_sunk:
                print(f"{ship.ship_type} has been destroyed!")

    Note:
        Ship coordinates must form a straight line (horizontal or vertical)
        and be contiguous. Size must match the ship type's expected size.
    """

    ship_type: ShipType = Field(
        ...,
        description="The class/type of naval vessel",
        examples=[ShipType.CARRIER, ShipType.BATTLESHIP, ShipType.DESTROYER],
    )

    size: int = Field(
        ...,
        ge=2,
        le=5,
        description="Number of grid squares occupied by the ship (2-5)",
        examples=[2, 3, 4, 5],
    )

    coordinates: list[Coordinates] = Field(
        default_factory=list,
        min_length=2,
        max_length=5,
        description="All board positions occupied by this ship",
        examples=[
            [
                Coordinates(row=3, col=4),
                Coordinates(row=3, col=5),
            ],  # Horizontal destroyer
            [
                Coordinates(row=2, col=1),
                Coordinates(row=3, col=1),
                Coordinates(row=4, col=1),
            ],  # Vertical cruiser
        ],
    )

    hits: int = Field(
        default=0,
        ge=0,
        le=5,
        description="Number of successful attacks against this ship (0-5)",
        examples=[0, 1, 2, 3, 4],
    )

    @field_validator("size")
    @classmethod
    def validate_size_matches_type(cls, v: int, info) -> int:
        """Validate ship size matches the expected size for its type.

        Args:
            v (int): Ship size to validate.
            info: Validation context with other field values.

        Returns:
            int: Validated size.

        Raises:
            ValueError: If size doesn't match expected size for ship type.
        """
        # Note: ship_type might not be available during validation
        # Size validation with type will be done in model_validator
        if not (2 <= v <= 5):
            raise ValueError("Ship size must be between 2 and 5")
        return v

    @model_validator(mode="after")
    def validate_ship_consistency(self) -> "Ship":
        """Validate ship size, coordinates, and type consistency.

        Returns:
            Ship: Validated ship instance.

        Raises:
            ValueError: If ship configuration is invalid.
        """
        # Validate size matches ship type
        expected_size = SHIP_SIZES.get(self.ship_type)
        if expected_size and self.size != expected_size:
            raise ValueError(
                f"{self.ship_type} must have size {expected_size}, got {self.size}"
            )

        # Validate coordinate count matches size
        if len(self.coordinates) != self.size:
            raise ValueError(
                f"Ship has {len(self.coordinates)} coordinates but size is {self.size}"
            )

        # Validate coordinates form a straight line
        if len(self.coordinates) >= 2:
            rows = [c.row for c in self.coordinates]
            cols = [c.col for c in self.coordinates]

            if len(set(rows)) == 1:  # Horizontal ship
                sorted_cols = sorted(cols)
                expected_cols = list(range(min(cols), max(cols) + 1))
                if sorted_cols != expected_cols:
                    raise ValueError("Horizontal ship coordinates must be contiguous")
            elif len(set(cols)) == 1:  # Vertical ship
                sorted_rows = sorted(rows)
                expected_rows = list(range(min(rows), max(rows) + 1))
                if sorted_rows != expected_rows:
                    raise ValueError("Vertical ship coordinates must be contiguous")
            else:
                raise ValueError(
                    "Ship coordinates must form a horizontal or vertical line"
                )

        return self

    @computed_field
    @property
    def is_sunk(self) -> bool:
        """Check if the ship has been completely destroyed.

        Returns:
            bool: True if hits equal or exceed ship size.

        Examples:
            >>> destroyer = Ship(ship_type=ShipType.DESTROYER, size=2, hits=2)
            >>> destroyer.is_sunk
            True
            >>> carrier = Ship(ship_type=ShipType.CARRIER, size=5, hits=3)
            >>> carrier.is_sunk
            False
        """
        return self.hits >= self.size

    @computed_field
    @property
    def damage_percentage(self) -> float:
        """Calculate percentage of ship that has been damaged.

        Returns:
            float: Damage percentage from 0.0 (undamaged) to 1.0 (sunk).

        Examples:
            >>> ship = Ship(ship_type=ShipType.CRUISER, size=3, hits=2)
            >>> ship.damage_percentage
            0.6666666666666666
        """
        return self.hits / max(1, self.size)

    @computed_field
    @property
    def orientation(self) -> str:
        """Determine ship orientation on the board.

        Returns:
            str: "horizontal", "vertical", or "single" for single-square ships.

        Note:
            Orientation affects targeting strategies and probability calculations.
        """
        if len(self.coordinates) <= 1:
            return "single"

        rows = [c.row for c in self.coordinates]
        if len(set(rows)) == 1:
            return "horizontal"
        return "vertical"

    def get_occupied_positions(self) -> list[tuple[int, int]]:
        """Get all board positions occupied by this ship.

        Returns:
            List[Tuple[int, int]]: List of (row, col) tuples.

        Examples:
            >>> ship = Ship(coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)])
            >>> ship.get_occupied_positions()
            [(3, 4), (3, 5)]
        """
        return [c.to_tuple() for c in self.coordinates]

    def __str__(self) -> str:
        """String representation of the ship.

        Returns:
            str: Human-readable ship description.

        Examples:
            >>> ship = Ship(ship_type=ShipType.DESTROYER, size=2,
            ...             coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)])
            >>> str(ship)
            "Destroyer (2): ['(3, 4)', '(3, 5)']"
        """
        return f"{self.ship_type} ({self.size}): {[str(c) for c in self.coordinates]}"


class ShipPlacement(BaseModel):
    """Represents a ship placement command for board setup.

    Ship placement defines where a naval vessel will be positioned on
    the game board. This model handles validation of placement rules
    including size requirements, orientation constraints, and overlap prevention.

    The placement system supports both manual positioning and AI-generated
    ship layouts with comprehensive validation for rule compliance.

    Attributes:
        ship_type (ShipType): The type of ship being placed.
        coordinates (List[Coordinates]): All positions the ship will occupy.

    Examples:
        Horizontal battleship placement::

            battleship_placement = ShipPlacement(
                ship_type=ShipType.BATTLESHIP,
                coordinates=[
                    Coordinates(row=5, col=2),
                    Coordinates(row=5, col=3),
                    Coordinates(row=5, col=4),
                    Coordinates(row=5, col=5)
                ]
            )

        Vertical submarine placement::

            submarine_placement = ShipPlacement(
                ship_type=ShipType.SUBMARINE,
                coordinates=[
                    Coordinates(row=1, col=8),
                    Coordinates(row=2, col=8),
                    Coordinates(row=3, col=8)
                ]
            )

        Compact destroyer placement::

            destroyer_placement = ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[
                    Coordinates(row=9, col=0),
                    Coordinates(row=9, col=1)
                ]
            )

    Note:
        Placement validation ensures ships don't overlap, stay within
        board boundaries, and maintain proper size and orientation.
    """

    ship_type: ShipType = Field(
        ...,
        description="The type of naval vessel being placed",
        examples=[
            ShipType.CARRIER,
            ShipType.BATTLESHIP,
            ShipType.CRUISER,
            ShipType.SUBMARINE,
            ShipType.DESTROYER,
        ],
    )

    coordinates: list[Coordinates] = Field(
        ...,
        min_length=2,
        max_length=5,
        description="All board positions the ship will occupy",
        examples=[
            [Coordinates(row=3, col=4), Coordinates(row=3, col=5)],  # Horizontal
            [Coordinates(row=2, col=1), Coordinates(row=3, col=1)],  # Vertical
        ],
    )

    @field_validator("coordinates")
    @classmethod
    def validate_coordinates(
        cls, coords: list[Coordinates | dict]
    ) -> list[Coordinates]:
        """Validate and normalize coordinate list.

        Args:
            coords: List of coordinates (Coordinates objects or dicts).

        Returns:
            List[Coordinates]: Validated coordinate list.

        Raises:
            ValueError: If coordinates are invalid format.
        """
        if not isinstance(coords, list):
            raise ValueError("Coordinates must be a list")

        processed_coords = []
        for c in coords:
            if isinstance(c, Coordinates):
                processed_coords.append(c)
            elif isinstance(c, dict):
                processed_coords.append(Coordinates(**c))
            else:
                raise ValueError(f"Invalid coordinate format: {c}")

        return processed_coords

    @model_validator(mode="after")
    def validate_placement_rules(self) -> "ShipPlacement":
        """Validate ship placement follows game rules.

        Returns:
            ShipPlacement: Validated placement.

        Raises:
            ValueError: If placement violates game rules.
        """
        # Validate coordinate count matches ship size
        expected_size = SHIP_SIZES[self.ship_type]
        if len(self.coordinates) != expected_size:
            raise ValueError(
                f"{self.ship_type} requires {expected_size} coordinates, got {len(self.coordinates)}"
            )

        # Validate coordinates form a straight line
        if len(self.coordinates) >= 2:
            rows = [c.row for c in self.coordinates]
            cols = [c.col for c in self.coordinates]

            if len(set(rows)) == 1:  # Horizontal
                sorted_cols = sorted(cols)
                expected_cols = list(range(min(cols), max(cols) + 1))
                if sorted_cols != expected_cols:
                    raise ValueError("Ship coordinates must be contiguous horizontally")
            elif len(set(cols)) == 1:  # Vertical
                sorted_rows = sorted(rows)
                expected_rows = list(range(min(rows), max(rows) + 1))
                if sorted_rows != expected_rows:
                    raise ValueError("Ship coordinates must be contiguous vertically")
            else:
                raise ValueError("Ship must be placed horizontally or vertically")

        return self

    def __str__(self) -> str:
        """String representation of the placement.

        Returns:
            str: Human-readable placement description.

        Examples:
            >>> placement = ShipPlacement(ship_type=ShipType.DESTROYER,
            ...                          coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)])
            >>> str(placement)
            "Destroyer at ['(3, 4)', '(3, 5)']"
        """
        return f"{self.ship_type} at {[str(c) for c in self.coordinates]}"


class ShipPlacementWrapper(BaseModel):
    """Wrapper for complete fleet placement returned by LLM agents.

    This model validates that a complete, legal fleet has been specified
    with all required ship types and no duplicates or overlaps. Used for
    AI-generated ship arrangements and setup validation.

    The wrapper ensures fleet completeness and provides structured error
    reporting for invalid configurations during automated setup.

    Attributes:
        placements (List[ShipPlacement]): Complete list of ship placements for one fleet.

    Examples:
        Complete fleet setup::

            fleet = ShipPlacementWrapper(
                placements=[
                    ShipPlacement(ship_type=ShipType.CARRIER, coordinates=[...]),
                    ShipPlacement(ship_type=ShipType.BATTLESHIP, coordinates=[...]),
                    ShipPlacement(ship_type=ShipType.CRUISER, coordinates=[...]),
                    ShipPlacement(ship_type=ShipType.SUBMARINE, coordinates=[...]),
                    ShipPlacement(ship_type=ShipType.DESTROYER, coordinates=[...])
                ]
            )

        Fleet validation::

            try:
                fleet = ShipPlacementWrapper(placements=ai_generated_placements)
                print("Fleet configuration is valid")
            except ValueError as e:
                print(f"Invalid fleet: {e}")

    Note:
        This wrapper enforces that exactly one ship of each type is included
        in the fleet, preventing duplicate or missing ships.
    """

    placements: list[ShipPlacement] = Field(
        ...,
        min_length=5,
        max_length=5,
        description="Complete list of ship placements for one fleet (exactly 5 ships)",
        examples=[
            [  # Example fleet with proper ship sizes
                ShipPlacement(
                    ship_type=ShipType.CARRIER,
                    coordinates=[
                        Coordinates(row=0, col=0),
                        Coordinates(row=0, col=1),
                        Coordinates(row=0, col=2),
                        Coordinates(row=0, col=3),
                        Coordinates(row=0, col=4),
                    ],
                ),
                ShipPlacement(
                    ship_type=ShipType.BATTLESHIP,
                    coordinates=[
                        Coordinates(row=1, col=0),
                        Coordinates(row=1, col=1),
                        Coordinates(row=1, col=2),
                        Coordinates(row=1, col=3),
                    ],
                ),
                ShipPlacement(
                    ship_type=ShipType.CRUISER,
                    coordinates=[
                        Coordinates(row=2, col=0),
                        Coordinates(row=2, col=1),
                        Coordinates(row=2, col=2),
                    ],
                ),
                ShipPlacement(
                    ship_type=ShipType.SUBMARINE,
                    coordinates=[
                        Coordinates(row=3, col=0),
                        Coordinates(row=3, col=1),
                        Coordinates(row=3, col=2),
                    ],
                ),
                ShipPlacement(
                    ship_type=ShipType.DESTROYER,
                    coordinates=[Coordinates(row=4, col=0), Coordinates(row=4, col=1)],
                ),
            ]
        ],
    )

    @model_validator(mode="after")
    def validate_complete_fleet(self) -> "ShipPlacementWrapper":
        """Validate fleet contains exactly one ship of each type.

        Returns:
            ShipPlacementWrapper: Validated fleet.

        Raises:
            ValueError: If fleet is incomplete or has duplicates.
        """
        placements = self.placements
        if not isinstance(placements, list):
            raise ValueError("Placements must be a list")

        # Check ship type completeness
        ship_types = [p.ship_type for p in placements]
        all_ship_types = list(ShipType)

        if len(ship_types) != len(all_ship_types):
            raise ValueError(
                f"Fleet must contain exactly {len(all_ship_types)} ships, got {len(ship_types)}"
            )

        # Find missing ship types
        missing_types = set(all_ship_types) - set(ship_types)
        if missing_types:
            raise ValueError(
                f"Missing ship types: {', '.join(t.value for t in missing_types)}"
            )

        # Find duplicate ship types
        duplicates = [t for t in ship_types if ship_types.count(t) > 1]
        if duplicates:
            raise ValueError(
                f"Duplicate ship types: {', '.join(t.value for t in set(duplicates))}"
            )

        # Check for coordinate overlaps
        all_coords = set()
        for placement in placements:
            placement_coords = {c.to_tuple() for c in placement.coordinates}
            overlap = all_coords.intersection(placement_coords)
            if overlap:
                raise ValueError(f"Ships overlap at coordinates: {overlap}")
            all_coords.update(placement_coords)

        return self


class MoveResult(str, Enum):
    """Possible outcomes of an attack in Battleship.

    Attack results determine game flow, strategic information, and AI
    decision-making. Each result type provides different levels of
    information about the target area and ship status.

    The result system enables sophisticated AI targeting that can learn
    from attack outcomes and adjust strategy accordingly.

    Attributes:
        HIT: Attack successfully damaged a ship.
        MISS: Attack struck empty water.
        SUNK: Attack destroyed the last undamaged section of a ship.
        INVALID: Attack targeted previously attacked coordinates.

    Examples:
        Processing attack results::

            if result == MoveResult.HIT:
                print("Ship damaged! Continue attacking nearby.")
            elif result == MoveResult.SUNK:
                print("Ship destroyed! Search for remaining fleet.")
            elif result == MoveResult.MISS:
                print("Miss. Try different area.")
            elif result == MoveResult.INVALID:
                print("Already attacked this position.")

        AI strategy adjustment::

            if result in [MoveResult.HIT, MoveResult.SUNK]:
                # Add adjacent coordinates to high-priority target list
                priority_targets.extend(get_adjacent_coordinates(attack_coords))

    Note:
        Results guide AI targeting algorithms, with hits triggering
        focused searching and sunk ships enabling area elimination.
    """

    HIT = "hit"  #: Attack damaged a ship
    MISS = "miss"  #: Attack struck empty water
    SUNK = "sunk"  #: Attack destroyed a ship completely
    INVALID = "invalid"  #: Attack targeted already-attacked coordinates


class MoveCommand(BaseModel):
    """Represents an attack command targeting specific coordinates.

    Move commands encapsulate player targeting decisions and provide
    the interface between strategic AI and game execution. Commands
    include validation and conversion utilities for different coordinate systems.

    The command structure supports both human input and AI-generated
    attacks with consistent validation and error handling.

    Attributes:
        row (int): Target row index (0-9).
        col (int): Target column index (0-9).

    Examples:
        Manual targeting::

            attack = MoveCommand(row=5, col=7)
            print(f"Attacking {attack}")  # Attacking (5, 7)

        AI-generated attacks::

            ai_targets = [
                MoveCommand(row=3, col=4),
                MoveCommand(row=3, col=5),
                MoveCommand(row=3, col=6)
            ]

        Coordinate conversion::

            attack = MoveCommand(row=2, col=8)
            coords = attack.to_coordinates()  # Get Coordinates object

    Note:
        Move commands validate target coordinates are within the 10x10
        game board but don't check for previous attacks (handled by board state).
    """

    row: int = Field(
        ...,
        ge=0,
        le=9,
        description="Target row index on the game board (0-9)",
        examples=[0, 3, 5, 7, 9],
    )

    col: int = Field(
        ...,
        ge=0,
        le=9,
        description="Target column index on the game board (0-9)",
        examples=[0, 2, 4, 6, 9],
    )

    def to_coordinates(self) -> Coordinates:
        """Convert move command to Coordinates object.

        Returns:
            Coordinates: Equivalent coordinate representation.

        Examples:
            >>> move = MoveCommand(row=3, col=5)
            >>> coords = move.to_coordinates()
            >>> coords.row, coords.col
            (3, 5)
        """
        return Coordinates(row=self.row, col=self.col)

    def __str__(self) -> str:
        """String representation of the attack command.

        Returns:
            str: Human-readable attack description.

        Examples:
            >>> move = MoveCommand(row=4, col=6)
            >>> str(move)
            "Attack (4, 6)"
        """
        return f"Attack ({self.row}, {self.col})"


class MoveOutcome(BaseModel):
    """Result of an executed attack with detailed outcome information.

    Move outcomes provide complete information about attack results,
    including coordinates, hit status, and ship destruction details.
    This information drives AI learning and strategic adjustment.

    The outcome model supports game state tracking, statistical analysis,
    and strategic decision-making for future moves.

    Attributes:
        row (int): Attacked row coordinate.
        col (int): Attacked column coordinate.
        result (MoveResult): Type of outcome (hit, miss, sunk, invalid).
        sunk_ship (Optional[ShipType]): Type of ship destroyed, if any.

    Examples:
        Successful hit outcome::

            outcome = MoveOutcome(
                row=3, col=5,
                result=MoveResult.HIT
            )

        Ship destruction outcome::

            outcome = MoveOutcome(
                row=7, col=2,
                result=MoveResult.SUNK,
                sunk_ship=ShipType.DESTROYER
            )

        Miss outcome::

            outcome = MoveOutcome(
                row=1, col=9,
                result=MoveResult.MISS
            )

    Note:
        Sunk ship information enables AI to eliminate search areas
        and adjust targeting priorities for remaining fleet.
    """

    row: int = Field(
        ..., ge=0, le=9, description="Row coordinate of the attack", examples=[3, 5, 7]
    )

    col: int = Field(
        ...,
        ge=0,
        le=9,
        description="Column coordinate of the attack",
        examples=[2, 4, 8],
    )

    result: MoveResult = Field(
        ...,
        description="Type of attack outcome",
        examples=[MoveResult.HIT, MoveResult.MISS, MoveResult.SUNK, MoveResult.INVALID],
    )

    sunk_ship: ShipType | None = Field(
        None,
        description="Type of ship destroyed by this attack, if any",
        examples=[ShipType.DESTROYER, ShipType.CRUISER, None],
    )

    @model_validator(mode="after")
    def validate_sunk_ship_consistency(self) -> "MoveOutcome":
        """Validate sunk ship is only specified for SUNK results.

        Returns:
            MoveOutcome: Validated outcome.

        Raises:
            ValueError: If sunk_ship is specified for non-SUNK results.
        """
        if self.result == MoveResult.SUNK and self.sunk_ship is None:
            raise ValueError("SUNK result must specify which ship was sunk")
        if self.result != MoveResult.SUNK and self.sunk_ship is not None:
            raise ValueError("sunk_ship should only be specified for SUNK results")
        return self

    def __str__(self) -> str:
        """String representation of the attack outcome.

        Returns:
            str: Human-readable outcome description.

        Examples:
            >>> outcome = MoveOutcome(row=3, col=5, result=MoveResult.HIT)
            >>> str(outcome)
            "(3, 5): hit"
            >>> outcome = MoveOutcome(row=7, col=2, result=MoveResult.SUNK, sunk_ship=ShipType.DESTROYER)
            >>> str(outcome)
            "(7, 2): sunk - Destroyer sunk!"
        """
        result_str = f"({self.row}, {self.col}): {self.result}"
        if self.sunk_ship:
            result_str += f" - {self.sunk_ship} sunk!"
        return result_str


class Analysis(BaseModel):
    """Strategic analysis of the current Battleship game state.

    Analysis provides AI-generated strategic assessment of board position,
    target priorities, and recommended actions. This enables sophisticated
    decision-making beyond simple random or pattern-based targeting.

    The analysis system considers ship placement probabilities, hit patterns,
    remaining fleet composition, and strategic positioning for optimal play.

    Attributes:
        analysis (str): Detailed strategic assessment text.
        priority_targets (Optional[List[Coordinates]]): High-value coordinates for next attacks.

    Examples:
        Post-hit analysis::

            analysis = Analysis(
                analysis="Hit detected at (5,3). Ship orientation unknown. Target adjacent squares to determine ship alignment and continue attack sequence.",
                priority_targets=[
                    Coordinates(row=4, col=3),  # North
                    Coordinates(row=6, col=3),  # South
                    Coordinates(row=5, col=2),  # West
                    Coordinates(row=5, col=4),  # East
                ]
            )

        Probability-based analysis::

            analysis = Analysis(
                analysis="Three ships remaining: Carrier, Battleship, Submarine. Focus on areas with sufficient space for large ships. Avoid edges where only small ships can fit.",
                priority_targets=[
                    Coordinates(row=2, col=4),
                    Coordinates(row=3, col=6),
                    Coordinates(row=7, col=2)
                ]
            )

        Cleanup analysis::

            analysis = Analysis(
                analysis="Only Destroyer remains (2 squares). Search remaining unexplored areas systematically. Focus on edge positions and corners.",
                priority_targets=[
                    Coordinates(row=0, col=8),
                    Coordinates(row=9, col=1),
                    Coordinates(row=8, col=9)
                ]
            )

    Note:
        Analysis quality directly impacts AI performance. Advanced analysis
        considers ship placement patterns, probability distributions, and
        optimal search strategies.
    """

    analysis: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Detailed strategic assessment of the current game state",
        examples=[
            "Hit detected. Target adjacent squares to find ship orientation.",
            "Large ships likely in center area. Focus on coordinates with sufficient surrounding space.",
            "Final destroyer remains. Systematic search of remaining coordinates recommended.",
        ],
    )

    priority_targets: list[Coordinates] | None = Field(
        default_factory=list,
        max_length=20,
        description="High-priority coordinates for next attacks based on strategic analysis",
        examples=[
            [Coordinates(row=3, col=4), Coordinates(row=3, col=6)],
            [Coordinates(row=5, col=2), Coordinates(row=7, col=8)],
            [],
        ],
    )

    @field_validator("priority_targets")
    @classmethod
    def validate_targets(
        cls, targets: list[Coordinates | dict] | None
    ) -> list[Coordinates]:
        """Validate and normalize priority target list.

        Args:
            targets: List of target coordinates (Coordinates objects or dicts).

        Returns:
            List[Coordinates]: Validated target list.
        """
        if not targets:
            return []

        if not isinstance(targets, list):
            return []

        processed_targets = []
        for t in targets:
            try:
                if isinstance(t, Coordinates):
                    processed_targets.append(t)
                elif isinstance(t, dict):
                    processed_targets.append(Coordinates(**t))
                # Skip invalid targets silently
            except Exception:
                continue

        return processed_targets


class PlayerBoard(BaseModel):
    """Represents a player's complete board state in Battleship.

    The player board manages all game state for one player, including
    ship placement, attack tracking, and game status. This model provides
    the core game logic for move validation, damage assessment, and victory determination.

    The board state enables AI analysis, strategic planning, and game
    progression tracking with comprehensive rule enforcement.

    Attributes:
        ships (List[Ship]): All ships placed on this player's board.
        hits (List[Coordinates]): Successful enemy attacks against this board.
        misses (List[Coordinates]): Failed enemy attacks against this board.
        attacks (List[Coordinates]): All attacks made by this player.
        successful_hits (List[Coordinates]): Successful attacks made by this player.
        failed_attacks (List[Coordinates]): Failed attacks made by this player.
        sunk_ships (List[ShipType]): Ships destroyed on this board.

    Examples:
        Setting up a player board::

            board = PlayerBoard()

            # Place ships
            destroyer_placement = ShipPlacement(
                ship_type=ShipType.DESTROYER,
                coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)]
            )
            board.place_ship(destroyer_placement)

        Processing an attack::

            outcome = board.receive_attack(3, 4)
            if outcome.result == MoveResult.HIT:
                print("Ship damaged!")

        Checking game status::

            if board.all_ships_sunk():
                print("Game over! All ships destroyed.")

    Note:
        Board state is mutable and updates as the game progresses.
        Each attack modifies the appropriate tracking lists.
    """

    ships: list[Ship] = Field(
        default_factory=list,
        max_length=5,
        description="All ships placed on this player's board (maximum 5)",
        examples=[
            [],  # Empty board
            [
                Ship(
                    ship_type=ShipType.DESTROYER,
                    size=2,
                    coordinates=[Coordinates(row=0, col=0), Coordinates(row=0, col=1)],
                )
            ],  # Single destroyer
        ],
    )

    hits: list[Coordinates] = Field(
        default_factory=list,
        description="Coordinates where this board has been successfully attacked",
        examples=[
            [],  # No hits yet
            [Coordinates(row=3, col=4), Coordinates(row=5, col=2)],  # Multiple hits
        ],
    )

    misses: list[Coordinates] = Field(
        default_factory=list,
        description="Coordinates where attacks against this board missed",
        examples=[
            [],  # No misses yet
            [Coordinates(row=1, col=1), Coordinates(row=7, col=8)],  # Multiple misses
        ],
    )

    attacks: list[Coordinates] = Field(
        default_factory=list,
        description="All attacks made by this player (hits and misses combined)",
        examples=[
            [],  # No attacks made
            [Coordinates(row=2, col=3), Coordinates(row=6, col=7)],  # Attack history
        ],
    )

    successful_hits: list[Coordinates] = Field(
        default_factory=list,
        description="Successful attacks made by this player against opponent",
        examples=[
            [],  # No successful hits
            [Coordinates(row=4, col=5), Coordinates(row=4, col=6)],  # Hit sequence
        ],
    )

    failed_attacks: list[Coordinates] = Field(
        default_factory=list,
        description="Failed attacks (misses) made by this player",
        examples=[
            [],  # No failed attacks
            [Coordinates(row=0, col=0), Coordinates(row=9, col=9)],  # Corner misses
        ],
    )

    sunk_ships: list[ShipType] = Field(
        default_factory=list,
        max_length=5,
        description="Types of ships that have been completely destroyed on this board",
        examples=[
            [],  # No ships sunk
            [ShipType.DESTROYER, ShipType.SUBMARINE],  # Two ships destroyed
        ],
    )

    def is_valid_placement(self, placement: ShipPlacement) -> bool:
        """Check if a ship placement is valid on this board.

        Args:
            placement (ShipPlacement): Proposed ship placement.

        Returns:
            bool: True if placement is valid, False otherwise.

        Examples:
            >>> board = PlayerBoard()
            >>> placement = ShipPlacement(ship_type=ShipType.DESTROYER, coordinates=[...])
            >>> if board.is_valid_placement(placement):
            ...     board.place_ship(placement)
        """
        # Check if ship size matches expected size
        expected_size = SHIP_SIZES[placement.ship_type]
        if len(placement.coordinates) != expected_size:
            return False

        # Check if ship type already exists
        existing_types = [ship.ship_type for ship in self.ships]
        if placement.ship_type in existing_types:
            return False

        # Check if ship is in a straight line (validation in ShipPlacement handles this)
        # Check if ship overlaps with existing ships
        proposed_coords = {c.to_tuple() for c in placement.coordinates}
        existing_coords = {
            coord for ship in self.ships for coord in ship.get_occupied_positions()
        }

        return not proposed_coords.intersection(existing_coords)

    def place_ship(self, placement: ShipPlacement) -> bool:
        """Place a ship on the board if placement is valid.

        Args:
            placement (ShipPlacement): Ship placement to execute.

        Returns:
            bool: True if ship was successfully placed, False otherwise.

        Examples:
            >>> board = PlayerBoard()
            >>> placement = ShipPlacement(ship_type=ShipType.CRUISER, coordinates=[...])
            >>> success = board.place_ship(placement)
            >>> print(f"Placement {'successful' if success else 'failed'}")
        """
        if not self.is_valid_placement(placement):
            return False

        ship = Ship(
            ship_type=placement.ship_type,
            size=SHIP_SIZES[placement.ship_type],
            coordinates=placement.coordinates,
        )

        self.ships.append(ship)
        return True

    def receive_attack(self, row: int, col: int) -> MoveOutcome:
        """Process an attack against this board.

        Args:
            row (int): Target row coordinate.
            col (int): Target column coordinate.

        Returns:
            MoveOutcome: Result of the attack with detailed information.

        Examples:
            >>> board = PlayerBoard()
            >>> # ... place ships ...
            >>> outcome = board.receive_attack(3, 4)
            >>> print(f"Attack result: {outcome.result}")
        """
        coord = Coordinates(row=row, col=col)
        coord_tuple = coord.to_tuple()

        # Check if this position has already been attacked
        for hit in self.hits:
            if hit.to_tuple() == coord_tuple:
                return MoveOutcome(row=row, col=col, result=MoveResult.INVALID)

        for miss in self.misses:
            if miss.to_tuple() == coord_tuple:
                return MoveOutcome(row=row, col=col, result=MoveResult.INVALID)

        # Check if the attack hits any ship
        for ship in self.ships:
            for ship_coord in ship.coordinates:
                if ship_coord.to_tuple() == coord_tuple:
                    # Record hit
                    self.hits.append(coord)
                    ship.hits += 1

                    if ship.is_sunk and ship.ship_type not in self.sunk_ships:
                        # Record ship as sunk
                        self.sunk_ships.append(ship.ship_type)
                        return MoveOutcome(
                            row=row,
                            col=col,
                            result=MoveResult.SUNK,
                            sunk_ship=ship.ship_type,
                        )

                    return MoveOutcome(row=row, col=col, result=MoveResult.HIT)

        # No hit, record as miss
        self.misses.append(coord)
        return MoveOutcome(row=row, col=col, result=MoveResult.MISS)

    def all_ships_sunk(self) -> bool:
        """Check if all ships on the board have been destroyed.

        Returns:
            bool: True if all ships are sunk, False otherwise.

        Examples:
            >>> board = PlayerBoard()
            >>> # ... game progression ...
            >>> if board.all_ships_sunk():
            ...     print("Game over!")
        """
        return len(self.ships) > 0 and all(ship.is_sunk for ship in self.ships)

    def get_occupied_positions(self) -> list[tuple[int, int]]:
        """Get all board positions occupied by ships.

        Returns:
            List[Tuple[int, int]]: List of (row, col) coordinates.

        Examples:
            >>> board = PlayerBoard()
            >>> # ... place ships ...
            >>> occupied = board.get_occupied_positions()
            >>> print(f"Ships occupy {len(occupied)} squares")
        """
        return [coord for ship in self.ships for coord in ship.get_occupied_positions()]

    @computed_field
    @property
    def ships_remaining(self) -> int:
        """Count ships that are still afloat.

        Returns:
            int: Number of ships not yet sunk.
        """
        return sum(1 for ship in self.ships if not ship.is_sunk)

    @computed_field
    @property
    def total_ship_squares(self) -> int:
        """Calculate total squares occupied by all ships.

        Returns:
            int: Total ship squares on the board.
        """
        return sum(ship.size for ship in self.ships)

    @computed_field
    @property
    def damage_taken(self) -> int:
        """Calculate total damage (hits) received.

        Returns:
            int: Number of ship squares that have been hit.
        """
        return len(self.hits)


class GamePhase(str, Enum):
    """Current phase of the Battleship game.

    Game phases track progression from initial setup through active
    combat to completion. Phase tracking enables proper game flow
    and determines available actions at each stage.

    Attributes:
        SETUP: Initial ship placement phase.
        PLAYING: Active combat phase with attacks and responses.
        ENDED: Game completion with victory determined.

    Examples:
        Game flow management::

            phase = GamePhase.SETUP
            while phase != GamePhase.ENDED:
                if phase == GamePhase.SETUP:
                    # Handle ship placement
                    phase = GamePhase.PLAYING
                elif phase == GamePhase.PLAYING:
                    # Handle combat turns
                    if game_over_condition():
                        phase = GamePhase.ENDED

    Note:
        Phase transitions are managed by the game controller and
        determine which operations are valid at any given time.
    """

    SETUP = "setup"  #: Ship placement and initial configuration
    PLAYING = "playing"  #: Active combat with attack/response cycles
    ENDED = "ended"  #: Game completion with winner determined
