games.fox_and_geese.models
==========================

.. py:module:: games.fox_and_geese.models

.. autoapi-nested-parse::

   Comprehensive data models for the Fox and Geese asymmetric strategy game.

   This module defines the complete set of data structures for the classic Fox and Geese
   game, providing models for position tracking, move validation, strategic analysis,
   and game state management. The implementation supports the traditional asymmetric
   gameplay where one fox attempts to capture geese while geese try to trap the fox.

   Fox and Geese is a classic asymmetric strategy game involving:
   - One fox piece that can move and capture in any direction
   - Multiple geese pieces that can only move forward and sideways
   - 7x7 board with specific starting positions
   - Victory conditions: fox captures enough geese OR geese trap the fox
   - Strategic depth through positioning and tactical maneuvering

   Key Models:
       FoxAndGeesePosition: Board coordinate representation with validation
       FoxAndGeeseMove: Complete move description with capture mechanics
       FoxAndGeeseAnalysis: Strategic evaluation for AI decision-making

   .. rubric:: Examples

   Working with positions::

       from haive.games.fox_and_geese.models import FoxAndGeesePosition

       # Create board positions
       fox_start = FoxAndGeesePosition(row=0, col=3)  # Fox starting position
       geese_line = FoxAndGeesePosition(row=6, col=2)  # Geese back line

       # Positions are hashable for set operations
       positions = {fox_start, geese_line}
       print(fox_start)  # "(0, 3)"

   Making moves::

       from haive.games.fox_and_geese.models import FoxAndGeeseMove

       # Fox move with capture
       fox_capture = FoxAndGeeseMove(
           from_pos=FoxAndGeesePosition(row=2, col=2),
           to_pos=FoxAndGeesePosition(row=4, col=4),
           piece_type="fox",
           capture=FoxAndGeesePosition(row=3, col=3)
       )

       # Goose defensive move
       goose_move = FoxAndGeeseMove(
           from_pos=FoxAndGeesePosition(row=5, col=1),
           to_pos=FoxAndGeesePosition(row=4, col=1),
           piece_type="goose"
       )

   Strategic analysis::

       from haive.games.fox_and_geese.models import FoxAndGeeseAnalysis

       analysis = FoxAndGeeseAnalysis(
           advantage="fox",
           advantage_level=7,
           key_features=["fox has breakthrough", "geese scattered"],
           fox_strategy="Push through center, target isolated geese",
           geese_strategy="Regroup and form defensive line",
           critical_squares=["(3,3)", "(4,4)", "(5,5)"],
           explanation="Fox has tactical advantage with open center control"
       )

   The models provide comprehensive support for asymmetric game analysis and
   strategic AI development with proper validation and immutable data structures.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/fox_and_geese/models/FoxAndGeeseAnalysis
   /autoapi/games/fox_and_geese/models/FoxAndGeeseMove
   /autoapi/games/fox_and_geese/models/FoxAndGeesePosition

.. autoapisummary::

   games.fox_and_geese.models.FoxAndGeeseAnalysis
   games.fox_and_geese.models.FoxAndGeeseMove
   games.fox_and_geese.models.FoxAndGeesePosition


