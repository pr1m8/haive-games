games.base.models
=================

.. py:module:: games.base.models

.. autoapi-nested-parse::

   Base models for game agents.

   This module provides the foundational data models used across game agents.
   It includes models for game state, player state, moves, and other common
   game-related data structures.

   .. rubric:: Examples

   >>> board = Board(size=(8, 8))
   >>> player = Player(id="p1", name="Player 1")
   >>> state = GameState(board=board, players=[player])

   Typical usage:
       - Use these models as base classes for game-specific models
       - Inherit from these models to add game-specific functionality



Attributes
----------

.. autoapisummary::

   games.base.models.TMove


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/base/models/Board
   /autoapi/games/base/models/Cell
   /autoapi/games/base/models/GameState
   /autoapi/games/base/models/MoveModel
   /autoapi/games/base/models/Piece
   /autoapi/games/base/models/Player

.. autoapisummary::

   games.base.models.Board
   games.base.models.Cell
   games.base.models.GameState
   games.base.models.MoveModel
   games.base.models.Piece
   games.base.models.Player


Module Contents
---------------

.. py:data:: TMove

