"""Test suite for Mafia game state manager."""

# Standard library imports
import random
from typing import Any, Dict, List, Optional

# Third-party imports
import pytest

# Local imports
from haive.games.mafia.models import (
    MafiaAction,
    MafiaActionType,
    MafiaGameConfig,
    MafiaGameState,
    MafiaObservation,
    MafiaPlayer,
    MafiaRole,
    MafiaRoundPhase,
    MafiaVote,
)
from haive.games.mafia.state import MafiaState
from haive.games.mafia.state_manager import MafiaStateManager


class TestMafiaStateManager:
    """Test the MafiaStateManager class."""

    def test_init_manager(self):
        """Test initializing the state manager."""
        manager = MafiaStateManager()

        assert isinstance(manager.state, MafiaState)
        assert isinstance(manager.config, MafiaGameConfig)
        assert manager.moderator_name == "Moderator"
        assert manager.state.game_state.players == []
        assert manager.state.game_state.game_over is False

    def test_init_with_custom_config(self):
        """Test initializing with custom config."""
        config = MafiaGameConfig(
            min_players=8, max_players=16, mafia_ratio=0.3, enable_detective=False
        )

        manager = MafiaStateManager(config=config)

        assert manager.config == config
        assert manager.config.min_players == 8
        assert manager.config.mafia_ratio == 0.3
        assert manager.config.enable_detective is False

    def test_init_with_moderator_name(self):
        """Test initializing with custom moderator name."""
        manager = MafiaStateManager(moderator_name="GameMaster")

        assert manager.moderator_name == "GameMaster"

    def test_reset_game(self):
        """Test resetting the game."""
        manager = MafiaStateManager()

        # Add some players and state
        manager.state.game_state.players = [
            MafiaPlayer(name="Player1", role=MafiaRole.CITIZEN),
            MafiaPlayer(name="Player2", role=MafiaRole.MAFIA),
        ]
        manager.state.game_state.round_number = 5
        manager.state.game_state.game_over = True

        # Reset
        manager.reset_game()

        # Verify reset
        assert manager.state.game_state.players == []
        assert manager.state.game_state.round_number == 0
        assert manager.state.game_state.phase == MafiaRoundPhase.NIGHT
        assert manager.state.game_state.game_over is False

    def test_add_player(self):
        """Test adding players."""
        manager = MafiaStateManager()

        # Add first player
        success1 = manager.add_player("Alice")
        assert success1 is True
        assert len(manager.state.players) == 1
        assert manager.state.players[0].name == "Alice"
        assert manager.state.players[0].role == MafiaRole.CITIZEN  # Default role

        # Add second player
        success2 = manager.add_player("Bob")
        assert success2 is True
        assert len(manager.state.players) == 2

        # Try to add duplicate
        success3 = manager.add_player("Alice")
        assert success3 is False
        assert len(manager.state.players) == 2

    def test_add_player_max_limit(self):
        """Test adding players beyond max limit."""
        config = MafiaGameConfig(max_players=3)
        manager = MafiaStateManager(config=config)

        # Add players up to limit
        assert manager.add_player("Player1") is True
        assert manager.add_player("Player2") is True
        assert manager.add_player("Player3") is True

        # Try to exceed limit
        assert manager.add_player("Player4") is False
        assert len(manager.state.players) == 3

    def test_remove_player(self):
        """Test removing players."""
        manager = MafiaStateManager()

        # Add players
        manager.add_player("Alice")
        manager.add_player("Bob")

        # Remove existing player
        success1 = manager.remove_player("Alice")
        assert success1 is True
        assert len(manager.state.players) == 1
        assert manager.state.players[0].name == "Bob"

        # Try to remove non-existent player
        success2 = manager.remove_player("Charlie")
        assert success2 is False
        assert len(manager.state.players) == 1

    def test_start_game_insufficient_players(self):
        """Test starting game with insufficient players."""
        manager = MafiaStateManager()

        # Add too few players
        manager.add_player("Player1")
        manager.add_player("Player2")

        # Try to start
        success = manager.start_game()
        assert success is False
        assert manager.state.game_state.game_over is False

    def test_start_game_assigns_roles(self):
        """Test starting game assigns roles correctly."""
        config = MafiaGameConfig(
            min_players=6,
            mafia_ratio=0.33,  # 2 mafia for 6 players
            enable_detective=True,
            enable_doctor=True,
        )
        manager = MafiaStateManager(config=config)

        # Add 6 players
        for i in range(6):
            manager.add_player(f"Player{i+1}")

        # Start game
        success = manager.start_game()
        assert success is True

        # Check role distribution
        roles = [p.role for p in manager.state.players]
        mafia_count = sum(1 for r in roles if r == MafiaRole.MAFIA)
        detective_count = sum(1 for r in roles if r == MafiaRole.DETECTIVE)
        doctor_count = sum(1 for r in roles if r == MafiaRole.DOCTOR)
        citizen_count = sum(1 for r in roles if r == MafiaRole.CITIZEN)

        assert mafia_count == 2  # 33% of 6 = 2
        assert detective_count == 1
        assert doctor_count == 1
        assert citizen_count == 2  # Remaining players

    def test_start_game_without_special_roles(self):
        """Test starting game without special roles."""
        config = MafiaGameConfig(
            min_players=6, mafia_ratio=0.25, enable_detective=False, enable_doctor=False
        )
        manager = MafiaStateManager(config=config)

        # Add 6 players
        for i in range(6):
            manager.add_player(f"Player{i+1}")

        # Start game
        success = manager.start_game()
        assert success is True

        # Check only mafia and citizens
        roles = [p.role for p in manager.state.players]
        assert MafiaRole.DETECTIVE not in roles
        assert MafiaRole.DOCTOR not in roles
        assert MafiaRole.MAFIA in roles
        assert MafiaRole.CITIZEN in roles

    def test_get_observation(self):
        """Test getting player observations."""
        manager = MafiaStateManager()

        # Setup game
        manager.state.game_state.players = [
            MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="Bob", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="Charlie", role=MafiaRole.DETECTIVE, is_alive=False),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.DAY_VOTING
        manager.state.game_state.eliminated_players = ["Charlie"]

        # Get observation for alive player
        obs = manager.get_observation("Alice")
        assert isinstance(obs, MafiaObservation)
        assert obs.player_name == "Alice"
        assert obs.role == MafiaRole.CITIZEN
        assert obs.is_alive is True
        assert obs.phase == MafiaRoundPhase.DAY_VOTING
        assert len(obs.alive_players) == 2
        assert obs.dead_players == ["Charlie"]

        # Get observation for moderator
        mod_obs = manager.get_observation("Moderator")
        assert mod_obs.role == MafiaRole.MODERATOR
        # Moderator sees all roles
        assert mod_obs.role_info is not None
        assert len(mod_obs.role_info) == 3

    def test_process_action_valid(self):
        """Test processing valid actions."""
        manager = MafiaStateManager()

        # Setup game
        manager.state.game_state.players = [
            MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="Victim", role=MafiaRole.CITIZEN, is_alive=True),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.NIGHT

        # Process valid kill action
        action = MafiaAction(
            player_name="Mafia", action_type=MafiaActionType.KILL, target="Victim"
        )

        success, message = manager.process_action(action)
        assert success is True
        assert "recorded" in message.lower()
        assert len(manager.state.game_state.actions) == 1

    def test_process_action_invalid(self):
        """Test processing invalid actions."""
        manager = MafiaStateManager()

        # Setup game
        manager.state.game_state.players = [
            MafiaPlayer(name="Citizen", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="Target", role=MafiaRole.MAFIA, is_alive=True),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.NIGHT

        # Process invalid action (citizen can't kill)
        action = MafiaAction(
            player_name="Citizen", action_type=MafiaActionType.KILL, target="Target"
        )

        success, message = manager.process_action(action)
        assert success is False
        assert "invalid" in message.lower()
        assert len(manager.state.game_state.actions) == 0

    def test_advance_phase(self):
        """Test advancing game phase."""
        manager = MafiaStateManager()

        # Setup game
        manager.state.game_state.players = [
            MafiaPlayer(name="Player1", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="Player2", role=MafiaRole.MAFIA, is_alive=True),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.NIGHT

        # Advance phase
        new_phase = manager.advance_phase()

        assert new_phase == MafiaRoundPhase.DAY_DISCUSSION
        assert manager.state.phase == MafiaRoundPhase.DAY_DISCUSSION

    def test_advance_phase_with_elimination(self):
        """Test advancing phase with player elimination."""
        manager = MafiaStateManager()

        # Setup game with kill action
        manager.state.game_state.players = [
            MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="Victim", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="Other", role=MafiaRole.CITIZEN, is_alive=True),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.NIGHT
        manager.state.game_state.actions = [
            MafiaAction(
                player_name="Mafia", action_type=MafiaActionType.KILL, target="Victim"
            )
        ]

        # Advance phase
        manager.advance_phase()

        # Check victim was eliminated
        victim = next(p for p in manager.state.players if p.name == "Victim")
        assert victim.is_alive is False
        assert "Victim" in manager.state.game_state.eliminated_players

    def test_advance_phase_game_over(self):
        """Test advancing phase when game should end."""
        manager = MafiaStateManager()

        # Setup game where mafia wins
        manager.state.game_state.players = [
            MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="Citizen", role=MafiaRole.CITIZEN, is_alive=True),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.DAY_DISCUSSION

        # Advance phase
        new_phase = manager.advance_phase()

        # Game should be over
        assert new_phase == MafiaRoundPhase.GAME_OVER
        assert manager.state.game_over is True
        assert manager.state.winner == "mafia"

    def test_get_game_status(self):
        """Test getting game status."""
        manager = MafiaStateManager()

        # Setup ongoing game
        manager.state.game_state.players = [
            MafiaPlayer(name="Player1", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="Player2", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="Player3", role=MafiaRole.CITIZEN, is_alive=False),
        ]
        manager.state.game_state.phase = MafiaRoundPhase.DAY_VOTING
        manager.state.game_state.round_number = 3
        manager.state.game_state.eliminated_players = ["Player3"]

        status = manager.get_game_status()

        assert status["phase"] == "day_voting"
        assert status["round"] == 3
        assert status["alive_count"] == 2
        assert status["dead_count"] == 1
        assert status["game_over"] is False
        assert status["winner"] is None
        assert status["last_eliminated"] is None

    def test_get_vote_summary(self):
        """Test getting vote summary."""
        manager = MafiaStateManager()

        # Setup votes
        manager.state.game_state.votes = [
            MafiaVote(voter="Player1", target="Suspect"),
            MafiaVote(voter="Player2", target="Suspect"),
            MafiaVote(voter="Player3", target="Other"),
        ]

        summary = manager.get_vote_summary()

        assert summary["Suspect"] == 2
        assert summary["Other"] == 1
        assert len(summary) == 2

    def test_state_persistence(self):
        """Test state save and load."""
        manager = MafiaStateManager()

        # Setup game state
        manager.add_player("Alice")
        manager.add_player("Bob")
        manager.state.game_state.round_number = 5
        manager.state.game_state.phase = MafiaRoundPhase.DAY_DISCUSSION

        # Save state
        state_dict = manager.save_state()

        # Create new manager and load state
        new_manager = MafiaStateManager()
        new_manager.load_state(state_dict)

        # Verify loaded state
        assert len(new_manager.state.players) == 2
        assert new_manager.state.players[0].name == "Alice"
        assert new_manager.state.round_number == 5
        assert new_manager.state.phase == MafiaRoundPhase.DAY_DISCUSSION

    def test_role_assignment_randomness(self):
        """Test that role assignment is random."""
        manager = MafiaStateManager()

        # Add players
        for i in range(6):
            manager.add_player(f"Player{i+1}")

        # Start multiple games and check role distribution
        role_sets = []
        for _ in range(5):
            manager.start_game()
            roles = tuple(sorted(p.role.value for p in manager.state.players))
            role_sets.append(roles)
            manager.reset_game()
            # Re-add players
            for i in range(6):
                manager.add_player(f"Player{i+1}")

        # Should have some variation in role assignment order
        # (This test might rarely fail due to random chance)
        unique_assignments = len(set(role_sets))
        assert unique_assignments > 1

    def test_get_action_results(self):
        """Test getting action results."""
        manager = MafiaStateManager()

        # Setup game with completed actions
        manager.state.game_state.players = [
            MafiaPlayer(name="Detective", role=MafiaRole.DETECTIVE, is_alive=True),
            MafiaPlayer(name="Suspect", role=MafiaRole.MAFIA, is_alive=True),
        ]

        # Add investigation result (this would normally be done during phase transition)
        manager.state.game_state.last_investigation = {
            "investigator": "Detective",
            "target": "Suspect",
            "is_mafia": True,
        }

        # Get results for detective
        results = manager.get_action_results("Detective")
        assert "investigation" in results
        assert results["investigation"]["target"] == "Suspect"
        assert results["investigation"]["is_mafia"] is True

        # Non-detective shouldn't see results
        other_results = manager.get_action_results("Suspect")
        assert "investigation" not in other_results
