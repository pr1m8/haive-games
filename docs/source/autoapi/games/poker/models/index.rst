
:py:mod:`games.poker.models`
============================

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


.. autolink-examples:: games.poker.models
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ActionRecord:

   .. graphviz::
      :align: center

      digraph inheritance_ActionRecord {
        node [shape=record];
        "ActionRecord" [label="ActionRecord"];
        "pydantic.BaseModel" -> "ActionRecord";
      }

.. autopydantic_model:: games.poker.models.ActionRecord
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

   Inheritance diagram for AgentDecision:

   .. graphviz::
      :align: center

      digraph inheritance_AgentDecision {
        node [shape=record];
        "AgentDecision" [label="AgentDecision"];
        "pydantic.BaseModel" -> "AgentDecision";
      }

.. autopydantic_model:: games.poker.models.AgentDecision
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

   Inheritance diagram for AgentDecisionSchema:

   .. graphviz::
      :align: center

      digraph inheritance_AgentDecisionSchema {
        node [shape=record];
        "AgentDecisionSchema" [label="AgentDecisionSchema"];
        "pydantic.BaseModel" -> "AgentDecisionSchema";
      }

.. autopydantic_model:: games.poker.models.AgentDecisionSchema
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

   Inheritance diagram for Card:

   .. graphviz::
      :align: center

      digraph inheritance_Card {
        node [shape=record];
        "Card" [label="Card"];
        "pydantic.BaseModel" -> "Card";
      }

.. autopydantic_model:: games.poker.models.Card
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

   Inheritance diagram for CardValue:

   .. graphviz::
      :align: center

      digraph inheritance_CardValue {
        node [shape=record];
        "CardValue" [label="CardValue"];
        "int" -> "CardValue";
        "enum.Enum" -> "CardValue";
      }

.. autoclass:: games.poker.models.CardValue
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CardValue** is an Enum defined in ``games.poker.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_GamePhase {
        node [shape=record];
        "GamePhase" [label="GamePhase"];
        "str" -> "GamePhase";
        "enum.Enum" -> "GamePhase";
      }

.. autoclass:: games.poker.models.GamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePhase** is an Enum defined in ``games.poker.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameResult:

   .. graphviz::
      :align: center

      digraph inheritance_GameResult {
        node [shape=record];
        "GameResult" [label="GameResult"];
        "pydantic.BaseModel" -> "GameResult";
      }

.. autopydantic_model:: games.poker.models.GameResult
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

   Inheritance diagram for Hand:

   .. graphviz::
      :align: center

      digraph inheritance_Hand {
        node [shape=record];
        "Hand" [label="Hand"];
        "pydantic.BaseModel" -> "Hand";
      }

.. autopydantic_model:: games.poker.models.Hand
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
        "int" -> "HandRank";
        "enum.Enum" -> "HandRank";
      }

.. autoclass:: games.poker.models.HandRank
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **HandRank** is an Enum defined in ``games.poker.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HandRanking:

   .. graphviz::
      :align: center

      digraph inheritance_HandRanking {
        node [shape=record];
        "HandRanking" [label="HandRanking"];
        "pydantic.BaseModel" -> "HandRanking";
      }

.. autopydantic_model:: games.poker.models.HandRanking
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

   Inheritance diagram for Player:

   .. graphviz::
      :align: center

      digraph inheritance_Player {
        node [shape=record];
        "Player" [label="Player"];
        "pydantic.BaseModel" -> "Player";
      }

.. autopydantic_model:: games.poker.models.Player
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

   Inheritance diagram for PlayerAction:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerAction {
        node [shape=record];
        "PlayerAction" [label="PlayerAction"];
        "str" -> "PlayerAction";
        "enum.Enum" -> "PlayerAction";
      }

.. autoclass:: games.poker.models.PlayerAction
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerAction** is an Enum defined in ``games.poker.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerObservation:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerObservation {
        node [shape=record];
        "PlayerObservation" [label="PlayerObservation"];
        "pydantic.BaseModel" -> "PlayerObservation";
      }

.. autopydantic_model:: games.poker.models.PlayerObservation
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

   Inheritance diagram for PokerGameState:

   .. graphviz::
      :align: center

      digraph inheritance_PokerGameState {
        node [shape=record];
        "PokerGameState" [label="PokerGameState"];
        "pydantic.BaseModel" -> "PokerGameState";
      }

.. autopydantic_model:: games.poker.models.PokerGameState
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

   Inheritance diagram for Pot:

   .. graphviz::
      :align: center

      digraph inheritance_Pot {
        node [shape=record];
        "Pot" [label="Pot"];
        "pydantic.BaseModel" -> "Pot";
      }

.. autopydantic_model:: games.poker.models.Pot
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

   Inheritance diagram for Suit:

   .. graphviz::
      :align: center

      digraph inheritance_Suit {
        node [shape=record];
        "Suit" [label="Suit"];
        "str" -> "Suit";
        "enum.Enum" -> "Suit";
      }

.. autoclass:: games.poker.models.Suit
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Suit** is an Enum defined in ``games.poker.models``.





.. rubric:: Related Links

.. autolink-examples:: games.poker.models
   :collapse:
   
.. autolink-skip:: next
