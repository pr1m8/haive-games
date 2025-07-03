"""Comprehensive tests for Connect4 generic agent system.

This test suite validates:
1. Generic engine creation and configuration
2. API functionality (sync and async)
3. End-to-end game execution
4. Error handling and edge cases
5. Configuration validation
"""

import asyncio
from unittest.mock import MagicMock, patch

import pytest

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.api import (
    Connect4API,
    Connect4GameResult,
    Connect4GameStatus,
    play_connect4_async,
    play_connect4_example,
    play_connect4_simple,
)
from haive.games.connect4.configurable_config import (
    ConfigurableConnect4Config,
    create_connect4_config,
    create_connect4_config_from_example,
    create_connect4_config_from_player_configs,
)
from haive.games.connect4.generic_engines import (
    Connect4PromptGenerator,
    connect4_players,
    create_generic_connect4_config_from_example,
    create_generic_connect4_engines,
    create_generic_connect4_engines_simple,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class TestConnect4GenericEngines:
    """Test Connect4 generic engine creation."""

    def test_create_generic_engines_simple(self):
        """Test creating engines with simple model strings."""
        engines = create_generic_connect4_engines_simple("gpt-4o", "claude-3-opus")

        # Check all expected engines are created
        expected_roles = [
            "red_player",
            "yellow_player",
            "red_analyzer",
            "yellow_analyzer",
        ]
        assert set(engines.keys()) == set(expected_roles)

        # Check engine properties
        for role, engine in engines.items():
            assert engine.name == role
            assert hasattr(engine, "llm_config")
            assert hasattr(engine, "prompt_template")
            assert hasattr(engine, "structured_output_model")

    def test_create_generic_engines_with_player_configs(self):
        """Test creating engines with detailed player configurations."""
        player_configs = {
            "red_player": PlayerAgentConfig(
                llm_config="gpt-4o", temperature=0.8, player_name="Red Master"
            ),
            "yellow_player": PlayerAgentConfig(
                llm_config="claude-3-opus", temperature=0.6, player_name="Yellow Pro"
            ),
            "red_analyzer": PlayerAgentConfig(
                llm_config="gemini-1.5-pro", temperature=0.3, player_name="Red Analyzer"
            ),
            "yellow_analyzer": PlayerAgentConfig(
                llm_config="llama-3.1-70b",
                temperature=0.3,
                player_name="Yellow Analyzer",
            ),
        }

        engines = create_generic_connect4_engines(player_configs)

        assert len(engines) == 4
        assert "red_player" in engines
        assert "yellow_player" in engines
        assert "red_analyzer" in engines
        assert "yellow_analyzer" in engines

    def test_create_engines_from_examples(self):
        """Test creating engines from example configurations."""
        examples = ["gpt_vs_claude", "gpt_only", "claude_only", "budget", "mixed"]

        for example_name in examples:
            engines = create_generic_connect4_config_from_example(example_name)
            assert len(engines) == 4
            assert all(
                role in engines
                for role in [
                    "red_player",
                    "yellow_player",
                    "red_analyzer",
                    "yellow_analyzer",
                ]
            )

    def test_prompt_generator(self):
        """Test Connect4 prompt generator."""
        generator = Connect4PromptGenerator(connect4_players)

        # Test move prompt creation
        red_prompt = generator.create_move_prompt("red")
        yellow_prompt = generator.create_move_prompt("yellow")

        assert red_prompt is not None
        assert yellow_prompt is not None

        # Test analysis prompt creation
        red_analysis = generator.create_analysis_prompt("red")
        yellow_analysis = generator.create_analysis_prompt("yellow")

        assert red_analysis is not None
        assert yellow_analysis is not None

        # Test output models
        move_model = generator.get_move_output_model()
        analysis_model = generator.get_analysis_output_model()

        assert move_model is not None
        assert analysis_model is not None


class TestConnect4ConfigurableConfig:
    """Test Connect4 configurable configuration."""

    def test_simple_model_configuration(self):
        """Test configuration with simple model strings."""
        config = create_connect4_config("gpt-4o", "claude-3-opus", temperature=0.8)

        assert config.red_model == "gpt-4o"
        assert config.yellow_model == "claude-3-opus"
        assert config.temperature == 0.8
        assert len(config.engines) == 4

    def test_example_configuration(self):
        """Test configuration from examples."""
        config = create_connect4_config_from_example("gpt_vs_claude")

        assert config.example_config == "gpt_vs_claude"
        assert len(config.engines) == 4
        assert (
            "gpt" in config.red_player_name.lower()
            or "claude" in config.red_player_name.lower()
        )

    def test_player_configs_configuration(self):
        """Test configuration with player configs."""
        player_configs = {
            "red_player": PlayerAgentConfig(
                llm_config="gpt-4o", player_name="Red Champion"
            ),
            "yellow_player": PlayerAgentConfig(
                llm_config="claude-3-opus", player_name="Yellow Expert"
            ),
            "red_analyzer": PlayerAgentConfig(
                llm_config="gpt-4o", player_name="Red Analyst"
            ),
            "yellow_analyzer": PlayerAgentConfig(
                llm_config="claude-3-opus", player_name="Yellow Analyst"
            ),
        }

        config = create_connect4_config_from_player_configs(player_configs)

        assert config.player_configs == player_configs
        assert config.red_player_name == "Red Champion"
        assert config.yellow_player_name == "Yellow Expert"
        assert len(config.engines) == 4

    def test_default_configuration(self):
        """Test default configuration when no options specified."""
        config = ConfigurableConnect4Config()

        assert len(config.engines) == 4
        assert config.red_player_name is not None
        assert config.yellow_player_name is not None


class TestConnect4API:
    """Test Connect4 API functionality."""

    @patch("haive.games.connect4.agent.Connect4Agent")
    def test_create_game_simple(self, mock_agent_class):
        """Test simple game creation via API."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        agent, game_id = Connect4API.create_game_simple("gpt-4o", "claude-3-opus")

        assert agent == mock_agent
        assert game_id.startswith("connect4_")
        mock_agent_class.assert_called_once()

    @patch("haive.games.connect4.agent.Connect4Agent")
    def test_create_game_from_example(self, mock_agent_class):
        """Test game creation from example via API."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        agent, game_id = Connect4API.create_game_from_example("budget")

        assert agent == mock_agent
        assert "budget" in game_id
        mock_agent_class.assert_called_once()

    @patch("haive.games.connect4.agent.Connect4Agent")
    def test_create_game_from_player_configs(self, mock_agent_class):
        """Test game creation from player configs via API."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        player_configs = {
            "red_player": PlayerAgentConfig(llm_config="gpt-4o"),
            "yellow_player": PlayerAgentConfig(llm_config="claude-3-opus"),
            "red_analyzer": PlayerAgentConfig(llm_config="gpt-4o"),
            "yellow_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
        }

        agent, game_id = Connect4API.create_game_from_player_configs(player_configs)

        assert agent == mock_agent
        assert "custom" in game_id
        mock_agent_class.assert_called_once()

    def test_run_game_success(self):
        """Test successful game execution."""
        # Mock agent with successful game result
        mock_agent = MagicMock()
        mock_agent.config.red_player_name = "Red Player"
        mock_agent.config.yellow_player_name = "Yellow Player"
        mock_agent.run.return_value = {
            "game_status": "game_over",
            "winner": "red",
            "move_history": [("red", 3), ("yellow", 2), ("red", 4)],
            "board_string": "mock_board",
        }

        result = Connect4API.run_game(mock_agent, "test_game_123")

        assert isinstance(result, Connect4GameResult)
        assert result.game_id == "test_game_123"
        assert result.status == Connect4GameStatus.RED_WIN
        assert result.winner == "red"
        assert result.total_moves == 3
        assert result.red_player == "Red Player"
        assert result.yellow_player == "Yellow Player"
        assert result.error_message is None

    def test_run_game_draw(self):
        """Test game ending in draw."""
        mock_agent = MagicMock()
        mock_agent.config.red_player_name = "Red Player"
        mock_agent.config.yellow_player_name = "Yellow Player"
        mock_agent.run.return_value = {
            "game_status": "draw",
            "winner": None,
            "move_history": [("red", i) for i in range(21)]
            + [("yellow", i) for i in range(21)],
        }

        result = Connect4API.run_game(mock_agent, "draw_game")

        assert result.status == Connect4GameStatus.DRAW
        assert result.winner is None
        assert result.total_moves == 42

    def test_run_game_error(self):
        """Test game execution with error."""
        mock_agent = MagicMock()
        mock_agent.config.red_player_name = "Red Player"
        mock_agent.config.yellow_player_name = "Yellow Player"
        mock_agent.run.side_effect = Exception("Game execution failed")

        result = Connect4API.run_game(mock_agent, "error_game")

        assert result.status == Connect4GameStatus.ERROR
        assert result.error_message == "Game execution failed"
        assert result.total_moves == 0

    def test_run_game_no_result(self):
        """Test game execution returning no result."""
        mock_agent = MagicMock()
        mock_agent.config.red_player_name = "Red Player"
        mock_agent.config.yellow_player_name = "Yellow Player"
        mock_agent.run.return_value = None

        result = Connect4API.run_game(mock_agent, "no_result_game")

        assert result.status == Connect4GameStatus.ERROR
        assert result.error_message == "Game returned no result"

    @pytest.mark.asyncio
    async def test_run_game_async(self):
        """Test asynchronous game execution."""
        mock_agent = MagicMock()
        mock_agent.config.red_player_name = "Red Player"
        mock_agent.config.yellow_player_name = "Yellow Player"
        mock_agent.run.return_value = {
            "game_status": "game_over",
            "winner": "yellow",
            "move_history": [("red", 3), ("yellow", 2)],
        }

        result = await Connect4API.run_game_async(mock_agent, "async_game")

        assert isinstance(result, Connect4GameResult)
        assert result.status == Connect4GameStatus.YELLOW_WIN
        assert result.winner == "yellow"


class TestConnect4ConvenienceFunctions:
    """Test Connect4 convenience functions."""

    @patch("haive.games.connect4.api.Connect4API.create_game_simple")
    @patch("haive.games.connect4.api.Connect4API.run_game")
    def test_play_connect4_simple(self, mock_run_game, mock_create_game):
        """Test simple Connect4 play function."""
        mock_agent = MagicMock()
        mock_create_game.return_value = (mock_agent, "test_game")
        mock_result = Connect4GameResult(
            game_id="test_game",
            status=Connect4GameStatus.RED_WIN,
            winner="red",
            total_moves=10,
            move_history=[],
            duration_seconds=30.0,
            red_player="Red",
            yellow_player="Yellow",
        )
        mock_run_game.return_value = mock_result

        result = play_connect4_simple("gpt-4o", "claude-3-opus", temperature=0.8)

        mock_create_game.assert_called_once_with(
            "gpt-4o", "claude-3-opus", temperature=0.8
        )
        mock_run_game.assert_called_once_with(mock_agent, "test_game")
        assert result == mock_result

    @patch("haive.games.connect4.api.Connect4API.create_game_from_example")
    @patch("haive.games.connect4.api.Connect4API.run_game")
    def test_play_connect4_example(self, mock_run_game, mock_create_game):
        """Test example Connect4 play function."""
        mock_agent = MagicMock()
        mock_create_game.return_value = (mock_agent, "example_game")
        mock_result = Connect4GameResult(
            game_id="example_game",
            status=Connect4GameStatus.DRAW,
            winner=None,
            total_moves=42,
            move_history=[],
            duration_seconds=60.0,
            red_player="Red",
            yellow_player="Yellow",
        )
        mock_run_game.return_value = mock_result

        result = play_connect4_example("budget", enable_analysis=True)

        mock_create_game.assert_called_once_with("budget", enable_analysis=True)
        mock_run_game.assert_called_once_with(mock_agent, "example_game")
        assert result == mock_result

    @pytest.mark.asyncio
    @patch("haive.games.connect4.api.Connect4API.create_game_simple")
    @patch("haive.games.connect4.api.Connect4API.run_game_async")
    async def test_play_connect4_async(self, mock_run_game_async, mock_create_game):
        """Test async Connect4 play function."""
        mock_agent = MagicMock()
        mock_create_game.return_value = (mock_agent, "async_game")
        mock_result = Connect4GameResult(
            game_id="async_game",
            status=Connect4GameStatus.YELLOW_WIN,
            winner="yellow",
            total_moves=15,
            move_history=[],
            duration_seconds=45.0,
            red_player="Red",
            yellow_player="Yellow",
        )
        mock_run_game_async.return_value = mock_result

        result = await play_connect4_async("gpt-4o", "claude-3-opus")

        mock_create_game.assert_called_once_with("gpt-4o", "claude-3-opus")
        mock_run_game_async.assert_called_once_with(mock_agent, "async_game")
        assert result == mock_result


class TestConnect4ErrorHandling:
    """Test Connect4 error handling and edge cases."""

    def test_invalid_example_name(self):
        """Test handling of invalid example names."""
        with pytest.raises(ValueError, match="Unknown example"):
            create_generic_connect4_config_from_example("invalid_example")

    def test_missing_player_config(self):
        """Test handling of missing player configurations."""
        incomplete_configs = {
            "red_player": PlayerAgentConfig(llm_config="gpt-4o"),
            # Missing other roles
        }

        with pytest.raises(ValueError, match="No player config provided"):
            create_generic_connect4_engines(incomplete_configs)

    def test_configuration_validation(self):
        """Test configuration validation."""
        # Test with invalid max_moves
        config = ConfigurableConnect4Config(max_moves=-1)
        assert config.max_moves == -1  # Should accept but may cause issues

        # Test with valid configuration
        config = ConfigurableConnect4Config(
            red_model="gpt-4o",
            yellow_model="claude-3-opus",
            max_moves=42,
            enable_analysis=True,
        )
        assert config.max_moves == 42
        assert config.enable_analysis is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
