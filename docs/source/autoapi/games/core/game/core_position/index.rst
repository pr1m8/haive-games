
:py:mod:`games.core.game.core_position`
=======================================

.. py:module:: games.core.game.core_position

Position models for the game framework.

This module defines the base Position class and its specific implementations for
different coordinate systems used in games.


.. autolink-examples:: games.core.game.core_position
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.game.core_position.GridPosition
   games.core.game.core_position.HexPosition
   games.core.game.core_position.PointPosition
   games.core.game.core_position.Position


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GridPosition:

   .. graphviz::
      :align: center

      digraph inheritance_GridPosition {
        node [shape=record];
        "GridPosition" [label="GridPosition"];
        "Position" -> "GridPosition";
      }

.. autoclass:: games.core.game.core_position.GridPosition
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HexPosition:

   .. graphviz::
      :align: center

      digraph inheritance_HexPosition {
        node [shape=record];
        "HexPosition" [label="HexPosition"];
        "Position" -> "HexPosition";
      }

.. autoclass:: games.core.game.core_position.HexPosition
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PointPosition:

   .. graphviz::
      :align: center

      digraph inheritance_PointPosition {
        node [shape=record];
        "PointPosition" [label="PointPosition"];
        "Position" -> "PointPosition";
      }

.. autoclass:: games.core.game.core_position.PointPosition
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Position:

   .. graphviz::
      :align: center

      digraph inheritance_Position {
        node [shape=record];
        "Position" [label="Position"];
        "pydantic.BaseModel" -> "Position";
      }

.. autopydantic_model:: games.core.game.core_position.Position
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

.. autolink-examples:: games.core.game.core_position
   :collapse:
   
.. autolink-skip:: next
