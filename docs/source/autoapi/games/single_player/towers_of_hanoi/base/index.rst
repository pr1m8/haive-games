games.single_player.towers_of_hanoi.base
========================================

.. py:module:: games.single_player.towers_of_hanoi.base


Attributes
----------

.. autoapisummary::

   games.single_player.towers_of_hanoi.base.D
   games.single_player.towers_of_hanoi.base.P
   games.single_player.towers_of_hanoi.base.PegNumber
   games.single_player.towers_of_hanoi.base.S


Classes
-------

.. autoapisummary::

   games.single_player.towers_of_hanoi.base.Disk
   games.single_player.towers_of_hanoi.base.Game
   games.single_player.towers_of_hanoi.base.GameStatus
   games.single_player.towers_of_hanoi.base.HanoiBoard
   games.single_player.towers_of_hanoi.base.HanoiGame
   games.single_player.towers_of_hanoi.base.HanoiMove
   games.single_player.towers_of_hanoi.base.HanoiSolver
   games.single_player.towers_of_hanoi.base.Peg
   games.single_player.towers_of_hanoi.base.PegPosition
   games.single_player.towers_of_hanoi.base.PegSpace


Module Contents
---------------

.. py:class:: Disk

   Bases: :py:obj:`haive.games.framework.core.piece.GamePiece`\ [\ :py:obj:`PegPosition`\ ]


   A disk in the Tower of Hanoi game.


   .. autolink-examples:: Disk
      :collapse:

   .. py:method:: _is_top_disk(board: HanoiBoard) -> bool

      Check if this disk is the top disk on its peg.


      .. autolink-examples:: _is_top_disk
         :collapse:


   .. py:method:: can_move_to(position: PegPosition, board: HanoiBoard) -> bool

      Check if this disk can be moved to the specified position.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:method:: validate_size(v: int) -> int
      :classmethod:


      Ensure size is positive.


      .. autolink-examples:: validate_size
         :collapse:


   .. py:attribute:: color
      :type:  str | None
      :value: None



   .. py:attribute:: size
      :type:  int


.. py:class:: Game(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`re.T`\ ]


   Base class for all games.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Game
      :collapse:

   .. py:method:: end_game() -> None

      End the game.


      .. autolink-examples:: end_game
         :collapse:


   .. py:method:: is_valid_move(move: dict[str, any]) -> bool

      Check if a move is valid.


      .. autolink-examples:: is_valid_move
         :collapse:


   .. py:method:: make_move(move: dict[str, any]) -> bool

      Make a move in the game.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: reset() -> None

      Reset the game to initial state.


      .. autolink-examples:: reset
         :collapse:


   .. py:method:: start_game() -> None

      Start the game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: board
      :type:  haive.games.framework.core.board.Board


   .. py:attribute:: current_player_id
      :type:  str | None
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:property:: move_count
      :type: int


      Get the number of moves made so far.

      .. autolink-examples:: move_count
         :collapse:


   .. py:attribute:: moves
      :type:  list[dict[str, any]]
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: players
      :type:  list[str]
      :value: None



   .. py:attribute:: status
      :type:  str
      :value: 'not_started'



.. py:class:: GameStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Status of a Tower of Hanoi game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GameStatus
      :collapse:

   .. py:attribute:: COMPLETED
      :value: 'completed'



   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'



   .. py:attribute:: NOT_STARTED
      :value: 'not_started'



.. py:class:: HanoiBoard

   Bases: :py:obj:`haive.games.framework.core.board.Board`\ [\ :py:obj:`PegSpace`\ [\ :py:obj:`Disk`\ ]\ , :py:obj:`PegPosition`\ , :py:obj:`Disk`\ ]


   A Tower of Hanoi board with pegs and disks.


   .. autolink-examples:: HanoiBoard
      :collapse:

   .. py:method:: get_peg_disks(peg: PegNumber) -> list[Disk]

      Get all disks on a specific peg, from bottom to top.


      .. autolink-examples:: get_peg_disks
         :collapse:


   .. py:method:: get_peg_spaces(peg: PegNumber) -> list[PegSpace[Disk]]

      Get all spaces on a specific peg.


      .. autolink-examples:: get_peg_spaces
         :collapse:


   .. py:method:: get_space_at_position(position: PegPosition) -> PegSpace[Disk] | None

      Get the space at the specified peg position.


      .. autolink-examples:: get_space_at_position
         :collapse:


   .. py:method:: get_top_disk(peg: PegNumber) -> Disk | None

      Get the top disk on a specific peg.


      .. autolink-examples:: get_top_disk
         :collapse:


   .. py:method:: get_top_level(peg: PegNumber) -> int

      Get the level of the top occupied space on a peg.


      .. autolink-examples:: get_top_level
         :collapse:


   .. py:method:: initialize_board() -> None

      Initialize the Tower of Hanoi board with all disks on the first peg.


      .. autolink-examples:: initialize_board
         :collapse:


   .. py:method:: move_disk(from_peg: PegNumber, to_peg: PegNumber) -> bool

      Move the top disk from one peg to another.


      .. autolink-examples:: move_disk
         :collapse:


   .. py:method:: validate_num_disks(v: int) -> int
      :classmethod:


      Ensure there's at least one disk.


      .. autolink-examples:: validate_num_disks
         :collapse:


   .. py:property:: is_solved
      :type: bool


      Check if all disks have been moved to the final peg.

      .. autolink-examples:: is_solved
         :collapse:


   .. py:attribute:: num_disks
      :type:  int


   .. py:attribute:: num_pegs
      :type:  Literal[3]
      :value: 3



