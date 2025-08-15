games.nim.standalone_game
=========================

.. py:module:: games.nim.standalone_game

.. autoapi-nested-parse::

   Standalone game implementation of Nim.

   This script allows playing Nim without requiring the full Haive framework.


   .. autolink-examples:: games.nim.standalone_game
      :collapse:


Attributes
----------

.. autoapisummary::

   games.nim.standalone_game.RICH_AVAILABLE
   games.nim.standalone_game.logger


Classes
-------

.. autoapisummary::

   games.nim.standalone_game.NimGameManager
   games.nim.standalone_game.NimMove
   games.nim.standalone_game.NimState
   games.nim.standalone_game.NimUI


Functions
---------

.. autoapisummary::

   games.nim.standalone_game.main
   games.nim.standalone_game.parse_args


Module Contents
---------------

.. py:class:: NimGameManager

   Manager for the Nim game.


   .. autolink-examples:: NimGameManager
      :collapse:

   .. py:method:: apply_move(state: NimState, move: NimMove) -> NimState
      :staticmethod:


      Apply a move to the current state.


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: NimState) -> NimState
      :staticmethod:


      Check and update the game status.


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: initialize(pile_sizes: list[int] = None, misere_mode: bool = False) -> NimState
      :staticmethod:


      Initialize a new game state.


      .. autolink-examples:: initialize
         :collapse:


.. py:class:: NimMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Move in the Nim game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NimMove
      :collapse:

   .. py:method:: __str__() -> str


   .. py:attribute:: pile_index
      :type:  int


   .. py:attribute:: stones_taken
      :type:  int


.. py:class:: NimState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for the Nim game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NimState
      :collapse:

   .. py:property:: board_string
      :type: str


      Return a string representation of the board.

      .. autolink-examples:: board_string
         :collapse:


   .. py:attribute:: game_status
      :type:  str
      :value: None



   .. py:property:: is_game_over
      :type: bool


      Check if the game is over.

      .. autolink-examples:: is_game_over
         :collapse:


   .. py:attribute:: misere_mode
      :type:  bool
      :value: None



   .. py:attribute:: move_history
      :type:  list[NimMove]
      :value: None



   .. py:property:: nim_sum
      :type: int


      Calculate the nim-sum (XOR sum) of the pile sizes.

      .. autolink-examples:: nim_sum
         :collapse:


   .. py:attribute:: piles
      :type:  list[int]
      :value: None



   .. py:property:: stones_left
      :type: int


      Return the total number of stones left.

      .. autolink-examples:: stones_left
         :collapse:


   .. py:attribute:: turn
      :type:  str
      :value: None



.. py:class:: NimUI(delay: float = 0.5)

   UI for the Nim game.

   Initialize the UI.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NimUI
      :collapse:

   .. py:method:: _display_rich_ui(state: NimState)

      Display game state using Rich UI.


      .. autolink-examples:: _display_rich_ui
         :collapse:


   .. py:method:: _display_text_ui(state: NimState)

      Display game state using text UI.


      .. autolink-examples:: _display_text_ui
         :collapse:


   .. py:method:: announce_winner(state: NimState)

      Announce the winner of the game.


      .. autolink-examples:: announce_winner
         :collapse:


   .. py:method:: display_game_state(state: NimState)

      Display the current game state.


      .. autolink-examples:: display_game_state
         :collapse:


   .. py:method:: get_computer_move(state: NimState) -> NimMove

      Generate a computer move.


      .. autolink-examples:: get_computer_move
         :collapse:


   .. py:method:: prompt_for_move(state: NimState) -> NimMove

      Prompt the user for a move.


      .. autolink-examples:: prompt_for_move
         :collapse:


   .. py:attribute:: EMPTY_SYMBOL
      :value: '⚫'



   .. py:attribute:: STONE_SYMBOL
      :value: '🔵'



   .. py:attribute:: delay
      :value: 0.5



.. py:function:: main()

   Run the Nim game.


   .. autolink-examples:: main
      :collapse:

.. py:function:: parse_args()

   Parse command line arguments.


   .. autolink-examples:: parse_args
      :collapse:

.. py:data:: RICH_AVAILABLE
   :value: True


.. py:data:: logger

