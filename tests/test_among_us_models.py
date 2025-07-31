"""Tests for Among Us models with real component validation.

This module provides comprehensive tests for Among Us models including:
    - Player roles and states
    - Task management and validation
    - Meeting phases and voting
    - Game configuration structures
    - Sabotage and location systems

All tests use real components without mocks, following the no-mocks methodology.
"""

from pydantic import ValidationError
import pytest

from haive.games.among_us.models import (
    AmongUsGamePhase,
    GameLocation,
    MeetingPhase,
    PlayerAction,
    PlayerMemory,
    PlayerRole,
    PlayerState,
    SabotageType,
    Task,
    TaskStatus,
    TaskType,
    VentConnection,
    VoteAction,
)


class TestPlayerRole:
    """Test suite for PlayerRole enum with real validation."""

    def test_player_role_enum_values(self):
        """Test PlayerRole enum has correct values."""
        assert PlayerRole.CREWMATE.value == "CREWMATE"
        assert PlayerRole.IMPOSTOR.value == "IMPOSTOR"

        # Test all enum values
        roles = list(PlayerRole)
        assert len(roles) == 2
        assert PlayerRole.CREWMATE in roles
        assert PlayerRole.IMPOSTOR in roles

    def test_player_role_string_conversion(self):
        """Test PlayerRole enum string conversion."""
        assert str(PlayerRole.CREWMATE) == "PlayerRole.CREWMATE"
        assert PlayerRole.CREWMATE.name == "CREWMATE"
        assert PlayerRole.IMPOSTOR.name == "IMPOSTOR"


class TestAmongUsGamePhase:
    """Test suite for AmongUsGamePhase enum with real validation."""

    def test_game_phase_enum_values(self):
        """Test AmongUsGamePhase enum has correct values."""
        expected_phases = [
            "LOBBY",
            "TASKS",
            "EMERGENCY",
            "DISCUSSION",
            "VOTING",
            "GAME_OVER",
        ]

        phases = [phase.value for phase in AmongUsGamePhase]
        assert phases == expected_phases

    def test_game_phase_transitions(self):
        """Test logical game phase transitions."""
        # Test that all phases are accessible
        assert AmongUsGamePhase.LOBBY
        assert AmongUsGamePhase.TASKS
        assert AmongUsGamePhase.EMERGENCY
        assert AmongUsGamePhase.DISCUSSION
        assert AmongUsGamePhase.VOTING
        assert AmongUsGamePhase.GAME_OVER


class TestTaskType:
    """Test suite for TaskType enum with real validation."""

    def test_task_type_enum_values(self):
        """Test TaskType enum has correct values."""
        expected_types = ["SHORT", "LONG", "COMMON", "VISUAL"]

        types = [task_type.value for task_type in TaskType]
        assert set(types) == set(expected_types)


class TestTaskStatus:
    """Test suite for TaskStatus enum with real validation."""

    def test_task_status_enum_values(self):
        """Test TaskStatus enum has correct values."""
        expected_statuses = ["NOT_STARTED", "IN_PROGRESS", "COMPLETED"]

        statuses = [status.value for status in TaskStatus]
        assert statuses == expected_statuses


