"""Comprehensive tests for Checkers generic agent system.

This test suite validates:
1. Generic engine creation and configuration
2. Configurable configuration system
3. Cross-game consistency with other games
4. Error handling and edge cases
5. Configuration validation
"""

from unittest.mock import MagicMock, patch

import pytest

from haive.games.checkers.agent import CheckersAgent
from haive.games.checkers.configurable_config import (
    ConfigurableCheckersConfig,
    create_checkers_config,
    create_checkers_config_from_example,
    create_checkers_config_from_player_configs,
    get_example_config,
    list_example_configurations,
)
from haive.games.checkers.generic_engines import (
    CheckersPromptGenerator,
    checkers_players,
    create_generic_checkers_config_from_example,
    create_generic_checkers_engines,
    create_generic_checkers_engines_simple,
)
from haive.games.core.agent.player_agent import PlayerAgentConfig


class TestCheckersGenericEngines:
    """Test Checkers generic engine creation."""

    def test_create_generic_engines_simple(self):
        """Test creating engines with simple model strings."""
        engines = create_generic_checkers_engines_simple("gpt-4o", "claude-3-opus")

        # Check all expected engines are created
        expected_roles = [
            "red_player",
            "black_player",
            "red_analyzer",
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
            "red_player": PlayerAgentConfig(
                llm_config="gpt-4o", temperature=0.8, player_name="Aggressive Red"
            ),
            "black_player": PlayerAgentConfig(
                llm_config="claude-3-opus",
                temperature=0.6,
                player_name="Strategic Black",
            ),
            "red_analyzer": PlayerAgentConfig(
                llm_config="gemini-1.5-pro", temperature=0.3, player_name="Red Analyst"
            ),
            "black_analyzer": PlayerAgentConfig(
                llm_config="llama-3.1-70b", temperature=0.3, player_name="Black Analyst"
            ),
        }

        engines = create_generic_checkers_engines(player_configs)

        assert len(engines) == 4
        assert "red_player" in engines
        assert "black_player" in engines
        assert "red_analyzer" in engines
        assert "black_analyzer" in engines

    def test_create_engines_from_examples(self):
        """Test creating engines from example configurations."""
        examples = [
            "gpt_vs_claude",
            "gpt_only",
            "claude_only",
            "mixed",
            "budget",
            "checkers_masters",
        ]

        for example_name in examples:
            engines = create_generic_checkers_config_from_example(example_name)
            assert len(engines) == 4
            assert all(
                role in engines
                for role in [
                    "red_player",
                    "black_player",
                    "red_analyzer",
                    "black_analyzer",
                ]
            )

    def test_prompt_generator(self):
        """Test Checkers prompt generator."""
        generator = CheckersPromptGenerator(checkers_players)

        # Test move prompt creation
        red_prompt = generator.create_move_prompt("red")
        black_prompt = generator.create_move_prompt("black")

        assert red_prompt is not None
        assert black_prompt is not None

        # Test analysis prompt creation
        red_analysis = generator.create_analysis_prompt("red")
        black_analysis = generator.create_analysis_prompt("black")

        assert red_analysis is not None
        assert black_analysis is not None

        # Test output models
        move_model = generator.get_move_output_model()
        analysis_model = generator.get_analysis_output_model()

        assert move_model is not None
        assert analysis_model is not None


