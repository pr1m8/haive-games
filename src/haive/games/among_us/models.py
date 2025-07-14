"""Comprehensive data models for Among Us social deduction gameplay.

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

Examples:
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

Note:
    All models use Pydantic for validation and support both JSON serialization
    and integration with LLM-based strategic decision systems.
"""

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, computed_field, field_validator


class PlayerRole(str, Enum):
    """Player roles defining objectives and abilities.

    Determines the player's win condition and available actions:
    - Crewmates: Complete tasks and identify impostors
    - Impostors: Eliminate crew and avoid detection

    Values:
        CREWMATE: Innocent crew member focused on tasks
        IMPOSTOR: Deceptive player who can kill and sabotage
    """

    CREWMATE = "crewmate"
    IMPOSTOR = "impostor"


class TaskType(str, Enum):
    """Types of tasks with different characteristics.

    Task types affect completion time and verification:
    - Visual tasks provide visible proof of innocence
    - Common tasks are shared by all crewmates
    - Short/Long tasks vary in completion time

    Values:
        VISUAL: Tasks with visible animations (proves innocence)
        COMMON: Tasks assigned to all crewmates
        SHORT: Quick tasks (1-3 seconds)
        LONG: Extended tasks (5-10 seconds)
    """

    VISUAL = "visual"
    COMMON = "common"
    SHORT = "short"
    LONG = "long"


class TaskStatus(str, Enum):
    """Task completion status for tracking progress.

    Values:
        NOT_STARTED: Task not yet attempted
        IN_PROGRESS: Task partially completed
        COMPLETED: Task fully finished
    """

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task(BaseModel):
    """Individual task assignment for crewmates.

    Tasks are the primary objective for crewmates, requiring them to visit
    specific locations and complete mini-games. Visual tasks can prove
    innocence by showing animations to nearby players.

    Attributes:
        id (str): Unique task identifier.
        type (TaskType): Category of task affecting behavior.
        location (str): Room where task must be performed.
        description (str): Human-readable task description.
        status (TaskStatus): Current completion state.
        visual_indicator (bool): Whether task shows visible proof.

    Examples:
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
    """

    id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique identifier for the task",
        examples=["fix_wiring_1", "medbay_scan", "download_data"],
    )

    type: TaskType = Field(
        ...,
        description="Category determining task behavior and timing",
        examples=[TaskType.VISUAL, TaskType.SHORT],
    )

    location: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Room ID where task must be performed",
        examples=["electrical", "medbay", "cafeteria", "reactor"],
    )

    description: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Human-readable description of the task",
        examples=["Fix wiring in electrical", "Submit to medbay scan", "Empty garbage"],
    )

    status: TaskStatus = Field(
        default=TaskStatus.NOT_STARTED,
        description="Current completion state of the task",
    )

    visual_indicator: bool = Field(
        default=False,
        description="Whether task completion is visibly shown to nearby players",
    )

    @computed_field
    @property
    def is_completed(self) -> bool:
        """Check if task is fully completed.

        Returns:
            bool: True if task status is COMPLETED.
        """
        return self.status == TaskStatus.COMPLETED

    @computed_field
    @property
    def completion_percentage(self) -> float:
        """Calculate task completion percentage.

        Returns:
            float: 0.0 for not started, 0.5 for in progress, 1.0 for completed.
        """
        if self.status == TaskStatus.NOT_STARTED:
            return 0.0
        elif self.status == TaskStatus.IN_PROGRESS:
            return 0.5
        else:
            return 1.0


class VentConnection(BaseModel):
    """Connection between two vents for impostor movement.

    Vents provide secret passages for impostors to move quickly and
    unseen between locations. Travel time simulates crawling through
    ventilation systems.

    Attributes:
        target_vent_id (str): ID of the connected vent.
        travel_time (int): Seconds required to traverse connection.

    Examples:
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
    """

    target_vent_id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="ID of the destination vent",
        examples=["medbay_vent", "electrical_vent", "reactor_vent"],
    )

    travel_time: int = Field(
        default=2,
        ge=1,
        le=10,
        description="Time in seconds to travel through the vent",
        examples=[1, 2, 3, 5],
    )


