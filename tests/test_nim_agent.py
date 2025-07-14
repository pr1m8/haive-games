"""Test cases for Nim game agent.

This module tests the NimAgent class and its methods for
game initialization, move generation, analysis, and visualization.
"""

from unittest.mock import Mock, patch

from langgraph.types import Command

from haive.games.nim.agent import NimAgent, ensure_game_state
from haive.games.nim.config import NimConfig
from haive.games.nim.models import NimAnalysis, NimMove
from haive.games.nim.state import NimState


class TestEnsureGameState:
    """Test cases for ensure_game_state helper function."""

    def test_ensure_game_state_with_nim_state(self) -> None:
        """Test ensure_game_state with NimState input."""
        state = NimState(piles=[3, 5, 7])
        result = ensure_game_state(state)

        assert result is state
        assert result.piles == [3, 5, 7]

    def test_ensure_game_state_with_dict(self) -> None:
        """Test ensure_game_state with dictionary input."""
        state_dict = {
            "piles": [1, 2, 3],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "misere_mode": False,
        }
        result = ensure_game_state(state_dict)

        assert isinstance(result, NimState)
        assert result.piles == [1, 2, 3]
        assert result.turn == "player1"

    def test_ensure_game_state_with_command_having_state(self) -> None:
        """Test ensure_game_state with Command containing state."""
        inner_state = NimState(piles=[2, 4])
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
        assert isinstance(result, NimState)
        assert result.piles == [3, 5, 7]  # Default pile sizes

    def test_ensure_game_state_with_invalid_dict(self) -> None:
        """Test ensure_game_state with invalid dictionary."""
        invalid_dict = {"invalid": "data"}

        result = ensure_game_state(invalid_dict)

        # Should return default initialized state as fallback
        assert isinstance(result, NimState)
        assert result.piles == [3, 5, 7]

    def test_ensure_game_state_with_invalid_type(self) -> None:
        """Test ensure_game_state with invalid input type."""
        invalid_input = "invalid string"

        result = ensure_game_state(invalid_input)

        # Should return default initialized state as fallback
        assert isinstance(result, NimState)
        assert result.piles == [3, 5, 7]


class TestNimAgentInitialization:
    """Test cases for NimAgent initialization."""

    def test_nim_agent_default_config(self) -> None:
        """Test creating NimAgent with default config."""
        agent = NimAgent()

        assert isinstance(agent.config, NimConfig)
        assert agent.config.pile_sizes == [3, 5, 7]
        assert agent.config.misere_mode is False
        assert agent.config.enable_analysis is True

    def test_nim_agent_custom_config(self) -> None:
        """Test creating NimAgent with custom config."""
        custom_config = NimConfig(
            pile_sizes=[1, 2, 3, 4], misere_mode=True, enable_analysis=False
        )
        agent = NimAgent(custom_config)

        assert agent.config.pile_sizes == [1, 2, 3, 4]
        assert agent.config.misere_mode is True
        assert agent.config.enable_analysis is False

    @patch("haive.games.nim.agent.RICH_AVAILABLE", True)
    @patch("haive.games.nim.agent.NimUI")
    def test_nim_agent_with_rich_ui(self, mock_ui_class) -> None:
        """Test creating NimAgent when Rich UI is available."""
        mock_ui_instance = Mock()
        mock_ui_class.return_value = mock_ui_instance

        agent = NimAgent()

        assert agent.ui is mock_ui_instance
        mock_ui_class.assert_called_once()

    @patch("haive.games.nim.agent.RICH_AVAILABLE", False)
    def test_nim_agent_without_rich_ui(self) -> None:
        """Test creating NimAgent when Rich UI is not available."""
        agent = NimAgent()

        assert agent.ui is None


