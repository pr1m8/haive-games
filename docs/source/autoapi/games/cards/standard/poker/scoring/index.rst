games.cards.standard.poker.scoring
==================================

.. py:module:: games.cards.standard.poker.scoring

Module documentation for games.cards.standard.poker.scoring


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span>   </div>


      
            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.cards.standard.poker.scoring.PokerHandEvaluator
      games.cards.standard.poker.scoring.PokerHandRank
      games.cards.standard.poker.scoring.PokerHandType

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerHandEvaluator

            Bases: :py:obj:`haive.games.cards.card.components.scoring.HandEvaluator`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ ]


            Evaluator for poker hands.


            .. py:method:: _check_flush(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
               :classmethod:


               Check for a flush (5+ cards of same suit).



            .. py:method:: _check_four_of_a_kind(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
               :classmethod:


               Check for four of a kind.



            .. py:method:: _check_full_house(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
               :classmethod:


               Check for a full house (three of a kind + pair).



            .. py:method:: _check_high_card(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank
               :classmethod:


               Return high card evaluation.



            .. py:method:: _check_pair(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
               :classmethod:


               Check for a pair.



            .. py:method:: _check_royal_flush(cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> PokerHandRank | None
               :classmethod:


               Check for a royal flush (A-K-Q-J-10 of same suit).



            .. py:method:: _check_straight(cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> PokerHandRank | None
               :classmethod:


               Check for a straight (5 consecutive ranked cards).



            .. py:method:: _check_straight_flush(cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> PokerHandRank | None
               :classmethod:


               Check for a straight flush.



            .. py:method:: _check_three_of_a_kind(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
               :classmethod:


               Check for three of a kind.



            .. py:method:: _check_two_pair(cards: list[haive.games.cards.card.components.standard.StandardCard]) -> PokerHandRank | None
               :classmethod:


               Check for two pair.



            .. py:method:: _find_straight(sorted_cards: list[haive.games.cards.card.components.standard.StandardCard], aces_high: bool) -> list[haive.games.cards.card.components.standard.StandardCard] | None
               :classmethod:


               Find a straight in a sorted list of cards.



            .. py:method:: evaluate(cards: list[haive.games.cards.card.components.standard.StandardCard], context: dict | None = None) -> PokerHandRank
               :classmethod:


               Evaluate a poker hand to determine its rank.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerHandRank

            Bases: :py:obj:`haive.games.cards.card.components.scoring.HandRank`\ [\ :py:obj:`haive.games.cards.card.components.standard.StandardCard`\ ]


            Detailed poker hand ranking.


            .. py:method:: __str__() -> str

               Human-readable description of the hand.



            .. py:attribute:: hand_cards
               :type:  list[haive.games.cards.card.components.standard.StandardCard]
               :value: []



            .. py:attribute:: hand_type
               :type:  PokerHandType


            .. py:attribute:: kicker_cards
               :type:  list[haive.games.cards.card.components.standard.StandardCard]
               :value: []




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PokerHandType

            Bases: :py:obj:`enum.IntEnum`


            Poker hand rankings in ascending order.

            Initialize self.  See help(type(self)) for accurate signature.


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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.poker.scoring import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

