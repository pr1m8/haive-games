games.cards.standard.poker.scoring
==================================

.. py:module:: games.cards.standard.poker.scoring


Classes
-------

.. autoapisummary::

   games.cards.standard.poker.scoring.PokerHandEvaluator
   games.cards.standard.poker.scoring.PokerHandRank
   games.cards.standard.poker.scoring.PokerHandType


Module Contents
---------------

.. py:class:: PokerHandEvaluator

   Bases: :py:obj:`haive.games.cards.card.components.scoring.HandEvaluator`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ ]


   Evaluator for poker hands.


   .. autolink-examples:: PokerHandEvaluator
      :collapse:

   .. py:method:: _check_flush(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
      :classmethod:


      Check for a flush (5+ cards of same suit).


      .. autolink-examples:: _check_flush
         :collapse:


   .. py:method:: _check_four_of_a_kind(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
      :classmethod:


      Check for four of a kind.


      .. autolink-examples:: _check_four_of_a_kind
         :collapse:


   .. py:method:: _check_full_house(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
      :classmethod:


      Check for a full house (three of a kind + pair).


      .. autolink-examples:: _check_full_house
         :collapse:


   .. py:method:: _check_high_card(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank
      :classmethod:


      Return high card evaluation.


      .. autolink-examples:: _check_high_card
         :collapse:


   .. py:method:: _check_pair(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
      :classmethod:


      Check for a pair.


      .. autolink-examples:: _check_pair
         :collapse:


   .. py:method:: _check_royal_flush(cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> PokerHandRank | None
      :classmethod:


      Check for a royal flush (A-K-Q-J-10 of same suit).


      .. autolink-examples:: _check_royal_flush
         :collapse:


   .. py:method:: _check_straight(cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> PokerHandRank | None
      :classmethod:


      Check for a straight (5 consecutive ranked cards).


      .. autolink-examples:: _check_straight
         :collapse:


   .. py:method:: _check_straight_flush(cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> PokerHandRank | None
      :classmethod:


      Check for a straight flush.


      .. autolink-examples:: _check_straight_flush
         :collapse:


   .. py:method:: _check_three_of_a_kind(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
      :classmethod:


      Check for three of a kind.


      .. autolink-examples:: _check_three_of_a_kind
         :collapse:


   .. py:method:: _check_two_pair(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
      :classmethod:


      Check for two pair.


      .. autolink-examples:: _check_two_pair
         :collapse:


   .. py:method:: _find_straight(sorted_cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> list[haive.games.cards.card.components.standard.StandardCard] | None
      :classmethod:


      Find a straight in a sorted list of cards.


      .. autolink-examples:: _find_straight
         :collapse:


   .. py:method:: evaluate(cards: list[haive.games.cards.card.components.standard.StandardCard], context: dict | None = None) -> PokerHandRank
      :classmethod:


      Evaluate a poker hand to determine its rank.


      .. autolink-examples:: evaluate
         :collapse:


.. py:class:: PokerHandRank

   Bases: :py:obj:`haive.games.cards.card.components.scoring.HandRank`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ ]


   Detailed poker hand ranking.


   .. autolink-examples:: PokerHandRank
      :collapse:

   .. py:method:: __str__() -> str

      Human-readable description of the hand.


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: hand_cards
      :type:  list[haive.games.cards.card.components.standard.StandardCard]
      :value: []



   .. py:attribute:: hand_type
      :type:  PokerHandType


   .. py:attribute:: kicker_cards
      :type:  list[haive.games.cards.card.components.standard.StandardCard]
      :value: []



.. py:class:: PokerHandType

   Bases: :py:obj:`enum.IntEnum`


   Poker hand rankings in ascending order.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerHandType
      :collapse:

   .. py:attribute:: FLUSH
      :value: 6



   .. py:attribute:: FOUR_OF_A_KIND
      :value: 8



   .. py:attribute:: FULL_HOUSE
      :value: 7



   .. py:attribute:: HIGH_CARD
      :value: 1



   .. py:attribute:: PAIR
      :value: 2



   .. py:attribute:: ROYAL_FLUSH
      :value: 10



   .. py:attribute:: STRAIGHT
      :value: 5



   .. py:attribute:: STRAIGHT_FLUSH
      :value: 9



   .. py:attribute:: THREE_OF_A_KIND
      :value: 4



   .. py:attribute:: TWO_PAIR
      :value: 3



