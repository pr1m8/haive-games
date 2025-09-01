games.reversi.models
====================

.. py:module:: games.reversi.models

.. autoapi-nested-parse::

   Comprehensive data models for Reversi (Othello) strategic board game.

   This module defines the complete set of data structures for the classic Reversi
   game, providing models for move validation, strategic analysis, and board
   position evaluation. The implementation supports standard 8x8 Reversi with
   traditional disc-flipping mechanics.

   Reversi is a strategic board game involving:
   - 8x8 board with alternating black and white disc placement
   - Disc-flipping mechanics with line capture rules
   - Strategic corner and edge control
   - Endgame optimization for maximum disc count

   Key Models:
       Position: Board coordinate representation (row, col)
       ReversiMove: Player's disc placement action
       ReversiAnalysis: Strategic evaluation for AI decision-making

   .. rubric:: Examples

   Working with positions::

       from haive.games.reversi.models import Position

       # Corner positions (strategic)
       corner = Position(row=0, col=0)
       opposite_corner = Position(row=7, col=7)

       # Center positions (opening)
       center = Position(row=3, col=3)
       adjacent = Position(row=4, col=4)

   Making moves::

       from haive.games.reversi.models import ReversiMove

       # Black player opening move
       move = ReversiMove(row=3, col=2, player="B")

       # White player response
       counter_move = ReversiMove(row=2, col=2, player="W")

   Strategic analysis::

       from haive.games.reversi.models import ReversiAnalysis

       analysis = ReversiAnalysis(
           mobility=12,
           stability=8,
           corner_control=2,
           edge_control=5,
           evaluation_score=0.3,
           strategy="Focus on corner control and edge stability"
       )

   The models provide comprehensive strategic analysis capabilities for
   AI-driven Reversi gameplay with position evaluation and move optimization.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/reversi/models/Position
   /autoapi/games/reversi/models/ReversiAnalysis
   /autoapi/games/reversi/models/ReversiMove

.. autoapisummary::

   games.reversi.models.Position
   games.reversi.models.ReversiAnalysis
   games.reversi.models.ReversiMove


