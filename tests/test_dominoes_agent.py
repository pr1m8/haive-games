"""Test cases for Dominoes game agent.

This module tests the DominoesAgent class and its methods for
game initialization, move generation, and visualization.
"""

from unittest.mock import Mock, patch

import pytest
from langgraph.types import Command

from haive.games.dominoes.agent import DominoesAgent
from haive.games.dominoes.config import DominoesConfig
from haive.games.dominoes.models import (
    DominoesAnalysis,
    DominoesPlayerDecision,
    DominoMove,
    DominoTile,
)
from haive.games.dominoes.state import DominoesState


class TestDominoesAgentInitialization:
    """Test cases for DominoesAgent initialization."""

    def test_dominoes_agent_default_config(self) -> None:
        """Test creating DominoesAgent with default config."""
        agent = DominoesAgent()

        assert isinstance(agent.config, DominoesConfig)
        assert agent.config.num_players == 2
        assert agent.config.tiles_per_hand == 7
        assert agent.config.enable_analysis is True

    def test_dominoes_agent_custom_config(self) -> None:
        """Test creating DominoesAgent with custom config."""
        custom_config = DominoesConfig(
            num_players=4, tiles_per_hand=5, enable_analysis=False
        )
        agent = DominoesAgent(custom_config)

        assert agent.config.num_players == 4
        assert agent.config.tiles_per_hand == 5
        assert agent.config.enable_analysis is False

    @patch("haive.games.dominoes.agent.UI_AVAILABLE", True)
    @patch("haive.games.dominoes.agent.DominoesUI")
    def test_dominoes_agent_with_ui(self, mock_ui_class) -> None:
        """Test creating DominoesAgent when UI is available."""
        mock_ui_instance = Mock()
        mock_ui_class.return_value = mock_ui_instance

        agent = DominoesAgent()

        assert agent.ui is mock_ui_instance
        mock_ui_class.assert_called_once()

    @patch("haive.games.dominoes.agent.UI_AVAILABLE", False)
    def test_dominoes_agent_without_ui(self) -> None:
        """Test creating DominoesAgent when UI is not available."""
        agent = DominoesAgent()

        assert agent.ui is None


class TestDominoesAgentGameInitialization:
    """Test cases for DominoesAgent game initialization."""

    def test_initialize_game_default(self) -> None:
        """Test initializing game with default settings."""
        agent = DominoesAgent()

        command = agent.initialize_game({})

        assert isinstance(command, Command)
        assert hasattr(command, "update")

        # Verify the state was initialized correctly
        updated_state = DominoesState(**command.update)
        assert len(updated_state.players) == 2
        assert updated_state.turn == "player1"
        assert updated_state.game_status == "in_progress"

    def test_initialize_game_four_players(self) -> None:
        """Test initializing game with four players."""
        config = DominoesConfig(num_players=4)
        agent = DominoesAgent(config)

        command = agent.initialize_game({})

        updated_state = DominoesState(**command.update)
        assert len(updated_state.players) == 4
        assert all(f"player{i}" in updated_state.players for i in range(1, 5))

    def test_initialize_game_custom_tiles(self) -> None:
        """Test initializing game with custom tiles per hand."""
        config = DominoesConfig(tiles_per_hand=5)
        agent = DominoesAgent(config)

        command = agent.initialize_game({})

        updated_state = DominoesState(**command.update)
        assert all(
            len(updated_state.hands[player]) == 5 for player in updated_state.players
        )


