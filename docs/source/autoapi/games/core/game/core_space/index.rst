games.core.game.core_space
==========================

.. py:module:: games.core.game.core_space

.. autoapi-nested-parse::

   Space models for the game framework.

   This module defines the base Space class and specific implementations for different
   types of board spaces.


   .. autolink-examples:: games.core.game.core_space
      :collapse:


Attributes
----------

.. autoapisummary::

   games.core.game.core_space.P
   games.core.game.core_space.T


Classes
-------

.. autoapisummary::

   games.core.game.core_space.GridSpace
   games.core.game.core_space.HexSpace
   games.core.game.core_space.Space
   games.core.game.core_space.SpaceProtocol


Module Contents
---------------

.. py:class:: GridSpace

   Bases: :py:obj:`Space`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


   A space on a grid-based board.

   Used for games like Chess, Checkers, Scrabble, etc.



   .. autolink-examples:: GridSpace
      :collapse:

   .. py:method:: get_grid_position() -> tuple[int, int]

      Get the grid coordinates of this space.

      :returns: Tuple of (row, col)


      .. autolink-examples:: get_grid_position
         :collapse:


   .. py:property:: coordinates
      :type: str


      Get human-readable coordinates for this space.

      :returns: String like "A1", "B2", etc.

      .. autolink-examples:: coordinates
         :collapse:


.. py:class:: HexSpace

   Bases: :py:obj:`Space`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


   A space on a hexagonal board.

   Used for games like Catan, hex-based war games, etc.



   .. autolink-examples:: HexSpace
      :collapse:

   .. py:property:: coordinates
      :type: tuple[int, int, int]


      Get the hex coordinates of this space.

      :returns: Tuple of (q, r, s) in cube coordinates

      .. autolink-examples:: coordinates
         :collapse:


.. py:class:: Space(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


   A space on a game board where pieces can be placed.

   A Space represents a location on a board that can hold a game piece. It has a
   position and can be connected to other spaces.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Space
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add_connection(space_id: str) -> None

      Add a connection to another space.

      :param space_id: ID of the space to connect to


      .. autolink-examples:: add_connection
         :collapse:


   .. py:method:: get_property(key: str, default: Any = None) -> Any

      Get a property value.

      :param key: Property name
      :param default: Default value if property doesn't exist

      :returns: Property value or default


      .. autolink-examples:: get_property
         :collapse:


   .. py:method:: is_connected_to(space_id: str) -> bool

      Check if this space is connected to another space.

      :param space_id: ID of the space to check

      :returns: True if connected, False otherwise


      .. autolink-examples:: is_connected_to
         :collapse:


   .. py:method:: is_occupied() -> bool

      Check if this space is occupied by a piece.

      :returns: True if the space has a piece, False otherwise


      .. autolink-examples:: is_occupied
         :collapse:


   .. py:method:: place_piece(piece: T) -> bool

      Place a piece on this space.

      :param piece: The piece to place

      :returns: True if placement was successful, False otherwise


      .. autolink-examples:: place_piece
         :collapse:


   .. py:method:: remove_connection(space_id: str) -> None

      Remove a connection to another space.

      :param space_id: ID of the space to disconnect from


      .. autolink-examples:: remove_connection
         :collapse:


   .. py:method:: remove_piece() -> T | None

      Remove and return the piece on this space.

      :returns: The removed piece, or None if no piece was on the space


      .. autolink-examples:: remove_piece
         :collapse:


   .. py:method:: set_property(key: str, value: Any) -> None

      Set a property value.

      :param key: Property name
      :param value: Property value


      .. autolink-examples:: set_property
         :collapse:


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



.. py:class:: SpaceProtocol

   Bases: :py:obj:`Protocol`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


   Protocol defining the required interface for board spaces.


   .. autolink-examples:: SpaceProtocol
      :collapse:

   .. py:method:: is_occupied() -> bool


   .. py:method:: place_piece(piece: T) -> bool


   .. py:method:: remove_piece() -> T | None


   .. py:attribute:: id
      :type:  str


   .. py:attribute:: position
      :type:  P


.. py:data:: P

.. py:data:: T