class TestNimAgentGameInitialization:
    """Test cases for NimAgent game initialization."""

    def test_initialize_game_with_dict(self) -> None:
        """Test initializing game with dictionary state."""
        agent = NimAgent()
        state_dict = {"some": "data"}

        command = agent.initialize_game(state_dict)

        assert isinstance(command, Command)
        assert hasattr(command, "update")

        # Verify the state was initialized with config settings
        updated_state = NimState(**command.update)
        assert updated_state.piles == [3, 5, 7]  # Default from config
        assert updated_state.misere_mode is False

    def test_initialize_game_with_custom_config(self) -> None:
        """Test initializing game with custom configuration."""
        config = NimConfig(pile_sizes=[1, 2, 3], misere_mode=True)
        agent = NimAgent(config)

        command = agent.initialize_game({})

        updated_state = NimState(**command.update)
        assert updated_state.piles == [1, 2, 3]
        assert updated_state.misere_mode is True

    def test_initialize_game_with_nim_state(self) -> None:
        """Test initializing game with NimState input."""
        agent = NimAgent()
        existing_state = NimState(piles=[5, 5])

        command = agent.initialize_game(existing_state)

        # Should initialize fresh state with config, not use existing
        updated_state = NimState(**command.update)
        assert updated_state.piles == [3, 5, 7]  # From config, not input


