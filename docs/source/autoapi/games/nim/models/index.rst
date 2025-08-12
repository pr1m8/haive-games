
:py:mod:`games.nim.models`
==========================

.. py:module:: games.nim.models


Classes
-------

.. autoapisummary::

   games.nim.models.NimAnalysis
   games.nim.models.NimMove
   games.nim.models.NimVariant
   games.nim.models.PositionType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for NimAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_NimAnalysis {
        node [shape=record];
        "NimAnalysis" [label="NimAnalysis"];
        "pydantic.BaseModel" -> "NimAnalysis";
      }

.. autopydantic_model:: games.nim.models.NimAnalysis
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

   Inheritance diagram for NimMove:

   .. graphviz::
      :align: center

      digraph inheritance_NimMove {
        node [shape=record];
        "NimMove" [label="NimMove"];
        "pydantic.BaseModel" -> "NimMove";
      }

.. autopydantic_model:: games.nim.models.NimMove
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

   Inheritance diagram for NimVariant:

   .. graphviz::
      :align: center

      digraph inheritance_NimVariant {
        node [shape=record];
        "NimVariant" [label="NimVariant"];
        "str" -> "NimVariant";
        "enum.Enum" -> "NimVariant";
      }

.. autoclass:: games.nim.models.NimVariant
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **NimVariant** is an Enum defined in ``games.nim.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PositionType:

   .. graphviz::
      :align: center

      digraph inheritance_PositionType {
        node [shape=record];
        "PositionType" [label="PositionType"];
        "str" -> "PositionType";
        "enum.Enum" -> "PositionType";
      }

.. autoclass:: games.nim.models.PositionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PositionType** is an Enum defined in ``games.nim.models``.





.. rubric:: Related Links

.. autolink-examples:: games.nim.models
   :collapse:
   
.. autolink-skip:: next
