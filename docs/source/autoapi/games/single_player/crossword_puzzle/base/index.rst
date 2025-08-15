games.single_player.crossword_puzzle.base
=========================================

.. py:module:: games.single_player.crossword_puzzle.base


Attributes
----------

.. autoapisummary::

   games.single_player.crossword_puzzle.base.CellType


Classes
-------

.. autoapisummary::

   games.single_player.crossword_puzzle.base.CrosswordCell
   games.single_player.crossword_puzzle.base.CrosswordClue
   games.single_player.crossword_puzzle.base.CrosswordGame
   games.single_player.crossword_puzzle.base.CrosswordMove
   games.single_player.crossword_puzzle.base.CrosswordTemplate
   games.single_player.crossword_puzzle.base.CrosswordWord
   games.single_player.crossword_puzzle.base.Direction


Module Contents
---------------

.. py:class:: CrosswordCell

   Bases: :py:obj:`game_framework_base.GridSpace`\ [\ :py:obj:`CrosswordLetter`\ ]


   A cell in a crossword puzzle.


   .. autolink-examples:: CrosswordCell
      :collapse:

   .. py:attribute:: cell_type
      :type:  CellType
      :value: 'empty'



   .. py:property:: current_letter
      :type: str | None


      Get the current letter in this cell, if any.

      .. autolink-examples:: current_letter
         :collapse:


   .. py:property:: is_block
      :type: bool


      Check if this cell is a block (black square).

      .. autolink-examples:: is_block
         :collapse:


   .. py:property:: is_filled
      :type: bool


      Check if this cell has been filled by the player.

      .. autolink-examples:: is_filled
         :collapse:


   .. py:property:: is_letter_cell
      :type: bool


      Check if this cell can contain a letter.

      .. autolink-examples:: is_letter_cell
         :collapse:


   .. py:attribute:: number
      :type:  int | None
      :value: None



.. py:class:: CrosswordClue(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A clue in a crossword puzzle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CrosswordClue
      :collapse:

   .. py:method:: validate_answer(v: str) -> str
      :classmethod:


      Ensure answer contains only letters and matches the length.


      .. autolink-examples:: validate_answer
         :collapse:


   .. py:attribute:: answer
      :type:  str


   .. py:attribute:: direction
      :type:  Direction


   .. py:property:: end_position
      :type: game_framework_base.GridPosition


      Calculate the ending position of the word.

      .. autolink-examples:: end_position
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: length
      :type:  int


   .. py:attribute:: number
      :type:  int


   .. py:attribute:: start_position
      :type:  game_framework_base.GridPosition


   .. py:attribute:: text
      :type:  str


.. py:class:: CrosswordGame

   Bases: :py:obj:`game_framework_base.Game`\ [\ :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`CrosswordLetter`\ ]


   Crossword puzzle game controller.


   .. autolink-examples:: CrosswordGame
      :collapse:

   .. py:method:: check_all() -> dict[str, bool]

      Check all filled letters against the solution.


      .. autolink-examples:: check_all
         :collapse:


   .. py:method:: check_word(clue_id: str) -> bool

      Check if a word is filled in correctly.


      .. autolink-examples:: check_word
         :collapse:


   .. py:method:: is_valid_move(move: CrosswordMove | dict[str, any]) -> bool

      Check if a move is valid.


      .. autolink-examples:: is_valid_move
         :collapse:


   .. py:method:: make_move(move: CrosswordMove | dict[str, any]) -> bool

      Make a move in the game.


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: reset() -> None

      Reset the game.


      .. autolink-examples:: reset
         :collapse:


   .. py:method:: reveal_letter(position: game_framework_base.GridPosition) -> bool

      Reveal the correct letter at a position.


      .. autolink-examples:: reveal_letter
         :collapse:


   .. py:method:: reveal_word(clue_id: str) -> bool

      Reveal all letters in a word.


      .. autolink-examples:: reveal_word
         :collapse:


   .. py:method:: select_cell(position: game_framework_base.GridPosition) -> bool

      Select a cell.


      .. autolink-examples:: select_cell
         :collapse:


   .. py:method:: start_game() -> None

      Start the game.


      .. autolink-examples:: start_game
         :collapse:


   .. py:attribute:: board
      :type:  CrosswordBoard


   .. py:attribute:: check_as_you_type
      :type:  bool
      :value: False



   .. py:attribute:: selected_position
      :type:  game_framework_base.GridPosition | None
      :value: None



.. py:class:: CrosswordMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A move in a crossword puzzle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CrosswordMove
      :collapse:

   .. py:attribute:: letter
      :type:  str


   .. py:attribute:: position
      :type:  game_framework_base.GridPosition


.. py:class:: CrosswordTemplate(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A pre-defined crossword template.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CrosswordTemplate
      :collapse:

   .. py:method:: create_game() -> CrosswordGame

      Create a game from this template.


      .. autolink-examples:: create_game
         :collapse:


   .. py:attribute:: block_positions
      :type:  list[tuple[int, int]]


   .. py:attribute:: clues
      :type:  list[dict[str, any]]


   .. py:attribute:: cols
      :type:  int


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: rows
      :type:  int


.. py:class:: CrosswordWord(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A word placement in a crossword puzzle.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CrosswordWord
      :collapse:

   .. py:method:: validate_word() -> CrosswordWord

      Ensure the word's length matches positions and letters.


      .. autolink-examples:: validate_word
         :collapse:


   .. py:attribute:: clue
      :type:  CrosswordClue


   .. py:attribute:: letters
      :type:  list[str]


   .. py:attribute:: positions
      :type:  list[game_framework_base.GridPosition]


.. py:class:: Direction

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Direction of a word in a crossword.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Direction
      :collapse:

   .. py:attribute:: ACROSS
      :value: 'across'



   .. py:attribute:: DOWN
      :value: 'down'



.. py:data:: CellType

