games.go.models
===============

.. py:module:: games.go.models

.. autoapi-nested-parse::

   Go game data models.

   This module provides Pydantic models for representing Go game concepts:
       - Move coordinates and validation
       - Player decisions
       - Position analysis and evaluation
       - Territory control tracking

   .. rubric:: Example

   >>> from haive.games.go.models import GoMoveModel, GoAnalysis
   >>>
   >>> # Create and validate a move
   >>> move = GoMoveModel(move=(3, 4), board_size=19)
   >>> move.to_tuple()
   (3, 4)
   >>>
   >>> # Create a position analysis
   >>> analysis = GoAnalysis(
   ...     territory_control={"black": 45, "white": 40},
   ...     strong_positions=[(3, 3), (15, 15)],
   ...     weak_positions=[(0, 0)],
   ...     suggested_strategies=["Strengthen the center group"]
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/go/models/GoAnalysis
   /autoapi/games/go/models/GoMoveModel
   /autoapi/games/go/models/GoPlayerDecision

.. autoapisummary::

   games.go.models.GoAnalysis
   games.go.models.GoMoveModel
   games.go.models.GoPlayerDecision


