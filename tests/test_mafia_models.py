"""Test suite for Mafia game models."""

# Standard library imports

# Third-party imports
import pytest
from pydantic import ValidationError

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
    create_mafia_observation,
)


class TestMafiaRole:
    """Test the MafiaRole enum."""

    def test_role_values(self):
        """Test that all role values are defined correctly."""
        assert MafiaRole.CITIZEN.value == "citizen"
        assert MafiaRole.MAFIA.value == "mafia"
        assert MafiaRole.DETECTIVE.value == "detective"
        assert MafiaRole.DOCTOR.value == "doctor"
        assert MafiaRole.MODERATOR.value == "moderator"

    def test_role_properties(self):
        """Test role properties."""
        # Test is_mafia property
        assert MafiaRole.MAFIA.is_mafia is True
        assert MafiaRole.CITIZEN.is_mafia is False
        assert MafiaRole.DETECTIVE.is_mafia is False
        assert MafiaRole.DOCTOR.is_mafia is False
        assert MafiaRole.MODERATOR.is_mafia is False

        # Test is_special property
        assert MafiaRole.DETECTIVE.is_special is True
        assert MafiaRole.DOCTOR.is_special is True
        assert MafiaRole.CITIZEN.is_special is False
        assert MafiaRole.MAFIA.is_special is False
        assert MafiaRole.MODERATOR.is_special is False

    def test_all_roles(self):
        """Test that we can iterate over all roles."""
        roles = list(MafiaRole)
        assert len(roles) == 5
        assert MafiaRole.CITIZEN in roles
        assert MafiaRole.MAFIA in roles
        assert MafiaRole.DETECTIVE in roles
        assert MafiaRole.DOCTOR in roles
        assert MafiaRole.MODERATOR in roles


class TestMafiaRoundPhase:
    """Test the MafiaRoundPhase enum."""

    def test_phase_values(self):
        """Test that all phase values are defined correctly."""
        assert MafiaRoundPhase.NIGHT.value == "night"
        assert MafiaRoundPhase.DAY_DISCUSSION.value == "day_discussion"
        assert MafiaRoundPhase.DAY_VOTING.value == "day_voting"
        assert MafiaRoundPhase.GAME_OVER.value == "game_over"

    def test_phase_properties(self):
        """Test phase properties."""
        # Test is_night property
        assert MafiaRoundPhase.NIGHT.is_night is True
        assert MafiaRoundPhase.DAY_DISCUSSION.is_night is False
        assert MafiaRoundPhase.DAY_VOTING.is_night is False
        assert MafiaRoundPhase.GAME_OVER.is_night is False

        # Test is_day property
        assert MafiaRoundPhase.DAY_DISCUSSION.is_day is True
        assert MafiaRoundPhase.DAY_VOTING.is_day is True
        assert MafiaRoundPhase.NIGHT.is_day is False
        assert MafiaRoundPhase.GAME_OVER.is_day is False


class TestMafiaActionType:
    """Test the MafiaActionType enum."""

    def test_action_values(self):
        """Test that all action values are defined correctly."""
        assert MafiaActionType.KILL.value == "kill"
        assert MafiaActionType.INVESTIGATE.value == "investigate"
        assert MafiaActionType.HEAL.value == "heal"
        assert MafiaActionType.VOTE.value == "vote"
        assert MafiaActionType.PASS.value == "pass"


class TestMafiaPlayer:
    """Test the MafiaPlayer class."""

    def test_create_valid_player(self):
        """Test creating a valid player."""
        player = MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN, is_alive=True)
        assert player.name == "Alice"
        assert player.role == MafiaRole.CITIZEN
        assert player.is_alive is True

    def test_player_defaults(self):
        """Test player default values."""
        player = MafiaPlayer(name="Bob", role=MafiaRole.MAFIA)
        assert player.is_alive is True

    def test_player_role_assignment(self):
        """Test different role assignments."""
        citizen = MafiaPlayer(name="C", role=MafiaRole.CITIZEN)
        mafia = MafiaPlayer(name="M", role=MafiaRole.MAFIA)
        detective = MafiaPlayer(name="D", role=MafiaRole.DETECTIVE)
        doctor = MafiaPlayer(name="Dr", role=MafiaRole.DOCTOR)
        moderator = MafiaPlayer(name="Mod", role=MafiaRole.MODERATOR)

        assert citizen.role == MafiaRole.CITIZEN
        assert mafia.role == MafiaRole.MAFIA
        assert detective.role == MafiaRole.DETECTIVE
        assert doctor.role == MafiaRole.DOCTOR
        assert moderator.role == MafiaRole.MODERATOR

    def test_player_serialization(self):
        """Test player serialization."""
        player = MafiaPlayer(name="Test", role=MafiaRole.DETECTIVE, is_alive=False)
        data = player.model_dump()

        assert data["name"] == "Test"
        assert data["role"] == "detective"
        assert data["is_alive"] is False

        # Test deserialization
        player2 = MafiaPlayer(**data)
        assert player2.name == player.name
        assert player2.role == player.role
        assert player2.is_alive == player.is_alive


