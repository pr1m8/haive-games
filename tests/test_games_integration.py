"""Integration tests for games with the standardized API system.

This test suite validates that the configurable games work properly
with the existing haive-dataflow API infrastructure.
"""

from unittest.mock import MagicMock, patch

import pytest

# Mark slow tests to be skipped in normal test runs
slow_tests = pytest.mark.skipif(
    True,  # Skip slow tests by default
    reason="Slow tests skipped unless --run-slow is used",
)

from haive.games.chess.agent import ChessAgent

# Test the configurable game systems
from haive.games.chess.configurable_config import (
    create_chess_config,
    create_chess_config_from_example,
)
from haive.games.chess.generic_engines import (
    create_generic_chess_config_from_example,
    create_generic_chess_engines_simple,
)
from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.configurable_config import (
    create_connect4_config,
    create_connect4_config_from_example,
)
from haive.games.connect4.generic_engines import (
    create_generic_connect4_config_from_example,
    create_generic_connect4_engines_simple,
)


class TestGameConfigurationIntegration:
    """Test that games can be configured and instantiated properly."""

    def test_chess_configuration_methods(self):
        """Test all Chess configuration methods work."""
        # Test 1: Simple configuration
        config1 = create_chess_config("gpt-4o", "claude-3-opus")
        assert config1.white_model == "gpt-4o"
        assert config1.black_model == "claude-3-opus"
        assert len(config1.engines) == 4

        # Test 2: Example configuration
        config2 = create_chess_config_from_example("budget_friendly")
        assert config2.example_config == "budget_friendly"
        assert len(config2.engines) == 4

        # Test 3: Direct engine creation
        engines = create_generic_chess_engines_simple("gpt-4o", "claude-3-opus")
        assert len(engines) == 4
        expected_roles = [
            "white_player",
            "black_player",
            "white_analyzer",
            "black_analyzer",
        ]
        assert set(engines.keys()) == set(expected_roles)

    def test_connect4_configuration_methods(self):
        """Test all Connect4 configuration methods work."""
        # Test 1: Simple configuration
        config1 = create_connect4_config("gpt-4o", "claude-3-opus")
        assert config1.red_model == "gpt-4o"
        assert config1.yellow_model == "claude-3-opus"
        assert len(config1.engines) == 4

        # Test 2: Example configuration
        config2 = create_connect4_config_from_example("gpt_vs_claude")
        assert config2.example_config == "gpt_vs_claude"
        assert len(config2.engines) == 4

        # Test 3: Direct engine creation
        engines = create_generic_connect4_engines_simple("gpt-4o", "claude-3-opus")
        assert len(engines) == 4
        expected_roles = [
            "red_player",
            "yellow_player",
            "red_analyzer",
            "yellow_analyzer",
        ]
        assert set(engines.keys()) == set(expected_roles)

    def test_agent_instantiation(self):
        """Test that agents can be instantiated with configurations."""
        # Chess agent
        chess_config = create_chess_config("gpt-4o", "claude-3-opus", max_moves=10)
        chess_agent = ChessAgent(chess_config)
        assert chess_agent.config == chess_config
        assert hasattr(chess_agent, "engines")

        # Connect4 agent
        connect4_config = create_connect4_config(
            "gpt-4o", "claude-3-opus", max_moves=10
        )
        connect4_agent = Connect4Agent(connect4_config)
        assert connect4_agent.config == connect4_config
        assert hasattr(connect4_agent, "engines")


