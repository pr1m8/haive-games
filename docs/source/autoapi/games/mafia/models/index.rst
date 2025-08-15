games.mafia.models
==================

.. py:module:: games.mafia.models

.. autoapi-nested-parse::

   Models for the Mafia game implementation.

   This module defines the core data models and enums used in the Mafia game, including:
       - Game phases (setup, night, day discussion, voting)
       - Player roles (villager, mafia, detective, doctor, narrator)
       - Action types (speak, vote, kill, investigate, save)
       - State tracking for players and game
       - Decision models for LLM output

   .. rubric:: Example

   >>> from mafia.models import PlayerRole, GamePhase, MafiaAction
   >>>
   >>> # Create a player action
   >>> action = MafiaAction(
   ...     player_id="Player_1",
   ...     action_type="vote",
   ...     phase=GamePhase.DAY_VOTING,
   ...     round_number=1,
   ...     target_id="Player_2"
   ... )


   .. autolink-examples:: games.mafia.models
      :collapse:


Classes
-------

.. autoapisummary::

   games.mafia.models.ActionType
   games.mafia.models.GamePhase
   games.mafia.models.MafiaAction
   games.mafia.models.MafiaPlayerDecision
   games.mafia.models.MafiaPlayerDecisionSchema
   games.mafia.models.NarratorAction
   games.mafia.models.NarratorDecision
   games.mafia.models.NarratorDecisionSchema
   games.mafia.models.PlayerRole
   games.mafia.models.PlayerState


Module Contents
---------------

.. py:class:: ActionType

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Action type enumeration for the Mafia game.

   This enum defines all possible actions that players can take during
   the game, including both general and role-specific actions.

   .. attribute:: SPEAK

      Make a public statement during discussion

   .. attribute:: VOTE

      Vote to eliminate a player during day voting

   .. attribute:: KILL

      Mafia night action to eliminate a player

   .. attribute:: INVESTIGATE

      Detective night action to learn a player's role

   .. attribute:: SAVE

      Doctor night action to protect a player

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: ActionType
      :collapse:

   .. py:attribute:: INVESTIGATE
      :value: 'investigate'



   .. py:attribute:: KILL
      :value: 'kill'



   .. py:attribute:: SAVE
      :value: 'save'



   .. py:attribute:: SPEAK
      :value: 'speak'



   .. py:attribute:: VOTE
      :value: 'vote'



.. py:class:: GamePhase

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Game phase enumeration for the Mafia game.

   This enum defines the possible phases of the game, which determine what
   actions players can take and how the game progresses.

   .. attribute:: SETUP

      Initial game setup phase

   .. attribute:: NIGHT

      Night phase where special roles act secretly

   .. attribute:: DAY_DISCUSSION

      Day phase for open discussion

   .. attribute:: DAY_VOTING

      Voting phase to eliminate a player

   .. attribute:: GAME_OVER

      Game has ended

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePhase
      :collapse:

   .. py:attribute:: DAY_DISCUSSION
      :value: 'day_discussion'



   .. py:attribute:: DAY_VOTING
      :value: 'day_voting'



   .. py:attribute:: GAME_OVER
      :value: 'game_over'



   .. py:attribute:: NIGHT
      :value: 'night'



   .. py:attribute:: SETUP
      :value: 'setup'



