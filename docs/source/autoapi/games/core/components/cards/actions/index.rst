games.core.components.cards.actions
===================================

.. py:module:: games.core.components.cards.actions

Module documentation for games.core.components.cards.actions


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>


      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.core.components.cards.actions.ActionResult
      games.core.components.cards.actions.CardAction
      games.core.components.cards.actions.DrawCardAction
      games.core.components.cards.actions.PlayCardAction

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ActionResult(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Result of executing a card action.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: message
               :type:  str
               :value: ''



            .. py:attribute:: state_updates
               :type:  dict[str, Any]
               :value: None



            .. py:attribute:: success
               :type:  bool



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardAction(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.cards.base.TCard`\ , :py:obj:`haive.games.core.components.cards.base.TState`\ ]


            Base model for card game actions.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: can_execute(state: haive.games.core.components.cards.base.TState) -> bool

               Check if this action can be executed in the current state.



            .. py:method:: execute(state: haive.games.core.components.cards.base.TState) -> ActionResult
               :abstractmethod:


               Execute this action on the game state.



            .. py:method:: validate_action() -> CardAction

               Validate the action is properly formed.



            .. py:attribute:: action_type
               :type:  str


            .. py:attribute:: player_id
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DrawCardAction

            Bases: :py:obj:`CardAction`\ [\ :py:obj:`haive.games.core.components.cards.base.TCard`\ , :py:obj:`haive.games.core.components.cards.base.TState`\ ]


            Action to draw a card from the deck.


            .. py:method:: can_execute(state: haive.games.core.components.cards.base.TState) -> bool

               Check if player can draw.



            .. py:method:: execute(state: haive.games.core.components.cards.base.TState) -> ActionResult

               Draw card(s) from deck to player's hand.



            .. py:method:: validate_action() -> DrawCardAction

               Validate draw count.



            .. py:attribute:: action_type
               :type:  str
               :value: 'draw_card'



            .. py:attribute:: count
               :type:  int
               :value: 1




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayCardAction

            Bases: :py:obj:`CardAction`\ [\ :py:obj:`haive.games.core.components.cards.base.TCard`\ , :py:obj:`haive.games.core.components.cards.base.TState`\ ]


            Action to play a card from hand.


            .. py:method:: can_execute(state: haive.games.core.components.cards.base.TState) -> bool

               Check if player can play the card.



            .. py:method:: execute(state: haive.games.core.components.cards.base.TState) -> ActionResult

               Play the card from hand.



            .. py:attribute:: action_type
               :type:  str
               :value: 'play_card'



            .. py:attribute:: card_id
               :type:  str


            .. py:attribute:: target_id
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.components.cards.actions import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

