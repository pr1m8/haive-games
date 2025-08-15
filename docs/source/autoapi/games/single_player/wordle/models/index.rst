games.single_player.wordle.models
=================================

.. py:module:: games.single_player.wordle.models


Classes
-------

.. autoapisummary::

   games.single_player.wordle.models.WordConnectionsMove
   games.single_player.wordle.models.WordConnectionsState


Module Contents
---------------

.. py:class:: WordConnectionsMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a move in Word Connections game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: WordConnectionsMove
      :collapse:

   .. py:method:: validate_words_length(v)
      :classmethod:


      Validate that exactly 4 words are provided.


      .. autolink-examples:: validate_words_length
         :collapse:


   .. py:attribute:: category_guess
      :type:  str
      :value: None



   .. py:attribute:: words
      :type:  list[str]
      :value: None



.. py:class:: WordConnectionsState

   Bases: :py:obj:`haive.games.framework.base.GameState`


   State for a Word Connections game.


   .. autolink-examples:: WordConnectionsState
      :collapse:

   .. py:attribute:: categories
      :type:  dict[str, list[str]]
      :value: None



   .. py:attribute:: difficulty_map
      :type:  dict[str, str]
      :value: None



   .. py:property:: display_grid
      :type: str


      Display the current grid state.

      .. autolink-examples:: display_grid
         :collapse:


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

      .. autolink-examples:: remaining_words
         :collapse:


