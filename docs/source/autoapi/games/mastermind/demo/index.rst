games.mastermind.demo
=====================

.. py:module:: games.mastermind.demo

Standalone demo for the Mastermind game with Rich UI.

This script demonstrates the Mastermind game without requiring the full Haive framework.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span> • <span class="module-stat">2 functions</span> • <span class="module-stat">1 attributes</span>   </div>

.. autoapi-nested-parse::

   Standalone demo for the Mastermind game with Rich UI.

   This script demonstrates the Mastermind game without requiring the full Haive framework.



      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.mastermind.demo.logger

            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.mastermind.demo.ColorCode
      games.mastermind.demo.Feedback
      games.mastermind.demo.MastermindState
      games.mastermind.demo.MastermindUI

            

.. admonition:: Functions (2)
   :class: info

   .. autoapisummary::

      games.mastermind.demo.calculate_feedback
      games.mastermind.demo.main

            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ColorCode(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Color code for Mastermind game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str


            .. py:attribute:: colors
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Feedback(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Feedback for a guess in Mastermind.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str


            .. py:attribute:: correct_color
               :type:  int
               :value: 0



            .. py:attribute:: correct_position
               :type:  int
               :value: 0




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MastermindState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            State for the Mastermind game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: initialize(secret_code: list[str] | None = None, max_turns: int = 10) -> MastermindState
               :classmethod:


               Initialize a new game state.



            .. py:method:: is_game_over() -> bool

               Check if the game is over.



            .. py:method:: make_guess(guess: list[str]) -> Feedback

               Make a guess and get feedback.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MastermindUI

            Rich terminal UI for the Mastermind game.

            Initialize the UI.


            .. py:method:: color_to_emoji(color: str) -> str

               Convert color name to emoji.



            .. py:method:: create_guesses_table(state: MastermindState) -> rich.table.Table

               Create table of guesses and feedback.



            .. py:method:: create_header(state: MastermindState) -> rich.panel.Panel

               Create header panel with game info.



            .. py:method:: create_layout(state: MastermindState, show_secret: bool = False) -> rich.layout.Layout

               Create complete layout for the game.



            .. py:method:: create_secret_panel(state: MastermindState, show_secret: bool = False) -> rich.panel.Panel

               Create panel showing the secret code (or hidden).



            .. py:method:: display_game_state(state: MastermindState, show_secret: bool = False)

               Display the current game state.



            .. py:method:: input_guess(available_colors: list[str]) -> list[str]

               Get guess input from user.



            .. py:method:: show_result(state: MastermindState)

               Show the game result.



            .. py:attribute:: COLOR_EMOJIS


            .. py:attribute:: FEEDBACK_SYMBOLS


            .. py:attribute:: console



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: calculate_feedback(secret_code: list[str], guess: list[str]) -> dict[str, int]

            Calculate feedback for a guess.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:function:: main()

            Run the Mastermind game.



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: logger




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.mastermind.demo import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

