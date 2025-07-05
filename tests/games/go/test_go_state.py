"""Unit tests for Go game state.

This module tests the GoGameState class, including board representation,
move history tracking, and game state management.
"""

import pytest

from haive.games.go.state import GoGameState


class TestGoGameState:
    """Test suite for GoGameState."""

    @pytest.fixture
    def initial_state(self) -> GoGameState:
        """Create an initial Go state for testing."""
        return GoGameState()

    @pytest.fixture
    def midgame_state(self) -> GoGameState:
        """Create a Go state in the middle of a game."""
        # This would typically contain an SGF representation of a game in progress
        # For testing, we'll use a simple state
        state = GoGameState()
        state.move_history = [
            ("black", (3, 3)),
            ("white", (15, 15)),
            ("black", (3, 15)),
            ("white", (15, 3)),
        ]
        state.turn = "black"
        state.passes = 0
        return state

    def test_initial_state_has_correct_defaults(
        self, initial_state: GoGameState
    ) -> None:
        """Test that initial state has correct default values."""
        # Assert
        assert initial_state.board_size == 19
        assert initial_state.turn == "black"
        assert initial_state.game_status == "ongoing"
        assert initial_state.move_history == []
        assert initial_state.captured_stones == {"black": 0, "white": 0}
        assert initial_state.passes == 0
        assert initial_state.game_result is None
        assert initial_state.black_analysis == []
        assert initial_state.white_analysis == []

    def test_board_sgf_validation(self) -> None:
        """Test board_sgf field validation."""
        # Arrange & Act
        state = GoGameState(board_sgf="(;GM[1]FF[4]CA[UTF-8]SZ[19];B[dd];W[pd])")

        # Assert
        assert state.board_sgf is not None
        assert "GM[1]" in state.board_sgf  # Go game format

    def test_turn_validation_accepts_valid_players(self) -> None:
        """Test that turn validation accepts valid players."""
        # Arrange & Act
        black_state = GoGameState(turn="black")
        white_state = GoGameState(turn="white")

        # Assert
        assert black_state.turn == "black"
        assert white_state.turn == "white"

    def test_turn_validation_rejects_invalid_players(self) -> None:
        """Test that turn validation rejects invalid players."""
        # Act & Assert
        with pytest.raises(ValueError):
            GoGameState(turn="red")

    def test_game_status_values(self) -> None:
        """Test valid game status values."""
        # Arrange & Act
        ongoing_state = GoGameState(game_status="ongoing")
        ended_state = GoGameState(game_status="ended")

        # Assert
        assert ongoing_state.game_status == "ongoing"
        assert ended_state.game_status == "ended"

    def test_move_history_tracking(self, midgame_state: GoGameState) -> None:
        """Test move history is properly tracked."""
        # Assert
        assert len(midgame_state.move_history) == 4
        assert midgame_state.move_history[0] == ("black", (3, 3))
        assert midgame_state.move_history[-1] == ("white", (15, 3))

        # Check alternating colors
        for i, (color, _) in enumerate(midgame_state.move_history):
            expected_color = "black" if i % 2 == 0 else "white"
            assert color == expected_color

    def test_captured_stones_tracking(self) -> None:
        """Test captured stones are tracked correctly."""
        # Arrange
        state = GoGameState()
        state.captured_stones = {"black": 3, "white": 5}

        # Assert
        assert state.captured_stones["black"] == 3
        assert state.captured_stones["white"] == 5

    def test_pass_counting(self) -> None:
        """Test that consecutive passes are counted."""
        # Arrange
        state = GoGameState()
        state.passes = 2

        # Assert
        assert state.passes == 2

    def test_board_size_validation(self) -> None:
        """Test board size validation."""
        # Act & Assert
        valid_sizes = [9, 13, 19]
        for size in valid_sizes:
            state = GoGameState(board_size=size)
            assert state.board_size == size

    def test_analysis_lists_empty_by_default(self, initial_state: GoGameState) -> None:
        """Test that analysis lists start empty."""
        # Assert
        assert initial_state.black_analysis == []
        assert initial_state.white_analysis == []

    def test_game_result_initially_none(self, initial_state: GoGameState) -> None:
        """Test that game result is initially None."""
        # Assert
        assert initial_state.game_result is None

    def test_state_serialization(self, midgame_state: GoGameState) -> None:
        """Test that state can be serialized and deserialized."""
        # Act
        state_dict = midgame_state.model_dump()
        restored_state = GoGameState(**state_dict)

        # Assert
        assert restored_state.board_size == midgame_state.board_size
        assert restored_state.turn == midgame_state.turn
        assert restored_state.game_status == midgame_state.game_status
        assert restored_state.move_history == midgame_state.move_history
        assert restored_state.captured_stones == midgame_state.captured_stones

    def test_complex_game_state(self) -> None:
        """Test a complex game state with multiple elements."""
        # Arrange & Act
        state = GoGameState(
            board_size=13,
            turn="white",
            game_status="ongoing",
            move_history=[
                ("black", (6, 6)),
                ("white", (3, 3)),
                ("black", (9, 9)),
            ],
            captured_stones={"black": 0, "white": 2},
            passes=0,
        )

        # Assert
        assert state.board_size == 13
        assert state.turn == "white"
        assert len(state.move_history) == 3
        assert state.captured_stones["white"] == 2
