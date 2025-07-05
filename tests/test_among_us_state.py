"""Tests for Among Us state with real component validation.

This module provides comprehensive tests for Among Us state management including:
    - Game initialization with player roles
    - Phase transitions and game flow
    - Player state management
    - Meeting and voting systems
    - Task completion tracking
    - Win condition detection

All tests use real components without mocks, following the no-mocks methodology.
"""

from datetime import datetime

import pytest

from haive.games.among_us.models import (
    AmongUsGamePhase,
    MeetingPhase,
    PlayerAction,
    PlayerMemory,
    PlayerRole,
    PlayerState,
    Task,
    TaskStatus,
    TaskType,
    VoteAction,
)
from haive.games.among_us.state import AmongUsState


class TestAmongUsState:
    """Test suite for AmongUsState with real state validation."""

    def test_among_us_state_initialization_default(self):
        """Test AmongUsState initialization with default values."""
        state = AmongUsState()

        # Check default values
        assert state.game_phase == AmongUsGamePhase.LOBBY
        assert state.players == {}
        assert state.eliminated_players == []
        assert state.current_round == 1
        assert state.emergency_meetings_called == 0
        assert state.bodies_reported == 0
        assert state.meeting_phase is None
        assert state.discussion_timer == 0
        assert state.voting_timer == 0
        assert state.current_votes == {}
        assert state.tasks_completed == 0
        assert state.total_tasks == 0
        assert state.sabotage_active is None
        assert state.sabotage_timer == 0
        assert state.winner is None
        assert state.game_end_reason is None

    def test_among_us_state_initialization_with_players(self):
        """Test AmongUsState initialization with player data."""
        # Create players
        player1 = PlayerState(
            id="player1",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            is_alive=True,
            memory=PlayerMemory(),
        )

        player2 = PlayerState(
            id="player2",
            role=PlayerRole.IMPOSTOR,
            location="cafeteria",
            is_alive=True,
            memory=PlayerMemory(),
        )

        players = {"player1": player1, "player2": player2}

        state = AmongUsState(
            game_phase=AmongUsGamePhase.TASKS, players=players, current_round=1
        )

        assert len(state.players) == 2
        assert state.players["player1"].role == PlayerRole.CREWMATE
        assert state.players["player2"].role == PlayerRole.IMPOSTOR
        assert state.game_phase == AmongUsGamePhase.TASKS

    def test_among_us_state_phase_transitions(self):
        """Test AmongUsState phase transition scenarios."""
        # Test all valid phases
        phases = [
            AmongUsGamePhase.LOBBY,
            AmongUsGamePhase.TASKS,
            AmongUsGamePhase.EMERGENCY,
            AmongUsGamePhase.DISCUSSION,
            AmongUsGamePhase.VOTING,
            AmongUsGamePhase.GAME_OVER,
        ]

        for phase in phases:
            state = AmongUsState(game_phase=phase)
            assert state.game_phase == phase

    def test_among_us_state_meeting_phases(self):
        """Test AmongUsState meeting phase management."""
        state = AmongUsState(
            game_phase=AmongUsGamePhase.DISCUSSION, meeting_phase=MeetingPhase.REPORT
        )

        assert state.meeting_phase == MeetingPhase.REPORT

        # Test all meeting phases
        meeting_phases = [
            MeetingPhase.REPORT,
            MeetingPhase.DISCUSSION,
            MeetingPhase.ACCUSATION,
            MeetingPhase.DEFENSE,
            MeetingPhase.VOTING,
        ]

        for phase in meeting_phases:
            state.meeting_phase = phase
            assert state.meeting_phase == phase

    def test_among_us_state_task_tracking(self):
        """Test AmongUsState task completion tracking."""
        # Create tasks
        task1 = Task(
            id="task1",
            name="Fix Wiring",
            type=TaskType.COMMON,
            location="electrical",
            steps_required=3,
            steps_completed=3,
            status=TaskStatus.COMPLETED,
        )

        task2 = Task(
            id="task2",
            name="Upload Data",
            type=TaskType.LONG,
            location="admin",
            steps_required=5,
            steps_completed=2,
            status=TaskStatus.IN_PROGRESS,
        )

        # Create player with tasks
        player = PlayerState(
            id="player1",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            tasks=[task1, task2],
            is_alive=True,
            memory=PlayerMemory(),
        )

        state = AmongUsState(
            players={"player1": player}, tasks_completed=1, total_tasks=2
        )

        assert state.tasks_completed == 1
        assert state.total_tasks == 2

    def test_among_us_state_voting_system(self):
        """Test AmongUsState voting system."""
        votes = {
            "player1": "player3",  # player1 votes for player3
            "player2": "player3",  # player2 votes for player3
            "player3": "skip",  # player3 votes to skip
            "player4": "player1",  # player4 votes for player1
        }

        state = AmongUsState(
            game_phase=AmongUsGamePhase.VOTING, current_votes=votes, voting_timer=30
        )

        assert len(state.current_votes) == 4
        assert state.current_votes["player1"] == "player3"
        assert state.current_votes["player3"] == "skip"
        assert state.voting_timer == 30

    def test_among_us_state_elimination_tracking(self):
        """Test AmongUsState player elimination tracking."""
        eliminated = ["player3", "player5"]

        state = AmongUsState(eliminated_players=eliminated, bodies_reported=2)

        assert len(state.eliminated_players) == 2
        assert "player3" in state.eliminated_players
        assert "player5" in state.eliminated_players
        assert state.bodies_reported == 2

    def test_among_us_state_emergency_meetings(self):
        """Test AmongUsState emergency meeting tracking."""
        state = AmongUsState(
            game_phase=AmongUsGamePhase.EMERGENCY,
            emergency_meetings_called=2,
            discussion_timer=120,
        )

        assert state.game_phase == AmongUsGamePhase.EMERGENCY
        assert state.emergency_meetings_called == 2
        assert state.discussion_timer == 120

    def test_among_us_state_sabotage_system(self):
        """Test AmongUsState sabotage system."""
        from haive.games.among_us.models import SabotageType

        state = AmongUsState(sabotage_active=SabotageType.REACTOR, sabotage_timer=30)

        assert state.sabotage_active == SabotageType.REACTOR
        assert state.sabotage_timer == 30

    def test_among_us_state_win_conditions(self):
        """Test AmongUsState win condition scenarios."""
        # Crewmate win by tasks
        state = AmongUsState(winner="crewmates", game_end_reason="All tasks completed")

        assert state.winner == "crewmates"
        assert state.game_end_reason == "All tasks completed"

        # Impostor win by elimination
        state = AmongUsState(
            winner="impostors", game_end_reason="Impostors equal crewmates"
        )

        assert state.winner == "impostors"
        assert state.game_end_reason == "Impostors equal crewmates"

    def test_among_us_state_complex_game_scenario(self):
        """Test AmongUsState with complex game scenario."""
        # Create diverse player states
        players = {}

        # Living crewmates
        for i in range(3):
            player = PlayerState(
                id=f"crewmate{i}",
                role=PlayerRole.CREWMATE,
                location="cafeteria",
                is_alive=True,
                memory=PlayerMemory(),
                tasks=[
                    Task(
                        id=f"task{i}",
                        name=f"Task {i}",
                        type=TaskType.COMMON,
                        location="electrical",
                        steps_required=3,
                        steps_completed=2,
                        status=TaskStatus.IN_PROGRESS,
                    )
                ],
            )
            players[f"crewmate{i}"] = player

        # Living impostor
        impostor = PlayerState(
            id="impostor1",
            role=PlayerRole.IMPOSTOR,
            location="electrical",
            is_alive=True,
            memory=PlayerMemory(),
            cooldown_remaining=15,
        )
        players["impostor1"] = impostor

        # Dead players
        ghost = PlayerState(
            id="ghost1",
            role=PlayerRole.CREWMATE,
            location="medical",
            is_alive=False,
            memory=PlayerMemory(),
        )
        players["ghost1"] = ghost

        # Create complex state
        state = AmongUsState(
            game_phase=AmongUsGamePhase.DISCUSSION,
            players=players,
            eliminated_players=["ghost1"],
            current_round=3,
            emergency_meetings_called=1,
            bodies_reported=1,
            meeting_phase=MeetingPhase.DISCUSSION,
            discussion_timer=60,
            tasks_completed=4,
            total_tasks=9,
        )

        # Verify complex state
        assert len(state.players) == 5
        assert sum(1 for p in state.players.values() if p.is_alive) == 4
        assert (
            sum(1 for p in state.players.values() if p.role == PlayerRole.CREWMATE) == 4
        )
        assert (
            sum(1 for p in state.players.values() if p.role == PlayerRole.IMPOSTOR) == 1
        )
        assert len(state.eliminated_players) == 1
        assert state.current_round == 3
        assert state.tasks_completed == 4
        assert state.total_tasks == 9

    def test_among_us_state_default_factories(self):
        """Test AmongUsState default factories create separate instances."""
        state1 = AmongUsState()
        state2 = AmongUsState()

        # Modify one instance
        state1.players["test"] = PlayerState(
            id="test",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            is_alive=True,
            memory=PlayerMemory(),
        )
        state1.eliminated_players.append("eliminated1")
        state1.current_votes["voter1"] = "target1"

        # Other instance should not be affected
        assert len(state2.players) == 0
        assert len(state2.eliminated_players) == 0
        assert len(state2.current_votes) == 0

    def test_among_us_state_serialization(self):
        """Test AmongUsState serialization to dictionary."""
        player = PlayerState(
            id="player1",
            role=PlayerRole.CREWMATE,
            location="cafeteria",
            is_alive=True,
            memory=PlayerMemory(),
        )

        state = AmongUsState(
            game_phase=AmongUsGamePhase.TASKS,
            players={"player1": player},
            current_round=2,
            tasks_completed=3,
            total_tasks=10,
        )

        state_dict = state.model_dump()

        assert state_dict["game_phase"] == "TASKS"
        assert "player1" in state_dict["players"]
        assert state_dict["current_round"] == 2
        assert state_dict["tasks_completed"] == 3
        assert state_dict["total_tasks"] == 10

    def test_among_us_state_deserialization(self):
        """Test AmongUsState deserialization from dictionary."""
        state_dict = {
            "game_phase": "TASKS",
            "players": {
                "player1": {
                    "id": "player1",
                    "role": "CREWMATE",
                    "location": "cafeteria",
                    "tasks": [],
                    "is_alive": True,
                    "observations": [],
                    "memory": {
                        "observations": [],
                        "player_suspicions": {},
                        "player_alibis": {},
                        "location_history": [],
                    },
                    "cooldown_remaining": 0,
                }
            },
            "eliminated_players": [],
            "current_round": 1,
            "emergency_meetings_called": 0,
            "bodies_reported": 0,
            "meeting_phase": None,
            "discussion_timer": 0,
            "voting_timer": 0,
            "current_votes": {},
            "tasks_completed": 0,
            "total_tasks": 5,
            "sabotage_active": None,
            "sabotage_timer": 0,
            "game_start_time": None,
            "winner": None,
            "game_end_reason": None,
        }

        state = AmongUsState(**state_dict)

        assert state.game_phase == AmongUsGamePhase.TASKS
        assert len(state.players) == 1
        assert state.players["player1"].role == PlayerRole.CREWMATE
        assert state.total_tasks == 5

    def test_among_us_state_player_location_tracking(self):
        """Test AmongUsState player location tracking."""
        players = {}
        locations = ["cafeteria", "electrical", "storage", "admin", "medbay"]

        for i, location in enumerate(locations):
            player = PlayerState(
                id=f"player{i}",
                role=PlayerRole.CREWMATE if i < 4 else PlayerRole.IMPOSTOR,
                location=location,
                is_alive=True,
                memory=PlayerMemory(location_history=[location]),
            )
            players[f"player{i}"] = player

        state = AmongUsState(players=players)

        # Verify all players have correct locations
        assert state.players["player0"].location == "cafeteria"
        assert state.players["player1"].location == "electrical"
        assert state.players["player2"].location == "storage"
        assert state.players["player3"].location == "admin"
        assert state.players["player4"].location == "medbay"

    def test_among_us_state_round_progression(self):
        """Test AmongUsState round progression tracking."""
        state = AmongUsState(current_round=1)

        # Simulate round progression
        for round_num in range(1, 6):
            state.current_round = round_num
            assert state.current_round == round_num

    def test_among_us_state_timer_management(self):
        """Test AmongUsState timer management for different phases."""
        # Discussion timer
        state = AmongUsState(
            game_phase=AmongUsGamePhase.DISCUSSION, discussion_timer=120
        )
        assert state.discussion_timer == 120

        # Voting timer
        state.game_phase = AmongUsGamePhase.VOTING
        state.voting_timer = 60
        assert state.voting_timer == 60

        # Sabotage timer
        from haive.games.among_us.models import SabotageType

        state.sabotage_active = SabotageType.REACTOR
        state.sabotage_timer = 30
        assert state.sabotage_timer == 30

    def test_among_us_state_empty_game(self):
        """Test AmongUsState with no players (edge case)."""
        state = AmongUsState(
            game_phase=AmongUsGamePhase.LOBBY, players={}, total_tasks=0
        )

        assert len(state.players) == 0
        assert state.total_tasks == 0
        assert state.game_phase == AmongUsGamePhase.LOBBY

    def test_among_us_state_all_players_dead(self):
        """Test AmongUsState with all players dead (edge case)."""
        players = {}
        for i in range(3):
            player = PlayerState(
                id=f"player{i}",
                role=PlayerRole.CREWMATE,
                location="graveyard",
                is_alive=False,
                memory=PlayerMemory(),
            )
            players[f"player{i}"] = player

        state = AmongUsState(
            players=players,
            eliminated_players=["player0", "player1", "player2"],
            winner="impostors",
            game_end_reason="All crewmates eliminated",
        )

        assert all(not p.is_alive for p in state.players.values())
        assert len(state.eliminated_players) == 3
        assert state.winner == "impostors"
