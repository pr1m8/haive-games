games.cards.standard.blackjack.models
=====================================

.. py:module:: games.cards.standard.blackjack.models

Module documentation for games.cards.standard.blackjack.models


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">6 classes</span>   </div>


      
            
            

.. admonition:: Classes (6)
   :class: note

   .. autoapisummary::

      games.cards.standard.blackjack.models.BlackjackGameState
      games.cards.standard.blackjack.models.Card
      games.cards.standard.blackjack.models.CardSuit
      games.cards.standard.blackjack.models.PlayerAction
      games.cards.standard.blackjack.models.PlayerHand
      games.cards.standard.blackjack.models.PlayerState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: BlackjackGameState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents the overall state of a Blackjack game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: current_hand_index
               :type:  int
               :value: None



            .. py:attribute:: current_player_index
               :type:  int
               :value: None



            .. py:attribute:: dealer_hand
               :type:  list[Card]
               :value: None



            .. py:attribute:: deck
               :type:  list[Card]
               :value: None



            .. py:attribute:: game_status
               :type:  Literal['betting', 'playing', 'dealer_turn', 'game_over']
               :value: None



            .. py:attribute:: players
               :type:  list[PlayerState]
               :value: None



            .. py:attribute:: round_winner
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Card(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a playing card.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str


            .. py:method:: point_value() -> int

               Calculate point value of the card.



            .. py:attribute:: suit
               :type:  CardSuit


            .. py:attribute:: value
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

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


            .. py:attribute:: CLUBS
               :value: 'clubs'



            .. py:attribute:: DIAMONDS
               :value: 'diamonds'



            .. py:attribute:: HEARTS
               :value: 'hearts'



            .. py:attribute:: SPADES
               :value: 'spades'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerAction(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a player's action in Blackjack.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: action
               :type:  Literal['hit', 'stand', 'double_down', 'split', 'surrender']
               :value: None



            .. py:attribute:: reasoning
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerHand(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a player's hand in Blackjack.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: is_blackjack() -> bool

               Check if the hand is a blackjack.



            .. py:method:: is_bust() -> bool

               Check if the hand is bust.



            .. py:method:: total_value() -> int

               Calculate the total value of the hand.



            .. py:attribute:: bet
               :type:  float
               :value: None



            .. py:attribute:: cards
               :type:  list[Card]
               :value: None



            .. py:attribute:: is_active
               :type:  bool
               :value: None



            .. py:attribute:: is_split
               :type:  bool
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Represents a player's state in the game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: add_hand(hand: PlayerHand)

               Add a hand to the player's state.



            .. py:attribute:: current_bet
               :type:  float
               :value: None



            .. py:attribute:: hands
               :type:  list[PlayerHand]
               :value: None



            .. py:attribute:: is_active
               :type:  bool
               :value: None



            .. py:attribute:: name
               :type:  str


            .. py:attribute:: total_chips
               :type:  float
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.cards.standard.blackjack.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

