
:py:mod:`games.go.models`
=========================

.. py:module:: games.go.models

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


.. autolink-examples:: games.go.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.go.models.GoAnalysis
   games.go.models.GoMoveModel
   games.go.models.GoPlayerDecision


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_GoAnalysis {
        node [shape=record];
        "GoAnalysis" [label="GoAnalysis"];
        "pydantic.BaseModel" -> "GoAnalysis";
      }

.. autopydantic_model:: games.go.models.GoAnalysis
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

   Inheritance diagram for GoMoveModel:

   .. graphviz::
      :align: center

      digraph inheritance_GoMoveModel {
        node [shape=record];
        "GoMoveModel" [label="GoMoveModel"];
        "pydantic.BaseModel" -> "GoMoveModel";
      }

.. autopydantic_model:: games.go.models.GoMoveModel
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

   Inheritance diagram for GoPlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_GoPlayerDecision {
        node [shape=record];
        "GoPlayerDecision" [label="GoPlayerDecision"];
        "pydantic.BaseModel" -> "GoPlayerDecision";
      }

.. autopydantic_model:: games.go.models.GoPlayerDecision
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

.. autolink-examples:: games.go.models
   :collapse:
   
.. autolink-skip:: next
