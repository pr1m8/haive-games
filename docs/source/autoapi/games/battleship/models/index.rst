
:py:mod:`games.battleship.models`
=================================

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


.. autolink-examples:: games.battleship.models
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Analysis:

   .. graphviz::
      :align: center

      digraph inheritance_Analysis {
        node [shape=record];
        "Analysis" [label="Analysis"];
        "pydantic.BaseModel" -> "Analysis";
      }

.. autopydantic_model:: games.battleship.models.Analysis
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

   Inheritance diagram for Coordinates:

   .. graphviz::
      :align: center

      digraph inheritance_Coordinates {
        node [shape=record];
        "Coordinates" [label="Coordinates"];
        "pydantic.BaseModel" -> "Coordinates";
      }

.. autopydantic_model:: games.battleship.models.Coordinates
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

   Inheritance diagram for GamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_GamePhase {
        node [shape=record];
        "GamePhase" [label="GamePhase"];
        "str" -> "GamePhase";
        "enum.Enum" -> "GamePhase";
      }

.. autoclass:: games.battleship.models.GamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePhase** is an Enum defined in ``games.battleship.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MoveCommand:

   .. graphviz::
      :align: center

      digraph inheritance_MoveCommand {
        node [shape=record];
        "MoveCommand" [label="MoveCommand"];
        "pydantic.BaseModel" -> "MoveCommand";
      }

.. autopydantic_model:: games.battleship.models.MoveCommand
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

   Inheritance diagram for MoveOutcome:

   .. graphviz::
      :align: center

      digraph inheritance_MoveOutcome {
        node [shape=record];
        "MoveOutcome" [label="MoveOutcome"];
        "pydantic.BaseModel" -> "MoveOutcome";
      }

.. autopydantic_model:: games.battleship.models.MoveOutcome
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

   Inheritance diagram for MoveResult:

   .. graphviz::
      :align: center

      digraph inheritance_MoveResult {
        node [shape=record];
        "MoveResult" [label="MoveResult"];
        "str" -> "MoveResult";
        "enum.Enum" -> "MoveResult";
      }

.. autoclass:: games.battleship.models.MoveResult
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MoveResult** is an Enum defined in ``games.battleship.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerBoard:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerBoard {
        node [shape=record];
        "PlayerBoard" [label="PlayerBoard"];
        "pydantic.BaseModel" -> "PlayerBoard";
      }

.. autopydantic_model:: games.battleship.models.PlayerBoard
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

   Inheritance diagram for Ship:

   .. graphviz::
      :align: center

      digraph inheritance_Ship {
        node [shape=record];
        "Ship" [label="Ship"];
        "pydantic.BaseModel" -> "Ship";
      }

.. autopydantic_model:: games.battleship.models.Ship
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

   Inheritance diagram for ShipPlacement:

   .. graphviz::
      :align: center

      digraph inheritance_ShipPlacement {
        node [shape=record];
        "ShipPlacement" [label="ShipPlacement"];
        "pydantic.BaseModel" -> "ShipPlacement";
      }

.. autopydantic_model:: games.battleship.models.ShipPlacement
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

   Inheritance diagram for ShipPlacementWrapper:

   .. graphviz::
      :align: center

      digraph inheritance_ShipPlacementWrapper {
        node [shape=record];
        "ShipPlacementWrapper" [label="ShipPlacementWrapper"];
        "pydantic.BaseModel" -> "ShipPlacementWrapper";
      }

.. autopydantic_model:: games.battleship.models.ShipPlacementWrapper
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

   Inheritance diagram for ShipType:

   .. graphviz::
      :align: center

      digraph inheritance_ShipType {
        node [shape=record];
        "ShipType" [label="ShipType"];
        "str" -> "ShipType";
        "enum.Enum" -> "ShipType";
      }

.. autoclass:: games.battleship.models.ShipType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ShipType** is an Enum defined in ``games.battleship.models``.





.. rubric:: Related Links

.. autolink-examples:: games.battleship.models
   :collapse:
   
.. autolink-skip:: next
