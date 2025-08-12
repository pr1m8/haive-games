
:py:mod:`games.tic_tac_toe.models`
==================================

.. py:module:: games.tic_tac_toe.models

Comprehensive data models for strategic Tic Tac Toe gameplay and positional analysis.

This module provides sophisticated data models for the classic game of Tic Tac Toe,
supporting both traditional gameplay and advanced strategic analysis. The models
enable structured data handling throughout the game implementation and provide
strong typing for LLM-based components and strategic decision-making systems.

The models support:
- Complete move representation with coordinate validation
- Strategic analysis with winning/blocking move detection
- Fork opportunity identification for advanced play
- Position evaluation from game theory perspective
- Multi-level strategic recommendations
- Perfect play analysis and minimax integration

.. rubric:: Examples

Basic move representation::

    move = TicTacToeMove(
        row=0,
        col=1,
        player="X"
    )
    print(str(move))  # Output: "X places at (0, 1)"

Strategic position analysis::

    analysis = TicTacToeAnalysis(
        winning_moves=[{"row": 0, "col": 2}],
        blocking_moves=[{"row": 1, "col": 1}],
        fork_opportunities=[],
        center_available=False,
        corner_available=True,
        position_evaluation="winning",
        recommended_move={"row": 0, "col": 2},
        strategy="Win immediately by completing top row"
    )

Fork creation analysis::

    analysis = TicTacToeAnalysis(
        winning_moves=[],
        blocking_moves=[],
        fork_opportunities=[{"row": 0, "col": 0}, {"row": 2, "col": 2}],
        center_available=False,
        corner_available=True,
        position_evaluation="unclear",
        recommended_move={"row": 0, "col": 0},
        strategy="Create fork with two winning threats"
    )

.. note::

   All models use Pydantic for validation and support both JSON serialization
   and integration with LLM-based strategic analysis systems for perfect play.


.. autolink-examples:: games.tic_tac_toe.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.tic_tac_toe.models.TicTacToeAnalysis
   games.tic_tac_toe.models.TicTacToeMove


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TicTacToeAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_TicTacToeAnalysis {
        node [shape=record];
        "TicTacToeAnalysis" [label="TicTacToeAnalysis"];
        "pydantic.BaseModel" -> "TicTacToeAnalysis";
      }

.. autopydantic_model:: games.tic_tac_toe.models.TicTacToeAnalysis
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

   Inheritance diagram for TicTacToeMove:

   .. graphviz::
      :align: center

      digraph inheritance_TicTacToeMove {
        node [shape=record];
        "TicTacToeMove" [label="TicTacToeMove"];
        "pydantic.BaseModel" -> "TicTacToeMove";
      }

.. autopydantic_model:: games.tic_tac_toe.models.TicTacToeMove
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

.. autolink-examples:: games.tic_tac_toe.models
   :collapse:
   
.. autolink-skip:: next
