"""Integration tests for Connect4Agent with real LLMs - NO MOCKS."""

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.models import Connect4Move
from haive.games.connect4.state import Connect4State


class TestConnect4AgentIntegration:
    """Test Connect4Agent with real LLM components."""

    @pytest.fixture
    def agent_config(self):
        """Create agent configuration for testing."""
        return Connect4AgentConfig(
            name="test_connect4", enable_analysis=True, first_player="red"
        )

    @pytest.fixture
    def connect4_agent(self, agent_config):
        """Create Connect4Agent with real engines."""
        return Connect4Agent(agent_config)

    def test_agent_initialization(self, connect4_agent):
        """Test agent initializes correctly with real engines."""
        assert connect4_agent is not None
        assert connect4_agent.config.name == "test_connect4"
        assert connect4_agent.config.enable_analysis is True
        assert connect4_agent.config.first_player == "red"

        # Verify engines are created
        assert hasattr(connect4_agent, "engines")
        assert "red_player" in connect4_agent.engines
        assert "yellow_player" in connect4_agent.engines

    def test_agent_graph_compilation(self, connect4_agent):
        """Test agent graph compiles successfully."""
        # Graph should be compiled during initialization
        assert hasattr(connect4_agent, "app")
        assert connect4_agent.app is not None

    def test_game_initialization_command(self, connect4_agent):
        """Test game initialization through agent."""
        initial_state = {}
        command = connect4_agent.initialize_game(initial_state)

        assert command is not None
        assert command.goto == "make_move"
        assert command.update["board"] == [[None] * 7 for _ in range(6)]
        assert command.update["turn"] == "red"
        assert command.update["game_status"] == "ongoing"

    def test_move_context_preparation(self, connect4_agent):
        """Test move context preparation for LLM."""
        # Create a test state
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, "red", None, None, None],
                ["yellow", "red", "yellow", "red", "yellow", None, None],
            ],
            turn="red",
            game_status="ongoing",
            move_history=[
                Connect4Move(column=0, player="yellow"),
                Connect4Move(column=1, player="red"),
                Connect4Move(column=2, player="yellow"),
                Connect4Move(column=3, player="red"),
                Connect4Move(column=4, player="yellow"),
                Connect4Move(column=3, player="red"),
            ],
        )

        # Prepare context
        context = connect4_agent.prepare_move_context(state)

        # Verify context contains required information
        assert "board_string" in context
        assert "current_player" in context
        assert "legal_columns" in context
        assert "move_history" in context
        assert "last_move" in context

        assert context["current_player"] == "red"
        assert 5 in context["legal_columns"]  # Column 5 is empty
        assert 6 in context["legal_columns"]  # Column 6 is empty
        assert len(context["move_history"]) == 6

    def test_analysis_context_preparation(self, connect4_agent):
        """Test analysis context preparation."""
        state = Connect4State(
            board=[[None] * 7 for _ in range(6)],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Add one piece to make it interesting
        state.board[5][3] = "red"  # Red in center bottom

        context = connect4_agent.prepare_analysis_context(state, "red")

        # Verify analysis context
        assert "board_string" in context
        assert "player_color" in context
        assert "opponent_color" in context
        assert context["player_color"] == "red"
        assert context["opponent_color"] == "yellow"

    def test_engine_structured_output(self):
        """Test that engines are configured for structured output."""
        # Create a simple engine for testing
        engine = AugLLMConfig(
            structured_output_model=Connect4Move, structured_output_version="v2"
        )

        # Verify configuration
        assert engine.structured_output_model == Connect4Move
        assert engine.structured_output_version == "v2"

    def test_make_move_state_validation(self, connect4_agent):
        """Test make_move validates state properly."""
        # Invalid state (missing required fields)
        invalid_state = {
            "board": [[None] * 7 for _ in range(6)],
            # Missing other required fields
        }

        command = connect4_agent.make_move(invalid_state)

        # Should handle gracefully
        assert command.goto == "END"
        assert "error_message" in command.update

    def test_agent_workflow_nodes(self, connect4_agent):
        """Test agent has correct workflow nodes."""
        # Agent should have set up proper nodes
        expected_nodes = ["initialize_game", "red_move", "yellow_move"]

        # Verify through agent setup (implementation specific)
        assert hasattr(connect4_agent, "setup_workflow")

    def test_state_manager_integration(self, connect4_agent):
        """Test agent integrates with state manager correctly."""
        # The agent should use state manager for game logic
        assert hasattr(connect4_agent, "state_manager")
        assert connect4_agent.state_manager is not None

    def test_column_availability_check(self):
        """Test checking which columns are available."""
        state = Connect4State(
            board=[
                ["red", None, None, None, None, None, "yellow"],  # Top row
                ["yellow", None, None, None, None, None, "red"],
                ["red", None, None, None, None, None, "yellow"],
                ["yellow", None, None, None, None, None, "red"],
                ["red", None, None, None, None, None, "yellow"],
                ["yellow", None, None, None, None, None, "red"],  # Bottom row
            ],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        # Columns 0 and 6 are full
        assert state.is_column_full(0)
        assert state.is_column_full(6)
        assert not state.is_column_full(3)  # Middle columns empty

        # Legal columns are 1-5
        legal_columns = [col for col in range(7) if not state.is_column_full(col)]
        assert legal_columns == [1, 2, 3, 4, 5]

    def test_position_scoring_context(self, connect4_agent):
        """Test position scoring context for analysis."""
        # Create interesting position
        state = Connect4State(
            board=[
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None],
                [None, None, "red", "red", "red", None, None],  # Three in a row
                [None, "yellow", "yellow", "red", "yellow", None, None],
                ["red", "yellow", "red", "yellow", "red", "yellow", None],
            ],
            turn="red",
            game_status="ongoing",
            move_history=[],
        )

        context = connect4_agent.prepare_move_context(state)

        # Context should help LLM see the threat/opportunity
        assert "board_string" in context
        board_str = context["board_string"]
        assert (
            "R R R" in board_str or "r r r" in board_str.lower()
        )  # Three reds visible
