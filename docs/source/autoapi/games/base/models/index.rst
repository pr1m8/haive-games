
:py:mod:`games.base.models`
===========================

.. py:module:: games.base.models

Base models for game agents.

This module provides the foundational data models used across game agents.
It includes models for game state, player state, moves, and other common
game-related data structures.

.. rubric:: Example

>>> board = Board(size=(8, 8))
>>> player = Player(id="p1", name="Player 1")
>>> state = GameState(board=board, players=[player])

Typical usage:
    - Use these models as base classes for game-specific models
    - Inherit from these models to add game-specific functionality


.. autolink-examples:: games.base.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.base.models.Board
   games.base.models.Cell
   games.base.models.GameState
   games.base.models.MoveModel
   games.base.models.Piece
   games.base.models.Player


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Board:

   .. graphviz::
      :align: center

      digraph inheritance_Board {
        node [shape=record];
        "Board" [label="Board"];
        "pydantic.BaseModel" -> "Board";
      }

.. autopydantic_model:: games.base.models.Board
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

   Inheritance diagram for Cell:

   .. graphviz::
      :align: center

      digraph inheritance_Cell {
        node [shape=record];
        "Cell" [label="Cell"];
        "pydantic.BaseModel" -> "Cell";
      }

.. autopydantic_model:: games.base.models.Cell
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

   Inheritance diagram for GameState:

   .. graphviz::
      :align: center

      digraph inheritance_GameState {
        node [shape=record];
        "GameState" [label="GameState"];
        "pydantic.BaseModel" -> "GameState";
      }

.. autopydantic_model:: games.base.models.GameState
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

   Inheritance diagram for MoveModel:

   .. graphviz::
      :align: center

      digraph inheritance_MoveModel {
        node [shape=record];
        "MoveModel" [label="MoveModel"];
        "pydantic.BaseModel" -> "MoveModel";
        "Generic[TMove]" -> "MoveModel";
        "abc.ABC" -> "MoveModel";
      }

.. autopydantic_model:: games.base.models.MoveModel
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

   Inheritance diagram for Piece:

   .. graphviz::
      :align: center

      digraph inheritance_Piece {
        node [shape=record];
        "Piece" [label="Piece"];
        "pydantic.BaseModel" -> "Piece";
      }

.. autopydantic_model:: games.base.models.Piece
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

.. autopydantic_model:: games.base.models.Player
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

.. autolink-examples:: games.base.models
   :collapse:
   
.. autolink-skip:: next
