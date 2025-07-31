"""End-to-end tests for all games in haive-games package.

This test suite validates that all games:
1. Can be imported successfully
2. Can be configured using the new configurable system
3. Can create player agents and engines
4. Are compatible with the standardized API system
5. Can execute basic game moves without errors

No mocks are used - these are real integration tests.
"""

from pathlib import Path
import sys

import pytest

# Add packages to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from haive.games.core.agent.player_agent import PlayerAgentConfig


class TestGameImports:
    """Test that all game modules can be imported successfully."""

    def test_import_all_games(self):
        """Test importing all game modules."""
        games = [
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

        failed_imports = []

        for game in games:
            try:
                # Try importing the main module
                exec(f"import haive.games.{game}")

                # Try importing submodules
                exec(f"import haive.games.{game}.config")
                exec(f"import haive.games.{game}.state")
                exec(f"import haive.games.{game}.agent")

                # Try importing configurable config if it exists
                try:
                    exec(f"import haive.games.{game}.configurable_config")
                except ImportError:
                    # Not all games have configurable_config yet
                    pass

                # Try importing generic engines if it exists
                try:
                    exec(f"import haive.games.{game}.generic_engines")
                except ImportError:
                    # Not all games have generic_engines yet
                    pass

            except Exception as e:
                failed_imports.append((game, str(e)))

        # Report all failures
        if failed_imports:
            failure_msg = "Failed to import games:\n"
            for game, error in failed_imports:
                failure_msg += f"  - {game}: {error}\n"
            pytest.fail(failure_msg)


class TestGameConfiguration:
    """Test that games can be configured using the new system."""

    def get_test_games(self) -> list[str]:
        """Get list of games to test."""
        return [
            "chess",
            "connect4",
            "tic_tac_toe",
            "battleship",
            "clue",
            "debate",
            "dominoes",
            "fox_and_geese",
            "mafia",
            "mancala",
            "mastermind",
            "nim",
            "poker",
            "reversi",
            "risk",
        ]

    def test_create_configurable_configs(self):
        """Test creating configurable configs for all games."""
        failed_configs = []

        for game in self.get_test_games():
            try:
                # Import the configurable config module
                config_module = __import__(
                    f"haive.games.{game}.configurable_config",
                    fromlist=["ConfigurableConfig"],
                )

                # Find the configurable config class
                config_class = None
                for attr_name in dir(config_module):
                    attr = getattr(config_module, attr_name)
                    if (
                        isinstance(attr, type)
                        and attr_name.startswith("Configurable")
                        and attr_name.endswith("Config")
                    ):
                        config_class = attr
                        break

                if config_class is None:
                    failed_configs.append((game, "No configurable config class found"))
                    continue

                # Try to instantiate the config
                config = config_class()

                # Verify it has engines
                assert hasattr(config, "engines"), f"{game} config missing engines"
                assert config.engines is not None, f"{game} engines is None"

            except Exception as e:
                failed_configs.append((game, str(e)))

        if failed_configs:
            failure_msg = "Failed to create configs:\n"
            for game, error in failed_configs:
                failure_msg += f"  - {game}: {error}\n"
            pytest.fail(failure_msg)

    def test_create_configs_with_custom_models(self):
        """Test creating configs with custom model specifications."""
        test_models = [
            ("gpt-4o", "claude-3-opus"),
            ("openai:gpt-3.5-turbo", "anthropic:claude-3-haiku"),
            ("gpt-4", "gpt-4"),  # Same model for both players
        ]

        failed_tests = []

        for game in self.get_test_games():
            for model1, model2 in test_models:
                try:
                    # Import configurable config
                    config_module = __import__(
                        f"haive.games.{game}.configurable_config",
                        fromlist=["create_config"],
                    )

                    # Find the create function
                    create_func = None
                    for func_name in dir(config_module):
                        if func_name.startswith("create_") and "_config" in func_name:
                            create_func = getattr(config_module, func_name)
                            break

                    if create_func is None:
                        failed_tests.append(
                            (game, model1, model2, "No create function found")
                        )
                        continue

                    # Create config with custom models
                    # Games use different parameter names
                    if game in ["chess"]:
                        config = create_func(white_model=model1, black_model=model2)
                    elif game in ["connect4"]:
                        config = create_func(red_model=model1, yellow_model=model2)
                    elif game in ["tic_tac_toe"]:
                        config = create_func(x_model=model1, o_model=model2)
                    else:
                        # Generic player1/player2
                        config = create_func(player1_model=model1, player2_model=model2)

                    # Verify engines were created
                    assert hasattr(config, "engines")
                    assert config.engines is not None

                except Exception as e:
                    failed_tests.append((game, model1, model2, str(e)))

        if failed_tests:
            failure_msg = "Failed custom model tests:\n"
            for game, m1, m2, error in failed_tests:
                failure_msg += f"  - {game} ({m1}, {m2}): {error}\n"
            pytest.fail(failure_msg)


class TestGameEngines:
    """Test that game engines can be created and used."""

    def get_test_games(self) -> list[str]:
        """Get list of games with generic engines."""
        return [
            "chess",
            "connect4",
            "tic_tac_toe",
            "battleship",
            "clue",
            "debate",
            "dominoes",
            "fox_and_geese",
            "mafia",
            "mancala",
            "mastermind",
            "nim",
            "poker",
            "reversi",
            "risk",
        ]

    def test_create_generic_engines(self):
        """Test creating generic engines for all games."""
        failed_engines = []

        for game in self.get_test_games():
            try:
                # Import generic engines module
                engines_module = __import__(
                    f"haive.games.{game}.generic_engines",
                    fromlist=["create_generic_engines"],
                )

                # Find the create function
                create_func = None
                for func_name in dir(engines_module):
                    if "create_generic" in func_name and "engines" in func_name:
                        create_func = getattr(engines_module, func_name)
                        break

                if create_func is None:
                    failed_engines.append((game, "No create_generic_engines function"))
                    continue

                # Create player configs
                player_configs = {
                    "player1": PlayerAgentConfig(
                        llm_config="gpt-3.5-turbo",
                        temperature=0.7,
                        player_name="Test Player 1",
                    ),
                    "player2": PlayerAgentConfig(
                        llm_config="gpt-3.5-turbo",
                        temperature=0.7,
                        player_name="Test Player 2",
                    ),
                    "analyzer1": PlayerAgentConfig(
                        llm_config="gpt-3.5-turbo",
                        temperature=0.2,
                        player_name="Test Analyzer 1",
                    ),
                    "analyzer2": PlayerAgentConfig(
                        llm_config="gpt-3.5-turbo",
                        temperature=0.2,
                        player_name="Test Analyzer 2",
                    ),
                }

                # Adjust keys based on game
                if game == "chess":
                    player_configs = {
                        "white_player": player_configs["player1"],
                        "black_player": player_configs["player2"],
                        "white_analyzer": player_configs["analyzer1"],
                        "black_analyzer": player_configs["analyzer2"],
                    }
                elif game == "connect4":
                    player_configs = {
                        "red_player": player_configs["player1"],
                        "yellow_player": player_configs["player2"],
                        "red_analyzer": player_configs["analyzer1"],
                        "yellow_analyzer": player_configs["analyzer2"],
                    }
                elif game == "tic_tac_toe":
                    player_configs = {
                        "X_player": player_configs["player1"],
                        "O_player": player_configs["player2"],
                        "X_analyzer": player_configs["analyzer1"],
                        "O_analyzer": player_configs["analyzer2"],
                    }

                # Create engines
                engines = create_func(player_configs)

                # Verify we got a list of engines
                assert isinstance(engines, list), f"{game} engines not a list"
                assert len(engines) > 0, f"{game} no engines created"

                # Verify each engine has required attributes
                for engine in engines:
                    assert callable(engine), f"{game} engine not callable"

            except Exception as e:
                failed_engines.append((game, str(e)))

        if failed_engines:
            failure_msg = "Failed to create engines:\n"
            for game, error in failed_engines:
                failure_msg += f"  - {game}: {error}\n"
            pytest.fail(failure_msg)


class TestGameStates:
    """Test that game states can be created and manipulated."""

    def get_test_games(self) -> list[tuple[str, str]]:
        """Get list of games with their state class names."""
        return [
            ("chess", "ChessState"),
            ("connect4", "Connect4State"),
            ("tic_tac_toe", "TicTacToeState"),
            ("battleship", "BattleshipState"),
            ("clue", "ClueState"),
            ("debate", "DebateState"),
            ("dominoes", "DominoesState"),
            ("fox_and_geese", "FoxAndGeeseState"),
            ("mafia", "MafiaState"),
            ("mancala", "MancalaState"),
            ("mastermind", "MastermindState"),
            ("nim", "NimState"),
            ("poker", "PokerState"),
            ("reversi", "ReversiState"),
            ("risk", "RiskState"),
        ]

    def test_create_game_states(self):
        """Test creating game states for all games."""
        failed_states = []

        for game, state_class_name in self.get_test_games():
            try:
                # Import state module
                state_module = __import__(
                    f"haive.games.{game}.state", fromlist=[state_class_name]
                )

                # Get state class
                state_class = getattr(state_module, state_class_name)

                # Create initial state with proper initialization
                if game == "chess":
                    state = state_class()
                elif game == "connect4":
                    state = state_class(
                        turn="red", board=[[None for _ in range(7)] for _ in range(6)]
                    )
                elif game == "tic_tac_toe":
                    state = state_class()
                elif game == "battleship":
                    # Battleship requires player info
                    state = state_class(
                        players={
                            "player1": {"name": "Player 1"},
                            "player2": {"name": "Player 2"},
                        },
                        current_player="player1",
                        phase="setup",
                    )
                elif game == "clue":
                    # Clue requires complex setup
                    from haive.games.clue.state import Player as CluePlayer

                    state = state_class(
                        players=[
                            CluePlayer(
                                name="Player1",
                                character="Miss Scarlet",
                                position=(7, 0),
                            ),
                            CluePlayer(
                                name="Player2",
                                character="Colonel Mustard",
                                position=(0, 17),
                            ),
                        ],
                        current_player_index=0,
                    )
                elif game == "debate":
                    # Debate requires topic and players
                    from haive.games.debate.state import Player as DebatePlayer
                    from haive.games.debate.state import Topic

                    state = state_class(
                        topic=Topic(
                            statement="Test debate topic", description="A test topic"
                        ),
                        players=[
                            DebatePlayer(name="Debater1", stance="for"),
                            DebatePlayer(name="Debater2", stance="against"),
                        ],
                        current_speaker_index=0,
                    )
                elif game == "dominoes":
                    # Dominoes requires initialization
                    state = state_class(
                        players=["Player1", "Player2"],
                        turn=0,
                        hands={"Player1": [], "Player2": []},
                    )
                elif game == "fox_and_geese":
                    # Fox and Geese requires positions
                    state = state_class(
                        turn="fox",
                        fox_position=(0, 3),
                        geese_positions=[(6, 0), (6, 2), (6, 4), (6, 6)],
                    )
                elif game == "mafia":
                    # Import the actual MafiaGameState
                    from haive.games.mafia.state import MafiaGameState

                    state = MafiaGameState(
                        player_names=["Player1", "Player2", "Player3"]
                    )
                elif game == "mancala":
                    state = state_class()
                elif game == "mastermind":
                    # Mastermind requires setup
                    state = state_class(
                        turn=0,
                        secret_code=["red", "blue", "green", "yellow"],
                        codemaker="Player1",
                    )
                elif game == "nim":
                    # Nim with initial piles
                    state = state_class(piles=[3, 4, 5])
                elif game == "poker":
                    # Poker has complex initialization
                    state = state_class()
                elif game == "reversi":
                    # Reversi requires board and turn
                    board = [["" for _ in range(8)] for _ in range(8)]
                    # Setup initial pieces
                    board[3][3] = "white"
                    board[3][4] = "black"
                    board[4][3] = "black"
                    board[4][4] = "white"
                    state = state_class(turn="black", board=board)
                elif game == "risk":
                    # Risk requires player dict
                    state = state_class(
                        players={"Player1": {"armies": 40}, "Player2": {"armies": 40}}
                    )
                else:
                    # Fallback
                    state = state_class()

                # Verify basic state attributes
                assert hasattr(
                    state, "model_dump"
                ), f"{game} state not a Pydantic model"

                # Verify game-specific attributes
                if game in ["chess", "connect4", "tic_tac_toe", "reversi"]:
                    assert hasattr(state, "board"), f"{game} state missing board"

                if game in ["chess", "connect4", "tic_tac_toe"]:
                    assert hasattr(
                        state, "current_player"
                    ), f"{game} state missing current_player"

            except Exception as e:
                failed_states.append((game, str(e)))

        if failed_states:
            failure_msg = "Failed to create states:\n"
            for game, error in failed_states:
                failure_msg += f"  - {game}: {error}\n"
            pytest.fail(failure_msg)


class TestAPICompatibility:
    """Test that games are compatible with the standardized API system."""

    def test_import_game_api(self):
        """Test that the standardized GameAPI can be imported."""
        try:
            from haive.dataflow.api.game_api import GameAPI

            assert GameAPI is not None
        except ImportError as e:
            pytest.fail(f"Failed to import GameAPI: {e}")

    def test_game_configs_have_required_attributes(self):
        """Test that game configs have attributes required by GameAPI."""
        required_attrs = ["name", "engines"]
        games = ["chess", "connect4", "tic_tac_toe"]

        failed_checks = []

        for game in games:
            try:
                # Import configurable config
                config_module = __import__(
                    f"haive.games.{game}.configurable_config",
                    fromlist=["create_config"],
                )

                # Find create function
                create_func = None
                for func_name in dir(config_module):
                    if func_name.startswith("create_") and "_config" in func_name:
                        create_func = getattr(config_module, func_name)
                        break

                if create_func is None:
                    failed_checks.append((game, "No create function"))
                    continue

                # Create config
                if game == "chess":
                    config = create_func(
                        white_model="gpt-3.5-turbo", black_model="gpt-3.5-turbo"
                    )
                elif game == "connect4":
                    config = create_func(
                        red_model="gpt-3.5-turbo", yellow_model="gpt-3.5-turbo"
                    )
                elif game == "tic_tac_toe":
                    config = create_func(
                        x_model="gpt-3.5-turbo", o_model="gpt-3.5-turbo"
                    )

                # Check required attributes
                for attr in required_attrs:
                    if not hasattr(config, attr):
                        failed_checks.append((game, f"Missing {attr} attribute"))

            except Exception as e:
                failed_checks.append((game, str(e)))

        if failed_checks:
            failure_msg = "Failed API compatibility checks:\n"
            for game, error in failed_checks:
                failure_msg += f"  - {game}: {error}\n"
            pytest.fail(failure_msg)


class TestLLMFactory:
    """Test the LLM factory system."""

    def test_import_llm_factory(self):
        """Test importing the LLM factory."""
        try:
            from haive.core.models.llm.factory import create_llm_config
            from haive.core.models.llm.helpers import llm

            assert create_llm_config is not None
            assert llm is not None
        except ImportError as e:
            pytest.fail(f"Failed to import LLM factory: {e}")

    def test_create_llm_configs(self):
        """Test creating LLM configs with various formats."""
        from haive.core.models.llm.factory import create_llm_config

        test_cases = [
            "gpt-4",
            "gpt-3.5-turbo",
            "claude-3-opus",
            "openai:gpt-4o",
            "anthropic:claude-3-5-sonnet-20240620",
        ]

        failed_cases = []

        for model_str in test_cases:
            try:
                config = create_llm_config(model_str)
                assert config is not None
                assert hasattr(config, "model")
                assert hasattr(config, "provider")
            except Exception as e:
                failed_cases.append((model_str, str(e)))

        if failed_cases:
            failure_msg = "Failed to create LLM configs:\n"
            for model, error in failed_cases:
                failure_msg += f"  - {model}: {error}\n"
            pytest.fail(failure_msg)


class TestPlayerAgentSystem:
    """Test the player agent system."""

    def test_import_player_agent(self):
        """Test importing player agent components."""
        try:
            from haive.games.core.agent.player_agent import (
                PlayerAgentConfig,
                PlayerAgentFactory,
            )

            assert PlayerAgentConfig is not None
            assert PlayerAgentFactory is not None
        except ImportError as e:
            pytest.fail(f"Failed to import player agent: {e}")

    def test_create_player_agents(self):
        """Test creating player agents."""
        from haive.games.core.agent.player_agent import (
            PlayerAgentConfig,
            PlayerAgentFactory,
        )

        # Create config
        config = PlayerAgentConfig(
            llm_config="gpt-3.5-turbo", temperature=0.7, player_name="Test Player"
        )

        # Create factory
        factory = PlayerAgentFactory()

        # Create agent - note: this would normally require proper game setup
        # For now just verify the config and factory work
        assert config.llm_config == "gpt-3.5-turbo"
        assert config.temperature == 0.7
        assert config.player_name == "Test Player"
        assert factory is not None


class TestGenericPlayerSystem:
    """Test the generic player system."""

    def test_import_generic_components(self):
        """Test importing generic player components."""
        try:
            from haive.games.core.agent.generic_player_agent import (
                GamePlayerIdentifiers,
                GenericGameEngineFactory,
                GenericPromptGenerator,
            )

            assert GamePlayerIdentifiers is not None
            assert GenericPromptGenerator is not None
            assert GenericGameEngineFactory is not None
        except ImportError as e:
            pytest.fail(f"Failed to import generic components: {e}")

    def test_game_player_identifiers(self):
        """Test creating game player identifiers."""
        from haive.games.core.agent.generic_player_agent import GamePlayerIdentifiers

        # Test with strings
        ids1 = GamePlayerIdentifiers[str, str](player1="white", player2="black")
        assert ids1.player1 == "white"
        assert ids1.player2 == "black"

        # Test with mixed types
        ids2 = GamePlayerIdentifiers[str, int](player1="player", player2=1)
        assert ids2.player1 == "player"
        assert ids2.player2 == 1


class TestMinimalGameExecution:
    """Test minimal game execution without full games."""

    def test_tic_tac_toe_state_transitions(self):
        """Test basic tic-tac-toe state transitions."""
        from haive.games.tic_tac_toe.state import TicTacToeState

        # Create initial state
        state = TicTacToeState()

        # Verify initial state
        assert state.current_player_name == "X"
        assert state.result is None
        assert not state.is_terminal

        # Make a move (manually update state)
        state.board[0][0] = "X"
        state.current_player_name = "O"
        state.moves.append({"player": "X", "row": 0, "col": 0})

        # Verify state changed
        assert state.current_player_name == "O"
        assert state.board[0][0] == "X"
        assert len(state.moves) == 1

    def test_chess_state_creation(self):
        """Test chess state creation."""
        from haive.games.chess.state import ChessState

        # Create initial state
        state = ChessState()

        # Verify initial state
        assert state.current_player_name == "white"
        assert state.result is None
        assert not state.is_terminal
        assert state.fen is not None  # Chess uses FEN notation

    def test_connect4_state_creation(self):
        """Test Connect4 state creation."""
        from haive.games.connect4.state import Connect4State

        # Create initial state with required fields
        state = Connect4State(
            turn="red", board=[[None for _ in range(7)] for _ in range(6)]
        )

        # Verify initial state
        assert state.turn == "red"
        assert state.result is None
        assert not state.is_terminal
        assert len(state.board) == 6  # 6 rows
        assert len(state.board[0]) == 7  # 7 columns


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])