class TestMafiaAction:
    """Test the MafiaAction class."""

    def test_create_valid_action(self):
        """Test creating valid actions."""
        # Kill action
        kill = MafiaAction(
            player_name="Mafia1", action_type=MafiaActionType.KILL, target="Victim"
        )
        assert kill.player_name == "Mafia1"
        assert kill.action_type == MafiaActionType.KILL
        assert kill.target == "Victim"

        # Pass action
        pass_action = MafiaAction(
            player_name="Player1", action_type=MafiaActionType.PASS
        )
        assert pass_action.player_name == "Player1"
        assert pass_action.action_type == MafiaActionType.PASS
        assert pass_action.target is None

    def test_action_with_optional_target(self):
        """Test actions with optional targets."""
        # Actions that require targets
        with pytest.raises(ValidationError):
            MafiaAction(
                player_name="Detective", action_type=MafiaActionType.INVESTIGATE
            )

        # Pass action doesn't need target
        pass_action = MafiaAction(
            player_name="Player", action_type=MafiaActionType.PASS
        )
        assert pass_action.target is None

    def test_action_serialization(self):
        """Test action serialization."""
        action = MafiaAction(
            player_name="Doctor", action_type=MafiaActionType.HEAL, target="Patient"
        )
        data = action.model_dump()

        assert data["player_name"] == "Doctor"
        assert data["action_type"] == "heal"
        assert data["target"] == "Patient"

        # Test deserialization
        action2 = MafiaAction(**data)
        assert action2.player_name == action.player_name
        assert action2.action_type == action.action_type
        assert action2.target == action.target


class TestMafiaVote:
    """Test the MafiaVote class."""

    def test_create_valid_vote(self):
        """Test creating a valid vote."""
        vote = MafiaVote(voter="Alice", target="Bob")
        assert vote.voter == "Alice"
        assert vote.target == "Bob"

    def test_vote_serialization(self):
        """Test vote serialization."""
        vote = MafiaVote(voter="Player1", target="Player2")
        data = vote.model_dump()

        assert data["voter"] == "Player1"
        assert data["target"] == "Player2"

        # Test deserialization
        vote2 = MafiaVote(**data)
        assert vote2.voter == vote.voter
        assert vote2.target == vote.target


class TestMafiaGameConfig:
    """Test the MafiaGameConfig class."""

    def test_create_default_config(self):
        """Test creating config with defaults."""
        config = MafiaGameConfig()
        assert config.min_players == 6
        assert config.max_players == 12
        assert config.mafia_ratio == 0.25
        assert config.enable_detective is True
        assert config.enable_doctor is True
        assert config.discussion_time_seconds == 180
        assert config.voting_time_seconds == 60
        assert config.night_time_seconds == 90

    def test_create_custom_config(self):
        """Test creating config with custom values."""
        config = MafiaGameConfig(
            min_players=8,
            max_players=16,
            mafia_ratio=0.3,
            enable_detective=False,
            enable_doctor=True,
            discussion_time_seconds=120,
            voting_time_seconds=30,
            night_time_seconds=60,
        )
        assert config.min_players == 8
        assert config.max_players == 16
        assert config.mafia_ratio == 0.3
        assert config.enable_detective is False
        assert config.enable_doctor is True
        assert config.discussion_time_seconds == 120
        assert config.voting_time_seconds == 30
        assert config.night_time_seconds == 60

    def test_config_validation(self):
        """Test config validation."""
        # Invalid mafia ratio
        with pytest.raises(ValidationError):
            MafiaGameConfig(mafia_ratio=1.5)

        with pytest.raises(ValidationError):
            MafiaGameConfig(mafia_ratio=-0.1)

        # Invalid player counts
        with pytest.raises(ValidationError):
            MafiaGameConfig(min_players=2)  # Too few

        with pytest.raises(ValidationError):
            MafiaGameConfig(max_players=50)  # Too many

        # Min > Max
        with pytest.raises(ValidationError):
            MafiaGameConfig(min_players=10, max_players=8)


