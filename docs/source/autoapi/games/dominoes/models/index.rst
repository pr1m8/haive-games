
:py:mod:`games.dominoes.models`
===============================

.. py:module:: games.dominoes.models

Comprehensive data models for the Dominoes tile game.

This module defines the complete set of data structures for traditional Dominoes
gameplay, providing models for tile representation, game moves, strategic
analysis, and game state management. The implementation supports standard
double-six dominoes with traditional matching rules.

Dominoes is a classic tile-matching game involving:
- 28 tiles in a double-six set (0-0 through 6-6)
- Line-building with matching endpoints
- Strategic tile placement and blocking
- Point-based scoring systems

Key Models:
    DominoTile: Individual domino tile with two values
    DominoMove: Player's tile placement action
    DominoLinePosition: Position tracking on the domino line
    DominoAnalysis: Strategic evaluation for AI decision-making

.. rubric:: Examples

Working with tiles::

    from haive.games.dominoes.models import DominoTile

    # Create standard tiles
    double_six = DominoTile(left=6, right=6)
    mixed_tile = DominoTile(left=3, right=5)

    # Check tile properties
    assert double_six.is_double() == True
    assert mixed_tile.sum() == 8
    print(double_six)  # "[6|6]"

Making moves::

    from haive.games.dominoes.models import DominoMove

    move = DominoMove(
        tile=DominoTile(left=4, right=2),
        position="left",
        player="player1"
    )

Strategic analysis::

    analysis = DominoAnalysis(
        available_moves=5,
        blocking_potential=3,
        point_value=12,
        strategy="Control high-value tiles"
    )

The models provide comprehensive tile management and strategic gameplay
support for AI-driven dominoes implementation.


.. autolink-examples:: games.dominoes.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.dominoes.models.DominoesAnalysis
   games.dominoes.models.DominoesPlayerDecision
   games.dominoes.models.DominoMove
   games.dominoes.models.DominoTile


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DominoMove:

   .. graphviz::
      :align: center

      digraph inheritance_DominoMove {
        node [shape=record];
        "DominoMove" [label="DominoMove"];
        "pydantic.BaseModel" -> "DominoMove";
      }

.. autopydantic_model:: games.dominoes.models.DominoMove
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

   Inheritance diagram for DominoTile:

   .. graphviz::
      :align: center

      digraph inheritance_DominoTile {
        node [shape=record];
        "DominoTile" [label="DominoTile"];
        "pydantic.BaseModel" -> "DominoTile";
      }

.. autopydantic_model:: games.dominoes.models.DominoTile
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

   Inheritance diagram for DominoesAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_DominoesAnalysis {
        node [shape=record];
        "DominoesAnalysis" [label="DominoesAnalysis"];
        "pydantic.BaseModel" -> "DominoesAnalysis";
      }

.. autopydantic_model:: games.dominoes.models.DominoesAnalysis
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

   Inheritance diagram for DominoesPlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_DominoesPlayerDecision {
        node [shape=record];
        "DominoesPlayerDecision" [label="DominoesPlayerDecision"];
        "pydantic.BaseModel" -> "DominoesPlayerDecision";
      }

.. autopydantic_model:: games.dominoes.models.DominoesPlayerDecision
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

.. autolink-examples:: games.dominoes.models
   :collapse:
   
.. autolink-skip:: next
