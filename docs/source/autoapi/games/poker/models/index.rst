games.poker.models
==================

.. py:module:: games.poker.models

Core data models for the Poker game implementation.

This module defines the fundamental data structures and models used in the poker game,
including:
    - Card suits and values
    - Hand rankings and game phases
    - Player actions and states
    - Game state tracking
    - Decision models for LLM output

The models use Pydantic for validation and serialization, ensuring type safety
and consistent data structures throughout the game.

.. rubric:: Example

>>> from poker.models import Card, Suit, CardValue
>>>
>>> # Create a card
>>> ace_of_spades = Card(suit=Suit.SPADES, value=CardValue.ACE)
>>> print(ace_of_spades)  # Shows "Ace of spades"



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">16 classes</span>   </div>

.. autoapi-nested-parse::

   Core data models for the Poker game implementation.

   This module defines the fundamental data structures and models used in the poker game,
   including:
       - Card suits and values
       - Hand rankings and game phases
       - Player actions and states
       - Game state tracking
       - Decision models for LLM output

   The models use Pydantic for validation and serialization, ensuring type safety
   and consistent data structures throughout the game.

   .. rubric:: Example

   >>> from poker.models import Card, Suit, CardValue
   >>>
   >>> # Create a card
   >>> ace_of_spades = Card(suit=Suit.SPADES, value=CardValue.ACE)
   >>> print(ace_of_spades)  # Shows "Ace of spades"



      
            
            

