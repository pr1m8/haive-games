games.core.components.cards.scoring
===================================

.. py:module:: games.core.components.cards.scoring

Module documentation for games.core.components.cards.scoring


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span>   </div>


      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.core.components.cards.scoring.HandEvaluator
      games.core.components.cards.scoring.HandRank

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HandEvaluator(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ ]


            Base model for hand evaluation strategies.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: compare_hands(hand1: list[haive.games.core.components.models.TCard], hand2: list[haive.games.core.components.models.TCard], context: dict = None) -> int
               :classmethod:


               Compare two hands.

               Returns: -1 if hand1 < hand2, 0 if equal, 1 if hand1 > hand2.




            .. py:method:: evaluate(cards: list[haive.games.core.components.models.TCard], context: dict = None) -> HandRank[haive.games.core.components.models.TCard]
               :classmethod:

               :abstractmethod:


               Evaluate a hand of cards.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: HandRank(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ ]


            Representation of a hand's rank in a card game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.components.cards.scoring import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

