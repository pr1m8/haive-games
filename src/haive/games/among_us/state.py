"""Comprehensive state management for Among Us social deduction gameplay.

This module provides the core state model for managing Among Us game sessions,
tracking player positions, tasks, sabotages, and game progression. The state
system supports complex spatial navigation, role-based mechanics, and real-time
event handling for authentic social deduction experiences.

The state management includes:
- Dynamic map initialization with rooms and vents
- Player position and status tracking
- Task completion monitoring
- Sabotage event management
- Meeting and voting mechanics
- Win condition evaluation
- Observation and memory systems

Examples:
    Initializing a game state::

        state = AmongUsState()
        state.initialize_map()  # Creates Skeld map by default

        # Add players
        state.player_states["player1"] = PlayerState(
            id="player1",
            role=PlayerRole.CREWMATE,
            location="cafeteria"
        )

    Checking win conditions::

        winner = state.check_win_condition()
        if winner == "crewmates":
            print("All tasks completed!")
        elif winner == "impostors":
            print("Impostors have taken control!")

    Managing sabotages::

        # Create reactor meltdown
        sabotage = SabotageEvent(
            type="reactor",
            location="reactor",
            timer=30
        )
        state.sabotages.append(sabotage)

        # Check if critical
        active = state.get_active_sabotage()
        if active and active.is_critical():
            print(f"Emergency! {active.timer}s remaining!")

Note:
    The state model extends MultiPlayerGameState and integrates with
    LangGraph for distributed game session management.

"""

from typing import Any, Literal

