games.battleship.models
=======================

.. py:module:: games.battleship.models

.. autoapi-nested-parse::

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



Attributes
----------

.. autoapisummary::

   games.battleship.models.SHIP_SIZES


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/battleship/models/Analysis
   /autoapi/games/battleship/models/Coordinates
   /autoapi/games/battleship/models/GamePhase
   /autoapi/games/battleship/models/MoveCommand
   /autoapi/games/battleship/models/MoveOutcome
   /autoapi/games/battleship/models/MoveResult
   /autoapi/games/battleship/models/PlayerBoard
   /autoapi/games/battleship/models/Ship
   /autoapi/games/battleship/models/ShipPlacement
   /autoapi/games/battleship/models/ShipPlacementWrapper
   /autoapi/games/battleship/models/ShipType

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

.. py:data:: SHIP_SIZES
   :type:  dict[ShipType, int]