class Vent(BaseModel):
    """Ventilation system access point for impostor movement.

    Vents are strategic tools exclusive to impostors, allowing rapid
    movement between connected locations while avoiding detection.
    Each vent can connect to multiple other vents forming a network.

    Attributes:
        id (str): Unique vent identifier.
        location (str): Room containing this vent.
        connections (List[VentConnection]): Available vent routes.

    Examples:
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
    """

    id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique identifier for the vent",
        examples=["electrical_vent", "medbay_vent", "cafeteria_vent"],
    )

    location: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Room ID where vent is located",
        examples=["electrical", "medbay", "reactor"],
    )

    connections: List[VentConnection] = Field(
        default_factory=list,
        description="List of connected vents forming the vent network",
    )

    @computed_field
    @property
    def is_connected(self) -> bool:
        """Check if vent has any connections.

        Returns:
            bool: True if vent connects to other vents.
        """
        return len(self.connections) > 0

    @computed_field
    @property
    def connection_count(self) -> int:
        """Count number of connected vents.

        Returns:
            int: Total number of vent connections.
        """
        return len(self.connections)


class RoomConnection(BaseModel):
    """Physical connection between adjacent rooms.

    Represents hallways and passages between rooms, defining the map
    topology. Connections can be blocked by door sabotages, forcing
    players to find alternate routes.

    Attributes:
        target_room (str): ID of the connected room.
        distance (int): Travel time in seconds.
        is_blocked (bool): Whether passage is sabotage-blocked.

    Examples:
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
    """

    target_room: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="ID of the connected room",
        examples=["cafeteria", "electrical", "reactor", "medbay"],
    )

    distance: int = Field(
        default=1,
        ge=1,
        le=5,
        description="Travel time in seconds between rooms",
        examples=[1, 2, 3],
    )

    is_blocked: bool = Field(
        default=False, description="Whether connection is blocked by door sabotage"
    )


class Room(BaseModel):
    """Physical location on the game map.

    Rooms are the primary spaces where gameplay occurs. Players move
    between rooms, complete tasks in specific rooms, and use room
    layout for strategic positioning. Some rooms contain vents for
    impostor movement.

    Attributes:
        id (str): Unique room identifier.
        name (str): Display name for the room.
        connections (List[RoomConnection]): Adjacent room connections.
        vents (List[str]): IDs of vents in this room.

    Examples:
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
    """

    id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique identifier for the room",
        examples=["cafeteria", "electrical", "reactor", "medbay"],
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Human-readable room name",
        examples=["Cafeteria", "Electrical", "Reactor", "MedBay"],
    )

    connections: List[RoomConnection] = Field(
        default_factory=list, description="List of connections to adjacent rooms"
    )

    vents: List[str] = Field(
        default_factory=list, description="List of vent IDs present in this room"
    )

    def is_connected_to(self, room_id: str) -> bool:
        """Check if this room directly connects to another room.

        Args:
            room_id (str): ID of the target room.

        Returns:
            bool: True if rooms are directly connected.

        Examples:
            >>> cafeteria.is_connected_to("medbay")
            True
            >>> cafeteria.is_connected_to("reactor")
            False
        """
        return any(conn.target_room == room_id for conn in self.connections)

    def get_connection(self, room_id: str) -> Optional[RoomConnection]:
        """Get the connection to another room if it exists.

        Args:
            room_id (str): ID of the target room.

        Returns:
            Optional[RoomConnection]: Connection object or None.

        Examples:
            >>> conn = cafeteria.get_connection("medbay")
            >>> conn.distance
            1
        """
        for conn in self.connections:
            if conn.target_room == room_id:
                return conn
        return None

    @computed_field
    @property
    def has_vent(self) -> bool:
        """Check if room contains any vents.

        Returns:
            bool: True if room has vents for impostor use.
        """
        return len(self.vents) > 0

    @computed_field
    @property
    def connection_count(self) -> int:
        """Count number of room connections.

        Returns:
            int: Total adjacent rooms.
        """
        return len(self.connections)


class PlayerMemory(BaseModel):
    """Cognitive model for player observations and deductions.

    Tracks what a player has observed and deduced during gameplay,
    forming the basis for social deduction. Memory includes direct
    observations, suspicion levels, alibis, and movement patterns.

    Attributes:
        observations (List[str]): Chronological list of observations.
        player_suspicions (Dict[str, float]): Suspicion levels (0-1) per player.
        player_alibis (Dict[str, str]): Last known locations of players.
        location_history (List[str]): Recent rooms visited by this player.

    Examples:
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
    """

    observations: List[str] = Field(
        default_factory=list,
        description="Chronological list of observations and events witnessed",
        examples=[
            [
                "Saw Red vent in electrical",
                "Blue completed scan in medbay",
                "Found body in reactor",
            ]
        ],
    )

    player_suspicions: Dict[str, float] = Field(
        default_factory=dict,
        description="Suspicion level (0.0-1.0) for each player",
        examples=[{"Red": 0.9, "Blue": 0.3, "Green": 0.1}],
    )

    player_alibis: Dict[str, str] = Field(
        default_factory=dict,
        description="Last known location for each player",
        examples=[{"Red": "electrical", "Blue": "medbay", "Green": "cafeteria"}],
    )

    location_history: List[str] = Field(
        default_factory=list,
        description="Recent locations visited by this player",
        examples=[
            ["cafeteria", "upper_engine", "reactor", "upper_engine", "cafeteria"]
        ],
    )

    @field_validator("player_suspicions")
    @classmethod
    def validate_suspicion_levels(cls, v: Dict[str, float]) -> Dict[str, float]:
        """Ensure suspicion levels are within valid range.

        Args:
            v (Dict[str, float]): Suspicion dictionary to validate.

        Returns:
            Dict[str, float]: Validated suspicion levels.

        Raises:
            ValueError: If suspicion level outside 0-1 range.
        """
        for player, level in v.items():
            if not 0.0 <= level <= 1.0:
                raise ValueError(
                    f"Suspicion level for {player} must be between 0 and 1"
                )
        return v

    @computed_field
    @property
    def most_suspicious(self) -> Optional[str]:
        """Identify the most suspicious player.

        Returns:
            Optional[str]: Player ID with highest suspicion or None.
        """
        if not self.player_suspicions:
            return None
        return max(self.player_suspicions.items(), key=lambda x: x[1])[0]

    @computed_field
    @property
    def trusted_players(self) -> List[str]:
        """List players with low suspicion (< 0.3).

        Returns:
            List[str]: IDs of trusted players.
        """
        return [p for p, s in self.player_suspicions.items() if s < 0.3]


class PlayerState(BaseModel):
    """Complete state representation for a player in Among Us.

    Encapsulates all information about a player including their role,
    location, tasks, survival status, and cognitive state. Supports
    both crewmate and impostor gameplay with appropriate abilities.

    Attributes:
        id (str): Unique player identifier.
        role (PlayerRole): Crewmate or Impostor designation.
        location (str): Current room location.
        tasks (List[Task]): Assigned tasks (empty for impostors).
        is_alive (bool): Whether player is still active.
        last_action (Optional[str]): Most recent action taken.
        observations (List[str]): Direct observations this turn.
        in_vent (bool): Whether currently hiding in vent.
        current_vent (Optional[str]): ID of occupied vent.
        memory (PlayerMemory): Cognitive state and deductions.

    Examples:
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
    """

    id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique identifier for the player",
        examples=["Red", "Blue", "Green", "Player1", "ImpostorBot"],
    )

    role: PlayerRole = Field(
        ..., description="Player's secret role determining abilities and objectives"
    )

    location: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Current room ID where player is located",
        examples=["cafeteria", "electrical", "reactor"],
    )

    tasks: List[Task] = Field(
        default_factory=list, description="List of assigned tasks (empty for impostors)"
    )

    is_alive: bool = Field(
        default=True, description="Whether player is still alive and active"
    )

    last_action: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Description of most recent action taken",
        examples=["Completed wiring task", "Moved to electrical", "Killed Blue"],
    )

    observations: List[str] = Field(
        default_factory=list,
        description="List of observations made this turn",
        examples=[["Saw Red vent", "Found body in electrical"]],
    )

    in_vent: bool = Field(
        default=False, description="Whether player is currently hiding in a vent"
    )

    current_vent: Optional[str] = Field(
        default=None,
        description="ID of vent currently occupied (if in_vent is True)",
        examples=["electrical_vent", "medbay_vent"],
    )

    memory: PlayerMemory = Field(
        default_factory=PlayerMemory,
        description="Player's cognitive state and deduction history",
    )

    def is_impostor(self) -> bool:
        """Check if the player is an impostor.

        Returns:
            bool: True if player has impostor role.

        Examples:
            >>> impostor = PlayerState(id="Red", role=PlayerRole.IMPOSTOR, location="cafeteria")
            >>> impostor.is_impostor()
            True
        """
        return self.role == PlayerRole.IMPOSTOR

    def is_crewmate(self) -> bool:
        """Check if the player is a crewmate.

        Returns:
            bool: True if player has crewmate role.

        Examples:
            >>> crew = PlayerState(id="Blue", role=PlayerRole.CREWMATE, location="cafeteria")
            >>> crew.is_crewmate()
            True
        """
        return self.role == PlayerRole.CREWMATE

    def can_kill(self, kill_cooldown: int = 0) -> bool:
        """Check if the player can perform a kill action.

        Kill ability requires:
        - Impostor role
        - Being alive
        - Kill cooldown expired
        - Not currently in vent

        Args:
            kill_cooldown (int): Remaining cooldown seconds.

        Returns:
            bool: True if all conditions met for killing.

        Examples:
            >>> impostor = PlayerState(id="Red", role=PlayerRole.IMPOSTOR,
            ...                        location="electrical", is_alive=True)
            >>> impostor.can_kill(kill_cooldown=0)
            True
            >>> impostor.can_kill(kill_cooldown=10)
            False
        """
        return (
            self.is_impostor()
            and self.is_alive
            and kill_cooldown <= 0
            and not self.in_vent
        )

    def can_use_vent(self) -> bool:
        """Check if the player can use ventilation systems.

        Vent usage requires:
        - Impostor role
        - Being alive

        Returns:
            bool: True if player can enter/exit vents.

        Examples:
            >>> impostor = PlayerState(id="Red", role=PlayerRole.IMPOSTOR,
            ...                        location="electrical", is_alive=True)
            >>> impostor.can_use_vent()
            True
        """
        return self.is_impostor() and self.is_alive

    @computed_field
    @property
    def task_completion_rate(self) -> float:
        """Calculate percentage of tasks completed.

        Returns:
            float: Completion percentage (0.0-100.0).
        """
        if not self.tasks:
            return 100.0 if self.is_impostor() else 0.0

        completed = sum(1 for task in self.tasks if task.is_completed)
        return (completed / len(self.tasks)) * 100.0

    @computed_field
    @property
    def incomplete_tasks(self) -> List[Task]:
        """Get list of uncompleted tasks.

        Returns:
            List[Task]: Tasks that still need completion.
        """
        return [task for task in self.tasks if not task.is_completed]

    @computed_field
    @property
    def is_ghost(self) -> bool:
        """Check if player is a ghost (dead but still participating).

        Returns:
            bool: True if player is dead.
        """
        return not self.is_alive


class SabotageType(str, Enum):
    """Types of sabotage available to impostors.

    Sabotages disrupt crewmate activities and create opportunities
    for kills. Critical sabotages can end the game if not resolved.

    Values:
        LIGHTS: Reduces crewmate vision radius
        COMMS: Hides task list and prevents meetings
        OXYGEN: Critical - requires two-point fix within time limit
        REACTOR: Critical - requires two-point fix within time limit
        DOORS: Locks specific room doors temporarily
    """

    LIGHTS = "lights"  # Reduces visibility
    COMMS = "comms"  # Disables task list
    OXYGEN = "o2"  # Time-critical, requires two-point fix
    REACTOR = "reactor"  # Time-critical, requires two-point fix
    DOORS = "doors"  # Locks doors to a room


class SabotageStatus(str, Enum):
    """Current state of a sabotage event.

    Values:
        ACTIVE: Sabotage in effect, needs resolution
        RESOLVED: Successfully fixed by crewmates
        FAILED: Timer expired on critical sabotage (impostor win)
    """

    ACTIVE = "active"
    RESOLVED = "resolved"
    FAILED = "failed"  # Timer ran out on critical sabotages


class SabotageResolutionPoint(BaseModel):
    """Interactive point for resolving sabotages.

    Critical sabotages require multiple resolution points to be
    activated simultaneously (e.g., reactor needs two players).
    Non-critical sabotages may have single resolution points.

    Attributes:
        id (str): Unique identifier for this point.
        location (str): Room containing the resolution point.
        description (str): What needs to be done here.
        resolved (bool): Whether this point is activated.
        resolver_id (Optional[str]): Player who resolved this.

    Examples:
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
    """

    id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Unique identifier for resolution point",
        examples=["reactor_left", "reactor_right", "o2_admin", "o2_greenhouse"],
    )

    location: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Room ID containing this resolution point",
        examples=["reactor", "admin", "greenhouse"],
    )

    description: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Instructions for resolving at this point",
        examples=["Hold reactor panel", "Enter O2 code", "Reset communications"],
    )

    resolved: bool = Field(
        default=False, description="Whether this point has been activated"
    )

    resolver_id: Optional[str] = Field(
        default=None,
        description="ID of player who resolved this point",
        examples=["Blue", "Green", None],
    )


class SabotageEvent(BaseModel):
    """Active sabotage affecting gameplay.

    Represents an ongoing sabotage that disrupts normal gameplay.
    Critical sabotages have timers and can end the game, while
    non-critical sabotages create tactical advantages.

    Attributes:
        type (str): Type of sabotage from SabotageType.
        location (str): Primary affected location.
        timer (int): Seconds until critical failure.
        resolved (bool): Whether sabotage is fixed.
        resolution_points (List[SabotageResolutionPoint]): Fix locations.

    Examples:
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
    """

    type: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Type of sabotage affecting gameplay",
        examples=["reactor", "o2", "lights", "comms", "doors"],
    )

    location: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Primary location affected by sabotage",
        examples=["reactor", "electrical", "admin"],
    )

    timer: int = Field(
        default=0,
        ge=0,
        le=60,
        description="Seconds until critical failure (0 for non-critical)",
        examples=[0, 30, 45],
    )

    resolved: bool = Field(
        default=False, description="Whether sabotage has been fully resolved"
    )

    resolution_points: List[SabotageResolutionPoint] = Field(
        default_factory=list,
        description="Points that must be activated to resolve sabotage",
    )

    def is_critical(self) -> bool:
        """Check if this is a game-ending critical sabotage.

        Critical sabotages (O2, Reactor) can end the game if not
        resolved within the time limit.

        Returns:
            bool: True if sabotage is critical.

        Examples:
            >>> reactor = SabotageEvent(type="reactor", location="reactor", timer=30)
            >>> reactor.is_critical()
            True
            >>> lights = SabotageEvent(type="lights", location="electrical", timer=0)
            >>> lights.is_critical()
            False
        """
        return self.type in ["o2", "reactor"]

    def is_resolved(self) -> bool:
        """Check if the sabotage is fully resolved.

        Sabotage is resolved when either marked resolved or all
        resolution points are activated.

        Returns:
            bool: True if sabotage is fixed.

        Examples:
            >>> sabotage = SabotageEvent(type="reactor", location="reactor", timer=30)
            >>> sabotage.is_resolved()
            False
            >>> sabotage.resolved = True
            >>> sabotage.is_resolved()
            True
        """
        return self.resolved or all(point.resolved for point in self.resolution_points)

    @computed_field
    @property
    def urgency_level(self) -> str:
        """Determine urgency of addressing this sabotage.

        Returns:
            str: Urgency classification.
        """
        if self.is_critical() and self.timer < 10:
            return "emergency"
        elif self.is_critical():
            return "critical"
        elif self.type == "lights":
            return "moderate"
        else:
            return "low"

    @computed_field
    @property
    def points_remaining(self) -> int:
        """Count unresolved resolution points.

        Returns:
            int: Number of points still needing activation.
        """
        return sum(1 for point in self.resolution_points if not point.resolved)


class AmongUsGamePhase(str, Enum):
    """Current phase of gameplay.

    Game alternates between task/action phases and discussion/voting.

    Values:
        TASKS: Normal gameplay with movement and actions
        MEETING: Discussion phase after body report or emergency
        VOTING: Active voting to eject a player
        GAME_OVER: Game concluded with winner determined
    """

    TASKS = "tasks"
    MEETING = "meeting"
    VOTING = "voting"
    GAME_OVER = "game_over"


class AmongUsActionType(str, Enum):
    """All possible player actions in Among Us.

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
    """

    MOVE = "move"
    DO_TASK = "do_task"
    KILL = "kill"
    SABOTAGE = "sabotage"
    USE_VENT = "use_vent"
    REPORT_BODY = "report_body"
    CALL_MEETING = "call_meeting"
    VOTE = "vote"
    SKIP_VOTE = "skip_vote"


class AmongUsPlayerDecision(BaseModel):
    """Strategic decision model for player actions.

    Encapsulates a player's chosen action with reasoning and confidence.
    Used by AI agents to make informed decisions based on game state
    and objectives. Includes justification for social deduction.

    Attributes:
        action_type (AmongUsActionType): Chosen action to perform.
        target_location (Optional[str]): Destination for movement.
        target_player (Optional[str]): Target for kill/vote actions.
        target_task (Optional[str]): Task ID to attempt.
        reasoning (str): Strategic justification for action.
        confidence (float): Confidence level in decision (0-1).

    Examples:
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
    """

    action_type: AmongUsActionType = Field(
        ..., description="Type of action to take this turn"
    )

    target_location: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Target room for movement or location-based actions",
        examples=["electrical", "medbay", "reactor", None],
    )

    target_player: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Target player ID for kill or vote actions",
        examples=["Red", "Blue", "Green", None],
    )

    target_task: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Target task ID to perform",
        examples=["fix_wiring_1", "medbay_scan", None],
    )

    reasoning: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Strategic explanation for the chosen action",
        examples=[
            "Need to complete visual task to prove innocence",
            "Red is suspicious, was near the body",
            "Sabotaging reactor will split the crew",
        ],
    )

    confidence: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        description="Confidence level in this decision (0.0=uncertain, 1.0=certain)",
        examples=[0.1, 0.5, 0.8, 0.95],
    )

    @field_validator("target_location")
    @classmethod
    def validate_location_for_action(cls, v: Optional[str], info) -> Optional[str]:
        """Ensure target location is provided for movement actions.

        Args:
            v (Optional[str]): Target location value.
            info: Validation context with other fields.

        Returns:
            Optional[str]: Validated location.

        Raises:
            ValueError: If location missing for movement.
        """
        if "action_type" in info.data:
            action = info.data["action_type"]
            if action == AmongUsActionType.MOVE and not v:
                raise ValueError("target_location required for MOVE action")
        return v

    @computed_field
    @property
    def is_aggressive_action(self) -> bool:
        """Check if action is aggressive/hostile.

        Returns:
            bool: True for kill/sabotage actions.
        """
        return self.action_type in [AmongUsActionType.KILL, AmongUsActionType.SABOTAGE]

    @computed_field
    @property
    def requires_target_player(self) -> bool:
        """Check if action needs a target player.

        Returns:
            bool: True for kill/vote actions.
        """
        return self.action_type in [AmongUsActionType.KILL, AmongUsActionType.VOTE]


class AmongUsAnalysis(BaseModel):
    """Comprehensive game state analysis for strategic planning.

    Provides high-level analysis of the current game situation,
    including win probability, player suspicions, and strategic
    recommendations. Used by AI agents for decision-making.

    Attributes:
        game_phase (AmongUsGamePhase): Current game phase.
        crew_advantage (float): Balance of power (-1 to +1).
        task_completion_percentage (float): Overall task progress.
        suspected_impostors (List[str]): Likely impostor IDs.
        trusted_players (List[str]): Confirmed crewmate IDs.
        active_sabotages (List[str]): Current sabotage types.
        recommended_strategy (str): Strategic advice.
        risk_assessment (str): Current danger evaluation.
        priority_actions (List[str]): Urgent actions needed.

    Examples:
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
    """

    game_phase: AmongUsGamePhase = Field(
        ..., description="Current phase of the game affecting available actions"
    )

    crew_advantage: float = Field(
        ...,
        ge=-1.0,
        le=1.0,
        description="Game balance (-1.0=impostor winning, 0.0=balanced, 1.0=crew winning)",
        examples=[-0.8, -0.3, 0.0, 0.5, 0.9],
    )

    task_completion_percentage: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Overall percentage of all crew tasks completed",
        examples=[0.0, 25.5, 50.0, 75.0, 95.0],
    )

    suspected_impostors: List[str] = Field(
        default_factory=list,
        description="Player IDs with high impostor probability",
        examples=[["Red"], ["Red", "Purple"], []],
    )

    trusted_players: List[str] = Field(
        default_factory=list,
        description="Player IDs confirmed or likely crewmates",
        examples=[["Blue", "Green"], ["Yellow"], []],
    )

    active_sabotages: List[str] = Field(
        default_factory=list,
        description="Currently active sabotage types",
        examples=[["reactor"], ["lights", "doors"], []],
    )

    recommended_strategy: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Strategic recommendation for current situation",
        examples=[
            "Focus on completing tasks while staying in groups",
            "Emergency! Fix reactor immediately or lose the game",
            "Vote Red - strong evidence of venting",
        ],
    )

    risk_assessment: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Evaluation of current dangers and threats",
        examples=[
            "Low risk - early game, no suspicious activity",
            "High risk - multiple impostors, low crew count",
            "Critical - reactor sabotage with 10 seconds remaining",
        ],
    )

    priority_actions: List[str] = Field(
        default_factory=list,
        max_length=5,
        description="Ordered list of most important immediate actions",
        examples=[
            ["Fix reactor", "Stay grouped"],
            ["Complete visual task", "Report suspicious behavior"],
            ["Vote Red", "Share alibi information"],
        ],
    )

    @field_validator("priority_actions")
    @classmethod
    def validate_priority_actions(cls, v: List[str]) -> List[str]:
        """Ensure priority actions list is reasonable length.

        Args:
            v (List[str]): Priority actions to validate.

        Returns:
            List[str]: Validated actions list.

        Raises:
            ValueError: If too many priorities listed.
        """
        if len(v) > 5:
            raise ValueError("Maximum 5 priority actions allowed")
        return v

    @computed_field
    @property
    def is_emergency(self) -> bool:
        """Check if situation requires immediate action.

        Returns:
            bool: True if critical sabotages active or crew disadvantaged.
        """
        critical_sabotages = ["reactor", "o2"]
        has_critical = any(sab in critical_sabotages for sab in self.active_sabotages)
        return has_critical or self.crew_advantage < -0.7

    @computed_field
    @property
    def win_probability(self) -> Dict[str, float]:
        """Estimate win probability for each team.

        Returns:
            Dict[str, float]: Win chances for crew and impostors.
        """
        # Simple linear mapping from advantage to probability
        crew_prob = (self.crew_advantage + 1.0) / 2.0
        return {"crew": crew_prob, "impostor": 1.0 - crew_prob}

    @computed_field
    @property
    def game_stage(self) -> str:
        """Classify game progression stage.

        Returns:
            str: Early, mid, or late game classification.
        """
        if self.task_completion_percentage < 30:
            return "early"
        elif self.task_completion_percentage < 70:
            return "mid"
        else:
            return "late"

    model_config = {"arbitrary_types_allowed": True}
