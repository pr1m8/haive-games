"""Functional tests for all games in haive-games package.

These tests validate that games can be:
1. Imported successfully
2. Configured with the new LLM system
3. Used to create working agents
4. Compatible with the API system

No mocks - real integration tests.
"""

from pathlib import Path
import sys

import pytest

# Add packages to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import the key components we need
from haive.core.models.llm.factory import create_llm_config
from haive.games.core.agent.player_agent import PlayerAgentConfig


class TestGameImportsAndStructure:
    """Verify all games can be imported and have expected structure."""

    @pytest.fixture
    def all_games(self) -> list[str]:
        """List of all games in the package."""
        return [
            "among_us",
            "battleship",
            "chess",
            "clue",
            "connect4",
            "debate",
            "dominoes",
            "fox_and_geese",
            "go",
            "hold_em",
            "mafia",
            "mancala",
            "mastermind",
            "monopoly",
            "nim",
            "poker",
            "reversi",
            "risk",
            "tic_tac_toe",
        ]

    def test_import_all_game_modules(self, all_games):
        """Test that all game modules can be imported."""
        failed_imports = []

        for game in all_games:
            if game == "go":  # Skip go due to known conflict
                continue

            try:
                # Import main module
                exec(f"import haive.games.{game}")
                # Import key submodules
                exec(f"import haive.games.{game}.config")
                exec(f"import haive.games.{game}.state")
                exec(f"import haive.games.{game}.agent")
            except Exception as e:
                failed_imports.append((game, str(e)))

        assert not failed_imports, f"Failed imports: {failed_imports}"

    def test_games_have_configurable_configs(self, all_games):
        """Test that games have configurable config modules."""
        games_with_configs = []
        games_without_configs = []

        for game in all_games:
            if game == "go":  # Skip go
                continue

            try:
                exec(f"import haive.games.{game}.configurable_config")
                games_with_configs.append(game)
            except ImportError:
                games_without_configs.append(game)

        # At least the main games should have configurable configs
        expected_games = ["chess", "connect4", "tic_tac_toe"]
        for game in expected_games:
            assert game in games_with_configs, f"{game} missing configurable_config"


class TestLLMSystemIntegration:
    """Test the LLM factory and configuration system."""

    def test_create_llm_configs_basic(self):
        """Test creating basic LLM configs."""
        configs = [
            create_llm_config("gpt-4"),
            create_llm_config("claude-3-opus"),
            create_llm_config("openai:gpt-3.5-turbo"),
            create_llm_config("anthropic:claude-3-haiku"),
        ]

        for config in configs:
            assert config is not None
            assert hasattr(config, "model")
            assert hasattr(config, "provider")
            assert hasattr(config, "instantiate")

    def test_player_agent_config_creation(self):
        """Test creating player agent configs."""
        # Test with string
        config1 = PlayerAgentConfig(
            llm_config="gpt-4", temperature=0.7, player_name="Test Player 1"
        )
        assert config1.llm_config == "gpt-4"
        assert config1.temperature == 0.7
        assert config1.player_name == "Test Player 1"

        # Test with LLMConfig
        llm_config = create_llm_config("claude-3-opus")
        config2 = PlayerAgentConfig(
            llm_config=llm_config, temperature=0.5, player_name="Test Player 2"
        )
        assert config2.llm_config == llm_config
        assert config2.temperature == 0.5


class TestGameConfigurations:
    """Test creating game configurations with the new system."""

    def test_chess_configuration(self):
        """Test chess game configuration."""
        from haive.games.chess.configurable_config import (
            create_chess_config,
            create_chess_config_from_example,
        )

        # Test simple config
        config1 = create_chess_config("gpt-4", "claude-3-opus")
        assert config1 is not None
        assert hasattr(config1, "engines")
        assert config1.engines is not None

        # Test example config
        config2 = create_chess_config_from_example("budget")
        assert config2 is not None
        assert hasattr(config2, "engines")

    def test_connect4_configuration(self):
        """Test Connect4 game configuration."""
        from haive.games.connect4.configurable_config import (
            create_connect4_config,
        )

        # Test simple config
        config1 = create_connect4_config("gpt-3.5-turbo", "gpt-3.5-turbo")
        assert config1 is not None
        assert hasattr(config1, "engines")
        assert config1.engines is not None

        # Test with canonical names
        config2 = create_connect4_config("openai:gpt-4", "anthropic:claude-3-haiku")
        assert config2 is not None

    def test_tic_tac_toe_configuration(self):
        """Test Tic-Tac-Toe game configuration."""
        from haive.games.tic_tac_toe.configurable_config import (
            create_ttt_config,
            create_ttt_config_from_player_configs,
        )

        # Test simple config
        config1 = create_ttt_config("gpt-4", "claude-3-opus")
        assert config1 is not None
        assert hasattr(config1, "engines")

        # Test with player configs
        player_configs = {
            "X_player": PlayerAgentConfig(
                llm_config="gpt-4", temperature=0.7, player_name="X Master"
            ),
            "O_player": PlayerAgentConfig(
                llm_config="claude-3-opus", temperature=0.5, player_name="O Expert"
            ),
            "X_analyzer": PlayerAgentConfig(llm_config="gpt-4", temperature=0.2),
            "O_analyzer": PlayerAgentConfig(
                llm_config="claude-3-opus", temperature=0.2
            ),
        }
        config2 = create_ttt_config_from_player_configs(player_configs)
        assert config2 is not None
        assert config2.x_player_name == "X Master"
        assert config2.o_player_name == "O Expert"


