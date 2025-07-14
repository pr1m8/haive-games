"""Unit tests for Go state manager.

This module tests the GoGameStateManager class, including move application,
game state updates, and Go-specific rules.
"""

import pytest

from haive.games.go.models import GoMove
from haive.games.go.state import GoGameState
from haive.games.go.state_manager import GoGameStateManager


class TestGoGameStateManager:
    """Test suite for GoGameStateManager."""

    @pytest.fixture
    def state_manager(self) -> GoGameStateManager:
        """Create a GoGameStateManager instance for testing."""
        return GoGameStateManager()

    @pytest.fixture
    def initial_state(self) -> GoGameState:
        """Create an initial Go state."""
        return GoGameState()

    def test_state_manager_initialization(
        self, state_manager: GoGameStateManager
    ) -> None:
        """Test that state manager initializes correctly."""
        # Assert
        assert isinstance(state_manager, GoGameStateManager)
        assert hasattr(state_manager, "apply_move")
        assert hasattr(state_manager, "initialize")

    def test_initialize_creates_default_state(
        self, state_manager: GoGameStateManager
    ) -> None:
        """Test that initialize creates a proper default state."""
        # Act
        state = state_manager.initialize()

        # Assert
        assert isinstance(state, GoGameState)
        assert state.board_size == 19
        assert state.turn == "black"
        assert state.game_status == "ongoing"
        assert state.move_history == []

    def test_initialize_with_custom_board_size(
        self, state_manager: GoGameStateManager
    ) -> None:
        """Test initialization with custom board size."""
        # Act
        state = state_manager.initialize(board_size=13)

        # Assert
        assert state.board_size == 13

    def test_apply_move_basic_placement(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test basic move application."""
        # Arrange
        move = GoMove(move=(3, 3), player="black", board_size=19)

        # Act
        new_state = state_manager.apply_move(initial_state, move)

        # Assert
        assert new_state != initial_state
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0] == ("black", (3, 3))
        assert new_state.turn == "white"  # Turn should switch

    def test_apply_move_alternating_turns(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test that turns alternate correctly."""
        # Arrange
        black_move = GoMove(move=(3, 3), player="black", board_size=19)
        white_move = GoMove(move=(15, 15), player="white", board_size=19)

        # Act
        state = state_manager.apply_move(initial_state, black_move)
        assert state.turn == "white"

        state = state_manager.apply_move(state, white_move)
        assert state.turn == "black"

        # Assert
        assert len(state.move_history) == 2
        assert state.move_history[0] == ("black", (3, 3))
        assert state.move_history[1] == ("white", (15, 15))

    def test_apply_move_updates_sgf(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test that SGF representation is updated with moves."""
        # Arrange
        move = GoMove(move=(3, 3), player="black", board_size=19)

        # Act
        new_state = state_manager.apply_move(initial_state, move)

        # Assert
        assert new_state.board_sgf != initial_state.board_sgf
        # SGF should contain the move information
        assert new_state.board_sgf is not None

    def test_apply_move_invalid_coordinates(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test handling of invalid move coordinates."""
        # Arrange
        with pytest.raises(ValueError):
            invalid_move = GoMove(move=(-1, 0), player="black", board_size=19)
            state_manager.apply_move(initial_state, invalid_move)

    def test_apply_move_occupied_position(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test handling of moves to occupied positions."""
        # Arrange
        move1 = GoMove(move=(3, 3), player="black", board_size=19)
        move2 = GoMove(move=(3, 3), player="white", board_size=19)

        # Act
        state = state_manager.apply_move(initial_state, move1)

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            state_manager.apply_move(state, move2)
        assert "occupied" in str(exc_info.value).lower()

    def test_apply_pass_move(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test applying a pass move."""
        # Act
        new_state = state_manager.apply_pass(initial_state)

        # Assert
        assert new_state.passes == 1
        assert new_state.turn == "white"  # Turn should switch
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0] == ("black", "pass")

    def test_two_consecutive_passes_end_game(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test that two consecutive passes end the game."""
        # Act
        state = state_manager.apply_pass(initial_state)  # Black passes
        state = state_manager.apply_pass(state)  # White passes

        # Assert
        assert state.passes == 2
        assert state.game_status == "ended"
        assert state.game_result is not None

    def test_capture_mechanics(self, state_manager: GoGameStateManager) -> None:
        """Test stone capture mechanics."""
        # Arrange - Set up a capture scenario
        GoGameState()
        # This would require setting up a specific board position
        # For now, we test that the method exists and handles captures

        # Act & Assert
        # Note: Full capture testing would require a more complex setup
        assert hasattr(state_manager, "check_captures")

    def test_game_ending_scenarios(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test various game ending scenarios."""
        # Test resignation
        resigned_state = state_manager.apply_resignation(initial_state, "black")
        assert resigned_state.game_status == "ended"
        assert resigned_state.game_result == "white_wins"

        # Test timeout (if implemented)
        if hasattr(state_manager, "apply_timeout"):
            timeout_state = state_manager.apply_timeout(initial_state, "white")
            assert timeout_state.game_status == "ended"

    def test_territory_calculation(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test territory calculation for game scoring."""
        # Act & Assert
        if hasattr(state_manager, "calculate_territory"):
            territory = state_manager.calculate_territory(initial_state)
            assert isinstance(territory, dict)
            assert "black" in territory
            assert "white" in territory

    def test_state_consistency_after_moves(
        self, state_manager: GoGameStateManager, initial_state: GoGameState
    ) -> None:
        """Test that state remains consistent after multiple moves."""
        # Arrange
        moves = [
            GoMove(move=(3, 3), player="black", board_size=19),
            GoMove(move=(15, 15), player="white", board_size=19),
            GoMove(move=(3, 15), player="black", board_size=19),
            GoMove(move=(15, 3), player="white", board_size=19),
        ]

        # Act
        state = initial_state
        for move in moves:
            state = state_manager.apply_move(state, move)

        # Assert
        assert len(state.move_history) == 4
        assert state.turn == "black"  # Should be black's turn after 4 moves
        assert state.game_status == "ongoing"
        assert state.passes == 0  # No passes made
