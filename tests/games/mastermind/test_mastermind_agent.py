"""Test cases for Mastermind game agent.

This module tests the MastermindAgent class and its methods for
game initialization, move generation, feedback, and visualization.
"""

from unittest.mock import Mock, patch

from langgraph.types import Command
import pytest

from haive.games.mastermind.agent import MastermindAgent, ensure_game_state
from haive.games.mastermind.config import MastermindConfig
from haive.games.mastermind.models import (
    ColorCode,
    MastermindAnalysis,
    MastermindFeedback,
    MastermindGuess,
)
from haive.games.mastermind.state import MastermindState


class TestEnsureGameState:
    """Test cases for ensure_game_state helper function."""

    def test_ensure_game_state_with_mastermind_state(self) -> None:
        """Test ensure_game_state with MastermindState input."""
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )
        result = ensure_game_state(state)

        assert result is state
        assert result.secret_code == ["red", "blue", "green", "yellow"]

    def test_ensure_game_state_with_dict(self) -> None:
        """Test ensure_game_state with dictionary input."""
        state_dict = {
            "secret_code": ["red", "blue", "green", "yellow"],
            "codemaker": "player1",
            "turn": "player2",
            "game_status": "ongoing",
            "guesses": [],
            "feedback": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "max_turns": 10,
            "winner": None,
        }
        result = ensure_game_state(state_dict)

        assert isinstance(result, MastermindState)
        assert result.secret_code == ["red", "blue", "green", "yellow"]
        assert result.codemaker == "player1"

    def test_ensure_game_state_with_command_having_state(self) -> None:
        """Test ensure_game_state with Command containing state."""
        inner_state = MastermindState(
            secret_code=["purple", "orange", "red", "blue"],
            codemaker="player2",
            turn="player1",
            game_status="ongoing",
        )
        command = Mock()
        command.state = inner_state

        result = ensure_game_state(command)

        assert result is inner_state

    def test_ensure_game_state_with_command_no_state(self) -> None:
        """Test ensure_game_state with Command without state."""
        command = Mock()
        delattr(command, "state")  # Remove state attribute

        result = ensure_game_state(command)

        # Should return default initialized state
        assert isinstance(result, MastermindState)
        assert result.codemaker == "player1"  # Default codemaker

    def test_ensure_game_state_with_invalid_dict(self) -> None:
        """Test ensure_game_state with invalid dictionary."""
        invalid_dict = {"invalid": "data"}

        result = ensure_game_state(invalid_dict)

        # Should return default initialized state as fallback
        assert isinstance(result, MastermindState)
        assert result.codemaker == "player1"

    def test_ensure_game_state_with_invalid_type(self) -> None:
        """Test ensure_game_state with invalid input type."""
        invalid_input = "invalid string"

        result = ensure_game_state(invalid_input)

        # Should return default initialized state as fallback
        assert isinstance(result, MastermindState)
        assert result.codemaker == "player1"


class TestMastermindAgentInitialization:
    """Test cases for MastermindAgent initialization."""

    def test_mastermind_agent_default_config(self) -> None:
        """Test creating MastermindAgent with default config."""
        agent = MastermindAgent()

        assert isinstance(agent.config, MastermindConfig)
        assert agent.config.codemaker == "player1"
        assert agent.config.max_turns == 10
        assert agent.config.enable_analysis is True
        assert len(agent.config.colors) == 6

    def test_mastermind_agent_custom_config(self) -> None:
        """Test creating MastermindAgent with custom config."""
        custom_config = MastermindConfig(
            codemaker="player2",
            max_turns=15,
            enable_analysis=False,
            colors=["red", "blue", "green", "yellow"],
        )
        agent = MastermindAgent(custom_config)

        assert agent.config.codemaker == "player2"
        assert agent.config.max_turns == 15
        assert agent.config.enable_analysis is False
        assert len(agent.config.colors) == 4

    @patch("haive.games.mastermind.agent.UI_AVAILABLE", True)
    @patch("haive.games.mastermind.agent.MastermindUI")
    def test_mastermind_agent_with_ui(self, mock_ui_class) -> None:
        """Test creating MastermindAgent when UI is available."""
        mock_ui_instance = Mock()
        mock_ui_class.return_value = mock_ui_instance

        agent = MastermindAgent()

        assert agent.ui is mock_ui_instance
        mock_ui_class.assert_called_once()

    @patch("haive.games.mastermind.agent.UI_AVAILABLE", False)
    def test_mastermind_agent_without_ui(self) -> None:
        """Test creating MastermindAgent when UI is not available."""
        agent = MastermindAgent()

        assert agent.ui is None

    @patch("haive.games.mastermind.agent.Console")
    def test_mastermind_agent_console_creation(self, mock_console_class) -> None:
        """Test that Console is created for the agent."""
        mock_console = Mock()
        mock_console_class.return_value = mock_console

        agent = MastermindAgent()

        assert agent.console is mock_console
        mock_console_class.assert_called_once()


class TestMastermindAgentGameInitialization:
    """Test cases for MastermindAgent game initialization."""

    def test_initialize_game_default(self) -> None:
        """Test initializing game with default settings."""
        agent = MastermindAgent()

        with patch.object(
            agent,
            "_generate_secret_code",
            return_value=["red", "blue", "green", "yellow"],
        ):
            command = agent.initialize_game({})

            assert isinstance(command, Command)
            assert hasattr(command, "update")

            updated_state = MastermindState(**command.update)
            assert updated_state.secret_code == ["red", "blue", "green", "yellow"]
            assert updated_state.codemaker == "player1"
            assert updated_state.turn == "player2"

    def test_initialize_game_with_predetermined_code(self) -> None:
        """Test initializing game with predetermined secret code."""
        config = MastermindConfig(secret_code=["purple", "orange", "red", "blue"])
        agent = MastermindAgent(config)

        command = agent.initialize_game({})

        updated_state = MastermindState(**command.update)
        assert updated_state.secret_code == ["purple", "orange", "red", "blue"]

    def test_initialize_game_player2_codemaker(self) -> None:
        """Test initializing game with player2 as codemaker."""
        config = MastermindConfig(codemaker="player2")
        agent = MastermindAgent(config)

        with patch.object(
            agent, "_generate_secret_code", return_value=["red", "red", "red", "red"]
        ):
            command = agent.initialize_game({})

            updated_state = MastermindState(**command.update)
            assert updated_state.codemaker == "player2"
            assert updated_state.turn == "player1"


class TestMastermindAgentSecretCodeGeneration:
    """Test cases for secret code generation."""

    def test_generate_secret_code_from_engine(self) -> None:
        """Test generating secret code from LLM engine."""
        agent = MastermindAgent()

        # Mock the engine response
        mock_engine = Mock()
        mock_engine.invoke.return_value = ColorCode(
            code=["red", "blue", "green", "yellow"]
        )
        agent.engines = {"codemaker": mock_engine}

        code = agent._generate_secret_code()

        assert code == ["red", "blue", "green", "yellow"]
        mock_engine.invoke.assert_called_once()

    def test_generate_secret_code_fallback_to_random(self) -> None:
        """Test fallback to random code when engine fails."""
        agent = MastermindAgent()

        # Mock the engine to raise exception
        mock_engine = Mock()
        mock_engine.invoke.side_effect = Exception("Engine error")
        agent.engines = {"codemaker": mock_engine}

        code = agent._generate_secret_code()

        assert len(code) == 4
        assert all(color in agent.config.colors for color in code)

    def test_generate_secret_code_invalid_response(self) -> None:
        """Test handling invalid engine response."""
        agent = MastermindAgent()

        # Mock the engine with invalid response
        mock_engine = Mock()
        mock_engine.invoke.return_value = "invalid response"
        agent.engines = {"codemaker": mock_engine}

        code = agent._generate_secret_code()

        # Should fall back to random
        assert len(code) == 4
        assert all(color in agent.config.colors for color in code)


class TestMastermindAgentMoveGeneration:
    """Test cases for move generation."""

    def test_make_guess_player2(self) -> None:
        """Test making a guess as player2 (codebreaker)."""
        agent = MastermindAgent()
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        # Mock the engine
        mock_engine = Mock()
        expected_guess = MastermindGuess(
            colors=["purple", "orange", "red", "blue"], player="player2"
        )
        mock_engine.invoke.return_value = expected_guess
        agent.engines = {"player2_guesser": mock_engine}

        command = agent.make_guess(state, "player2")

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_make_guess_player1_as_codebreaker(self) -> None:
        """Test making a guess as player1 when they are codebreaker."""
        config = MastermindConfig(codemaker="player2")
        agent = MastermindAgent(config)
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player2",
            turn="player1",
            game_status="ongoing",
        )

        # Mock the engine
        mock_engine = Mock()
        expected_guess = MastermindGuess(
            colors=["red", "red", "blue", "blue"], player="player1"
        )
        mock_engine.invoke.return_value = expected_guess
        agent.engines = {"player1_guesser": mock_engine}

        command = agent.make_guess(state, "player1")

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_extract_move_mastermind_guess(self) -> None:
        """Test extracting move when response is MastermindGuess."""
        agent = MastermindAgent()
        guess = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )

        result = agent.extract_move(guess)

        assert result == guess

    def test_extract_move_dict_response(self) -> None:
        """Test extracting move from dictionary response."""
        agent = MastermindAgent()
        response = {"colors": ["red", "blue", "green", "yellow"]}

        result = agent.extract_move(response)

        assert isinstance(result, MastermindGuess)
        assert result.colors == ["red", "blue", "green", "yellow"]
        assert result.player == "player2"  # Default

    def test_extract_move_list_response(self) -> None:
        """Test extracting move from list response."""
        agent = MastermindAgent()
        response = ["red", "blue", "green", "yellow"]

        result = agent.extract_move(response)

        assert isinstance(result, MastermindGuess)
        assert result.colors == ["red", "blue", "green", "yellow"]

    def test_extract_move_invalid_response(self) -> None:
        """Test extracting move from invalid response."""
        agent = MastermindAgent()

        with pytest.raises(ValueError, match="Could not extract guess"):
            agent.extract_move("invalid response")


