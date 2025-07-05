"""Unit tests for mancala game state.

This module tests the MancalaState class, including board representation,
move history tracking, and game state management.
"""

import pytest

from haive.games.mancala.models import MancalaMove
from haive.games.mancala.state import MancalaState


class TestMancalaState:
    """Test suite for MancalaState."""

    @pytest.fixture
    def initial_state(self) -> MancalaState:
        """Create an initial mancala state for testing."""
        return MancalaState()

    @pytest.fixture
    def midgame_state(self) -> MancalaState:
        """Create a mancala state in the middle of a game."""
        state = MancalaState()
        state.board = [3, 0, 2, 1, 0, 1, 8, 4, 5, 0, 2, 1, 0, 6]
        state.turn = "player2"
        state.move_history = [
            MancalaMove(pit_index=2, player="player1"),
            MancalaMove(pit_index=3, player="player2"),
            MancalaMove(pit_index=0, player="player1"),
        ]
        return state

    def test_initial_state_has_correct_defaults(
        self, initial_state: MancalaState
    ) -> None:
        """Test that initial state has correct default values."""
        # Assert board setup
        expected_board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        assert initial_state.board == expected_board

        # Assert game state
        assert initial_state.turn == "player1"
        assert initial_state.game_status == "ongoing"
        assert initial_state.move_history == []
        assert initial_state.free_turn is False
        assert initial_state.winner is None

        # Assert analysis lists
        assert initial_state.player1_analysis == []
        assert initial_state.player2_analysis == []

    def test_board_validation_rejects_wrong_size(self) -> None:
        """Test that board must have exactly 14 positions."""
        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            MancalaState(board=[1, 2, 3])
        assert "14 positions" in str(exc_info.value)

    def test_display_board_formatting(self, initial_state: MancalaState) -> None:
        """Test the board display format."""
        # Act
        display = initial_state.display_board()

        # Assert
        assert "Player 2" in display
        assert "Player 1" in display
        # Check that all initial stones are displayed as "4"
        assert display.count(" 4") == 12  # 6 pits per player
        assert display.count(" 0") == 2  # 2 stores

    def test_get_valid_moves_player1(self, initial_state: MancalaState) -> None:
        """Test getting valid moves for player1."""
        # Act
        valid_moves = initial_state.get_valid_moves("player1")

        # Assert
        assert valid_moves == [0, 1, 2, 3, 4, 5]

    def test_get_valid_moves_player2(self, initial_state: MancalaState) -> None:
        """Test getting valid moves for player2."""
        # Act
        valid_moves = initial_state.get_valid_moves("player2")

        # Assert - indices are normalized to 0-5 range
        assert valid_moves == [0, 1, 2, 3, 4, 5]

    def test_get_valid_moves_with_empty_pits(self, midgame_state: MancalaState) -> None:
        """Test getting valid moves when some pits are empty."""
        # Act
        p1_moves = midgame_state.get_valid_moves("player1")
        p2_moves = midgame_state.get_valid_moves("player2")

        # Assert
        # Player 1's board: [3, 0, 2, 1, 0, 1] - indices 1 and 4 are empty
        assert p1_moves == [0, 2, 3, 5]
        # Player 2's board: [4, 5, 0, 2, 1, 0] - indices 2 and 5 are empty
        assert p2_moves == [0, 1, 3, 4]

    def test_is_game_over_false_initially(self, initial_state: MancalaState) -> None:
        """Test that game is not over in initial state."""
        # Act & Assert
        assert initial_state.is_game_over() is False

    def test_is_game_over_true_when_side_empty(self) -> None:
        """Test that game is over when one side has no stones."""
        # Arrange - Player 1 has no stones
        state = MancalaState()
        state.board = [0, 0, 0, 0, 0, 0, 24, 4, 4, 4, 4, 4, 4, 0]

        # Act & Assert
        assert state.is_game_over() is True

    def test_get_scores(self, midgame_state: MancalaState) -> None:
        """Test getting current scores."""
        # Act
        scores = midgame_state.get_scores()

        # Assert
        assert scores["player1"] == 8  # Store at index 6
        assert scores["player2"] == 6  # Store at index 13

    def test_determine_winner_player1_wins(self) -> None:
        """Test determining winner when player1 has more stones."""
        # Arrange
        state = MancalaState()
        state.board = [0, 0, 0, 0, 0, 0, 30, 0, 0, 0, 0, 0, 0, 18]

        # Act
        winner = state.determine_winner()

        # Assert
        assert winner == "player1"

    def test_determine_winner_player2_wins(self) -> None:
        """Test determining winner when player2 has more stones."""
        # Arrange
        state = MancalaState()
        state.board = [0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 28]

        # Act
        winner = state.determine_winner()

        # Assert
        assert winner == "player2"

    def test_determine_winner_draw(self) -> None:
        """Test determining winner when scores are tied."""
        # Arrange
        state = MancalaState()
        state.board = [0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 24]

        # Act
        winner = state.determine_winner()

        # Assert
        assert winner == "draw"

    def test_state_serialization(self, midgame_state: MancalaState) -> None:
        """Test that state can be serialized and deserialized."""
        # Act
        state_dict = midgame_state.model_dump()
        restored_state = MancalaState(**state_dict)

        # Assert
        assert restored_state.board == midgame_state.board
        assert restored_state.turn == midgame_state.turn
        assert restored_state.game_status == midgame_state.game_status
        assert len(restored_state.move_history) == len(midgame_state.move_history)

    def test_initialization_with_custom_stones(self) -> None:
        """Test state initialization with custom number of stones."""
        # Arrange
        init_data = {"initialize": {"stones_per_pit": 6}}

        # Act
        state = MancalaState(**init_data)

        # Assert
        expected_board = [6, 6, 6, 6, 6, 6, 0, 6, 6, 6, 6, 6, 6, 0]
        assert state.board == expected_board
