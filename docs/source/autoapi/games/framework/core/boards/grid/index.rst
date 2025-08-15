games.framework.core.boards.grid
================================

.. py:module:: games.framework.core.boards.grid


Attributes
----------

.. autoapisummary::

   games.framework.core.boards.grid.T


Classes
-------

.. autoapisummary::

   games.framework.core.boards.grid.GridBoard


Module Contents
---------------

.. py:class:: GridBoard

   Bases: :py:obj:`haive.games.framework.core.board.Board`\ [\ :py:obj:`haive.games.framework.core.spaces.grid.GridSpace`\ [\ :py:obj:`T`\ ]\ , :py:obj:`haive.games.framework.core.positions.grid.GridPosition`\ , :py:obj:`T`\ ]


   A grid-based board (Chess, Checkers, Scrabble).

   This represents a rectangular grid of spaces.



   .. autolink-examples:: GridBoard
      :collapse:

   .. py:method:: get_space_at(row: int, col: int) -> haive.games.framework.core.spaces.grid.GridSpace[T] | None

      Get the space at the specified grid coordinates.

      :param row: Row index
      :param col: Column index

      :returns: The space at the position, or None if no space exists there


      .. autolink-examples:: get_space_at
         :collapse:


   .. py:method:: get_space_at_position(position: haive.games.framework.core.positions.grid.GridPosition) -> haive.games.framework.core.spaces.grid.GridSpace[T] | None

      Get the space at the specified grid coordinates.

      :param position: Grid position to look up

      :returns: The space at the position, or None if no space exists there


      .. autolink-examples:: get_space_at_position
         :collapse:


   .. py:method:: initialize_grid(space_factory: collections.abc.Callable[[int, int], haive.games.framework.core.spaces.grid.GridSpace[T]] | None = None) -> None

      Initialize a standard grid with the specified dimensions.

      :param space_factory: Optional factory function to create spaces


      .. autolink-examples:: initialize_grid
         :collapse:


   .. py:method:: validate_dimensions(v: int) -> int
      :classmethod:


      Ensure board dimensions are positive.


      .. autolink-examples:: validate_dimensions
         :collapse:


   .. py:attribute:: cols
      :type:  int


   .. py:attribute:: rows
      :type:  int


.. py:data:: T

