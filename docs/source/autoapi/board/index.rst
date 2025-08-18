board
=====

.. py:module:: board

Module documentation for board


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      board.CrosswordBoard

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CrosswordBoard

            Bases: :py:obj:`GridBoard`\ [\ :py:obj:`CrosswordCell`\ [\ :py:obj:`CrosswordLetter`\ ]\ , :py:obj:`GridPosition`\ , :py:obj:`CrosswordLetter`\ ]


            A crossword puzzle board.


            .. py:method:: _get_word_positions(word: str, start_position: GridPosition, direction: Direction) -> list[GridPosition]

               Calculate the positions for each letter of a word.



            .. py:method:: _validate_word_placement(word: str, start_position: GridPosition, direction: Direction) -> bool

               Check if a word can be placed at the specified position.



            .. py:method:: add_clue(number: int, direction: Direction, text: str, answer: str, start_position: GridPosition) -> str | None

               Add a clue to the crossword.



            .. py:method:: check_letter(position: GridPosition) -> bool

               Check if the letter at a position is correct.



            .. py:method:: enter_letter(position: GridPosition, letter: str, is_filled: bool = True) -> bool

               Enter a letter in a cell.



            .. py:method:: initialize_grid() -> None

               Initialize an empty crossword grid.



            .. py:method:: set_cell_type(position: GridPosition, cell_type: CellType) -> bool

               Set the type of a cell.



            .. py:attribute:: clues
               :type:  dict[str, CrosswordClue]
               :value: None



            .. py:property:: is_complete
               :type: bool


               Check if the crossword is complete and correct.


            .. py:attribute:: words
               :type:  dict[str, CrosswordWord]
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from board import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

