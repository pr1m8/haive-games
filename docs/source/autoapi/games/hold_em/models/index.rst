
:py:mod:`games.hold_em.models`
==============================

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


.. autolink-examples:: games.hold_em.models
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BettingDecision:

   .. graphviz::
      :align: center

      digraph inheritance_BettingDecision {
        node [shape=record];
        "BettingDecision" [label="BettingDecision"];
        "pydantic.BaseModel" -> "BettingDecision";
      }

.. autopydantic_model:: games.hold_em.models.BettingDecision
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameSituationAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_GameSituationAnalysis {
        node [shape=record];
        "GameSituationAnalysis" [label="GameSituationAnalysis"];
        "pydantic.BaseModel" -> "GameSituationAnalysis";
      }

.. autopydantic_model:: games.hold_em.models.GameSituationAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HandEvaluation:

   .. graphviz::
      :align: center

      digraph inheritance_HandEvaluation {
        node [shape=record];
        "HandEvaluation" [label="HandEvaluation"];
        "pydantic.BaseModel" -> "HandEvaluation";
      }

.. autopydantic_model:: games.hold_em.models.HandEvaluation
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HandRank:

   .. graphviz::
      :align: center

      digraph inheritance_HandRank {
        node [shape=record];
        "HandRank" [label="HandRank"];
        "str" -> "HandRank";
        "enum.Enum" -> "HandRank";
      }

.. autoclass:: games.hold_em.models.HandRank
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HandRank** is an Enum defined in ``games.hold_em.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for OpponentModel:

   .. graphviz::
      :align: center

      digraph inheritance_OpponentModel {
        node [shape=record];
        "OpponentModel" [label="OpponentModel"];
        "pydantic.BaseModel" -> "OpponentModel";
      }

.. autopydantic_model:: games.hold_em.models.OpponentModel
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerDecisionModel:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerDecisionModel {
        node [shape=record];
        "PlayerDecisionModel" [label="PlayerDecisionModel"];
        "pydantic.BaseModel" -> "PlayerDecisionModel";
      }

.. autopydantic_model:: games.hold_em.models.PlayerDecisionModel
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerAction:

   .. graphviz::
      :align: center

      digraph inheritance_PokerAction {
        node [shape=record];
        "PokerAction" [label="PokerAction"];
        "str" -> "PokerAction";
        "enum.Enum" -> "PokerAction";
      }

.. autoclass:: games.hold_em.models.PokerAction
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PokerAction** is an Enum defined in ``games.hold_em.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_PokerAnalysis {
        node [shape=record];
        "PokerAnalysis" [label="PokerAnalysis"];
        "pydantic.BaseModel" -> "PokerAnalysis";
      }

.. autopydantic_model:: games.hold_em.models.PokerAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerCard:

   .. graphviz::
      :align: center

      digraph inheritance_PokerCard {
        node [shape=record];
        "PokerCard" [label="PokerCard"];
        "pydantic.BaseModel" -> "PokerCard";
      }

.. autopydantic_model:: games.hold_em.models.PokerCard
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerHandHistory:

   .. graphviz::
      :align: center

      digraph inheritance_PokerHandHistory {
        node [shape=record];
        "PokerHandHistory" [label="PokerHandHistory"];
        "pydantic.BaseModel" -> "PokerHandHistory";
      }

.. autopydantic_model:: games.hold_em.models.PokerHandHistory
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Position:

   .. graphviz::
      :align: center

      digraph inheritance_Position {
        node [shape=record];
        "Position" [label="Position"];
        "str" -> "Position";
        "enum.Enum" -> "Position";
      }

.. autoclass:: games.hold_em.models.Position
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Position** is an Enum defined in ``games.hold_em.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TableDynamics:

   .. graphviz::
      :align: center

      digraph inheritance_TableDynamics {
        node [shape=record];
        "TableDynamics" [label="TableDynamics"];
        "pydantic.BaseModel" -> "TableDynamics";
      }

.. autopydantic_model:: games.hold_em.models.TableDynamics
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: games.hold_em.models
   :collapse:
   
.. autolink-skip:: next
