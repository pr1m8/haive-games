games.core.components.cards.turns
=================================

.. py:module:: games.core.components.cards.turns


Classes
-------

.. autoapisummary::

   games.core.components.cards.turns.CardGameTurn
   games.core.components.cards.turns.TurnManager
   games.core.components.cards.turns.TurnPhase


Module Contents
---------------

.. py:class:: CardGameTurn(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ , :py:obj:`haive.games.core.components.actions.TAction`\ , :py:obj:`haive.games.core.components.models.TState`\ ]


   Model representing a turn in a card game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CardGameTurn
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add_action(action: haive.games.core.components.actions.TAction) -> None

      Record an action taken during this turn.


      .. autolink-examples:: add_action
         :collapse:


   .. py:method:: get_next_phase() -> TurnPhase | None

      Get the next phase of the turn.


      .. autolink-examples:: get_next_phase
         :collapse:


   .. py:method:: is_complete(state: haive.games.core.components.models.TState) -> bool

      Check if the turn is complete.


      .. autolink-examples:: is_complete
         :collapse:


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


.. py:class:: TurnManager(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`haive.games.core.components.models.TCard`\ , :py:obj:`haive.games.core.components.actions.TAction`\ , :py:obj:`haive.games.core.components.models.TState`\ ]


   Manages turn progression in a card game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TurnManager
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: end_turn(state: haive.games.core.components.models.TState) -> haive.games.core.components.models.TState

      End the current turn and advance to the next player.


      .. autolink-examples:: end_turn
         :collapse:


   .. py:method:: get_current_player() -> str

      Get the current player's ID.


      .. autolink-examples:: get_current_player
         :collapse:


   .. py:method:: process_action(action: haive.games.core.components.actions.TAction, state: haive.games.core.components.models.TState) -> tuple[haive.games.core.components.actions.ActionResult, haive.games.core.components.models.TState]

      Process an action within the current turn.


      .. autolink-examples:: process_action
         :collapse:


   .. py:method:: reverse_direction() -> None

      Reverse the turn order direction.


      .. autolink-examples:: reverse_direction
         :collapse:


   .. py:method:: start_game(players: list[str]) -> None

      Initialize the turn manager with players.


      .. autolink-examples:: start_game
         :collapse:


   .. py:method:: start_turn(state: haive.games.core.components.models.TState) -> haive.games.core.components.models.TState

      Start a new turn.


      .. autolink-examples:: start_turn
         :collapse:


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



.. py:class:: TurnPhase

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Common phases in a card game turn.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: TurnPhase
      :collapse:

   .. py:attribute:: DISCARD
      :value: 'discard'



   .. py:attribute:: DRAW
      :value: 'draw'



   .. py:attribute:: PLAY
      :value: 'play'



   .. py:attribute:: SPECIAL
      :value: 'special'



