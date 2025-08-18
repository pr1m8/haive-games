games.single_player.logic_grid.base
===================================

.. py:module:: games.single_player.logic_grid.base

Module documentation for games.single_player.logic_grid.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">10 classes</span>   </div>


      
            
            

.. admonition:: Classes (10)
   :class: note

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

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ClueType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of clues in a logic grid puzzle.

            Initialize self.  See help(type(self)) for accurate signature.


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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGrid

            Bases: :py:obj:`game_framework_base.Board`\ [\ :py:obj:`LogicGridSpace`\ [\ :py:obj:`LogicGridMark`\ ]\ , :py:obj:`LogicGridPosition`\ , :py:obj:`LogicGridMark`\ ]


            A logic grid board.


            .. py:method:: get_category_index(category: str) -> int

               Get the index of a category.



            .. py:method:: get_grid_for_categories(category1: str, category2: str) -> list[list[MarkType]]

               Get the grid of marks for a pair of categories.



            .. py:method:: get_space_at_position(position: LogicGridPosition) -> LogicGridSpace[LogicGridMark] | None

               Get the space at the specified position.



            .. py:method:: initialize_grid() -> None

               Initialize the grid with empty spaces.



            .. py:method:: set_mark(position: LogicGridPosition, mark_type: MarkType) -> bool

               Set a mark at the specified position.



            .. py:attribute:: categories
               :type:  list[str]


            .. py:attribute:: category_items
               :type:  list[list[str]]


            .. py:attribute:: category_sizes
               :type:  list[int]


            .. py:property:: is_solved
               :type: bool


               Check if the puzzle is solved.


            .. py:attribute:: relations
               :type:  dict[str, dict[str, list[LogicGridSpace[LogicGridMark]]]]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridClue(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A clue in a logic grid puzzle.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: apply_to_grid(grid: LogicGrid) -> bool

               Apply this clue to the grid.



            .. py:method:: validate_clue() -> LogicGridClue

               Validate the clue based on its type.



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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridMark

            Bases: :py:obj:`game_framework_base.GamePiece`\ [\ :py:obj:`LogicGridPosition`\ ]


            A mark in a logic grid.


            .. py:method:: can_move_to(position: LogicGridPosition, board: game_framework_base.Board) -> bool

               Marks can be placed on any empty space.



            .. py:attribute:: mark_type
               :type:  MarkType



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A move in a Logic Grid puzzle.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: mark_type
               :type:  MarkType


            .. py:attribute:: position
               :type:  LogicGridPosition



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridPosition

            Bases: :py:obj:`game_framework_base.Position`


            Position in a logic grid.


            .. py:method:: __eq__(other: object) -> bool


            .. py:method:: __hash__() -> int


            .. py:method:: validate_indices(v: int) -> int
               :classmethod:


               Ensure indices are non-negative.



            .. py:attribute:: category1_index
               :type:  int


            .. py:attribute:: category2_index
               :type:  int


            .. py:property:: display_coords
               :type: str


               Return human-readable coordinates.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridPuzzle

            Bases: :py:obj:`game_framework_base.Game`\ [\ :py:obj:`LogicGridPosition`\ , :py:obj:`LogicGridMark`\ ]


            Logic Grid puzzle game controller.


            .. py:method:: add_clue(clue: LogicGridClue) -> None

               Add a clue to the puzzle.



            .. py:method:: apply_clues() -> None

               Apply all clues to the grid.



            .. py:method:: is_valid_move(move: LogicGridMove) -> bool

               Check if a move is valid.



            .. py:method:: make_move(move: LogicGridMove) -> bool

               Make a move in the game.



            .. py:method:: propagate_constraints() -> int

               Propagate constraints from currently placed marks.



            .. py:method:: reset() -> None

               Reset the game.



            .. py:method:: start_game() -> None

               Start the game.



            .. py:attribute:: board
               :type:  LogicGrid


            .. py:attribute:: clues
               :type:  list[LogicGridClue]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridPuzzleDefinition(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Definition of a logic grid puzzle.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: create_game() -> LogicGridPuzzle

               Create a game from this definition.



            .. py:attribute:: categories
               :type:  list[str]


            .. py:attribute:: category_items
               :type:  list[list[str]]


            .. py:attribute:: clues
               :type:  list[dict[str, any]]


            .. py:attribute:: name
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: LogicGridSpace

            Bases: :py:obj:`game_framework_base.Space`\ [\ :py:obj:`LogicGridPosition`\ , :py:obj:`LogicGridMark`\ ]


            A cell in a logic grid.


            .. py:property:: mark_type
               :type: MarkType


               Get the type of mark in this space.


            .. py:attribute:: position
               :type:  LogicGridPosition



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MarkType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of marks in a logic grid.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: NO
               :value: 'no'



            .. py:attribute:: NONE
               :value: 'none'



            .. py:attribute:: YES
               :value: 'yes'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.logic_grid.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