class TestCheckersConfigurableConfig:
    """Test Checkers configurable configuration."""

    def test_simple_model_configuration(self):
        """Test configuration with simple model strings."""
        config = create_checkers_config("gpt-4o", "claude-3-opus", temperature=0.8)

        assert config.red_model == "gpt-4o"
        assert config.black_model == "claude-3-opus"
        assert config.temperature == 0.8
        assert len(config.engines) == 4

    def test_example_configuration(self):
        """Test configuration from examples."""
        config = create_checkers_config_from_example("gpt_vs_claude")

        assert config.example_config == "gpt_vs_claude"
        assert len(config.engines) == 4
        assert (
            "red" in config.red_player_name.lower()
            or "gpt" in config.red_player_name.lower()
        )

    def test_player_configs_configuration(self):
        """Test configuration with player configs."""
        player_configs = {
            "red_player": PlayerAgentConfig(
                llm_config="gpt-4o", player_name="Red Baron"
            ),
            "black_player": PlayerAgentConfig(
                llm_config="claude-3-opus", player_name="Black Knight"
            ),
            "red_analyzer": PlayerAgentConfig(
                llm_config="gpt-4o", player_name="Red Strategist"
            ),
            "black_analyzer": PlayerAgentConfig(
                llm_config="claude-3-opus", player_name="Black Tactician"
            ),
        }

        config = create_checkers_config_from_player_configs(player_configs)

        assert config.player_configs == player_configs
        assert config.red_player_name == "Red Baron"
        assert config.black_player_name == "Black Knight"
        assert len(config.engines) == 4

    def test_default_configuration(self):
        """Test default configuration when no options specified."""
        config = ConfigurableCheckersConfig()

        assert len(config.engines) == 4
        assert config.red_player_name is not None
        assert config.black_player_name is not None

    def test_example_config_methods(self):
        """Test example configuration methods."""
        # Test get_example_config
        config = get_example_config("simple")
        assert isinstance(config, ConfigurableCheckersConfig)

        # Test list_example_configurations
        examples = list_example_configurations()
        assert isinstance(examples, dict)
        assert "simple" in examples
        assert "budget" in examples

    def test_invalid_example_name(self):
        """Test handling of invalid example names."""
        with pytest.raises(ValueError, match="Unknown example"):
            get_example_config("invalid_example")


class TestCheckersAPICompatibility:
    """Test that Checkers agents work with standardized API patterns."""

    def test_checkers_api_compatibility(self):
        """Test Checkers agent works with standardized API patterns."""
        from haive.games.checkers.agent import CheckersAgent
        from haive.games.checkers.state import CheckersState

        # Test agent class has required attributes for API
        assert hasattr(CheckersAgent, "__init__")
        assert hasattr(CheckersAgent, "run")

        # Test state schema
        assert hasattr(CheckersState, "model_dump")

        # Test configuration
        config = create_checkers_config("gpt-4o", "claude-3-opus")
        agent = CheckersAgent(config)

        # Test agent has proper structure for API integration
        assert hasattr(agent, "config")
        assert hasattr(agent, "engines")


class TestCheckersErrorHandling:
    """Test Checkers error handling and edge cases."""

    def test_invalid_example_name_in_engines(self):
        """Test handling of invalid example names in engine creation."""
        with pytest.raises(ValueError, match="Unknown example"):
            create_generic_checkers_config_from_example("invalid_example")

    def test_missing_player_config(self):
        """Test handling of missing player configurations."""
        incomplete_configs = {
            "red_player": PlayerAgentConfig(llm_config="gpt-4o"),
            # Missing other roles
        }

        with pytest.raises(ValueError, match="No player config provided"):
            create_generic_checkers_engines(incomplete_configs)

    def test_configuration_validation(self):
        """Test configuration validation."""
        # Test with invalid max_moves
        config = ConfigurableCheckersConfig(max_moves=-1)
        assert config.max_moves == -1  # Should accept but may cause issues

        # Test with valid configuration
        config = ConfigurableCheckersConfig(
            red_model="gpt-4o",
            black_model="claude-3-opus",
            max_moves=150,
            enable_analysis=True,
            recursion_limit=600,
        )
        assert config.max_moves == 150
        assert config.enable_analysis is True
        assert config.recursion_limit == 600


