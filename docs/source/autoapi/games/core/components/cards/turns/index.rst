games.core.components.cards.turns
=================================

.. py:module:: games.core.components.cards.turns

Module documentation for games.core.components.cards.turns


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">3 classes</span>   </div>


      
            
            

.. admonition:: Classes (3)
   :class: note

   .. autoapisummary::

      games.core.components.cards.turns.CardGameTurn
      games.core.components.cards.turns.TurnManager
      games.core.components.cards.turns.TurnPhase

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardGameTurn(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ , :py:obj:`haive.games.core.components.actions.TAction`\ , :py:obj:`haive.games.core.components.models.TState`\ ]


            Model representing a turn in a card game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: add_action(action: haive.games.core.components.actions.TAction) -> None

               Record an action taken during this turn.



            .. py:method:: get_next_phase() -> TurnPhase | None

               Get the next phase of the turn.



            .. py:method:: is_complete(state: haive.games.core.components.models.TState) -> bool

               Check if the turn is complete.



            .. py:attribute:: actions
               :type:  list[haive.games.core.components.actions.TAction]
               :value: None



            .. py:attribute:: available_actions
               :type:  list[str]
               :value: None



            .. py:attribute:: phase
               :type:  TurnPhase


            .. py:attribute:: player_id
               :type:  str


            .. py:attribute:: turn_number
               :type:  int



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TurnManager(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ , :py:obj:`haive.games.core.components.actions.TAction`\ , :py:obj:`haive.games.core.components.models.TState`\ ]


            Manages turn progression in a card game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: end_turn(state: haive.games.core.components.models.TState) -> haive.games.core.components.models.TState

               End the current turn and advance to the next player.



            .. py:method:: get_current_player() -> str

               Get the current player's ID.



            .. py:method:: process_action(action: haive.games.core.components.actions.TAction, state: haive.games.core.components.models.TState) -> tuple[haive.games.core.components.actions.ActionResult, haive.games.core.components.models.TState]

               Process an action within the current turn.



            .. py:method:: reverse_direction() -> None

               Reverse the turn order direction.



            .. py:method:: start_game(players: list[str]) -> None

               Initialize the turn manager with players.



            .. py:method:: start_turn(state: haive.games.core.components.models.TState) -> haive.games.core.components.models.TState

               Start a new turn.



            .. py:attribute:: current_player_idx
               :type:  int
               :value: 0



            .. py:attribute:: current_turn
               :type:  CardGameTurn[haive.games.core.components.models.TCard, haive.games.core.components.actions.TAction, haive.games.core.components.models.TState] | None
               :value: None



            .. py:attribute:: player_order
               :type:  list[str]
               :value: None



            .. py:attribute:: turn_direction
               :type:  int
               :value: 1



            .. py:attribute:: turn_number
               :type:  int
               :value: 0




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TurnPhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Common phases in a card game turn.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: DISCARD
               :value: 'discard'



            .. py:attribute:: DRAW
               :value: 'draw'



            .. py:attribute:: PLAY
               :value: 'play'



            .. py:attribute:: SPECIAL
               :value: 'special'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.components.cards.turns import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

