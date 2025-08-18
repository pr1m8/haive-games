games.single_player.towers_of_hanoi.base
========================================

.. py:module:: games.single_player.towers_of_hanoi.base

Module documentation for games.single_player.towers_of_hanoi.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">10 classes</span> • <span class="module-stat">4 attributes</span>   </div>


      

.. admonition:: Attributes (4)
   :class: tip

   .. autoapisummary::

      games.single_player.towers_of_hanoi.base.D
      games.single_player.towers_of_hanoi.base.P
      games.single_player.towers_of_hanoi.base.PegNumber
      games.single_player.towers_of_hanoi.base.S

            
            

.. admonition:: Classes (10)
   :class: note

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

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Disk

            Bases: :py:obj:`haive.games.framework.core.piece.GamePiece`\ [\ :py:obj:`PegPosition`\ ]


            A disk in the Tower of Hanoi game.


            .. py:method:: _is_top_disk(board: HanoiBoard) -> bool

               Check if this disk is the top disk on its peg.



            .. py:method:: can_move_to(position: PegPosition, board: HanoiBoard) -> bool

               Check if this disk can be moved to the specified position.



            .. py:method:: validate_size(v: int) -> int
               :classmethod:


               Ensure size is positive.



            .. py:attribute:: color
               :type:  str | None
               :value: None



            .. py:attribute:: size
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Game(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`re.T`\ ]


            Base class for all games.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: end_game() -> None

               End the game.



            .. py:method:: is_valid_move(move: dict[str, any]) -> bool

               Check if a move is valid.



            .. py:method:: make_move(move: dict[str, any]) -> bool

               Make a move in the game.



            .. py:method:: reset() -> None

               Reset the game to initial state.



            .. py:method:: start_game() -> None

               Start the game.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GameStatus

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Status of a Tower of Hanoi game.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: COMPLETED
               :value: 'completed'



            .. py:attribute:: IN_PROGRESS
               :value: 'in_progress'



            .. py:attribute:: NOT_STARTED
               :value: 'not_started'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HanoiBoard

            Bases: :py:obj:`haive.games.framework.core.board.Board`\ [\ :py:obj:`PegSpace`\ [\ :py:obj:`Disk`\ ]\ , :py:obj:`PegPosition`\ , :py:obj:`Disk`\ ]


            A Tower of Hanoi board with pegs and disks.


            .. py:method:: get_peg_disks(peg: PegNumber) -> list[Disk]

               Get all disks on a specific peg, from bottom to top.



            .. py:method:: get_peg_spaces(peg: PegNumber) -> list[PegSpace[Disk]]

               Get all spaces on a specific peg.



            .. py:method:: get_space_at_position(position: PegPosition) -> PegSpace[Disk] | None

               Get the space at the specified peg position.



            .. py:method:: get_top_disk(peg: PegNumber) -> Disk | None

               Get the top disk on a specific peg.



            .. py:method:: get_top_level(peg: PegNumber) -> int

               Get the level of the top occupied space on a peg.



            .. py:method:: initialize_board() -> None

               Initialize the Tower of Hanoi board with all disks on the first peg.



            .. py:method:: move_disk(from_peg: PegNumber, to_peg: PegNumber) -> bool

               Move the top disk from one peg to another.



            .. py:method:: validate_num_disks(v: int) -> int
               :classmethod:


               Ensure there's at least one disk.



            .. py:property:: is_solved
               :type: bool


               Check if all disks have been moved to the final peg.


            .. py:attribute:: num_disks
               :type:  int


            .. py:attribute:: num_pegs
               :type:  Literal[3]
               :value: 3




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HanoiGame

            Bases: :py:obj:`Game`\ [\ :py:obj:`PegPosition`\ , :py:obj:`Disk`\ ]


            Tower of Hanoi game, extending the base Game class.


            .. py:method:: calculate_min_moves() -> HanoiGame

               Calculate the minimum number of moves to solve the puzzle.



            .. py:method:: is_valid_move(move: dict[str, any]) -> bool

               Check if a move is valid according to Tower of Hanoi rules.



            .. py:method:: make_move(move: dict[str, any]) -> bool

               Make a move in the Tower of Hanoi game.



            .. py:method:: move_disk(from_peg: PegNumber, to_peg: PegNumber) -> bool

               Move disk from one peg to another (convenience method).



            .. py:method:: reset() -> None

               Reset the game to the initial state.



            .. py:method:: start_game() -> None

               Start a new game.



            .. py:attribute:: board
               :type:  HanoiBoard


            .. py:property:: is_optimal
               :type: bool


               Check if the solution is optimal (using minimum moves).


            .. py:attribute:: min_moves
               :type:  int
               :value: 0



            .. py:attribute:: status
               :type:  GameStatus



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HanoiMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a move in Tower of Hanoi.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_different_pegs(v: PegNumber, info: Any) -> PegNumber
               :classmethod:


               Validate that source and destination pegs are different.



            .. py:attribute:: from_peg
               :type:  PegNumber


            .. py:attribute:: to_peg
               :type:  PegNumber



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HanoiSolver(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Solver for Tower of Hanoi puzzles.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: solve(num_disks: int) -> list[HanoiMove]
               :staticmethod:


               Generate the optimal solution sequence.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Peg

            Bases: :py:obj:`haive.games.framework.core.container.GamePieceContainer`\ [\ :py:obj:`Disk`\ ]


            A peg in Tower of Hanoi that contains disks.


            .. py:method:: add_disk(disk: Disk, validate: bool = True) -> bool

               Add a disk to this peg if valid.



            .. py:method:: remove_top_disk() -> Disk | None

               Remove and return the top disk.



            .. py:attribute:: max_disks
               :type:  int


            .. py:attribute:: peg_number
               :type:  PegNumber


            .. py:property:: top_disk
               :type: Disk | None


               Get the top disk without removing it.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PegPosition(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.core.position.Position`


            Position on a Tower of Hanoi peg.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __eq__(other: object) -> bool

               Equality check must be implemented by subclasses.

               The base implementation just checks if the IDs match.




            .. py:method:: __hash__() -> int

               Hash implementation must be consistent with __eq__.

               The base implementation uses the ID.




            .. py:method:: validate_level(v: int) -> int
               :classmethod:


               Ensure level is valid.



            .. py:property:: display_coords
               :type: str


               Return human-readable coordinates.


            .. py:attribute:: level
               :type:  int


            .. py:attribute:: peg
               :type:  PegNumber



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PegSpace

            Bases: :py:obj:`haive.games.framework.core.space.Space`\ [\ :py:obj:`PegPosition`\ , :py:obj:`Disk`\ ]


            A space on a Tower of Hanoi peg.


            .. py:method:: is_valid_for_disk(disk: Disk) -> bool

               Check if a disk can be placed on this space.



            .. py:property:: level
               :type: int


               Get the level of this space.


            .. py:property:: peg_number
               :type: PegNumber


               Get the peg number this space is on.


            .. py:attribute:: position
               :type:  PegPosition



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: D


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: P


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: PegNumber


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: S




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.towers_of_hanoi.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

