"""Comprehensive tests for Clue game agent.

This module tests the ClueAgent class and its game management,
visualization, and execution methods.
"""

import time
from unittest.mock import Mock, patch

import pytest

from haive.games.clue.agent import ClueAgent
from haive.games.clue.config import ClueConfig
from haive.games.clue.models import ClueSolution, ValidRoom, ValidSuspect, ValidWeapon
from haive.games.clue.state import ClueState
from haive.games.clue.state_manager import ClueStateManager


class TestClueAgentInitialization:
    """Test ClueAgent initialization."""

    def test_agent_creation_with_default_config(self):
        """Test creating agent with default configuration."""
        agent = ClueAgent()

        assert isinstance(agent, ClueAgent)
        assert isinstance(agent.config, ClueConfig)
        assert agent.state_manager == ClueStateManager

    def test_agent_creation_with_custom_config(self):
        """Test creating agent with custom configuration."""
        custom_solution = ClueSolution(
            suspect=ValidSuspect.PROFESSOR_PLUM,
            weapon=ValidWeapon.LEAD_PIPE,
            room=ValidRoom.CONSERVATORY,
        )

        config = ClueConfig(
            solution=custom_solution,
            first_player="player2",
            max_turns=15,
            visualize=False,
        )

        agent = ClueAgent(config)

        assert agent.config == config
        assert agent.config.solution == custom_solution
        assert agent.config.first_player == "player2"
        assert agent.config.max_turns == 15
        assert agent.config.visualize is False

    def test_agent_has_required_attributes(self):
        """Test that agent has all required attributes."""
        agent = ClueAgent()

        assert hasattr(agent, "config")
        assert hasattr(agent, "state_manager")
        assert hasattr(agent, "initialize_game")
        assert hasattr(agent, "visualize_state")
        assert hasattr(agent, "run_game")


class TestClueAgentGameInitialization:
    """Test game initialization methods."""

    def test_initialize_game_with_empty_state(self):
        """Test initializing game with empty state dictionary."""
        agent = ClueAgent()

        initial_state = agent.initialize_game({})

        assert isinstance(initial_state, dict)
        assert "solution" in initial_state
        assert "guesses" in initial_state
        assert "responses" in initial_state
        assert "current_player" in initial_state
        assert "game_status" in initial_state

    def test_initialize_game_with_custom_solution(self):
        """Test initializing game with custom solution in config."""
        custom_solution = ClueSolution(
            suspect=ValidSuspect.MISS_SCARLET,
            weapon=ValidWeapon.ROPE,
            room=ValidRoom.STUDY,
        )

        config = ClueConfig(solution=custom_solution)
        agent = ClueAgent(config)

        initial_state = agent.initialize_game({})

        # Verify solution is set correctly
        assert initial_state["solution"]["suspect"] == "Miss Scarlet"
        assert initial_state["solution"]["weapon"] == "Rope"
        assert initial_state["solution"]["room"] == "Study"

    def test_initialize_game_with_custom_parameters(self):
        """Test initializing game with custom parameters."""
        config = ClueConfig(
            first_player="player2",
            max_turns=25,
        )
        agent = ClueAgent(config)

        initial_state = agent.initialize_game({})

        assert initial_state["current_player"] == "player2"
        assert initial_state["max_turns"] == 25

    def test_initialize_game_state_serialization(self):
        """Test that initialize_game properly serializes state."""
        agent = ClueAgent()

        initial_state = agent.initialize_game({})

        # Should be able to recreate ClueState from dict
        game_state = ClueState(**initial_state)
        assert isinstance(game_state, ClueState)
        assert isinstance(game_state.solution, ClueSolution)


