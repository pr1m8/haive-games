games.risk.models
=================

.. py:module:: games.risk.models

Pydantic models for Risk game components.

This module defines comprehensive data models for the Risk strategy game,
including territories, continents, players, cards, moves, and game analysis.
All models use Pydantic for validation with extensive documentation and examples.

The Risk implementation supports classic world domination gameplay with
AI-powered strategic analysis, multi-phase turns, and complex territorial
control mechanics.

.. rubric:: Examples

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">10 classes</span>   </div>

.. autoapi-nested-parse::

   Pydantic models for Risk game components.

   This module defines comprehensive data models for the Risk strategy game,
   including territories, continents, players, cards, moves, and game analysis.
   All models use Pydantic for validation with extensive documentation and examples.

   The Risk implementation supports classic world domination gameplay with
   AI-powered strategic analysis, multi-phase turns, and complex territorial
   control mechanics.

   .. rubric:: Examples

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



      
            
            

.. admonition:: Classes (10)
   :class: note

   .. autoapisummary::

      games.risk.models.Card
      games.risk.models.CardType
      games.risk.models.Continent
      games.risk.models.GameStatus
      games.risk.models.MoveType
      games.risk.models.PhaseType
      games.risk.models.Player
      games.risk.models.RiskAnalysis
      games.risk.models.RiskMove
      games.risk.models.Territory

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Card(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A Risk card that can be traded for army reinforcements.

            Risk cards are earned by conquering at least one territory per turn
            and can be accumulated and traded in strategic sets for additional
            armies. Each card typically shows a territory and has a unit type.

            The card system adds strategic depth by encouraging aggressive play
            (to earn cards) while providing timing decisions about when to trade
            for maximum advantage.

            .. attribute:: card_type

               The military unit type shown on the card.

               :type: CardType

            .. attribute:: territory_name

               Territory depicted on the card, if any.

               :type: Optional[str]

            .. rubric:: Examples

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

            .. note::

               Territory names on cards are typically for thematic purposes
               and don't affect trading value, but may provide strategic
               information about board state.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the card.

               :returns: Human-readable card description.
               :rtype: str

               .. rubric:: Examples

               >>> card = Card(card_type=CardType.INFANTRY, territory_name="Alaska")
               >>> str(card)
               "Infantry (Alaska)"
               >>> card = Card(card_type=CardType.WILD)
               >>> str(card)
               "Wild"



            .. py:attribute:: card_type
               :type:  CardType
               :value: None



            .. py:property:: is_wild
               :type: bool


               Check if this is a wild card.

               :returns: True if this is a wild card that can substitute for any type.
               :rtype: bool

               .. rubric:: Examples

               >>> wild_card = Card(card_type=CardType.WILD)
               >>> wild_card.is_wild
               True
               >>> infantry_card = Card(card_type=CardType.INFANTRY)
               >>> infantry_card.is_wild
               False


            .. py:attribute:: territory_name
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of Risk cards for army reinforcement trading.

            Risk cards are collected by conquering territories and can be traded
            in sets for additional armies. The four card types correspond to
            different military units and provide strategic options for players.

            .. attribute:: INFANTRY

               Basic ground unit card, most common type.

            .. attribute:: CAVALRY

               Mobile unit card, medium rarity.

            .. attribute:: ARTILLERY

               Heavy weapon card, provides firepower bonus.

            .. attribute:: WILD

               Special card that can substitute for any other type.

            .. rubric:: Examples

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

            .. note::

               Card trading values typically increase each time cards are traded,
               starting at 4 armies for the first trade and increasing by 2 each time.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ARTILLERY
               :value: 'artillery'



            .. py:attribute:: CAVALRY
               :value: 'cavalry'



            .. py:attribute:: INFANTRY
               :value: 'infantry'



            .. py:attribute:: WILD
               :value: 'wild'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Continent(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A continent grouping of territories with bonus reinforcements.

            Continents provide structure to the Risk board and offer strategic
            objectives. Players who control all territories in a continent
            receive bonus armies each turn, creating natural strategic goals.

            Continental control is often the key to victory in Risk, as the
            bonus armies compound over time and provide significant advantages
            in the lengthy conquest campaigns.

            .. attribute:: name

               The name of the continent.

               :type: str

            .. attribute:: bonus

               Bonus armies awarded for complete continental control.

               :type: int

            .. attribute:: territories

               Names of all territories in this continent.

               :type: List[str]

            .. rubric:: Examples

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

            .. note::

               Continent bonuses create risk-reward tradeoffs. Larger continents
               offer bigger bonuses but are harder to conquer and defend.
               Australia is traditionally the easiest to defend but offers
               the smallest bonus.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the continent.

               :returns: Human-readable continent description.
               :rtype: str

               .. rubric:: Examples

               >>> continent = Continent(name="Europe", bonus=5, territories=["..."])
               >>> str(continent)
               "Europe (Bonus: 5)"



            .. py:method:: validate_territories(v: list[str]) -> list[str]
               :classmethod:


               Validate territory list is not empty and contains valid names.

               :param v: Territory names to validate.
               :type v: List[str]

               :returns: Validated territory list.
               :rtype: List[str]

               :raises ValueError: If territory list is empty or contains invalid names.



            .. py:attribute:: bonus
               :type:  int
               :value: None



            .. py:property:: bonus_per_territory
               :type: float


               Calculate bonus armies per territory in this continent.

               :returns: Bonus efficiency ratio for strategic evaluation.
               :rtype: float

               .. note::

                  Higher ratios indicate more efficient continents to control.
                  Australia typically has the highest ratio (0.5), while
                  Asia has a lower ratio (0.58) despite its large bonus.


            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: territories
               :type:  list[str]
               :value: None



            .. py:property:: territory_count
               :type: int


               Get the number of territories in this continent.

               :returns: Count of territories in the continent.
               :rtype: int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameStatus

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Overall status of the Risk game.

            Tracks the high-level state of the game to determine whether
            play should continue or if victory conditions have been met.

            .. attribute:: IN_PROGRESS

               Game is actively being played.

            .. attribute:: FINISHED

               Game has ended with a clear victory.

            .. rubric:: Examples

            Active game::

                status = GameStatus.IN_PROGRESS
                # Players continue taking turns

            Completed game::

                status = GameStatus.FINISHED
                # Victory conditions met, declare winner

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: FINISHED
               :value: 'finished'



            .. py:attribute:: IN_PROGRESS
               :value: 'in_progress'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MoveType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of moves available in Risk gameplay.

            Risk turns are structured around specific move types that correspond
            to different phases of play. Each move type has distinct rules,
            timing requirements, and strategic implications.

            The move type system ensures proper game flow and enables the AI
            to understand and plan appropriate actions for each phase.

            .. attribute:: PLACE_ARMIES

               Deploy reinforcement armies to controlled territories.

            .. attribute:: ATTACK

               Launch military attacks against adjacent enemy territories.

            .. attribute:: FORTIFY

               Transfer armies between connected friendly territories.

            .. attribute:: TRADE_CARDS

               Exchange card sets for additional armies.

            .. rubric:: Examples

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

            .. note::

               Move types correspond to Risk's traditional turn structure:
               reinforcement → attack → fortification. Card trading can
               occur at the start if the player has 3+ cards.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ATTACK
               :value: 'attack'



            .. py:attribute:: FORTIFY
               :value: 'fortify'



            .. py:attribute:: PLACE_ARMIES
               :value: 'place_armies'



            .. py:attribute:: TRADE_CARDS
               :value: 'trade_cards'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PhaseType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Game phases in Risk turn structure.

            Risk gameplay follows a structured turn sequence with distinct phases
            that determine available actions and strategic timing. Understanding
            phase transitions is crucial for AI planning and move validation.

            The phase system provides clear game flow while allowing for strategic
            flexibility within each phase's constraints.

            .. attribute:: SETUP

               Initial game setup with territory allocation and army placement.

            .. attribute:: REINFORCE

               Army reinforcement and card trading phase.

            .. attribute:: ATTACK

               Combat phase with territorial conquest attempts.

            .. attribute:: FORTIFY

               End-of-turn army repositioning and consolidation.

            .. attribute:: GAME_OVER

               Game completion with victory conditions met.

            .. rubric:: Examples

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

            .. note::

               Phase enforcement ensures proper Risk rule compliance and
               provides structure for AI decision-making algorithms.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ATTACK
               :value: 'attack'



            .. py:attribute:: FORTIFY
               :value: 'fortify'



            .. py:attribute:: GAME_OVER
               :value: 'game_over'



            .. py:attribute:: REINFORCE
               :value: 'reinforce'



            .. py:attribute:: SETUP
               :value: 'setup'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Player(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A player in the Risk game.

            Players are the strategic decision-makers in Risk, controlling
            territories, managing armies, and executing complex multi-turn
            plans for world domination. Each player maintains their own
            hand of cards and army reserves.

            Player management includes tracking eliminated status, which
            occurs when a player loses all territories, transferring their
            cards to the conquering player and removing them from play.

            .. attribute:: name

               The player's identifier and display name.

               :type: str

            .. attribute:: cards

               Risk cards in the player's hand for trading.

               :type: List[Card]

            .. attribute:: unplaced_armies

               Armies available for placement but not yet deployed.

               :type: int

            .. attribute:: eliminated

               Whether this player has been defeated.

               :type: bool

            .. rubric:: Examples

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

            .. note::

               Card accumulation is crucial for late-game army generation.
               Players must balance aggressive expansion (to earn cards)
               with defensive positioning (to avoid elimination).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the player.

               :returns: Human-readable player description.
               :rtype: str

               .. rubric:: Examples

               >>> player = Player(name="General Patton", unplaced_armies=5,
               ...                cards=[Card(card_type=CardType.INFANTRY)])
               >>> str(player)
               "General Patton (Active, 5 unplaced armies, 1 cards)"



            .. py:method:: validate_unplaced_armies(v: int) -> int
               :classmethod:


               Validate unplaced army count is reasonable.

               :param v: Unplaced army count to validate.
               :type v: int

               :returns: Validated army count.
               :rtype: int

               :raises ValueError: If army count is negative.



            .. py:property:: can_trade_cards
               :type: bool


               Check if player has enough cards to make a trade.

               :returns: True if player has 3+ cards (minimum for trading).
               :rtype: bool

               .. note::

                  Players with 5+ cards must trade at the start of their turn.
                  Trading with exactly 3 cards is optional but often strategic.


            .. py:attribute:: cards
               :type:  list[Card]
               :value: None



            .. py:attribute:: eliminated
               :type:  bool
               :value: None



            .. py:property:: must_trade_cards
               :type: bool


               Check if player is forced to trade cards.

               :returns: True if player has 5+ cards and must trade before placing armies.
               :rtype: bool

               .. note:: This rule prevents card hoarding and maintains game flow.


            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: unplaced_armies
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RiskAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Comprehensive analysis of a player's Risk position.

            Strategic analysis is crucial for AI decision-making in Risk's
            complex, multi-turn gameplay. This model provides structured
            evaluation of territorial control, military strength, and
            strategic positioning.

            The analysis system enables sophisticated AI that can evaluate
            long-term strategic positions beyond immediate tactical moves,
            considering continental bonuses, defensive positioning, and
            overall game progression.

            .. attribute:: player

               The player being analyzed.

               :type: str

            .. attribute:: controlled_continents

               Continents fully controlled by the player.

               :type: List[str]

            .. attribute:: controlled_territories

               Total number of territories owned.

               :type: int

            .. attribute:: total_armies

               Sum of all armies across all territories.

               :type: int

            .. attribute:: position_evaluation

               Overall strategic assessment.

               :type: str

            .. attribute:: recommended_move

               Suggested optimal move.

               :type: RiskMove

            .. attribute:: explanation

               Detailed reasoning for the analysis and recommendation.

               :type: str

            .. rubric:: Examples

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

            .. note::

               Analysis quality directly impacts AI performance. Sophisticated
               evaluation considers not just current position but also trajectory,
               opponent threats, and multi-turn strategic opportunities.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the analysis.

               :returns: Comprehensive analysis summary.
               :rtype: str

               .. rubric:: Examples

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



            .. py:method:: validate_position_evaluation(v: str) -> str
               :classmethod:


               Validate position evaluation uses standard terminology.

               :param v: Position evaluation to validate.
               :type v: str

               :returns: Validated evaluation string.
               :rtype: str

               :raises ValueError: If evaluation is not recognized.



            .. py:property:: average_armies_per_territory
               :type: float


               Calculate average army strength per territory.

               :returns: Average armies per territory for strategic assessment.
               :rtype: float

               .. note::

                  Higher ratios indicate stronger defensive positions or
                  preparation for major offensives.


            .. py:property:: continent_bonus
               :type: int


               Calculate total bonus armies from controlled continents.

               :returns: Total bonus armies per turn from continental control.
               :rtype: int

               .. note::

                  This is a simplified calculation. Real implementation would
                  need access to continent definitions with their bonus values.


            .. py:attribute:: controlled_continents
               :type:  list[str]
               :value: None



            .. py:attribute:: controlled_territories
               :type:  int
               :value: None



            .. py:attribute:: explanation
               :type:  str
               :value: None



            .. py:attribute:: player
               :type:  str
               :value: None



            .. py:attribute:: position_evaluation
               :type:  str
               :value: None



            .. py:attribute:: recommended_move
               :type:  RiskMove
               :value: None



            .. py:attribute:: total_armies
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RiskMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A move action in the Risk game.

            Risk moves represent all player actions during gameplay, from army
            placement and attacks to strategic repositioning. Each move contains
            all necessary information for validation and execution.

            The flexible move structure accommodates Risk's varied action types
            while providing clear validation rules and strategic context for
            AI decision-making systems.

            .. attribute:: move_type

               The category of action being performed.

               :type: MoveType

            .. attribute:: player

               The player executing this move.

               :type: str

            .. attribute:: from_territory

               Source territory for attacks and fortifications.

               :type: Optional[str]

            .. attribute:: to_territory

               Target territory for all move types.

               :type: Optional[str]

            .. attribute:: armies

               Number of armies to deploy, attack with, or transfer.

               :type: Optional[int]

            .. attribute:: cards

               Cards to trade for army bonuses.

               :type: Optional[List[Card]]

            .. attribute:: attack_dice

               Number of dice to use in attack (1-3).

               :type: Optional[int]

            .. rubric:: Examples

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

            .. note::

               Move validation depends on game state, including territory
               ownership, army counts, and adjacency relationships.
               Invalid moves should be rejected with clear error messages.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the move.

               :returns: Human-readable move description.
               :rtype: str

               .. rubric:: Examples

               >>> move = RiskMove(move_type=MoveType.ATTACK, player="player_1",
               ...                from_territory="Ukraine", to_territory="Middle East",
               ...                attack_dice=3)
               >>> str(move)
               "player_1 attacks from Ukraine to Middle East with 3 dice"



            .. py:method:: validate_armies(v: int | None) -> int | None
               :classmethod:


               Validate army count is positive if provided.

               :param v: Army count to validate.
               :type v: Optional[int]

               :returns: Validated army count or None.
               :rtype: Optional[int]

               :raises ValueError: If army count is not positive.



            .. py:method:: validate_attack_dice(v: int | None) -> int | None
               :classmethod:


               Validate attack dice count is within valid range.

               :param v: Dice count to validate.
               :type v: Optional[int]

               :returns: Validated dice count or None.
               :rtype: Optional[int]

               :raises ValueError: If dice count is not 1-3.



            .. py:attribute:: armies
               :type:  int | None
               :value: None



            .. py:attribute:: attack_dice
               :type:  int | None
               :value: None



            .. py:attribute:: cards
               :type:  list[Card] | None
               :value: None



            .. py:attribute:: from_territory
               :type:  str | None
               :value: None



            .. py:property:: is_aggressive
               :type: bool


               Determine if this move is aggressive (attack or large army placement).

               :returns: True if move represents aggressive action.
               :rtype: bool

               .. note:: Used for AI personality and strategic analysis.


            .. py:attribute:: move_type
               :type:  MoveType
               :value: None



            .. py:attribute:: player
               :type:  str
               :value: None



            .. py:attribute:: to_territory
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Territory(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A territory on the Risk game board.

            Territories are the fundamental units of control in Risk. Each territory
            belongs to a continent, can be owned by a player, contains armies for
            defense, and connects to adjacent territories for movement and attack.

            The territorial system forms the core of Risk strategy, as players
            must control territories to earn reinforcements and achieve victory
            conditions (total world domination or objective completion).

            .. attribute:: name

               Unique identifier and display name for the territory.

               :type: str

            .. attribute:: continent

               The continent this territory belongs to.

               :type: str

            .. attribute:: owner

               The player who currently controls this territory.

               :type: Optional[str]

            .. attribute:: armies

               Number of armies stationed in this territory for defense.

               :type: int

            .. attribute:: adjacent

               Names of territories that border this one.

               :type: List[str]

            .. rubric:: Examples

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

            .. note::

               Territory adjacency defines the game's strategic geography.
               Control of key chokepoints and continental borders often
               determines game outcomes.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the territory.

               :returns: Human-readable territory description.
               :rtype: str

               .. rubric:: Examples

               >>> territory = Territory(name="Alaska", continent="North America",
               ...                      owner="player_1", armies=3)
               >>> str(territory)
               "Alaska (player_1, 3 armies)"



            .. py:method:: validate_armies(v: int) -> int
               :classmethod:


               Validate army count is reasonable.

               :param v: Army count to validate.
               :type v: int

               :returns: Validated army count.
               :rtype: int

               :raises ValueError: If army count is negative.



            .. py:method:: validate_name(v: str) -> str
               :classmethod:


               Validate territory name is properly formatted.

               :param v: Territory name to validate.
               :type v: str

               :returns: Cleaned and validated territory name.
               :rtype: str

               :raises ValueError: If name is empty or contains invalid characters.



            .. py:attribute:: adjacent
               :type:  list[str]
               :value: None



            .. py:attribute:: armies
               :type:  int
               :value: None



            .. py:attribute:: continent
               :type:  str
               :value: None



            .. py:property:: defense_strength
               :type: int


               Calculate defensive strength of this territory.

               :returns: Maximum dice this territory can roll in defense (1-2).
               :rtype: int

               .. note::

                  Territories with 1 army can defend with 1 die,
                  territories with 2+ armies can defend with 2 dice.


            .. py:property:: is_occupied
               :type: bool


               Check if territory is currently occupied by a player.

               :returns: True if territory has an owner, False if neutral.
               :rtype: bool


            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: owner
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.risk.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