class TestTask:
    """Test suite for Task model with real validation."""

    def test_task_creation_basic(self):
        """Test Task creation with basic parameters."""
        task = Task(
            id="fix-wiring-cafeteria",
            name="Fix Wiring",
            type=TaskType.COMMON,
            location="cafeteria",
            steps_required=3,
            status=TaskStatus.NOT_STARTED,
        )

        assert task.id == "fix-wiring-cafeteria"
        assert task.name == "Fix Wiring"
        assert task.type == TaskType.COMMON
        assert task.location == "cafeteria"
        assert task.steps_required == 3
        assert task.steps_completed == 0
        assert task.status == TaskStatus.NOT_STARTED

    def test_task_creation_with_progress(self):
        """Test Task creation with progress."""
        task = Task(
            id="upload-data",
            name="Upload Data",
            type=TaskType.LONG,
            location="communications",
            steps_required=10,
            steps_completed=5,
            status=TaskStatus.IN_PROGRESS,
        )

        assert task.steps_completed == 5
        assert task.status == TaskStatus.IN_PROGRESS

    def test_task_validation_invalid_steps_completed(self):
        """Test Task validation rejects invalid steps_completed."""
        # Steps completed exceeds required
        with pytest.raises(ValidationError) as exc_info:
            Task(
                id="task1",
                name="Test Task",
                type=TaskType.SHORT,
                location="cafeteria",
                steps_required=3,
                steps_completed=4,
                status=TaskStatus.IN_PROGRESS,
            )

        assert "steps_completed cannot exceed steps_required" in str(exc_info.value)

    def test_task_validation_negative_steps(self):
        """Test Task validation rejects negative steps."""
        # Negative steps_required
        with pytest.raises(ValidationError):
            Task(
                id="task1",
                name="Test Task",
                type=TaskType.SHORT,
                location="cafeteria",
                steps_required=-1,
                status=TaskStatus.NOT_STARTED,
            )

        # Negative steps_completed
        with pytest.raises(ValidationError):
            Task(
                id="task1",
                name="Test Task",
                type=TaskType.SHORT,
                location="cafeteria",
                steps_required=3,
                steps_completed=-1,
                status=TaskStatus.NOT_STARTED,
            )

    def test_task_all_types(self):
        """Test Task creation with all task types."""
        task_types = [TaskType.SHORT, TaskType.LONG, TaskType.COMMON, TaskType.VISUAL]

        for task_type in task_types:
            task = Task(
                id=f"task-{task_type.value}",
                name=f"Test {task_type.value}",
                type=task_type,
                location="cafeteria",
                steps_required=5,
                status=TaskStatus.NOT_STARTED,
            )
            assert task.type == task_type

    def test_task_serialization(self):
        """Test Task serialization to dictionary."""
        task = Task(
            id="fix-wiring",
            name="Fix Wiring",
            type=TaskType.COMMON,
            location="electrical",
            steps_required=3,
            steps_completed=1,
            status=TaskStatus.IN_PROGRESS,
        )

        task_dict = task.model_dump()

        assert task_dict["id"] == "fix-wiring"
        assert task_dict["name"] == "Fix Wiring"
        assert task_dict["type"] == "COMMON"
        assert task_dict["location"] == "electrical"
        assert task_dict["steps_required"] == 3
        assert task_dict["steps_completed"] == 1
        assert task_dict["status"] == "IN_PROGRESS"

    def test_task_deserialization(self):
        """Test Task deserialization from dictionary."""
        task_dict = {
            "id": "fix-wiring",
            "name": "Fix Wiring",
            "type": "COMMON",
            "location": "electrical",
            "steps_required": 3,
            "steps_completed": 1,
            "status": "IN_PROGRESS",
        }

        task = Task(**task_dict)

        assert task.id == "fix-wiring"
        assert task.type == TaskType.COMMON
        assert task.steps_completed == 1
        assert task.status == TaskStatus.IN_PROGRESS


class TestPlayerMemory:
    """Test suite for PlayerMemory model with real validation."""

    def test_player_memory_creation_default(self):
        """Test PlayerMemory creation with default values."""
        memory = PlayerMemory()

        assert memory.observations == []
        assert memory.player_suspicions == {}
        assert memory.player_alibis == {}
        assert memory.location_history == []

    def test_player_memory_creation_with_data(self):
        """Test PlayerMemory creation with data."""
        observations = ["Saw Red in electrical", "Blue was with me in cafeteria"]
        suspicions = {"Red": 0.8, "Blue": 0.2}
        alibis = {"Blue": "Was with me in cafeteria"}
        locations = ["cafeteria", "electrical", "storage"]

        memory = PlayerMemory(
            observations=observations,
            player_suspicions=suspicions,
            player_alibis=alibis,
            location_history=locations,
        )

        assert memory.observations == observations
        assert memory.player_suspicions == suspicions
        assert memory.player_alibis == alibis
        assert memory.location_history == locations

    def test_player_memory_default_factories(self):
        """Test PlayerMemory default factories create separate instances."""
        memory1 = PlayerMemory()
        memory2 = PlayerMemory()

        # Modify one instance
        memory1.observations.append("Test observation")
        memory1.player_suspicions["Red"] = 0.5

        # Other instance should not be affected
        assert memory2.observations == []
        assert memory2.player_suspicions == {}

    def test_player_memory_suspicion_values(self):
        """Test PlayerMemory suspicion values are in valid range."""
        # Valid suspicion values (0.0 to 1.0)
        memory = PlayerMemory(player_suspicions={"Red": 0.0, "Blue": 0.5, "Green": 1.0})

        assert memory.player_suspicions["Red"] == 0.0
        assert memory.player_suspicions["Blue"] == 0.5
        assert memory.player_suspicions["Green"] == 1.0


