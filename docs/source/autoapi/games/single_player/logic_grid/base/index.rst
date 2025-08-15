games.single_player.logic_grid.base
===================================

.. py:module:: games.single_player.logic_grid.base


Classes
-------

.. autoapisummary::

   games.single_player.logic_grid.base.ClueType
   games.single_player.logic_grid.base.LogicGrid
   games.single_player.logic_grid.base.LogicGridClue
   games.single_player.logic_grid.base.LogicGridMark
   games.single_player.logic_grid.base.LogicGridMove
   games.single_player.logic_grid.base.LogicGridPosition
   games.single_player.logic_grid.base.LogicGridPuzzle
   games.single_player.logic_grid.base.LogicGridPuzzleDefinition
   games.single_player.logic_grid.base.LogicGridSpace
   games.single_player.logic_grid.base.MarkType


Module Contents
---------------

.. py:class:: ClueType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of clues in a logic grid puzzle.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ClueType
      :collapse:

   .. py:attribute:: CUSTOM
      :value: 'custom'



   .. py:attribute:: DIRECT_MATCH
      :value: 'direct_match'



   .. py:attribute:: DIRECT_NONMATCH
      :value: 'direct_nonmatch'



   .. py:attribute:: ORDERING
      :value: 'ordering'



   .. py:attribute:: RELATIVE
      :value: 'relative'



.. py:class:: LogicGrid

   Bases: :py:obj:`game_framework_base.Board`\ [\ :py:obj:`LogicGridSpace`\ [\ :py:obj:`LogicGridMark`\ ]\ , :py:obj:`LogicGridPosition`\ , :py:obj:`LogicGridMark`\ ]


   A logic grid board.


   .. autolink-examples:: LogicGrid
      :collapse:

   .. py:method:: get_category_index(category: str) -> int

      Get the index of a category.


      .. autolink-examples:: get_category_index
         :collapse:


   .. py:method:: get_grid_for_categories(category1: str, category2: str) -> list[list[MarkType]]

      Get the grid of marks for a pair of categories.


      .. autolink-examples:: get_grid_for_categories
         :collapse:


   .. py:method:: get_space_at_position(position: LogicGridPosition) -> LogicGridSpace[LogicGridMark] | None

      Get the space at the specified position.


      .. autolink-examples:: get_space_at_position
         :collapse:


   .. py:method:: initialize_grid() -> None

      Initialize the grid with empty spaces.


      .. autolink-examples:: initialize_grid
         :collapse:


   .. py:method:: set_mark(position: LogicGridPosition, mark_type: MarkType) -> bool

      Set a mark at the specified position.


      .. autolink-examples:: set_mark
         :collapse:


   .. py:attribute:: categories
      :type:  list[str]


   .. py:attribute:: category_items
      :type:  list[list[str]]


   .. py:attribute:: category_sizes
      :type:  list[int]


   .. py:property:: is_solved
      :type: bool


      Check if the puzzle is solved.

      .. autolink-examples:: is_solved
         :collapse:


   .. py:attribute:: relations
      :type:  dict[str, dict[str, list[LogicGridSpace[LogicGridMark]]]]
      :value: None



