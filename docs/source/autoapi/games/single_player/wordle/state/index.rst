games.single_player.wordle.state
================================

.. py:module:: games.single_player.wordle.state


Classes
-------

.. autoapisummary::

   games.single_player.wordle.state.WordConnectionsState


Module Contents
---------------

.. py:class:: WordConnectionsState

   Bases: :py:obj:`haive.games.framework.base.state.GameState`


   State for a Word Connections game.


   .. autolink-examples:: WordConnectionsState
      :collapse:

   .. py:attribute:: analysis_history
      :type:  list[dict]
      :value: None



   .. py:attribute:: attempts_remaining
      :type:  int
      :value: None



   .. py:property:: board_string
      :type: str


      Get a string representation of the board.

      .. autolink-examples:: board_string
         :collapse:


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



