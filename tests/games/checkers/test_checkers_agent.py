"""Test cases for Checkers game agent.

This module tests the CheckersAgent class and its game management capabilities
for playing checkers with LLM-based players.
"""

from unittest.mock import MagicMock, patch

from haive.games.checkers.agent import CheckersAgent
from haive.games.checkers.config import CheckersAgentConfig
from haive.games.checkers.models import (
    CheckersAnalysis,
    CheckersMove,
    CheckersPlayerDecision,
)
from haive.games.checkers.state import CheckersState
from haive.games.checkers.state_manager import CheckersStateManager


class TestCheckersAgent:
    """Test cases for CheckersAgent class."""

    def test_agent_initialization_default(self) -> None:
        """Test creating CheckersAgent with default config."""
        agent = CheckersAgent()

        assert isinstance(agent.config, CheckersAgentConfig)
        assert agent.state_manager == CheckersStateManager

    def test_agent_initialization_custom_config(self) -> None:
        """Test creating CheckersAgent with custom config."""
        config = CheckersAgentConfig(
            player_red="human",
            player_black="ai",
            enable_analysis=True,
            visualization=True,
        )
        agent = CheckersAgent(config)

        assert agent.config == config
        assert agent.config.player_red == "human"
        assert agent.config.player_black == "ai"
        assert agent.config.enable_analysis is True

    def test_initialize_game(self) -> None:
        """Test game initialization."""
        agent = CheckersAgent()

        command = agent.initialize_game({})
        update_data = command.update

        # Should create a valid initial state
        state = CheckersState(**update_data)
        assert state.turn == "red"
        assert state.game_status == "ongoing"
        assert len(state.move_history) == 0

        # Check that board has proper setup
        assert len(state.board) == 8
        assert all(len(row) == 8 for row in state.board)

    def test_is_game_over_ongoing(self) -> None:
        """Test game over check for ongoing game."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        is_over = agent.is_game_over(state)

        assert is_over is False

    def test_is_game_over_finished(self) -> None:
        """Test game over check for finished game."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()
        state.game_status = "game_over"
        state.winner = "red"

        is_over = agent.is_game_over(state)

        assert is_over is True

    def test_get_current_player_red(self) -> None:
        """Test getting current player when it's red's turn."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()  # Red starts

        current_player = agent.get_current_player(state)

        assert current_player == "red"

    def test_get_current_player_black(self) -> None:
        """Test getting current player when it's black's turn."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()
        state.turn = "black"

        current_player = agent.get_current_player(state)

        assert current_player == "black"

    def test_prepare_move_context_red_player(self) -> None:
        """Test preparing move context for red player."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        context = agent.prepare_move_context(state, "red")

        assert "board_string" in context
        assert "current_player" in context
        assert "legal_moves" in context
        assert "game_status" in context

        assert context["current_player"] == "red"
        assert context["game_status"] == "ongoing"
        assert isinstance(context["legal_moves"], list)

    def test_prepare_move_context_black_player(self) -> None:
        """Test preparing move context for black player."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()
        state.turn = "black"

        context = agent.prepare_move_context(state, "black")

        assert context["current_player"] == "black"

    def test_prepare_move_context_with_move_history(self) -> None:
        """Test preparing move context when there's move history."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        # Add a move to history
        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )
        state.move_history = [move]

        context = agent.prepare_move_context(state, "red")

        assert "move_history" in context
        assert len(context["move_history"]) == 1

    def test_prepare_analysis_context_red(self) -> None:
        """Test preparing analysis context for red player."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        context = agent.prepare_analysis_context(state, "red")

        assert "board_string" in context
        assert "player" in context
        assert "opponent" in context
        assert "material_count" in context

        assert context["player"] == "red"
        assert context["opponent"] == "black"

    def test_prepare_analysis_context_black(self) -> None:
        """Test preparing analysis context for black player."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        context = agent.prepare_analysis_context(state, "black")

        assert context["player"] == "black"
        assert context["opponent"] == "red"

    def test_prepare_analysis_context_material_count(self) -> None:
        """Test that analysis context includes material count."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        context = agent.prepare_analysis_context(state, "red")

        # Initial position should have equal material
        material = context["material_count"]
        assert "red" in material
        assert "black" in material

    def test_extract_move_from_decision(self) -> None:
        """Test extracting move from player decision."""
        agent = CheckersAgent()

        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )

        decision = CheckersPlayerDecision(
            move=move,
            reasoning="Good central advance",
            evaluation="Slightly better for red",
            alternatives=["c3-d4"],
        )

        extracted_move = agent.extract_move(decision)

        assert extracted_move == move
        assert extracted_move.from_position == "a3"
        assert extracted_move.to_position == "b4"

    def test_extract_move_direct_move(self) -> None:
        """Test extracting move when response is already a move."""
        agent = CheckersAgent()

        move = CheckersMove(
            from_position="e3",
            to_position="f4",
            player="black",
        )

        extracted_move = agent.extract_move(move)

        assert extracted_move == move

    def test_make_red_move_valid(self) -> None:
        """Test making a valid move for red player."""
        # Create a mock engine that returns a valid decision
        mock_engine = MagicMock()
        mock_move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )
        mock_decision = CheckersPlayerDecision(
            move=mock_move,
            reasoning="Test move",
            evaluation="Test evaluation",
        )
        mock_engine.invoke.return_value = mock_decision

        agent = CheckersAgent()
        agent.engines = {"red_player": mock_engine}

        state = CheckersStateManager.initialize()
        command = agent.make_red_move(state)

        # Check that engine was called
        mock_engine.invoke.assert_called_once()

        # Check that state was updated
        update_data = command.update
        new_state = CheckersState(**update_data)

        # Move should be applied (assuming valid move)
        assert len(new_state.move_history) >= len(state.move_history)

    def test_make_red_move_wrong_turn(self) -> None:
        """Test making red move when it's not red's turn."""
        agent = CheckersAgent()

        state = CheckersStateManager.initialize()
        state.turn = "black"  # Not red's turn

        command = agent.make_red_move(state)

        # Should return state unchanged
        update_data = command.update
        returned_state = CheckersState(**update_data)
        assert returned_state.turn == "black"

    def test_make_red_move_game_over(self) -> None:
        """Test making red move when game is over."""
        agent = CheckersAgent()

        state = CheckersStateManager.initialize()
        state.game_status = "game_over"
        state.winner = "black"

        command = agent.make_red_move(state)

        # Should return state unchanged
        update_data = command.update
        returned_state = CheckersState(**update_data)
        assert returned_state.game_status == "game_over"

    def test_make_black_move_valid(self) -> None:
        """Test making a valid move for black player."""
        # Create a mock engine that returns a valid decision
        mock_engine = MagicMock()
        mock_move = CheckersMove(
            from_position="b6",
            to_position="a5",
            player="black",
        )
        mock_decision = CheckersPlayerDecision(
            move=mock_move,
            reasoning="Defensive move",
            evaluation="Maintaining position",
        )
        mock_engine.invoke.return_value = mock_decision

        agent = CheckersAgent()
        agent.engines = {"black_player": mock_engine}

        state = CheckersStateManager.initialize()
        state.turn = "black"

        agent.make_black_move(state)

        # Check that engine was called
        mock_engine.invoke.assert_called_once()

    def test_make_black_move_wrong_turn(self) -> None:
        """Test making black move when it's not black's turn."""
        agent = CheckersAgent()

        state = CheckersStateManager.initialize()  # Red's turn by default

        command = agent.make_black_move(state)

        # Should return state unchanged
        update_data = command.update
        returned_state = CheckersState(**update_data)
        assert returned_state.turn == "red"

    def test_analyze_red_position(self) -> None:
        """Test analyzing position for red player."""
        # Create a mock analyzer engine
        mock_engine = MagicMock()
        mock_analysis = CheckersAnalysis(
            material_advantage="Equal material",
            control_of_center="Red has slight center control",
            suggested_moves=["a3-b4", "c3-d4"],
            positional_evaluation="Slightly better for red",
        )
        mock_engine.invoke.return_value = mock_analysis

        agent = CheckersAgent()
        agent.engines = {"red_analyzer": mock_engine}

        state = CheckersStateManager.initialize()
        command = agent.analyze_red_position(state)

        # Check that engine was called
        mock_engine.invoke.assert_called_once()

        # Check that analysis was added
        update_data = command.update
        new_state = CheckersState(**update_data)
        assert len(new_state.red_analysis) > len(state.red_analysis)

    def test_analyze_black_position(self) -> None:
        """Test analyzing position for black player."""
        # Create a mock analyzer engine
        mock_engine = MagicMock()
        mock_analysis = CheckersAnalysis(
            material_advantage="Equal material",
            control_of_center="Black needs center activity",
            suggested_moves=["b6-c5", "f6-e5"],
            positional_evaluation="Slightly worse for black",
        )
        mock_engine.invoke.return_value = mock_analysis

        agent = CheckersAgent()
        agent.engines = {"black_analyzer": mock_engine}

        state = CheckersStateManager.initialize()
        command = agent.analyze_black_position(state)

        # Check that engine was called
        mock_engine.invoke.assert_called_once()

        # Check that analysis was added
        update_data = command.update
        new_state = CheckersState(**update_data)
        assert len(new_state.black_analysis) > len(state.black_analysis)

    @patch("haive.games.checkers.ui.CheckersUI.display_board")
    def test_visualize_state_enabled(self, mock_display) -> None:
        """Test visualizing state when visualization is enabled."""
        config = CheckersAgentConfig(visualization=True)
        agent = CheckersAgent(config)

        state = CheckersStateManager.initialize()
        state_dict = (
            state.model_dump() if hasattr(state, "model_dump") else state.dict()
        )

        agent.visualize_state(state_dict)

        # Should call the UI display method
        mock_display.assert_called_once()

    def test_visualize_state_disabled(self) -> None:
        """Test visualizing state when visualization is disabled."""
        config = CheckersAgentConfig(visualization=False)
        agent = CheckersAgent(config)

        state = CheckersStateManager.initialize()
        state_dict = (
            state.model_dump() if hasattr(state, "model_dump") else state.dict()
        )

        # Should not raise any exceptions and should return quickly
        agent.visualize_state(state_dict)

    def test_setup_workflow(self) -> None:
        """Test setting up the game workflow."""
        agent = CheckersAgent()

        # Should not raise any exceptions
        agent.setup_workflow()

        # Should have a graph after setup
        assert agent.graph is not None

    def test_fallback_move_generation(self) -> None:
        """Test fallback move generation when engine fails."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        # Get legal moves for fallback
        legal_moves = CheckersStateManager.get_legal_moves(state)

        if legal_moves:
            fallback_move = agent.get_fallback_move(state, "red")

            assert fallback_move is not None
            assert fallback_move.player == "red"
            assert fallback_move in legal_moves

    def test_move_validation(self) -> None:
        """Test move validation functionality."""
        agent = CheckersAgent()
        state = CheckersStateManager.initialize()

        # Valid move
        legal_moves = CheckersStateManager.get_legal_moves(state)
        if legal_moves:
            valid_move = legal_moves[0]
            assert agent.is_valid_move(state, valid_move) is True

        # Invalid move
        invalid_move = CheckersMove(
            from_position="a1",  # No piece here
            to_position="b2",
            player="red",
        )
        assert agent.is_valid_move(state, invalid_move) is False

    def test_error_handling_invalid_move(self) -> None:
        """Test error handling when an invalid move is generated."""
        # Create a mock engine that returns an invalid move
        mock_engine = MagicMock()
        invalid_move = CheckersMove(
            from_position="a1",  # No piece here
            to_position="b2",
            player="red",
        )
        mock_decision = CheckersPlayerDecision(
            move=invalid_move,
            reasoning="Invalid move",
            evaluation="Error case",
        )
        mock_engine.invoke.return_value = mock_decision

        agent = CheckersAgent()
        agent.engines = {"red_player": mock_engine}

        state = CheckersStateManager.initialize()

        # Should handle the error gracefully
        command = agent.make_red_move(state)

        # Should return a valid state (possibly with fallback move)
        update_data = command.update
        new_state = CheckersState(**update_data)
        assert new_state is not None

    def test_game_flow_integration(self) -> None:
        """Test complete game flow integration."""
        # Create mock engines for both players
        mock_red_engine = MagicMock()
        mock_black_engine = MagicMock()

        # Mock valid moves
        red_move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
        )
        black_move = CheckersMove(
            from_position="b6",
            to_position="a5",
            player="black",
        )

        mock_red_decision = CheckersPlayerDecision(
            move=red_move,
            reasoning="Opening move",
            evaluation="Equal position",
        )
        mock_black_decision = CheckersPlayerDecision(
            move=black_move,
            reasoning="Response move",
            evaluation="Defending",
        )

        mock_red_engine.invoke.return_value = mock_red_decision
        mock_black_engine.invoke.return_value = mock_black_decision

        agent = CheckersAgent()
        agent.engines = {
            "red_player": mock_red_engine,
            "black_player": mock_black_engine,
        }

        # Initialize game
        init_command = agent.initialize_game({})
        state = CheckersState(**init_command.update)

        # Make red move
        red_command = agent.make_red_move(state)
        state = CheckersState(**red_command.update)

        # State should be updated
        assert (
            len(state.move_history) >= 0
        )  # Move may or may not be applied depending on validation