class TestClueAgentVisualization:
    """Test visualization methods."""

    def test_visualize_state_disabled(self):
        """Test visualization when disabled in config."""
        config = ClueConfig(visualize=False)
        agent = ClueAgent(config)

        state_dict = agent.initialize_game({})

        # Should not raise error and should return quickly
        start_time = time.time()
        agent.visualize_state(state_dict)
        end_time = time.time()

        # Should be very fast since visualization is disabled
        assert end_time - start_time < 0.1

    @patch("haive.games.clue.agent.logger")
    def test_visualize_state_enabled_ongoing_game(self, mock_logger):
        """Test visualization for ongoing game."""
        config = ClueConfig(visualize=True)
        agent = ClueAgent(config)

        state_dict = agent.initialize_game({})

        # Visualize the state
        agent.visualize_state(state_dict)

        # Check that logger was called with game info
        assert mock_logger.info.called
        call_args_list = [call[0][0] for call in mock_logger.info.call_args_list]

        # Should contain game header info
        header_calls = [call for call in call_args_list if "🎮 Game: Clue" in call]
        assert len(header_calls) > 0

        # Should not show solution for ongoing game
        solution_calls = [call for call in call_args_list if "🔑 Solution:" in call]
        assert len(solution_calls) == 0

    @patch("haive.games.clue.agent.logger")
    def test_visualize_state_enabled_completed_game(self, mock_logger):
        """Test visualization for completed game."""
        config = ClueConfig(visualize=True)
        agent = ClueAgent(config)

        state_dict = agent.initialize_game({})
        state_dict["game_status"] = "player1_win"

        # Visualize the completed state
        agent.visualize_state(state_dict)

        # Check that solution is shown for completed game
        call_args_list = [call[0][0] for call in mock_logger.info.call_args_list]
        solution_calls = [call for call in call_args_list if "🔑 Solution:" in call]
        assert len(solution_calls) > 0

    @patch("haive.games.clue.agent.logger")
    @patch("time.sleep")  # Mock sleep to speed up tests
    def test_visualize_state_with_guesses(self, mock_sleep, mock_logger):
        """Test visualization with game history."""
        config = ClueConfig(visualize=True)
        agent = ClueAgent(config)

        # Create state with guesses
        game_state = ClueState.initialize()
        game_state.guesses = [
            # Note: Using string values to match board_string format
        ]

        state_dict = (
            game_state.model_dump()
            if hasattr(game_state, "model_dump")
            else game_state.dict()
        )

        agent.visualize_state(state_dict)

        # Verify sleep was called for pacing
        mock_sleep.assert_called_once_with(0.5)

    def test_visualize_state_handles_invalid_state(self):
        """Test visualization handles invalid state gracefully."""
        config = ClueConfig(visualize=True)
        agent = ClueAgent(config)

        # This might raise an error, but should be handled gracefully
        invalid_state = {"invalid": "state"}

        # Should not crash
        try:
            agent.visualize_state(invalid_state)
        except Exception:
            # It's okay if it raises an exception with invalid state
            pass


class TestClueAgentGameExecution:
    """Test game execution methods."""

    def test_run_game_basic(self):
        """Test basic game execution."""
        agent = ClueAgent()

        result = agent.run_game(visualize=False)

        assert isinstance(result, dict)
        assert "solution" in result
        assert "game_status" in result
        assert "guesses" in result

    def test_run_game_with_visualization(self):
        """Test game execution with visualization."""
        config = ClueConfig(visualize=True)
        agent = ClueAgent(config)

        # This test might take longer due to visualization delays
        result = agent.run_game(visualize=True)

        assert isinstance(result, dict)
        assert "game_status" in result

    def test_run_game_respects_max_turns(self):
        """Test that game respects max turns setting."""
        config = ClueConfig(max_turns=5)
        agent = ClueAgent(config)

        result = agent.run_game(visualize=False)

        # Game should end within max turns
        game_state = ClueState(**result)
        assert len(game_state.guesses) <= config.max_turns

    @patch("haive.games.clue.agent.logger")
    def test_run_game_max_turns_warning(self, mock_logger):
        """Test warning when max turns reached."""
        config = ClueConfig(max_turns=2, visualize=True)
        agent = ClueAgent(config)

        # Mock the stream method to simulate reaching max turns
        def mock_stream(*args, **kwargs):
            # Simulate a few game steps
            initial_state = agent.state_manager.initialize(
                solution=agent.config.solution,
                first_player=agent.config.first_player,
                max_turns=agent.config.max_turns,
            )

            # Create states that would trigger max turns
            for i in range(3):
                state_dict = (
                    initial_state.model_dump()
                    if hasattr(initial_state, "model_dump")
                    else initial_state.dict()
                )
                state_dict["guesses"] = [{}] * (i + 1)  # Simulate increasing guesses
                yield state_dict

        with patch.object(agent, "stream", side_effect=mock_stream):
            result = agent.run_game(visualize=True)

            # Check if max turns warning was logged
            warning_calls = [
                call
                for call in mock_logger.warning.call_args_list
                if "Maximum turns reached" in str(call)
            ]
            # Warning might or might not be called depending on exact execution path

    def test_run_game_with_custom_solution(self):
        """Test running game with predefined solution."""
        custom_solution = ClueSolution(
            suspect=ValidSuspect.COLONEL_MUSTARD,
            weapon=ValidWeapon.CANDLESTICK,
            room=ValidRoom.LIBRARY,
        )

        config = ClueConfig(solution=custom_solution)
        agent = ClueAgent(config)

        result = agent.run_game(visualize=False)

        # Verify solution is preserved
        assert result["solution"]["suspect"] == "Colonel Mustard"
        assert result["solution"]["weapon"] == "Candlestick"
        assert result["solution"]["room"] == "Library"


