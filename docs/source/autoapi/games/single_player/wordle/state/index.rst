games.single_player.wordle.state
================================

.. py:module:: games.single_player.wordle.state

Module documentation for games.single_player.wordle.state


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.wordle.state.WordConnectionsState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: WordConnectionsState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.state.GameState`


            State for a Word Connections game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: analysis_history
               :type:  list[dict]
               :value: None



            .. py:attribute:: attempts_remaining
               :type:  int
               :value: None



            .. py:property:: board_string
               :type: str


               Get a string representation of the board.


            .. py:attribute:: categories
               :type:  dict[str, list[str]]
               :value: None



            .. py:attribute:: category_difficulty
               :type:  dict[str, str]
               :value: None



            .. py:attribute:: cells
               :type:  list[haive.games.single_player.wordle.models.WordCell]
               :value: None



            .. py:attribute:: discovered_groups
               :type:  dict[str, list[str]]
               :value: None



            .. py:attribute:: game_date
               :type:  str | None
               :value: None



            .. py:attribute:: game_source
               :type:  haive.games.single_player.wordle.models.GameSource
               :value: None



            .. py:attribute:: game_status
               :type:  Literal['ongoing', 'victory', 'defeat']
               :value: None



            .. py:attribute:: incorrect_attempts
               :type:  list[list[str]]
               :value: None



            .. py:attribute:: incorrect_submissions
               :type:  int
               :value: None



            .. py:attribute:: move_history
               :type:  list[haive.games.single_player.wordle.models.WordConnectionsMove]
               :value: None



            .. py:attribute:: remaining_words
               :type:  list[str]
               :value: None



            .. py:attribute:: score
               :type:  int
               :value: None



            .. py:attribute:: selected_indices
               :type:  list[int]
               :value: None



            .. py:attribute:: turn
               :type:  str
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.wordle.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

