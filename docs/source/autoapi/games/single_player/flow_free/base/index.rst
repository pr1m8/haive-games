
:py:mod:`games.single_player.flow_free.base`
============================================

.. py:module:: games.single_player.flow_free.base


Classes
-------

.. autoapisummary::

   games.single_player.flow_free.base.EndpointType
   games.single_player.flow_free.base.FlowBoard
   games.single_player.flow_free.base.FlowEndpoint
   games.single_player.flow_free.base.FlowFreeGame
   games.single_player.flow_free.base.FlowFreeLevel
   games.single_player.flow_free.base.FlowFreeMove
   games.single_player.flow_free.base.FlowGridSpace
   games.single_player.flow_free.base.FlowPiece
   games.single_player.flow_free.base.FlowPipe
   games.single_player.flow_free.base.PipeDirection


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for EndpointType:

   .. graphviz::
      :align: center

      digraph inheritance_EndpointType {
        node [shape=record];
        "EndpointType" [label="EndpointType"];
        "str" -> "EndpointType";
        "enum.Enum" -> "EndpointType";
      }

.. autoclass:: games.single_player.flow_free.base.EndpointType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **EndpointType** is an Enum defined in ``games.single_player.flow_free.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowBoard:

   .. graphviz::
      :align: center

      digraph inheritance_FlowBoard {
        node [shape=record];
        "FlowBoard" [label="FlowBoard"];
        "game_framework_base.GridBoard[FlowGridSpace[FlowPiece], game_framework_base.GridPosition, FlowPiece]" -> "FlowBoard";
      }

.. autoclass:: games.single_player.flow_free.base.FlowBoard
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowEndpoint:

   .. graphviz::
      :align: center

      digraph inheritance_FlowEndpoint {
        node [shape=record];
        "FlowEndpoint" [label="FlowEndpoint"];
        "FlowPiece" -> "FlowEndpoint";
      }

.. autoclass:: games.single_player.flow_free.base.FlowEndpoint
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowFreeGame:

   .. graphviz::
      :align: center

      digraph inheritance_FlowFreeGame {
        node [shape=record];
        "FlowFreeGame" [label="FlowFreeGame"];
        "game_framework_base.Game[game_framework_base.GridPosition, FlowPiece]" -> "FlowFreeGame";
      }

.. autoclass:: games.single_player.flow_free.base.FlowFreeGame
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowFreeLevel:

   .. graphviz::
      :align: center

      digraph inheritance_FlowFreeLevel {
        node [shape=record];
        "FlowFreeLevel" [label="FlowFreeLevel"];
        "pydantic.BaseModel" -> "FlowFreeLevel";
      }

.. autopydantic_model:: games.single_player.flow_free.base.FlowFreeLevel
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

.. autopydantic_model:: games.single_player.flow_free.base.FlowFreeMove
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

   Inheritance diagram for FlowGridSpace:

   .. graphviz::
      :align: center

      digraph inheritance_FlowGridSpace {
        node [shape=record];
        "FlowGridSpace" [label="FlowGridSpace"];
        "game_framework_base.GridSpace[FlowPiece]" -> "FlowGridSpace";
      }

.. autoclass:: games.single_player.flow_free.base.FlowGridSpace
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowPiece:

   .. graphviz::
      :align: center

      digraph inheritance_FlowPiece {
        node [shape=record];
        "FlowPiece" [label="FlowPiece"];
        "game_framework_base.GamePiece[game_framework_base.GridPosition]" -> "FlowPiece";
      }

.. autoclass:: games.single_player.flow_free.base.FlowPiece
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for FlowPipe:

   .. graphviz::
      :align: center

      digraph inheritance_FlowPipe {
        node [shape=record];
        "FlowPipe" [label="FlowPipe"];
        "FlowPiece" -> "FlowPipe";
      }

.. autoclass:: games.single_player.flow_free.base.FlowPipe
   :members:
   :undoc-members:
   :show-inheritance:




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

.. autoclass:: games.single_player.flow_free.base.PipeDirection
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PipeDirection** is an Enum defined in ``games.single_player.flow_free.base``.





.. rubric:: Related Links

.. autolink-examples:: games.single_player.flow_free.base
   :collapse:
   
.. autolink-skip:: next
