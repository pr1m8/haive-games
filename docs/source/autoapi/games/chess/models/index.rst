
:py:mod:`games.chess.models`
============================

.. py:module:: games.chess.models

Chess game models module.

This module provides data models for the chess game, including:
    - Move representation
    - Player decisions
    - Position analysis
    - Structured output models for LLMs


.. autolink-examples:: games.chess.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.models.ChessAnalysis
   games.chess.models.ChessMoveModel
   games.chess.models.ChessMoveValidation
   games.chess.models.ChessPlayerDecision
   games.chess.models.SegmentedAnalysis


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_ChessAnalysis {
        node [shape=record];
        "ChessAnalysis" [label="ChessAnalysis"];
        "pydantic.BaseModel" -> "ChessAnalysis";
      }

.. autopydantic_model:: games.chess.models.ChessAnalysis
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

   Inheritance diagram for ChessMoveModel:

   .. graphviz::
      :align: center

      digraph inheritance_ChessMoveModel {
        node [shape=record];
        "ChessMoveModel" [label="ChessMoveModel"];
        "pydantic.BaseModel" -> "ChessMoveModel";
      }

.. autopydantic_model:: games.chess.models.ChessMoveModel
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

   Inheritance diagram for ChessMoveValidation:

   .. graphviz::
      :align: center

      digraph inheritance_ChessMoveValidation {
        node [shape=record];
        "ChessMoveValidation" [label="ChessMoveValidation"];
        "pydantic.BaseModel" -> "ChessMoveValidation";
      }

.. autopydantic_model:: games.chess.models.ChessMoveValidation
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

   Inheritance diagram for ChessPlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_ChessPlayerDecision {
        node [shape=record];
        "ChessPlayerDecision" [label="ChessPlayerDecision"];
        "pydantic.BaseModel" -> "ChessPlayerDecision";
      }

.. autopydantic_model:: games.chess.models.ChessPlayerDecision
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

   Inheritance diagram for SegmentedAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_SegmentedAnalysis {
        node [shape=record];
        "SegmentedAnalysis" [label="SegmentedAnalysis"];
        "pydantic.BaseModel" -> "SegmentedAnalysis";
      }

.. autopydantic_model:: games.chess.models.SegmentedAnalysis
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

.. autolink-examples:: games.chess.models
   :collapse:
   
.. autolink-skip:: next
