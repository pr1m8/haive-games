games.core.components.cards.actions
===================================

.. py:module:: games.core.components.cards.actions


Classes
-------

.. autoapisummary::

   games.core.components.cards.actions.ActionResult
   games.core.components.cards.actions.CardAction
   games.core.components.cards.actions.DrawCardAction
   games.core.components.cards.actions.PlayCardAction


Module Contents
---------------

.. py:class:: ActionResult(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Result of executing a card action.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionResult
      :collapse:

   .. py:attribute:: message
      :type:  str
      :value: ''



   .. py:attribute:: state_updates
      :type:  dict[str, Any]
      :value: None



   .. py:attribute:: success
      :type:  bool


.. py:class:: CardAction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.cards.base.TCard`\ , :py:obj:`haive.games.core.components.cards.base.TState`\ ]


   Base model for card game actions.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CardAction
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: can_execute(state: haive.games.core.components.cards.base.TState) -> bool

      Check if this action can be executed in the current state.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.core.components.cards.base.TState) -> ActionResult
      :abstractmethod:


      Execute this action on the game state.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: validate_action() -> CardAction

      Validate the action is properly formed.


      .. autolink-examples:: validate_action
         :collapse:


   .. py:attribute:: action_type
      :type:  str


   .. py:attribute:: player_id
      :type:  str


.. py:class:: DrawCardAction

   Bases: :py:obj:`CardAction`\ [\ :py:obj:`haive.games.core.components.cards.base.TCard`\ , :py:obj:`haive.games.core.components.cards.base.TState`\ ]


   Action to draw a card from the deck.


   .. autolink-examples:: DrawCardAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.core.components.cards.base.TState) -> bool

      Check if player can draw.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.core.components.cards.base.TState) -> ActionResult

      Draw card(s) from deck to player's hand.


      .. autolink-examples:: execute
         :collapse:


   .. py:method:: validate_action() -> DrawCardAction

      Validate draw count.


      .. autolink-examples:: validate_action
         :collapse:


   .. py:attribute:: action_type
      :type:  str
      :value: 'draw_card'



   .. py:attribute:: count
      :type:  int
      :value: 1



.. py:class:: PlayCardAction

   Bases: :py:obj:`CardAction`\ [\ :py:obj:`haive.games.core.components.cards.base.TCard`\ , :py:obj:`haive.games.core.components.cards.base.TState`\ ]


   Action to play a card from hand.


   .. autolink-examples:: PlayCardAction
      :collapse:

   .. py:method:: can_execute(state: haive.games.core.components.cards.base.TState) -> bool

      Check if player can play the card.


      .. autolink-examples:: can_execute
         :collapse:


   .. py:method:: execute(state: haive.games.core.components.cards.base.TState) -> ActionResult

      Play the card from hand.


      .. autolink-examples:: execute
         :collapse:


   .. py:attribute:: action_type
      :type:  str
      :value: 'play_card'



   .. py:attribute:: card_id
      :type:  str


   .. py:attribute:: target_id
      :type:  str | None
      :value: None



