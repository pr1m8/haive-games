deck
====

.. py:module:: deck

Module documentation for deck


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      deck.C

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      deck.Deck

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Deck

            Bases: :py:obj:`haive.games.framework.core.container.GamePieceContainer`\ [\ :py:obj:`C`\ ]


            A deck of cards.

            This represents a collection of cards that can be drawn, shuffled, and dealt.



            .. py:method:: create_standard_deck() -> Deck[haive.games.framework.pieces.card.PlayingCard]
               :classmethod:


               Create a standard 52-card deck.

               :returns: A new deck with standard playing cards



            .. py:method:: discard(card: C) -> None

               Add a card to the discard pile.

               :param card: Card to discard



            .. py:method:: draw() -> C | None

               Draw the top card and set its face up/down based on deck configuration.

               :returns: The drawn card, or None if deck is empty



            .. py:method:: draw_many(count: int) -> list[C]

               Draw multiple cards from the top.

               :param count: Number of cards to draw

               :returns: List of drawn cards



            .. py:attribute:: discard_pile
               :type:  list[C]
               :value: None



            .. py:attribute:: face_down
               :type:  bool
               :value: True




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: C




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from deck import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