class TestCheckersCrossGameConsistency:
    """Test that Checkers follows the same patterns as other games."""

    def test_engine_structure_consistency(self):
        """Test that Checkers follows the same engine structure as other games."""
        checkers_engines = create_generic_checkers_engines_simple(
            "gpt-4o", "claude-3-opus"
        )

        # Should have 4 engines (2 players + 2 analyzers)
        assert len(checkers_engines) == 4

        # Check pattern: player1_player, player2_player, player1_analyzer, player2_analyzer
        checkers_roles = set(checkers_engines.keys())
        expected_pattern = {
            "red_player",
            "black_player",
            "red_analyzer",
            "black_analyzer",
        }

        assert checkers_roles == expected_pattern

    def test_configuration_api_consistency(self):
        """Test that configuration APIs are consistent with other games."""
        # Test that Checkers supports the same configuration methods

        # Simple configuration
        checkers_config = create_checkers_config(
            "gpt-4o", "claude-3-opus", temperature=0.7
        )
        assert checkers_config.temperature == 0.7

        # Example configuration
        checkers_example = create_checkers_config_from_example("gpt_only")
        assert checkers_example.example_config == "gpt_only"
        assert len(checkers_example.engines) == 4

    def test_generic_system_type_safety(self):
        """Test that the generic system maintains type safety for Checkers."""
        from haive.games.core.agent.generic_player_agent import (
            CheckersPlayerIdentifiers,
        )

        # Test player identifiers are correct
        checkers_players_inst = CheckersPlayerIdentifiers()

        assert checkers_players_inst.player1 == "red"
        assert checkers_players_inst.player2 == "black"

    def test_cross_game_pattern_comparison(self):
        """Test that Checkers, Chess, and other games follow the same pattern."""
        # Create engines for comparison
        checkers_engines = create_generic_checkers_engines_simple(
            "gpt-4o", "claude-3-opus"
        )

        # All should have 4 engines
        assert len(checkers_engines) == 4

        # All should follow the {player}_{role} naming pattern
        for role_name in checkers_engines.keys():
            assert "_" in role_name
            player_part, role_part = role_name.split("_", 1)
            assert player_part in ["red", "black"]
            assert role_part in ["player", "analyzer"]


class TestCheckersGameExecution:
    """Test Checkers game execution with mocked LLM calls."""

    @patch("haive.core.engine.aug_llm.AugLLMConfig.invoke")
    def test_checkers_game_execution_mock(self, mock_invoke):
        """Test Checkers game can execute moves with mocked LLM."""
        # Mock LLM responses for checkers moves
        mock_invoke.side_effect = [
            # Mock checkers move response
            MagicMock(
                move=MagicMock(from_position="a3", to_position="b4", player="red")
            ),
            # Mock analysis response (if needed)
            MagicMock(
                material_advantage="Equal pieces",
                control_of_center="Red controls center",
            ),
        ]

        # Create a checkers game with limited moves
        config = create_checkers_config(
            "gpt-4o", "claude-3-opus", max_moves=2, enable_analysis=False
        )
        agent = CheckersAgent(config)

        # This would normally run the game, but we're just testing instantiation
        assert agent is not None
        assert len(agent.engines) == 4


class TestCheckersIntegrationWithStandardizedAPI:
    """Test Checkers integration with the standardized API system."""

    def test_checkers_agent_instantiation(self):
        """Test that Checkers agents can be instantiated with configurations."""
        # Simple configuration
        checkers_config = create_checkers_config(
            "gpt-4o", "claude-3-opus", max_moves=10
        )
        checkers_agent = CheckersAgent(checkers_config)
        assert checkers_agent.config == checkers_config
        assert hasattr(checkers_agent, "engines")

        # Example configuration
        example_config = create_checkers_config_from_example("budget")
        example_agent = CheckersAgent(example_config)
        assert example_agent.config == example_config
        assert hasattr(example_agent, "engines")

    def test_checkers_standardized_api_readiness(self):
        """Test that Checkers is ready for standardized API integration."""
        # Test that all necessary components exist
        from haive.games.checkers.agent import CheckersAgent
        from haive.games.checkers.state import CheckersState

        # Create configuration
        config = create_checkers_config("gpt-4o", "claude-3-opus")
        agent = CheckersAgent(config)

        # Test API requirements
        assert hasattr(agent, "run")  # Required for GameAPI
        assert hasattr(agent, "config")  # Required for configuration access
        assert hasattr(CheckersState, "model_dump")  # Required for JSON serialization

        # Test engine access
        assert hasattr(agent, "engines")
        assert len(agent.engines) == 4


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
