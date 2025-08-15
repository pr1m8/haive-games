games.core.game.piece
=====================

.. py:module:: games.core.game.piece


Classes
-------

.. autoapisummary::

   games.core.game.piece.GamePiece
   games.core.game.piece.GamePieceProtocol


Module Contents
---------------

.. py:class:: GamePiece(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ ]


   Base class for any game piece that can be placed on a board.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePiece
      :collapse:

   .. py:method:: assign_to_player(player_id: str) -> None

      Assign this piece to a player.


      .. autolink-examples:: assign_to_player
         :collapse:


   .. py:method:: can_move_to(position: P, board: Board) -> bool
      :abstractmethod:


      Check if this piece can move to the specified position.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:method:: place_at(position: P) -> None

      Place this piece at the specified position.


      .. autolink-examples:: place_at
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: owner_id
      :type:  str | None
      :value: None



   .. py:attribute:: position
      :type:  P | None
      :value: None



.. py:class:: GamePieceProtocol

   Bases: :py:obj:`Protocol`


   Protocol defining the required interface for game pieces.


   .. autolink-examples:: GamePieceProtocol
      :collapse:

   .. py:method:: assign_to_player(player_id: str) -> None


   .. py:method:: can_move_to(position: Position, board: Board) -> bool


   .. py:method:: place_at(position: Position) -> None


   .. py:attribute:: id
      :type:  str


   .. py:attribute:: owner_id
      :type:  str | None


   .. py:attribute:: position
      :type:  Position | None