.. admonition:: Classes (16)
   :class: note

   .. autoapisummary::

      games.poker.models.ActionRecord
      games.poker.models.AgentDecision
      games.poker.models.AgentDecisionSchema
      games.poker.models.Card
      games.poker.models.CardValue
      games.poker.models.GamePhase
      games.poker.models.GameResult
      games.poker.models.Hand
      games.poker.models.HandRank
      games.poker.models.HandRanking
      games.poker.models.Player
      games.poker.models.PlayerAction
      games.poker.models.PlayerObservation
      games.poker.models.PokerGameState
      games.poker.models.Pot
      games.poker.models.Suit

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ActionRecord(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Record of a player's action.

            Tracks a single action taken by a player during the game,
            including the type of action, amount (if any), and game phase.

            .. attribute:: player_id

               ID of player who took action

               :type: str

            .. attribute:: action

               Type of action taken

               :type: PlayerAction

            .. attribute:: amount

               Chips bet/raised, if applicable

               :type: int

            .. attribute:: phase

               Game phase when action occurred

               :type: GamePhase

            .. rubric:: Example

            >>> record = ActionRecord(
            ...     player_id="p1",
            ...     action=PlayerAction.RAISE,
            ...     amount=100,
            ...     phase=GamePhase.FLOP
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: action
               :type:  PlayerAction
               :value: None



            .. py:attribute:: amount
               :type:  int
               :value: None



            .. py:attribute:: phase
               :type:  GamePhase
               :value: None



            .. py:attribute:: player_id
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AgentDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Agent's decision in the game.

            Represents a decision made by an AI agent, including the action,
            bet amount (if any), and reasoning behind the decision.

            .. attribute:: action

               Chosen action

               :type: PlayerAction

            .. attribute:: amount

               Bet/raise amount if applicable

               :type: int

            .. attribute:: reasoning

               Explanation of decision

               :type: str

            .. rubric:: Example

            >>> decision = AgentDecision(
            ...     action=PlayerAction.RAISE,
            ...     amount=100,
            ...     reasoning="Strong hand, building pot"
            ... )
            >>> print(decision)  # Shows decision details

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__()

               String representation of the decision.



            .. py:attribute:: action
               :type:  PlayerAction
               :value: None



            .. py:attribute:: amount
               :type:  int
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AgentDecisionSchema(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Schema for LLM decision output.

            Defines the expected structure for decisions generated by the language
            model, ensuring consistent and valid output format.

            .. attribute:: action

               Type of action to take

               :type: PlayerAction

            .. attribute:: amount

               Chips to bet/raise

               :type: int

            .. attribute:: reasoning

               Explanation of decision

               :type: str

            .. rubric:: Example

            >>> schema = AgentDecisionSchema(
            ...     action=PlayerAction.CALL,
            ...     amount=50,
            ...     reasoning="Good pot odds with drawing hand"
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: json_schema_extra



            .. py:attribute:: action
               :type:  PlayerAction
               :value: None



            .. py:attribute:: amount
               :type:  int
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Card(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Playing card model.

            Represents a standard playing card with suit and value.
            Provides methods for numeric value comparison.

            .. attribute:: suit

               Card's suit

               :type: Suit

            .. attribute:: value

               Card's value

               :type: CardValue

            .. rubric:: Example

            >>> card = Card(suit=Suit.HEARTS, value=CardValue.ACE)
            >>> print(card)  # Shows "Ace of hearts"
            >>> print(card.numeric_value)  # Shows 14

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the card.



            .. py:property:: numeric_value
               :type: int


               Get numeric value of card (2-14, with Ace being 14).


            .. py:property:: numeric_value_low
               :type: int


               Get numeric value treating Ace as 1.

               Used for A-2-3-4-5 straight calculations.


            .. py:attribute:: suit
               :type:  Suit
               :value: None



            .. py:attribute:: value
               :type:  CardValue
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardValue

            Bases: :py:obj:`int`, :py:obj:`enum.Enum`


            Card value enumeration.

            Represents standard playing card values from 2 to Ace. Inherits from int.Enum
            for numeric comparison (e.g., King > Queen). Ace is highest by default (14)
            but can be treated as 1 in certain contexts (e.g., A-2-3-4-5 straight).

            .. attribute:: TWO

               Value 2

               :type: int

            .. attribute:: THREE

               Value 3

               :type: int

            .. attribute:: ...

               

            .. attribute:: KING

               Value 13

               :type: int

            .. attribute:: ACE

               Value 14 (or 1 in some contexts)

               :type: int

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ACE
               :value: 14



            .. py:attribute:: EIGHT
               :value: 8



            .. py:attribute:: FIVE
               :value: 5



            .. py:attribute:: FOUR
               :value: 4



            .. py:attribute:: JACK
               :value: 11



            .. py:attribute:: KING
               :value: 13



            .. py:attribute:: NINE
               :value: 9



            .. py:attribute:: QUEEN
               :value: 12



            .. py:attribute:: SEVEN
               :value: 7



            .. py:attribute:: SIX
               :value: 6



            .. py:attribute:: TEN
               :value: 10



            .. py:attribute:: THREE
               :value: 3



            .. py:attribute:: TWO
               :value: 2




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Poker game phase enumeration.

            Represents the different phases of a Texas Hold'em poker game.
            Inherits from str.Enum for easy serialization and comparison.

            .. attribute:: SETUP

               Initial game setup

               :type: str

            .. attribute:: PREFLOP

               Before community cards

               :type: str

            .. attribute:: FLOP

               First three community cards

               :type: str

            .. attribute:: TURN

               Fourth community card

               :type: str

            .. attribute:: RIVER

               Fifth community card

               :type: str

            .. attribute:: SHOWDOWN

               Hand comparison

               :type: str

            .. attribute:: GAME_OVER

               Game completed

               :type: str

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: FLOP
               :value: 'flop'



            .. py:attribute:: GAME_OVER
               :value: 'game_over'



            .. py:attribute:: PREFLOP
               :value: 'preflop'



            .. py:attribute:: RIVER
               :value: 'river'



            .. py:attribute:: SETUP
               :value: 'setup'



            .. py:attribute:: SHOWDOWN
               :value: 'showdown'



            .. py:attribute:: TURN
               :value: 'turn'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameResult(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Poker game result record.

            Stores the final outcome of a completed game, including winners,
            chip counts, and hand rankings.

            .. attribute:: winners

               IDs of winning players

               :type: List[str]

            .. attribute:: final_chips

               Final chip counts by player

               :type: Dict[str, int]

            .. attribute:: hand_rankings

               Final hand evaluations

               :type: Dict[str, HandRanking]

            .. attribute:: total_hands_played

               Number of hands completed

               :type: int

            .. rubric:: Example

            >>> result = GameResult(
            ...     winners=["p1"],
            ...     final_chips={"p1": 2000, "p2": 0},
            ...     hand_rankings={"p1": ace_high_flush},
            ...     total_hands_played=1
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: final_chips
               :type:  dict[str, int]
               :value: None



            .. py:attribute:: hand_rankings
               :type:  dict[str, HandRanking]
               :value: None



            .. py:attribute:: total_hands_played
               :type:  int
               :value: None



            .. py:attribute:: winners
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Hand(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Playing hand model.

            Represents a collection of cards held by a player or on the board.
            Limited to 7 cards maximum (2 hole cards + 5 community cards).

            .. attribute:: cards

               List of cards in the hand

               :type: List[Card]

            .. rubric:: Example

            >>> hand = Hand(cards=[
            ...     Card(suit=Suit.HEARTS, value=CardValue.ACE),
            ...     Card(suit=Suit.HEARTS, value=CardValue.KING)
            ... ])
            >>> print(hand)  # Shows "Ace of hearts, King of hearts"

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the hand.



            .. py:attribute:: cards
               :type:  list[Card]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HandRank

            Bases: :py:obj:`int`, :py:obj:`enum.Enum`


            Poker hand ranking enumeration.

            Represents the standard poker hand rankings from high card to royal flush.
            Inherits from int.Enum for easy comparison of hand strengths.

            .. attribute:: HIGH_CARD

               Highest card in hand

               :type: int

            .. attribute:: PAIR

               Two cards of same value

               :type: int

            .. attribute:: TWO_PAIR

               Two different pairs

               :type: int

            .. attribute:: THREE_OF_A_KIND

               Three cards of same value

               :type: int

            .. attribute:: STRAIGHT

               Five sequential cards

               :type: int

            .. attribute:: FLUSH

               Five cards of same suit

               :type: int

            .. attribute:: FULL_HOUSE

               Three of a kind plus a pair

               :type: int

            .. attribute:: FOUR_OF_A_KIND

               Four cards of same value

               :type: int

            .. attribute:: STRAIGHT_FLUSH

               Sequential cards of same suit

               :type: int

            .. attribute:: ROYAL_FLUSH

               A-K-Q-J-10 of same suit

               :type: int

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: FLUSH
               :value: 5



            .. py:attribute:: FOUR_OF_A_KIND
               :value: 7



            .. py:attribute:: FULL_HOUSE
               :value: 6



            .. py:attribute:: HIGH_CARD
               :value: 0



            .. py:attribute:: PAIR
               :value: 1



            .. py:attribute:: ROYAL_FLUSH
               :value: 9



            .. py:attribute:: STRAIGHT
               :value: 4



            .. py:attribute:: STRAIGHT_FLUSH
               :value: 8



            .. py:attribute:: THREE_OF_A_KIND
               :value: 3



            .. py:attribute:: TWO_PAIR
               :value: 2




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HandRanking(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Poker hand ranking result.

            Represents the evaluation of a player's best possible hand,
            including rank, high cards for tiebreakers, and description.

            .. attribute:: player_id

               ID of player whose hand was ranked

               :type: str

            .. attribute:: rank

               Type of hand (pair, flush, etc.)

               :type: HandRank

            .. attribute:: high_cards

               Cards used for tiebreaking

               :type: List[CardValue]

            .. attribute:: description

               Human-readable hand description

               :type: str

            .. rubric:: Example

            >>> ranking = HandRanking(
            ...     player_id="p1",
            ...     rank=HandRank.FLUSH,
            ...     high_cards=[CardValue.ACE, CardValue.KING],
            ...     description="Ace-high flush"
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: high_cards
               :type:  list[CardValue]
               :value: None



            .. py:attribute:: player_id
               :type:  str
               :value: None



            .. py:attribute:: rank
               :type:  HandRank
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Player(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Player model for poker game.

            Represents a player in the game, tracking their cards, chips, and game status.
            Includes betting information and position at the table.

            .. attribute:: id

               Unique identifier for the player

               :type: str

            .. attribute:: name

               Display name of the player

               :type: str

            .. attribute:: chips

               Current chip count, defaults to 1000

               :type: int

            .. attribute:: hand

               Player's hole cards

               :type: Hand

            .. attribute:: is_active

               Whether player is still in current hand

               :type: bool

            .. attribute:: is_all_in

               Whether player has gone all-in

               :type: bool

            .. attribute:: current_bet

               Amount bet in current round

               :type: int

            .. attribute:: total_bet

               Total amount bet in current hand

               :type: int

            .. attribute:: position

               Position at table (0 = dealer)

               :type: int

            .. rubric:: Example

            >>> player = Player(
            ...     id="p1",
            ...     name="Alice",
            ...     chips=1000,
            ...     position=0
            ... )
            >>> print(player)  # Shows "Player Alice ($1000)"

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the player.



            .. py:attribute:: chips
               :type:  int
               :value: None



            .. py:attribute:: current_bet
               :type:  int
               :value: None



            .. py:attribute:: hand
               :type:  Hand
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: is_active
               :type:  bool
               :value: None



            .. py:attribute:: is_all_in
               :type:  bool
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: position
               :type:  int
               :value: None



            .. py:attribute:: total_bet
               :type:  int
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerAction

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Player action enumeration.

            Represents the possible actions a player can take during their turn.
            Inherits from str.Enum for easy serialization and comparison.

            .. attribute:: FOLD

               Give up hand

               :type: str

            .. attribute:: CHECK

               Pass action when no bet to call

               :type: str

            .. attribute:: CALL

               Match current bet

               :type: str

            .. attribute:: BET

               Place initial bet

               :type: str

            .. attribute:: RAISE

               Increase current bet

               :type: str

            .. attribute:: ALL_IN

               Bet all remaining chips

               :type: str

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ALL_IN
               :value: 'all_in'



            .. py:attribute:: BET
               :value: 'bet'



            .. py:attribute:: CALL
               :value: 'call'



            .. py:attribute:: CHECK
               :value: 'check'



            .. py:attribute:: FOLD
               :value: 'fold'



            .. py:attribute:: RAISE
               :value: 'raise'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerObservation(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Player's view of the game state.

            Represents what a specific player can observe about the current game
            state, hiding information they shouldn't have access to (e.g., other
            players' hole cards).

            .. attribute:: player_id

               ID of observing player

               :type: str

            .. attribute:: hand

               Player's hole cards

               :type: Hand

            .. attribute:: chips

               Player's chip count

               :type: int

            .. attribute:: position

               Player's position at table

               :type: int

            .. attribute:: position_name

               Name of position (e.g., "Button")

               :type: str

            .. attribute:: community_cards

               Shared cards on board

               :type: List[Card]

            .. attribute:: visible_players

               Observable player info

               :type: List[Dict[str, Any]]

            .. attribute:: phase

               Current game phase

               :type: GamePhase

            .. attribute:: current_bet

               Amount to call

               :type: int

            .. attribute:: pot_sizes

               Sizes of all pots

               :type: List[int]

            .. attribute:: recent_actions

               Recent action history

               :type: List[ActionRecord]

            .. attribute:: min_raise

               Minimum raise amount

               :type: int

            .. attribute:: is_active

               Whether player is in hand

               :type: bool

            .. attribute:: is_current_player

               Whether it's player's turn

               :type: bool

            .. rubric:: Example

            >>> obs = PlayerObservation(
            ...     player_id="p1",
            ...     hand=Hand(cards=[ace_of_spades, king_of_hearts]),
            ...     position=0,
            ...     position_name="Button"
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: chips
               :type:  int
               :value: None



            .. py:attribute:: community_cards
               :type:  list[Card]
               :value: None



            .. py:attribute:: current_bet
               :type:  int
               :value: None



            .. py:attribute:: hand
               :type:  Hand
               :value: None



            .. py:attribute:: is_active
               :type:  bool
               :value: None



            .. py:attribute:: is_current_player
               :type:  bool
               :value: None



            .. py:attribute:: min_raise
               :type:  int
               :value: None



            .. py:attribute:: phase
               :type:  GamePhase
               :value: None



            .. py:attribute:: player_id
               :type:  str
               :value: None



            .. py:attribute:: position
               :type:  int
               :value: None



            .. py:attribute:: position_name
               :type:  str
               :value: None



            .. py:attribute:: pot_sizes
               :type:  list[int]
               :value: None



            .. py:attribute:: recent_actions
               :type:  list[ActionRecord]
               :value: None



            .. py:attribute:: visible_players
               :type:  list[dict[str, Any]]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerGameState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Texas Hold'em poker game state.

            Comprehensive model of the current game state, including all player
            information, community cards, betting status, and game progression.

            .. attribute:: players

               All players in the game

               :type: List[Player]

            .. attribute:: active_players

               IDs of players still in hand

               :type: List[str]

            .. attribute:: dealer_position

               Position of dealer button

               :type: int

            .. attribute:: current_player_idx

               Index of player to act

               :type: int

            .. attribute:: community_cards

               Shared cards on board

               :type: List[Card]

            .. attribute:: deck

               Remaining cards in deck

               :type: List[Card]

            .. attribute:: phase

               Current game phase

               :type: GamePhase

            .. attribute:: pots

               Main pot and side pots

               :type: List[Pot]

            .. attribute:: current_bet

               Amount to call

               :type: int

            .. attribute:: small_blind

               Small blind amount

               :type: int

            .. attribute:: big_blind

               Big blind amount

               :type: int

            .. attribute:: min_raise

               Minimum raise amount

               :type: int

            .. attribute:: action_history

               Record of all actions

               :type: List[ActionRecord]

            .. attribute:: last_aggressor

               ID of last betting/raising player

               :type: Optional[str]

            .. attribute:: hand_rankings

               Final hand evaluations

               :type: Dict[str, HandRanking]

            .. attribute:: winners

               IDs of hand winners

               :type: List[str]

            .. attribute:: round_complete

               Whether betting round is finished

               :type: bool

            .. rubric:: Example

            >>> state = PokerGameState(
            ...     players=[Player(id="p1", name="Alice")],
            ...     small_blind=5,
            ...     big_blind=10
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: action_history
               :type:  list[ActionRecord]
               :value: None



            .. py:property:: active_player_count
               :type: int


               Get the number of active players in the game.


            .. py:attribute:: active_players
               :type:  list[str]
               :value: None



            .. py:attribute:: big_blind
               :type:  int
               :value: None



            .. py:attribute:: community_cards
               :type:  list[Card]
               :value: None



            .. py:attribute:: current_bet
               :type:  int
               :value: None



            .. py:attribute:: current_player_idx
               :type:  int
               :value: None



            .. py:attribute:: dealer_position
               :type:  int
               :value: None



            .. py:attribute:: deck
               :type:  list[Card]
               :value: None



            .. py:attribute:: hand_rankings
               :type:  dict[str, HandRanking]
               :value: None



            .. py:attribute:: last_aggressor
               :type:  str | None
               :value: None



            .. py:attribute:: min_raise
               :type:  int
               :value: None



            .. py:attribute:: phase
               :type:  GamePhase
               :value: None



            .. py:attribute:: players
               :type:  list[Player]
               :value: None



            .. py:attribute:: pots
               :type:  list[Pot]
               :value: None



            .. py:attribute:: round_complete
               :type:  bool
               :value: None



            .. py:attribute:: small_blind
               :type:  int
               :value: None



            .. py:attribute:: winners
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Pot(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Poker pot model.

            Represents a pot of chips in the game, tracking both the amount
            and which players are eligible to win it (for side pots).

            .. attribute:: amount

               Total chips in the pot

               :type: int

            .. attribute:: eligible_players

               IDs of players who can win

               :type: List[str]

            .. rubric:: Example

            >>> pot = Pot(
            ...     amount=500,
            ...     eligible_players=["p1", "p2", "p3"]
            ... )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: amount
               :type:  int
               :value: None



            .. py:attribute:: eligible_players
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Suit

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Card suit enumeration.

            Represents the four standard playing card suits. Inherits from str.Enum
            for easy serialization and string comparison.

            .. attribute:: HEARTS

               Hearts suit

               :type: str

            .. attribute:: DIAMONDS

               Diamonds suit

               :type: str

            .. attribute:: CLUBS

               Clubs suit

               :type: str

            .. attribute:: SPADES

               Spades suit

               :type: str

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CLUBS
               :value: 'clubs'



            .. py:attribute:: DIAMONDS
               :value: 'diamonds'



            .. py:attribute:: HEARTS
               :value: 'hearts'



            .. py:attribute:: SPADES
               :value: 'spades'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.poker.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

