games.mastermind.demo
=====================

.. py:module:: games.mastermind.demo

.. autoapi-nested-parse::

   Standalone demo for the Mastermind game with Rich UI.

   This script demonstrates the Mastermind game without requiring the full Haive framework.


   .. autolink-examples:: games.mastermind.demo
      :collapse:


Attributes
----------

.. autoapisummary::

   games.mastermind.demo.logger


Classes
-------

.. autoapisummary::

   games.mastermind.demo.ColorCode
   games.mastermind.demo.Feedback
   games.mastermind.demo.MastermindState
   games.mastermind.demo.MastermindUI


Functions
---------

.. autoapisummary::

   games.mastermind.demo.calculate_feedback
   games.mastermind.demo.main


Module Contents
---------------

.. py:class:: ColorCode(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Color code for Mastermind game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ColorCode
      :collapse:

   .. py:method:: __str__() -> str


   .. py:attribute:: colors
      :type:  list[str]
      :value: None



.. py:class:: Feedback(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Feedback for a guess in Mastermind.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Feedback
      :collapse:

   .. py:method:: __str__() -> str


   .. py:attribute:: correct_color
      :type:  int
      :value: 0



   .. py:attribute:: correct_position
      :type:  int
      :value: 0



.. py:class:: MastermindState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for the Mastermind game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MastermindState
      :collapse:

   .. py:method:: initialize(secret_code: list[str] | None = None, max_turns: int = 10) -> MastermindState
      :classmethod:


      Initialize a new game state.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: make_guess(guess: list[str]) -> Feedback

      Make a guess and get feedback.


      .. autolink-examples:: make_guess
         :collapse:


   .. py:attribute:: codemaker
      :type:  str
      :value: 'player1'



   .. py:attribute:: feedback
      :type:  list[Feedback]
      :value: None



   .. py:attribute:: game_status
      :type:  str
      :value: 'in_progress'



   .. py:attribute:: guesses
      :type:  list[ColorCode]
      :value: None



   .. py:attribute:: max_turns
      :type:  int
      :value: 10



   .. py:attribute:: secret_code
      :type:  ColorCode


   .. py:attribute:: turn
      :type:  int
      :value: 1



.. py:class:: MastermindUI

   Rich terminal UI for the Mastermind game.

   Initialize the UI.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MastermindUI
      :collapse:

   .. py:method:: color_to_emoji(color: str) -> str

      Convert color name to emoji.


      .. autolink-examples:: color_to_emoji
         :collapse:


   .. py:method:: create_guesses_table(state: MastermindState) -> rich.table.Table

      Create table of guesses and feedback.


      .. autolink-examples:: create_guesses_table
         :collapse:


   .. py:method:: create_header(state: MastermindState) -> rich.panel.Panel

      Create header panel with game info.


      .. autolink-examples:: create_header
         :collapse:


   .. py:method:: create_layout(state: MastermindState, show_secret: bool = False) -> rich.layout.Layout

      Create complete layout for the game.


      .. autolink-examples:: create_layout
         :collapse:


   .. py:method:: create_secret_panel(state: MastermindState, show_secret: bool = False) -> rich.panel.Panel

      Create panel showing the secret code (or hidden).


      .. autolink-examples:: create_secret_panel
         :collapse:


   .. py:method:: display_game_state(state: MastermindState, show_secret: bool = False)

      Display the current game state.


      .. autolink-examples:: display_game_state
         :collapse:


   .. py:method:: input_guess(available_colors: list[str]) -> list[str]

      Get guess input from user.


      .. autolink-examples:: input_guess
         :collapse:


   .. py:method:: show_result(state: MastermindState)

      Show the game result.


      .. autolink-examples:: show_result
         :collapse:


   .. py:attribute:: COLOR_EMOJIS


   .. py:attribute:: FEEDBACK_SYMBOLS


   .. py:attribute:: console


.. py:function:: calculate_feedback(secret_code: list[str], guess: list[str]) -> dict[str, int]

   Calculate feedback for a guess.


   .. autolink-examples:: calculate_feedback
      :collapse:

.. py:function:: main()

   Run the Mastermind game.


   .. autolink-examples:: main
      :collapse:

.. py:data:: logger

