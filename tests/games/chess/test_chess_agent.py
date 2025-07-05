"""Unit tests for chess agent.

This module tests the ChessAgent class, including graph construction,
move generation, and game flow management.
"""

import pytest

from haive.games.chess.agent import ChessAgent
from haive.games.chess.config import ChessConfig
from haive.games.chess.engines import RandomChessEngine
from haive.games.chess.state import ChessState


class TestChessAgent:
    """Test suite for ChessAgent."""

    @pytest.fixture
    def random_engine(self) -> RandomChessEngine:
        """Create a random chess engine for testing."""
        return RandomChessEngine()

    @pytest.fixture
    def chess_config(self, random_engine: RandomChessEngine) -> ChessConfig:
        """Create a chess configuration for testing."""
        return ChessConfig(
            name="test_chess",
            white_player="AI",
            black_player="AI",
            enable_analysis=False,
            max_turns=100,
            engines={"white": random_engine, "black": random_engine},
        )

    @pytest.fixture
    def chess_agent(self, chess_config: ChessConfig) -> ChessAgent:
        """Create a ChessAgent instance for testing."""
        return ChessAgent(chess_config)

    def test_chess_agent_initialization(
        self, chess_agent: ChessAgent, chess_config: ChessConfig
    ) -> None:
        """Test that ChessAgent initializes correctly."""
        # Assert
        assert chess_agent.config == chess_config
        assert chess_agent.graph is not None
        assert chess_agent._app is not None
        assert hasattr(chess_agent, "make_move")
        assert hasattr(chess_agent, "check_game_status")

    def test_graph_construction_without_analysis(
        self, chess_config: ChessConfig
    ) -> None:
        """Test graph construction when analysis is disabled."""
        # Arrange
        chess_config.enable_analysis = False

        # Act
        agent = ChessAgent(chess_config)

        # Assert
        # Check that graph has expected nodes
        nodes = list(agent.graph.nodes)
        assert "white_move" in nodes
        assert "black_move" in nodes
        assert "check_game_status" in nodes
        assert "white_analysis" not in nodes
        assert "black_analysis" not in nodes

    def test_graph_construction_with_analysis(self, chess_config: ChessConfig) -> None:
        """Test graph construction when analysis is enabled."""
        # Arrange
        chess_config.enable_analysis = True

        # Act
        agent = ChessAgent(chess_config)

        # Assert
        # Check that graph has analysis nodes
        nodes = list(agent.graph.nodes)
        assert "white_move" in nodes
        assert "black_move" in nodes
        assert "check_game_status" in nodes
        assert "white_analysis" in nodes
        assert "black_analysis" in nodes

    def test_make_move_generates_valid_move(self, chess_agent: ChessAgent) -> None:
        """Test that make_move generates a valid move command."""
        # Arrange
        state = ChessState()

        # Act
        result = chess_agent.make_move(state, "white")

        # Assert
        assert result.update is not None
        assert "move_history" in result.update
        assert len(result.update["move_history"]) > 0

        # Verify the move is valid
        move_color, move_uci = result.update["move_history"][-1]
        assert move_color == "white"
        assert len(move_uci) >= 4  # Valid UCI format

    def test_make_move_updates_board_state(self, chess_agent: ChessAgent) -> None:
        """Test that make_move correctly updates the board state."""
        # Arrange
        state = ChessState()

        # Act
        result = chess_agent.make_move(state, "white")

        # Assert
        assert "board_fen" in result.update
        assert result.update["board_fen"] != state.board_fen
        assert "turn" in result.update
        assert result.update["turn"] == "black"

    def test_make_move_handles_special_moves(self, chess_agent: ChessAgent) -> None:
        """Test that make_move can handle castling and other special moves."""
        # Arrange - Position where castling is possible
        state = ChessState()
        state.board_fen = "r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1"

        # Act - Make several moves to test different scenarios
        result = chess_agent.make_move(state, "white")

        # Assert
        assert result.update is not None
        assert "move_history" in result.update
        # The RandomEngine should be able to find valid moves
        assert len(result.update["move_history"]) > 0

    def test_check_game_status_detects_ongoing_game(
        self, chess_agent: ChessAgent
    ) -> None:
        """Test that check_game_status correctly identifies ongoing game."""
        # Arrange
        state = ChessState()

        # Act
        result = chess_agent.check_game_status(state)

        # Assert
        assert result.graph == "continue"

    def test_check_game_status_detects_checkmate(self, chess_agent: ChessAgent) -> None:
        """Test that check_game_status correctly identifies checkmate."""
        # Arrange
        state = ChessState()
        state.game_status = "checkmate"
        state.game_result = "white_win"

        # Act
        result = chess_agent.check_game_status(state)

        # Assert
        assert result.graph == "game_over"

    def test_check_game_status_detects_draw(self, chess_agent: ChessAgent) -> None:
        """Test that check_game_status correctly identifies draw."""
        # Arrange
        state = ChessState()
        state.game_status = "draw"
        state.game_result = "draw"

        # Act
        result = chess_agent.check_game_status(state)

        # Assert
        assert result.graph == "game_over"

    def test_check_game_status_respects_max_turns(
        self, chess_agent: ChessAgent
    ) -> None:
        """Test that game ends when max turns is reached."""
        # Arrange
        state = ChessState()
        chess_agent.config.max_turns = 10
        state.move_history = [("white", f"move{i}") for i in range(10)]

        # Act
        result = chess_agent.check_game_status(state)

        # Assert
        assert result.graph == "game_over"
        assert state.game_status == "draw"
        assert state.game_result == "draw_max_turns"

    def test_white_move_method(self, chess_agent: ChessAgent) -> None:
        """Test the white_move method correctly makes a white move."""
        # Arrange
        state = ChessState()

        # Act
        result = chess_agent.make_white_move(state)

        # Assert
        assert result.update is not None
        assert "move_history" in result.update
        move_color, _ = result.update["move_history"][-1]
        assert move_color == "white"

    def test_black_move_method(self, chess_agent: ChessAgent) -> None:
        """Test the black_move method correctly makes a black move."""
        # Arrange
        state = ChessState()
        state.turn = "black"
        # Make a white move first to set up the board
        state.board_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
        state.move_history = [("white", "e2e4")]

        # Act
        result = chess_agent.make_black_move(state)

        # Assert
        assert result.update is not None
        assert "move_history" in result.update
        # Should have both the initial white move and new black move
        assert len(result.update["move_history"]) == 2
        move_color, _ = result.update["move_history"][-1]
        assert move_color == "black"

    def test_full_game_flow(self, chess_agent: ChessAgent) -> None:
        """Test a few moves of a complete game flow."""
        # Arrange
        state = ChessState()
        chess_agent.config.max_turns = 10  # Limit for quick test

        # Act - Play a few moves
        moves_played = 0
        for i in range(6):  # Play 3 moves each
            color = "white" if i % 2 == 0 else "black"
            result = chess_agent.make_move(state, color)

            if result.update:
                state = ChessState(**{**state.model_dump(), **result.update})
                moves_played += 1

        # Assert
        assert moves_played == 6
        assert len(state.move_history) == 6
        assert state.turn == "white"  # After 6 moves, should be white's turn
