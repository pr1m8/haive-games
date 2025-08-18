games.nim.state
===============

.. py:module:: games.nim.state

Module documentation for games.nim.state


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.nim.state.NimState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents the state of a Nim game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:property:: board_string
               :type: str


               Return a string representation of the board.


            .. py:attribute:: game_status
               :type:  Literal['in_progress', 'player1_win', 'player2_win']
               :value: None



            .. py:property:: is_game_over
               :type: bool


               Check if the game is over.


            .. py:attribute:: misere_mode
               :type:  bool
               :value: None



            .. py:attribute:: move_history
               :type:  list[haive.games.nim.models.NimMove]
               :value: None



            .. py:property:: nim_sum
               :type: int


               Calculate the nim-sum (XOR sum) of the pile sizes.


            .. py:attribute:: piles
               :type:  list[int]
               :value: None



            .. py:attribute:: player1_analysis
               :type:  list[haive.games.nim.models.NimAnalysis]
               :value: None



            .. py:attribute:: player2_analysis
               :type:  list[haive.games.nim.models.NimAnalysis]
               :value: None



            .. py:property:: stones_left
               :type: int


               Return the total number of stones left.


            .. py:attribute:: turn
               :type:  Literal['player1', 'player2']
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