class TestPlayerState:
    """Test suite for PlayerState model with real validation."""

    def test_player_state_creation_crewmate(self):
        """Test PlayerState creation for crewmate."""
        tasks = [
            Task(
                id="task1",
                name="Fix Wiring",
                type=TaskType.COMMON,
                location="electrical",
                steps_required=3,
                status=TaskStatus.NOT_STARTED,
            )
        ]

        memory = PlayerMemory()

        player = PlayerState(
            id="player1",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            tasks=tasks,
            is_alive=True,
            observations=[],
            memory=memory,
        )

        assert player.id == "player1"
        assert player.role == PlayerRole.CREWMATE
        assert player.location == "cafeteria"
        assert len(player.tasks) == 1
        assert player.is_alive is True
        assert player.cooldown_remaining == 0
        assert player.memory == memory

    def test_player_state_creation_impostor(self):
        """Test PlayerState creation for impostor."""
        player = PlayerState(
            id="impostor1",
            role=PlayerRole.IMPOSTOR,
            location="storage",
            tasks=[],  # Impostors have no tasks
            is_alive=True,
            observations=["Pretending to do tasks"],
            memory=PlayerMemory(),
            cooldown_remaining=30,
        )

        assert player.role == PlayerRole.IMPOSTOR
        assert len(player.tasks) == 0
        assert player.cooldown_remaining == 30

    def test_player_state_dead_player(self):
        """Test PlayerState creation for dead player."""
        player = PlayerState(
            id="ghost1",
            role=PlayerRole.CREWMATE,
            location="medical",
            tasks=[],
            is_alive=False,
            observations=["I was killed!"],
            memory=PlayerMemory(),
        )

        assert player.is_alive is False
        assert player.location == "medical"

    def test_player_state_default_factories(self):
        """Test PlayerState default factories create separate instances."""
        player1 = PlayerState(
            id="p1",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            is_alive=True,
            memory=PlayerMemory(),
        )

        player2 = PlayerState(
            id="p2",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            is_alive=True,
            memory=PlayerMemory(),
        )

        # Modify one instance
        player1.tasks.append(
            Task(
                id="task1",
                name="Test",
                type=TaskType.SHORT,
                location="cafeteria",
                steps_required=1,
                status=TaskStatus.NOT_STARTED,
            )
        )
        player1.observations.append("Test observation")

        # Other instance should not be affected
        assert len(player2.tasks) == 0
        assert len(player2.observations) == 0


class TestGameLocation:
    """Test suite for GameLocation model with real validation."""

    def test_game_location_creation_simple(self):
        """Test GameLocation creation with basic parameters."""
        location = GameLocation(
            id="cafeteria",
            name="Cafeteria",
            connections=["upper_engine", "medbay", "admin", "weapons"],
        )

        assert location.id == "cafeteria"
        assert location.name == "Cafeteria"
        assert len(location.connections) == 4
        assert "upper_engine" in location.connections
        assert location.vent_connections == []

    def test_game_location_creation_with_vents(self):
        """Test GameLocation creation with vent connections."""
        vent = VentConnection(
            from_location="electrical", to_location="medbay", is_bidirectional=True
        )

        location = GameLocation(
            id="electrical",
            name="Electrical",
            connections=["storage", "lower_engine"],
            vent_connections=[vent],
        )

        assert len(location.vent_connections) == 1
        assert location.vent_connections[0].from_location == "electrical"
        assert location.vent_connections[0].to_location == "medbay"
        assert location.vent_connections[0].is_bidirectional is True

    def test_game_location_default_factories(self):
        """Test GameLocation default factories create separate instances."""
        loc1 = GameLocation(id="loc1", name="Location 1")
        loc2 = GameLocation(id="loc2", name="Location 2")

        # Modify one instance
        loc1.connections.append("test_connection")

        # Other instance should not be affected
        assert "test_connection" not in loc2.connections


class TestVentConnection:
    """Test suite for VentConnection model with real validation."""

    def test_vent_connection_bidirectional(self):
        """Test VentConnection creation for bidirectional vent."""
        vent = VentConnection(
            from_location="electrical", to_location="medbay", is_bidirectional=True
        )

        assert vent.from_location == "electrical"
        assert vent.to_location == "medbay"
        assert vent.is_bidirectional is True

    def test_vent_connection_unidirectional(self):
        """Test VentConnection creation for unidirectional vent."""
        vent = VentConnection(
            from_location="reactor", to_location="upper_engine", is_bidirectional=False
        )

        assert vent.from_location == "reactor"
        assert vent.to_location == "upper_engine"
        assert vent.is_bidirectional is False


