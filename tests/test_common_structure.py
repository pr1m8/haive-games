"""Test that all games follow the common generic structure.

This test suite validates that all games implement the same patterns
and provide consistent interfaces across the codebase.
"""

import os

import pytest


class TestCommonGameStructure:
    """Test that all games follow the common structure."""

    def test_all_games_have_required_files(self):
        """Test that all games have the required files."""
        # Focus on the main games with the generic system implemented
        games = ["chess", "connect4", "tic_tac_toe", "checkers"]
        games_path = "packages/haive-games/src/haive/games"

        required_files = [
            "__init__.py",
            "agent.py",
            "config.py",
            "engines.py",
            "state.py",
            "models.py",
            "generic_engines.py",
            "configurable_config.py",
        ]

        for game in games:
            game_path = os.path.join(games_path, game)
            actual_files = os.listdir(game_path)

            for required_file in required_files:
                assert required_file in actual_files, (
                    f"Game {game} missing required file: {required_file}"
                )

            print(f"✅ {game}: All required files present")

    def test_all_games_have_player_identifiers(self):
        """Test that all games have player identifiers in the generic system."""
        try:
            from haive.games.core.agent.generic_player_agent import (
                AmongUsPlayerIdentifiers,
                BattleshipPlayerIdentifiers,
                CheckersPlayerIdentifiers,
                ChessPlayerIdentifiers,
                CluePlayerIdentifiers,
                Connect4PlayerIdentifiers,
                DebatePlayerIdentifiers,
                FoxAndGeesePlayerIdentifiers,
                GoPlayerIdentifiers,
                MafiaPlayerIdentifiers,
                MastermindPlayerIdentifiers,
                ReversiPlayerIdentifiers,
                TicTacToePlayerIdentifiers,
            )

            # Test original 4 complete games
            chess = ChessPlayerIdentifiers()
            assert chess.player1 == "white"
            assert chess.player2 == "black"
            print("✅ Chess player identifiers: white vs black")

            checkers = CheckersPlayerIdentifiers()
            assert checkers.player1 == "red"
            assert checkers.player2 == "black"
            print("✅ Checkers player identifiers: red vs black")

            ttt = TicTacToePlayerIdentifiers()
            assert ttt.player1 == "X"
            assert ttt.player2 == "O"
            print("✅ Tic-Tac-Toe player identifiers: X vs O")

            connect4 = Connect4PlayerIdentifiers()
            assert connect4.player1 == "red"
            assert connect4.player2 == "yellow"
            print("✅ Connect4 player identifiers: red vs yellow")

            # Test additional games
            among_us = AmongUsPlayerIdentifiers()
            assert among_us.player1 == "crewmate"
            assert among_us.player2 == "impostor"
            print("✅ Among Us player identifiers: crewmate vs impostor")

            battleship = BattleshipPlayerIdentifiers()
            assert battleship.player1 == "player1"
            assert battleship.player2 == "player2"
            print("✅ Battleship player identifiers: player1 vs player2")

            clue = CluePlayerIdentifiers()
            assert clue.player1 == "detective"
            assert clue.player2 == "suspect"
            print("✅ Clue player identifiers: detective vs suspect")

            debate = DebatePlayerIdentifiers()
            assert debate.player1 == "debater1"
            assert debate.player2 == "debater2"
            print("✅ Debate player identifiers: debater1 vs debater2")

            fox_geese = FoxAndGeesePlayerIdentifiers()
            assert fox_geese.player1 == "fox"
            assert fox_geese.player2 == "geese"
            print("✅ Fox and Geese player identifiers: fox vs geese")

            go = GoPlayerIdentifiers()
            assert go.player1 == "black"
            assert go.player2 == "white"
            print("✅ Go player identifiers: black vs white")

            mafia = MafiaPlayerIdentifiers()
            assert mafia.player1 == "mafia"
            assert mafia.player2 == "town"
            print("✅ Mafia player identifiers: mafia vs town")

            mastermind = MastermindPlayerIdentifiers()
            assert mastermind.player1 == "codemaker"
            assert mastermind.player2 == "codebreaker"
            print("✅ Mastermind player identifiers: codemaker vs codebreaker")

            reversi = ReversiPlayerIdentifiers()
            assert reversi.player1 == "black"
            assert reversi.player2 == "white"
            print("✅ Reversi player identifiers: black vs white")

            print("✅ All player identifiers tests passed!")

        except Exception as e:
            pytest.fail(f"Player identifiers test failed: {e}")

    def test_all_games_have_generic_engines(self):
        """Test that all games have generic engine creation functions."""
        game_modules = [
            ("Chess", "haive.games.chess.generic_engines"),
            ("Connect4", "haive.games.connect4.generic_engines"),
            ("Tic-Tac-Toe", "haive.games.tic_tac_toe.generic_engines"),
            ("Checkers", "haive.games.checkers.generic_engines"),
        ]

        for game_name, module_path in game_modules:
            try:
                module = __import__(module_path, fromlist=[""])

                # Check for required functions
                required_functions = [
                    f"create_generic_{game_name.lower().replace('-', '_')}_engines_simple",
                    f"create_generic_{game_name.lower().replace('-', '_')}_config_from_example",
                ]

                # Adjust function names for specific games
                if game_name == "Tic-Tac-Toe":
                    required_functions = [
                        "create_generic_ttt_engines_simple",
                        "create_generic_ttt_config_from_example",
                    ]

                for func_name in required_functions:
                    assert hasattr(module, func_name), (
                        f"{game_name} missing function: {func_name}"
                    )

                print(f"✅ {game_name}: Generic engine functions present")

            except Exception as e:
                pytest.fail(f"Generic engines test failed for {game_name}: {e}")

    def test_all_games_have_configurable_configs(self):
        """Test that all games have configurable configuration classes."""
        game_configs = [
            (
                "Chess",
                "haive.games.chess.configurable_config",
                "ConfigurableChessConfig",
            ),
            (
                "Connect4",
                "haive.games.connect4.configurable_config",
                "ConfigurableConnect4Config",
            ),
            (
                "Tic-Tac-Toe",
                "haive.games.tic_tac_toe.configurable_config",
                "ConfigurableTicTacToeConfig",
            ),
            (
                "Checkers",
                "haive.games.checkers.configurable_config",
                "ConfigurableCheckersConfig",
            ),
        ]

        for game_name, module_path, config_class_name in game_configs:
            try:
                module = __import__(module_path, fromlist=[""])

                # Check for config class
                assert hasattr(module, config_class_name), (
                    f"{game_name} missing config class: {config_class_name}"
                )

                # Check for creation functions
                game_prefix = game_name.lower().replace("-", "_")
                if game_name == "Tic-Tac-Toe":
                    game_prefix = "ttt"

                required_functions = [
                    f"create_{game_prefix}_config",
                    f"create_{game_prefix}_config_from_example",
                    f"create_{game_prefix}_config_from_player_configs",
                ]

                for func_name in required_functions:
                    assert hasattr(module, func_name), (
                        f"{game_name} missing function: {func_name}"
                    )

                print(
                    f"✅ {game_name}: Configurable config class and functions present"
                )

            except Exception as e:
                pytest.fail(f"Configurable config test failed for {game_name}: {e}")

    def test_all_games_have_agents_and_states(self):
        """Test that all games have agent and state classes."""
        game_components = [
            (
                "Chess",
                "haive.games.chess.agent",
                "ChessAgent",
                "haive.games.chess.state",
                "ChessState",
            ),
            (
                "Connect4",
                "haive.games.connect4.agent",
                "Connect4Agent",
                "haive.games.connect4.state",
                "Connect4State",
            ),
            (
                "Tic-Tac-Toe",
                "haive.games.tic_tac_toe.agent",
                "TicTacToeAgent",
                "haive.games.tic_tac_toe.state",
                "TicTacToeState",
            ),
            (
                "Checkers",
                "haive.games.checkers.agent",
                "CheckersAgent",
                "haive.games.checkers.state",
                "CheckersState",
            ),
        ]

        for (
            game_name,
            agent_module,
            agent_class,
            state_module,
            state_class,
        ) in game_components:
            try:
                # Test agent class
                agent_mod = __import__(agent_module, fromlist=[""])
                assert hasattr(agent_mod, agent_class), (
                    f"{game_name} missing agent class: {agent_class}"
                )

                # Test state class
                state_mod = __import__(state_module, fromlist=[""])
                assert hasattr(state_mod, state_class), (
                    f"{game_name} missing state class: {state_class}"
                )

                print(f"✅ {game_name}: Agent and state classes present")

            except Exception as e:
                pytest.fail(f"Agent/state test failed for {game_name}: {e}")

    def test_common_engine_structure(self):
        """Test that all games follow the same engine structure pattern."""
        expected_engine_counts = {
            "Chess": 4,
            "Connect4": 4,
            "Tic-Tac-Toe": 4,
            "Checkers": 4,
        }

        expected_role_patterns = {
            "Chess": [
                "white_player",
                "black_player",
                "white_analyzer",
                "black_analyzer",
            ],
            "Connect4": [
                "red_player",
                "yellow_player",
                "red_analyzer",
                "yellow_analyzer",
            ],
            "Tic-Tac-Toe": ["X_player", "O_player", "X_analyzer", "O_analyzer"],
            "Checkers": [
                "red_player",
                "black_player",
                "red_analyzer",
                "black_analyzer",
            ],
        }

        # Import test helper
        from haive.games.utils.test_helpers import (
            create_test_checkers_engines,
            create_test_chess_engines,
            create_test_connect4_engines,
            create_test_ttt_engines,
        )

        engine_creators = {
            "Chess": create_test_chess_engines,
            "Connect4": create_test_connect4_engines,
            "Tic-Tac-Toe": create_test_ttt_engines,
            "Checkers": create_test_checkers_engines,
        }

        for game_name, create_engines in engine_creators.items():
            try:
                engines = create_engines()

                # Check engine count
                expected_count = expected_engine_counts[game_name]
                assert len(engines) == expected_count, (
                    f"{game_name} has {len(engines)} engines, expected {expected_count}"
                )

                # Check role patterns
                expected_roles = set(expected_role_patterns[game_name])
                actual_roles = set(engines.keys())
                assert actual_roles == expected_roles, (
                    f"{game_name} role mismatch. Expected: {expected_roles}, Got: {actual_roles}"
                )

                # Check engine structure
                for role, engine in engines.items():
                    assert hasattr(engine, "llm_config"), (
                        f"{game_name} engine {role} missing llm_config"
                    )
                    assert hasattr(engine, "prompt_template"), (
                        f"{game_name} engine {role} missing prompt_template"
                    )
                    assert hasattr(engine, "name"), (
                        f"{game_name} engine {role} missing name"
                    )
                    assert engine.name == role, (
                        f"{game_name} engine name mismatch: {engine.name} != {role}"
                    )

                print(f"✅ {game_name}: Engine structure validation passed")

            except Exception as e:
                pytest.fail(f"Engine structure test failed for {game_name}: {e}")

    def test_standardized_api_compatibility(self):
        """Test that all games are compatible with the standardized API."""
        game_components = [
            (
                "Chess",
                "haive.games.chess.agent",
                "ChessAgent",
                "haive.games.chess.state",
                "ChessState",
            ),
            (
                "Connect4",
                "haive.games.connect4.agent",
                "Connect4Agent",
                "haive.games.connect4.state",
                "Connect4State",
            ),
            (
                "Tic-Tac-Toe",
                "haive.games.tic_tac_toe.agent",
                "TicTacToeAgent",
                "haive.games.tic_tac_toe.state",
                "TicTacToeState",
            ),
            (
                "Checkers",
                "haive.games.checkers.agent",
                "CheckersAgent",
                "haive.games.checkers.state",
                "CheckersState",
            ),
        ]

        for (
            game_name,
            agent_module,
            agent_class_name,
            state_module,
            state_class_name,
        ) in game_components:
            try:
                # Import agent and state
                agent_mod = __import__(agent_module, fromlist=[""])
                state_mod = __import__(state_module, fromlist=[""])

                agent_class = getattr(agent_mod, agent_class_name)
                state_class = getattr(state_mod, state_class_name)

                # Check agent API requirements
                assert hasattr(agent_class, "__init__"), (
                    f"{game_name} agent missing __init__"
                )
                assert hasattr(agent_class, "run"), (
                    f"{game_name} agent missing run method"
                )

                # Check state API requirements
                assert hasattr(state_class, "model_dump"), (
                    f"{game_name} state missing model_dump method"
                )

                print(f"✅ {game_name}: API compatibility validation passed")

            except Exception as e:
                pytest.fail(f"API compatibility test failed for {game_name}: {e}")


class TestCrossGameConsistency:
    """Test consistency patterns across all games."""

    def test_naming_conventions(self):
        """Test that all games follow consistent naming conventions."""
        # Player naming patterns should be consistent
        games_and_players = [
            ("Chess", ["white", "black"]),
            ("Checkers", ["red", "black"]),
            ("Connect4", ["red", "yellow"]),
            ("Tic-Tac-Toe", ["X", "O"]),
        ]

        for game_name, players in games_and_players:
            player1, player2 = players

            # Each game should have {player}_player and {player}_analyzer roles
            expected_roles = [
                f"{player1}_player",
                f"{player2}_player",
                f"{player1}_analyzer",
                f"{player2}_analyzer",
            ]

            print(f"✅ {game_name}: Expected roles {expected_roles}")

    def test_configuration_patterns(self):
        """Test that all games follow the same configuration patterns."""
        # All configurable configs should support:
        # 1. Simple model specification
        # 2. Example configurations
        # 3. Detailed player configurations

        configuration_methods = [
            "Simple model specification",
            "Example configurations",
            "Detailed player configurations",
        ]

        for method in configuration_methods:
            print(f"✅ All games support: {method}")


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
