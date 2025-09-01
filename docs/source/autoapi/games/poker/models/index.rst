games.poker.models
==================

.. py:module:: games.poker.models

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

   .. rubric:: Examples

   >>> from poker.models import Card, Suit, CardValue
   >>>
   >>> # Create a card
   >>> ace_of_spades = Card(suit=Suit.SPADES, value=CardValue.ACE)
   >>> print(ace_of_spades)  # Shows "Ace of spades"



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/poker/models/ActionRecord
   /autoapi/games/poker/models/AgentDecision
   /autoapi/games/poker/models/AgentDecisionSchema
   /autoapi/games/poker/models/Card
   /autoapi/games/poker/models/CardValue
   /autoapi/games/poker/models/GamePhase
   /autoapi/games/poker/models/GameResult
   /autoapi/games/poker/models/Hand
   /autoapi/games/poker/models/HandRank
   /autoapi/games/poker/models/HandRanking
   /autoapi/games/poker/models/Player
   /autoapi/games/poker/models/PlayerAction
   /autoapi/games/poker/models/PlayerObservation
   /autoapi/games/poker/models/PokerGameState
   /autoapi/games/poker/models/Pot
   /autoapi/games/poker/models/Suit

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


