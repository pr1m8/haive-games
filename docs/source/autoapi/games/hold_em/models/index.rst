games.hold_em.models
====================

.. py:module:: games.hold_em.models

Comprehensive data models for Texas Hold'em poker gameplay.

This module defines the complete set of data structures for Texas Hold'em poker,
providing models for betting actions, hand evaluation, strategic analysis, and
game state management. The implementation supports standard No-Limit Texas Hold'em
rules with comprehensive position and action tracking.

Texas Hold'em is a strategic poker variant involving:
- Two hole cards dealt to each player
- Five community cards dealt in stages (flop, turn, river)
- Multiple betting rounds with strategic decision-making
- Hand ranking system for winner determination
- Position-based strategy and betting patterns

Key Models:
    HandRank: Poker hand strength enumeration
    PokerAction: Available betting actions
    Position: Player seating positions with strategic implications
    HoldEmDecision: Complete player decision with analysis
    HoldEmAnalysis: Strategic position evaluation

.. rubric:: Examples

Working with hand rankings::

    from haive.games.hold_em.models import HandRank

    # Hand strength comparison
    royal_flush = HandRank.ROYAL_FLUSH
    high_card = HandRank.HIGH_CARD
    assert royal_flush.value == "royal_flush"

    # Ranking order (strongest to weakest)
    hand_strength = [
        HandRank.ROYAL_FLUSH,
        HandRank.STRAIGHT_FLUSH,
        HandRank.FOUR_OF_A_KIND,
        HandRank.FULL_HOUSE,
        HandRank.FLUSH,
        HandRank.STRAIGHT,
        HandRank.THREE_OF_A_KIND,
        HandRank.TWO_PAIR,
        HandRank.PAIR,
        HandRank.HIGH_CARD
    ]

Making betting decisions::

    from haive.games.hold_em.models import PokerAction, HoldEmDecision

    # Aggressive betting decision
    decision = HoldEmDecision(
        action=PokerAction.RAISE,
        amount=100,
        reasoning="Strong hand with flush draw",
        confidence=0.85
    )

    # Conservative play
    conservative = HoldEmDecision(
        action=PokerAction.CHECK,
        amount=0,
        reasoning="Weak hand, wait for better spot",
        confidence=0.9
    )

Strategic position analysis::

    from haive.games.hold_em.models import Position, HoldEmAnalysis

    analysis = HoldEmAnalysis(
        position=Position.BUTTON,
        hand_strength=0.75,
        pot_odds=2.5,
        implied_odds=4.0,
        strategic_advice="Raise for value, good position"
    )

The models provide comprehensive support for strategic poker AI development
with proper validation and poker-specific business logic.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">12 classes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive data models for Texas Hold'em poker gameplay.

   This module defines the complete set of data structures for Texas Hold'em poker,
   providing models for betting actions, hand evaluation, strategic analysis, and
   game state management. The implementation supports standard No-Limit Texas Hold'em
   rules with comprehensive position and action tracking.

   Texas Hold'em is a strategic poker variant involving:
   - Two hole cards dealt to each player
   - Five community cards dealt in stages (flop, turn, river)
   - Multiple betting rounds with strategic decision-making
   - Hand ranking system for winner determination
   - Position-based strategy and betting patterns

   Key Models:
       HandRank: Poker hand strength enumeration
       PokerAction: Available betting actions
       Position: Player seating positions with strategic implications
       HoldEmDecision: Complete player decision with analysis
       HoldEmAnalysis: Strategic position evaluation

   .. rubric:: Examples

   Working with hand rankings::

       from haive.games.hold_em.models import HandRank

       # Hand strength comparison
       royal_flush = HandRank.ROYAL_FLUSH
       high_card = HandRank.HIGH_CARD
       assert royal_flush.value == "royal_flush"

       # Ranking order (strongest to weakest)
       hand_strength = [
           HandRank.ROYAL_FLUSH,
           HandRank.STRAIGHT_FLUSH,
           HandRank.FOUR_OF_A_KIND,
           HandRank.FULL_HOUSE,
           HandRank.FLUSH,
           HandRank.STRAIGHT,
           HandRank.THREE_OF_A_KIND,
           HandRank.TWO_PAIR,
           HandRank.PAIR,
           HandRank.HIGH_CARD
       ]

   Making betting decisions::

       from haive.games.hold_em.models import PokerAction, HoldEmDecision

       # Aggressive betting decision
       decision = HoldEmDecision(
           action=PokerAction.RAISE,
           amount=100,
           reasoning="Strong hand with flush draw",
           confidence=0.85
       )

       # Conservative play
       conservative = HoldEmDecision(
           action=PokerAction.CHECK,
           amount=0,
           reasoning="Weak hand, wait for better spot",
           confidence=0.9
       )

   Strategic position analysis::

       from haive.games.hold_em.models import Position, HoldEmAnalysis

       analysis = HoldEmAnalysis(
           position=Position.BUTTON,
           hand_strength=0.75,
           pot_odds=2.5,
           implied_odds=4.0,
           strategic_advice="Raise for value, good position"
       )

   The models provide comprehensive support for strategic poker AI development
   with proper validation and poker-specific business logic.



      
            
            

