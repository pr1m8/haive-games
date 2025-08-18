games.core.position.base
========================

.. py:module:: games.core.position.base

Module documentation for games.core.position.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span>   </div>


      
            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.core.position.base.GridPosition
      games.core.position.base.HexPosition
      games.core.position.base.NodePosition
      games.core.position.base.PointPosition
      games.core.position.base.Position

            
            

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


            Position on a grid-based board (Chess, Checkers, Scrabble).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool


            .. py:method:: __hash__() -> int


            .. py:method:: validate_coordinates(v: int) -> int
               :classmethod:


               Ensure coordinates are valid.



            .. py:attribute:: col
               :type:  int


            .. py:property:: display_coords
               :type: str


               Return human-readable coordinates (e.g. 'A1' for chess).


            .. py:attribute:: row
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HexPosition(/, **data: Any)

            Bases: :py:obj:`Position`


            Position on a hexagonal grid (e.g., Settlers of Catan).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool


            .. py:method:: __hash__() -> int


            .. py:method:: neighbors() -> list[HexPosition]

               Get all adjacent hex positions.



            .. py:method:: validate_hex_coords(v: int) -> int
               :classmethod:


               Hex coordinates can be negative.



            .. py:attribute:: q
               :type:  int


            .. py:attribute:: r
               :type:  int


            .. py:property:: s
               :type: int


               Compute third coordinate for cube representation.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NodePosition(/, **data: Any)

            Bases: :py:obj:`Position`


            Position in a graph-based board (e.g., Ticket to Ride).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool


            .. py:method:: __hash__() -> int


            .. py:attribute:: node_id
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PointPosition(/, **data: Any)

            Bases: :py:obj:`Position`


            Position using floating point coordinates (e.g., Go, graph-based games).

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool


            .. py:method:: __hash__() -> int


            .. py:method:: distance_to(other: PointPosition) -> float

               Calculate Euclidean distance to another point.



            .. py:attribute:: x
               :type:  float


            .. py:attribute:: y
               :type:  float


            .. py:attribute:: z
               :type:  float | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Position(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Base class for all position types in games.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: frozen
                  :value: True




            .. py:attribute:: id
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.position.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

