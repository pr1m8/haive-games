"""Comprehensive tests for TicTacToeAgent."""

from unittest.mock import Mock, patch

from langchain_core.runnables import Runnable
from langgraph.types import Command
import pytest

from haive.games.framework.base.agent import GameAgent
from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.models import TicTacToeMove
from haive.games.tic_tac_toe.state import TicTacToeState


class TestTicTacToeAgent:
    """Test suite for TicTacToeAgent functionality."""

    @pytest.fixture
    def mock_engines(self) -> dict[str, Mock]:
        """Create mock LLM engines for testing."""
        x_engine = Mock(spec=Runnable)
        o_engine = Mock(spec=Runnable)
        x_analysis = Mock(spec=Runnable)
        o_analysis = Mock(spec=Runnable)

        return {
            "X_player": x_engine,
            "O_player": o_engine,
            "X_analysis": x_analysis,
            "O_analysis": o_analysis,
        }

    @pytest.fixture
    def agent_config(self, mock_engines: dict[str, Mock]) -> TicTacToeConfig:
        """Create a test agent configuration with mock engines."""
        config = TicTacToeConfig(
            player_X="player1",
            player_O="player2",
            first_player="X",
            enable_analysis=False,
        )
        # We'll patch the engines after agent creation
        return config

    @pytest.fixture
    def tic_tac_toe_agent(
        self, agent_config: TicTacToeConfig, mock_engines: dict[str, Mock]
    ) -> TicTacToeAgent:
        """Create a test TicTacToeAgent instance with mock engines."""
        agent = TicTacToeAgent(agent_config)
        # Replace engines with mocks
        agent.engines = mock_engines
        return agent

    def test_agent_initialization(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test that agent initializes correctly."""
        assert tic_tac_toe_agent is not None
        assert tic_tac_toe_agent.state_manager is not None
        assert isinstance(tic_tac_toe_agent, GameAgent)
        assert tic_tac_toe_agent.config.player_X == "player1"
        assert tic_tac_toe_agent.config.player_O == "player2"

    def test_initialize_game(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test game initialization."""
        # Execute initialization
        command = tic_tac_toe_agent.initialize_game({})

        # Verify command structure
        assert isinstance(command, Command)
        assert command.goto == "make_move"

        # Verify initial state
        update = command.update
        assert update["board"] == [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        assert update["turn"] == "X"  # First player
        assert update["game_status"] == "ongoing"
        assert update["player_X"] == "player1"
        assert update["player_O"] == "player2"
        assert update["winner"] is None
        assert update["error_message"] is None
        assert update["move_history"] == []

    def test_prepare_move_context(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test move context preparation."""
        # Create a test state
        state = TicTacToeState(
            board=[["X", None, None], [None, "O", None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
            move_history=[
                TicTacToeMove(row=0, col=0, player="X"),
                TicTacToeMove(row=1, col=1, player="O"),
            ],
        )

        # Prepare context
        context = tic_tac_toe_agent.prepare_move_context(state)

        # Verify context
        assert "board_string" in context
        assert "current_player" in context
        assert "legal_moves" in context
        assert "player_analysis" in context

        assert context["current_player"] == "X"
        assert "(0, 1)" in context["legal_moves"]
        assert "(0, 2)" in context["legal_moves"]
        assert "(0, 0)" not in context["legal_moves"]  # Already occupied

    def test_prepare_analysis_context(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test analysis context preparation."""
        state = TicTacToeState(
            board=[["X", None, None], [None, None, None], [None, None, None]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        # Prepare context for X
        context = tic_tac_toe_agent.prepare_analysis_context(state, "X")

        assert context["player_symbol"] == "X"
        assert context["opponent_symbol"] == "O"
        assert "board_string" in context

    def test_make_move_success(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test successful move execution."""
        # Setup state
        state = {
            "board": [[None, None, None], [None, None, None], [None, None, None]],
            "turn": "X",
            "game_status": "ongoing",
            "player_X": "player1",
            "player_O": "player2",
            "winner": None,
            "error_message": None,
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
        }

        # Mock engine to return a valid move
        mock_move = TicTacToeMove(row=1, col=1, player="X")
        tic_tac_toe_agent.engines["X_player"].invoke.return_value = mock_move

        # Execute move
        command = tic_tac_toe_agent.make_move(state)

        # Verify engine was called
        tic_tac_toe_agent.engines["X_player"].invoke.assert_called_once()

        # Verify command
        assert isinstance(command, Command)
        assert command.goto == "make_move"  # Game continues

        # Verify state update
        update = command.update
        assert update["board"][1][1] == "X"
        assert update["turn"] == "O"  # Turn switched
        assert update["game_status"] == "ongoing"
        assert len(update["move_history"]) == 1

    def test_make_move_with_invalid_move_retry(
        self, tic_tac_toe_agent: TicTacToeAgent
    ) -> None:
        """Test move retry logic when invalid move is provided."""
        # Setup state with one occupied cell
        state = {
            "board": [["X", None, None], [None, None, None], [None, None, None]],
            "turn": "O",
            "game_status": "ongoing",
            "player_X": "player1",
            "player_O": "player2",
            "winner": None,
            "error_message": None,
            "move_history": [{"row": 0, "col": 0, "player": "X"}],
            "player1_analysis": [],
            "player2_analysis": [],
        }

        # Mock engine to return occupied cell first, then valid move
        invalid_move = TicTacToeMove(row=0, col=0, player="O")  # Already occupied
        valid_move = TicTacToeMove(row=1, col=1, player="O")

        # Mock apply_move to raise ValueError for invalid move
        with patch.object(tic_tac_toe_agent.state_manager, "apply_move") as mock_apply:
            mock_apply.side_effect = [
                ValueError("Cell already occupied"),
                TicTacToeState(
                    board=[["X", None, None], [None, "O", None], [None, None, None]],
                    turn="X",
                    game_status="ongoing",
                    player_X="player1",
                    player_O="player2",
                    move_history=[
                        TicTacToeMove(row=0, col=0, player="X"),
                        TicTacToeMove(row=1, col=1, player="O"),
                    ],
                ),
            ]

            tic_tac_toe_agent.engines["O_player"].invoke.side_effect = [
                invalid_move,
                valid_move,
            ]

            # Execute move
            command = tic_tac_toe_agent.make_move(state)

            # Verify retry happened
            assert tic_tac_toe_agent.engines["O_player"].invoke.call_count == 2
            assert mock_apply.call_count == 2

            # Verify final command
            assert command.goto == "make_move"
            assert command.update["turn"] == "X"

    def test_make_move_game_ending(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test move that ends the game."""
        # Setup state where X can win
        state = {
            "board": [["X", "X", None], ["O", "O", None], [None, None, None]],
            "turn": "X",
            "game_status": "ongoing",
            "player_X": "player1",
            "player_O": "player2",
            "winner": None,
            "error_message": None,
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
        }

        # Mock engine to return winning move
        winning_move = TicTacToeMove(row=0, col=2, player="X")
        tic_tac_toe_agent.engines["X_player"].invoke.return_value = winning_move

        # Mock state manager to return winning state
        winning_state = TicTacToeState(
            board=[["X", "X", "X"], ["O", "O", None], [None, None, None]],
            turn="O",
            game_status="X_win",
            winner="X",
            player_X="player1",
            player_O="player2",
        )

        with patch.object(
            tic_tac_toe_agent.state_manager, "apply_move", return_value=winning_state
        ):
            # Execute move
            command = tic_tac_toe_agent.make_move(state)

            # Verify command directs to END
            assert command.goto == "END"
            assert command.update["game_status"] == "X_win"
            assert command.update["winner"] == "X"

    def test_make_move_with_completed_game(
        self, tic_tac_toe_agent: TicTacToeAgent
    ) -> None:
        """Test handling of move request on completed game."""
        # Setup already completed game
        state = {
            "board": [["X", "X", "X"], ["O", "O", None], [None, None, None]],
            "turn": "O",
            "game_status": "X_win",
            "winner": "X",
            "player_X": "player1",
            "player_O": "player2",
            "error_message": None,
            "move_history": [],
            "player1_analysis": [],
            "player2_analysis": [],
        }

        # Execute move
        command = tic_tac_toe_agent.make_move(state)

        # Should go to END without calling engine
        assert command.goto == "END"
        tic_tac_toe_agent.engines["O_player"].invoke.assert_not_called()

    def test_make_move_state_conversion_error(
        self, tic_tac_toe_agent: TicTacToeAgent
    ) -> None:
        """Test handling of invalid state data."""
        # Invalid state missing required field
        invalid_state = {
            "board": [[None, None, None]],  # Invalid board
            "turn": "X",
            # Missing other required fields
        }

        # Execute move
        command = tic_tac_toe_agent.make_move(invalid_state)

        # Should handle error gracefully
        assert command.goto == "END"
        assert "error_message" in command.update
        assert "State conversion failed" in command.update["error_message"]

    def test_workflow_setup(self, tic_tac_toe_agent: TicTacToeAgent) -> None:
        """Test that workflow is set up correctly."""
        # Mock the graph
        mock_graph = Mock()
        tic_tac_toe_agent.graph = mock_graph

        # Setup workflow
        tic_tac_toe_agent.setup_workflow()

        # Verify core nodes are added
        expected_nodes = ["initialize_game", "player1_move", "player2_move"]
        for node_name in expected_nodes:
            mock_graph.add_node.assert_any_call(node_name, pytest.Any())

        # Verify edges are added
        assert mock_graph.add_edge.call_count > 0

    @pytest.mark.integration
    @pytest.mark.skip(reason="Requires real LLM engines")
    async def test_full_game_flow(self, agent_config: TicTacToeConfig) -> None:
        """Integration test of complete game flow."""
        # Create agent with real engines
        agent = TicTacToeAgent(agent_config)

        # Run a complete game
        result = await agent.arun({})

        # Verify game completed
        assert result["game_status"] in ["X_win", "O_win", "draw"]
        if result["game_status"] != "draw":
            assert result["winner"] in ["X", "O"]

        # Verify move history exists
        assert len(result["move_history"]) >= 5  # Minimum moves for a win
        assert len(result["move_history"]) <= 9  # Maximum possible moves

        # Verify final board state
        board = result["board"]
        moves_on_board = sum(1 for row in board for cell in row if cell is not None)
        assert moves_on_board == len(result["move_history"])
