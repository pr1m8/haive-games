games.base.models
=================

.. py:module:: games.base.models

.. autoapi-nested-parse::

   Base models for game agents.

   This module provides the foundational data models used across game agents.
   It includes models for game state, player state, moves, and other common
   game-related data structures.

   .. rubric:: Example

   >>> board = Board(size=(8, 8))
   >>> player = Player(id="p1", name="Player 1")
   >>> state = GameState(board=board, players=[player])

   Typical usage:
       - Use these models as base classes for game-specific models
       - Inherit from these models to add game-specific functionality


   .. autolink-examples:: games.base.models
      :collapse:


Attributes
----------

.. autoapisummary::

   games.base.models.TMove


Classes
-------

.. autoapisummary::

   games.base.models.Board
   games.base.models.Cell
   games.base.models.GameState
   games.base.models.MoveModel
   games.base.models.Piece
   games.base.models.Player


Module Contents
---------------

.. py:class:: Board(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a generic game board.

   This class provides a basic representation of a game board with
   dimensions and optional grid-based structure.

   .. attribute:: size

      The dimensions of the board (width, height).

      :type: Tuple[int, int]

   .. attribute:: grid

      Optional grid representation.

      :type: Optional[List[List[str]]]

   .. rubric:: Example

   >>> board = Board(size=(8, 8))
   >>> chess_board = Board(size=(8, 8), grid=[["R", "N", "B", ...]])

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Board
      :collapse:

   .. py:attribute:: grid
      :type:  list[list[str]] | None
      :value: None



   .. py:attribute:: size
      :type:  tuple[int, int]
      :value: None



.. py:class:: Cell(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a cell on the board.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Cell
      :collapse:

   .. py:attribute:: col
      :type:  int
      :value: None



   .. py:attribute:: content
      :type:  str | None
      :value: None



   .. py:attribute:: row
      :type:  int
      :value: None



.. py:class:: GameState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents the state of a generic game.

   Core game state model that can be extended for specific games.

   .. attribute:: board

      The game board.

      :type: Board

   .. attribute:: players

      List of players in the game.

      :type: List[Player]

   .. attribute:: current_player

      The player whose turn it is.

      :type: Player

   .. attribute:: game_status

      Current game status.

      :type: Literal["ongoing", "ended"]

   .. attribute:: game_result

      Final result when game ends.

      :type: Optional[str]

   .. rubric:: Example

   >>> state = GameState(
   ...     board=Board(size=(8, 8)),
   ...     players=[Player(id="p1", name="Player 1")],
   ...     current_player=player,
   ...     game_status="ongoing"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameState
      :collapse:

   .. py:attribute:: board
      :type:  Board
      :value: None



   .. py:attribute:: current_player
      :type:  Player
      :value: None



   .. py:attribute:: game_result
      :type:  str | None
      :value: None



   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'ended']
      :value: None



   .. py:attribute:: players
      :type:  list[Player]
      :value: None



.. py:class:: MoveModel(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`TMove`\ ], :py:obj:`abc.ABC`


   Generic model for game moves.

   This class represents a move in the game, generic over the specific
   type of move (TMove) used in the game.

   .. attribute:: move

      The actual move data.

      :type: TMove

   .. attribute:: player_id

      ID of the player making the move.

      :type: str

   .. attribute:: timestamp

      When the move was made.

      :type: float

   .. rubric:: Example

   >>> class ChessMove(BaseModel):
   ...     from_pos: str
   ...     to_pos: str
   >>> move = MoveModel[ChessMove](
   ...     move=ChessMove(from_pos="e2", to_pos="e4"),
   ...     player_id="p1"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MoveModel
      :collapse:

   .. py:method:: validate_move(move, info) -> Any
      :classmethod:


      Override in game-specific models to validate the move.


      .. autolink-examples:: validate_move
         :collapse:


   .. py:attribute:: move
      :type:  TMove
      :value: None



   .. py:attribute:: player_id
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  float
      :value: None



.. py:class:: Piece(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a piece on the board.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Piece
      :collapse:

   .. py:attribute:: player
      :type:  Player
      :value: None



   .. py:attribute:: position
      :type:  Cell
      :value: None



   .. py:attribute:: type
      :type:  str
      :value: None



.. py:class:: Player(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a player in the game.

   Base player model with essential player information and state.

   .. attribute:: id

      Unique identifier for the player.

      :type: str

   .. attribute:: name

      Display name of the player.

      :type: str

   .. attribute:: score

      Current score or points.

      :type: int

   .. attribute:: is_active

      Whether the player is still active in the game.

      :type: bool

   .. rubric:: Example

   >>> player = Player(id="p1", name="Player 1", score=0)

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Player
      :collapse:

   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: is_active
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: score
      :type:  int
      :value: None



.. py:data:: TMove

