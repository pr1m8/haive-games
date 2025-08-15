board
=====

.. py:module:: board


Classes
-------

.. autoapisummary::

   board.CrosswordBoard


Module Contents
---------------

.. py:class:: CrosswordBoard

   Bases: :py:obj:`GridBoard`\ [\ :py:obj:`CrosswordCell`\ [\ :py:obj:`CrosswordLetter`\ ]\ , :py:obj:`GridPosition`\ , :py:obj:`CrosswordLetter`\ ]


   A crossword puzzle board.


   .. autolink-examples:: CrosswordBoard
      :collapse:

   .. py:method:: _get_word_positions(word: str, start_position: GridPosition, direction: Direction) -> list[GridPosition]

      Calculate the positions for each letter of a word.


      .. autolink-examples:: _get_word_positions
         :collapse:


   .. py:method:: _validate_word_placement(word: str, start_position: GridPosition, direction: Direction) -> bool

      Check if a word can be placed at the specified position.


      .. autolink-examples:: _validate_word_placement
         :collapse:


   .. py:method:: add_clue(number: int, direction: Direction, text: str, answer: str, start_position: GridPosition) -> str | None

      Add a clue to the crossword.


      .. autolink-examples:: add_clue
         :collapse:


   .. py:method:: check_letter(position: GridPosition) -> bool

      Check if the letter at a position is correct.


      .. autolink-examples:: check_letter
         :collapse:


   .. py:method:: enter_letter(position: GridPosition, letter: str, is_filled: bool = True) -> bool

      Enter a letter in a cell.


      .. autolink-examples:: enter_letter
         :collapse:


   .. py:method:: initialize_grid() -> None

      Initialize an empty crossword grid.


      .. autolink-examples:: initialize_grid
         :collapse:


   .. py:method:: set_cell_type(position: GridPosition, cell_type: CellType) -> bool

      Set the type of a cell.


      .. autolink-examples:: set_cell_type
         :collapse:


   .. py:attribute:: clues
      :type:  dict[str, CrosswordClue]
      :value: None



   .. py:property:: is_complete
      :type: bool


      Check if the crossword is complete and correct.

      .. autolink-examples:: is_complete
         :collapse:


   .. py:attribute:: words
      :type:  dict[str, CrosswordWord]
      :value: None



