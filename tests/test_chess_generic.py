"""Comprehensive tests for Chess generic agent system.

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

from haive.games.chess.agent import ChessAgent
from haive.games.chess.api import (
    ChessAPI,
    ChessGameResult,
    ChessGameStatus,
    play_chess_async,
    play_chess_example,
    play_chess_simple,
)
from haive.games.chess.configurable_config import (
    ConfigurableChessConfig,
    create_chess_config,
    create_chess_config_from_example,
    create_chess_config_from_player_configs,
)
from haive.games.chess.generic_engines import (
    ChessPromptGenerator,
    chess_players,
    create_generic_chess_config_from_example,
    create_generic_chess_engines,
    create_generic_chess_engines_simple,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class TestChessGenericEngines:
    """Test Chess generic engine creation."""

    def test_create_generic_engines_simple(self):
        """Test creating engines with simple model strings."""
        engines = create_generic_chess_engines_simple("gpt-4o", "claude-3-opus")

        # Check all expected engines are created
        expected_roles = [
            "white_player",
            "black_player",
            "white_analyzer",
            "black_analyzer",
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
            "white_player": PlayerAgentConfig(
                llm_config="gpt-4o", temperature=0.8, player_name="Grandmaster White"
            ),
            "black_player": PlayerAgentConfig(
                llm_config="claude-3-opus",
                temperature=0.6,
                player_name="Strategic Black",
            ),
            "white_analyzer": PlayerAgentConfig(
                llm_config="gemini-1.5-pro",
                temperature=0.3,
                player_name="White Analyst",
            ),
            "black_analyzer": PlayerAgentConfig(
                llm_config="llama-3.1-70b", temperature=0.3, player_name="Black Analyst"
            ),
        }

        engines = create_generic_chess_engines(player_configs)

        assert len(engines) == 4
        assert "white_player" in engines
        assert "black_player" in engines
        assert "white_analyzer" in engines
        assert "black_analyzer" in engines

    def test_create_engines_from_examples(self):
        """Test creating engines from example configurations."""
        examples = [
            "anthropic_vs_openai",
            "gpt4_only",
            "claude_only",
            "mixed_providers",
            "budget_friendly",
        ]

        for example_name in examples:
            engines = create_generic_chess_config_from_example(example_name)
            assert len(engines) == 4
            assert all(
                role in engines
                for role in [
                    "white_player",
                    "black_player",
                    "white_analyzer",
                    "black_analyzer",
                ]
            )

    def test_prompt_generator(self):
        """Test Chess prompt generator."""
        generator = ChessPromptGenerator(chess_players)

        # Test move prompt creation
        white_prompt = generator.create_move_prompt("white")
        black_prompt = generator.create_move_prompt("black")

        assert white_prompt is not None
        assert black_prompt is not None

        # Test analysis prompt creation
        white_analysis = generator.create_analysis_prompt("white")
        black_analysis = generator.create_analysis_prompt("black")

        assert white_analysis is not None
        assert black_analysis is not None

        # Test output models
        move_model = generator.get_move_output_model()
        analysis_model = generator.get_analysis_output_model()

        assert move_model is not None
        assert analysis_model is not None


class TestChessConfigurableConfig:
    """Test Chess configurable configuration."""

    def test_simple_model_configuration(self):
        """Test configuration with simple model strings."""
        config = create_chess_config("gpt-4o", "claude-3-opus", temperature=0.8)

        assert config.white_model == "gpt-4o"
        assert config.black_model == "claude-3-opus"
        assert config.temperature == 0.8
        assert len(config.engines) == 4

    def test_example_configuration(self):
        """Test configuration from examples."""
        config = create_chess_config_from_example("anthropic_vs_openai")

        assert config.example_config == "anthropic_vs_openai"
        assert len(config.engines) == 4
        assert (
            "claude" in config.white_player_name.lower()
            or "gpt" in config.white_player_name.lower()
        )

    def test_player_configs_configuration(self):
        """Test configuration with player configs."""
        player_configs = {
            "white_player": PlayerAgentConfig(
                llm_config="gpt-4o", player_name="Deep Blue 2024"
            ),
            "black_player": PlayerAgentConfig(
                llm_config="claude-3-opus", player_name="AlphaZero Claude"
            ),
            "white_analyzer": PlayerAgentConfig(
                llm_config="gpt-4o", player_name="White Analyst"
            ),
            "black_analyzer": PlayerAgentConfig(
                llm_config="claude-3-opus", player_name="Black Analyst"
            ),
        }

        config = create_chess_config_from_player_configs(player_configs)

        assert config.player_configs == player_configs
        assert config.white_player_name == "Deep Blue 2024"
        assert config.black_player_name == "AlphaZero Claude"
        assert len(config.engines) == 4

    def test_default_configuration(self):
        """Test default configuration when no options specified."""
        config = ConfigurableChessConfig()

        assert len(config.engines) == 4
        assert config.white_player_name is not None
        assert config.black_player_name is not None


class TestChessAPI:
    """Test Chess API functionality."""

    @patch("haive.games.chess.agent.ChessAgent")
    def test_create_game_simple(self, mock_agent_class):
        """Test simple game creation via API."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        agent, game_id = ChessAPI.create_game_simple("gpt-4o", "claude-3-opus")

        assert agent == mock_agent
        assert game_id.startswith("chess_")
        mock_agent_class.assert_called_once()

    @patch("haive.games.chess.agent.ChessAgent")
    def test_create_game_from_example(self, mock_agent_class):
        """Test game creation from example via API."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        agent, game_id = ChessAPI.create_game_from_example("budget_friendly")

        assert agent == mock_agent
        assert "budget_friendly" in game_id
        mock_agent_class.assert_called_once()

    @patch("haive.games.chess.agent.ChessAgent")
    def test_create_game_from_player_configs(self, mock_agent_class):
        """Test game creation from player configs via API."""
        mock_agent = MagicMock()
        mock_agent_class.return_value = mock_agent

        player_configs = {
            "white_player": PlayerAgentConfig(llm_config="gpt-4o"),
            "black_player": PlayerAgentConfig(llm_config="claude-3-opus"),
            "white_analyzer": PlayerAgentConfig(llm_config="gpt-4o"),
            "black_analyzer": PlayerAgentConfig(llm_config="claude-3-opus"),
        }

        agent, game_id = ChessAPI.create_game_from_player_configs(player_configs)

        assert agent == mock_agent
        assert "custom" in game_id
        mock_agent_class.assert_called_once()

    def test_run_game_success(self):
        """Test successful game execution."""
        # Mock agent with successful game result
        mock_agent = MagicMock()
        mock_agent.config.white_player_name = "White Player"
        mock_agent.config.black_player_name = "Black Player"
        mock_agent.run.return_value = {
            "game_status": "checkmate",
            "game_result": "white_win",
            "move_history": [("white", "e2e4"), ("black", "e7e5"), ("white", "Qh5")],
            "board_fens": ["start_fen", "fen_after_e4", "fen_after_e5", "final_fen"],
            "current_player": "black",
        }

        result = ChessAPI.run_game(mock_agent, "test_game_123")

        assert isinstance(result, ChessGameResult)
        assert result.game_id == "test_game_123"
        assert result.status == ChessGameStatus.WHITE_WIN
        assert result.winner == "white"
        assert result.total_moves == 3
        assert result.white_player == "White Player"
        assert result.black_player == "Black Player"
        assert result.error_message is None

    def test_run_game_draw(self):
        """Test game ending in draw."""
        mock_agent = MagicMock()
        mock_agent.config.white_player_name = "White Player"
        mock_agent.config.black_player_name = "Black Player"
        mock_agent.run.return_value = {
            "game_status": "draw",
            "game_result": "draw",
            "move_history": [("white", "e2e4"), ("black", "e7e5")] * 50,  # 100 moves
            "board_fens": ["fen1", "fen2"],
        }

        result = ChessAPI.run_game(mock_agent, "draw_game")

        assert result.status == ChessGameStatus.DRAW
        assert result.winner is None
        assert result.total_moves == 100

    def test_run_game_stalemate(self):
        """Test game ending in stalemate."""
        mock_agent = MagicMock()
        mock_agent.config.white_player_name = "White Player"
        mock_agent.config.black_player_name = "Black Player"
        mock_agent.run.return_value = {
            "game_status": "stalemate",
            "move_history": [("white", "e2e4"), ("black", "e7e5")],
            "board_fens": ["start", "final"],
        }

        result = ChessAPI.run_game(mock_agent, "stalemate_game")

        assert result.status == ChessGameStatus.STALEMATE
        assert result.winner is None

    def test_run_game_error(self):
        """Test game execution with error."""
        mock_agent = MagicMock()
        mock_agent.config.white_player_name = "White Player"
        mock_agent.config.black_player_name = "Black Player"
        mock_agent.run.side_effect = Exception("Chess game execution failed")

        result = ChessAPI.run_game(mock_agent, "error_game")

        assert result.status == ChessGameStatus.ERROR
        assert result.error_message == "Chess game execution failed"
        assert result.total_moves == 0

    def test_run_game_no_result(self):
        """Test game execution returning no result."""
        mock_agent = MagicMock()
        mock_agent.config.white_player_name = "White Player"
        mock_agent.config.black_player_name = "Black Player"
        mock_agent.run.return_value = None

        result = ChessAPI.run_game(mock_agent, "no_result_game")

        assert result.status == ChessGameStatus.ERROR
        assert result.error_message == "Game returned no result"

    @pytest.mark.asyncio
    async def test_run_game_async(self):
        """Test asynchronous game execution."""
        mock_agent = MagicMock()
        mock_agent.config.white_player_name = "White Player"
        mock_agent.config.black_player_name = "Black Player"
        mock_agent.run.return_value = {
            "game_status": "checkmate",
            "game_result": "black_win",
            "move_history": [("white", "e2e4"), ("black", "Nc6")],
            "board_fens": ["start", "final"],
            "current_player": "white",
        }

        result = await ChessAPI.run_game_async(mock_agent, "async_game")

        assert isinstance(result, ChessGameResult)
        assert result.status == ChessGameStatus.BLACK_WIN
        assert result.winner == "black"


class TestChessConvenienceFunctions:
    """Test Chess convenience functions."""

    @patch("haive.games.chess.api.ChessAPI.create_game_simple")
    @patch("haive.games.chess.api.ChessAPI.run_game")
    def test_play_chess_simple(self, mock_run_game, mock_create_game):
        """Test simple Chess play function."""
        mock_agent = MagicMock()
        mock_create_game.return_value = (mock_agent, "test_game")
        mock_result = ChessGameResult(
            game_id="test_game",
            status=ChessGameStatus.WHITE_WIN,
            winner="white",
            total_moves=25,
            move_history=[],
            duration_seconds=120.0,
            white_player="White",
            black_player="Black",
        )
        mock_run_game.return_value = mock_result

        result = play_chess_simple("gpt-4o", "claude-3-opus", temperature=0.8)

        mock_create_game.assert_called_once_with(
            "gpt-4o", "claude-3-opus", temperature=0.8
        )
        mock_run_game.assert_called_once_with(mock_agent, "test_game")
        assert result == mock_result

    @patch("haive.games.chess.api.ChessAPI.create_game_from_example")
    @patch("haive.games.chess.api.ChessAPI.run_game")
    def test_play_chess_example(self, mock_run_game, mock_create_game):
        """Test example Chess play function."""
        mock_agent = MagicMock()
        mock_create_game.return_value = (mock_agent, "example_game")
        mock_result = ChessGameResult(
            game_id="example_game",
            status=ChessGameStatus.DRAW,
            winner=None,
            total_moves=100,
            move_history=[],
            duration_seconds=300.0,
            white_player="White",
            black_player="Black",
        )
        mock_run_game.return_value = mock_result

        result = play_chess_example("budget_friendly", enable_analysis=False)

        mock_create_game.assert_called_once_with(
            "budget_friendly", enable_analysis=False
        )
        mock_run_game.assert_called_once_with(mock_agent, "example_game")
        assert result == mock_result

    @pytest.mark.asyncio
    @patch("haive.games.chess.api.ChessAPI.create_game_simple")
    @patch("haive.games.chess.api.ChessAPI.run_game_async")
    async def test_play_chess_async(self, mock_run_game_async, mock_create_game):
        """Test async Chess play function."""
        mock_agent = MagicMock()
        mock_create_game.return_value = (mock_agent, "async_game")
        mock_result = ChessGameResult(
            game_id="async_game",
            status=ChessGameStatus.BLACK_WIN,
            winner="black",
            total_moves=40,
            move_history=[],
            duration_seconds=180.0,
            white_player="White",
            black_player="Black",
        )
        mock_run_game_async.return_value = mock_result

        result = await play_chess_async("gpt-4o", "claude-3-opus")

        mock_create_game.assert_called_once_with("gpt-4o", "claude-3-opus")
        mock_run_game_async.assert_called_once_with(mock_agent, "async_game")
        assert result == mock_result


class TestChessErrorHandling:
    """Test Chess error handling and edge cases."""

    def test_invalid_example_name(self):
        """Test handling of invalid example names."""
        with pytest.raises(ValueError, match="Unknown example"):
            create_generic_chess_config_from_example("invalid_example")

    def test_missing_player_config(self):
        """Test handling of missing player configurations."""
        incomplete_configs = {
            "white_player": PlayerAgentConfig(llm_config="gpt-4o"),
            # Missing other roles
        }

        with pytest.raises(ValueError, match="No player config provided"):
            create_generic_chess_engines(incomplete_configs)

    def test_configuration_validation(self):
        """Test configuration validation."""
        # Test with invalid max_moves
        config = ConfigurableChessConfig(max_moves=-1)
        assert config.max_moves == -1  # Should accept but may cause issues

        # Test with valid configuration
        config = ConfigurableChessConfig(
            white_model="gpt-4o",
            black_model="claude-3-opus",
            max_moves=100,
            enable_analysis=True,
        )
        assert config.max_moves == 100
        assert config.enable_analysis is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