.. py:class:: HanoiGame

   Bases: :py:obj:`Game`\ [\ :py:obj:`PegPosition`\ , :py:obj:`Disk`\ ]


   Tower of Hanoi game, extending the base Game class.


   .. autolink-examples:: HanoiGame
      :collapse:

   .. py:method:: calculate_min_moves() -> HanoiGame

      Calculate the minimum number of moves to solve the puzzle.


      .. autolink-examples:: calculate_min_moves
         :collapse:


   .. py:method:: is_valid_move(move: dict[str, any]) -> bool

      Check if a move is valid according to Tower of Hanoi rules.


      .. autolink-examples:: is_valid_move
         :collapse:


   .. py:method:: make_move(move: dict[str, any]) -> bool

      Make a move in the Tower of Hanoi game.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: move_disk(from_peg: PegNumber, to_peg: PegNumber) -> bool

      Move disk from one peg to another (convenience method).


      .. autolink-examples:: move_disk
         :collapse:


   .. py:method:: reset() -> None

      Reset the game to the initial state.


      .. autolink-examples:: reset
         :collapse:


   .. py:method:: start_game() -> None

      Start a new game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: board
      :type:  HanoiBoard


   .. py:property:: is_optimal
      :type: bool


      Check if the solution is optimal (using minimum moves).

      .. autolink-examples:: is_optimal
         :collapse:


   .. py:attribute:: min_moves
      :type:  int
      :value: 0



   .. py:attribute:: status
      :type:  GameStatus


.. py:class:: HanoiMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a move in Tower of Hanoi.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HanoiMove
      :collapse:

   .. py:method:: validate_different_pegs(v: PegNumber, info: Any) -> PegNumber
      :classmethod:


      Validate that source and destination pegs are different.


      .. autolink-examples:: validate_different_pegs
         :collapse:


   .. py:attribute:: from_peg
      :type:  PegNumber


   .. py:attribute:: to_peg
      :type:  PegNumber


.. py:class:: HanoiSolver(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Solver for Tower of Hanoi puzzles.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HanoiSolver
      :collapse:

   .. py:method:: solve(num_disks: int) -> list[HanoiMove]
      :staticmethod:


      Generate the optimal solution sequence.


      .. autolink-examples:: solve
         :collapse:


.. py:class:: Peg

   Bases: :py:obj:`haive.games.framework.core.container.GamePieceContainer`\ [\ :py:obj:`Disk`\ ]


   A peg in Tower of Hanoi that contains disks.


   .. autolink-examples:: Peg
      :collapse:

   .. py:method:: add_disk(disk: Disk, validate: bool = True) -> bool

      Add a disk to this peg if valid.


      .. autolink-examples:: add_disk
         :collapse:


   .. py:method:: remove_top_disk() -> Disk | None

      Remove and return the top disk.


      .. autolink-examples:: remove_top_disk
         :collapse:


   .. py:attribute:: max_disks
      :type:  int


   .. py:attribute:: peg_number
      :type:  PegNumber


   .. py:property:: top_disk
      :type: Disk | None


      Get the top disk without removing it.

      .. autolink-examples:: top_disk
         :collapse:


.. py:class:: PegPosition

   Bases: :py:obj:`haive.games.framework.core.position.Position`


   Position on a Tower of Hanoi peg.


   .. autolink-examples:: PegPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: validate_level(v: int) -> int
      :classmethod:


      Ensure level is valid.


      .. autolink-examples:: validate_level
         :collapse:


   .. py:property:: display_coords
      :type: str


      Return human-readable coordinates.

      .. autolink-examples:: display_coords
         :collapse:


   .. py:attribute:: level
      :type:  int


   .. py:attribute:: peg
      :type:  PegNumber


.. py:class:: PegSpace

   Bases: :py:obj:`haive.games.framework.core.space.Space`\ [\ :py:obj:`PegPosition`\ , :py:obj:`Disk`\ ]


   A space on a Tower of Hanoi peg.


   .. autolink-examples:: PegSpace
      :collapse:

   .. py:method:: is_valid_for_disk(disk: Disk) -> bool

      Check if a disk can be placed on this space.


      .. autolink-examples:: is_valid_for_disk
         :collapse:


   .. py:property:: level
      :type: int


      Get the level of this space.

      .. autolink-examples:: level
         :collapse:


   .. py:property:: peg_number
      :type: PegNumber


      Get the peg number this space is on.

      .. autolink-examples:: peg_number
         :collapse:


   .. py:attribute:: position
      :type:  PegPosition


.. py:data:: D

.. py:data:: P

.. py:data:: PegNumber

.. py:data:: S

