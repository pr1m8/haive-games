games.core.game.core_position
=============================

.. py:module:: games.core.game.core_position

Position models for the game framework.

This module defines the base Position class and its specific implementations for
different coordinate systems used in games.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>

.. autoapi-nested-parse::

   Position models for the game framework.

   This module defines the base Position class and its specific implementations for
   different coordinate systems used in games.



      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.core.game.core_position.GridPosition
      games.core.game.core_position.HexPosition
      games.core.game.core_position.PointPosition
      games.core.game.core_position.Position

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GridPosition(/, **data: Any)

            Bases: :py:obj:`Position`


            Position on a grid-based board with row and column coordinates.

            Used in games like Chess, Checkers, Scrabble, etc. where the board is organized as a
            rectangular grid of cells.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool

               Grid positions are equal if they have the same row and column.



            .. py:method:: __hash__() -> int

               Hash based on row and column.



            .. py:method:: chebyshev_distance(other: GridPosition) -> int

               Calculate the Chebyshev distance to another grid position.

               This is the maximum of the horizontal and vertical distances, which corresponds
               to the number of moves a king in chess would need.




            .. py:method:: manhattan_distance(other: GridPosition) -> int

               Calculate the Manhattan distance to another grid position.



            .. py:method:: neighbors() -> dict[str, GridPosition]

               Get all adjacent grid positions (orthogonal).

               :returns: Dictionary mapping direction names to positions.



            .. py:method:: neighbors_with_diagonals() -> dict[str, GridPosition]

               Get all adjacent grid positions including diagonals.

               :returns: Dictionary mapping direction names to positions.



            .. py:method:: offset(row_offset: int, col_offset: int) -> GridPosition

               Create a new position that is offset from this one.



            .. py:method:: validate_coordinates(v: int) -> int
               :classmethod:


               Ensure coordinates are valid.



            .. py:attribute:: col
               :type:  int


            .. py:property:: coordinates
               :type: tuple[int, int]


               Get the row and column as a tuple.


            .. py:property:: display_coords
               :type: str


               Return human-readable coordinates.

               For chess-style notation, this returns coordinates like 'A1', 'B2', etc. where
               the column is a letter (A-Z) and the row is a number (1-based).


            .. py:attribute:: row
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HexPosition(/, **data: Any)

            Bases: :py:obj:`Position`


            Position on a hexagonal grid using cube coordinates.

            Used in games like Catan, hex-based war games, etc.

            This uses cube coordinates (q, r, s) where q + r + s = 0.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool

               Hex positions are equal if they have the same q, r, and s.



            .. py:method:: __hash__() -> int

               Hash based on q, r, and s coordinates.



            .. py:method:: distance(other: HexPosition) -> int

               Calculate the distance to another hex position.



            .. py:method:: from_axial(q: int, r: int) -> HexPosition
               :classmethod:


               Create a hex position from axial coordinates (q, r).



            .. py:method:: neighbors() -> dict[str, HexPosition]

               Get all adjacent hex positions.

               :returns: Dictionary mapping direction names to positions.



            .. py:method:: validate_cube_coords(v: int, values: dict) -> int
               :classmethod:


               Ensure cube coordinates are valid (q + r + s = 0).



            .. py:property:: axial_coords
               :type: tuple[int, int]


               Get the axial coordinates (q, r) as a tuple.


            .. py:attribute:: q
               :type:  int


            .. py:attribute:: r
               :type:  int


            .. py:attribute:: s
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PointPosition(/, **data: Any)

            Bases: :py:obj:`Position`


            Position using floating point coordinates in a 2D space.

            Used in games with continuous coordinates like territory maps or physics-based
            games.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool

               Point positions are equal if they have the same x and y.



            .. py:method:: __hash__() -> int

               Hash based on x and y coordinates.



            .. py:method:: distance_to(other: PointPosition) -> float

               Calculate the Euclidean distance to another point position.



            .. py:method:: offset(x_offset: float, y_offset: float) -> PointPosition

               Create a new position that is offset from this one.



            .. py:property:: coordinates
               :type: tuple[float, float]


               Get the x and y as a tuple.


            .. py:attribute:: x
               :type:  float


            .. py:attribute:: y
               :type:  float



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Position(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Base class for all position types in games.

            A Position represents a location in a game. Different games use different coordinate
            systems, so this base class is extended for specific needs.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: frozen
                  :value: True




            .. py:method:: __eq__(other: object) -> bool

               Check if positions are equal.

               Base implementation compares IDs; subclasses should override.




            .. py:method:: __hash__() -> int

               Hash implementation for dictionary keys and sets.



            .. py:method:: serialize() -> dict[str, Any]

               Convert the position to a serializable dictionary.



            .. py:attribute:: id
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.game.core_position import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

