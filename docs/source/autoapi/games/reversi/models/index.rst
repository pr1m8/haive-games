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


   .. autolink-examples:: games.reversi.models
      :collapse:


Classes
-------

.. autoapisummary::

   games.reversi.models.Position
   games.reversi.models.ReversiAnalysis
   games.reversi.models.ReversiMove


Module Contents
---------------

.. py:class:: Position(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A coordinate on the Reversi board.

   .. attribute:: row

      Row index (0-7).

      :type: int

   .. attribute:: col

      Column index (0-7).

      :type: int

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Position
      :collapse:

   .. py:attribute:: col
      :type:  int
      :value: None



   .. py:attribute:: row
      :type:  int
      :value: None



.. py:class:: ReversiAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Strategy and evaluation report for a Reversi position.

   .. attribute:: mobility

      Number of legal moves available.

      :type: int

   .. attribute:: frontier_discs

      Count of discs adjacent to at least one empty space.

      :type: int

   .. attribute:: corner_discs

      Number of corners occupied by the player.

      :type: int

   .. attribute:: stable_discs

      Discs that cannot be flipped.

      :type: int

   .. attribute:: positional_score

      Positional heuristic score.

      :type: int

   .. attribute:: position_evaluation

      Assessment of advantage (e.g., 'winning', 'equal').

      :type: str

   .. attribute:: recommended_moves

      Preferred moves based on analysis.

      :type: List[Position]

   .. attribute:: danger_zones

      High-risk positions to avoid.

      :type: List[Position]

   .. attribute:: strategy

      Summary of strategic approach.

      :type: str

   .. attribute:: reasoning

      Detailed explanation of analysis.

      :type: str

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReversiAnalysis
      :collapse:

   .. py:attribute:: corner_discs
      :type:  int
      :value: None



   .. py:attribute:: danger_zones
      :type:  list[Position]
      :value: None



   .. py:attribute:: frontier_discs
      :type:  int
      :value: None



   .. py:attribute:: mobility
      :type:  int
      :value: None



   .. py:attribute:: position_evaluation
      :type:  Literal['winning', 'losing', 'equal', 'unclear']
      :value: None



   .. py:attribute:: positional_score
      :type:  int
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: recommended_moves
      :type:  list[Position]
      :value: None



   .. py:attribute:: stable_discs
      :type:  int
      :value: None



   .. py:attribute:: strategy
      :type:  str
      :value: None



.. py:class:: ReversiMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a single Reversi move.

   .. attribute:: row

      Row position of the move (0-7).

      :type: int

   .. attribute:: col

      Column position of the move (0-7).

      :type: int

   .. attribute:: player

      The player making the move ('B' or 'W').

      :type: str

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ReversiMove
      :collapse:

   .. py:method:: __str__() -> str


   .. py:attribute:: col
      :type:  int
      :value: None



   .. py:attribute:: player
      :type:  Literal['B', 'W']
      :value: None



   .. py:attribute:: row
      :type:  int
      :value: None



