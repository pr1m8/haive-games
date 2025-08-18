games.core.game.core_space
==========================

.. py:module:: games.core.game.core_space

Space models for the game framework.

This module defines the base Space class and specific implementations for different
types of board spaces.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Space models for the game framework.

   This module defines the base Space class and specific implementations for different
   types of board spaces.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.core.game.core_space.P
      games.core.game.core_space.T

            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.core.game.core_space.GridSpace
      games.core.game.core_space.HexSpace
      games.core.game.core_space.Space
      games.core.game.core_space.SpaceProtocol

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GridSpace

            Bases: :py:obj:`Space`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


            A space on a grid-based board.

            Used for games like Chess, Checkers, Scrabble, etc.



            .. py:method:: get_grid_position() -> tuple[int, int]

               Get the grid coordinates of this space.

               :returns: Tuple of (row, col)



            .. py:property:: coordinates
               :type: str


               Get human-readable coordinates for this space.

               :returns: String like "A1", "B2", etc.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HexSpace

            Bases: :py:obj:`Space`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


            A space on a hexagonal board.

            Used for games like Catan, hex-based war games, etc.



            .. py:property:: coordinates
               :type: tuple[int, int, int]


               Get the hex coordinates of this space.

               :returns: Tuple of (q, r, s) in cube coordinates



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Space(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


            A space on a game board where pieces can be placed.

            A Space represents a location on a board that can hold a game piece. It has a
            position and can be connected to other spaces.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: add_connection(space_id: str) -> None

               Add a connection to another space.

               :param space_id: ID of the space to connect to



            .. py:method:: get_property(key: str, default: Any = None) -> Any

               Get a property value.

               :param key: Property name
               :param default: Default value if property doesn't exist

               :returns: Property value or default



            .. py:method:: is_connected_to(space_id: str) -> bool

               Check if this space is connected to another space.

               :param space_id: ID of the space to check

               :returns: True if connected, False otherwise



            .. py:method:: is_occupied() -> bool

               Check if this space is occupied by a piece.

               :returns: True if the space has a piece, False otherwise



            .. py:method:: place_piece(piece: T) -> bool

               Place a piece on this space.

               :param piece: The piece to place

               :returns: True if placement was successful, False otherwise



            .. py:method:: remove_connection(space_id: str) -> None

               Remove a connection to another space.

               :param space_id: ID of the space to disconnect from



            .. py:method:: remove_piece() -> T | None

               Remove and return the piece on this space.

               :returns: The removed piece, or None if no piece was on the space



            .. py:method:: set_property(key: str, value: Any) -> None

               Set a property value.

               :param key: Property name
               :param value: Property value



            .. py:attribute:: connections
               :type:  set[str]
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str | None
               :value: None



            .. py:attribute:: piece
               :type:  T | None
               :value: None



            .. py:attribute:: position
               :type:  P


            .. py:attribute:: properties
               :type:  dict[str, Any]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SpaceProtocol

            Bases: :py:obj:`Protocol`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


            Protocol defining the required interface for board spaces.


            .. py:method:: is_occupied() -> bool


            .. py:method:: place_piece(piece: T) -> bool


            .. py:method:: remove_piece() -> T | None


            .. py:attribute:: id
               :type:  str


            .. py:attribute:: position
               :type:  P



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: P


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: T




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.game.core_space import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