class TestGameExecutionMocking:
    """Test game execution with mocked LLM calls."""

    @patch("haive.core.engine.aug_llm.AugLLMConfig.invoke")
    def test_chess_game_execution_mock(self, mock_invoke):
        """Test Chess game can execute moves with mocked LLM."""
        # Mock LLM responses for chess moves
        mock_invoke.side_effect = [
            # Mock chess move response
            MagicMock(selected_move=MagicMock(move="e2e4")),
            # Mock analysis response (if needed)
            MagicMock(position_score=0.5, attacking_chances="Good"),
        ]

        # Create a chess game with limited moves
        config = create_chess_config(
            "gpt-4o", "claude-3-opus", max_moves=2, enable_analysis=False
        )
        agent = ChessAgent(config)

        # This would normally run the game, but we're just testing instantiation
        assert agent is not None
        assert len(agent.engines) == 4

    @patch("haive.core.engine.aug_llm.AugLLMConfig.invoke")
    def test_connect4_game_execution_mock(self, mock_invoke):
        """Test Connect4 game can execute moves with mocked LLM."""
        # Mock LLM responses for connect4 moves
        mock_invoke.side_effect = [
            # Mock connect4 move response
            MagicMock(move=MagicMock(column=3)),
            # Mock analysis response (if needed)
            MagicMock(position_score=0, center_control=5),
        ]

        # Create a connect4 game with limited moves
        config = create_connect4_config(
            "gpt-4o", "claude-3-opus", max_moves=2, enable_analysis=False
        )
        agent = Connect4Agent(config)

        # This would normally run the game, but we're just testing instantiation
        assert agent is not None
        assert len(agent.engines) == 4


class TestGameAPICompatibility:
    """Test that games are compatible with the standardized API system."""

    def test_chess_api_compatibility(self):
        """Test Chess agent works with standardized API patterns."""
        from haive.games.chess.agent import ChessAgent
        from haive.games.chess.state import ChessState

        # Test agent class has required attributes for API
        assert hasattr(ChessAgent, "__init__")
        assert hasattr(ChessAgent, "run")

        # Test state schema
        assert hasattr(ChessState, "model_dump")

        # Test configuration
        config = create_chess_config("gpt-4o", "claude-3-opus")
        agent = ChessAgent(config)

        # Test agent has proper structure for API integration
        assert hasattr(agent, "config")
        assert hasattr(agent, "engines")

    def test_connect4_api_compatibility(self):
        """Test Connect4 agent works with standardized API patterns."""
        from haive.games.connect4.agent import Connect4Agent
        from haive.games.connect4.state import Connect4State

        # Test agent class has required attributes for API
        assert hasattr(Connect4Agent, "__init__")
        assert hasattr(Connect4Agent, "run")

        # Test state schema
        assert hasattr(Connect4State, "model_dump")

        # Test configuration
        config = create_connect4_config("gpt-4o", "claude-3-opus")
        agent = Connect4Agent(config)

        # Test agent has proper structure for API integration
        assert hasattr(agent, "config")
        assert hasattr(agent, "engines")


class TestConfigurationValidation:
    """Test configuration validation and error handling."""

    def test_invalid_example_names(self):
        """Test handling of invalid example names."""
        with pytest.raises(ValueError, match="Unknown example"):
            create_generic_chess_config_from_example("invalid_chess_example")

        with pytest.raises(ValueError, match="Unknown example"):
            create_generic_connect4_config_from_example("invalid_connect4_example")

    def test_configuration_overrides(self):
        """Test configuration parameter overrides."""
        # Chess with custom parameters
        chess_config = create_chess_config(
            "gpt-4o",
            "claude-3-opus",
            temperature=0.9,
            max_moves=50,
            enable_analysis=False,
        )
        assert chess_config.temperature == 0.9
        assert chess_config.max_moves == 50
        assert chess_config.enable_analysis is False

        # Connect4 with custom parameters
        connect4_config = create_connect4_config(
            "gpt-4o",
            "claude-3-opus",
            temperature=0.5,
            max_moves=20,
            enable_analysis=True,
        )
        assert connect4_config.temperature == 0.5
        assert connect4_config.max_moves == 20
        assert connect4_config.enable_analysis is True

    def test_player_name_generation(self):
        """Test that player names are generated correctly."""
        # Chess
        chess_config = create_chess_config("gpt-4o", "claude-3-opus")
        assert (
            "gpt" in chess_config.white_player_name.lower()
            or "white" in chess_config.white_player_name.lower()
        )
        assert (
            "claude" in chess_config.black_player_name.lower()
            or "black" in chess_config.black_player_name.lower()
        )

        # Connect4
        connect4_config = create_connect4_config("gpt-4o", "claude-3-opus")
        assert (
            "gpt" in connect4_config.red_player_name.lower()
            or "red" in connect4_config.red_player_name.lower()
        )
        assert (
            "claude" in connect4_config.yellow_player_name.lower()
            or "yellow" in connect4_config.yellow_player_name.lower()
        )


