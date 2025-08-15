games.core.game.core_board
==========================

.. py:module:: games.core.game.core_board

.. autoapi-nested-parse::

   Board models for the game framework.

   This module defines the base Board class and specific implementations for different
   types of game boards.


   .. autolink-examples:: games.core.game.core_board
      :collapse:


Attributes
----------

.. autoapisummary::

   games.core.game.core_board.P
   games.core.game.core_board.S
   games.core.game.core_board.T


Classes
-------

.. autoapisummary::

   games.core.game.core_board.Board
   games.core.game.core_board.GridBoard


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


   .. py:method:: get_all_pieces() -> dict[str, T]

      Get all pieces currently on the board.

      :returns: Dictionary mapping piece IDs to pieces


      .. autolink-examples:: get_all_pieces
         :collapse:


   .. py:method:: get_connected_spaces(space_id: str) -> list[S]

      Get all spaces connected to the given space.

      :param space_id: ID of the space to get connections for

      :returns: List of connected spaces

      :raises ValueError: If the space doesn't exist on the board


      .. autolink-examples:: get_connected_spaces
         :collapse:


   .. py:method:: get_player_pieces(player_id: str) -> list[T]

      Get all pieces belonging to a specific player.

      :param player_id: ID of the player

      :returns: List of pieces owned by the player


      .. autolink-examples:: get_player_pieces
         :collapse:


   .. py:method:: get_property(key: str, default: Any = None) -> Any

      Get a board property.

      :param key: Property name
      :param default: Default value if property doesn't exist

      :returns: Property value or default


      .. autolink-examples:: get_property
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


   .. py:method:: is_position_valid(position: P) -> bool

      Check if a position is valid on this board.

      :param position: Position to check

      :returns: True if the position is valid, False otherwise


      .. autolink-examples:: is_position_valid
         :collapse:


   .. py:method:: place_piece(piece: T, position: P) -> bool

      Place a piece at the specified position.

      :param piece: The piece to place
      :param position: Position to place the piece at

      :returns: True if placement was successful, False otherwise


      .. autolink-examples:: place_piece
         :collapse:


   .. py:method:: remove_piece(position: P) -> T | None

      Remove a piece from the specified position.

      :param position: Position to remove the piece from

      :returns: The removed piece, or None if no piece was at the position


      .. autolink-examples:: remove_piece
         :collapse:


   .. py:method:: set_property(key: str, value: Any) -> None

      Set a board property.

      :param key: Property name
      :param value: Property value


      .. autolink-examples:: set_property
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



.. py:class:: GridBoard

   Bases: :py:obj:`Board`\ [\ :py:obj:`haive.games.core.game.core.space.GridSpace`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]\ , :py:obj:`P`\ , :py:obj:`T`\ ]


   A grid-based board (Chess, Checkers, Scrabble).

   This represents a rectangular grid of spaces.



   .. autolink-examples:: GridBoard
      :collapse:

   .. py:method:: get_column(col: int) -> list[haive.games.core.game.core.space.GridSpace[P, T]]

      Get all spaces in a column.

      :param col: Column index

      :returns: List of spaces in the column, ordered by row


      .. autolink-examples:: get_column
         :collapse:


   .. py:method:: get_row(row: int) -> list[haive.games.core.game.core.space.GridSpace[P, T]]

      Get all spaces in a row.

      :param row: Row index

      :returns: List of spaces in the row, ordered by column


      .. autolink-examples:: get_row
         :collapse:


   .. py:method:: get_space_at(row: int, col: int) -> haive.games.core.game.core.space.GridSpace[P, T] | None

      Get the space at the specified grid coordinates.

      :param row: Row index
      :param col: Column index

      :returns: The space at the position, or None if no space exists there


      .. autolink-examples:: get_space_at
         :collapse:


   .. py:method:: get_space_at_position(position: P) -> haive.games.core.game.core.space.GridSpace[P, T] | None

      Get the space at the specified grid coordinates.

      :param position: Grid position to look up

      :returns: The space at the position, or None if no space exists there


      .. autolink-examples:: get_space_at_position
         :collapse:


   .. py:method:: initialize_grid(space_factory: collections.abc.Callable[[int, int], haive.games.core.game.core.space.GridSpace[P, T]] | None = None) -> None

      Initialize a standard grid with the specified dimensions.

      :param space_factory: Optional factory function to create spaces


      .. autolink-examples:: initialize_grid
         :collapse:


   .. py:method:: is_position_valid(position: P) -> bool

      Check if a position is within the grid bounds.

      :param position: Position to check

      :returns: True if the position is valid, False otherwise


      .. autolink-examples:: is_position_valid
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


   .. py:property:: size
      :type: int


      Get the total number of spaces on the board.

      :returns: Total number of spaces

      .. autolink-examples:: size
         :collapse:


.. py:data:: P

.. py:data:: S

.. py:data:: T

