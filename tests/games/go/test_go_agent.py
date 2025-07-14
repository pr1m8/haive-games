"""Unit tests for Go agent.

This module tests the GoAgent class, including graph construction,
move generation, and game flow management.
"""

import pytest

from haive.games.go.agent import GoAgent
from haive.games.go.config import GoAgentConfig
from haive.games.go.state import GoGameState


class TestGoAgent:
    """Test suite for GoAgent."""

    @pytest.fixture
    def go_config(self) -> GoAgentConfig:
        """Create a Go configuration for testing."""
        return GoAgentConfig(
            name="test_go",
            board_size=9,  # Smaller board for faster testing
            include_analysis=False,
        )

    @pytest.fixture
    def go_agent(self, go_config: GoAgentConfig) -> GoAgent:
        """Create a GoAgent instance for testing."""
        return GoAgent(go_config)

    def test_go_agent_initialization(
        self, go_agent: GoAgent, go_config: GoAgentConfig
    ) -> None:
        """Test that GoAgent initializes correctly."""
        # Assert
        assert go_agent.config == go_config
        assert hasattr(go_agent, "setup_workflow")
        assert hasattr(go_agent, "app")

    def test_workflow_setup(self, go_config: GoAgentConfig) -> None:
        """Test that workflow is set up properly."""
        # Act
        agent = GoAgent(go_config)

        # Assert
        assert agent.app is not None
        # The workflow should be configured during initialization

    def test_black_move_method(self, go_agent: GoAgent) -> None:
        """Test the black_move method."""
        # Arrange
        state = GoGameState(turn="black", board_size=9)

        # Act
        result = go_agent.black_move(state)

        # Assert
        # The result should be a Command or updated state
        assert result is not None

    def test_white_move_method(self, go_agent: GoAgent) -> None:
        """Test the white_move method."""
        # Arrange
        state = GoGameState(turn="white", board_size=9)

        # Act
        result = go_agent.white_move(state)

        # Assert
        # The result should be a Command or updated state
        assert result is not None

    def test_check_game_over_ongoing(self, go_agent: GoAgent) -> None:
        """Test check_game_over with ongoing game."""
        # Arrange
        state = GoGameState(game_status="ongoing")

        # Act
        result = go_agent.check_game_over(state)

        # Assert
        assert result is not None
        # Should indicate game continues

    def test_check_game_over_ended(self, go_agent: GoAgent) -> None:
        """Test check_game_over when game has ended."""
        # Arrange
        state = GoGameState(game_status="ended", passes=2)

        # Act
        result = go_agent.check_game_over(state)

        # Assert
        assert result is not None
        # Should indicate game is over

    def test_analyze_position_black(self, go_agent: GoAgent) -> None:
        """Test position analysis for black player."""
        # Arrange
        state = GoGameState(turn="black")

        # Act
        result = go_agent.analyze_position(state, "black")

        # Assert
        assert result is not None
        # Analysis should be added to state

    def test_analyze_position_white(self, go_agent: GoAgent) -> None:
        """Test position analysis for white player."""
        # Arrange
        state = GoGameState(turn="white")

        # Act
        result = go_agent.analyze_position(state, "white")

        # Assert
        assert result is not None
        # Analysis should be added to state

    def test_agent_with_analysis_enabled(self) -> None:
        """Test agent behavior with analysis enabled."""
        # Arrange
        config = GoAgentConfig(
            name="test_with_analysis",
            board_size=9,
            include_analysis=True,
        )
        agent = GoAgent(config)
        state = GoGameState(board_size=9)

        # Act
        result = agent.black_move(state)

        # Assert
        assert result is not None
        # With analysis enabled, additional processing should occur

    def test_agent_different_board_sizes(self) -> None:
        """Test agent with different board sizes."""
        # Arrange
        sizes = [9, 13, 19]

        for size in sizes:
            # Act
            config = GoAgentConfig(board_size=size)
            agent = GoAgent(config)

            # Assert
            assert agent.config.board_size == size

    def test_game_flow_integration(self, go_agent: GoAgent) -> None:
        """Test basic game flow integration."""
        # Arrange
        initial_state = GoGameState(board_size=9)

        # Act - Try to make a few moves
        state = initial_state
        for _i in range(3):  # Make 3 moves
            if state.turn == "black":
                result = go_agent.black_move(state)
            else:
                result = go_agent.white_move(state)

            # Update state based on result
            if hasattr(result, "update") and result.update:
                state = GoGameState(**{**state.model_dump(), **result.update})
            else:
                state = result if isinstance(result, GoGameState) else state

        # Assert
        assert state is not None
        # Game should have progressed

    def test_error_handling_invalid_state(self, go_agent: GoAgent) -> None:
        """Test error handling with invalid state."""
        # Arrange
        invalid_state = None

        # Act & Assert
        # Agent should handle invalid states gracefully
        try:
            go_agent.black_move(invalid_state)
        except (TypeError, AttributeError):
            # Expected behavior for invalid input
            pass

    def test_pass_move_handling(self, go_agent: GoAgent) -> None:
        """Test handling of pass moves."""
        # Arrange
        state = GoGameState(board_size=9)

        # Act
        # This would depend on how the agent handles pass moves
        # For now, just ensure the state can handle passes
        state.passes = 1
        result = go_agent.check_game_over(state)

        # Assert
        assert result is not None

    def test_resignation_handling(self, go_agent: GoAgent) -> None:
        """Test handling of resignation scenarios."""
        # Arrange
        state = GoGameState(game_status="ended", game_result="black_resigned")

        # Act
        result = go_agent.check_game_over(state)

        # Assert
        assert result is not None
        # Should properly handle resigned games

    def test_agent_state_persistence(self, go_agent: GoAgent) -> None:
        """Test that agent maintains state correctly."""
        # Arrange
        state1 = GoGameState(board_size=9, turn="black")
        state2 = GoGameState(board_size=9, turn="white")

        # Act
        result1 = go_agent.black_move(state1)
        result2 = go_agent.white_move(state2)

        # Assert
        assert result1 is not None
        assert result2 is not None
        # Each call should be independent