.. py:class:: MafiaAction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An action taken by a player in the Mafia game.

   This model represents any action a player can take, including speaking,
   voting, and role-specific night actions.

   .. attribute:: player_id

      ID of the player taking the action

      :type: str

   .. attribute:: action_type

      Type of action being taken

      :type: ActionType

   .. attribute:: phase

      Game phase when the action occurs

      :type: GamePhase

   .. attribute:: round_number

      Current round number

      :type: int

   .. attribute:: target_id

      Target player for the action

      :type: Optional[str]

   .. attribute:: message

      Content for speak actions

      :type: Optional[str]

   .. rubric:: Example

   >>> action = MafiaAction(
   ...     player_id="Player_1",
   ...     action_type=ActionType.VOTE,
   ...     phase=GamePhase.DAY_VOTING,
   ...     round_number=1,
   ...     target_id="Player_2"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MafiaAction
      :collapse:

   .. py:method:: __str__() -> str

      Get a human-readable string representation of the action.

      :returns: Description of the action
      :rtype: str


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: to_dict() -> dict[str, Any]

      Convert the action to a dictionary format.

      :returns: Dictionary representation of the action
      :rtype: Dict[str, Any]


      .. autolink-examples:: to_dict
         :collapse:


   .. py:attribute:: action_type
      :type:  ActionType


   .. py:attribute:: message
      :type:  str | None
      :value: None



   .. py:attribute:: phase
      :type:  GamePhase


   .. py:attribute:: player_id
      :type:  str


   .. py:attribute:: round_number
      :type:  int


   .. py:attribute:: target_id
      :type:  str | None
      :value: None



.. py:class:: MafiaPlayerDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A decision made by a player in the Mafia game.

   This model represents the complete decision output from a player's
   LLM, including both the action and reasoning.

   .. attribute:: action

      The action the player will take

      :type: MafiaAction

   .. attribute:: reasoning

      Explanation for the decision

      :type: Optional[str]

   .. rubric:: Example

   >>> decision = MafiaPlayerDecision(
   ...     action=MafiaAction(...),
   ...     reasoning="Player seems suspicious based on voting pattern"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MafiaPlayerDecision
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: action
      :type:  MafiaAction


   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



.. py:class:: MafiaPlayerDecisionSchema(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Schema for LLM to output structured player decisions.

   This model provides a simplified schema for LLM output that can be
   converted into a full MafiaPlayerDecision.

   .. attribute:: action_type

      Type of action to take

      :type: str

   .. attribute:: target_id

      Target player for the action

      :type: Optional[str]

   .. attribute:: message

      Content for speak actions

      :type: Optional[str]

   .. attribute:: reasoning

      Explanation for the decision

      :type: Optional[str]

   .. rubric:: Example

   >>> schema = MafiaPlayerDecisionSchema(
   ...     action_type="vote",
   ...     target_id="Player_2",
   ...     reasoning="Suspicious behavior during discussion"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MafiaPlayerDecisionSchema
      :collapse:

   .. py:class:: Config

      .. py:attribute:: json_schema_extra



   .. py:attribute:: action_type
      :type:  str
      :value: None



   .. py:attribute:: message
      :type:  str | None
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



   .. py:attribute:: target_id
      :type:  str | None
      :value: None



.. py:class:: NarratorAction(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   An action taken by the narrator in the Mafia game.

   This model represents narrator actions that control game flow and
   provide information to players.

   .. attribute:: announcement

      Public message to all players

      :type: Optional[str]

   .. attribute:: player_state_updates

      State changes

      :type: Dict[str, Dict[str, Any]]

   .. attribute:: phase_transition

      Whether to move to next phase

      :type: bool

   .. attribute:: next_phase

      Phase to transition to

      :type: Optional[GamePhase]

   .. attribute:: round_number

      Current round number

      :type: int

   .. rubric:: Example

   >>> action = NarratorAction(
   ...     announcement="Night falls on the village.",
   ...     phase_transition=True,
   ...     next_phase=GamePhase.NIGHT,
   ...     round_number=1
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NarratorAction
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: __str__() -> str

      Get a human-readable string representation of the action.

      :returns: Description of the narrator action
      :rtype: str


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: serialize_next_phase(next_phase: GamePhase | None) -> str | None

      Serialize the next_phase enum to a string.

      :param next_phase: Phase to serialize
      :type next_phase: Optional[GamePhase]

      :returns: String value of the phase or None
      :rtype: Optional[str]


      .. autolink-examples:: serialize_next_phase
         :collapse:


   .. py:attribute:: announcement
      :type:  str | None
      :value: None



   .. py:attribute:: next_phase
      :type:  GamePhase | None
      :value: None



   .. py:attribute:: phase_transition
      :type:  bool
      :value: False



   .. py:attribute:: player_state_updates
      :type:  dict[str, dict[str, Any]]
      :value: None



   .. py:attribute:: round_number
      :type:  int
      :value: 1



.. py:class:: NarratorDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   A decision made by the narrator in the Mafia game.

   This model represents the complete decision output from the narrator's
   LLM, including both the action and reasoning.

   .. attribute:: action

      The action the narrator will take

      :type: NarratorAction

   .. attribute:: reasoning

      Explanation for the decision

      :type: Optional[str]

   .. rubric:: Example

   >>> decision = NarratorDecision(
   ...     action=NarratorAction(...),
   ...     reasoning="All players have completed their night actions"
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NarratorDecision
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: action
      :type:  NarratorAction


   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



.. py:class:: NarratorDecisionSchema(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Schema for LLM to output structured narrator decisions.

   This model provides a simplified schema for LLM output that can be
   converted into a full NarratorDecision.

   .. attribute:: announcement

      Public message to all players

      :type: Optional[str]

   .. attribute:: phase_transition

      Whether to move to next phase

      :type: bool

   .. attribute:: reasoning

      Explanation for the decision

      :type: Optional[str]

   .. rubric:: Example

   >>> schema = NarratorDecisionSchema(
   ...     announcement="The village falls quiet as night approaches.",
   ...     phase_transition=True,
   ...     reasoning="All players have completed their day actions."
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: NarratorDecisionSchema
      :collapse:

   .. py:class:: Config

      .. py:attribute:: json_schema_extra



   .. py:attribute:: announcement
      :type:  str | None
      :value: None



   .. py:attribute:: phase_transition
      :type:  bool
      :value: None



   .. py:attribute:: reasoning
      :type:  str | None
      :value: None



.. py:class:: PlayerRole

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Player role enumeration for the Mafia game.

   This enum defines the possible roles a player can have, each with
   unique abilities and win conditions.

   .. attribute:: VILLAGER

      Basic role with no special abilities

   .. attribute:: MAFIA

      Can kill one player each night

   .. attribute:: DETECTIVE

      Can investigate one player's role each night

   .. attribute:: DOCTOR

      Can protect one player from death each night

   .. attribute:: NARRATOR

      Game master role that manages game flow

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerRole
      :collapse:

   .. py:attribute:: DETECTIVE
      :value: 'detective'



   .. py:attribute:: DOCTOR
      :value: 'doctor'



   .. py:attribute:: MAFIA
      :value: 'mafia'



   .. py:attribute:: NARRATOR
      :value: 'narrator'



   .. py:attribute:: VILLAGER
      :value: 'villager'



.. py:class:: PlayerState(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   State information for a player in the Mafia game.

   This model tracks all information about a player's current state,
   including their role, alive status, and what they know about others.

   .. attribute:: player_id

      Unique identifier for the player

      :type: Optional[str]

   .. attribute:: role

      The player's assigned role

      :type: PlayerRole

   .. attribute:: is_alive

      Whether the player is still alive

      :type: bool

   .. attribute:: known_roles

      Roles known to this player

      :type: Dict[str, PlayerRole]

   .. attribute:: investigation_results

      Detective's investigation results

      :type: Dict[str, bool]

   .. rubric:: Example

   >>> state = PlayerState(
   ...     player_id="Player_1",
   ...     role=PlayerRole.DETECTIVE,
   ...     known_roles={"Player_1": PlayerRole.DETECTIVE}
   ... )

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: PlayerState
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:attribute:: investigation_results
      :type:  dict[str, bool]
      :value: None



   .. py:attribute:: is_alive
      :type:  bool
      :value: True



   .. py:attribute:: known_roles
      :type:  dict[str, PlayerRole]
      :value: None



   .. py:attribute:: player_id
      :type:  str | None
      :value: None



   .. py:attribute:: role
      :type:  PlayerRole