from pydantic import Field, computed_field, field_validator

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
    """Comprehensive state model for Among Us game sessions.

    This class manages all aspects of an Among Us game state, including
    spatial layout, player tracking, task management, and game progression.
    It provides methods for querying game state, updating player positions,
    managing events, and evaluating win conditions.

    The state model supports:
    - Multiple map layouts (currently Skeld, with Polus/Mira HQ planned)
    - Real-time player position and status tracking
    - Task assignment and completion monitoring
    - Sabotage event lifecycle management
    - Emergency meeting and voting systems
    - Observation and memory tracking for deduction
    - Flexible win condition evaluation

    Attributes:
        map_locations: List of valid room IDs for the current map.
            Used for movement validation and spawn points.
        map_name: Name of the current map (e.g., "skeld", "polus").
            Determines room layout and task locations.
        rooms: Mapping of room IDs to Room objects.
            Defines spatial layout and connections.
        vents: Mapping of vent IDs to Vent objects.
            Enables impostor movement through vent network.
        player_states: Mapping of player IDs to PlayerState objects.
            Tracks all player information including role and position.
        tasks: Mapping of task IDs to Task objects.
            Defines available tasks and their completion status.
        sabotages: List of active and resolved sabotage events.
            Tracks sabotage history and current emergencies.
        eliminated_players: List of player IDs who have been eliminated.
            Used for ghost mechanics and win conditions.
        meeting_active: Whether an emergency meeting is in progress.
            Pauses gameplay and enables discussion/voting.
        meeting_caller: Player ID who called the current meeting.
            None if meeting was triggered by body report.
        reported_body: Player ID of body that triggered meeting.
            None if meeting was called via emergency button.
        votes: Mapping of voter ID to target ID for current meeting.
            Tracks voting progress and determines ejection.
        game_phase: Current phase of gameplay.
            Controls available actions and UI state.
        impostor_count: Number of living impostors.
            Cached for efficient win condition checks.
        crewmate_count: Number of living crewmates.
            Cached for efficient win condition checks.
        discussion_history: List of discussion events and messages.
            Provides context for AI decision-making.
        kill_cooldowns: Mapping of impostor ID to remaining cooldown.
            Prevents rapid elimination chains.

    Examples:
        Creating a new game state::

            state = AmongUsState(
                map_name="skeld",
                impostor_count=2,
                crewmate_count=8
            )
            state.initialize_map()

        Checking task progress::

            progress = state.get_task_completion_percentage()
            if progress >= 100:
                print("Crewmates win by tasks!")

        Managing meetings::

            state.meeting_active = True
            state.meeting_caller = "player1"
            state.votes["player1"] = "player3"  # Voting for player3
            state.votes["player2"] = "skip"     # Voting to skip

    """

    map_locations: list[str] = Field(
        default_factory=list,
        description="List of valid room IDs for movement validation",
        examples=[["cafeteria", "admin", "electrical", "reactor"]],
    )
    map_name: str = Field(
        default="skeld",
        description="Current map name determining layout and tasks",
        examples=["skeld", "polus", "mira_hq"],
    )
    rooms: dict[str, Room] = Field(
        default_factory=dict,
        description="Spatial layout mapping room IDs to Room objects",
    )
    vents: dict[str, Vent] = Field(
        default_factory=dict,
        description="Vent network mapping vent IDs to Vent objects",
    )
    player_states: dict[str, PlayerState] = Field(
        default_factory=dict,
        description="Player information mapping IDs to PlayerState objects",
    )
    tasks: dict[str, Task] = Field(
        default_factory=dict,
        description="Task registry mapping task IDs to Task objects",
    )
    sabotages: list[SabotageEvent] = Field(
        default_factory=list,
        description="History of sabotage events including active ones",
    )
    eliminated_players: list[str] = Field(
        default_factory=list,
        description="IDs of eliminated players for ghost mechanics",
        examples=[["player3", "player7"]],
    )
    meeting_active: bool = Field(
        default=False, description="Whether emergency meeting is currently in progress"
    )
    meeting_caller: str | None = Field(
        default=None, description="ID of player who called current meeting"
    )
    reported_body: str | None = Field(
        default=None, description="ID of body that triggered current meeting"
    )
    votes: dict[str, str] = Field(
        default_factory=dict,
        description="Current meeting votes mapping voter to target",
    )
    game_phase: AmongUsGamePhase = Field(
        default=AmongUsGamePhase.TASKS,
        description="Current gameplay phase controlling available actions",
    )
    impostor_count: int = Field(
        default=0, ge=0, description="Number of living impostors for win conditions"
    )
    crewmate_count: int = Field(
        default=0, ge=0, description="Number of living crewmates for win conditions"
    )
    discussion_history: list[dict[str, Any]] = Field(
        default_factory=list, description="Meeting discussions and chat for AI context"
    )
    kill_cooldowns: dict[str, int] = Field(
        default_factory=dict, description="Impostor kill cooldowns in seconds"
    )

    def get_alive_players(self) -> list[str]:
        """Get list of alive player IDs.

        Returns only players who have not been eliminated, useful for
        voting counts, task assignments, and win condition checks.

        Returns:
            List[str]: IDs of all living players.

        Examples:
            During meeting::

                alive = state.get_alive_players()
                print(f"{len(alive)} players can vote")

            Win condition check::

                alive = state.get_alive_players()
                if len(alive) <= 2:
                    # Check for impostor majority
                    pass

        """
        return [pid for pid, pstate in self.player_states.items() if pstate.is_alive]

    def get_task_completion_percentage(self) -> float:
        """Calculate overall task completion percentage.

        Computes the percentage of all tasks that have been completed
        across all crewmates. This is a primary win condition - crewmates
        win immediately when this reaches 100%.

        Returns:
            float: Percentage of completed tasks (0-100).

        Examples:
            Progress tracking::

                progress = state.get_task_completion_percentage()
                print(f"Tasks: {progress:.1f}% complete")

            Win condition::

                if state.get_task_completion_percentage() >= 100:
                    return "crewmates_win_by_tasks"

        Note:
            Returns 100.0 if no tasks exist (edge case handling).

        """
        total = len(self.tasks)
        if total == 0:
            return 100.0

        completed = sum(
            1 for task in self.tasks.values() if task.status == TaskStatus.COMPLETED
        )
        return (completed / total) * 100

    def check_win_condition(self) -> Literal["crewmates", "impostors"] | None:
        """Check if either side has achieved victory.

        Evaluates all win conditions for both teams:

        Crewmate victories:
        - All tasks completed
        - All impostors eliminated

        Impostor victories:
        - Impostor count >= crewmate count
        - Critical sabotage timer expired

        Returns:
            Optional[Literal["crewmates", "impostors"]]: Winning team or None.

        Examples:
            Task victory::

                # All tasks done
                winner = state.check_win_condition()
                assert winner == "crewmates"

            Impostor majority::

                # 2 impostors, 2 crewmates remaining
                winner = state.check_win_condition()
                assert winner == "impostors"

            Sabotage victory::

                # Reactor meltdown timer reaches 0
                winner = state.check_win_condition()
                assert winner == "impostors"

        """
        # Crewmate task victory
        if self.get_task_completion_percentage() >= 100:
            return "crewmates"

        # Count living players by role
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

        # Crewmate elimination victory
        if alive_impostors == 0:
            return "crewmates"

        # Impostor majority victory
        if alive_impostors >= alive_crewmates:
            return "impostors"

        # Check critical sabotage failures
        for sabotage in self.sabotages:
            if (
                sabotage.is_critical()
                and not sabotage.is_resolved()
                and sabotage.timer <= 0
            ):
                return "impostors"

        return None

    def get_room(self, room_id: str) -> Room | None:
        """Get a room by its unique identifier.

        Args:
            room_id: Unique room identifier (e.g., "cafeteria").

        Returns:
            Optional[Room]: Room object if found, None otherwise.

        Examples:
            Checking room properties::

                room = state.get_room("electrical")
                if room and room.has_security_camera:
                    print("This room is monitored")

        """
        return self.rooms.get(room_id)

    def get_vent(self, vent_id: str) -> Vent | None:
        """Get a vent by its unique identifier.

        Args:
            vent_id: Unique vent identifier (e.g., "electrical_vent").

        Returns:
            Optional[Vent]: Vent object if found, None otherwise.

        Examples:
            Checking vent connections::

                vent = state.get_vent("cafeteria_vent")
                if vent:
                    connected = [c.target_vent_id for c in vent.connections]
                    print(f"Can travel to: {connected}")

        """
        return self.vents.get(vent_id)

    def get_vents_in_room(self, room_id: str) -> list[Vent]:
        """Get all vents located in a specific room.

        Used for impostor movement options and vent camping detection.

        Args:
            room_id: Room to search for vents.

        Returns:
            List[Vent]: All vents in the specified room.

        Examples:
            Impostor options::

                vents = state.get_vents_in_room("electrical")
                if vents and player.role == PlayerRole.IMPOSTOR:
                    print(f"Can enter {len(vents)} vent(s) here")

        """
        return [
            vent for vent_id, vent in self.vents.items() if vent.location == room_id
        ]

    def get_connected_rooms(self, room_id: str) -> list[str]:
        """Get all rooms directly connected to the given room.

        Returns only accessible connections (not blocked by sabotage).
        Used for pathfinding and movement validation.

        Args:
            room_id: Source room to check connections from.

        Returns:
            List[str]: IDs of all accessible connected rooms.

        Examples:
            Movement options::

                adjacent = state.get_connected_rooms("cafeteria")
                print(f"Can move to: {', '.join(adjacent)}")

            Sabotage effects::

                # During O2 sabotage, some doors may be sealed
                rooms = state.get_connected_rooms("admin")
                if len(rooms) < normal_count:
                    print("Some exits are blocked!")

        """
        room = self.get_room(room_id)
        if not room:
            return []
        return [conn.target_room for conn in room.connections if not conn.is_blocked]

    def get_connected_vents(self, vent_id: str) -> list[str]:
        """Get all vents connected to the given vent.

        Used for impostor movement through the vent network.
        All vent connections are always accessible (no blocking).

        Args:
            vent_id: Source vent to check connections from.

        Returns:
            List[str]: IDs of all connected vents.

        Examples:
            Vent navigation::

                connected = state.get_connected_vents("electrical_vent")
                for vent_id in connected:
                    vent = state.get_vent(vent_id)
                    print(f"Can emerge in: {vent.location}")

        """
        vent = self.get_vent(vent_id)
        if not vent:
            return []
        return [conn.target_vent_id for conn in vent.connections]

    def add_observation(self, player_id: str, observation: str) -> None:
        """Add an observation to a player's memory.

        Observations form the basis of deduction in Among Us. This method
        records what a player has witnessed for later analysis.

        Args:
            player_id: ID of the observing player.
            observation: Description of what was observed.

        Examples:
            Witnessing movement::

                state.add_observation(
                    "player1",
                    "Saw player3 enter electrical at 14:32"
                )

            Task verification::

                state.add_observation(
                    "player2",
                    "Watched player4 complete medbay scan"
                )

        """
        if player_id in self.player_states:
            self.player_states[player_id].observations.append(observation)
            # Also add to player's memory model if available
            if (
                hasattr(self.player_states[player_id], "memory")
                and self.player_states[player_id].memory is not None
            ):
                self.player_states[player_id].memory.observations.append(observation)

    def add_observation_to_all_in_room(
        self,
        room_id: str,
        observation: str,
        exclude_players: list[str] | None = None,
    ) -> None:
        """Add an observation to all players in a specific room.

        Used for events that are visible to everyone in a location,
        such as sabotages, eliminations, or visual tasks.

        Args:
            room_id: Room where the event occurred.
            observation: Description of the observed event.
            exclude_players: Optional list of player IDs to exclude.
                Typically used to exclude the actor from observations.

        Examples:
            Elimination witnessed::

                state.add_observation_to_all_in_room(
                    "electrical",
                    "Player5 eliminated player2!",
                    exclude_players=["player5"]  # Killer doesn't observe self
                )

            Visual task::

                state.add_observation_to_all_in_room(
                    "medbay",
                    "Player3 completed scan (confirmed crewmate)"
                )

        """
        exclude_players = exclude_players or []
        for pid, pstate in self.player_states.items():
            if (
                pstate.is_alive
                and pstate.location == room_id
                and pid not in exclude_players
            ):
                self.add_observation(pid, observation)

    def get_active_sabotage(self) -> SabotageEvent | None:
        """Get the currently active sabotage event.

        Only one sabotage can be active at a time. This method returns
        the first unresolved sabotage found.

        Returns:
            Optional[SabotageEvent]: Active sabotage or None.

        Examples:
            Emergency response::

                sabotage = state.get_active_sabotage()
                if sabotage and sabotage.is_critical():
                    print(f"EMERGENCY: {sabotage.type} - {sabotage.timer}s left!")

            Checking if sabotage is possible::

                if state.get_active_sabotage() is None:
                    # Impostors can trigger new sabotage
                    pass

        """
        for sabotage in self.sabotages:
            if not sabotage.is_resolved():
                return sabotage
        return None

    def get_player_cooldown(self, player_id: str) -> int:
        """Get a player's kill cooldown in seconds.

        Args:
            player_id: ID of the player (impostor) to check.

        Returns:
            int: Remaining cooldown seconds (0 if can kill).

        Examples:
            Checking kill availability::

                cooldown = state.get_player_cooldown("impostor1")
                if cooldown == 0:
                    print("Kill ability ready")
                else:
                    print(f"Kill on cooldown: {cooldown}s")

        """
        return self.kill_cooldowns.get(player_id, 0)

    def set_player_cooldown(self, player_id: str, cooldown: int) -> None:
        """Set a player's kill cooldown.

        Typically called after an impostor eliminates someone.

        Args:
            player_id: ID of the player (impostor).
            cooldown: Cooldown duration in seconds.

        Examples:
            After elimination::

                # Standard 30 second cooldown
                state.set_player_cooldown("impostor1", 30)

            Custom game settings::

                # Fast-paced game with 10s cooldown
                state.set_player_cooldown("impostor1", 10)

        """
        self.kill_cooldowns[player_id] = cooldown

    def decrement_cooldowns(self) -> None:
        """Decrement all active kill cooldowns by 1 second.

        Should be called each game tick/second to update cooldowns.
        Automatically removes cooldowns that reach 0.

        Examples:
            Game loop integration::

                # In game tick handler
                state.decrement_cooldowns()

                # Check if any impostors can now kill
                for impostor_id in impostor_ids:
                    if state.get_player_cooldown(impostor_id) == 0:
                        # Enable kill button in UI
                        pass

        """
        for player_id in list(self.kill_cooldowns.keys()):
            if self.kill_cooldowns[player_id] > 0:
                self.kill_cooldowns[player_id] -= 1

    def initialize_map(self) -> None:
        """Initialize the map with rooms and vents based on the map name.

        Creates the spatial layout for the selected map, including all rooms,
        connections, and vent networks. Currently supports the Skeld map with
        plans for Polus and Mira HQ.

        The initialization includes:
        - Room creation with connections and properties
        - Vent network setup with travel times
        - Map location list for spawn points

        Examples:
            Default Skeld initialization::

                state = AmongUsState(map_name="skeld")
                state.initialize_map()
                assert "cafeteria" in state.rooms
                assert len(state.vents) == 10  # Skeld has 10 vents

            Future map support::

                state = AmongUsState(map_name="polus")
                state.initialize_map()  # Will support Polus layout

        Note:
            This method clears any existing rooms and vents before
            creating the new map layout.

        """
        # Clear existing spatial data
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

            # Update map_locations to include all room IDs for spawn/movement
            # validation
            self.map_locations = list(self.rooms.keys())

        # TODO: Add other maps (Polus, Mira HQ) in the future
        # elif self.map_name.lower() == "polus":
        #     self._initialize_polus_map()
        # elif self.map_name.lower() == "mira_hq":
        #     self._initialize_mira_hq_map()

    @field_validator("map_name")
    @classmethod
    def validate_map_name(cls, v: str) -> str:
        """Validate map name is supported.

        Args:
            v: Map name to validate.

        Returns:
            str: Validated map name in lowercase.

        Raises:
            ValueError: If map name is not supported.

        """
        supported_maps = ["skeld"]  # Add "polus", "mira_hq" when implemented
        if v.lower() not in supported_maps:
            raise ValueError(f"Unsupported map: {v}. Choose from: {supported_maps}")
        return v.lower()

    @computed_field
    @property
    def game_statistics(self) -> dict[str, Any]:
        """Calculate comprehensive game statistics.

        Returns:
            Dict[str, Any]: Statistics including player counts, progress, etc.

        Examples:
            Displaying game stats::

                stats = state.game_statistics
                print(f"Tasks: {stats['task_progress']:.1f}%")
                print(f"Impostors: {stats['alive_impostors']}/{stats['total_impostors']}")

        """
        total_players = len(self.player_states)
        alive_players = len(self.get_alive_players())

        total_impostors = sum(
            1 for p in self.player_states.values() if p.role == PlayerRole.IMPOSTOR
        )
        alive_impostors = sum(
            1
            for p in self.player_states.values()
            if p.role == PlayerRole.IMPOSTOR and p.is_alive
        )

        return {
            "total_players": total_players,
            "alive_players": alive_players,
            "eliminated_players": len(self.eliminated_players),
            "total_impostors": total_impostors,
            "alive_impostors": alive_impostors,
            "total_crewmates": total_players - total_impostors,
            "alive_crewmates": alive_players - alive_impostors,
            "task_progress": self.get_task_completion_percentage(),
            "active_sabotage": self.get_active_sabotage() is not None,
            "meeting_active": self.meeting_active,
            "game_phase": self.game_phase.value,
        }

    model_config = {"arbitrary_types_allowed": True}