class TestDominoesAgentMoveContext:
    """Test cases for move context preparation."""

    def test_prepare_move_context_empty_board(self) -> None:
        """Test preparing move context with empty board."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5), DominoTile(left=2, right=4)],
                "player2": [],
            },
            board=[],
            boneyard=[DominoTile(left=6, right=6)],
            turn="player1",
            game_status="in_progress",
        )

        context = agent.prepare_move_context(state, "player1")

        assert context["player"] == "player1"
        assert context["board_state"] == "(empty)"
        assert context["open_ends"] == "None"
        assert "hand" in context
        assert context["boneyard_count"] == 1
        assert context["legal_moves"] != ""

    def test_prepare_move_context_with_board(self) -> None:
        """Test preparing move context with tiles on board."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=3)],
                "player2": [DominoTile(left=5, right=6)],
            },
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        context = agent.prepare_move_context(state, "player1")

        assert context["board_state"] == "[3|5]"
        assert context["open_ends"] == "3 and 5"
        assert "[3|3]" in context["hand"]
        legal_moves = context["legal_moves"]
        assert "Play [3|3] on the left" in legal_moves

    def test_prepare_move_context_no_legal_moves(self) -> None:
        """Test preparing context when no legal moves available."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=0, right=1)], "player2": []},
            board=[DominoTile(left=5, right=6)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        context = agent.prepare_move_context(state, "player1")

        assert context["legal_moves"] == "No legal moves - must pass or draw"


class TestDominoesAgentMoveExtraction:
    """Test cases for move extraction from engine responses."""

    def test_extract_move_dominoes_player_decision(self) -> None:
        """Test extracting move from DominoesPlayerDecision."""
        agent = DominoesAgent()

        tile = DominoTile(left=3, right=5)
        move = DominoMove(tile=tile, end="left")
        decision = DominoesPlayerDecision(
            move=move, pass_turn=False, reasoning="Best move"
        )

        result = agent.extract_move(decision)

        assert result == move

    def test_extract_move_pass_decision(self) -> None:
        """Test extracting pass from DominoesPlayerDecision."""
        agent = DominoesAgent()

        decision = DominoesPlayerDecision(
            move=None, pass_turn=True, reasoning="No legal moves"
        )

        result = agent.extract_move(decision)

        assert result == "pass"

    def test_extract_move_domino_move(self) -> None:
        """Test extracting move when response is already DominoMove."""
        agent = DominoesAgent()

        tile = DominoTile(left=2, right=4)
        move = DominoMove(tile=tile, end="right")

        result = agent.extract_move(move)

        assert result == move

    def test_extract_move_string_pass(self) -> None:
        """Test extracting pass from string response."""
        agent = DominoesAgent()

        result = agent.extract_move("pass")

        assert result == "pass"

    def test_extract_move_dict_response(self) -> None:
        """Test extracting move from dictionary response."""
        agent = DominoesAgent()

        response = {
            "move": {"tile": {"left": 3, "right": 5}, "end": "left"},
            "pass_turn": False,
            "reasoning": "Playing double",
        }

        result = agent.extract_move(response)

        assert isinstance(result, DominoMove)
        assert result.tile.left == 3
        assert result.tile.right == 5
        assert result.end == "left"

    def test_extract_move_ai_message_with_tool_calls(self) -> None:
        """Test extracting move from AIMessage with tool calls."""
        agent = DominoesAgent()

        # Mock AIMessage
        mock_message = Mock()
        mock_message.tool_calls = [
            {
                "args": {
                    "move": {"tile": {"left": 1, "right": 1}, "end": "right"},
                    "pass_turn": False,
                    "reasoning": "Double one",
                }
            }
        ]

        result = agent.extract_move(mock_message)

        assert isinstance(result, DominoMove)
        assert result.tile.left == 1
        assert result.tile.right == 1

    def test_extract_move_invalid_response(self) -> None:
        """Test extracting move from invalid response."""
        agent = DominoesAgent()

        with pytest.raises(ValueError, match="Could not extract move"):
            agent.extract_move(12345)  # Invalid type


class TestDominoesAgentMoveGeneration:
    """Test cases for move generation."""

    def test_make_move_player1(self) -> None:
        """Test making a move as player1."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=3, right=5)], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Mock the engine
        mock_engine = Mock()
        expected_decision = DominoesPlayerDecision(
            move=DominoMove(tile=DominoTile(left=3, right=5), end="left"),
            pass_turn=False,
            reasoning="First move",
        )
        mock_engine.invoke.return_value = expected_decision
        agent.engines = {"player1_player": mock_engine}

        command = agent.make_player1_move(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_make_move_player2(self) -> None:
        """Test making a move as player2."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": [DominoTile(left=5, right=6)]},
            board=[DominoTile(left=3, right=5)],
            boneyard=[],
            turn="player2",
            game_status="in_progress",
        )

        # Mock the engine
        mock_engine = Mock()
        expected_decision = DominoesPlayerDecision(
            move=DominoMove(tile=DominoTile(left=5, right=6), end="right"),
            pass_turn=False,
            reasoning="Match 5",
        )
        mock_engine.invoke.return_value = expected_decision
        agent.engines = {"player2_player": mock_engine}

        command = agent.make_player2_move(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_make_pass_move(self) -> None:
        """Test making a pass move."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [DominoTile(left=0, right=1)], "player2": []},
            board=[DominoTile(left=5, right=6)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Mock the engine to return pass
        mock_engine = Mock()
        pass_decision = DominoesPlayerDecision(
            move=None, pass_turn=True, reasoning="No matches"
        )
        mock_engine.invoke.return_value = pass_decision
        agent.engines = {"player1_player": mock_engine}

        command = agent.make_move(state, "player1")

        updated_state = DominoesState(**command.update)
        assert updated_state.move_history[-1] == "pass"
        assert updated_state.turn == "player2"


class TestDominoesAgentAnalysis:
    """Test cases for analysis functionality."""

    def test_analyze_position_enabled(self) -> None:
        """Test analyzing position when analysis is enabled."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [DominoTile(left=3, right=5), DominoTile(left=5, right=5)],
                "player2": [],
            },
            board=[DominoTile(left=2, right=3)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        # Mock the analyzer engine
        mock_engine = Mock()
        expected_analysis = DominoesAnalysis(
            hand_strength=8,
            pip_count_assessment="High",
            open_ends=["2", "3"],
            missing_values=[],
            suggested_strategy="Play [3|5] to control",
            blocking_potential="High",
            reasoning="Strong position",
        )
        mock_engine.invoke.return_value = expected_analysis
        agent.engines = {"player1_analyzer": mock_engine}

        command = agent.analyze_player1(state)

        assert isinstance(command, Command)
        mock_engine.invoke.assert_called_once()

    def test_analyze_position_disabled(self) -> None:
        """Test analyzing position when analysis is disabled."""
        config = DominoesConfig(enable_analysis=False)
        agent = DominoesAgent(config)
        state = DominoesState(
            players=["player1", "player2"],
            hands={"player1": [], "player2": []},
            board=[],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        command = agent.analyze_position(state, "player1")

        # Should return state unchanged
        updated_state = DominoesState(**command.update)
        assert updated_state.player1_analysis == []

    def test_prepare_analysis_context(self) -> None:
        """Test preparing analysis context."""
        agent = DominoesAgent()
        state = DominoesState(
            players=["player1", "player2"],
            hands={
                "player1": [
                    DominoTile(left=6, right=6),
                    DominoTile(left=5, right=6),
                    DominoTile(left=4, right=5),
                ],
                "player2": [DominoTile(left=1, right=2)],
            },
            board=[DominoTile(left=3, right=4)],
            boneyard=[],
            turn="player1",
            game_status="in_progress",
        )

        context = agent.prepare_analysis_context(state, "player1")

        assert context["player"] == "player1"
        assert "[6|6]" in context["hand"]
        assert context["board_state"] == "[3|4]"
        assert context["open_ends"] == "3 and 4"
        assert "player2: 1 tiles" in context["opponent_tiles"]

        # Check pip count
        12 + 11 + 9  # 32
        assert "32 pips" in context["hand"]


class TestDominoesAgentVisualization:
    """Test cases for visualization methods."""

    def test_visualize_state_with_ui(self) -> None:
        """Test visualizing state with UI available."""
        agent = DominoesAgent()
        mock_ui = Mock()
        agent.ui = mock_ui

        state_dict = {
            "players": ["player1", "player2"],
            "hands": {"player1": [{"left": 3, "right": 5}], "player2": []},
            "board": [],
            "boneyard": [],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "winner": None,
        }

        with patch("time.sleep"):  # Skip delay
            agent.visualize_state(state_dict)

        mock_ui.display_game_state.assert_called_once()

    def test_visualize_state_without_ui(self) -> None:
        """Test visualizing state without UI (fallback to logging)."""
        agent = DominoesAgent()
        agent.ui = None

        state_dict = {
            "players": ["player1", "player2"],
            "hands": {
                "player1": [{"left": 3, "right": 5}],
                "player2": [{"left": 2, "right": 4}],
            },
            "board": [{"left": 1, "right": 3}],
            "boneyard": [],
            "turn": "player1",
            "game_status": "in_progress",
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
            "winner": None,
        }

        with patch("haive.games.dominoes.agent.logger") as mock_logger:
            agent.visualize_state(state_dict)

            # Should have logged game information
            assert mock_logger.info.called
            info_calls = [call[0][0] for call in mock_logger.info.call_args_list]
            assert any("Current Player: player1" in str(call) for call in info_calls)
            assert any("[1|3]" in str(call) for call in info_calls)

    def test_visualize_state_with_error(self) -> None:
        """Test handling errors during visualization."""
        agent = DominoesAgent()
        invalid_state = {"invalid": "state"}

        with patch("haive.games.dominoes.agent.logger") as mock_logger:
            agent.visualize_state(invalid_state)

            # Should log error
            mock_logger.error.assert_called()


class TestDominoesAgentWorkflowSetup:
    """Test cases for workflow setup."""

    def test_setup_workflow_nodes(self) -> None:
        """Test that workflow setup creates expected nodes."""
        agent = DominoesAgent()

        with patch("haive.games.dominoes.agent.DynamicGraph") as mock_graph_class:
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

    def test_setup_workflow_four_players(self) -> None:
        """Test workflow setup with four players."""
        config = DominoesConfig(num_players=4)
        agent = DominoesAgent(config)

        with patch("haive.games.dominoes.agent.DynamicGraph") as mock_graph_class:
            mock_builder = Mock()
            mock_graph_class.return_value = mock_builder
            mock_builder.build.return_value = Mock()

            agent.setup_workflow()

            # Should have nodes for all 4 players
            add_node_calls = mock_builder.add_node.call_args_list
            added_node_names = [call[0][0] for call in add_node_calls]

            assert "player3_move" in added_node_names
            assert "player4_move" in added_node_names
            assert "analyze_player3" in added_node_names
            assert "analyze_player4" in added_node_names


class TestDominoesAgentIntegration:
    """Integration test cases for DominoesAgent."""

    def test_complete_agent_workflow(self) -> None:
        """Test complete agent workflow with mocked engines."""
        config = DominoesConfig(
            num_players=2,
            tiles_per_hand=1,  # Simplified for test
            enable_analysis=False,
        )
        agent = DominoesAgent(config)

        # Mock engines
        mock_player1_engine = Mock()
        mock_player2_engine = Mock()

        # Set up move sequence
        move1 = DominoesPlayerDecision(
            move=DominoMove(tile=DominoTile(left=3, right=5), end="left"),
            pass_turn=False,
            reasoning="First move",
        )
        pass_move = DominoesPlayerDecision(
            move=None, pass_turn=True, reasoning="No matches"
        )

        mock_player1_engine.invoke.return_value = move1
        mock_player2_engine.invoke.return_value = pass_move

        agent.engines = {
            "player1_player": mock_player1_engine,
            "player2_player": mock_player2_engine,
        }

        # Initialize with specific tiles
        init_command = agent.initialize_game({})
        state = DominoesState(**init_command.update)

        # Override hands for predictable test
        state.hands = {
            "player1": [DominoTile(left=3, right=5)],
            "player2": [DominoTile(left=1, right=2)],
        }
        state.boneyard = []

        # Player1 move (wins)
        move_command = agent.make_move(state, "player1")
        final_state = DominoesState(**move_command.update)

        assert len(final_state.board) == 1
        assert final_state.board[0].left == 3
        assert final_state.board[0].right == 5
        assert final_state.game_status == "player1_win"
        assert final_state.winner == "player1"
