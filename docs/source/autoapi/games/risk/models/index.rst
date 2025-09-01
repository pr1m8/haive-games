games.risk.models
=================

.. py:module:: games.risk.models

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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/risk/models/Card
   /autoapi/games/risk/models/CardType
   /autoapi/games/risk/models/Continent
   /autoapi/games/risk/models/GameStatus
   /autoapi/games/risk/models/MoveType
   /autoapi/games/risk/models/PhaseType
   /autoapi/games/risk/models/Player
   /autoapi/games/risk/models/RiskAnalysis
   /autoapi/games/risk/models/RiskMove
   /autoapi/games/risk/models/Territory

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


