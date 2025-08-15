games.core.components.cards.scoring
===================================

.. py:module:: games.core.components.cards.scoring


Classes
-------

.. autoapisummary::

   games.core.components.cards.scoring.HandEvaluator
   games.core.components.cards.scoring.HandRank


Module Contents
---------------

.. py:class:: HandEvaluator(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ ]


   Base model for hand evaluation strategies.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HandEvaluator
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: compare_hands(hand1: list[haive.games.core.components.models.TCard], hand2: list[haive.games.core.components.models.TCard], context: dict = None) -> int
      :classmethod:


      Compare two hands.

      Returns: -1 if hand1 < hand2, 0 if equal, 1 if hand1 > hand2.



      .. autolink-examples:: compare_hands
         :collapse:


   .. py:method:: evaluate(cards: list[haive.games.core.components.models.TCard], context: dict = None) -> HandRank[haive.games.core.components.models.TCard]
      :classmethod:

      :abstractmethod:


      Evaluate a hand of cards.


      .. autolink-examples:: evaluate
         :collapse:


.. py:class:: HandRank(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ ]


   Representation of a hand's rank in a card game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HandRank
      :collapse:

   .. py:method:: __eq__(other: HandRank) -> bool


   .. py:method:: __lt__(other: HandRank) -> bool


   .. py:attribute:: primary_cards
      :type:  list[haive.games.core.components.models.TCard]
      :value: None



   .. py:attribute:: rank_name
      :type:  str


   .. py:attribute:: rank_value
      :type:  int


   .. py:attribute:: secondary_cards
      :type:  list[haive.games.core.components.models.TCard]
      :value: None



