games.framework.core.boards.grid
================================

.. py:module:: games.framework.core.boards.grid

Module documentation for games.framework.core.boards.grid


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.framework.core.boards.grid.T

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.boards.grid.GridBoard

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GridBoard

            Bases: :py:obj:`haive.games.framework.core.board.Board`\ [\ :py:obj:`haive.games.framework.core.spaces.grid.GridSpace`\ [\ :py:obj:`T`\ ]\ , :py:obj:`haive.games.framework.core.positions.grid.GridPosition`\ , :py:obj:`T`\ ]


            A grid-based board (Chess, Checkers, Scrabble).

            This represents a rectangular grid of spaces.



            .. py:method:: get_space_at(row: int, col: int) -> haive.games.framework.core.spaces.grid.GridSpace[T] | None

               Get the space at the specified grid coordinates.

               :param row: Row index
               :param col: Column index

               :returns: The space at the position, or None if no space exists there



            .. py:method:: get_space_at_position(position: haive.games.framework.core.positions.grid.GridPosition) -> haive.games.framework.core.spaces.grid.GridSpace[T] | None

               Get the space at the specified grid coordinates.

               :param position: Grid position to look up

               :returns: The space at the position, or None if no space exists there



            .. py:method:: initialize_grid(space_factory: collections.abc.Callable[[int, int], haive.games.framework.core.spaces.grid.GridSpace[T]] | None = None) -> None

               Initialize a standard grid with the specified dimensions.

               :param space_factory: Optional factory function to create spaces



            .. py:method:: validate_dimensions(v: int) -> int
               :classmethod:


               Ensure board dimensions are positive.



            .. py:attribute:: cols
               :type:  int


            .. py:attribute:: rows
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.boards.grid import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