class TestNimAgentMoveContext:
    """Test cases for NimAgent move context preparation."""

    def test_prepare_move_context_basic(self) -> None:
        """Test preparing move context with basic state."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7], turn="player1")

        context = agent.prepare_move_context(state, "player1")

        assert context["player"] == "player1"
        assert context["misere_mode"] is False
        assert "board_string" in context
        assert "legal_moves" in context
        assert "move_history" in context

    def test_prepare_move_context_with_move_history(self) -> None:
        """Test preparing move context with move history."""
        agent = NimAgent()
        move1 = NimMove(pile_index=0, stones_taken=1)
        move2 = NimMove(pile_index=1, stones_taken=2)
        state = NimState(piles=[2, 3, 7], turn="player2", move_history=[move1, move2])

        context = agent.prepare_move_context(state, "player2")

        assert context["player"] == "player2"
        move_history_str = context["move_history"]
        assert "Take 1 stones from pile 0" in move_history_str
        assert "Take 2 stones from pile 1" in move_history_str

    def test_prepare_move_context_legal_moves_format(self) -> None:
        """Test that legal moves are properly formatted in context."""
        agent = NimAgent()
        state = NimState(piles=[1, 2], turn="player1")

        context = agent.prepare_move_context(state, "player1")

        legal_moves_str = context["legal_moves"]
        assert "Take 1 stones from pile 0 (current size: 1)" in legal_moves_str
        assert "Take 1 stones from pile 1 (current size: 2)" in legal_moves_str
        assert "Take 2 stones from pile 1 (current size: 2)" in legal_moves_str

    def test_prepare_move_context_long_history(self) -> None:
        """Test preparing context with long move history (should be truncated)."""
        agent = NimAgent()
        moves = [NimMove(pile_index=0, stones_taken=1) for _ in range(10)]
        state = NimState(piles=[3, 5, 7], move_history=moves)

        context = agent.prepare_move_context(state, "player1")

        # Should only include last 5 moves
        move_history_lines = context["move_history"].split("\n")
        # Filter out empty lines
        move_history_lines = [line for line in move_history_lines if line.strip()]
        assert len(move_history_lines) <= 5


class TestNimAgentMoveGeneration:
    """Test cases for NimAgent move generation."""

    def test_extract_move(self) -> None:
        """Test extracting move from engine response."""
        agent = NimAgent()
        move = NimMove(pile_index=1, stones_taken=3)

        extracted = agent.extract_move(move)

        assert extracted is move

    def test_make_player1_move(self) -> None:
        """Test making move for player1."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7], turn="player1")

        # Mock the engine
        mock_engine = Mock()
        expected_move = NimMove(pile_index=1, stones_taken=2)
        mock_engine.invoke.return_value = expected_move
        agent.engines = {"player1_player": mock_engine}

        command = agent.make_player1_move(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_make_player2_move(self) -> None:
        """Test making move for player2."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7], turn="player2")

        # Mock the engine
        mock_engine = Mock()
        expected_move = NimMove(pile_index=0, stones_taken=1)
        mock_engine.invoke.return_value = expected_move
        agent.engines = {"player2_player": mock_engine}

        command = agent.make_player2_move(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_make_move_wrong_turn_warning(self) -> None:
        """Test making move when it's not the player's turn generates warning."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7], turn="player1")  # Player1's turn

        mock_engine = Mock()
        mock_engine.invoke.return_value = NimMove(pile_index=0, stones_taken=1)
        agent.engines = {"player2_player": mock_engine}

        with patch("haive.games.nim.agent.logger") as mock_logger:
            agent.make_move(state, "player2")  # Try player2 move

            mock_logger.warning.assert_called_once_with(
                "Not player2's turn, but was asked to make a move"
            )

    def test_make_move_with_dict_state(self) -> None:
        """Test making move with dictionary state input."""
        agent = NimAgent()
        state_dict = {
            "piles": [3, 5, 7],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "misere_mode": False,
        }

        mock_engine = Mock()
        mock_engine.invoke.return_value = NimMove(pile_index=1, stones_taken=2)
        agent.engines = {"player1_player": mock_engine}

        command = agent.make_move(state_dict, "player1")

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()


class TestNimAgentAnalysis:
    """Test cases for NimAgent analysis functionality."""

    def test_prepare_analysis_context(self) -> None:
        """Test preparing analysis context."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7], turn="player1")

        context = agent.prepare_analysis_context(state, "player1")

        assert context["player"] == "player1"
        assert context["misere_mode"] is False
        assert context["nim_sum"] == state.nim_sum
        assert "board_string" in context
        assert "move_history" in context

    def test_analyze_player1(self) -> None:
        """Test analyzing position for player1."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7])

        # Mock the analyzer engine
        mock_engine = Mock()
        expected_analysis = NimAnalysis(
            nim_sum=1,
            position_evaluation="winning",
            recommended_move=NimMove(pile_index=0, stones_taken=1),
            explanation="Test analysis",
        )
        mock_engine.invoke.return_value = expected_analysis
        agent.engines = {"player1_analyzer": mock_engine}

        command = agent.analyze_player1(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_analyze_player2(self) -> None:
        """Test analyzing position for player2."""
        agent = NimAgent()
        state = NimState(piles=[3, 5, 7])

        # Mock the analyzer engine
        mock_engine = Mock()
        expected_analysis = NimAnalysis(
            nim_sum=1,
            position_evaluation="losing",
            recommended_move=NimMove(pile_index=1, stones_taken=3),
            explanation="Test analysis for player2",
        )
        mock_engine.invoke.return_value = expected_analysis
        agent.engines = {"player2_analyzer": mock_engine}

        command = agent.analyze_player2(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_analyze_position_disabled(self) -> None:
        """Test analyzing position when analysis is disabled."""
        config = NimConfig(enable_analysis=False)
        agent = NimAgent(config)
        state = NimState(piles=[3, 5, 7])

        command = agent.analyze_position(state, "player1")

        assert isinstance(command, Command)
        # Should return state unchanged when analysis is disabled
        updated_state = NimState(**command.update)
        assert updated_state.piles == state.piles

    def test_analyze_position_with_dict_state(self) -> None:
        """Test analyzing position with dictionary state input."""
        agent = NimAgent()
        state_dict = {
            "piles": [3, 5, 7],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "misere_mode": False,
        }

        mock_engine = Mock()
        mock_analysis = NimAnalysis(
            nim_sum=1,
            position_evaluation="winning",
            recommended_move=NimMove(pile_index=0, stones_taken=1),
            explanation="Test",
        )
        mock_engine.invoke.return_value = mock_analysis
        agent.engines = {"player1_analyzer": mock_engine}

        command = agent.analyze_position(state_dict, "player1")

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()


class TestNimAgentVisualization:
    """Test cases for NimAgent visualization methods."""

    def test_visualize_state_without_rich(self) -> None:
        """Test visualizing state without Rich UI."""
        agent = NimAgent()
        agent.ui = None  # No Rich UI

        state_dict = {
            "piles": [2, 3, 1],
            "turn": "player2",
            "game_status": "in_progress",
            "move_history": [{"pile_index": 0, "stones_taken": 1}],
            "player1_analysis": [],
            "player2_analysis": [],
            "misere_mode": False,
        }

        with patch("builtins.print") as mock_print, patch("time.sleep"):
            agent.visualize_state(state_dict)

            # Should have printed game information
            mock_print.assert_called()
            print_calls = [call[0][0] for call in mock_print.call_args_list]
            game_info_printed = any(
                "Current Player: player2" in call for call in print_calls
            )
            assert game_info_printed

    @patch("haive.games.nim.agent.RICH_AVAILABLE", True)
    def test_visualize_state_with_rich(self) -> None:
        """Test visualizing state with Rich UI."""
        agent = NimAgent()
        mock_ui = Mock()
        agent.ui = mock_ui

        state_dict = {
            "piles": [2, 3, 1],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "misere_mode": True,
        }

        with patch("time.sleep"):
            agent.visualize_state(state_dict)

            mock_ui.display_game_state.assert_called_once_with(state_dict)

    def test_visualize_state_with_analysis(self) -> None:
        """Test visualizing state with player analysis."""
        agent = NimAgent()
        agent.ui = None

        analysis_data = {
            "nim_sum": 3,
            "position_evaluation": "winning",
            "recommended_move": {"pile_index": 1, "stones_taken": 2},
            "explanation": "Take 2 from pile 1 to win",
        }

        state_dict = {
            "piles": [1, 3, 2],
            "turn": "player2",  # Show player1's analysis
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [analysis_data],
            "player2_analysis": [],
            "misere_mode": False,
        }

        with patch("builtins.print") as mock_print, patch("time.sleep"):
            agent.visualize_state(state_dict)

            print_calls = [call[0][0] for call in mock_print.call_args_list]
            analysis_printed = any(
                "Player 1's Analysis" in call for call in print_calls
            )
            assert analysis_printed


class TestNimAgentGameExecution:
    """Test cases for NimAgent game execution methods."""

    def test_run_game_without_visualization(self) -> None:
        """Test running game without visualization."""
        agent = NimAgent()

        # Mock the superclass run method
        expected_result = {"final": "state"}
        with patch.object(
            agent.__class__.__bases__[0], "run", return_value=expected_result
        ):
            result = agent.run_game(visualize=False)

            assert result == expected_result

    def test_run_game_with_visualization(self) -> None:
        """Test running game with visualization."""
        agent = NimAgent()

        # Mock the stream method to return a sequence of states
        mock_states = [
            {"step": 1, "piles": [3, 5, 7]},
            {"step": 2, "piles": [2, 5, 7]},
            {"step": 3, "piles": [0, 0, 0]},
        ]

        with patch.object(
            agent, "stream", return_value=iter(mock_states)
        ), patch.object(agent, "visualize_state") as mock_visualize:

            result = agent.run_game(visualize=True)

            # Should have visualized each state
            assert mock_visualize.call_count == 3
            assert result == mock_states[-1]  # Should return final state

    @patch("haive.games.nim.agent.RICH_AVAILABLE", True)
    def test_run_game_with_ui(self) -> None:
        """Test running game with Rich UI."""
        agent = NimAgent()
        mock_ui = Mock()
        agent.ui = mock_ui

        mock_states = [{"step": 1, "piles": [1, 2]}, {"step": 2, "piles": [0, 0]}]

        with patch.object(agent, "stream", return_value=iter(mock_states)):
            result = agent.run_game_with_ui(show_analysis=True)

            assert result == mock_states[-1]
            assert agent.config.enable_analysis  # Should be restored

    @patch("haive.games.nim.agent.RICH_AVAILABLE", False)
    def test_run_game_with_ui_fallback(self) -> None:
        """Test running game with UI when Rich is not available."""
        agent = NimAgent()

        with patch.object(agent, "run_game") as mock_run_game:
            agent.run_game_with_ui()

            mock_run_game.assert_called_once_with(visualize=True)

    def test_run_game_with_ui_analysis_setting_restoration(self) -> None:
        """Test that analysis setting is properly restored after UI game."""
        config = NimConfig(enable_analysis=False)
        agent = NimAgent(config)

        mock_states = [{"final": "state"}]

        with patch("haive.games.nim.agent.RICH_AVAILABLE", True), patch.object(
            agent, "stream", return_value=iter(mock_states)
        ):

            # Run with analysis enabled
            agent.run_game_with_ui(show_analysis=True)

            # Should be restored to original setting
            assert agent.config.enable_analysis is False


class TestNimAgentWorkflowSetup:
    """Test cases for NimAgent workflow setup."""

    def test_setup_workflow_nodes(self) -> None:
        """Test that workflow setup creates expected nodes."""
        agent = NimAgent()

        with patch("haive.games.nim.agent.DynamicGraph") as mock_graph_class:
            mock_builder = Mock()
            mock_graph_class.return_value = mock_builder
            mock_builder.build.return_value = Mock()

            agent.setup_workflow()

            # Check that required nodes were added
            expected_nodes = [
                "initialize",
                "player1_move",
                "player2_move",
                "analyze_player1",
                "analyze_player2",
            ]

            add_node_calls = mock_builder.add_node.call_args_list
            added_node_names = [call[0][0] for call in add_node_calls]

            for expected_node in expected_nodes:
                assert expected_node in added_node_names

    def test_setup_workflow_edges(self) -> None:
        """Test that workflow setup creates expected edges."""
        agent = NimAgent()

        with patch("haive.games.nim.agent.DynamicGraph") as mock_graph_class:
            mock_builder = Mock()
            mock_graph_class.return_value = mock_builder
            mock_builder.build.return_value = Mock()

            agent.setup_workflow()

            # Check that edges were added
            mock_builder.add_edge.assert_called()
            assert mock_builder.build.called
            assert hasattr(agent, "graph")


class TestNimAgentIntegration:
    """Integration test cases for NimAgent."""

    def test_complete_agent_workflow(self) -> None:
        """Test complete agent workflow with mocked engines."""
        config = NimConfig(pile_sizes=[1, 1], enable_analysis=False)
        agent = NimAgent(config)

        # Mock engines
        mock_player1_engine = Mock()
        mock_player2_engine = Mock()

        # Set up move sequence
        move1 = NimMove(pile_index=0, stones_taken=1)
        move2 = NimMove(pile_index=1, stones_taken=1)
        mock_player1_engine.invoke.return_value = move1
        mock_player2_engine.invoke.return_value = move2

        agent.engines = {
            "player1_player": mock_player1_engine,
            "player2_player": mock_player2_engine,
        }

        # Initialize and run moves
        init_command = agent.initialize_game({})
        state = NimState(**init_command.update)

        # Player1 move
        move1_command = agent.make_move(state, "player1")
        state = NimState(**move1_command.update)
        assert state.piles == [0, 1]
        assert state.turn == "player2"

        # Player2 move (should win the game)
        move2_command = agent.make_move(state, "player2")
        final_state = NimState(**move2_command.update)
        assert final_state.piles == [0, 0]
        assert final_state.game_status == "player2_win"  # Player2 wins in standard mode