class TestMafiaGameState:
    """Test the MafiaGameState class."""

    def test_create_minimal_state(self):
        """Test creating a minimal game state."""
        state = MafiaGameState()
        assert state.players == []
        assert state.round_number == 0
        assert state.phase == MafiaRoundPhase.NIGHT
        assert state.actions == []
        assert state.votes == []
        assert state.eliminated_players == []
        assert state.last_eliminated is None
        assert state.winner is None
        assert state.game_over is False
        assert isinstance(state.config, MafiaGameConfig)

    def test_create_full_state(self):
        """Test creating a full game state."""
        players = [
            MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN),
            MafiaPlayer(name="Bob", role=MafiaRole.MAFIA),
            MafiaPlayer(name="Charlie", role=MafiaRole.DETECTIVE),
        ]

        actions = [
            MafiaAction(
                player_name="Bob", action_type=MafiaActionType.KILL, target="Alice"
            )
        ]

        votes = [
            MafiaVote(voter="Alice", target="Bob"),
            MafiaVote(voter="Charlie", target="Bob"),
        ]

        state = MafiaGameState(
            players=players,
            round_number=2,
            phase=MafiaRoundPhase.DAY_VOTING,
            actions=actions,
            votes=votes,
            eliminated_players=["David"],
            last_eliminated="David",
            config=MafiaGameConfig(min_players=4),
        )

        assert len(state.players) == 3
        assert state.round_number == 2
        assert state.phase == MafiaRoundPhase.DAY_VOTING
        assert len(state.actions) == 1
        assert len(state.votes) == 2
        assert state.eliminated_players == ["David"]
        assert state.last_eliminated == "David"
        assert state.config.min_players == 4

    def test_game_state_properties(self):
        """Test computed properties."""
        players = [
            MafiaPlayer(name="A", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="B", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="C", role=MafiaRole.CITIZEN, is_alive=False),
            MafiaPlayer(name="D", role=MafiaRole.DETECTIVE, is_alive=True),
        ]

        state = MafiaGameState(players=players)

        # Test alive_players property
        alive = state.alive_players
        assert len(alive) == 3
        assert all(p.is_alive for p in alive)

        # Test mafia_count property
        assert state.mafia_count == 1

        # Test citizen_count property
        assert state.citizen_count == 2  # 1 citizen + 1 detective

    def test_game_over_conditions(self):
        """Test game over detection."""
        # Mafia wins
        players1 = [
            MafiaPlayer(name="A", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="B", role=MafiaRole.CITIZEN, is_alive=True),
        ]
        state1 = MafiaGameState(players=players1, game_over=True, winner="mafia")
        assert state1.game_over is True
        assert state1.winner == "mafia"

        # Citizens win
        players2 = [
            MafiaPlayer(name="A", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="B", role=MafiaRole.DETECTIVE, is_alive=True),
            MafiaPlayer(name="C", role=MafiaRole.MAFIA, is_alive=False),
        ]
        state2 = MafiaGameState(players=players2, game_over=True, winner="citizens")
        assert state2.game_over is True
        assert state2.winner == "citizens"

    def test_state_serialization(self):
        """Test state serialization."""
        state = MafiaGameState(
            players=[MafiaPlayer(name="Test", role=MafiaRole.DOCTOR)],
            round_number=5,
            phase=MafiaRoundPhase.NIGHT,
        )

        data = state.model_dump()
        assert len(data["players"]) == 1
        assert data["round_number"] == 5
        assert data["phase"] == "night"

        # Test deserialization
        state2 = MafiaGameState(**data)
        assert len(state2.players) == 1
        assert state2.round_number == 5
        assert state2.phase == MafiaRoundPhase.NIGHT


