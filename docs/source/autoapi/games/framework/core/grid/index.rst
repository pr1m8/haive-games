games.framework.core.grid
=========================

.. py:module:: games.framework.core.grid


Classes
-------

.. autoapisummary::

   games.framework.core.grid.GridPosition


Module Contents
---------------

.. py:class:: GridPosition

   Bases: :py:obj:`haive.games.framework.core.position.Position`


   Position on a grid-based board with row and column coordinates.

   Used in games like Chess, Checkers, Scrabble, etc. where the board is organized as a
   rectangular grid of cells.



   .. autolink-examples:: GridPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool

      Grid positions are equal if they have the same row and column.


      .. autolink-examples:: __eq__
         :collapse:


   .. py:method:: __hash__() -> int

      Hash based on row and column.


      .. autolink-examples:: __hash__
         :collapse:


   .. py:method:: validate_coordinates(v: int) -> int
      :classmethod:


      Ensure coordinates are valid.


      .. autolink-examples:: validate_coordinates
         :collapse:


   .. py:attribute:: col
      :type:  int


   .. py:property:: coordinates
      :type: tuple[int, int]


      Get the row and column as a tuple.

      .. autolink-examples:: coordinates
         :collapse:


   .. py:property:: display_coords
      :type: str


      Return human-readable coordinates.

      For chess-style notation, this returns coordinates like 'A1', 'B2', etc. where
      the column is a letter (A-Z) and the row is a number (1-based).

      .. autolink-examples:: display_coords
         :collapse:


   .. py:attribute:: row
      :type:  int


