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


   .. autolink-examples:: games.fox_and_geese.models
      :collapse:


Classes
-------

.. autoapisummary::

   games.fox_and_geese.models.FoxAndGeeseAnalysis
   games.fox_and_geese.models.FoxAndGeeseMove
   games.fox_and_geese.models.FoxAndGeesePosition


Module Contents
---------------

.. py:class:: FoxAndGeeseAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of a Fox and Geese position.

   This class defines the structure of an analysis of a Fox and Geese position, which
   includes an advantage, an advantage level, key features, fox strategy, geese
   strategy, and critical squares.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FoxAndGeeseAnalysis
      :collapse:

   .. py:method:: __eq__(other) -> bool


   .. py:method:: __hash__() -> int


   .. py:attribute:: advantage
      :type:  Literal['fox', 'geese', 'equal']
      :value: None



   .. py:attribute:: advantage_level
      :type:  int
      :value: None



   .. py:attribute:: critical_squares
      :type:  list[str]
      :value: None



   .. py:attribute:: explanation
      :type:  str
      :value: None



   .. py:attribute:: fox_strategy
      :type:  str
      :value: None



   .. py:attribute:: geese_strategy
      :type:  str
      :value: None



   .. py:attribute:: key_features
      :type:  list[str]
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


.. py:class:: FoxAndGeeseMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a move in Fox and Geese.

   This class defines the structure of a move in Fox and Geese, which includes a
   starting position, an ending position, a piece type, and an optional captured
   position.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FoxAndGeeseMove
      :collapse:

   .. py:method:: __eq__(other) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __str__() -> str


   .. py:attribute:: capture
      :type:  FoxAndGeesePosition | None
      :value: None



   .. py:attribute:: from_pos
      :type:  FoxAndGeesePosition
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: piece_type
      :type:  Literal['fox', 'goose']
      :value: None



   .. py:attribute:: to_pos
      :type:  FoxAndGeesePosition
      :value: None



.. py:class:: FoxAndGeesePosition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Immutable position coordinate on the Fox and Geese board.

   Represents a specific square on the 7x7 Fox and Geese board using
   zero-indexed row and column coordinates. The position is immutable
   and hashable, making it suitable for use in sets and as dictionary keys.

   The board layout follows traditional Fox and Geese conventions:
   - Row 0: Top of the board (fox starting area)
   - Row 6: Bottom of the board (geese starting area)
   - Column 0-6: Left to right across the board

   .. attribute:: row

      Row coordinate (0-6) from top to bottom of the board.

   .. attribute:: col

      Column coordinate (0-6) from left to right of the board.

   .. rubric:: Examples

   Creating positions::

       # Fox starting position (center top)
       fox_start = FoxAndGeesePosition(row=0, col=3)

       # Geese starting positions (bottom row)
       geese_positions = [
           FoxAndGeesePosition(row=6, col=i) for i in range(7)
       ]

       # Center board position
       center = FoxAndGeesePosition(row=3, col=3)

   Position validation::

       # Valid positions
       valid_pos = FoxAndGeesePosition(row=5, col=2)
       assert 0 <= valid_pos.row < 7
       assert 0 <= valid_pos.col < 7

       # Invalid positions raise validation errors
       try:
           invalid = FoxAndGeesePosition(row=7, col=3)  # Row too high
       except ValueError as e:
           print(f"Invalid position: {e}")

   Working with position sets::

       # Positions are hashable
       occupied_squares = {
           FoxAndGeesePosition(row=0, col=3),  # Fox
           FoxAndGeesePosition(row=6, col=0),  # Goose
           FoxAndGeesePosition(row=6, col=1),  # Goose
       }

       # Check if position is occupied
       test_pos = FoxAndGeesePosition(row=3, col=3)
       is_occupied = test_pos in occupied_squares

   Strategic context::

       # Corner positions (strategic for fox)
       corners = [
           FoxAndGeesePosition(row=0, col=0),
           FoxAndGeesePosition(row=0, col=6),
           FoxAndGeesePosition(row=6, col=0),
           FoxAndGeesePosition(row=6, col=6)
       ]

       # Center control positions
       center_squares = [
           FoxAndGeesePosition(row=3, col=3),
           FoxAndGeesePosition(row=3, col=4),
           FoxAndGeesePosition(row=4, col=3),
           FoxAndGeesePosition(row=4, col=4)
       ]

   .. note::

      The position is frozen (immutable) to ensure data integrity and
      enable use as dictionary keys and in sets. String representation
      uses mathematical coordinate notation: "(row, col)".

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: FoxAndGeesePosition
      :collapse:

   .. py:method:: __eq__(other) -> bool

      Check equality with another position.

      :param other: Object to compare with.

      :returns: True if positions have same row and column.
      :rtype: bool


      .. autolink-examples:: __eq__
         :collapse:


   .. py:method:: __hash__() -> int

      Generate hash for use in sets and dictionaries.

      :returns: Hash value based on row and column coordinates.
      :rtype: int


      .. autolink-examples:: __hash__
         :collapse:


   .. py:method:: __str__() -> str

      String representation of the position.

      :returns: Position in format "(row, col)".
      :rtype: str

      .. rubric:: Examples

      Position display::

          pos = FoxAndGeesePosition(row=3, col=4)
          print(pos)  # "(3, 4)"


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: col
      :type:  int
      :value: None



   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].

      .. autolink-examples:: model_config
         :collapse:


   .. py:attribute:: row
      :type:  int
      :value: None



