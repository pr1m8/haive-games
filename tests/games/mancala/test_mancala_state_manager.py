"""Unit tests for mancala state manager.

This module tests the MancalaStateManager class, including move application,
game state updates, and special game rules like free turns.
"""

import pytest

from haive.games.mancala.models import MancalaMove
from haive.games.mancala.state import MancalaState
from haive.games.mancala.state_manager import MancalaStateManager


class TestMancalaStateManager:
    """Test suite for MancalaStateManager."""

    @pytest.fixture
    def state_manager(self) -> MancalaStateManager:
        """Create a MancalaStateManager instance for testing."""
        return MancalaStateManager()

    @pytest.fixture
    def initial_state(self) -> MancalaState:
        """Create an initial mancala state."""
        return MancalaState()

    def test_state_manager_initialization(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test that state manager initializes correctly."""
        # Assert
        assert isinstance(state_manager, MancalaStateManager)
        assert hasattr(state_manager, "apply_move")
        assert hasattr(state_manager, "initialize")

    def test_initialize_creates_default_state(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test that initialize creates a proper default state."""
        # Act
        state = state_manager.initialize()

        # Assert
        assert isinstance(state, MancalaState)
        assert state.board == [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        assert state.turn == "player1"
        assert state.game_status == "ongoing"

    def test_initialize_with_custom_stones(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test initialization with custom number of stones."""
        # Act
        state = state_manager.initialize(stones_per_pit=6)

        # Assert
        assert state.board == [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]

    def test_apply_move_basic_sowing(
        self, state_manager: MancalaStateManager, initial_state: MancalaState
    ) -> None:
        """Test basic move application and sowing mechanics."""
        # Arrange
        move = MancalaMove(pit_index=2, player="player1")

        # Act
        new_state = state_manager.apply_move(initial_state, move)

        # Assert
        # Pit 2 should be empty, next 4 pits should have 5 stones each
        assert new_state.board[2] == 0
        assert new_state.board[3] == 5
        assert new_state.board[4] == 5
        assert new_state.board[5] == 5
        assert new_state.board[6] == 1  # Player 1's store
        assert new_state.turn == "player2"

    def test_apply_move_free_turn_when_ending_in_store(
        self, state_manager: MancalaStateManager, initial_state: MancalaState
    ) -> None:
        """Test that landing in own store grants a free turn."""
        # Arrange
        move = MancalaMove(pit_index=2, player="player1")

        # Act
        new_state = state_manager.apply_move(initial_state, move)

        # Assert
        assert new_state.free_turn is True
        assert new_state.turn == "player1"  # Same player continues

    def test_apply_move_capture_opponent_stones(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test capturing opponent's stones when landing in empty pit."""
        # Arrange
        state = MancalaState()
        # Set up board for capture scenario
        state.board = [1, 0, 0, 0, 0, 0, 10, 4, 4, 4, 4, 4, 4, 10]
        move = MancalaMove(pit_index=0, player="player1")

        # Act
        new_state = state_manager.apply_move(state, move)

        # Assert
        # Should capture from pit 11 (opposite of pit 1)
        assert new_state.board[1] == 0  # Capturing pit becomes empty
        assert new_state.board[11] == 0  # Opponent pit becomes empty
        assert new_state.board[6] == 15  # Store gets original + captured

    def test_apply_move_skip_opponent_store(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test that sowing skips opponent's store."""
        # Arrange
        state = MancalaState()
        state.board = [4, 4, 4, 4, 4, 10, 0, 4, 4, 4, 4, 4, 4, 0]
        move = MancalaMove(pit_index=5, player="player1")

        # Act
        new_state = state_manager.apply_move(state, move)

        # Assert
        # Should skip index 13 (player 2's store)
        assert new_state.board[13] == 0  # Player 2's store unchanged
        assert new_state.board[0] == 5  # Wrapped around to player 1's side

    def test_apply_move_updates_move_history(
        self, state_manager: MancalaStateManager, initial_state: MancalaState
    ) -> None:
        """Test that moves are added to history."""
        # Arrange
        move = MancalaMove(pit_index=1, player="player1")

        # Act
        new_state = state_manager.apply_move(initial_state, move)

        # Assert
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0] == move

    def test_apply_move_invalid_pit_empty(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test that moving from empty pit raises error."""
        # Arrange
        state = MancalaState()
        state.board[0] = 0  # Empty pit
        move = MancalaMove(pit_index=0, player="player1")

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            state_manager.apply_move(state, move)
        assert "empty" in str(exc_info.value).lower()

    def test_apply_move_wrong_player_pit(
        self, state_manager: MancalaStateManager, initial_state: MancalaState
    ) -> None:
        """Test that player can't move from opponent's pit."""
        # Arrange
        move = MancalaMove(pit_index=0, player="player2")

        # Act & Assert
        # This should work as pit_index is normalized (0-5 for both players)
        new_state = state_manager.apply_move(initial_state, move)
        assert new_state.board[7] == 0  # Player 2's first pit is emptied

    def test_game_ending_moves_remaining_stones(
        self, state_manager: MancalaStateManager
    ) -> None:
        """Test that remaining stones are collected when game ends."""
        # Arrange
        state = MancalaState()
        # Player 1 has only one stone left
        state.board = [1, 0, 0, 0, 0, 0, 20, 4, 4, 4, 4, 4, 4, 10]
        move = MancalaMove(pit_index=0, player="player1")

        # Act
        new_state = state_manager.apply_move(state, move)

        # Assert
        assert new_state.game_status == "ended"
        assert new_state.winner is not None
        # All stones should be in stores
        assert all(new_state.board[i] == 0 for i in range(6))
        assert all(new_state.board[i] == 0 for i in range(7, 13))

    def test_consecutive_free_turns(self, state_manager: MancalaStateManager) -> None:
        """Test multiple free turns in sequence."""
        # Arrange
        state = MancalaState()
        state.board = [1, 2, 3, 4, 5, 6, 0, 4, 4, 4, 4, 4, 4, 0]

        # Act - First move ends in store
        move1 = MancalaMove(pit_index=3, player="player1")
        state = state_manager.apply_move(state, move1)
        assert state.free_turn is True
        assert state.turn == "player1"

        # Second move also ends in store
        move2 = MancalaMove(pit_index=0, player="player1")
        state = state_manager.apply_move(state, move2)
        assert state.free_turn is True
        assert state.turn == "player1"

        # Third move doesn't end in store
        move3 = MancalaMove(pit_index=1, player="player1")
        state = state_manager.apply_move(state, move3)
        assert state.free_turn is False
        assert state.turn == "player2"
