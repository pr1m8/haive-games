
:py:mod:`games.checkers.state`
==============================

.. py:module:: games.checkers.state


Classes
-------

.. autoapisummary::

   games.checkers.state.CheckersState
   games.checkers.state.GamePhase
   games.checkers.state.PieceType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CheckersState:

   .. graphviz::
      :align: center

      digraph inheritance_CheckersState {
        node [shape=record];
        "CheckersState" [label="CheckersState"];
        "pydantic.BaseModel" -> "CheckersState";
      }

.. autopydantic_model:: games.checkers.state.CheckersState
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

   Inheritance diagram for GamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_GamePhase {
        node [shape=record];
        "GamePhase" [label="GamePhase"];
        "str" -> "GamePhase";
        "enum.Enum" -> "GamePhase";
      }

.. autoclass:: games.checkers.state.GamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePhase** is an Enum defined in ``games.checkers.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PieceType:

   .. graphviz::
      :align: center

      digraph inheritance_PieceType {
        node [shape=record];
        "PieceType" [label="PieceType"];
        "int" -> "PieceType";
        "enum.Enum" -> "PieceType";
      }

.. autoclass:: games.checkers.state.PieceType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PieceType** is an Enum defined in ``games.checkers.state``.





.. rubric:: Related Links

.. autolink-examples:: games.checkers.state
   :collapse:
   
.. autolink-skip:: next