.. py:class:: LogicGridClue(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A clue in a logic grid puzzle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LogicGridClue
      :collapse:

   .. py:method:: apply_to_grid(grid: LogicGrid) -> bool

      Apply this clue to the grid.


      .. autolink-examples:: apply_to_grid
         :collapse:


   .. py:method:: validate_clue() -> LogicGridClue

      Validate the clue based on its type.


      .. autolink-examples:: validate_clue
         :collapse:


   .. py:attribute:: categories
      :type:  list[str]


   .. py:attribute:: clue_type
      :type:  ClueType


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: items
      :type:  list[list[int]]


   .. py:attribute:: text
      :type:  str


.. py:class:: LogicGridMark

   Bases: :py:obj:`game_framework_base.GamePiece`\ [\ :py:obj:`LogicGridPosition`\ ]


   A mark in a logic grid.


   .. autolink-examples:: LogicGridMark
      :collapse:

   .. py:method:: can_move_to(position: LogicGridPosition, board: game_framework_base.Board) -> bool

      Marks can be placed on any empty space.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:attribute:: mark_type
      :type:  MarkType


.. py:class:: LogicGridMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A move in a Logic Grid puzzle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LogicGridMove
      :collapse:

   .. py:attribute:: mark_type
      :type:  MarkType


   .. py:attribute:: position
      :type:  LogicGridPosition


.. py:class:: LogicGridPosition

   Bases: :py:obj:`game_framework_base.Position`


   Position in a logic grid.


   .. autolink-examples:: LogicGridPosition
      :collapse:

   .. py:method:: __eq__(other: object) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: validate_indices(v: int) -> int
      :classmethod:


      Ensure indices are non-negative.


      .. autolink-examples:: validate_indices
         :collapse:


   .. py:attribute:: category1_index
      :type:  int


   .. py:attribute:: category2_index
      :type:  int


   .. py:property:: display_coords
      :type: str


      Return human-readable coordinates.

      .. autolink-examples:: display_coords
         :collapse:


.. py:class:: LogicGridPuzzle

   Bases: :py:obj:`game_framework_base.Game`\ [\ :py:obj:`LogicGridPosition`\ , :py:obj:`LogicGridMark`\ ]


   Logic Grid puzzle game controller.


   .. autolink-examples:: LogicGridPuzzle
      :collapse:

   .. py:method:: add_clue(clue: LogicGridClue) -> None

      Add a clue to the puzzle.


      .. autolink-examples:: add_clue
         :collapse:


   .. py:method:: apply_clues() -> None

      Apply all clues to the grid.


      .. autolink-examples:: apply_clues
         :collapse:


   .. py:method:: is_valid_move(move: LogicGridMove) -> bool

      Check if a move is valid.


      .. autolink-examples:: is_valid_move
         :collapse:


   .. py:method:: make_move(move: LogicGridMove) -> bool

      Make a move in the game.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: propagate_constraints() -> int

      Propagate constraints from currently placed marks.


      .. autolink-examples:: propagate_constraints
         :collapse:


   .. py:method:: reset() -> None

      Reset the game.


      .. autolink-examples:: reset
         :collapse:


   .. py:method:: start_game() -> None

      Start the game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: board
      :type:  LogicGrid


   .. py:attribute:: clues
      :type:  list[LogicGridClue]
      :value: None



.. py:class:: LogicGridPuzzleDefinition(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Definition of a logic grid puzzle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: LogicGridPuzzleDefinition
      :collapse:

   .. py:method:: create_game() -> LogicGridPuzzle

      Create a game from this definition.


      .. autolink-examples:: create_game
         :collapse:


   .. py:attribute:: categories
      :type:  list[str]


   .. py:attribute:: category_items
      :type:  list[list[str]]


   .. py:attribute:: clues
      :type:  list[dict[str, any]]


   .. py:attribute:: name
      :type:  str


.. py:class:: LogicGridSpace

   Bases: :py:obj:`game_framework_base.Space`\ [\ :py:obj:`LogicGridPosition`\ , :py:obj:`LogicGridMark`\ ]


   A cell in a logic grid.


   .. autolink-examples:: LogicGridSpace
      :collapse:

   .. py:property:: mark_type
      :type: MarkType


      Get the type of mark in this space.

      .. autolink-examples:: mark_type
         :collapse:


   .. py:attribute:: position
      :type:  LogicGridPosition


.. py:class:: MarkType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Types of marks in a logic grid.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MarkType
      :collapse:

   .. py:attribute:: NO
      :value: 'no'



   .. py:attribute:: NONE
      :value: 'none'



   .. py:attribute:: YES
      :value: 'yes'



