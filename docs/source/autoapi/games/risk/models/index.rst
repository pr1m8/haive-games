
:py:mod:`games.risk.models`
===========================

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


.. autolink-examples:: games.risk.models
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Card:

   .. graphviz::
      :align: center

      digraph inheritance_Card {
        node [shape=record];
        "Card" [label="Card"];
        "pydantic.BaseModel" -> "Card";
      }

.. autopydantic_model:: games.risk.models.Card
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

   Inheritance diagram for CardType:

   .. graphviz::
      :align: center

      digraph inheritance_CardType {
        node [shape=record];
        "CardType" [label="CardType"];
        "str" -> "CardType";
        "enum.Enum" -> "CardType";
      }

.. autoclass:: games.risk.models.CardType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CardType** is an Enum defined in ``games.risk.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Continent:

   .. graphviz::
      :align: center

      digraph inheritance_Continent {
        node [shape=record];
        "Continent" [label="Continent"];
        "pydantic.BaseModel" -> "Continent";
      }

.. autopydantic_model:: games.risk.models.Continent
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

   Inheritance diagram for GameStatus:

   .. graphviz::
      :align: center

      digraph inheritance_GameStatus {
        node [shape=record];
        "GameStatus" [label="GameStatus"];
        "str" -> "GameStatus";
        "enum.Enum" -> "GameStatus";
      }

.. autoclass:: games.risk.models.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``games.risk.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MoveType:

   .. graphviz::
      :align: center

      digraph inheritance_MoveType {
        node [shape=record];
        "MoveType" [label="MoveType"];
        "str" -> "MoveType";
        "enum.Enum" -> "MoveType";
      }

.. autoclass:: games.risk.models.MoveType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MoveType** is an Enum defined in ``games.risk.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PhaseType:

   .. graphviz::
      :align: center

      digraph inheritance_PhaseType {
        node [shape=record];
        "PhaseType" [label="PhaseType"];
        "str" -> "PhaseType";
        "enum.Enum" -> "PhaseType";
      }

.. autoclass:: games.risk.models.PhaseType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PhaseType** is an Enum defined in ``games.risk.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Player:

   .. graphviz::
      :align: center

      digraph inheritance_Player {
        node [shape=record];
        "Player" [label="Player"];
        "pydantic.BaseModel" -> "Player";
      }

.. autopydantic_model:: games.risk.models.Player
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

   Inheritance diagram for RiskAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_RiskAnalysis {
        node [shape=record];
        "RiskAnalysis" [label="RiskAnalysis"];
        "pydantic.BaseModel" -> "RiskAnalysis";
      }

.. autopydantic_model:: games.risk.models.RiskAnalysis
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

   Inheritance diagram for RiskMove:

   .. graphviz::
      :align: center

      digraph inheritance_RiskMove {
        node [shape=record];
        "RiskMove" [label="RiskMove"];
        "pydantic.BaseModel" -> "RiskMove";
      }

.. autopydantic_model:: games.risk.models.RiskMove
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

   Inheritance diagram for Territory:

   .. graphviz::
      :align: center

      digraph inheritance_Territory {
        node [shape=record];
        "Territory" [label="Territory"];
        "pydantic.BaseModel" -> "Territory";
      }

.. autopydantic_model:: games.risk.models.Territory
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

.. autolink-examples:: games.risk.models
   :collapse:
   
.. autolink-skip:: next
