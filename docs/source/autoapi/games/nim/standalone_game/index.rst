games.nim.standalone_game
=========================

.. py:module:: games.nim.standalone_game

Standalone game implementation of Nim.

This script allows playing Nim without requiring the full Haive framework.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span> • <span class="module-stat">2 functions</span> • <span class="module-stat">2 attributes</span>   </div>

.. autoapi-nested-parse::

   Standalone game implementation of Nim.

   This script allows playing Nim without requiring the full Haive framework.



      

.. admonition:: Attributes (2)
   :class: tip

   .. autoapisummary::

      games.nim.standalone_game.RICH_AVAILABLE
      games.nim.standalone_game.logger

            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.nim.standalone_game.NimGameManager
      games.nim.standalone_game.NimMove
      games.nim.standalone_game.NimState
      games.nim.standalone_game.NimUI

            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.nim.standalone_game.main
      games.nim.standalone_game.parse_args

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimGameManager

            Manager for the Nim game.


            .. py:method:: apply_move(state: NimState, move: NimMove) -> NimState
               :staticmethod:


               Apply a move to the current state.



            .. py:method:: check_game_status(state: NimState) -> NimState
               :staticmethod:


               Check and update the game status.



            .. py:method:: initialize(pile_sizes: list[int] = None, misere_mode: bool = False) -> NimState
               :staticmethod:


               Initialize a new game state.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Move in the Nim game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str


            .. py:attribute:: pile_index
               :type:  int


            .. py:attribute:: stones_taken
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            State for the Nim game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:property:: board_string
               :type: str


               Return a string representation of the board.


            .. py:attribute:: game_status
               :type:  str
               :value: None



            .. py:property:: is_game_over
               :type: bool


               Check if the game is over.


            .. py:attribute:: misere_mode
               :type:  bool
               :value: None



            .. py:attribute:: move_history
               :type:  list[NimMove]
               :value: None



            .. py:property:: nim_sum
               :type: int


               Calculate the nim-sum (XOR sum) of the pile sizes.


            .. py:attribute:: piles
               :type:  list[int]
               :value: None



            .. py:property:: stones_left
               :type: int


               Return the total number of stones left.


            .. py:attribute:: turn
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimUI(delay: float = 0.5)

            UI for the Nim game.

            Initialize the UI.


            .. py:method:: _display_rich_ui(state: NimState)

               Display game state using Rich UI.



            .. py:method:: _display_text_ui(state: NimState)

               Display game state using text UI.



            .. py:method:: announce_winner(state: NimState)

               Announce the winner of the game.



            .. py:method:: display_game_state(state: NimState)

               Display the current game state.



            .. py:method:: get_computer_move(state: NimState) -> NimMove

               Generate a computer move.



            .. py:method:: prompt_for_move(state: NimState) -> NimMove

               Prompt the user for a move.



            .. py:attribute:: EMPTY_SYMBOL
               :value: '⚫'



            .. py:attribute:: STONE_SYMBOL
               :value: '🔵'



            .. py:attribute:: delay
               :value: 0.5




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run the Nim game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: parse_args()

            Parse command line arguments.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: RICH_AVAILABLE
            :value: True



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.standalone_game import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

