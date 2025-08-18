games.among_us.models
=====================

.. py:module:: games.among_us.models

Comprehensive data models for Among Us social deduction gameplay.

This module provides sophisticated data models for the Among Us game implementation,
supporting both cooperative crew tasks and deceptive impostor gameplay. The models
enable structured data handling for complex social deduction mechanics, spatial
navigation, task management, and strategic decision-making.

The models support:
- Role-based gameplay (Crewmate vs Impostor)
- Spatial navigation with rooms and vents
- Task management with multiple task types
- Sabotage systems with critical and non-critical events
- Memory and observation tracking for deduction
- Strategic analysis and decision-making
- Meeting and voting mechanics

.. rubric:: Examples

Creating a player with tasks::

    player = PlayerState(
        id="player1",
        role=PlayerRole.CREWMATE,
        location="cafeteria",
        tasks=[
            Task(
                id="task1",
                type=TaskType.SHORT,
                location="electrical",
                description="Fix wiring"
            )
        ]
    )

Impostor actions::

    impostor = PlayerState(
        id="impostor1",
        role=PlayerRole.IMPOSTOR,
        location="medbay"
    )

    # Check kill ability
    if impostor.can_kill(kill_cooldown=0):
        decision = AmongUsPlayerDecision(
            action_type=AmongUsActionType.KILL,
            target_player="player2",
            reasoning="Isolated target in medbay"
        )

Sabotage management::

    sabotage = SabotageEvent(
        type="reactor",
        location="reactor",
        timer=30,
        resolution_points=[
            SabotageResolutionPoint(
                id="reactor_left",
                location="reactor",
                description="Left panel"
            ),
            SabotageResolutionPoint(
                id="reactor_right",
                location="reactor",
                description="Right panel"
            )
        ]
    )

    # Check if critical
    if sabotage.is_critical():
        print("Emergency! Reactor meltdown imminent!")

.. note::

   All models use Pydantic for validation and support both JSON serialization
   and integration with LLM-based strategic decision systems.



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">18 classes</span>   </div>

.. autoapi-nested-parse::

   Comprehensive data models for Among Us social deduction gameplay.

   This module provides sophisticated data models for the Among Us game implementation,
   supporting both cooperative crew tasks and deceptive impostor gameplay. The models
   enable structured data handling for complex social deduction mechanics, spatial
   navigation, task management, and strategic decision-making.

   The models support:
   - Role-based gameplay (Crewmate vs Impostor)
   - Spatial navigation with rooms and vents
   - Task management with multiple task types
   - Sabotage systems with critical and non-critical events
   - Memory and observation tracking for deduction
   - Strategic analysis and decision-making
   - Meeting and voting mechanics

   .. rubric:: Examples

   Creating a player with tasks::

       player = PlayerState(
           id="player1",
           role=PlayerRole.CREWMATE,
           location="cafeteria",
           tasks=[
               Task(
                   id="task1",
                   type=TaskType.SHORT,
                   location="electrical",
                   description="Fix wiring"
               )
           ]
       )

   Impostor actions::

       impostor = PlayerState(
           id="impostor1",
           role=PlayerRole.IMPOSTOR,
           location="medbay"
       )

       # Check kill ability
       if impostor.can_kill(kill_cooldown=0):
           decision = AmongUsPlayerDecision(
               action_type=AmongUsActionType.KILL,
               target_player="player2",
               reasoning="Isolated target in medbay"
           )

   Sabotage management::

       sabotage = SabotageEvent(
           type="reactor",
           location="reactor",
           timer=30,
           resolution_points=[
               SabotageResolutionPoint(
                   id="reactor_left",
                   location="reactor",
                   description="Left panel"
               ),
               SabotageResolutionPoint(
                   id="reactor_right",
                   location="reactor",
                   description="Right panel"
               )
           ]
       )

       # Check if critical
       if sabotage.is_critical():
           print("Emergency! Reactor meltdown imminent!")

   .. note::

      All models use Pydantic for validation and support both JSON serialization
      and integration with LLM-based strategic decision systems.



      
            
            