class TestMastermindAgentFeedback:
    """Test cases for feedback provision."""

    def test_provide_feedback_correct_guess(self) -> None:
        """Test providing feedback for correct guess."""
        agent = MastermindAgent()
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["red", "blue", "green", "yellow"], player="player2"
                )
            ],
        )

        command = agent.provide_feedback(state)

        assert isinstance(command, Command)
        updated_state = MastermindState(**command.update)
        assert len(updated_state.feedback) == 1
        assert updated_state.feedback[0].correct_position == 4
        assert updated_state.game_status == "player2_win"

    def test_provide_feedback_partial_match(self) -> None:
        """Test providing feedback for partial match."""
        agent = MastermindAgent()
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(
                    colors=["red", "green", "blue", "purple"], player="player2"
                )
            ],
        )

        command = agent.provide_feedback(state)

        updated_state = MastermindState(**command.update)
        assert updated_state.feedback[0].correct_position == 1  # red
        assert updated_state.feedback[0].correct_color == 2  # blue and green


class TestMastermindAgentAnalysis:
    """Test cases for analysis functionality."""

    def test_analyze_position_enabled(self) -> None:
        """Test analyzing position when analysis is enabled."""
        agent = MastermindAgent()
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(colors=["red", "red", "red", "red"], player="player2")
            ],
            feedback=[MastermindFeedback(correct_position=1, correct_color=0)],
        )

        # Mock the analyzer engine
        mock_engine = Mock()
        expected_analysis = MastermindAnalysis(
            possible_combinations=200,
            high_probability_colors=["blue", "green"],
            strategy="Explore other colors",
            reasoning="Red appears once",
            confidence=5,
        )
        mock_engine.invoke.return_value = expected_analysis
        agent.engines = {"player2_analyzer": mock_engine}

        command = agent.analyze_position(state, "player2")

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_analyze_position_disabled(self) -> None:
        """Test analyzing position when analysis is disabled."""
        config = MastermindConfig(enable_analysis=False)
        agent = MastermindAgent(config)
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
        )

        command = agent.analyze_position(state, "player2")

        assert isinstance(command, Command)
        # Should return state unchanged
        updated_state = MastermindState(**command.update)
        assert updated_state.player2_analysis == []

    def test_prepare_analysis_context(self) -> None:
        """Test preparing analysis context."""
        agent = MastermindAgent()
        state = MastermindState(
            secret_code=["red", "blue", "green", "yellow"],
            codemaker="player1",
            turn="player2",
            game_status="ongoing",
            guesses=[
                MastermindGuess(colors=["red", "red", "red", "red"], player="player2"),
                MastermindGuess(
                    colors=["blue", "blue", "blue", "blue"], player="player2"
                ),
            ],
            feedback=[
                MastermindFeedback(correct_position=1, correct_color=0),
                MastermindFeedback(correct_position=1, correct_color=0),
            ],
        )

        context = agent.prepare_analysis_context(state, "player2")

        assert context["player"] == "player2"
        assert len(context["guesses"]) == 2
        assert len(context["feedback"]) == 2
        assert "board_string" in context
        assert context["remaining_turns"] == 8


