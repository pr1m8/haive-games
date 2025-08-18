games.single_player.wordle.models
=================================

.. py:module:: games.single_player.wordle.models

Module documentation for games.single_player.wordle.models


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span>   </div>


      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.single_player.wordle.models.WordConnectionsMove
      games.single_player.wordle.models.WordConnectionsState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a move in Word Connections game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_words_length(v)
               :classmethod:


               Validate that exactly 4 words are provided.



            .. py:attribute:: category_guess
               :type:  str
               :value: None



            .. py:attribute:: words
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.GameState`


            State for a Word Connections game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: categories
               :type:  dict[str, list[str]]
               :value: None



            .. py:attribute:: difficulty_map
               :type:  dict[str, str]
               :value: None



            .. py:property:: display_grid
               :type: str


               Display the current grid state.


            .. py:attribute:: found_categories
               :type:  dict[str, list[str]]
               :value: None



            .. py:attribute:: game_status
               :type:  Literal['playing', 'won', 'lost']
               :value: None



            .. py:attribute:: grid
               :type:  list[str]
               :value: None



            .. py:attribute:: incorrect_guesses
               :type:  list[list[str]]
               :value: None



            .. py:attribute:: mistakes_remaining
               :type:  int
               :value: None



            .. py:property:: remaining_words
               :type: list[str]


               Get words not yet correctly categorized.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.wordle.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

