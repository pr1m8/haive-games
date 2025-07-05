"""Integration tests for TicTacToeAgent with real gameplay."""

from typing import Any, Dict

import pytest

from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig
from haive.games.tic_tac_toe.models import TicTacToeMove
from haive.games.tic_tac_toe.state import TicTacToeState
from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager


class TestTicTacToeIntegration:
    """Integration tests for real Tic Tac Toe gameplay."""

    def test_game_initialization_creates_valid_state(self) -> None:
        """Test that game initialization creates a valid starting state."""
        agent = TicTacToeAgent()

        # Initialize game
        command = agent.initialize_game({})
        state = command.update

        # Verify board is empty
        assert state["board"] == [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        assert state["turn"] in ["X", "O"]
        assert state["game_status"] == "ongoing"
        assert state["winner"] is None
        assert state["move_history"] == []

    def test_state_manager_legal_moves_calculation(self) -> None:
        """Test that legal moves are calculated correctly."""
        # Empty board - all moves should be legal
        state = TicTacToeStateManager.initialize()
        legal_moves = TicTacToeStateManager.get_legal_moves(state)

        assert len(legal_moves) == 9
        for move in legal_moves:
            assert 0 <= move.row <= 2
            assert 0 <= move.col <= 2
            assert move.player == state.turn

        # Partially filled board
        state = TicTacToeState(
            board=[["X", None, None], [None, "O", None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )
        legal_moves = TicTacToeStateManager.get_legal_moves(state)

        assert len(legal_moves) == 7  # 9 - 2 occupied cells
        # Verify occupied cells are not in legal moves
        occupied_positions = {(0, 0), (1, 1)}
        legal_positions = {(move.row, move.col) for move in legal_moves}
        assert occupied_positions.isdisjoint(legal_positions)

    def test_move_application_updates_state_correctly(self) -> None:
        """Test that moves are applied correctly to game state."""
        state = TicTacToeStateManager.initialize()

        # Apply first move
        move = TicTacToeMove(row=1, col=1, player="X")
        new_state = TicTacToeStateManager.apply_move(state, move)

        assert new_state.board[1][1] == "X"
        assert new_state.turn == "O"  # Turn should switch
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0].row == 1
        assert new_state.move_history[0].col == 1
        assert new_state.move_history[0].player == "X"

    def test_illegal_move_raises_error(self) -> None:
        """Test that illegal moves raise appropriate errors."""
        state = TicTacToeState(
            board=[["X", None, None], [None, None, None], [None, None, None]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        # Try to move to occupied cell
        illegal_move = TicTacToeMove(row=0, col=0, player="O")
        with pytest.raises(ValueError, match="already occupied"):
            TicTacToeStateManager.apply_move(state, illegal_move)

        # Try to move out of turn
        wrong_turn_move = TicTacToeMove(row=0, col=1, player="X")  # Should be O's turn
        with pytest.raises(ValueError, match="not your turn"):
            TicTacToeStateManager.apply_move(state, wrong_turn_move)

    def test_win_detection_horizontal(self) -> None:
        """Test horizontal win detection."""
        # Create winning state
        state = TicTacToeState(
            board=[["X", "X", "X"], ["O", "O", None], [None, None, None]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        result_state = TicTacToeStateManager.check_game_status(state)
        assert result_state.game_status == "X_win"
        assert result_state.winner == "X"

    def test_win_detection_vertical(self) -> None:
        """Test vertical win detection."""
        state = TicTacToeState(
            board=[["X", "O", None], ["X", "O", None], ["X", None, None]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        result_state = TicTacToeStateManager.check_game_status(state)
        assert result_state.game_status == "X_win"
        assert result_state.winner == "X"

    def test_win_detection_diagonal(self) -> None:
        """Test diagonal win detection."""
        # Main diagonal
        state = TicTacToeState(
            board=[["X", "O", None], ["O", "X", None], [None, None, "X"]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        result_state = TicTacToeStateManager.check_game_status(state)
        assert result_state.game_status == "X_win"
        assert result_state.winner == "X"

        # Anti-diagonal
        state = TicTacToeState(
            board=[["O", "X", "X"], ["O", "X", "O"], ["X", "O", "O"]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        result_state = TicTacToeStateManager.check_game_status(state)
        assert result_state.game_status == "X_win"
        assert result_state.winner == "X"

    def test_draw_detection(self) -> None:
        """Test draw detection when board is full."""
        # Create a draw board
        state = TicTacToeState(
            board=[["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]],
            turn="O",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        result_state = TicTacToeStateManager.check_game_status(state)
        assert result_state.game_status == "draw"
        assert result_state.winner is None

    def test_winning_move_detection(self) -> None:
        """Test detection of winning moves."""
        # X can win on top row
        state = TicTacToeState(
            board=[["X", "X", None], ["O", "O", None], [None, None, None]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        winning_moves = TicTacToeStateManager.find_winning_move(state, "X")
        assert len(winning_moves) == 1
        assert winning_moves[0] == (0, 2)

        # O can win on middle row
        winning_moves = TicTacToeStateManager.find_winning_move(state, "O")
        assert len(winning_moves) == 1
        assert winning_moves[0] == (1, 2)

    def test_board_string_representation(self) -> None:
        """Test board string formatting."""
        state = TicTacToeState(
            board=[["X", "O", None], ["X", None, "O"], [None, "X", "O"]],
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

        board_str = state.board_string
        assert "X" in board_str
        assert "O" in board_str
        assert "-" in board_str or " " in board_str  # Empty cells representation

        # Verify it's a readable format
        lines = board_str.strip().split("\n")
        assert len(lines) >= 3  # Should have at least 3 rows

    def test_game_state_consistency_after_moves(self) -> None:
        """Test that game state remains consistent through a sequence of moves."""
        state = TicTacToeStateManager.initialize()

        # Sequence of moves
        moves = [
            TicTacToeMove(row=1, col=1, player="X"),  # Center
            TicTacToeMove(row=0, col=0, player="O"),  # Top-left
            TicTacToeMove(row=2, col=2, player="X"),  # Bottom-right
            TicTacToeMove(row=0, col=2, player="O"),  # Top-right
            TicTacToeMove(row=0, col=1, player="X"),  # Top-center - blocks O win
        ]

        for i, move in enumerate(moves):
            # Verify move is legal
            legal_moves = TicTacToeStateManager.get_legal_moves(state)
            legal_positions = {(m.row, m.col) for m in legal_moves}
            assert (move.row, move.col) in legal_positions

            # Apply move
            state = TicTacToeStateManager.apply_move(state, move)

            # Verify consistency
            assert len(state.move_history) == i + 1
            assert state.board[move.row][move.col] == move.player

            # Verify turn alternation
            expected_turn = "O" if move.player == "X" else "X"
            if state.game_status == "ongoing":
                assert state.turn == expected_turn

    def test_move_validation_edge_cases(self) -> None:
        """Test move validation for edge cases."""
        state = TicTacToeStateManager.initialize()

        # Out of bounds moves
        invalid_moves = [
            TicTacToeMove(row=-1, col=0, player="X"),
            TicTacToeMove(row=3, col=0, player="X"),
            TicTacToeMove(row=0, col=-1, player="X"),
            TicTacToeMove(row=0, col=3, player="X"),
        ]

        for invalid_move in invalid_moves:
            with pytest.raises(ValueError):
                TicTacToeStateManager.apply_move(state, invalid_move)

    def test_game_state_immutability(self) -> None:
        """Test that applying moves doesn't modify original state."""
        original_state = TicTacToeStateManager.initialize()
        original_board = [row[:] for row in original_state.board]  # Deep copy

        move = TicTacToeMove(row=1, col=1, player="X")
        new_state = TicTacToeStateManager.apply_move(original_state, move)

        # Original state should be unchanged
        assert original_state.board == original_board
        assert original_state.turn == "X"
        assert len(original_state.move_history) == 0

        # New state should have the move
        assert new_state.board[1][1] == "X"
        assert new_state.turn == "O"
        assert len(new_state.move_history) == 1

    def test_complete_game_simulation(self) -> None:
        """Test a complete game from start to finish."""
        # Simulate a specific game sequence
        state = TicTacToeStateManager.initialize()

        # Game: X wins diagonally
        moves = [
            TicTacToeMove(row=0, col=0, player="X"),
            TicTacToeMove(row=0, col=1, player="O"),
            TicTacToeMove(row=1, col=1, player="X"),
            TicTacToeMove(row=0, col=2, player="O"),
            TicTacToeMove(row=2, col=2, player="X"),  # Winning move
        ]

        for move in moves[:-1]:
            state = TicTacToeStateManager.apply_move(state, move)
            state = TicTacToeStateManager.check_game_status(state)
            assert state.game_status == "ongoing"

        # Apply winning move
        state = TicTacToeStateManager.apply_move(state, moves[-1])
        state = TicTacToeStateManager.check_game_status(state)

        # Verify game ended with X win
        assert state.game_status == "X_win"
        assert state.winner == "X"
        assert len(state.move_history) == 5

        # Verify final board state
        expected_board = [["X", "O", "O"], [None, "X", None], [None, None, "X"]]
        assert state.board == expected_board
