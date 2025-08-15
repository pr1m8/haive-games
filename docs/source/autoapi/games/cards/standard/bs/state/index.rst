games.cards.standard.bs.state
=============================

.. py:module:: games.cards.standard.bs.state


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.state.BullshitGameState


Module Contents
---------------

.. py:class:: BullshitGameState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents the overall state of a Bullshit game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: BullshitGameState
      :collapse:

   .. py:attribute:: challenge_history
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: current_claimed_value
      :type:  str | None
      :value: None



   .. py:attribute:: current_pile
      :type:  list[haive.games.cards.standard.bs.models.Card]
      :value: None



   .. py:attribute:: current_player_index
      :type:  int
      :value: None



   .. py:attribute:: game_status
      :type:  str
      :value: None



   .. py:attribute:: last_played_cards
      :type:  list[haive.games.cards.standard.bs.models.Card]
      :value: None



   .. py:attribute:: players
      :type:  list[haive.games.cards.standard.bs.models.PlayerState]
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