class TestMafiaObservation:
    """Test the MafiaObservation class."""

    def test_create_observation(self):
        """Test creating an observation."""
        obs = MafiaObservation(
            player_name="Alice",
            role=MafiaRole.DETECTIVE,
            is_alive=True,
            phase=MafiaRoundPhase.NIGHT,
            round_number=3,
            alive_players=["Alice", "Bob", "Charlie"],
            dead_players=["David"],
            last_eliminated="David",
            game_over=False,
            winner=None,
            available_actions=[MafiaActionType.INVESTIGATE, MafiaActionType.PASS],
            role_info={"Bob": MafiaRole.CITIZEN},
        )

        assert obs.player_name == "Alice"
        assert obs.role == MafiaRole.DETECTIVE
        assert obs.is_alive is True
        assert obs.phase == MafiaRoundPhase.NIGHT
        assert obs.round_number == 3
        assert len(obs.alive_players) == 3
        assert obs.dead_players == ["David"]
        assert obs.last_eliminated == "David"
        assert obs.game_over is False
        assert obs.winner is None
        assert len(obs.available_actions) == 2
        assert obs.role_info == {"Bob": MafiaRole.CITIZEN}

    def test_observation_defaults(self):
        """Test observation default values."""
        obs = MafiaObservation(
            player_name="Test",
            role=MafiaRole.CITIZEN,
            is_alive=True,
            phase=MafiaRoundPhase.DAY_DISCUSSION,
            round_number=1,
            alive_players=["Test"],
            dead_players=[],
            game_over=False,
            available_actions=[],
        )

        assert obs.last_eliminated is None
        assert obs.winner is None
        assert obs.role_info is None

    def test_observation_serialization(self):
        """Test observation serialization."""
        obs = MafiaObservation(
            player_name="Player",
            role=MafiaRole.MAFIA,
            is_alive=True,
            phase=MafiaRoundPhase.NIGHT,
            round_number=2,
            alive_players=["Player", "Other"],
            dead_players=[],
            game_over=False,
            available_actions=[MafiaActionType.KILL],
        )

        data = obs.model_dump()
        assert data["player_name"] == "Player"
        assert data["role"] == "mafia"
        assert data["phase"] == "night"
        assert data["available_actions"] == ["kill"]

        # Test deserialization
        obs2 = MafiaObservation(**data)
        assert obs2.player_name == obs.player_name
        assert obs2.role == obs.role
        assert obs2.available_actions == obs.available_actions


class TestCreateMafiaObservation:
    """Test the create_mafia_observation function."""

    def test_create_citizen_observation(self):
        """Test creating observation for a citizen."""
        state = MafiaGameState(
            players=[
                MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Bob", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Charlie", role=MafiaRole.DETECTIVE, is_alive=False),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
            round_number=2,
            eliminated_players=["Charlie"],
            last_eliminated="Charlie",
        )

        obs = create_mafia_observation(state, "Alice")

        assert obs.player_name == "Alice"
        assert obs.role == MafiaRole.CITIZEN
        assert obs.is_alive is True
        assert obs.phase == MafiaRoundPhase.DAY_VOTING
        assert obs.round_number == 2
        assert len(obs.alive_players) == 2
        assert "Alice" in obs.alive_players
        assert "Bob" in obs.alive_players
        assert obs.dead_players == ["Charlie"]
        assert obs.last_eliminated == "Charlie"
        assert MafiaActionType.VOTE in obs.available_actions
        assert obs.role_info is None  # Citizens don't know roles

    def test_create_mafia_observation(self):
        """Test creating observation for mafia."""
        state = MafiaGameState(
            players=[
                MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Bob", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Charlie", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
            round_number=1,
        )

        obs = create_mafia_observation(state, "Bob")

        assert obs.player_name == "Bob"
        assert obs.role == MafiaRole.MAFIA
        assert obs.phase == MafiaRoundPhase.NIGHT
        assert MafiaActionType.KILL in obs.available_actions
        assert obs.role_info is not None
        assert obs.role_info.get("Charlie") == MafiaRole.MAFIA  # Mafia know each other
        assert "Alice" not in obs.role_info  # But not citizens

    def test_create_detective_observation(self):
        """Test creating observation for detective."""
        state = MafiaGameState(
            players=[
                MafiaPlayer(name="Alice", role=MafiaRole.DETECTIVE, is_alive=True),
                MafiaPlayer(name="Bob", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
            round_number=1,
        )

        obs = create_mafia_observation(state, "Alice")

        assert obs.role == MafiaRole.DETECTIVE
        assert MafiaActionType.INVESTIGATE in obs.available_actions
        assert MafiaActionType.PASS in obs.available_actions

    def test_create_dead_player_observation(self):
        """Test creating observation for dead player."""
        state = MafiaGameState(
            players=[
                MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN, is_alive=False),
                MafiaPlayer(name="Bob", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
            round_number=2,
            eliminated_players=["Alice"],
        )

        obs = create_mafia_observation(state, "Alice")

        assert obs.is_alive is False
        assert obs.available_actions == []  # Dead players can't act

    def test_game_over_observation(self):
        """Test creating observation for game over state."""
        state = MafiaGameState(
            players=[
                MafiaPlayer(name="Alice", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Bob", role=MafiaRole.CITIZEN, is_alive=False),
            ],
            phase=MafiaRoundPhase.GAME_OVER,
            game_over=True,
            winner="mafia",
        )

        obs = create_mafia_observation(state, "Alice")

        assert obs.game_over is True
        assert obs.winner == "mafia"
        assert obs.available_actions == []  # No actions in game over

    def test_invalid_player_name(self):
        """Test creating observation for non-existent player."""
        state = MafiaGameState(
            players=[MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN)]
        )

        with pytest.raises(ValueError):
            create_mafia_observation(state, "Bob")