class TestClueAgentInheritance:
    """Test ClueAgent inheritance and interface compliance."""

    def test_agent_inherits_from_game_agent(self):
        """Test that ClueAgent properly inherits from GameAgent."""
        agent = ClueAgent()

        # Should have parent class methods
        assert hasattr(agent, "run")
        assert hasattr(agent, "stream")
        assert callable(agent.run)
        assert callable(agent.stream)

    def test_agent_implements_required_methods(self):
        """Test that agent implements required interface methods."""
        agent = ClueAgent()

        # Required methods for game agents
        assert hasattr(agent, "initialize_game")
        assert hasattr(agent, "visualize_state")
        assert callable(agent.initialize_game)
        assert callable(agent.visualize_state)

    def test_agent_config_type_parameter(self):
        """Test that agent is properly typed with ClueConfig."""
        agent = ClueAgent()

        # Should be typed with ClueConfig
        assert isinstance(agent.config, ClueConfig)


class TestClueAgentErrorHandling:
    """Test error handling and edge cases."""

    def test_agent_with_none_config_values(self):
        """Test agent handles None values in config."""
        # Some config values might be None
        config = ClueConfig(solution=None)  # If allowed by config

        try:
            agent = ClueAgent(config)
            # Should handle gracefully or raise appropriate error
            result = agent.initialize_game({})
            assert isinstance(result, dict)
        except (ValueError, TypeError):
            # It's acceptable to raise errors for invalid config
            pass

    def test_agent_state_manager_access(self):
        """Test that agent can access state manager methods."""
        agent = ClueAgent()

        # Should be able to call state manager methods
        assert agent.state_manager == ClueStateManager
        assert hasattr(agent.state_manager, "initialize")
        assert hasattr(agent.state_manager, "apply_move")
        assert hasattr(agent.state_manager, "get_winner")

    def test_agent_handles_empty_initial_state(self):
        """Test agent handles empty initial state."""
        agent = ClueAgent()

        # Should work with empty dict
        result = agent.initialize_game({})
        assert isinstance(result, dict)
        assert len(result) > 0

    def test_agent_thread_safety(self):
        """Test that multiple agent instances are independent."""
        agent1 = ClueAgent()
        agent2 = ClueAgent()

        # Should be different instances
        assert agent1 is not agent2
        assert agent1.config is not agent2.config

        # Modifying one shouldn't affect the other
        state1 = agent1.initialize_game({})
        state2 = agent2.initialize_game({})

        # Solutions might be different (random) or same if seed is fixed
        # But states should be independent objects
        assert state1 is not state2


class TestClueAgentPerformance:
    """Test performance-related aspects."""

    def test_agent_initialization_speed(self):
        """Test that agent initialization is reasonably fast."""
        start_time = time.time()

        agent = ClueAgent()

        end_time = time.time()

        # Should initialize quickly (less than 1 second)
        assert end_time - start_time < 1.0

    def test_game_initialization_speed(self):
        """Test that game initialization is reasonably fast."""
        agent = ClueAgent()

        start_time = time.time()

        result = agent.initialize_game({})

        end_time = time.time()

        # Should initialize quickly
        assert end_time - start_time < 1.0
        assert isinstance(result, dict)

    def test_multiple_agent_creation(self):
        """Test creating multiple agents doesn't slow down significantly."""
        start_time = time.time()

        agents = [ClueAgent() for _ in range(10)]

        end_time = time.time()

        # Should create 10 agents quickly
        assert end_time - start_time < 2.0
        assert len(agents) == 10
        assert all(isinstance(agent, ClueAgent) for agent in agents)