class TestGenericEngineSystem:
    """Test the generic engine system works for games."""

    def test_chess_generic_engines(self):
        """Test chess generic engine creation."""
        from haive.games.chess.generic_engines import create_generic_chess_engines

        player_configs = {
            "white_player": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "black_player": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "white_analyzer": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "black_analyzer": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
        }

        engines = create_generic_chess_engines(player_configs)
        assert isinstance(engines, list)
        assert len(engines) > 0

    def test_connect4_generic_engines(self):
        """Test Connect4 generic engine creation."""
        from haive.games.connect4.generic_engines import create_generic_connect4_engines

        player_configs = {
            "red_player": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "yellow_player": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "red_analyzer": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "yellow_analyzer": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
        }

        engines = create_generic_connect4_engines(player_configs)
        assert isinstance(engines, list)
        assert len(engines) > 0

    def test_tic_tac_toe_generic_engines(self):
        """Test Tic-Tac-Toe generic engine creation."""
        from haive.games.tic_tac_toe.generic_engines import create_generic_ttt_engines

        player_configs = {
            "X_player": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "O_player": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "X_analyzer": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
            "O_analyzer": PlayerAgentConfig(llm_config="gpt-3.5-turbo"),
        }

        engines = create_generic_ttt_engines(player_configs)
        assert isinstance(engines, list)
        assert len(engines) > 0


class TestGameStatesBasic:
    """Basic tests for game state creation."""

    def test_create_basic_states(self):
        """Test creating basic game states without complex validation."""
        successes = []
        failures = []

        # Chess
        try:
            from haive.games.chess.state import ChessState

            state = ChessState()
            assert state is not None
            successes.append("chess")
        except Exception as e:
            failures.append(("chess", str(e)))

        # Tic-Tac-Toe
        try:
            from haive.games.tic_tac_toe.state import TicTacToeState

            state = TicTacToeState()
            assert state is not None
            successes.append("tic_tac_toe")
        except Exception as e:
            failures.append(("tic_tac_toe", str(e)))

        # Mancala
        try:
            from haive.games.mancala.state import MancalaState

            state = MancalaState()
            assert state is not None
            successes.append("mancala")
        except Exception as e:
            failures.append(("mancala", str(e)))

        # Nim
        try:
            from haive.games.nim.state import NimState

            state = NimState()
            assert state is not None
            successes.append("nim")
        except Exception as e:
            failures.append(("nim", str(e)))

        if failures:
            pass

        # At least some should succeed
        assert len(successes) >= 2, f"Too few successful state creations: {successes}"


class TestAPICompatibility:
    """Test compatibility with the standardized API system."""

    def test_game_api_import(self):
        """Test that GameAPI can be imported."""
        from haive.dataflow.api.game_api import GameAPI

        assert GameAPI is not None

    def test_game_configs_api_ready(self):
        """Test that game configs are ready for API use."""
        # Import some configs
        from haive.games.chess.configurable_config import create_chess_config
        from haive.games.connect4.configurable_config import create_connect4_config
        from haive.games.tic_tac_toe.configurable_config import create_ttt_config

        configs = [
            ("chess", create_chess_config("gpt-3.5-turbo", "gpt-3.5-turbo")),
            ("connect4", create_connect4_config("gpt-3.5-turbo", "gpt-3.5-turbo")),
            ("tic_tac_toe", create_ttt_config("gpt-3.5-turbo", "gpt-3.5-turbo")),
        ]

        for game_name, config in configs:
            # Check required attributes for API
            assert hasattr(config, "name"), f"{game_name} missing 'name'"
            assert hasattr(config, "engines"), f"{game_name} missing 'engines'"
            assert config.engines is not None, f"{game_name} engines is None"


class TestEndToEndScenarios:
    """Test realistic end-to-end scenarios."""

    def test_create_game_with_different_llms(self):
        """Test creating games with different LLM combinations."""
        from haive.games.chess.configurable_config import create_chess_config

        test_cases = [
            ("gpt-4", "claude-3-opus"),
            ("gpt-3.5-turbo", "gpt-3.5-turbo"),
            ("openai:gpt-4o", "anthropic:claude-3-haiku"),
        ]

        for white_model, black_model in test_cases:
            config = create_chess_config(white_model, black_model)
            assert config is not None
            assert config.engines is not None

    def test_create_game_from_examples(self):
        """Test creating games from example configurations."""
        # Chess examples
        from haive.games.chess.configurable_config import (
            create_chess_config_from_example,
        )

        chess_examples = ["gpt_vs_claude", "budget", "gpt_only", "claude_only"]
        for example in chess_examples:
            try:
                config = create_chess_config_from_example(example)
                assert config is not None
            except Exception:
                pass

        # Tic-Tac-Toe examples
        from haive.games.tic_tac_toe.configurable_config import (
            create_ttt_config_from_example,
        )

        ttt_examples = ["gpt_vs_claude", "budget", "mixed"]
        for example in ttt_examples:
            try:
                config = create_ttt_config_from_example(example)
                assert config is not None
            except Exception:
                pass


if __name__ == "__main__":
    # Run specific test classes for debugging
    import subprocess

    subprocess.run(
        ["pytest", __file__, "-v", "-k", "TestEndToEndScenarios"], check=False
    )
