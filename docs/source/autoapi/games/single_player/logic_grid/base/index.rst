
:py:mod:`games.single_player.logic_grid.base`
=============================================

.. py:module:: games.single_player.logic_grid.base


Classes
-------

.. autoapisummary::

   games.single_player.logic_grid.base.ClueType
   games.single_player.logic_grid.base.LogicGrid
   games.single_player.logic_grid.base.LogicGridClue
   games.single_player.logic_grid.base.LogicGridMark
   games.single_player.logic_grid.base.LogicGridMove
   games.single_player.logic_grid.base.LogicGridPosition
   games.single_player.logic_grid.base.LogicGridPuzzle
   games.single_player.logic_grid.base.LogicGridPuzzleDefinition
   games.single_player.logic_grid.base.LogicGridSpace
   games.single_player.logic_grid.base.MarkType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ClueType:

   .. graphviz::
      :align: center

      digraph inheritance_ClueType {
        node [shape=record];
        "ClueType" [label="ClueType"];
        "str" -> "ClueType";
        "enum.Enum" -> "ClueType";
      }

.. autoclass:: games.single_player.logic_grid.base.ClueType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ClueType** is an Enum defined in ``games.single_player.logic_grid.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LogicGrid:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGrid {
        node [shape=record];
        "LogicGrid" [label="LogicGrid"];
        "game_framework_base.Board[LogicGridSpace[LogicGridMark], LogicGridPosition, LogicGridMark]" -> "LogicGrid";
      }

.. autoclass:: games.single_player.logic_grid.base.LogicGrid
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LogicGridClue:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridClue {
        node [shape=record];
        "LogicGridClue" [label="LogicGridClue"];
        "pydantic.BaseModel" -> "LogicGridClue";
      }

.. autopydantic_model:: games.single_player.logic_grid.base.LogicGridClue
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

   Inheritance diagram for LogicGridMark:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridMark {
        node [shape=record];
        "LogicGridMark" [label="LogicGridMark"];
        "game_framework_base.GamePiece[LogicGridPosition]" -> "LogicGridMark";
      }

.. autoclass:: games.single_player.logic_grid.base.LogicGridMark
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LogicGridMove:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridMove {
        node [shape=record];
        "LogicGridMove" [label="LogicGridMove"];
        "pydantic.BaseModel" -> "LogicGridMove";
      }

.. autopydantic_model:: games.single_player.logic_grid.base.LogicGridMove
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

   Inheritance diagram for LogicGridPosition:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridPosition {
        node [shape=record];
        "LogicGridPosition" [label="LogicGridPosition"];
        "game_framework_base.Position" -> "LogicGridPosition";
      }

.. autoclass:: games.single_player.logic_grid.base.LogicGridPosition
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LogicGridPuzzle:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridPuzzle {
        node [shape=record];
        "LogicGridPuzzle" [label="LogicGridPuzzle"];
        "game_framework_base.Game[LogicGridPosition, LogicGridMark]" -> "LogicGridPuzzle";
      }

.. autoclass:: games.single_player.logic_grid.base.LogicGridPuzzle
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for LogicGridPuzzleDefinition:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridPuzzleDefinition {
        node [shape=record];
        "LogicGridPuzzleDefinition" [label="LogicGridPuzzleDefinition"];
        "pydantic.BaseModel" -> "LogicGridPuzzleDefinition";
      }

.. autopydantic_model:: games.single_player.logic_grid.base.LogicGridPuzzleDefinition
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

   Inheritance diagram for LogicGridSpace:

   .. graphviz::
      :align: center

      digraph inheritance_LogicGridSpace {
        node [shape=record];
        "LogicGridSpace" [label="LogicGridSpace"];
        "game_framework_base.Space[LogicGridPosition, LogicGridMark]" -> "LogicGridSpace";
      }

.. autoclass:: games.single_player.logic_grid.base.LogicGridSpace
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MarkType:

   .. graphviz::
      :align: center

      digraph inheritance_MarkType {
        node [shape=record];
        "MarkType" [label="MarkType"];
        "str" -> "MarkType";
        "enum.Enum" -> "MarkType";
      }

.. autoclass:: games.single_player.logic_grid.base.MarkType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **MarkType** is an Enum defined in ``games.single_player.logic_grid.base``.





.. rubric:: Related Links

.. autolink-examples:: games.single_player.logic_grid.base
   :collapse:
   
.. autolink-skip:: next
