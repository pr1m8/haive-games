"""Real gameplay tests for TicTacToeAgent with LLM engines."""

import os
from typing import Any, Dict

import pytest
from haive.core.engine.aug_llm import AugLLMConfig

from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig


class TestTicTacToeGameplay:
    """Tests for real TicTacToe gameplay with LLM engines."""

    @pytest.fixture
    def simple_config(self) -> TicTacToeConfig:
        """Create a simple config for testing."""
        return TicTacToeConfig(
            player_X="player1",
            player_O="player2",
            first_player="X",
            enable_analysis=False,
        )

    @pytest.fixture
    def llm_config(self) -> TicTacToeConfig:
        """Create config with real LLM engines if API key available."""
        # Check if we have API keys for testing
        has_openai = bool(os.getenv("OPENAI_API_KEY"))
        has_anthropic = bool(os.getenv("ANTHROPIC_API_KEY"))

        if not (has_openai or has_anthropic):
            pytest.skip("No LLM API keys available for testing")

        # Use simple, fast model for testing
        llm_config = AugLLMConfig(
            model="gpt-3.5-turbo" if has_openai else "claude-3-haiku-20240307",
            temperature=0.7,
            max_tokens=150,
        )

        return TicTacToeConfig(
            player_X="player1",
            player_O="player2",
            first_player="X",
            enable_analysis=False,
            engines={"X_player": llm_config, "O_player": llm_config},
        )

    def test_agent_creation(self, simple_config: TicTacToeConfig) -> None:
        """Test agent can be created successfully."""
        agent = TicTacToeAgent(simple_config)
        assert agent is not None
        assert agent.config.player_X == "player1"
        assert agent.config.player_O == "player2"

    def test_game_initialization_workflow(self, simple_config: TicTacToeConfig) -> None:
        """Test that game initialization works correctly."""
        agent = TicTacToeAgent(simple_config)

        # Test initialization
        result = agent.initialize_game({})

        assert result.goto == "make_move"
        assert result.update["game_status"] == "ongoing"
        assert result.update["turn"] in ["X", "O"]
        assert result.update["winner"] is None

    def test_context_preparation(self, simple_config: TicTacToeConfig) -> None:
        """Test that move context is prepared correctly."""
        agent = TicTacToeAgent(simple_config)

        # Create a test state
        from haive.games.tic_tac_toe.state import TicTacToeState

        state = TicTacToeState(
            board=[["X", None, "O"], [None, "X", None], ["O", None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        context = agent.prepare_move_context(state)

        # Verify context contains required fields
        required_fields = [
            "board_string",
            "current_player",
            "legal_moves",
            "player_analysis",
        ]
        for field in required_fields:
            assert field in context

        # Verify content makes sense
        assert context["current_player"] == "X"
        assert "(" in context["legal_moves"]  # Should contain move coordinates
        assert ")" in context["legal_moves"]

        # Legal moves should not include occupied positions
        legal_moves_str = context["legal_moves"]
        assert "(0, 0)" not in legal_moves_str  # X occupied
        assert "(0, 2)" not in legal_moves_str  # O occupied
        assert "(1, 1)" not in legal_moves_str  # X occupied
        assert "(2, 0)" not in legal_moves_str  # O occupied

    def test_analysis_context_preparation(self, simple_config: TicTacToeConfig) -> None:
        """Test analysis context preparation."""
        agent = TicTacToeAgent(simple_config)

        from haive.games.tic_tac_toe.state import TicTacToeState

        state = TicTacToeState(
            board=[["X", None, None], [None, "O", None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        # Test context for X
        context_x = agent.prepare_analysis_context(state, "X")
        assert context_x["player_symbol"] == "X"
        assert context_x["opponent_symbol"] == "O"
        assert "board_string" in context_x

        # Test context for O
        context_o = agent.prepare_analysis_context(state, "O")
        assert context_o["player_symbol"] == "O"
        assert context_o["opponent_symbol"] == "X"

    @pytest.mark.integration
    @pytest.mark.slow
    def test_complete_game_with_llm(self, llm_config: TicTacToeConfig) -> None:
        """Test a complete game with real LLM engines."""
        agent = TicTacToeAgent(llm_config)

        try:
            # Run a complete game
            result = agent.run({})

            # Verify game completed
            assert "game_status" in result
            assert result["game_status"] in ["X_win", "O_win", "draw", "error"]

            # If game didn't error, verify valid end state
            if result["game_status"] != "error":
                assert "board" in result
                assert "move_history" in result

                # Check move history is reasonable
                move_count = len(result["move_history"])
                assert 3 <= move_count <= 9  # Minimum 3 for win, max 9 for draw

                # Verify winner is consistent with game status
                if result["game_status"] == "X_win":
                    assert result.get("winner") == "X"
                elif result["game_status"] == "O_win":
                    assert result.get("winner") == "O"
                elif result["game_status"] == "draw":
                    assert result.get("winner") is None
                    assert move_count == 9  # Draw means board is full

        except Exception as e:
            # If test fails due to API issues, that's acceptable
            if "API" in str(e) or "rate limit" in str(e).lower():
                pytest.skip(f"API error during testing: {e}")
            else:
                raise

    @pytest.mark.integration
    def test_game_state_transitions(self, simple_config: TicTacToeConfig) -> None:
        """Test game state transitions without LLM calls."""
        agent = TicTacToeAgent(simple_config)

        # Test state conversion from dict to TicTacToeState
        state_dict = {
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

        # This would normally call LLM engines, but we can test state handling
        # by checking that invalid states are handled properly
        invalid_state = {"invalid": "state"}

        result = agent.make_move(invalid_state)
        assert result.goto == "END"
        assert "error_message" in result.update

    def test_completed_game_handling(self, simple_config: TicTacToeConfig) -> None:
        """Test handling of already completed games."""
        agent = TicTacToeAgent(simple_config)

        completed_state = {
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

        result = agent.make_move(completed_state)
        assert result.goto == "END"
        # Should not attempt to make a move on completed game

    def test_error_state_handling(self, simple_config: TicTacToeConfig) -> None:
        """Test handling of error states."""
        agent = TicTacToeAgent(simple_config)

        # Test with missing required state fields
        incomplete_state = {
            "board": [[None, None, None], [None, None, None], [None, None, None]],
            "turn": "X",
            # Missing other required fields
        }

        result = agent.make_move(incomplete_state)
        assert result.goto == "END"
        assert "error_message" in result.update

    @pytest.mark.performance
    def test_game_performance_bounds(self, simple_config: TicTacToeConfig) -> None:
        """Test that game operations complete within reasonable time."""
        import time

        agent = TicTacToeAgent(simple_config)

        # Test initialization performance
        start_time = time.time()
        result = agent.initialize_game({})
        init_time = time.time() - start_time

        assert init_time < 1.0  # Should initialize quickly
        assert result.goto == "make_move"

        # Test context preparation performance
        from haive.games.tic_tac_toe.state import TicTacToeState

        state = TicTacToeState(
            board=[["X", None, None], [None, "O", None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        start_time = time.time()
        context = agent.prepare_move_context(state)
        context_time = time.time() - start_time

        assert context_time < 0.1  # Context prep should be very fast
        assert len(context) > 0

    def test_board_representation_quality(self, simple_config: TicTacToeConfig) -> None:
        """Test that board representations are clear and correct."""
        from haive.games.tic_tac_toe.state import TicTacToeState

        # Test various board states
        test_boards = [
            # Empty board
            [[None, None, None], [None, None, None], [None, None, None]],
            # Partially filled
            [["X", None, "O"], [None, "X", None], ["O", None, None]],
            # Full board
            [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]],
        ]

        for board in test_boards:
            state = TicTacToeState(
                board=board,
                turn="X",
                game_status="ongoing",
                player_X="player1",
                player_O="player2",
            )

            board_str = state.board_string

            # Verify board string contains expected elements
            assert isinstance(board_str, str)
            assert len(board_str) > 0

            # Count X's and O's in string representation
            x_count = sum(1 for row in board for cell in row if cell == "X")
            o_count = sum(1 for row in board for cell in row if cell == "O")

            if x_count > 0:
                assert "X" in board_str
            if o_count > 0:
                assert "O" in board_str
