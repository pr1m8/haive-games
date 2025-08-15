games.nim.state
===============

.. py:module:: games.nim.state


Classes
-------

.. autoapisummary::

   games.nim.state.NimState


Module Contents
---------------

.. py:class:: NimState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents the state of a Nim game.

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
      :type:  Literal['in_progress', 'player1_win', 'player2_win']
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
      :type:  list[haive.games.nim.models.NimMove]
      :value: None



   .. py:property:: nim_sum
      :type: int


      Calculate the nim-sum (XOR sum) of the pile sizes.

      .. autolink-examples:: nim_sum
         :collapse:


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

      .. autolink-examples:: stones_left
         :collapse:


   .. py:attribute:: turn
      :type:  Literal['player1', 'player2']
      :value: None



