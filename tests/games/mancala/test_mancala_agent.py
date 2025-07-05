"""Unit tests for mancala agent.

This module tests the MancalaAgent class, including graph construction,
move generation, and game flow management.
"""

import pytest

from haive.games.mancala.agent import MancalaAgent
from haive.games.mancala.config import MancalaConfig
from haive.games.mancala.engines import RandomMancalaEngine
from haive.games.mancala.state import MancalaState


class TestMancalaAgent:
    """Test suite for MancalaAgent."""

    @pytest.fixture
    def random_engine(self) -> RandomMancalaEngine:
        """Create a random mancala engine for testing."""
        return RandomMancalaEngine()

    @pytest.fixture
    def mancala_config(self, random_engine: RandomMancalaEngine) -> MancalaConfig:
        """Create a mancala configuration for testing."""
        return MancalaConfig(
            name="test_mancala",
            player1="AI",
            player2="AI",
            enable_analysis=False,
            stones_per_pit=4,
            engines={"player1": random_engine, "player2": random_engine},
        )

    @pytest.fixture
    def mancala_agent(self, mancala_config: MancalaConfig) -> MancalaAgent:
        """Create a MancalaAgent instance for testing."""
        return MancalaAgent(mancala_config)

    def test_mancala_agent_initialization(
        self, mancala_agent: MancalaAgent, mancala_config: MancalaConfig
    ) -> None:
        """Test that MancalaAgent initializes correctly."""
        # Assert
        assert mancala_agent.config == mancala_config
        assert mancala_agent.graph_builder is not None
        assert mancala_agent._app is not None
        assert hasattr(mancala_agent, "state_manager")
        assert hasattr(mancala_agent, "make_move")

    def test_graph_construction(self, mancala_config: MancalaConfig) -> None:
        """Test that game graph is constructed properly."""
        # Act
        agent = MancalaAgent(mancala_config)

        # Assert
        nodes = list(agent.graph_builder.nodes)
        assert "check_game_over" in nodes
        assert "player_turn" in nodes
        assert "player1_turn" in nodes
        assert "player2_turn" in nodes
        assert "after_move" in nodes

    def test_check_game_over_ongoing(self, mancala_agent: MancalaAgent) -> None:
        """Test check_game_over with ongoing game."""
        # Arrange
        state = MancalaState()

        # Act
        result = mancala_agent.check_game_over(state)

        # Assert
        assert result.game_status == "ongoing"
        assert result.winner is None

    def test_check_game_over_ended(self, mancala_agent: MancalaAgent) -> None:
        """Test check_game_over when game should end."""
        # Arrange
        state = MancalaState()
        # All player1 pits empty
        state.board = [0, 0, 0, 0, 0, 0, 20, 4, 4, 4, 4, 4, 4, 8]

        # Act
        result = mancala_agent.check_game_over(state)

        # Assert
        assert result.game_status == "ended"
        assert result.winner is not None

    def test_make_move_generates_valid_move(self, mancala_agent: MancalaAgent) -> None:
        """Test that make_move generates a valid move."""
        # Arrange
        state = MancalaState()

        # Act
        result = mancala_agent.make_move(state, "player1")

        # Assert
        assert result != state  # State was modified
        assert len(result.move_history) == 1
        assert result.move_history[0].player == "player1"
        assert 0 <= result.move_history[0].pit_index < 6

    def test_make_move_handles_no_valid_moves(
        self, mancala_agent: MancalaAgent
    ) -> None:
        """Test make_move when player has no valid moves."""
        # Arrange
        state = MancalaState()
        # All player1 pits empty
        state.board = [0, 0, 0, 0, 0, 0, 20, 4, 4, 4, 4, 4, 4, 8]

        # Act
        result = mancala_agent.make_move(state, "player1")

        # Assert
        assert result == state  # State unchanged
        assert len(result.move_history) == 0

    def test_player1_turn_method(self, mancala_agent: MancalaAgent) -> None:
        """Test player1_turn method delegates correctly."""
        # Arrange
        state = MancalaState()

        # Act
        result = mancala_agent.player1_turn(state)

        # Assert
        assert len(result.move_history) == 1
        assert result.move_history[0].player == "player1"

    def test_player2_turn_method(self, mancala_agent: MancalaAgent) -> None:
        """Test player2_turn method delegates correctly."""
        # Arrange
        state = MancalaState()
        state.turn = "player2"

        # Act
        result = mancala_agent.player2_turn(state)

        # Assert
        assert len(result.move_history) == 1
        assert result.move_history[0].player == "player2"

    def test_full_game_flow(self, mancala_agent: MancalaAgent) -> None:
        """Test playing several moves in sequence."""
        # Arrange
        state = MancalaState()
        moves_played = 0

        # Act - Play up to 20 moves or until game ends
        for i in range(20):
            if state.game_status == "ended":
                break

            player = "player1" if i % 2 == 0 else "player2"
            old_history_len = len(state.move_history)
            state = mancala_agent.make_move(state, player)

            # Check if a move was made
            if len(state.move_history) > old_history_len:
                moves_played += 1

            # Handle free turns
            if state.free_turn:
                # Same player goes again
                state = mancala_agent.make_move(state, player)
                if len(state.move_history) > old_history_len + 1:
                    moves_played += 1

        # Assert
        assert moves_played > 0
        assert len(state.move_history) == moves_played
        if state.game_status == "ended":
            assert state.winner is not None

    def test_fallback_graph_construction(self, mancala_config: MancalaConfig) -> None:
        """Test fallback graph when main construction fails."""
        # Arrange
        agent = MancalaAgent(mancala_config)

        # Force use of simple graph
        agent.graph_builder = agent._create_simple_graph()
        agent._app = agent.graph_builder.build()

        # Act
        nodes = list(agent.graph_builder.nodes)

        # Assert
        assert "play" in nodes
        assert len(nodes) == 1  # Simple graph has only one node

    def test_simple_play_method(self, mancala_agent: MancalaAgent) -> None:
        """Test the simple_play fallback method."""
        # Arrange
        state = MancalaState()

        # Act
        result = mancala_agent.simple_play(state)

        # Assert
        assert len(result.move_history) >= 1
        if result.game_status != "ended":
            assert result.turn in ["player1", "player2"]

    def test_agent_with_analysis_enabled(
        self, random_engine: RandomMancalaEngine
    ) -> None:
        """Test agent behavior with analysis enabled."""
        # Arrange
        config = MancalaConfig(
            name="test_with_analysis",
            player1="AI",
            player2="AI",
            enable_analysis=True,
            engines={"player1": random_engine, "player2": random_engine},
        )
        agent = MancalaAgent(config)
        state = MancalaState()

        # Act
        result = agent.make_move(state, "player1")

        # Assert
        # With RandomEngine, analysis won't be added, but move should work
        assert len(result.move_history) == 1
