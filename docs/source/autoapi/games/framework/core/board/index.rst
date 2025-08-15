games.framework.core.board
==========================

.. py:module:: games.framework.core.board


Attributes
----------

.. autoapisummary::

   games.framework.core.board.P
   games.framework.core.board.S
   games.framework.core.board.T


Classes
-------

.. autoapisummary::

   games.framework.core.board.Board


Module Contents
---------------

.. py:class:: Board(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`S`\ , :py:obj:`P`\ , :py:obj:`T`\ ]


   Base class for all game boards.

   A Board represents the playing surface in a game, containing spaces where pieces can
   be placed. It manages the spatial relationships between spaces.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Board
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add_space(space: S) -> str

      Add a space to the board.

      :param space: The space to add

      :returns: ID of the added space


      .. autolink-examples:: add_space
         :collapse:


   .. py:method:: connect_spaces(space1_id: str, space2_id: str) -> None

      Connect two spaces bidirectionally.

      :param space1_id: ID of the first space
      :param space2_id: ID of the second space

      :raises ValueError: If either space doesn't exist on the board


      .. autolink-examples:: connect_spaces
         :collapse:


   .. py:method:: get_space_at_position(position: P) -> S | None
      :abstractmethod:


      Get the space at the specified position.

      This is an abstract method that must be implemented by subclasses
      to provide position-based lookup.

      :param position: The position to look up

      :returns: The space at the position, or None if no space exists there


      .. autolink-examples:: get_space_at_position
         :collapse:


   .. py:method:: place_piece(piece: T, position: P) -> bool

      Place a piece at the specified position.

      :param piece: The piece to place
      :param position: Position to place the piece at

      :returns: True if placement was successful, False otherwise


      .. autolink-examples:: place_piece
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: spaces
      :type:  dict[str, S]
      :value: None



.. py:data:: P

.. py:data:: S

.. py:data:: T

