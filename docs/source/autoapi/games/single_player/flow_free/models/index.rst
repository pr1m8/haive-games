
:py:mod:`games.single_player.flow_free.models`
==============================================

.. py:module:: games.single_player.flow_free.models

Models for Flow Free gameplay and analysis.

This module defines the core data models for the Flow Free puzzle game, including move
representation and strategic analysis.


.. autolink-examples:: games.single_player.flow_free.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.single_player.flow_free.models.FlowColor
   games.single_player.flow_free.models.FlowFreeAnalysis
   games.single_player.flow_free.models.FlowFreeMove
   games.single_player.flow_free.models.PipeDirection
   games.single_player.flow_free.models.Position


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowColor:

   .. graphviz::
      :align: center

      digraph inheritance_FlowColor {
        node [shape=record];
        "FlowColor" [label="FlowColor"];
        "str" -> "FlowColor";
        "enum.Enum" -> "FlowColor";
      }

.. autoclass:: games.single_player.flow_free.models.FlowColor
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **FlowColor** is an Enum defined in ``games.single_player.flow_free.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowFreeAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_FlowFreeAnalysis {
        node [shape=record];
        "FlowFreeAnalysis" [label="FlowFreeAnalysis"];
        "pydantic.BaseModel" -> "FlowFreeAnalysis";
      }

.. autopydantic_model:: games.single_player.flow_free.models.FlowFreeAnalysis
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

   Inheritance diagram for FlowFreeMove:

   .. graphviz::
      :align: center

      digraph inheritance_FlowFreeMove {
        node [shape=record];
        "FlowFreeMove" [label="FlowFreeMove"];
        "pydantic.BaseModel" -> "FlowFreeMove";
      }

.. autopydantic_model:: games.single_player.flow_free.models.FlowFreeMove
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

   Inheritance diagram for PipeDirection:

   .. graphviz::
      :align: center

      digraph inheritance_PipeDirection {
        node [shape=record];
        "PipeDirection" [label="PipeDirection"];
        "str" -> "PipeDirection";
        "enum.Enum" -> "PipeDirection";
      }

.. autoclass:: games.single_player.flow_free.models.PipeDirection
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PipeDirection** is an Enum defined in ``games.single_player.flow_free.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Position:

   .. graphviz::
      :align: center

      digraph inheritance_Position {
        node [shape=record];
        "Position" [label="Position"];
        "pydantic.BaseModel" -> "Position";
      }

.. autopydantic_model:: games.single_player.flow_free.models.Position
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

.. autolink-examples:: games.single_player.flow_free.models
   :collapse:
   
.. autolink-skip:: next
