games.single_player.crossword_puzzle.base
=========================================

.. py:module:: games.single_player.crossword_puzzle.base

Module documentation for games.single_player.crossword_puzzle.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">7 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.single_player.crossword_puzzle.base.CellType

            
            

.. admonition:: Classes (7)
   :class: note

   .. autoapisummary::

      games.single_player.crossword_puzzle.base.CrosswordCell
      games.single_player.crossword_puzzle.base.CrosswordClue
      games.single_player.crossword_puzzle.base.CrosswordGame
      games.single_player.crossword_puzzle.base.CrosswordMove
      games.single_player.crossword_puzzle.base.CrosswordTemplate
      games.single_player.crossword_puzzle.base.CrosswordWord
      games.single_player.crossword_puzzle.base.Direction

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordCell

            Bases: :py:obj:`game_framework_base.GridSpace`\ [\ :py:obj:`CrosswordLetter`\ ]


            A cell in a crossword puzzle.


            .. py:attribute:: cell_type
               :type:  CellType
               :value: 'empty'



            .. py:property:: current_letter
               :type: str | None


               Get the current letter in this cell, if any.


            .. py:property:: is_block
               :type: bool


               Check if this cell is a block (black square).


            .. py:property:: is_filled
               :type: bool


               Check if this cell has been filled by the player.


            .. py:property:: is_letter_cell
               :type: bool


               Check if this cell can contain a letter.


            .. py:attribute:: number
               :type:  int | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordClue(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A clue in a crossword puzzle.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_answer(v: str) -> str
               :classmethod:


               Ensure answer contains only letters and matches the length.



            .. py:attribute:: answer
               :type:  str


            .. py:attribute:: direction
               :type:  Direction


            .. py:property:: end_position
               :type: game_framework_base.GridPosition


               Calculate the ending position of the word.


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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordGame

            Bases: :py:obj:`game_framework_base.Game`\ [\ :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`CrosswordLetter`\ ]


            Crossword puzzle game controller.


            .. py:method:: check_all() -> dict[str, bool]

               Check all filled letters against the solution.



            .. py:method:: check_word(clue_id: str) -> bool

               Check if a word is filled in correctly.



            .. py:method:: is_valid_move(move: CrosswordMove | dict[str, any]) -> bool

               Check if a move is valid.



            .. py:method:: make_move(move: CrosswordMove | dict[str, any]) -> bool

               Make a move in the game.



            .. py:method:: reset() -> None

               Reset the game.



            .. py:method:: reveal_letter(position: game_framework_base.GridPosition) -> bool

               Reveal the correct letter at a position.



            .. py:method:: reveal_word(clue_id: str) -> bool

               Reveal all letters in a word.



            .. py:method:: select_cell(position: game_framework_base.GridPosition) -> bool

               Select a cell.



            .. py:method:: start_game() -> None

               Start the game.



            .. py:attribute:: board
               :type:  CrosswordBoard


            .. py:attribute:: check_as_you_type
               :type:  bool
               :value: False



            .. py:attribute:: selected_position
               :type:  game_framework_base.GridPosition | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A move in a crossword puzzle.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: letter
               :type:  str


            .. py:attribute:: position
               :type:  game_framework_base.GridPosition



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordTemplate(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A pre-defined crossword template.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: create_game() -> CrosswordGame

               Create a game from this template.



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



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordWord(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            A word placement in a crossword puzzle.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_word() -> CrosswordWord

               Ensure the word's length matches positions and letters.



            .. py:attribute:: clue
               :type:  CrosswordClue


            .. py:attribute:: letters
               :type:  list[str]


            .. py:attribute:: positions
               :type:  list[game_framework_base.GridPosition]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Direction

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Direction of a word in a crossword.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ACROSS
               :value: 'across'



            .. py:attribute:: DOWN
               :value: 'down'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: CellType




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.crossword_puzzle.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