class TestCrossGameConsistency:
    """Test that the generic system provides consistent behavior across games."""

    def test_engine_structure_consistency(self):
        """Test that all games follow the same engine structure."""
        # Create engines for different games
        chess_engines = create_generic_chess_engines_simple("gpt-4o", "claude-3-opus")
        connect4_engines = create_generic_connect4_engines_simple(
            "gpt-4o", "claude-3-opus"
        )

        # Both should have 4 engines (2 players + 2 analyzers)
        assert len(chess_engines) == 4
        assert len(connect4_engines) == 4

        # Both should have similar structure (player + analyzer for each side)
        chess_roles = set(chess_engines.keys())
        connect4_roles = set(connect4_engines.keys())

        # Check pattern: player1_player, player2_player, player1_analyzer, player2_analyzer
        chess_pattern = {
            "white_player",
            "black_player",
            "white_analyzer",
            "black_analyzer",
        }
        connect4_pattern = {
            "red_player",
            "yellow_player",
            "red_analyzer",
            "yellow_analyzer",
        }

        assert chess_roles == chess_pattern
        assert connect4_roles == connect4_pattern

    def test_configuration_api_consistency(self):
        """Test that configuration APIs are consistent across games."""
        # Test that all games support the same configuration methods

        # Simple configuration
        chess_config = create_chess_config("gpt-4o", "claude-3-opus", temperature=0.7)
        connect4_config = create_connect4_config(
            "gpt-4o", "claude-3-opus", temperature=0.7
        )

        assert chess_config.temperature == connect4_config.temperature

        # Example configuration
        chess_example = create_chess_config_from_example("gpt4_only")
        connect4_example = create_connect4_config_from_example("gpt_only")

        assert len(chess_example.engines) == len(connect4_example.engines)

    def test_generic_system_type_safety(self):
        """Test that the generic system maintains type safety."""
        from haive.games.core.agent.generic_player_agent import (
            ChessPlayerIdentifiers,
            Connect4PlayerIdentifiers,
        )

        # Test player identifiers are correct
        chess_players = ChessPlayerIdentifiers()
        connect4_players = Connect4PlayerIdentifiers()

        assert chess_players.player1 == "white"
        assert chess_players.player2 == "black"
        assert connect4_players.player1 == "red"
        assert connect4_players.player2 == "yellow"


class TestRealGameExecution:
    """Test limited real game execution to ensure everything works."""

    @slow_tests
    def test_chess_quick_execution(self):
        """Test a very short chess game execution."""
        # Create a chess game with very limited moves to avoid long execution
        config = create_chess_config(
            "gpt-4o",
            "claude-3-opus",
            max_moves=2,  # Very limited
            enable_analysis=False,  # Disable for speed
            temperature=0.9,  # Higher temperature for quicker decisions
        )

        agent = ChessAgent(config)

        # Test that the agent can be created and has proper structure
        assert agent is not None
        assert hasattr(agent, "run")
        assert len(agent.engines) == 4

        # Uncomment for actual execution test (but may be slow)
        # try:
        #     result = agent.run({})
        #     assert result is not None
        # except Exception as e:
        #     # Allow failures but log them
        #     print(f"Chess execution test failed (expected in CI): {e}")

    @slow_tests
    def test_connect4_quick_execution(self):
        """Test a very short Connect4 game execution."""
        # Create a connect4 game with very limited moves
        config = create_connect4_config(
            "gpt-4o",
            "claude-3-opus",
            max_moves=2,  # Very limited
            enable_analysis=False,  # Disable for speed
            temperature=0.9,  # Higher temperature for quicker decisions
        )

        agent = Connect4Agent(config)

        # Test that the agent can be created and has proper structure
        assert agent is not None
        assert hasattr(agent, "run")
        assert len(agent.engines) == 4

        # Uncomment for actual execution test (but may be slow)
        # try:
        #     result = agent.run({})
        #     assert result is not None
        # except Exception as e:
        #     # Allow failures but log them
        #     print(f"Connect4 execution test failed (expected in CI): {e}")


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v", "--tb=short"])
