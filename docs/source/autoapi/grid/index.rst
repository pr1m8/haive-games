grid
====

.. py:module:: grid

Module documentation for grid


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      grid.GridPosition

            
            

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

            Bases: :py:obj:`haive.games.framework.core.position.Position`


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





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from grid import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

