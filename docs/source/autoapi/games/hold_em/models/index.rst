games.hold_em.models
====================

.. py:module:: games.hold_em.models

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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/models/BettingDecision
   /autoapi/games/hold_em/models/GameSituationAnalysis
   /autoapi/games/hold_em/models/HandEvaluation
   /autoapi/games/hold_em/models/HandRank
   /autoapi/games/hold_em/models/OpponentModel
   /autoapi/games/hold_em/models/PlayerDecisionModel
   /autoapi/games/hold_em/models/PokerAction
   /autoapi/games/hold_em/models/PokerAnalysis
   /autoapi/games/hold_em/models/PokerCard
   /autoapi/games/hold_em/models/PokerHandHistory
   /autoapi/games/hold_em/models/Position
   /autoapi/games/hold_em/models/TableDynamics

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


