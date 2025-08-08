"""Test suite for Mafia game state."""

# Standard library imports

# Third-party imports

# Local imports
from haive.games.mafia.models import (
    MafiaAction,
    MafiaActionType,
    MafiaGameState,
    MafiaPlayer,
    MafiaRole,
    MafiaRoundPhase,
    MafiaVote,
)
from haive.games.mafia.state import MafiaState


class TestMafiaState:
    """Test the MafiaState class."""

    def test_init_empty_state(self):
        """Test initializing an empty state."""
        state = MafiaState()

        assert isinstance(state.game_state, MafiaGameState)
        assert state.game_state.players == []
        assert state.game_state.round_number == 0
        assert state.game_state.phase == MafiaRoundPhase.NIGHT
        assert state.game_state.game_over is False

    def test_init_with_game_state(self):
        """Test initializing with existing game state."""
        players = [
            MafiaPlayer(name="Alice", role=MafiaRole.CITIZEN),
            MafiaPlayer(name="Bob", role=MafiaRole.MAFIA),
        ]
        game_state = MafiaGameState(
            players=players, round_number=3, phase=MafiaRoundPhase.DAY_DISCUSSION
        )

        state = MafiaState(game_state=game_state)

        assert state.game_state == game_state
        assert len(state.game_state.players) == 2
        assert state.game_state.round_number == 3
        assert state.game_state.phase == MafiaRoundPhase.DAY_DISCUSSION

    def test_state_properties(self):
        """Test state properties."""
        players = [
            MafiaPlayer(name="A", role=MafiaRole.CITIZEN, is_alive=True),
            MafiaPlayer(name="B", role=MafiaRole.MAFIA, is_alive=True),
            MafiaPlayer(name="C", role=MafiaRole.CITIZEN, is_alive=False),
            MafiaPlayer(name="D", role=MafiaRole.DETECTIVE, is_alive=True),
        ]
        game_state = MafiaGameState(
            players=players,
            phase=MafiaRoundPhase.NIGHT,
            round_number=2,
            eliminated_players=["C"],
            last_eliminated="C",
            game_over=False,
        )

        state = MafiaState(game_state=game_state)

        # Test properties forwarding
        assert state.players == players
        assert state.phase == MafiaRoundPhase.NIGHT
        assert state.round_number == 2
        assert len(state.alive_players) == 3
        assert state.mafia_count == 1
        assert state.citizen_count == 2
        assert state.game_over is False
        assert state.winner is None

    def test_dict_conversion(self):
        """Test conversion to/from dict."""
        players = [
            MafiaPlayer(name="Player1", role=MafiaRole.MAFIA),
            MafiaPlayer(name="Player2", role=MafiaRole.CITIZEN),
        ]
        game_state = MafiaGameState(
            players=players, round_number=5, phase=MafiaRoundPhase.DAY_VOTING
        )

        state = MafiaState(game_state=game_state)

        # Convert to dict
        state_dict = state.to_dict()

        assert "game_state" in state_dict
        assert state_dict["game_state"]["round_number"] == 5
        assert state_dict["game_state"]["phase"] == "day_voting"
        assert len(state_dict["game_state"]["players"]) == 2

        # Convert from dict
        new_state = MafiaState.from_dict(state_dict)

        assert new_state.round_number == 5
        assert new_state.phase == MafiaRoundPhase.DAY_VOTING
        assert len(new_state.players) == 2
        assert new_state.players[0].name == "Player1"
        assert new_state.players[0].role == MafiaRole.MAFIA

    def test_copy_state(self):
        """Test copying state."""
        game_state = MafiaGameState(
            players=[MafiaPlayer(name="Test", role=MafiaRole.DOCTOR)],
            round_number=3,
            actions=[
                MafiaAction(
                    player_name="Test", action_type=MafiaActionType.HEAL, target="Other"
                )
            ],
        )

        state = MafiaState(game_state=game_state)

        # Create copy
        state_copy = state.copy()

        # Verify copy
        assert state_copy is not state
        assert state_copy.game_state is not state.game_state
        assert state_copy.round_number == state.round_number
        assert len(state_copy.players) == len(state.players)
        assert len(state_copy.game_state.actions) == 1

        # Modify copy and verify original unchanged
        state_copy.game_state.round_number = 10
        assert state.round_number == 3

    def test_get_valid_actions(self):
        """Test getting valid actions for players."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia1", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Detective", role=MafiaRole.DETECTIVE, is_alive=True),
                MafiaPlayer(name="Citizen", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Dead", role=MafiaRole.CITIZEN, is_alive=False),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        state = MafiaState(game_state=game_state)

        # Test mafia actions at night
        mafia_actions = state.get_valid_actions("Mafia1")
        assert MafiaActionType.KILL in mafia_actions
        assert MafiaActionType.PASS in mafia_actions

        # Test detective actions at night
        detective_actions = state.get_valid_actions("Detective")
        assert MafiaActionType.INVESTIGATE in detective_actions
        assert MafiaActionType.PASS in detective_actions

        # Test citizen actions at night
        citizen_actions = state.get_valid_actions("Citizen")
        assert citizen_actions == []  # Citizens sleep at night

        # Test dead player actions
        dead_actions = state.get_valid_actions("Dead")
        assert dead_actions == []  # Dead players can't act

    def test_get_valid_actions_day_phase(self):
        """Test getting valid actions during day phases."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Player1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Player2", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
        )

        state = MafiaState(game_state=game_state)

        # All alive players can vote during day voting
        p1_actions = state.get_valid_actions("Player1")
        assert MafiaActionType.VOTE in p1_actions

        p2_actions = state.get_valid_actions("Player2")
        assert MafiaActionType.VOTE in p2_actions

    def test_is_valid_action(self):
        """Test action validation."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Citizen", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Detective", role=MafiaRole.DETECTIVE, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        state = MafiaState(game_state=game_state)

        # Valid mafia kill at night
        kill_action = MafiaAction(
            player_name="Mafia", action_type=MafiaActionType.KILL, target="Citizen"
        )
        assert state.is_valid_action(kill_action) is True

        # Invalid - citizen can't kill
        invalid_kill = MafiaAction(
            player_name="Citizen", action_type=MafiaActionType.KILL, target="Mafia"
        )
        assert state.is_valid_action(invalid_kill) is False

        # Invalid - can't kill self
        self_kill = MafiaAction(
            player_name="Mafia", action_type=MafiaActionType.KILL, target="Mafia"
        )
        assert state.is_valid_action(self_kill) is False

        # Valid detective investigate
        investigate = MafiaAction(
            player_name="Detective",
            action_type=MafiaActionType.INVESTIGATE,
            target="Mafia",
        )
        assert state.is_valid_action(investigate) is True

    def test_apply_action_kill(self):
        """Test applying kill action."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Victim", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        state = MafiaState(game_state=game_state)

        kill_action = MafiaAction(
            player_name="Mafia", action_type=MafiaActionType.KILL, target="Victim"
        )

        # Apply action
        new_state = state.apply_action(kill_action)

        # Verify action was recorded
        assert len(new_state.game_state.actions) == 1
        assert new_state.game_state.actions[0] == kill_action

        # Victim should still be alive (kill happens at phase transition)
        victim = next(p for p in new_state.players if p.name == "Victim")
        assert victim.is_alive is True

    def test_apply_action_vote(self):
        """Test applying vote action."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Voter", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Target", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
        )

        state = MafiaState(game_state=game_state)

        vote_action = MafiaAction(
            player_name="Voter", action_type=MafiaActionType.VOTE, target="Target"
        )

        # Apply action
        new_state = state.apply_action(vote_action)

        # Verify vote was recorded
        assert len(new_state.game_state.votes) == 1
        assert new_state.game_state.votes[0].voter == "Voter"
        assert new_state.game_state.votes[0].target == "Target"

    def test_transition_night_to_day(self):
        """Test phase transition from night to day."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Victim", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Other", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
            actions=[
                MafiaAction(
                    player_name="Mafia",
                    action_type=MafiaActionType.KILL,
                    target="Victim",
                )
            ],
        )

        state = MafiaState(game_state=game_state)

        # Transition to day
        new_state = state.transition_phase()

        # Verify phase changed
        assert new_state.phase == MafiaRoundPhase.DAY_DISCUSSION

        # Verify victim was killed
        victim = next(p for p in new_state.players if p.name == "Victim")
        assert victim.is_alive is False
        assert "Victim" in new_state.game_state.eliminated_players
        assert new_state.game_state.last_eliminated == "Victim"

        # Actions should be cleared
        assert new_state.game_state.actions == []

    def test_transition_voting_to_night(self):
        """Test phase transition from voting to night."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Player1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Player2", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Player3", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
            round_number=1,
            votes=[
                MafiaVote(voter="Player1", target="Player2"),
                MafiaVote(voter="Player3", target="Player2"),
            ],
        )

        state = MafiaState(game_state=game_state)

        # Transition to night
        new_state = state.transition_phase()

        # Verify phase changed and round incremented
        assert new_state.phase == MafiaRoundPhase.NIGHT
        assert new_state.round_number == 2

        # Verify player was eliminated by vote
        player2 = next(p for p in new_state.players if p.name == "Player2")
        assert player2.is_alive is False
        assert "Player2" in new_state.game_state.eliminated_players

        # Votes should be cleared
        assert new_state.game_state.votes == []

    def test_check_game_over_mafia_wins(self):
        """Test game over when mafia wins."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Citizen", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_DISCUSSION,
        )

        state = MafiaState(game_state=game_state)

        # Check game over condition
        is_over, winner = state._check_game_over()

        assert is_over is True
        assert winner == "mafia"

    def test_check_game_over_citizens_win(self):
        """Test game over when citizens win."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Citizen1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Detective", role=MafiaRole.DETECTIVE, is_alive=True),
                MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=False),
            ],
            phase=MafiaRoundPhase.DAY_DISCUSSION,
        )

        state = MafiaState(game_state=game_state)

        # Check game over condition
        is_over, winner = state._check_game_over()

        assert is_over is True
        assert winner == "citizens"

    def test_check_game_over_not_over(self):
        """Test game not over condition."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Citizen1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Citizen2", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        state = MafiaState(game_state=game_state)

        # Check game over condition
        is_over, winner = state._check_game_over()

        assert is_over is False
        assert winner is None

    def test_serialization_compatibility(self):
        """Test that state serialization is compatible with game state."""
        original_state = MafiaState()
        original_state.game_state.players = [
            MafiaPlayer(name="Test", role=MafiaRole.DOCTOR)
        ]
        original_state.game_state.round_number = 7

        # Serialize and deserialize
        state_dict = original_state.to_dict()
        restored_state = MafiaState.from_dict(state_dict)

        # Verify restoration
        assert len(restored_state.players) == 1
        assert restored_state.players[0].name == "Test"
        assert restored_state.players[0].role == MafiaRole.DOCTOR
        assert restored_state.round_number == 7

    def test_edge_case_empty_votes(self):
        """Test handling of empty votes (no elimination)."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Player1", role=MafiaRole.CITIZEN, is_alive=True),
                MafiaPlayer(name="Player2", role=MafiaRole.MAFIA, is_alive=True),
            ],
            phase=MafiaRoundPhase.DAY_VOTING,
            votes=[],  # No votes cast
        )

        state = MafiaState(game_state=game_state)

        # Transition with no votes
        new_state = state.transition_phase()

        # No one should be eliminated
        assert all(p.is_alive for p in new_state.players)
        assert new_state.game_state.last_eliminated is None
        assert new_state.phase == MafiaRoundPhase.NIGHT

    def test_multiple_actions_same_phase(self):
        """Test handling multiple actions in the same phase."""
        game_state = MafiaGameState(
            players=[
                MafiaPlayer(name="Mafia1", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Mafia2", role=MafiaRole.MAFIA, is_alive=True),
                MafiaPlayer(name="Victim", role=MafiaRole.CITIZEN, is_alive=True),
            ],
            phase=MafiaRoundPhase.NIGHT,
        )

        state = MafiaState(game_state=game_state)

        # Apply multiple kill actions (should take the last one)
        action1 = MafiaAction(
            player_name="Mafia1", action_type=MafiaActionType.KILL, target="Victim"
        )
        action2 = MafiaAction(
            player_name="Mafia2", action_type=MafiaActionType.KILL, target="Victim"
        )

        state = state.apply_action(action1)
        state = state.apply_action(action2)

        # Both actions should be recorded
        assert len(state.game_state.actions) == 2