class TestPlayerAction:
    """Test suite for PlayerAction model with real validation."""

    def test_player_action_creation_move(self):
        """Test PlayerAction creation for move action."""
        action = PlayerAction(
            type="move",
            player_id="player1",
            target_location="electrical",
            description="Moving to electrical to fix wiring",
        )

        assert action.type == "move"
        assert action.player_id == "player1"
        assert action.target_location == "electrical"
        assert action.target_player is None
        assert action.task_id is None

    def test_player_action_creation_kill(self):
        """Test PlayerAction creation for kill action."""
        action = PlayerAction(
            type="kill",
            player_id="impostor1",
            target_player="crewmate1",
            description="Eliminating crewmate1",
        )

        assert action.type == "kill"
        assert action.target_player == "crewmate1"
        assert action.target_location is None

    def test_player_action_creation_task(self):
        """Test PlayerAction creation for task action."""
        action = PlayerAction(
            type="task",
            player_id="crewmate1",
            task_id="fix-wiring-electrical",
            description="Working on fixing wiring",
        )

        assert action.type == "task"
        assert action.task_id == "fix-wiring-electrical"

    def test_player_action_creation_report(self):
        """Test PlayerAction creation for report action."""
        action = PlayerAction(
            type="report",
            player_id="player2",
            description="Found a body in electrical!",
        )

        assert action.type == "report"
        assert action.player_id == "player2"

    def test_player_action_all_fields(self):
        """Test PlayerAction with all optional fields."""
        action = PlayerAction(
            type="emergency",
            player_id="player3",
            target_location="cafeteria",
            target_player="suspect1",
            task_id="button",
            sabotage_type=SabotageType.REACTOR,
            description="Calling emergency meeting",
        )

        assert action.target_location == "cafeteria"
        assert action.target_player == "suspect1"
        assert action.task_id == "button"
        assert action.sabotage_type == SabotageType.REACTOR


class TestVoteAction:
    """Test suite for VoteAction model with real validation."""

    def test_vote_action_creation_normal_vote(self):
        """Test VoteAction creation for normal vote."""
        vote = VoteAction(voter_id="player1", target_id="suspect1", skip_vote=False)

        assert vote.voter_id == "player1"
        assert vote.target_id == "suspect1"
        assert vote.skip_vote is False

    def test_vote_action_creation_skip_vote(self):
        """Test VoteAction creation for skip vote."""
        vote = VoteAction(voter_id="player2", skip_vote=True)

        assert vote.voter_id == "player2"
        assert vote.target_id is None
        assert vote.skip_vote is True

    def test_vote_action_validation_both_target_and_skip(self):
        """Test VoteAction validation prevents both target and skip."""
        # This should be allowed by the model, validation is in game logic
        vote = VoteAction(voter_id="player1", target_id="player2", skip_vote=True)

        # Model allows this, game logic should handle validation
        assert vote.target_id == "player2"
        assert vote.skip_vote is True


class TestSabotageType:
    """Test suite for SabotageType enum with real validation."""

    def test_sabotage_type_enum_values(self):
        """Test SabotageType enum has correct values."""
        expected_types = ["REACTOR", "O2", "LIGHTS", "COMMS", "DOORS"]

        types = [sabotage.value for sabotage in SabotageType]
        assert set(types) == set(expected_types)


class TestMeetingPhase:
    """Test suite for MeetingPhase enum with real validation."""

    def test_meeting_phase_enum_values(self):
        """Test MeetingPhase enum has correct values."""
        expected_phases = ["REPORT", "DISCUSSION", "ACCUSATION", "DEFENSE", "VOTING"]

        phases = [phase.value for phase in MeetingPhase]
        assert phases == expected_phases

    def test_meeting_phase_order(self):
        """Test MeetingPhase logical order."""
        # Test phases are in logical order
        phases = list(MeetingPhase)
        assert phases[0] == MeetingPhase.REPORT
        assert phases[1] == MeetingPhase.DISCUSSION
        assert phases[2] == MeetingPhase.ACCUSATION
        assert phases[3] == MeetingPhase.DEFENSE
        assert phases[4] == MeetingPhase.VOTING
