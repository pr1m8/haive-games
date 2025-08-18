games.battleship.models
=======================

.. py:module:: games.battleship.models

Pydantic models for Battleship naval strategy game components.

This module defines comprehensive data models for the classic Battleship game,
including ships, coordinates, attacks, board state, and strategic analysis.
All models use Pydantic for validation with extensive documentation and examples.

The Battleship implementation supports classic naval combat gameplay with
AI-powered strategic targeting, ship placement validation, and sophisticated
probability-based attack algorithms.

.. rubric:: Examples

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">11 classes</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Pydantic models for Battleship naval strategy game components.

   This module defines comprehensive data models for the classic Battleship game,
   including ships, coordinates, attacks, board state, and strategic analysis.
   All models use Pydantic for validation with extensive documentation and examples.

   The Battleship implementation supports classic naval combat gameplay with
   AI-powered strategic targeting, ship placement validation, and sophisticated
   probability-based attack algorithms.

   .. rubric:: Examples

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



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.battleship.models.SHIP_SIZES

            
            

.. admonition:: Classes (11)
   :class: note

   .. autoapisummary::

      games.battleship.models.Analysis
      games.battleship.models.Coordinates
      games.battleship.models.GamePhase
      games.battleship.models.MoveCommand
      games.battleship.models.MoveOutcome
      games.battleship.models.MoveResult
      games.battleship.models.PlayerBoard
      games.battleship.models.Ship
      games.battleship.models.ShipPlacement
      games.battleship.models.ShipPlacementWrapper
      games.battleship.models.ShipType

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Analysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Strategic analysis of the current Battleship game state.

            Analysis provides AI-generated strategic assessment of board position,
            target priorities, and recommended actions. This enables sophisticated
            decision-making beyond simple random or pattern-based targeting.

            The analysis system considers ship placement probabilities, hit patterns,
            remaining fleet composition, and strategic positioning for optimal play.

            .. attribute:: analysis

               Detailed strategic assessment text.

               :type: str

            .. attribute:: priority_targets

               High-value coordinates for next attacks.

               :type: Optional[List[Coordinates]]

            .. rubric:: Examples

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

            .. note::

               Analysis quality directly impacts AI performance. Advanced analysis
               considers ship placement patterns, probability distributions, and
               optimal search strategies.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_targets(targets: list[Coordinates | dict] | None) -> list[Coordinates]
               :classmethod:


               Validate and normalize priority target list.

               :param targets: List of target coordinates (Coordinates objects or dicts).

               :returns: Validated target list.
               :rtype: List[Coordinates]



            .. py:attribute:: analysis
               :type:  str
               :value: None



            .. py:attribute:: priority_targets
               :type:  list[Coordinates] | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Coordinates(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a coordinate position on the Battleship game board.

            Coordinates use a standard (row, col) system with 0-based indexing
            for a 10x10 grid. This provides precise targeting for naval combat
            and supports conversion between different coordinate representations.

            The coordinate system enables strategic analysis, pattern recognition,
            and systematic search algorithms for AI targeting systems.

            .. attribute:: row

               Row index from 0-9 (top to bottom).

               :type: int

            .. attribute:: col

               Column index from 0-9 (left to right).

               :type: int

            .. rubric:: Examples

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

            .. note::

               Standard naval notation (A1, B2, etc.) can be converted to/from
               this coordinate system for human-readable game interfaces.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other) -> bool

               Equality comparison for coordinates.

               :param other: Another Coordinates instance or compatible object.

               :returns: True if coordinates are equal.
               :rtype: bool



            .. py:method:: __hash__() -> int

               Hash implementation for set operations and dictionary keys.

               :returns: Hash value based on coordinate tuple.
               :rtype: int



            .. py:method:: __str__() -> str

               String representation of coordinates.

               :returns: Human-readable coordinate description.
               :rtype: str

               .. rubric:: Examples

               >>> coord = Coordinates(row=3, col=5)
               >>> str(coord)
               "(3, 5)"



            .. py:method:: to_tuple() -> tuple[int, int]

               Convert coordinates to tuple representation.

               :returns: (row, col) tuple for easy comparison and hashing.
               :rtype: Tuple[int, int]

               .. rubric:: Examples

               >>> coord = Coordinates(row=3, col=5)
               >>> coord.to_tuple()
               (3, 5)
               >>> coord_set = {coord.to_tuple() for coord in coordinates_list}



            .. py:attribute:: col
               :type:  int
               :value: None



            .. py:property:: is_corner
               :type: bool


               Check if coordinate is in a corner of the board.

               :returns: True if coordinate is at (0,0), (0,9), (9,0), or (9,9).
               :rtype: bool

               .. note::

                  Corner positions have unique strategic properties for ship
                  placement and targeting algorithms.


            .. py:property:: is_edge
               :type: bool


               Check if coordinate is on the edge of the board.

               :returns: True if coordinate is on any board edge.
               :rtype: bool

               .. note::

                  Edge positions limit ship placement options and affect
                  AI search patterns.


            .. py:attribute:: row
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Current phase of the Battleship game.

            Game phases track progression from initial setup through active
            combat to completion. Phase tracking enables proper game flow
            and determines available actions at each stage.

            .. attribute:: SETUP

               Initial ship placement phase.

            .. attribute:: PLAYING

               Active combat phase with attacks and responses.

            .. attribute:: ENDED

               Game completion with victory determined.

            .. rubric:: Examples

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

            .. note::

               Phase transitions are managed by the game controller and
               determine which operations are valid at any given time.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ENDED
               :value: 'ended'



            .. py:attribute:: PLAYING
               :value: 'playing'



            .. py:attribute:: SETUP
               :value: 'setup'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MoveCommand(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents an attack command targeting specific coordinates.

            Move commands encapsulate player targeting decisions and provide
            the interface between strategic AI and game execution. Commands
            include validation and conversion utilities for different coordinate systems.

            The command structure supports both human input and AI-generated
            attacks with consistent validation and error handling.

            .. attribute:: row

               Target row index (0-9).

               :type: int

            .. attribute:: col

               Target column index (0-9).

               :type: int

            .. rubric:: Examples

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

            .. note::

               Move commands validate target coordinates are within the 10x10
               game board but don't check for previous attacks (handled by board state).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the attack command.

               :returns: Human-readable attack description.
               :rtype: str

               .. rubric:: Examples

               >>> move = MoveCommand(row=4, col=6)
               >>> str(move)
               "Attack (4, 6)"



            .. py:method:: to_coordinates() -> Coordinates

               Convert move command to Coordinates object.

               :returns: Equivalent coordinate representation.
               :rtype: Coordinates

               .. rubric:: Examples

               >>> move = MoveCommand(row=3, col=5)
               >>> coords = move.to_coordinates()
               >>> coords.row, coords.col
               (3, 5)



            .. py:attribute:: col
               :type:  int
               :value: None



            .. py:attribute:: row
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MoveOutcome(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Result of an executed attack with detailed outcome information.

            Move outcomes provide complete information about attack results,
            including coordinates, hit status, and ship destruction details.
            This information drives AI learning and strategic adjustment.

            The outcome model supports game state tracking, statistical analysis,
            and strategic decision-making for future moves.

            .. attribute:: row

               Attacked row coordinate.

               :type: int

            .. attribute:: col

               Attacked column coordinate.

               :type: int

            .. attribute:: result

               Type of outcome (hit, miss, sunk, invalid).

               :type: MoveResult

            .. attribute:: sunk_ship

               Type of ship destroyed, if any.

               :type: Optional[ShipType]

            .. rubric:: Examples

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

            .. note::

               Sunk ship information enables AI to eliminate search areas
               and adjust targeting priorities for remaining fleet.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the attack outcome.

               :returns: Human-readable outcome description.
               :rtype: str

               .. rubric:: Examples

               >>> outcome = MoveOutcome(row=3, col=5, result=MoveResult.HIT)
               >>> str(outcome)
               "(3, 5): hit"
               >>> outcome = MoveOutcome(row=7, col=2, result=MoveResult.SUNK, sunk_ship=ShipType.DESTROYER)
               >>> str(outcome)
               "(7, 2): sunk - Destroyer sunk!"



            .. py:method:: validate_sunk_ship_consistency() -> MoveOutcome

               Validate sunk ship is only specified for SUNK results.

               :returns: Validated outcome.
               :rtype: MoveOutcome

               :raises ValueError: If sunk_ship is specified for non-SUNK results.



            .. py:attribute:: col
               :type:  int
               :value: None



            .. py:attribute:: result
               :type:  MoveResult
               :value: None



            .. py:attribute:: row
               :type:  int
               :value: None



            .. py:attribute:: sunk_ship
               :type:  ShipType | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MoveResult

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Possible outcomes of an attack in Battleship.

            Attack results determine game flow, strategic information, and AI
            decision-making. Each result type provides different levels of
            information about the target area and ship status.

            The result system enables sophisticated AI targeting that can learn
            from attack outcomes and adjust strategy accordingly.

            .. attribute:: HIT

               Attack successfully damaged a ship.

            .. attribute:: MISS

               Attack struck empty water.

            .. attribute:: SUNK

               Attack destroyed the last undamaged section of a ship.

            .. attribute:: INVALID

               Attack targeted previously attacked coordinates.

            .. rubric:: Examples

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

            .. note::

               Results guide AI targeting algorithms, with hits triggering
               focused searching and sunk ships enabling area elimination.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: HIT
               :value: 'hit'



            .. py:attribute:: INVALID
               :value: 'invalid'



            .. py:attribute:: MISS
               :value: 'miss'



            .. py:attribute:: SUNK
               :value: 'sunk'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerBoard(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a player's complete board state in Battleship.

            The player board manages all game state for one player, including
            ship placement, attack tracking, and game status. This model provides
            the core game logic for move validation, damage assessment, and victory determination.

            The board state enables AI analysis, strategic planning, and game
            progression tracking with comprehensive rule enforcement.

            .. attribute:: ships

               All ships placed on this player's board.

               :type: List[Ship]

            .. attribute:: hits

               Successful enemy attacks against this board.

               :type: List[Coordinates]

            .. attribute:: misses

               Failed enemy attacks against this board.

               :type: List[Coordinates]

            .. attribute:: attacks

               All attacks made by this player.

               :type: List[Coordinates]

            .. attribute:: successful_hits

               Successful attacks made by this player.

               :type: List[Coordinates]

            .. attribute:: failed_attacks

               Failed attacks made by this player.

               :type: List[Coordinates]

            .. attribute:: sunk_ships

               Ships destroyed on this board.

               :type: List[ShipType]

            .. rubric:: Examples

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

            .. note::

               Board state is mutable and updates as the game progresses.
               Each attack modifies the appropriate tracking lists.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: all_ships_sunk() -> bool

               Check if all ships on the board have been destroyed.

               :returns: True if all ships are sunk, False otherwise.
               :rtype: bool

               .. rubric:: Examples

               >>> board = PlayerBoard()
               >>> # ... game progression ...
               >>> if board.all_ships_sunk():
               ...     print("Game over!")



            .. py:method:: get_occupied_positions() -> list[tuple[int, int]]

               Get all board positions occupied by ships.

               :returns: List of (row, col) coordinates.
               :rtype: List[Tuple[int, int]]

               .. rubric:: Examples

               >>> board = PlayerBoard()
               >>> # ... place ships ...
               >>> occupied = board.get_occupied_positions()
               >>> print(f"Ships occupy {len(occupied)} squares")



            .. py:method:: is_valid_placement(placement: ShipPlacement) -> bool

               Check if a ship placement is valid on this board.

               :param placement: Proposed ship placement.
               :type placement: ShipPlacement

               :returns: True if placement is valid, False otherwise.
               :rtype: bool

               .. rubric:: Examples

               >>> board = PlayerBoard()
               >>> placement = ShipPlacement(ship_type=ShipType.DESTROYER, coordinates=[...])
               >>> if board.is_valid_placement(placement):
               ...     board.place_ship(placement)



            .. py:method:: place_ship(placement: ShipPlacement) -> bool

               Place a ship on the board if placement is valid.

               :param placement: Ship placement to execute.
               :type placement: ShipPlacement

               :returns: True if ship was successfully placed, False otherwise.
               :rtype: bool

               .. rubric:: Examples

               >>> board = PlayerBoard()
               >>> placement = ShipPlacement(ship_type=ShipType.CRUISER, coordinates=[...])
               >>> success = board.place_ship(placement)
               >>> print(f"Placement {'successful' if success else 'failed'}")



            .. py:method:: receive_attack(row: int, col: int) -> MoveOutcome

               Process an attack against this board.

               :param row: Target row coordinate.
               :type row: int
               :param col: Target column coordinate.
               :type col: int

               :returns: Result of the attack with detailed information.
               :rtype: MoveOutcome

               .. rubric:: Examples

               >>> board = PlayerBoard()
               >>> # ... place ships ...
               >>> outcome = board.receive_attack(3, 4)
               >>> print(f"Attack result: {outcome.result}")



            .. py:attribute:: attacks
               :type:  list[Coordinates]
               :value: None



            .. py:property:: damage_taken
               :type: int


               Calculate total damage (hits) received.

               :returns: Number of ship squares that have been hit.
               :rtype: int


            .. py:attribute:: failed_attacks
               :type:  list[Coordinates]
               :value: None



            .. py:attribute:: hits
               :type:  list[Coordinates]
               :value: None



            .. py:attribute:: misses
               :type:  list[Coordinates]
               :value: None



            .. py:attribute:: ships
               :type:  list[Ship]
               :value: None



            .. py:property:: ships_remaining
               :type: int


               Count ships that are still afloat.

               :returns: Number of ships not yet sunk.
               :rtype: int


            .. py:attribute:: successful_hits
               :type:  list[Coordinates]
               :value: None



            .. py:attribute:: sunk_ships
               :type:  list[ShipType]
               :value: None



            .. py:property:: total_ship_squares
               :type: int


               Calculate total squares occupied by all ships.

               :returns: Total ship squares on the board.
               :rtype: int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Ship(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a naval vessel on the Battleship game board.

            Ships are the primary game entities, each with a specific type, size,
            position, and damage state. Ship management includes placement validation,
            hit tracking, and sunk status determination.

            The ship model supports sophisticated damage tracking and strategic
            analysis for AI decision-making, including damage assessment and
            targeting priority calculations.

            .. attribute:: ship_type

               The class of naval vessel.

               :type: ShipType

            .. attribute:: size

               Number of grid squares occupied by the ship.

               :type: int

            .. attribute:: coordinates

               All positions occupied by the ship.

               :type: List[Coordinates]

            .. attribute:: hits

               Number of successful attacks against this ship.

               :type: int

            .. rubric:: Examples

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

            .. note::

               Ship coordinates must form a straight line (horizontal or vertical)
               and be contiguous. Size must match the ship type's expected size.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the ship.

               :returns: Human-readable ship description.
               :rtype: str

               .. rubric:: Examples

               >>> ship = Ship(ship_type=ShipType.DESTROYER, size=2,
               ...             coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)])
               >>> str(ship)
               "Destroyer (2): ['(3, 4)', '(3, 5)']"



            .. py:method:: get_occupied_positions() -> list[tuple[int, int]]

               Get all board positions occupied by this ship.

               :returns: List of (row, col) tuples.
               :rtype: List[Tuple[int, int]]

               .. rubric:: Examples

               >>> ship = Ship(coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)])
               >>> ship.get_occupied_positions()
               [(3, 4), (3, 5)]



            .. py:method:: validate_ship_consistency() -> Ship

               Validate ship size, coordinates, and type consistency.

               :returns: Validated ship instance.
               :rtype: Ship

               :raises ValueError: If ship configuration is invalid.



            .. py:method:: validate_size_matches_type(v: int, info) -> int
               :classmethod:


               Validate ship size matches the expected size for its type.

               :param v: Ship size to validate.
               :type v: int
               :param info: Validation context with other field values.

               :returns: Validated size.
               :rtype: int

               :raises ValueError: If size doesn't match expected size for ship type.



            .. py:attribute:: coordinates
               :type:  list[Coordinates]
               :value: None



            .. py:property:: damage_percentage
               :type: float


               Calculate percentage of ship that has been damaged.

               :returns: Damage percentage from 0.0 (undamaged) to 1.0 (sunk).
               :rtype: float

               .. rubric:: Examples

               >>> ship = Ship(ship_type=ShipType.CRUISER, size=3, hits=2)
               >>> ship.damage_percentage
               0.6666666666666666


            .. py:attribute:: hits
               :type:  int
               :value: None



            .. py:property:: is_sunk
               :type: bool


               Check if the ship has been completely destroyed.

               :returns: True if hits equal or exceed ship size.
               :rtype: bool

               .. rubric:: Examples

               >>> destroyer = Ship(ship_type=ShipType.DESTROYER, size=2, hits=2)
               >>> destroyer.is_sunk
               True
               >>> carrier = Ship(ship_type=ShipType.CARRIER, size=5, hits=3)
               >>> carrier.is_sunk
               False


            .. py:property:: orientation
               :type: str


               Determine ship orientation on the board.

               :returns: "horizontal", "vertical", or "single" for single-square ships.
               :rtype: str

               .. note:: Orientation affects targeting strategies and probability calculations.


            .. py:attribute:: ship_type
               :type:  ShipType
               :value: None



            .. py:attribute:: size
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ShipPlacement(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a ship placement command for board setup.

            Ship placement defines where a naval vessel will be positioned on
            the game board. This model handles validation of placement rules
            including size requirements, orientation constraints, and overlap prevention.

            The placement system supports both manual positioning and AI-generated
            ship layouts with comprehensive validation for rule compliance.

            .. attribute:: ship_type

               The type of ship being placed.

               :type: ShipType

            .. attribute:: coordinates

               All positions the ship will occupy.

               :type: List[Coordinates]

            .. rubric:: Examples

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

            .. note::

               Placement validation ensures ships don't overlap, stay within
               board boundaries, and maintain proper size and orientation.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the placement.

               :returns: Human-readable placement description.
               :rtype: str

               .. rubric:: Examples

               >>> placement = ShipPlacement(ship_type=ShipType.DESTROYER,
               ...                          coordinates=[Coordinates(row=3, col=4), Coordinates(row=3, col=5)])
               >>> str(placement)
               "Destroyer at ['(3, 4)', '(3, 5)']"



            .. py:method:: validate_coordinates(coords: list[Coordinates | dict]) -> list[Coordinates]
               :classmethod:


               Validate and normalize coordinate list.

               :param coords: List of coordinates (Coordinates objects or dicts).

               :returns: Validated coordinate list.
               :rtype: List[Coordinates]

               :raises ValueError: If coordinates are invalid format.



            .. py:method:: validate_placement_rules() -> ShipPlacement

               Validate ship placement follows game rules.

               :returns: Validated placement.
               :rtype: ShipPlacement

               :raises ValueError: If placement violates game rules.



            .. py:attribute:: coordinates
               :type:  list[Coordinates]
               :value: None



            .. py:attribute:: ship_type
               :type:  ShipType
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ShipPlacementWrapper(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Wrapper for complete fleet placement returned by LLM agents.

            This model validates that a complete, legal fleet has been specified
            with all required ship types and no duplicates or overlaps. Used for
            AI-generated ship arrangements and setup validation.

            The wrapper ensures fleet completeness and provides structured error
            reporting for invalid configurations during automated setup.

            .. attribute:: placements

               Complete list of ship placements for one fleet.

               :type: List[ShipPlacement]

            .. rubric:: Examples

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

            .. note::

               This wrapper enforces that exactly one ship of each type is included
               in the fleet, preventing duplicate or missing ships.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_complete_fleet() -> ShipPlacementWrapper

               Validate fleet contains exactly one ship of each type.

               :returns: Validated fleet.
               :rtype: ShipPlacementWrapper

               :raises ValueError: If fleet is incomplete or has duplicates.



            .. py:attribute:: placements
               :type:  list[ShipPlacement]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ShipType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Naval ship types in Battleship with varying sizes and strategic roles.

            Each ship type represents a different class of naval vessel with unique
            characteristics. Ship variety adds strategic depth through different
            target profiles and placement considerations.

            The traditional Battleship fleet composition balances large, valuable
            targets (carriers, battleships) with smaller, harder-to-find vessels
            (destroyers, submarines).

            .. attribute:: CARRIER

               Largest ship, primary strategic target (5 squares).

            .. attribute:: BATTLESHIP

               Heavy combat vessel, major threat (4 squares).

            .. attribute:: CRUISER

               Balanced warship, versatile platform (3 squares).

            .. attribute:: SUBMARINE

               Stealth vessel, hard to detect (3 squares).

            .. attribute:: DESTROYER

               Fast escort ship, smallest target (2 squares).

            .. rubric:: Examples

            Fleet composition analysis::

                fleet = [ShipType.CARRIER, ShipType.BATTLESHIP, ShipType.CRUISER,
                        ShipType.SUBMARINE, ShipType.DESTROYER]
                total_squares = sum(SHIP_SIZES[ship] for ship in fleet)  # 17 squares

            Strategic targeting priority::

                high_value_targets = [ShipType.CARRIER, ShipType.BATTLESHIP]
                stealth_targets = [ShipType.SUBMARINE]
                quick_targets = [ShipType.DESTROYER]

            .. note::

               Ship types follow traditional naval classifications and provide
               different strategic value in terms of size, placement difficulty,
               and target priority for AI decision-making.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: BATTLESHIP
               :value: 'Battleship'



            .. py:attribute:: CARRIER
               :value: 'Carrier'



            .. py:attribute:: CRUISER
               :value: 'Cruiser'



            .. py:attribute:: DESTROYER
               :value: 'Destroyer'



            .. py:attribute:: SUBMARINE
               :value: 'Submarine'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: SHIP_SIZES
            :type:  dict[ShipType, int]




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.battleship.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