class TestMastermindAgentVisualization:
    """Test cases for visualization methods."""

    def test_visualize_state_with_ui(self) -> None:
        """Test visualizing state with UI available."""
        agent = MastermindAgent()
        mock_ui = Mock()
        agent.ui = mock_ui

        state_dict = {
            "secret_code": ["red", "blue", "green", "yellow"],
            "codemaker": "player1",
            "turn": "player2",
            "game_status": "ongoing",
            "guesses": [],
            "feedback": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "max_turns": 10,
            "winner": None,
        }

        agent.visualize_state(state_dict)

        mock_ui.display_game_state.assert_called_once()

    def test_visualize_state_without_ui(self) -> None:
        """Test visualizing state without UI (fallback to logging)."""
        agent = MastermindAgent()
        agent.ui = None

        state_dict = {
            "secret_code": ["red", "blue", "green", "yellow"],
            "codemaker": "player1",
            "turn": "player2",
            "game_status": "ongoing",
            "guesses": [],
            "feedback": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "max_turns": 10,
            "winner": None,
        }

        with patch("haive.games.mastermind.agent.logger") as mock_logger:
            agent.visualize_state(state_dict)

            # Should have logged game information
            assert mock_logger.info.called
            info_calls = [call[0][0] for call in mock_logger.info.call_args_list]
            assert any("Game: Mastermind" in call for call in info_calls)

    def test_visualize_state_with_error(self) -> None:
        """Test handling errors during visualization."""
        agent = MastermindAgent()
        invalid_state = {"invalid": "state"}

        with patch("haive.games.mastermind.agent.logger") as mock_logger:
            agent.visualize_state(invalid_state)

            # Should log error
            mock_logger.error.assert_called()


class TestMastermindAgentWorkflowSetup:
    """Test cases for workflow setup."""

    def test_setup_workflow_nodes(self) -> None:
        """Test that workflow setup creates expected nodes."""
        agent = MastermindAgent()

        with patch("haive.games.mastermind.agent.DynamicGraph") as mock_graph_class:
            mock_builder = Mock()
            mock_graph_class.return_value = mock_builder
            mock_builder.build.return_value = Mock()

            agent.setup_workflow()

            # Check that required nodes were added
            expected_nodes = [
                "initialize",
                "player1_guess",
                "player2_guess",
                "provide_feedback",
                "analyze_player1",
                "analyze_player2",
            ]

            add_node_calls = mock_builder.add_node.call_args_list
            added_node_names = [call[0][0] for call in add_node_calls]

            for expected_node in expected_nodes:
                assert expected_node in added_node_names

    def test_setup_workflow_edges(self) -> None:
        """Test that workflow setup creates expected edges."""
        agent = MastermindAgent()

        with patch("haive.games.mastermind.agent.DynamicGraph") as mock_graph_class:
            mock_builder = Mock()
            mock_graph_class.return_value = mock_builder
            mock_builder.build.return_value = Mock()

            agent.setup_workflow()

            # Check that edges were added
            mock_builder.add_edge.assert_called()
            mock_builder.add_conditional_edges.assert_called()
            assert mock_builder.build.called
            assert hasattr(agent, "graph")


class TestMastermindAgentIntegration:
    """Integration test cases for MastermindAgent."""

    def test_complete_agent_workflow(self) -> None:
        """Test complete agent workflow with mocked engines."""
        config = MastermindConfig(
            secret_code=["red", "blue", "green", "yellow"],
            max_turns=3,
            enable_analysis=False,
        )
        agent = MastermindAgent(config)

        # Mock engines
        mock_guesser = Mock()

        # Set up guess sequence
        guess1 = MastermindGuess(colors=["red", "red", "red", "red"], player="player2")
        guess2 = MastermindGuess(
            colors=["blue", "blue", "blue", "blue"], player="player2"
        )
        guess3 = MastermindGuess(
            colors=["red", "blue", "green", "yellow"], player="player2"
        )

        mock_guesser.invoke.side_effect = [guess1, guess2, guess3]

        agent.engines = {"player2_guesser": mock_guesser}

        # Initialize
        init_command = agent.initialize_game({})
        state = MastermindState(**init_command.update)

        # First guess and feedback
        guess_command = agent.make_guess(state, "player2")
        state = MastermindState(**guess_command.update)
        feedback_command = agent.provide_feedback(state)
        state = MastermindState(**feedback_command.update)

        assert state.feedback[0].correct_position == 1
        assert state.feedback[0].correct_color == 0

        # Second guess and feedback
        guess_command = agent.make_guess(state, "player2")
        state = MastermindState(**guess_command.update)
        feedback_command = agent.provide_feedback(state)
        state = MastermindState(**feedback_command.update)

        assert state.feedback[1].correct_position == 1
        assert state.feedback[1].correct_color == 0

        # Third guess - winning
        guess_command = agent.make_guess(state, "player2")
        state = MastermindState(**guess_command.update)
        feedback_command = agent.provide_feedback(state)
        final_state = MastermindState(**feedback_command.update)

        assert final_state.feedback[2].correct_position == 4
        assert final_state.feedback[2].correct_color == 0
        assert final_state.game_status == "player2_win"
        assert final_state.winner == "player2"
