# Updated AmongUsState model

from typing import Any, Literal

from pydantic import Field

from haive.games.among_us.models import (
    AmongUsGamePhase,
    PlayerRole,
    PlayerState,
    Room,
    RoomConnection,
    SabotageEvent,
    Task,
    TaskStatus,
    Vent,
    VentConnection,
)
from haive.games.framework.multi_player.state import MultiPlayerGameState


class AmongUsState(MultiPlayerGameState):
    map_locations: list[str] = Field(default_factory=list)
    map_name: str = Field(default="skeld")
    rooms: dict[str, Room] = Field(default_factory=dict)
    vents: dict[str, Vent] = Field(default_factory=dict)
    player_states: dict[str, PlayerState] = Field(default_factory=dict)
    tasks: dict[str, Task] = Field(default_factory=dict)
    sabotages: list[SabotageEvent] = Field(default_factory=list)
    eliminated_players: list[str] = Field(default_factory=list)
    meeting_active: bool = Field(default=False)
    meeting_caller: str | None = Field(default=None)
    reported_body: str | None = Field(default=None)
    votes: dict[str, str] = Field(default_factory=dict)
    game_phase: AmongUsGamePhase = Field(default=AmongUsGamePhase.TASKS)
    impostor_count: int = Field(default=0)
    crewmate_count: int = Field(default=0)
    discussion_history: list[dict[str, Any]] = Field(default_factory=list)
    kill_cooldowns: dict[str, int] = Field(
        default_factory=dict
    )  # Player ID -> cooldown in seconds

    def get_alive_players(self) -> list[str]:
        """Get list of alive player IDs."""
        return [pid for pid, pstate in self.player_states.items() if pstate.is_alive]

    def get_task_completion_percentage(self) -> float:
        """Calculate task completion percentage."""
        total = len(self.tasks)
        if total == 0:
            return 100.0

        completed = sum(
            1 for task in self.tasks.values() if task.status == TaskStatus.COMPLETED
        )
        return (completed / total) * 100

    def check_win_condition(self) -> Literal["crewmates", "impostors"] | None:
        """Check if either side has won."""
        if self.get_task_completion_percentage() >= 100:
            return "crewmates"

        alive_impostors = sum(
            1
            for pid, pstate in self.player_states.items()
            if pstate.is_alive and pstate.role == PlayerRole.IMPOSTOR
        )
        alive_crewmates = sum(
            1
            for pid, pstate in self.player_states.items()
            if pstate.is_alive and pstate.role == PlayerRole.CREWMATE
        )

        if alive_impostors == 0:
            return "crewmates"
        if alive_impostors >= alive_crewmates:
            return "impostors"

        # Check if any critical sabotage has failed
        for sabotage in self.sabotages:
            if (
                sabotage.is_critical()
                and not sabotage.is_resolved()
                and sabotage.timer <= 0
            ):
                return "impostors"

        return None

    def get_room(self, room_id: str) -> Room | None:
        """Get a room by ID."""
        return self.rooms.get(room_id)

    def get_vent(self, vent_id: str) -> Vent | None:
        """Get a vent by ID."""
        return self.vents.get(vent_id)

    def get_vents_in_room(self, room_id: str) -> list[Vent]:
        """Get all vents in a room."""
        return [
            vent for vent_id, vent in self.vents.items() if vent.location == room_id
        ]

    def get_connected_rooms(self, room_id: str) -> list[str]:
        """Get all rooms connected to the given room."""
        room = self.get_room(room_id)
        if not room:
            return []
        return [conn.target_room for conn in room.connections if not conn.is_blocked]

    def get_connected_vents(self, vent_id: str) -> list[str]:
        """Get all vents connected to the given vent."""
        vent = self.get_vent(vent_id)
        if not vent:
            return []
        return [conn.target_vent_id for conn in vent.connections]

    def add_observation(self, player_id: str, observation: str):
        """Add an observation to a player's observations."""
        if player_id in self.player_states:
            self.player_states[player_id].observations.append(observation)
            # Also add to player's memory
            if hasattr(self.player_states[player_id], "memory"):
                self.player_states[player_id].memory.observations.append(observation)

    def add_observation_to_all_in_room(
        self, room_id: str, observation: str, exclude_players: list[str] = None
    ):
        """Add an observation to all players in a room."""
        exclude_players = exclude_players or []
        for pid, pstate in self.player_states.items():
            if (
                pstate.is_alive
                and pstate.location == room_id
                and pid not in exclude_players
            ):
                self.add_observation(pid, observation)

    def get_active_sabotage(self) -> SabotageEvent | None:
        """Get the currently active sabotage, if any."""
        for sabotage in self.sabotages:
            if not sabotage.is_resolved():
                return sabotage
        return None

    def get_player_cooldown(self, player_id: str) -> int:
        """Get a player's kill cooldown."""
        return self.kill_cooldowns.get(player_id, 0)

    def set_player_cooldown(self, player_id: str, cooldown: int):
        """Set a player's kill cooldown."""
        self.kill_cooldowns[player_id] = cooldown

    def decrement_cooldowns(self):
        """Decrement all cooldowns by 1."""
        for player_id in list(self.kill_cooldowns.keys()):
            if self.kill_cooldowns[player_id] > 0:
                self.kill_cooldowns[player_id] -= 1

    def initialize_map(self):
        """Initialize the map with rooms and vents based on the map name."""
        # Clear existing rooms and vents
        self.rooms = {}
        self.vents = {}

        if self.map_name.lower() == "skeld":
            # Create rooms
            self.rooms = {
                "cafeteria": Room(
                    id="cafeteria",
                    name="Cafeteria",
                    connections=[
                        RoomConnection(target_room="admin", distance=2),
                        RoomConnection(target_room="weapons", distance=2),
                        RoomConnection(target_room="storage", distance=3),
                    ],
                    vents=["cafeteria_vent"],
                ),
                "admin": Room(
                    id="admin",
                    name="Admin",
                    connections=[
                        RoomConnection(target_room="cafeteria", distance=2),
                        RoomConnection(target_room="storage", distance=2),
                        RoomConnection(target_room="shields", distance=3),
                    ],
                    vents=["admin_vent"],
                ),
                "weapons": Room(
                    id="weapons",
                    name="Weapons",
                    connections=[
                        RoomConnection(target_room="cafeteria", distance=2),
                        RoomConnection(target_room="navigation", distance=3),
                        RoomConnection(target_room="o2", distance=2),
                    ],
                    vents=[],
                ),
                "o2": Room(
                    id="o2",
                    name="O2",
                    connections=[
                        RoomConnection(target_room="weapons", distance=2),
                        RoomConnection(target_room="navigation", distance=2),
                        RoomConnection(target_room="shields", distance=2),
                    ],
                    vents=["o2_vent"],
                ),
                "navigation": Room(
                    id="navigation",
                    name="Navigation",
                    connections=[
                        RoomConnection(target_room="weapons", distance=3),
                        RoomConnection(target_room="o2", distance=2),
                        RoomConnection(target_room="shields", distance=3),
                    ],
                    vents=["navigation_vent"],
                ),
                "shields": Room(
                    id="shields",
                    name="Shields",
                    connections=[
                        RoomConnection(target_room="admin", distance=3),
                        RoomConnection(target_room="navigation", distance=3),
                        RoomConnection(target_room="o2", distance=2),
                        RoomConnection(target_room="communications", distance=2),
                    ],
                    vents=[],
                ),
                "communications": Room(
                    id="communications",
                    name="Communications",
                    connections=[
                        RoomConnection(target_room="shields", distance=2),
                        RoomConnection(target_room="storage", distance=2),
                    ],
                    vents=["communications_vent"],
                ),
                "storage": Room(
                    id="storage",
                    name="Storage",
                    connections=[
                        RoomConnection(target_room="cafeteria", distance=3),
                        RoomConnection(target_room="admin", distance=2),
                        RoomConnection(target_room="communications", distance=2),
                        RoomConnection(target_room="electrical", distance=2),
                        RoomConnection(target_room="lower_engine", distance=3),
                    ],
                    vents=[],
                ),
                "electrical": Room(
                    id="electrical",
                    name="Electrical",
                    connections=[
                        RoomConnection(target_room="storage", distance=2),
                        RoomConnection(target_room="lower_engine", distance=2),
                    ],
                    vents=["electrical_vent"],
                ),
                "lower_engine": Room(
                    id="lower_engine",
                    name="Lower Engine",
                    connections=[
                        RoomConnection(target_room="storage", distance=3),
                        RoomConnection(target_room="electrical", distance=2),
                        RoomConnection(target_room="reactor", distance=2),
                        RoomConnection(target_room="upper_engine", distance=3),
                    ],
                    vents=["lower_engine_vent"],
                ),
                "reactor": Room(
                    id="reactor",
                    name="Reactor",
                    connections=[
                        RoomConnection(target_room="lower_engine", distance=2),
                        RoomConnection(target_room="upper_engine", distance=2),
                        RoomConnection(target_room="security", distance=2),
                    ],
                    vents=[],
                ),
                "upper_engine": Room(
                    id="upper_engine",
                    name="Upper Engine",
                    connections=[
                        RoomConnection(target_room="reactor", distance=2),
                        RoomConnection(target_room="lower_engine", distance=3),
                        RoomConnection(target_room="security", distance=2),
                        RoomConnection(target_room="cafeteria", distance=3),
                    ],
                    vents=["upper_engine_vent"],
                ),
                "security": Room(
                    id="security",
                    name="Security",
                    connections=[
                        RoomConnection(target_room="reactor", distance=2),
                        RoomConnection(target_room="upper_engine", distance=2),
                        RoomConnection(target_room="cafeteria", distance=3),
                    ],
                    vents=["security_vent"],
                ),
                "medbay": Room(
                    id="medbay",
                    name="Medbay",
                    connections=[
                        RoomConnection(target_room="upper_engine", distance=2),
                        RoomConnection(target_room="cafeteria", distance=2),
                    ],
                    vents=["medbay_vent"],
                ),
            }

            # Create vents
            self.vents = {
                "cafeteria_vent": Vent(
                    id="cafeteria_vent",
                    location="cafeteria",
                    connections=[
                        VentConnection(target_vent_id="admin_vent", travel_time=2),
                        VentConnection(target_vent_id="electrical_vent", travel_time=3),
                    ],
                ),
                "admin_vent": Vent(
                    id="admin_vent",
                    location="admin",
                    connections=[
                        VentConnection(target_vent_id="cafeteria_vent", travel_time=2),
                        VentConnection(target_vent_id="navigation_vent", travel_time=3),
                    ],
                ),
                "electrical_vent": Vent(
                    id="electrical_vent",
                    location="electrical",
                    connections=[
                        VentConnection(target_vent_id="cafeteria_vent", travel_time=3),
                        VentConnection(target_vent_id="security_vent", travel_time=2),
                        VentConnection(target_vent_id="medbay_vent", travel_time=3),
                    ],
                ),
                "navigation_vent": Vent(
                    id="navigation_vent",
                    location="navigation",
                    connections=[
                        VentConnection(target_vent_id="admin_vent", travel_time=3),
                        VentConnection(target_vent_id="o2_vent", travel_time=2),
                    ],
                ),
                "o2_vent": Vent(
                    id="o2_vent",
                    location="o2",
                    connections=[
                        VentConnection(target_vent_id="navigation_vent", travel_time=2),
                        VentConnection(
                            target_vent_id="communications_vent", travel_time=3
                        ),
                    ],
                ),
                "communications_vent": Vent(
                    id="communications_vent",
                    location="communications",
                    connections=[
                        VentConnection(target_vent_id="o2_vent", travel_time=3),
                        VentConnection(
                            target_vent_id="lower_engine_vent", travel_time=4
                        ),
                    ],
                ),
                "lower_engine_vent": Vent(
                    id="lower_engine_vent",
                    location="lower_engine",
                    connections=[
                        VentConnection(
                            target_vent_id="communications_vent", travel_time=4
                        ),
                        VentConnection(
                            target_vent_id="upper_engine_vent", travel_time=3
                        ),
                    ],
                ),
                "upper_engine_vent": Vent(
                    id="upper_engine_vent",
                    location="upper_engine",
                    connections=[
                        VentConnection(
                            target_vent_id="lower_engine_vent", travel_time=3
                        ),
                        VentConnection(target_vent_id="security_vent", travel_time=2),
                    ],
                ),
                "security_vent": Vent(
                    id="security_vent",
                    location="security",
                    connections=[
                        VentConnection(target_vent_id="electrical_vent", travel_time=2),
                        VentConnection(
                            target_vent_id="upper_engine_vent", travel_time=2
                        ),
                        VentConnection(target_vent_id="medbay_vent", travel_time=2),
                    ],
                ),
                "medbay_vent": Vent(
                    id="medbay_vent",
                    location="medbay",
                    connections=[
                        VentConnection(target_vent_id="electrical_vent", travel_time=3),
                        VentConnection(target_vent_id="security_vent", travel_time=2),
                    ],
                ),
            }

            # Update map_locations to include all room IDs
            self.map_locations = list(self.rooms.keys())

        # TODO: Add other maps (Polus, Mira HQ) in the future
