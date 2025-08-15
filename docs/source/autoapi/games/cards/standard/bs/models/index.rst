games.cards.standard.bs.models
==============================

.. py:module:: games.cards.standard.bs.models


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.models.Card
   games.cards.standard.bs.models.CardSuit
   games.cards.standard.bs.models.ChallengeAction
   games.cards.standard.bs.models.PlayerClaimAction
   games.cards.standard.bs.models.PlayerState


Module Contents
---------------

.. py:class:: Card(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a playing card.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Card
      :collapse:

   .. py:method:: __str__() -> str


   .. py:method:: create_deck() -> list[Card]
      :classmethod:


      Create a full deck of 52 cards.


      .. autolink-examples:: create_deck
         :collapse:


   .. py:attribute:: suit
      :type:  CardSuit


   .. py:attribute:: value
      :type:  str


.. py:class:: CardSuit

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CardSuit
      :collapse:

   .. py:attribute:: CLUBS
      :value: 'clubs'



   .. py:attribute:: DIAMONDS
      :value: 'diamonds'



   .. py:attribute:: HEARTS
      :value: 'hearts'



   .. py:attribute:: SPADES
      :value: 'spades'



.. py:class:: ChallengeAction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a player challenging another player's claim.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ChallengeAction
      :collapse:

   .. py:attribute:: challenge_type
      :type:  str
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



   .. py:attribute:: target_player_index
      :type:  int
      :value: None



.. py:class:: PlayerClaimAction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a player's claim during their turn.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerClaimAction
      :collapse:

   .. py:attribute:: claimed_value
      :type:  str
      :value: None



   .. py:attribute:: is_truth
      :type:  bool
      :value: None



   .. py:attribute:: number_of_cards
      :type:  int
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



.. py:class:: PlayerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a player's state in the Bullshit game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerState
      :collapse:

   .. py:method:: play_cards(cards: list[Card]) -> None

      Remove played cards from hand.


      .. autolink-examples:: play_cards
         :collapse:


   .. py:attribute:: cards_played
      :type:  list[Card]
      :value: None



   .. py:attribute:: hand
      :type:  list[Card]
      :value: None



   .. py:attribute:: name
      :type:  str


