"""Tests for Among Us state manager with real component validation.

This module provides comprehensive tests for Among Us state management including:
    - Game initialization with role assignment
    - Player action processing
    - Meeting and voting mechanics
    - Task completion logic
    - Win condition checking
    - Sabotage systems

All tests use real components without mocks, following the no-mocks methodology.
"""

from haive.games.among_us.models import (
    AmongUsGamePhase,
    PlayerAction,
    PlayerRole,
    SabotageType,
    Task,
    TaskStatus,
    VoteAction,
)
from haive.games.among_us.state import AmongUsState
from haive.games.among_us.state_manager import AmongUsStateManagerMixin


class TestAmongUsStateManager(AmongUsStateManagerMixin):
    """Test implementation of AmongUsStateManagerMixin for testing."""

    def __init__(self):
        """Initialize test state manager."""
        # Required for mixin to work
        pass


class TestAmongUsStateManagerMixin:
    """Test suite for AmongUsStateManagerMixin with real state operations."""

    def create_test_manager(self):
        """Create a test instance of the state manager."""
        return TestAmongUsStateManager()

    def test_state_manager_initialization(self):
        """Test state manager can be initialized."""
        manager = self.create_test_manager()
        assert manager is not None

    def test_initialize_state_basic(self):
        """Test basic state initialization with default player count."""
        manager = self.create_test_manager()

        # Initialize with 5 players
        state = manager.initialize_state(player_count=5)

        assert isinstance(state, AmongUsState)
        assert len(state.players) == 5
        assert state.game_phase == AmongUsGamePhase.LOBBY
        assert state.current_round == 1

        # Check role distribution (1 impostor for 5 players)
        impostors = sum(
            1 for p in state.players.values() if p.role == PlayerRole.IMPOSTOR
        )
        crewmates = sum(
            1 for p in state.players.values() if p.role == PlayerRole.CREWMATE
        )
        assert impostors == 1
        assert crewmates == 4

    def test_initialize_state_various_player_counts(self):
        """Test state initialization with various player counts."""
        manager = self.create_test_manager()

        # Test different player counts and expected impostor counts
        test_cases = [
            (4, 1),  # 4 players, 1 impostor
            (5, 1),  # 5 players, 1 impostor
            (6, 1),  # 6 players, 1 impostor
            (7, 2),  # 7 players, 2 impostors
            (8, 2),  # 8 players, 2 impostors
            (9, 2),  # 9 players, 2 impostors
            (10, 3),  # 10 players, 3 impostors
        ]

        for player_count, expected_impostors in test_cases:
            state = manager.initialize_state(player_count=player_count)

            assert len(state.players) == player_count
            impostors = sum(
                1 for p in state.players.values() if p.role == PlayerRole.IMPOSTOR
            )
            assert impostors == expected_impostors

    def test_initialize_state_player_names(self):
        """Test state initialization creates correct player names."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=3)

        # Check player names
        expected_names = {"player1", "player2", "player3"}
        actual_names = set(state.players.keys())
        assert actual_names == expected_names

    def test_initialize_state_player_tasks(self):
        """Test state initialization assigns tasks to crewmates."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        for player in state.players.values():
            if player.role == PlayerRole.CREWMATE:
                # Crewmates should have tasks
                assert len(player.tasks) > 0
                # Check task properties
                for task in player.tasks:
                    assert isinstance(task, Task)
                    assert task.status == TaskStatus.NOT_STARTED
                    assert task.steps_completed == 0
            else:
                # Impostors should have no tasks
                assert len(player.tasks) == 0

    def test_initialize_state_total_tasks_calculation(self):
        """Test state initialization calculates total tasks correctly."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        # Calculate total tasks from all crewmates
        total_tasks = sum(
            len(player.tasks)
            for player in state.players.values()
            if player.role == PlayerRole.CREWMATE
        )

        assert state.total_tasks == total_tasks
        assert state.tasks_completed == 0

    def test_apply_player_action_move(self):
        """Test applying move action for player."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Get a player and create move action
        player_id = "player1"
        action = PlayerAction(
            type="move",
            player_id=player_id,
            target_location="electrical",
            description="Moving to electrical",
        )

        # Apply action
        new_state = manager.apply_player_action(state, player_id, action)

        # Verify player moved
        assert new_state.players[player_id].location == "electrical"
        # Memory should track location
        assert "electrical" in new_state.players[player_id].memory.location_history

    def test_apply_player_action_task_progress(self):
        """Test applying task action for crewmate."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Find a crewmate with tasks
        crewmate_id = None
        task_id = None
        for player_id, player in state.players.items():
            if player.role == PlayerRole.CREWMATE and player.tasks:
                crewmate_id = player_id
                task_id = player.tasks[0].id
                break

        assert crewmate_id is not None

        # Create task action
        action = PlayerAction(
            type="task",
            player_id=crewmate_id,
            task_id=task_id,
            description="Working on task",
        )

        # Apply action
        new_state = manager.apply_player_action(state, crewmate_id, action)

        # Find the task and verify progress
        task = next(t for t in new_state.players[crewmate_id].tasks if t.id == task_id)
        assert task.steps_completed > 0
        assert task.status == TaskStatus.IN_PROGRESS

    def test_apply_player_action_kill(self):
        """Test applying kill action for impostor."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Find impostor and crewmate
        impostor_id = None
        crewmate_id = None
        for player_id, player in state.players.items():
            if player.role == PlayerRole.IMPOSTOR:
                impostor_id = player_id
            elif player.role == PlayerRole.CREWMATE and crewmate_id is None:
                crewmate_id = player_id

        assert impostor_id is not None
        assert crewmate_id is not None

        # Create kill action
        action = PlayerAction(
            type="kill",
            player_id=impostor_id,
            target_player=crewmate_id,
            description="Eliminating crewmate",
        )

        # Apply action
        new_state = manager.apply_player_action(state, impostor_id, action)

        # Verify kill
        assert not new_state.players[crewmate_id].is_alive
        assert crewmate_id in new_state.eliminated_players
        # Impostor should have cooldown
        assert new_state.players[impostor_id].cooldown_remaining > 0

    def test_apply_player_action_report_body(self):
        """Test applying report action when finding a body."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Kill a player first
        impostor_id = next(
            pid for pid, p in state.players.items() if p.role == PlayerRole.IMPOSTOR
        )
        victim_id = next(
            pid for pid, p in state.players.items() if p.role == PlayerRole.CREWMATE
        )

        kill_action = PlayerAction(
            type="kill", player_id=impostor_id, target_player=victim_id
        )
        state = manager.apply_player_action(state, impostor_id, kill_action)

        # Another player reports the body
        reporter_id = next(
            pid for pid, p in state.players.items() if p.is_alive and pid != impostor_id
        )

        report_action = PlayerAction(
            type="report", player_id=reporter_id, description="Found a body!"
        )

        new_state = manager.apply_player_action(state, reporter_id, report_action)

        # Should transition to emergency phase
        assert new_state.game_phase == AmongUsGamePhase.EMERGENCY
        assert new_state.bodies_reported == 1

    def test_apply_player_action_emergency_meeting(self):
        """Test applying emergency meeting action."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Player calls emergency meeting
        caller_id = "player1"
        action = PlayerAction(
            type="emergency",
            player_id=caller_id,
            description="Calling emergency meeting",
        )

        new_state = manager.apply_player_action(state, caller_id, action)

        # Should transition to emergency phase
        assert new_state.game_phase == AmongUsGamePhase.EMERGENCY
        assert new_state.emergency_meetings_called == 1

    def test_apply_player_action_sabotage(self):
        """Test applying sabotage action for impostor."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Find impostor
        impostor_id = next(
            pid for pid, p in state.players.items() if p.role == PlayerRole.IMPOSTOR
        )

        # Create sabotage action
        action = PlayerAction(
            type="sabotage",
            player_id=impostor_id,
            sabotage_type=SabotageType.REACTOR,
            description="Sabotaging reactor",
        )

        new_state = manager.apply_player_action(state, impostor_id, action)

        # Verify sabotage
        assert new_state.sabotage_active == SabotageType.REACTOR
        assert new_state.sabotage_timer > 0

    def test_process_voting_simple_majority(self):
        """Test voting process with simple majority."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.VOTING

        # Create votes - majority votes for player3
        votes = [
            VoteAction(voter_id="player1", target_id="player3"),
            VoteAction(voter_id="player2", target_id="player3"),
            VoteAction(voter_id="player3", target_id="player1"),
            VoteAction(voter_id="player4", skip_vote=True),
            VoteAction(voter_id="player5", target_id="player3"),
        ]

        new_state = manager.process_voting(state, votes)

        # player3 should be eliminated
        assert not new_state.players["player3"].is_alive
        assert "player3" in new_state.eliminated_players
        # Should return to tasks phase
        assert new_state.game_phase == AmongUsGamePhase.TASKS

    def test_process_voting_skip_majority(self):
        """Test voting process with skip vote majority."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.VOTING

        # Create votes - majority skips
        votes = [
            VoteAction(voter_id="player1", skip_vote=True),
            VoteAction(voter_id="player2", skip_vote=True),
            VoteAction(voter_id="player3", skip_vote=True),
            VoteAction(voter_id="player4", target_id="player5"),
            VoteAction(voter_id="player5", target_id="player4"),
        ]

        new_state = manager.process_voting(state, votes)

        # No one should be eliminated
        assert all(p.is_alive for p in new_state.players.values())
        assert len(new_state.eliminated_players) == 0
        # Should return to tasks phase
        assert new_state.game_phase == AmongUsGamePhase.TASKS

    def test_process_voting_tie(self):
        """Test voting process with tie."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=4)
        state.game_phase = AmongUsGamePhase.VOTING

        # Create votes - tie between player1 and player2
        votes = [
            VoteAction(voter_id="player1", target_id="player2"),
            VoteAction(voter_id="player2", target_id="player1"),
            VoteAction(voter_id="player3", target_id="player1"),
            VoteAction(voter_id="player4", target_id="player2"),
        ]

        new_state = manager.process_voting(state, votes)

        # No one should be eliminated on tie
        assert all(p.is_alive for p in new_state.players.values())
        assert len(new_state.eliminated_players) == 0

    def test_check_win_conditions_crewmate_task_win(self):
        """Test crewmate win by completing all tasks."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        # Set all tasks as completed
        state.tasks_completed = state.total_tasks

        new_state = manager.check_win_conditions(state)

        assert new_state.winner == "crewmates"
        assert new_state.game_end_reason == "All tasks completed"
        assert new_state.game_phase == AmongUsGamePhase.GAME_OVER

    def test_check_win_conditions_crewmate_elimination_win(self):
        """Test crewmate win by eliminating all impostors."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        # Eliminate all impostors
        for player_id, player in state.players.items():
            if player.role == PlayerRole.IMPOSTOR:
                player.is_alive = False
                state.eliminated_players.append(player_id)

        new_state = manager.check_win_conditions(state)

        assert new_state.winner == "crewmates"
        assert new_state.game_end_reason == "All impostors eliminated"
        assert new_state.game_phase == AmongUsGamePhase.GAME_OVER

    def test_check_win_conditions_impostor_win(self):
        """Test impostor win by equal numbers."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        # Kill crewmates until impostors equal crewmates
        alive_crewmates = []
        for player_id, player in state.players.items():
            if player.role == PlayerRole.CREWMATE:
                alive_crewmates.append(player_id)

        # Kill all but one crewmate
        for player_id in alive_crewmates[1:]:
            state.players[player_id].is_alive = False
            state.eliminated_players.append(player_id)

        new_state = manager.check_win_conditions(state)

        assert new_state.winner == "impostors"
        assert new_state.game_end_reason == "Impostors equal crewmates"
        assert new_state.game_phase == AmongUsGamePhase.GAME_OVER

    def test_check_win_conditions_no_winner(self):
        """Test no win condition met."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        # Normal game state - no win condition
        new_state = manager.check_win_conditions(state)

        assert new_state.winner is None
        assert new_state.game_phase == AmongUsGamePhase.LOBBY  # Unchanged

    def test_complete_task_increments_counter(self):
        """Test task completion increments counters correctly."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Find a crewmate with tasks
        crewmate_id = None
        task = None
        for player_id, player in state.players.items():
            if player.role == PlayerRole.CREWMATE and player.tasks:
                crewmate_id = player_id
                task = player.tasks[0]
                break

        # Complete the task by applying multiple task actions
        for _ in range(task.steps_required):
            action = PlayerAction(type="task", player_id=crewmate_id, task_id=task.id)
            state = manager.apply_player_action(state, crewmate_id, action)

        # Task should be completed
        completed_task = next(
            t for t in state.players[crewmate_id].tasks if t.id == task.id
        )
        assert completed_task.status == TaskStatus.COMPLETED
        assert state.tasks_completed > 0

    def test_multiple_impostors_coordination(self):
        """Test game with multiple impostors."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=8)  # Should have 2 impostors

        # Count impostors
        impostors = [
            pid for pid, p in state.players.items() if p.role == PlayerRole.IMPOSTOR
        ]
        assert len(impostors) == 2

        # Both impostors should be able to kill (with cooldown)
        state.game_phase = AmongUsGamePhase.TASKS

        # First impostor kills
        victim1 = next(
            pid for pid, p in state.players.items() if p.role == PlayerRole.CREWMATE
        )
        kill1 = PlayerAction(type="kill", player_id=impostors[0], target_player=victim1)
        state = manager.apply_player_action(state, impostors[0], kill1)

        # First impostor should have cooldown
        assert state.players[impostors[0]].cooldown_remaining > 0
        # Second impostor should not have cooldown
        assert state.players[impostors[1]].cooldown_remaining == 0

    def test_location_based_actions(self):
        """Test location-based game mechanics."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Move all players to different locations
        locations = ["cafeteria", "electrical", "storage", "admin", "medbay"]
        for _i, (player_id, location) in enumerate(
            zip(state.players.keys(), locations)
        ):
            action = PlayerAction(
                type="move", player_id=player_id, target_location=location
            )
            state = manager.apply_player_action(state, player_id, action)

        # Verify all players are in different locations
        player_locations = [p.location for p in state.players.values()]
        assert len(set(player_locations)) == 5  # All unique locations

    def test_emergency_meeting_limits(self):
        """Test emergency meeting call limits."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)

        # Call multiple emergency meetings
        for i in range(3):
            state.game_phase = AmongUsGamePhase.TASKS
            action = PlayerAction(type="emergency", player_id="player1")
            state = manager.apply_player_action(state, "player1", action)
            assert state.emergency_meetings_called == i + 1

            # Resolve the meeting
            state.game_phase = AmongUsGamePhase.TASKS

    def test_dead_players_cannot_act(self):
        """Test that dead players cannot perform actions."""
        manager = self.create_test_manager()
        state = manager.initialize_state(player_count=5)
        state.game_phase = AmongUsGamePhase.TASKS

        # Kill a player
        victim_id = "player1"
        state.players[victim_id].is_alive = False
        state.eliminated_players.append(victim_id)

        # Dead player tries to move
        action = PlayerAction(
            type="move", player_id=victim_id, target_location="electrical"
        )

        new_state = manager.apply_player_action(state, victim_id, action)

        # Location should not change
        assert (
            new_state.players[victim_id].location == state.players[victim_id].location
        )
