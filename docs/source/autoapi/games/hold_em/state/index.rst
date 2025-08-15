games.hold_em.state
===================

.. py:module:: games.hold_em.state

.. autoapi-nested-parse::

   Fixed Texas Hold'em game state models.

   Key fixes:
   1. Added Annotated type for current_player_index to handle concurrent updates
   2. Fixed reducer setup for fields that might be updated concurrently
   3. Added proper field annotations for LangGraph compatibility


   .. autolink-examples:: games.hold_em.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.hold_em.state.GamePhase
   games.hold_em.state.HoldemState
   games.hold_em.state.PlayerAction
   games.hold_em.state.PlayerDecision
   games.hold_em.state.PlayerState
   games.hold_em.state.PlayerStatus
   games.hold_em.state.PokerAction


Functions
---------

.. autoapisummary::

   games.hold_em.state.last_value_reducer


Module Contents
---------------

.. py:class:: GamePhase

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Game phases in Texas Hold'em.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePhase
      :collapse:

   .. py:attribute:: FLOP
      :value: 'flop'



   .. py:attribute:: GAME_OVER
      :value: 'game_over'



   .. py:attribute:: PREFLOP
      :value: 'preflop'



   .. py:attribute:: RIVER
      :value: 'river'



   .. py:attribute:: SHOWDOWN
      :value: 'showdown'



   .. py:attribute:: TURN
      :value: 'turn'



.. py:class:: HoldemState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for the Texas Hold'em game.

   This class represents the complete game state including:
       - Players and their states
       - Community cards
       - Betting rounds
       - Pot information
       - Game phase tracking


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: HoldemState
      :collapse:

   .. py:class:: Config

      Pydantic configuration.


      .. autolink-examples:: Config
         :collapse:

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: advance_to_next_player() -> int | None

      Advance to the next player who can act.


      .. autolink-examples:: advance_to_next_player
         :collapse:


   .. py:method:: get_player_by_id(player_id: str) -> PlayerState | None

      Get player by ID.


      .. autolink-examples:: get_player_by_id
         :collapse:


   .. py:method:: get_player_by_index(index: int) -> PlayerState | None

      Get player by index.


      .. autolink-examples:: get_player_by_index
         :collapse:


   .. py:method:: is_betting_complete() -> bool

      Check if betting round is complete.


      .. autolink-examples:: is_betting_complete
         :collapse:


   .. py:attribute:: actions_this_round
      :type:  Annotated[list[dict[str, Any]], operator.add]
      :value: None



   .. py:property:: active_players
      :type: list[PlayerState]


      Get list of active players.

      .. autolink-examples:: active_players
         :collapse:


   .. py:attribute:: betting_round_complete
      :type:  Annotated[bool, last_value_reducer]
      :value: None



   .. py:attribute:: big_blind
      :type:  int
      :value: None



   .. py:attribute:: burned_cards
      :type:  list[str]
      :value: None



   .. py:attribute:: community_cards
      :type:  list[str]
      :value: None



   .. py:attribute:: current_bet
      :type:  Annotated[int, last_value_reducer]
      :value: None



   .. py:attribute:: current_phase
      :type:  GamePhase
      :value: None



   .. py:property:: current_player
      :type: PlayerState | None


      Get the current player to act.

      .. autolink-examples:: current_player
         :collapse:


   .. py:attribute:: current_player_index
      :type:  Annotated[int, last_value_reducer]
      :value: None



   .. py:attribute:: dealer_position
      :type:  int
      :value: None



   .. py:attribute:: deck
      :type:  list[str]
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_id
      :type:  str
      :value: None



   .. py:attribute:: game_over
      :type:  bool
      :value: None



   .. py:attribute:: hand_history
      :type:  Annotated[list[dict[str, Any]], operator.add]
      :value: None



   .. py:attribute:: hand_number
      :type:  int
      :value: None



   .. py:attribute:: last_action
      :type:  Annotated[dict[str, Any] | None, last_value_reducer]
      :value: None



   .. py:attribute:: max_players
      :type:  int
      :value: None



   .. py:attribute:: min_raise
      :type:  int
      :value: None



   .. py:attribute:: players
      :type:  list[PlayerState]
      :value: None



   .. py:property:: players_in_hand
      :type: list[PlayerState]


      Get players still in the current hand (not folded).

      .. autolink-examples:: players_in_hand
         :collapse:


   .. py:property:: players_to_act
      :type: list[PlayerState]


      Get players who still need to act this round.

      .. autolink-examples:: players_to_act
         :collapse:


   .. py:attribute:: pot
      :type:  int
      :value: None



   .. py:attribute:: side_pots
      :type:  list[dict[str, Any]]
      :value: None



   .. py:attribute:: small_blind
      :type:  int
      :value: None



   .. py:property:: total_pot
      :type: int


      Calculate total pot including side pots.

      .. autolink-examples:: total_pot
         :collapse:


   .. py:attribute:: winner
      :type:  str | None
      :value: None



.. py:class:: PlayerAction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a player action.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerAction
      :collapse:

   .. py:attribute:: action
      :type:  PokerAction
      :value: None



   .. py:attribute:: amount
      :type:  int
      :value: None



   .. py:attribute:: phase
      :type:  GamePhase
      :value: None



   .. py:attribute:: player_id
      :type:  str
      :value: None



   .. py:attribute:: timestamp
      :type:  str | None
      :value: None



.. py:class:: PlayerDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for player decision-making.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerDecision
      :collapse:

   .. py:attribute:: action
      :type:  PokerAction
      :value: None



   .. py:attribute:: amount
      :type:  int
      :value: None



   .. py:attribute:: confidence
      :type:  float
      :value: None



   .. py:attribute:: hand_strength_estimate
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



.. py:class:: PlayerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State for an individual player.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerState
      :collapse:

   .. py:attribute:: actions_this_hand
      :type:  Annotated[list[dict[str, Any]], operator.add]
      :value: None



   .. py:attribute:: chips
      :type:  int
      :value: None



   .. py:attribute:: current_bet
      :type:  int
      :value: None



   .. py:attribute:: hole_cards
      :type:  list[str]
      :value: None



   .. py:attribute:: is_big_blind
      :type:  bool
      :value: None



   .. py:attribute:: is_dealer
      :type:  bool
      :value: None



   .. py:attribute:: is_small_blind
      :type:  bool
      :value: None



   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: player_id
      :type:  str
      :value: None



   .. py:attribute:: position
      :type:  int
      :value: None



   .. py:attribute:: status
      :type:  PlayerStatus
      :value: None



   .. py:attribute:: total_bet
      :type:  int
      :value: None



.. py:class:: PlayerStatus

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Player status in the game.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerStatus
      :collapse:

   .. py:attribute:: ACTIVE
      :value: 'active'



   .. py:attribute:: ALL_IN
      :value: 'all_in'



   .. py:attribute:: FOLDED
      :value: 'folded'



   .. py:attribute:: OUT
      :value: 'out'



.. py:class:: PokerAction

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Possible poker actions.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PokerAction
      :collapse:

   .. py:attribute:: ALL_IN
      :value: 'all_in'



   .. py:attribute:: BET
      :value: 'bet'



   .. py:attribute:: CALL
      :value: 'call'



   .. py:attribute:: CHECK
      :value: 'check'



   .. py:attribute:: FOLD
      :value: 'fold'



   .. py:attribute:: RAISE
      :value: 'raise'



.. py:function:: last_value_reducer(a: Any, b: Any) -> Any

   Reducer that takes the last value - for fields that should be overwritten.


   .. autolink-examples:: last_value_reducer
      :collapse:

