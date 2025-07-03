# among_us_models.py
from enum import Enum

from pydantic import BaseModel, Field


class PlayerRole(str, Enum):
    CREWMATE = "crewmate"
    IMPOSTOR = "impostor"


class TaskType(str, Enum):
    VISUAL = "visual"
    COMMON = "common"
    SHORT = "short"
    LONG = "long"


class TaskStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task(BaseModel):
    id: str
    type: TaskType
    location: str
    description: str
    status: TaskStatus = TaskStatus.NOT_STARTED
    visual_indicator: bool = (
        False  # Whether the task shows a visible confirmation when completed
    )


class VentConnection(BaseModel):
    """Connection between two vents."""

    target_vent_id: str
    travel_time: int = 2  # Time in seconds to travel between vents


class Vent(BaseModel):
    """Vent that impostors can use to move between rooms."""

    id: str
    location: str
    connections: list[VentConnection] = Field(default_factory=list)


class RoomConnection(BaseModel):
    """Connection between two rooms."""

    target_room: str
    distance: int = 1  # Travel time in seconds
    is_blocked: bool = False  # Can be blocked by sabotage


class Room(BaseModel):
    """Room on the map."""

    id: str
    name: str
    connections: list[RoomConnection] = Field(default_factory=list)
    vents: list[str] = Field(default_factory=list)  # Vent IDs in this room

    def is_connected_to(self, room_id: str) -> bool:
        """Check if this room is connected to another room."""
        return any(conn.target_room == room_id for conn in self.connections)

    def get_connection(self, room_id: str) -> RoomConnection | None:
        """Get the connection to another room if it exists."""
        for conn in self.connections:
            if conn.target_room == room_id:
                return conn
        return None


class PlayerMemory(BaseModel):
    """Player's memory of observations and suspicions."""

    observations: list[str] = Field(default_factory=list)
    player_suspicions: dict[str, float] = Field(
        default_factory=dict
    )  # Player ID -> suspicion level (0-1)
    player_alibis: dict[str, str] = Field(default_factory=dict)  # Player ID -> location
    location_history: list[str] = Field(
        default_factory=list
    )  # Recent locations visited


class PlayerState(BaseModel):
    id: str
    role: PlayerRole
    location: str
    tasks: list[Task]
    is_alive: bool = True
    last_action: str | None = None
    observations: list[str] = Field(default_factory=list)
    in_vent: bool = False
    current_vent: str | None = None
    memory: PlayerMemory = Field(default_factory=PlayerMemory)

    def is_impostor(self) -> bool:
        """Check if the player is an impostor."""
        return self.role == PlayerRole.IMPOSTOR

    def is_crewmate(self) -> bool:
        """Check if the player is a crewmate."""
        return self.role == PlayerRole.CREWMATE

    def can_kill(self, kill_cooldown: int = 0) -> bool:
        """Check if the player can kill."""
        return (
            self.is_impostor()
            and self.is_alive
            and kill_cooldown <= 0
            and not self.in_vent
        )

    def can_use_vent(self) -> bool:
        """Check if the player can use vents."""
        return self.is_impostor() and self.is_alive


class SabotageType(str, Enum):
    LIGHTS = "lights"  # Reduces visibility
    COMMS = "comms"  # Disables task list
    OXYGEN = "o2"  # Time-critical, requires two-point fix
    REACTOR = "reactor"  # Time-critical, requires two-point fix
    DOORS = "doors"  # Locks doors to a room


class SabotageStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    FAILED = "failed"  # Timer ran out on critical sabotages


class SabotageResolutionPoint(BaseModel):
    """Resolution point for a sabotage."""

    id: str
    location: str  # Room ID
    description: str
    resolved: bool = False
    resolver_id: str | None = None  # Player ID who resolved this point


class SabotageEvent(BaseModel):
    """Sabotage event in the game."""

    type: str
    location: str
    timer: int
    resolved: bool = False
    resolution_points: list[SabotageResolutionPoint] = Field(default_factory=list)

    def is_critical(self) -> bool:
        """Check if this is a critical sabotage."""
        return self.type in ["o2", "reactor"]

    def is_resolved(self) -> bool:
        """Check if the sabotage is resolved."""
        return self.resolved or all(point.resolved for point in self.resolution_points)


class AmongUsGamePhase(str, Enum):
    TASKS = "tasks"
    MEETING = "meeting"
    VOTING = "voting"
    GAME_OVER = "game_over"


class AmongUsActionType(str, Enum):
    """Available actions in Among Us."""

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
    """Decision model for Among Us player actions."""

    action_type: AmongUsActionType = Field(description="Type of action to take")
    target_location: str | None = Field(
        default=None, description="Target location for movement or action"
    )
    target_player: str | None = Field(
        default=None, description="Target player for actions like kill or vote"
    )
    target_task: str | None = Field(default=None, description="Target task to perform")
    reasoning: str = Field(description="Explanation for the chosen action")
    confidence: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Confidence in this decision (0-1)"
    )


class AmongUsAnalysis(BaseModel):
    """Analysis model for Among Us game state evaluation."""

    game_phase: AmongUsGamePhase = Field(description="Current phase of the game")
    crew_advantage: float = Field(
        ge=-1.0,
        le=1.0,
        description="Current advantage (-1 = impostor wins, +1 = crew wins)",
    )
    task_completion_percentage: float = Field(
        ge=0.0, le=100.0, description="Percentage of tasks completed"
    )
    suspected_impostors: list[str] = Field(
        default_factory=list, description="List of player IDs suspected to be impostors"
    )
    trusted_players: list[str] = Field(
        default_factory=list, description="List of player IDs trusted to be crewmates"
    )
    active_sabotages: list[str] = Field(
        default_factory=list, description="List of currently active sabotages"
    )
    recommended_strategy: str = Field(
        description="Recommended strategy for current situation"
    )
    risk_assessment: str = Field(description="Assessment of current risks and threats")
    priority_actions: list[str] = Field(
        default_factory=list, description="List of priority actions to focus on"
    )