.. admonition:: Classes (12)
   :class: note

   .. autoapisummary::

      games.hold_em.models.BettingDecision
      games.hold_em.models.GameSituationAnalysis
      games.hold_em.models.HandEvaluation
      games.hold_em.models.HandRank
      games.hold_em.models.OpponentModel
      games.hold_em.models.PlayerDecisionModel
      games.hold_em.models.PokerAction
      games.hold_em.models.PokerAnalysis
      games.hold_em.models.PokerCard
      games.hold_em.models.PokerHandHistory
      games.hold_em.models.Position
      games.hold_em.models.TableDynamics

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BettingDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Structured betting decision.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: aggression_level
               :type:  str
               :value: None



            .. py:attribute:: alternative_action
               :type:  PokerAction | None
               :value: None



            .. py:attribute:: bet_size
               :type:  int
               :value: None



            .. py:attribute:: expected_outcome
               :type:  str
               :value: None



            .. py:attribute:: primary_action
               :type:  PokerAction
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameSituationAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Analysis of the current game situation.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: betting_action
               :type:  str
               :value: None



            .. py:attribute:: game_stage
               :type:  str
               :value: None



            .. py:attribute:: players_in_hand
               :type:  int
               :value: None



            .. py:attribute:: position_description
               :type:  str
               :value: None



            .. py:attribute:: pot_size
               :type:  int
               :value: None



            .. py:attribute:: stack_sizes
               :type:  dict[str, int]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HandEvaluation(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for hand evaluation.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: hand_rank
               :type:  HandRank
               :value: None



            .. py:attribute:: kickers
               :type:  list[str]
               :value: None



            .. py:attribute:: made_hand
               :type:  list[str]
               :value: None



            .. py:attribute:: strength
               :type:  float
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HandRank

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Hand rankings in poker.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: FLUSH
               :value: 'flush'



            .. py:attribute:: FOUR_OF_A_KIND
               :value: 'four_of_a_kind'



            .. py:attribute:: FULL_HOUSE
               :value: 'full_house'



            .. py:attribute:: HIGH_CARD
               :value: 'high_card'



            .. py:attribute:: PAIR
               :value: 'pair'



            .. py:attribute:: ROYAL_FLUSH
               :value: 'royal_flush'



            .. py:attribute:: STRAIGHT
               :value: 'straight'



            .. py:attribute:: STRAIGHT_FLUSH
               :value: 'straight_flush'



            .. py:attribute:: THREE_OF_A_KIND
               :value: 'three_of_a_kind'



            .. py:attribute:: TWO_PAIR
               :value: 'two_pair'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: OpponentModel(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model of an opponent's playing style.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: aggression_factor
               :type:  float
               :value: None



            .. py:attribute:: bluff_frequency
               :type:  float
               :value: None



            .. py:attribute:: fold_to_aggression
               :type:  float
               :value: None



            .. py:attribute:: notes
               :type:  list[str]
               :value: None



            .. py:attribute:: player_id
               :type:  str
               :value: None



            .. py:attribute:: tightness_factor
               :type:  float
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerDecisionModel(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for player decision-making.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_amount(v: int) -> int
               :classmethod:


               Validate bet amount.



            .. py:method:: validate_confidence(v: float) -> float
               :classmethod:


               Validate confidence score.



            .. py:attribute:: action
               :type:  PokerAction
               :value: None



            .. py:attribute:: amount
               :type:  int
               :value: None



            .. py:attribute:: confidence
               :type:  float
               :value: None



            .. py:attribute:: hand_strength_estimate
               :type:  str | None
               :value: None



            .. py:attribute:: reasoning
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerAction

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Possible poker actions.

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

.. py:class:: PokerAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for poker position analysis.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: bluff_potential
               :type:  float
               :value: None



            .. py:attribute:: fold_equity
               :type:  float
               :value: None



            .. py:attribute:: hand_strength
               :type:  float
               :value: None



            .. py:attribute:: opponent_analysis
               :type:  list[str]
               :value: None



            .. py:attribute:: position_advantage
               :type:  str
               :value: None



            .. py:attribute:: pot_odds
               :type:  float
               :value: None



            .. py:attribute:: recommended_actions
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerCard(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for a poker card.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of card.



            .. py:method:: validate_rank(v: str) -> str
               :classmethod:


               Validate card rank.



            .. py:method:: validate_suit(v: str) -> str
               :classmethod:


               Validate card suit.



            .. py:attribute:: rank
               :type:  str
               :value: None



            .. py:attribute:: suit
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerHandHistory(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            History of a completed poker hand.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: actions
               :type:  list[dict[str, Any]]
               :value: None



            .. py:attribute:: final_pot
               :type:  int
               :value: None



            .. py:attribute:: hand_id
               :type:  str
               :value: None



            .. py:attribute:: showdown_cards
               :type:  dict[str, list[str]]
               :value: None



            .. py:attribute:: winner
               :type:  str
               :value: None



            .. py:attribute:: winning_hand
               :type:  HandEvaluation
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Position

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Player positions.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: BIG_BLIND
               :value: 'big_blind'



            .. py:attribute:: BUTTON
               :value: 'button'



            .. py:attribute:: CUTOFF
               :value: 'cutoff'



            .. py:attribute:: LATE_POSITION
               :value: 'late_position'



            .. py:attribute:: MIDDLE_POSITION
               :value: 'middle_position'



            .. py:attribute:: SMALL_BLIND
               :value: 'small_blind'



            .. py:attribute:: UNDER_THE_GUN
               :value: 'under_the_gun'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TableDynamics(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Analysis of table dynamics.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: opportunities
               :type:  list[str]
               :value: None



            .. py:attribute:: player_types
               :type:  dict[str, str]
               :value: None



            .. py:attribute:: recent_action
               :type:  str
               :value: None



            .. py:attribute:: stack_distribution
               :type:  str
               :value: None



            .. py:attribute:: table_image
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.hold_em.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

