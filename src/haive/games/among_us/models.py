# among_us_models.py
from enum import Enum
from typing import Dict, List, Optional

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
    connections: List[VentConnection] = Field(default_factory=list)


class RoomConnection(BaseModel):
    """Connection between two rooms."""

    target_room: str
    distance: int = 1  # Travel time in seconds
    is_blocked: bool = False  # Can be blocked by sabotage


class Room(BaseModel):
    """Room on the map."""

    id: str
    name: str
    connections: List[RoomConnection] = Field(default_factory=list)
    vents: List[str] = Field(default_factory=list)  # Vent IDs in this room

    def is_connected_to(self, room_id: str) -> bool:
        """Check if this room is connected to another room."""
        return any(conn.target_room == room_id for conn in self.connections)

    def get_connection(self, room_id: str) -> Optional[RoomConnection]:
        """Get the connection to another room if it exists."""
        for conn in self.connections:
            if conn.target_room == room_id:
                return conn
        return None


class PlayerMemory(BaseModel):
    """Player's memory of observations and suspicions."""

    observations: List[str] = Field(default_factory=list)
    player_suspicions: Dict[str, float] = Field(
        default_factory=dict
    )  # Player ID -> suspicion level (0-1)
    player_alibis: Dict[str, str] = Field(default_factory=dict)  # Player ID -> location
    location_history: List[str] = Field(
        default_factory=list
    )  # Recent locations visited


class PlayerState(BaseModel):
    id: str
    role: PlayerRole
    location: str
    tasks: List[Task]
    is_alive: bool = True
    last_action: Optional[str] = None
    observations: List[str] = Field(default_factory=list)
    in_vent: bool = False
    current_vent: Optional[str] = None
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
    resolver_id: Optional[str] = None  # Player ID who resolved this point


class SabotageEvent(BaseModel):
    """Sabotage event in the game."""

    type: str
    location: str
    timer: int
    resolved: bool = False
    resolution_points: List[SabotageResolutionPoint] = Field(default_factory=list)

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
