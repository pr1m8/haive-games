games.core.position.base
========================

.. py:module:: games.core.position.base


Classes
-------

.. autoapisummary::

   games.core.position.base.GridPosition
   games.core.position.base.HexPosition
   games.core.position.base.NodePosition
   games.core.position.base.PointPosition
   games.core.position.base.Position


Module Contents
---------------

.. py:class:: GridPosition(/, **data: Any)

   Bases: :py:obj:`Position`


   Position on a grid-based board (Chess, Checkers, Scrabble).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GridPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: validate_coordinates(v: int) -> int
      :classmethod:


      Ensure coordinates are valid.


      .. autolink-examples:: validate_coordinates
         :collapse:


   .. py:attribute:: col
      :type:  int


   .. py:property:: display_coords
      :type: str


      Return human-readable coordinates (e.g. 'A1' for chess).

      .. autolink-examples:: display_coords
         :collapse:


   .. py:attribute:: row
      :type:  int


.. py:class:: HexPosition(/, **data: Any)

   Bases: :py:obj:`Position`


   Position on a hexagonal grid (e.g., Settlers of Catan).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HexPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: neighbors() -> list[HexPosition]

      Get all adjacent hex positions.


      .. autolink-examples:: neighbors
         :collapse:


   .. py:method:: validate_hex_coords(v: int) -> int
      :classmethod:


      Hex coordinates can be negative.


      .. autolink-examples:: validate_hex_coords
         :collapse:


   .. py:attribute:: q
      :type:  int


   .. py:attribute:: r
      :type:  int


   .. py:property:: s
      :type: int


      Compute third coordinate for cube representation.

      .. autolink-examples:: s
         :collapse:


.. py:class:: NodePosition(/, **data: Any)

   Bases: :py:obj:`Position`


   Position in a graph-based board (e.g., Ticket to Ride).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NodePosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:attribute:: node_id
      :type:  str


.. py:class:: PointPosition(/, **data: Any)

   Bases: :py:obj:`Position`


   Position using floating point coordinates (e.g., Go, graph-based games).

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PointPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: distance_to(other: PointPosition) -> float

      Calculate Euclidean distance to another point.


      .. autolink-examples:: distance_to
         :collapse:


   .. py:attribute:: x
      :type:  float


   .. py:attribute:: y
      :type:  float


   .. py:attribute:: z
      :type:  float | None
      :value: None



.. py:class:: Position(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base class for all position types in games.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Position
      :collapse:

   .. py:class:: Config

      .. py:attribute:: frozen
         :value: True




   .. py:attribute:: id
      :type:  str
      :value: None