.. admonition:: Classes (18)
   :class: note

   .. autoapisummary::

      games.among_us.models.AmongUsActionType
      games.among_us.models.AmongUsAnalysis
      games.among_us.models.AmongUsGamePhase
      games.among_us.models.AmongUsPlayerDecision
      games.among_us.models.PlayerMemory
      games.among_us.models.PlayerRole
      games.among_us.models.PlayerState
      games.among_us.models.Room
      games.among_us.models.RoomConnection
      games.among_us.models.SabotageEvent
      games.among_us.models.SabotageResolutionPoint
      games.among_us.models.SabotageStatus
      games.among_us.models.SabotageType
      games.among_us.models.Task
      games.among_us.models.TaskStatus
      games.among_us.models.TaskType
      games.among_us.models.Vent
      games.among_us.models.VentConnection

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsActionType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            All possible player actions in Among Us.

            Actions are phase-dependent and role-restricted:
            - Movement and tasks: Available to all during task phase
            - Kill/Sabotage/Vent: Impostor-only actions
            - Report/Meeting: Emergency actions
            - Vote/Skip: Meeting phase only

            Values:
                MOVE: Travel between connected rooms
                DO_TASK: Perform assigned task (crewmates)
                KILL: Eliminate a player (impostors)
                SABOTAGE: Trigger map disruption (impostors)
                USE_VENT: Enter/exit ventilation (impostors)
                REPORT_BODY: Report a discovered body
                CALL_MEETING: Call emergency meeting
                VOTE: Vote to eject a player
                SKIP_VOTE: Vote to skip ejection


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CALL_MEETING
               :value: 'call_meeting'



            .. py:attribute:: DO_TASK
               :value: 'do_task'



            .. py:attribute:: KILL
               :value: 'kill'



            .. py:attribute:: MOVE
               :value: 'move'



            .. py:attribute:: REPORT_BODY
               :value: 'report_body'



            .. py:attribute:: SABOTAGE
               :value: 'sabotage'



            .. py:attribute:: SKIP_VOTE
               :value: 'skip_vote'



            .. py:attribute:: USE_VENT
               :value: 'use_vent'



            .. py:attribute:: VOTE
               :value: 'vote'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Comprehensive game state analysis for strategic planning.

            Provides high-level analysis of the current game situation,
            including win probability, player suspicions, and strategic
            recommendations. Used by AI agents for decision-making.

            .. attribute:: game_phase

               Current game phase.

               :type: AmongUsGamePhase

            .. attribute:: crew_advantage

               Balance of power (-1 to +1).

               :type: float

            .. attribute:: task_completion_percentage

               Overall task progress.

               :type: float

            .. attribute:: suspected_impostors

               Likely impostor IDs.

               :type: List[str]

            .. attribute:: trusted_players

               Confirmed crewmate IDs.

               :type: List[str]

            .. attribute:: active_sabotages

               Current sabotage types.

               :type: List[str]

            .. attribute:: recommended_strategy

               Strategic advice.

               :type: str

            .. attribute:: risk_assessment

               Current danger evaluation.

               :type: str

            .. attribute:: priority_actions

               Urgent actions needed.

               :type: List[str]

            .. rubric:: Examples

            Early game analysis::

                analysis = AmongUsAnalysis(
                    game_phase=AmongUsGamePhase.TASKS,
                    crew_advantage=0.0,
                    task_completion_percentage=15.0,
                    suspected_impostors=[],
                    trusted_players=["Green"],  # Did visual task
                    active_sabotages=[],
                    recommended_strategy="Focus on tasks, stay in groups",
                    risk_assessment="Low risk, no suspicious behavior yet",
                    priority_actions=["Complete tasks", "Observe players"]
                )

            Critical situation::

                analysis = AmongUsAnalysis(
                    game_phase=AmongUsGamePhase.TASKS,
                    crew_advantage=-0.7,
                    task_completion_percentage=80.0,
                    suspected_impostors=["Red", "Purple"],
                    trusted_players=["Blue", "Green"],
                    active_sabotages=["reactor"],
                    recommended_strategy="Fix reactor immediately!",
                    risk_assessment="Critical: reactor meltdown imminent",
                    priority_actions=["Fix reactor", "Stay together"]
                )

            Meeting phase analysis::

                analysis = AmongUsAnalysis(
                    game_phase=AmongUsGamePhase.VOTING,
                    crew_advantage=-0.3,
                    task_completion_percentage=60.0,
                    suspected_impostors=["Red"],
                    trusted_players=["Blue", "Green", "Yellow"],
                    active_sabotages=[],
                    recommended_strategy="Vote Red based on venting evidence",
                    risk_assessment="High stakes vote - wrong choice loses game",
                    priority_actions=["Vote Red", "Share observations"]
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_priority_actions(v: list[str]) -> list[str]
               :classmethod:


               Ensure priority actions list is reasonable length.

               :param v: Priority actions to validate.
               :type v: List[str]

               :returns: Validated actions list.
               :rtype: List[str]

               :raises ValueError: If too many priorities listed.



            .. py:attribute:: active_sabotages
               :type:  list[str]
               :value: None



            .. py:attribute:: crew_advantage
               :type:  float
               :value: None



            .. py:attribute:: game_phase
               :type:  AmongUsGamePhase
               :value: None



            .. py:property:: game_stage
               :type: str


               Classify game progression stage.

               :returns: Early, mid, or late game classification.
               :rtype: str


            .. py:property:: is_emergency
               :type: bool


               Check if situation requires immediate action.

               :returns: True if critical sabotages active or crew disadvantaged.
               :rtype: bool


            .. py:attribute:: model_config

               Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


            .. py:attribute:: priority_actions
               :type:  list[str]
               :value: None



            .. py:attribute:: recommended_strategy
               :type:  str
               :value: None



            .. py:attribute:: risk_assessment
               :type:  str
               :value: None



            .. py:attribute:: suspected_impostors
               :type:  list[str]
               :value: None



            .. py:attribute:: task_completion_percentage
               :type:  float
               :value: None



            .. py:attribute:: trusted_players
               :type:  list[str]
               :value: None



            .. py:property:: win_probability
               :type: dict[str, float]


               Estimate win probability for each team.

               :returns: Win chances for crew and impostors.
               :rtype: Dict[str, float]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsGamePhase

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Current phase of gameplay.

            Game alternates between task/action phases and discussion/voting.

            Values:
                TASKS: Normal gameplay with movement and actions
                MEETING: Discussion phase after body report or emergency
                VOTING: Active voting to eject a player
                GAME_OVER: Game concluded with winner determined


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: GAME_OVER
               :value: 'game_over'



            .. py:attribute:: MEETING
               :value: 'meeting'



            .. py:attribute:: TASKS
               :value: 'tasks'



            .. py:attribute:: VOTING
               :value: 'voting'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: AmongUsPlayerDecision(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Strategic decision model for player actions.

            Encapsulates a player's chosen action with reasoning and confidence.
            Used by AI agents to make informed decisions based on game state
            and objectives. Includes justification for social deduction.

            .. attribute:: action_type

               Chosen action to perform.

               :type: AmongUsActionType

            .. attribute:: target_location

               Destination for movement.

               :type: Optional[str]

            .. attribute:: target_player

               Target for kill/vote actions.

               :type: Optional[str]

            .. attribute:: target_task

               Task ID to attempt.

               :type: Optional[str]

            .. attribute:: reasoning

               Strategic justification for action.

               :type: str

            .. attribute:: confidence

               Confidence level in decision (0-1).

               :type: float

            .. rubric:: Examples

            Crewmate task decision::

                decision = AmongUsPlayerDecision(
                    action_type=AmongUsActionType.DO_TASK,
                    target_task="fix_wiring_1",
                    reasoning="Completing tasks helps crew win",
                    confidence=0.9
                )

            Impostor kill decision::

                decision = AmongUsPlayerDecision(
                    action_type=AmongUsActionType.KILL,
                    target_player="Blue",
                    reasoning="Blue is isolated in electrical",
                    confidence=0.8
                )

            Strategic movement::

                decision = AmongUsPlayerDecision(
                    action_type=AmongUsActionType.MOVE,
                    target_location="medbay",
                    reasoning="Need to establish alibi with visual task",
                    confidence=0.7
                )

            Voting decision::

                decision = AmongUsPlayerDecision(
                    action_type=AmongUsActionType.VOTE,
                    target_player="Red",
                    reasoning="Red was seen venting by Green",
                    confidence=0.95
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_location_for_action(v: str | None, info) -> str | None
               :classmethod:


               Ensure target location is provided for movement actions.

               :param v: Target location value.
               :type v: Optional[str]
               :param info: Validation context with other fields.

               :returns: Validated location.
               :rtype: Optional[str]

               :raises ValueError: If location missing for movement.



            .. py:attribute:: action_type
               :type:  AmongUsActionType
               :value: None



            .. py:attribute:: confidence
               :type:  float
               :value: None



            .. py:property:: is_aggressive_action
               :type: bool


               Check if action is aggressive/hostile.

               :returns: True for kill/sabotage actions.
               :rtype: bool


            .. py:attribute:: reasoning
               :type:  str
               :value: None



            .. py:property:: requires_target_player
               :type: bool


               Check if action needs a target player.

               :returns: True for kill/vote actions.
               :rtype: bool


            .. py:attribute:: target_location
               :type:  str | None
               :value: None



            .. py:attribute:: target_player
               :type:  str | None
               :value: None



            .. py:attribute:: target_task
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerMemory(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Cognitive model for player observations and deductions.

            Tracks what a player has observed and deduced during gameplay,
            forming the basis for social deduction. Memory includes direct
            observations, suspicion levels, alibis, and movement patterns.

            .. attribute:: observations

               Chronological list of observations.

               :type: List[str]

            .. attribute:: player_suspicions

               Suspicion levels (0-1) per player.

               :type: Dict[str, float]

            .. attribute:: player_alibis

               Last known locations of players.

               :type: Dict[str, str]

            .. attribute:: location_history

               Recent rooms visited by this player.

               :type: List[str]

            .. rubric:: Examples

            Tracking suspicious behavior::

                memory = PlayerMemory(
                    observations=[
                        "Saw Red near body in electrical",
                        "Blue was alone in medbay",
                        "Green completed visual task"
                    ],
                    player_suspicions={
                        "Red": 0.8,
                        "Blue": 0.4,
                        "Green": 0.0
                    }
                )

            Building alibis::

                memory.player_alibis = {
                    "Red": "electrical",
                    "Blue": "medbay",
                    "Green": "cafeteria"
                }

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: validate_suspicion_levels(v: dict[str, float]) -> dict[str, float]
               :classmethod:


               Ensure suspicion levels are within valid range.

               :param v: Suspicion dictionary to validate.
               :type v: Dict[str, float]

               :returns: Validated suspicion levels.
               :rtype: Dict[str, float]

               :raises ValueError: If suspicion level outside 0-1 range.



            .. py:attribute:: location_history
               :type:  list[str]
               :value: None



            .. py:property:: most_suspicious
               :type: str | None


               Identify the most suspicious player.

               :returns: Player ID with highest suspicion or None.
               :rtype: Optional[str]


            .. py:attribute:: observations
               :type:  list[str]
               :value: None



            .. py:attribute:: player_alibis
               :type:  dict[str, str]
               :value: None



            .. py:attribute:: player_suspicions
               :type:  dict[str, float]
               :value: None



            .. py:property:: trusted_players
               :type: list[str]


               List players with low suspicion (< 0.3).

               :returns: IDs of trusted players.
               :rtype: List[str]



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerRole

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Player roles defining objectives and abilities.

            Determines the player's win condition and available actions:
            - Crewmates: Complete tasks and identify impostors
            - Impostors: Eliminate crew and avoid detection

            Values:
                CREWMATE: Innocent crew member focused on tasks
                IMPOSTOR: Deceptive player who can kill and sabotage


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CREWMATE
               :value: 'crewmate'



            .. py:attribute:: IMPOSTOR
               :value: 'impostor'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PlayerState(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Complete state representation for a player in Among Us.

            Encapsulates all information about a player including their role,
            location, tasks, survival status, and cognitive state. Supports
            both crewmate and impostor gameplay with appropriate abilities.

            .. attribute:: id

               Unique player identifier.

               :type: str

            .. attribute:: role

               Crewmate or Impostor designation.

               :type: PlayerRole

            .. attribute:: location

               Current room location.

               :type: str

            .. attribute:: tasks

               Assigned tasks (empty for impostors).

               :type: List[Task]

            .. attribute:: is_alive

               Whether player is still active.

               :type: bool

            .. attribute:: last_action

               Most recent action taken.

               :type: Optional[str]

            .. attribute:: observations

               Direct observations this turn.

               :type: List[str]

            .. attribute:: in_vent

               Whether currently hiding in vent.

               :type: bool

            .. attribute:: current_vent

               ID of occupied vent.

               :type: Optional[str]

            .. attribute:: memory

               Cognitive state and deductions.

               :type: PlayerMemory

            .. rubric:: Examples

            Crewmate with tasks::

                crewmate = PlayerState(
                    id="Blue",
                    role=PlayerRole.CREWMATE,
                    location="electrical",
                    tasks=[
                        Task(id="wire1", type=TaskType.COMMON,
                             location="electrical", description="Fix wiring"),
                        Task(id="scan1", type=TaskType.VISUAL,
                             location="medbay", description="Submit to scan")
                    ]
                )

            Impostor in vent::

                impostor = PlayerState(
                    id="Red",
                    role=PlayerRole.IMPOSTOR,
                    location="electrical",
                    tasks=[],
                    in_vent=True,
                    current_vent="electrical_vent"
                )

            Dead player::

                ghost = PlayerState(
                    id="Green",
                    role=PlayerRole.CREWMATE,
                    location="cafeteria",
                    tasks=[],
                    is_alive=False
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: can_kill(kill_cooldown: int = 0) -> bool

               Check if the player can perform a kill action.

               Kill ability requires:
               - Impostor role
               - Being alive
               - Kill cooldown expired
               - Not currently in vent

               :param kill_cooldown: Remaining cooldown seconds.
               :type kill_cooldown: int

               :returns: True if all conditions met for killing.
               :rtype: bool

               .. rubric:: Examples

               >>> impostor = PlayerState(id="Red", role=PlayerRole.IMPOSTOR,
               ...                        location="electrical", is_alive=True)
               >>> impostor.can_kill(kill_cooldown=0)
               True
               >>> impostor.can_kill(kill_cooldown=10)
               False



            .. py:method:: can_use_vent() -> bool

               Check if the player can use ventilation systems.

               Vent usage requires:
               - Impostor role
               - Being alive

               :returns: True if player can enter/exit vents.
               :rtype: bool

               .. rubric:: Examples

               >>> impostor = PlayerState(id="Red", role=PlayerRole.IMPOSTOR,
               ...                        location="electrical", is_alive=True)
               >>> impostor.can_use_vent()
               True



            .. py:method:: is_crewmate() -> bool

               Check if the player is a crewmate.

               :returns: True if player has crewmate role.
               :rtype: bool

               .. rubric:: Examples

               >>> crew = PlayerState(id="Blue", role=PlayerRole.CREWMATE, location="cafeteria")
               >>> crew.is_crewmate()
               True



            .. py:method:: is_impostor() -> bool

               Check if the player is an impostor.

               :returns: True if player has impostor role.
               :rtype: bool

               .. rubric:: Examples

               >>> impostor = PlayerState(id="Red", role=PlayerRole.IMPOSTOR, location="cafeteria")
               >>> impostor.is_impostor()
               True



            .. py:attribute:: current_vent
               :type:  str | None
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: in_vent
               :type:  bool
               :value: None



            .. py:property:: incomplete_tasks
               :type: list[Task]


               Get list of uncompleted tasks.

               :returns: Tasks that still need completion.
               :rtype: List[Task]


            .. py:attribute:: is_alive
               :type:  bool
               :value: None



            .. py:property:: is_ghost
               :type: bool


               Check if player is a ghost (dead but still participating).

               :returns: True if player is dead.
               :rtype: bool


            .. py:attribute:: last_action
               :type:  str | None
               :value: None



            .. py:attribute:: location
               :type:  str
               :value: None



            .. py:attribute:: memory
               :type:  PlayerMemory
               :value: None



            .. py:attribute:: observations
               :type:  list[str]
               :value: None



            .. py:attribute:: role
               :type:  PlayerRole
               :value: None



            .. py:property:: task_completion_rate
               :type: float


               Calculate percentage of tasks completed.

               :returns: Completion percentage (0.0-100.0).
               :rtype: float


            .. py:attribute:: tasks
               :type:  list[Task]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Room(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Physical location on the game map.

            Rooms are the primary spaces where gameplay occurs. Players move
            between rooms, complete tasks in specific rooms, and use room
            layout for strategic positioning. Some rooms contain vents for
            impostor movement.

            .. attribute:: id

               Unique room identifier.

               :type: str

            .. attribute:: name

               Display name for the room.

               :type: str

            .. attribute:: connections

               Adjacent room connections.

               :type: List[RoomConnection]

            .. attribute:: vents

               IDs of vents in this room.

               :type: List[str]

            .. rubric:: Examples

            Central hub room::

                cafeteria = Room(
                    id="cafeteria",
                    name="Cafeteria",
                    connections=[
                        RoomConnection(target_room="upper_engine"),
                        RoomConnection(target_room="medbay"),
                        RoomConnection(target_room="admin")
                    ]
                )

            Task room with vent::

                electrical = Room(
                    id="electrical",
                    name="Electrical",
                    connections=[
                        RoomConnection(target_room="storage"),
                        RoomConnection(target_room="lower_engine")
                    ],
                    vents=["electrical_vent"]
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: get_connection(room_id: str) -> RoomConnection | None

               Get the connection to another room if it exists.

               :param room_id: ID of the target room.
               :type room_id: str

               :returns: Connection object or None.
               :rtype: Optional[RoomConnection]

               .. rubric:: Examples

               >>> conn = cafeteria.get_connection("medbay")
               >>> conn.distance
               1



            .. py:method:: is_connected_to(room_id: str) -> bool

               Check if this room directly connects to another room.

               :param room_id: ID of the target room.
               :type room_id: str

               :returns: True if rooms are directly connected.
               :rtype: bool

               .. rubric:: Examples

               >>> cafeteria.is_connected_to("medbay")
               True
               >>> cafeteria.is_connected_to("reactor")
               False



            .. py:property:: connection_count
               :type: int


               Count number of room connections.

               :returns: Total adjacent rooms.
               :rtype: int


            .. py:attribute:: connections
               :type:  list[RoomConnection]
               :value: None



            .. py:property:: has_vent
               :type: bool


               Check if room contains any vents.

               :returns: True if room has vents for impostor use.
               :rtype: bool


            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str
               :value: None



            .. py:attribute:: vents
               :type:  list[str]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: RoomConnection(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Physical connection between adjacent rooms.

            Represents hallways and passages between rooms, defining the map
            topology. Connections can be blocked by door sabotages, forcing
            players to find alternate routes.

            .. attribute:: target_room

               ID of the connected room.

               :type: str

            .. attribute:: distance

               Travel time in seconds.

               :type: int

            .. attribute:: is_blocked

               Whether passage is sabotage-blocked.

               :type: bool

            .. rubric:: Examples

            Standard hallway::

                connection = RoomConnection(
                    target_room="cafeteria",
                    distance=1
                )

            Long corridor::

                connection = RoomConnection(
                    target_room="reactor",
                    distance=3
                )

            Sabotaged door::

                connection = RoomConnection(
                    target_room="electrical",
                    distance=1,
                    is_blocked=True
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: distance
               :type:  int
               :value: None



            .. py:attribute:: is_blocked
               :type:  bool
               :value: None



            .. py:attribute:: target_room
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SabotageEvent(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Active sabotage affecting gameplay.

            Represents an ongoing sabotage that disrupts normal gameplay.
            Critical sabotages have timers and can end the game, while
            non-critical sabotages create tactical advantages.

            .. attribute:: type

               Type of sabotage from SabotageType.

               :type: str

            .. attribute:: location

               Primary affected location.

               :type: str

            .. attribute:: timer

               Seconds until critical failure.

               :type: int

            .. attribute:: resolved

               Whether sabotage is fixed.

               :type: bool

            .. attribute:: resolution_points

               Fix locations.

               :type: List[SabotageResolutionPoint]

            .. rubric:: Examples

            Critical reactor sabotage::

                sabotage = SabotageEvent(
                    type="reactor",
                    location="reactor",
                    timer=30,
                    resolution_points=[
                        SabotageResolutionPoint(
                            id="reactor_left",
                            location="reactor",
                            description="Left panel"
                        ),
                        SabotageResolutionPoint(
                            id="reactor_right",
                            location="reactor",
                            description="Right panel"
                        )
                    ]
                )

            Non-critical lights sabotage::

                sabotage = SabotageEvent(
                    type="lights",
                    location="electrical",
                    timer=0,  # No timer for non-critical
                    resolution_points=[
                        SabotageResolutionPoint(
                            id="light_panel",
                            location="electrical",
                            description="Fix light switches"
                        )
                    ]
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: is_critical() -> bool

               Check if this is a game-ending critical sabotage.

               Critical sabotages (O2, Reactor) can end the game if not
               resolved within the time limit.

               :returns: True if sabotage is critical.
               :rtype: bool

               .. rubric:: Examples

               >>> reactor = SabotageEvent(type="reactor", location="reactor", timer=30)
               >>> reactor.is_critical()
               True
               >>> lights = SabotageEvent(type="lights", location="electrical", timer=0)
               >>> lights.is_critical()
               False



            .. py:method:: is_resolved() -> bool

               Check if the sabotage is fully resolved.

               Sabotage is resolved when either marked resolved or all
               resolution points are activated.

               :returns: True if sabotage is fixed.
               :rtype: bool

               .. rubric:: Examples

               >>> sabotage = SabotageEvent(type="reactor", location="reactor", timer=30)
               >>> sabotage.is_resolved()
               False
               >>> sabotage.resolved = True
               >>> sabotage.is_resolved()
               True



            .. py:attribute:: location
               :type:  str
               :value: None



            .. py:property:: points_remaining
               :type: int


               Count unresolved resolution points.

               :returns: Number of points still needing activation.
               :rtype: int


            .. py:attribute:: resolution_points
               :type:  list[SabotageResolutionPoint]
               :value: None



            .. py:attribute:: resolved
               :type:  bool
               :value: None



            .. py:attribute:: timer
               :type:  int
               :value: None



            .. py:attribute:: type
               :type:  str
               :value: None



            .. py:property:: urgency_level
               :type: str


               Determine urgency of addressing this sabotage.

               :returns: Urgency classification.
               :rtype: str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SabotageResolutionPoint(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Interactive point for resolving sabotages.

            Critical sabotages require multiple resolution points to be
            activated simultaneously (e.g., reactor needs two players).
            Non-critical sabotages may have single resolution points.

            .. attribute:: id

               Unique identifier for this point.

               :type: str

            .. attribute:: location

               Room containing the resolution point.

               :type: str

            .. attribute:: description

               What needs to be done here.

               :type: str

            .. attribute:: resolved

               Whether this point is activated.

               :type: bool

            .. attribute:: resolver_id

               Player who resolved this.

               :type: Optional[str]

            .. rubric:: Examples

            Reactor resolution point::

                point = SabotageResolutionPoint(
                    id="reactor_left",
                    location="reactor",
                    description="Hold left reactor panel"
                )

            O2 resolution point::

                point = SabotageResolutionPoint(
                    id="o2_admin",
                    location="admin",
                    description="Enter O2 code in admin"
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: location
               :type:  str
               :value: None



            .. py:attribute:: resolved
               :type:  bool
               :value: None



            .. py:attribute:: resolver_id
               :type:  str | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SabotageStatus

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Current state of a sabotage event.

            Values:
                ACTIVE: Sabotage in effect, needs resolution
                RESOLVED: Successfully fixed by crewmates
                FAILED: Timer expired on critical sabotage (impostor win)


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ACTIVE
               :value: 'active'



            .. py:attribute:: FAILED
               :value: 'failed'



            .. py:attribute:: RESOLVED
               :value: 'resolved'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SabotageType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of sabotage available to impostors.

            Sabotages disrupt crewmate activities and create opportunities
            for kills. Critical sabotages can end the game if not resolved.

            Values:
                LIGHTS: Reduces crewmate vision radius
                COMMS: Hides task list and prevents meetings
                OXYGEN: Critical - requires two-point fix within time limit
                REACTOR: Critical - requires two-point fix within time limit
                DOORS: Locks specific room doors temporarily


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: COMMS
               :value: 'comms'



            .. py:attribute:: DOORS
               :value: 'doors'



            .. py:attribute:: LIGHTS
               :value: 'lights'



            .. py:attribute:: OXYGEN
               :value: 'o2'



            .. py:attribute:: REACTOR
               :value: 'reactor'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Task(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Individual task assignment for crewmates.

            Tasks are the primary objective for crewmates, requiring them to visit
            specific locations and complete mini-games. Visual tasks can prove
            innocence by showing animations to nearby players.

            .. attribute:: id

               Unique task identifier.

               :type: str

            .. attribute:: type

               Category of task affecting behavior.

               :type: TaskType

            .. attribute:: location

               Room where task must be performed.

               :type: str

            .. attribute:: description

               Human-readable task description.

               :type: str

            .. attribute:: status

               Current completion state.

               :type: TaskStatus

            .. attribute:: visual_indicator

               Whether task shows visible proof.

               :type: bool

            .. rubric:: Examples

            Visual task proving innocence::

                task = Task(
                    id="medbay_scan",
                    type=TaskType.VISUAL,
                    location="medbay",
                    description="Submit to medbay scan",
                    visual_indicator=True
                )

            Common electrical task::

                task = Task(
                    id="fix_wiring",
                    type=TaskType.COMMON,
                    location="electrical",
                    description="Fix wiring"
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:property:: completion_percentage
               :type: float


               Calculate task completion percentage.

               :returns: 0.0 for not started, 0.5 for in progress, 1.0 for completed.
               :rtype: float


            .. py:attribute:: description
               :type:  str
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:property:: is_completed
               :type: bool


               Check if task is fully completed.

               :returns: True if task status is COMPLETED.
               :rtype: bool


            .. py:attribute:: location
               :type:  str
               :value: None



            .. py:attribute:: status
               :type:  TaskStatus
               :value: None



            .. py:attribute:: type
               :type:  TaskType
               :value: None



            .. py:attribute:: visual_indicator
               :type:  bool
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TaskStatus

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Task completion status for tracking progress.

            Values:
                NOT_STARTED: Task not yet attempted
                IN_PROGRESS: Task partially completed
                COMPLETED: Task fully finished


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: COMPLETED
               :value: 'completed'



            .. py:attribute:: IN_PROGRESS
               :value: 'in_progress'



            .. py:attribute:: NOT_STARTED
               :value: 'not_started'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TaskType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Types of tasks with different characteristics.

            Task types affect completion time and verification:
            - Visual tasks provide visible proof of innocence
            - Common tasks are shared by all crewmates
            - Short/Long tasks vary in completion time

            Values:
                VISUAL: Tasks with visible animations (proves innocence)
                COMMON: Tasks assigned to all crewmates
                SHORT: Quick tasks (1-3 seconds)
                LONG: Extended tasks (5-10 seconds)


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: COMMON
               :value: 'common'



            .. py:attribute:: LONG
               :value: 'long'



            .. py:attribute:: SHORT
               :value: 'short'



            .. py:attribute:: VISUAL
               :value: 'visual'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Vent(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Ventilation system access point for impostor movement.

            Vents are strategic tools exclusive to impostors, allowing rapid
            movement between connected locations while avoiding detection.
            Each vent can connect to multiple other vents forming a network.

            .. attribute:: id

               Unique vent identifier.

               :type: str

            .. attribute:: location

               Room containing this vent.

               :type: str

            .. attribute:: connections

               Available vent routes.

               :type: List[VentConnection]

            .. rubric:: Examples

            Central vent hub::

                vent = Vent(
                    id="electrical_vent",
                    location="electrical",
                    connections=[
                        VentConnection(target_vent_id="medbay_vent"),
                        VentConnection(target_vent_id="security_vent")
                    ]
                )

            Isolated vent::

                vent = Vent(
                    id="reactor_vent",
                    location="reactor",
                    connections=[
                        VentConnection(
                            target_vent_id="upper_engine_vent",
                            travel_time=3
                        )
                    ]
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:property:: connection_count
               :type: int


               Count number of connected vents.

               :returns: Total number of vent connections.
               :rtype: int


            .. py:attribute:: connections
               :type:  list[VentConnection]
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:property:: is_connected
               :type: bool


               Check if vent has any connections.

               :returns: True if vent connects to other vents.
               :rtype: bool


            .. py:attribute:: location
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: VentConnection(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Connection between two vents for impostor movement.

            Vents provide secret passages for impostors to move quickly and
            unseen between locations. Travel time simulates crawling through
            ventilation systems.

            .. attribute:: target_vent_id

               ID of the connected vent.

               :type: str

            .. attribute:: travel_time

               Seconds required to traverse connection.

               :type: int

            .. rubric:: Examples

            Fast vent connection::

                connection = VentConnection(
                    target_vent_id="medbay_vent",
                    travel_time=1
                )

            Distant vent connection::

                connection = VentConnection(
                    target_vent_id="reactor_vent",
                    travel_time=4
                )

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:attribute:: target_vent_id
               :type:  str
               :value: None



            .. py:attribute:: travel_time
               :type:  int
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.among_us.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

