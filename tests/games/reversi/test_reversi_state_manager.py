"""Test cases for Reversi game state manager.

This module tests the ReversiStateManager class and its methods for managing
game state transitions, move validation, and game logic.
"""

import pytest

from haive.games.reversi.models import Position, ReversiAnalysis, ReversiMove
from haive.games.reversi.state import ReversiState
from haive.games.reversi.state_manager import ReversiStateManager


class TestReversiStateManagerInitialization:
    """Test cases for ReversiStateManager initialization."""

    def test_initialize_default(self) -> None:
        """Test initializing with default parameters."""
        state = ReversiStateManager.initialize()

        assert state.turn == "B"
        assert state.player_B == "player1"
        assert state.player_W == "player2"
        assert state.game_status == "ongoing"
        assert state.skip_count == 0

        # Check initial board setup
        counts = state.disc_count
        assert counts["B"] == 2
        assert counts["W"] == 2

        # Check specific positions
        assert state.board[3][3] == "W"
        assert state.board[3][4] == "B"
        assert state.board[4][3] == "B"
        assert state.board[4][4] == "W"

    def test_initialize_custom_first_player(self) -> None:
        """Test initializing with custom first player."""
        state = ReversiStateManager.initialize(first_player="W")

        assert state.turn == "W"
        assert state.player_B == "player1"
        assert state.player_W == "player2"

    def test_initialize_custom_players(self) -> None:
        """Test initializing with custom player assignments."""
        state = ReversiStateManager.initialize(
            first_player="B",
            player_B="player2",
            player_W="player1",
        )

        assert state.turn == "B"
        assert state.player_B == "player2"
        assert state.player_W == "player1"


class TestGetLegalMoves:
    """Test cases for getting legal moves."""

    def test_get_legal_moves_initial_position(self) -> None:
        """Test getting legal moves from initial position."""
        state = ReversiStateManager.initialize()
        legal_moves = ReversiStateManager.get_legal_moves(state)

        # Initial position should have 4 legal moves for Black
        assert len(legal_moves) == 4

        # Check that all moves are for the current player
        for move in legal_moves:
            assert move.player == "B"

        # Check expected positions (standard Reversi opening)
        expected_positions = {(2, 3), (3, 2), (4, 5), (5, 4)}
        actual_positions = {(move.row, move.col) for move in legal_moves}
        assert actual_positions == expected_positions

    def test_get_legal_moves_white_turn(self) -> None:
        """Test getting legal moves when it's White's turn."""
        state = ReversiStateManager.initialize(first_player="W")
        legal_moves = ReversiStateManager.get_legal_moves(state)

        # Check that all moves are for White
        for move in legal_moves:
            assert move.player == "W"

        # Should have same positions available as Black
        assert len(legal_moves) == 4

    def test_get_legal_moves_no_moves_available(self) -> None:
        """Test getting legal moves when no moves are available."""
        # Create a board where current player has no legal moves
        board = [[None for _ in range(8)] for _ in range(8)]
        # Fill most of the board to create a no-move situation
        for i in range(8):
            for j in range(8):
                if i < 7:  # Leave last row empty
                    board[i][j] = "W"

        state = ReversiState(board=board, turn="B")
        legal_moves = ReversiStateManager.get_legal_moves(state)

        assert len(legal_moves) == 0

    def test_get_legal_moves_after_move(self) -> None:
        """Test getting legal moves after making a move."""
        state = ReversiStateManager.initialize()

        # Make a move
        move = ReversiMove(row=2, col=3, player="B")
        new_state = ReversiStateManager.apply_move(state, move)

        # Get legal moves for White
        legal_moves = ReversiStateManager.get_legal_moves(new_state)

        # All moves should be for White
        for move in legal_moves:
            assert move.player == "W"

        # Should have legal moves available
        assert len(legal_moves) > 0


class TestMoveValidation:
    """Test cases for move validation and application."""

    def test_apply_move_valid(self) -> None:
        """Test applying a valid move."""
        state = ReversiStateManager.initialize()
        move = ReversiMove(row=2, col=3, player="B")

        new_state = ReversiStateManager.apply_move(state, move)

        # Check that the move was added to history
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0] == move

        # Check that the disc was placed
        assert new_state.board[2][3] == "B"

        # Check that turn switched to White
        assert new_state.turn == "W"

        # Check that some discs were flipped
        disc_count = new_state.disc_count
        assert disc_count["B"] > 2  # Should have more than initial 2

    def test_apply_move_wrong_player(self) -> None:
        """Test that applying move for wrong player raises error."""
        state = ReversiStateManager.initialize()  # Black's turn
        move = ReversiMove(row=2, col=3, player="W")  # Wrong player

        with pytest.raises(ValueError, match="Not W's turn"):
            ReversiStateManager.apply_move(state, move)

    def test_apply_move_illegal_position(self) -> None:
        """Test that applying illegal move raises error."""
        state = ReversiStateManager.initialize()
        move = ReversiMove(row=0, col=0, player="B")  # Illegal position

        with pytest.raises(ValueError, match="Illegal move"):
            ReversiStateManager.apply_move(state, move)

    def test_apply_move_occupied_cell(self) -> None:
        """Test that applying move to occupied cell raises error."""
        state = ReversiStateManager.initialize()
        move = ReversiMove(row=3, col=3, player="B")  # Already occupied by White

        with pytest.raises(ValueError, match="Illegal move"):
            ReversiStateManager.apply_move(state, move)

    def test_apply_move_disc_flipping(self) -> None:
        """Test that applying move correctly flips opponent discs."""
        state = ReversiStateManager.initialize()
        move = ReversiMove(row=2, col=3, player="B")

        # Before move: B=2, W=2
        initial_counts = state.disc_count
        assert initial_counts["B"] == 2
        assert initial_counts["W"] == 2

        new_state = ReversiStateManager.apply_move(state, move)

        # After move: should have flipped one White disc
        new_counts = new_state.disc_count
        assert new_counts["B"] == 4  # 2 initial + 1 placed + 1 flipped
        assert new_counts["W"] == 1  # 2 initial - 1 flipped


class TestSkipMoves:
    """Test cases for skip moves when no legal moves available."""

    def test_skip_move_when_no_legal_moves(self) -> None:
        """Test skipping turn when player has no legal moves."""
        # Create a state where current player has no moves
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "W"
        board[3][4] = "W"
        board[4][3] = "W"
        board[4][4] = "W"

        state = ReversiState(board=board, turn="B", skip_count=0)

        # Verify no legal moves
        legal_moves = ReversiStateManager.get_legal_moves(state)
        assert len(legal_moves) == 0

        # Apply skip move
        new_state = ReversiStateManager.get_skip_move(state)

        assert new_state.skip_count == 1
        assert new_state.turn == "W"  # Should switch to other player

    def test_skip_move_increments_counter(self) -> None:
        """Test that skip move increments skip counter."""
        state = ReversiStateManager.initialize()
        state.skip_count = 1

        new_state = ReversiStateManager.get_skip_move(state)

        assert new_state.skip_count == 2


class TestGameStatusChecking:
    """Test cases for game status checking and winning conditions."""

    def test_check_game_status_ongoing(self) -> None:
        """Test game status remains ongoing during normal play."""
        state = ReversiStateManager.initialize()
        checked_state = ReversiStateManager.check_game_status(state)

        assert checked_state.game_status == "ongoing"
        assert checked_state.winner is None

    def test_check_game_status_both_players_skip(self) -> None:
        """Test game ends when both players skip (no legal moves)."""
        # Create a board with Black having more discs
        board = [["B" for _ in range(8)] for _ in range(8)]
        board[7][7] = "W"  # One White disc

        state = ReversiState(
            board=board,
            turn="B",
            skip_count=2,  # Both players skipped
        )

        checked_state = ReversiStateManager.check_game_status(state)

        assert checked_state.game_status == "B_win"
        assert checked_state.winner == "B"

    def test_check_game_status_draw_after_skips(self) -> None:
        """Test game ends in draw when disc counts are equal after skips."""
        # Create a board with equal disc counts
        board = [[None for _ in range(8)] for _ in range(8)]
        board[3][3] = "B"
        board[3][4] = "W"

        state = ReversiState(
            board=board,
            turn="B",
            skip_count=2,  # Both players skipped
        )

        checked_state = ReversiStateManager.check_game_status(state)

        assert checked_state.game_status == "draw"
        assert checked_state.winner is None

    def test_check_game_status_full_board_black_wins(self) -> None:
        """Test game ends when board is full with Black winning."""
        # Create a full board with Black having more discs
        board = [["B" for _ in range(8)] for _ in range(8)]
        # Change some to White so Black still wins but not by much
        for i in range(3):
            for j in range(8):
                board[i][j] = "W"  # 24 White, 40 Black

        state = ReversiState(board=board, turn="B")
        checked_state = ReversiStateManager.check_game_status(state)

        assert checked_state.game_status == "B_win"
        assert checked_state.winner == "B"

    def test_check_game_status_full_board_white_wins(self) -> None:
        """Test game ends when board is full with White winning."""
        # Create a full board with White having more discs
        board = [["W" for _ in range(8)] for _ in range(8)]
        # Change some to Black so White still wins
        for i in range(3):
            for j in range(8):
                board[i][j] = "B"  # 24 Black, 40 White

        state = ReversiState(board=board, turn="W")
        checked_state = ReversiStateManager.check_game_status(state)

        assert checked_state.game_status == "W_win"
        assert checked_state.winner == "W"

    def test_check_game_status_full_board_draw(self) -> None:
        """Test game ends in draw when board is full with equal discs."""
        # Create a full board with equal disc counts
        board = [["B" if i < 4 else "W" for j in range(8)] for i in range(8)]

        state = ReversiState(board=board, turn="B")
        checked_state = ReversiStateManager.check_game_status(state)

        assert checked_state.game_status == "draw"
        assert checked_state.winner is None


class TestGetFlips:
    """Test cases for the _get_flips helper method."""

    def test_get_flips_initial_position(self) -> None:
        """Test getting flips from initial position."""
        state = ReversiStateManager.initialize()

        # Test a legal move
        flips = ReversiStateManager._get_flips(state.board, 2, 3, "B")

        # Should flip one disc
        assert len(flips) == 1
        assert (3, 3) in flips  # Should flip the White disc at (3,3)

    def test_get_flips_no_flips(self) -> None:
        """Test getting flips when no discs would be flipped."""
        state = ReversiStateManager.initialize()

        # Test an illegal move (no flips)
        flips = ReversiStateManager._get_flips(state.board, 0, 0, "B")

        assert len(flips) == 0

    def test_get_flips_multiple_directions(self) -> None:
        """Test getting flips in multiple directions."""
        board = [[None for _ in range(8)] for _ in range(8)]
        # Set up a position where placing at (3,3) flips in multiple directions
        board[3][1] = "B"  # West
        board[3][2] = "W"  # West
        board[1][3] = "B"  # North
        board[2][3] = "W"  # North
        board[3][4] = "W"  # East
        board[3][5] = "B"  # East

        flips = ReversiStateManager._get_flips(board, 3, 3, "B")

        # Should flip discs in three directions
        expected_flips = {(3, 2), (2, 3), (3, 4)}
        assert flips == expected_flips

    def test_get_flips_occupied_cell(self) -> None:
        """Test getting flips for occupied cell returns empty set."""
        state = ReversiStateManager.initialize()

        # Test occupied cell
        flips = ReversiStateManager._get_flips(state.board, 3, 3, "B")

        assert len(flips) == 0


class TestLegalMoveChecking:
    """Test cases for is_legal_move method."""

    def test_is_legal_move_valid(self) -> None:
        """Test is_legal_move with valid move."""
        state = ReversiStateManager.initialize()

        assert ReversiStateManager.is_legal_move(state, 2, 3, "B") is True

    def test_is_legal_move_invalid_position(self) -> None:
        """Test is_legal_move with invalid position."""
        state = ReversiStateManager.initialize()

        assert ReversiStateManager.is_legal_move(state, 0, 0, "B") is False

    def test_is_legal_move_occupied_cell(self) -> None:
        """Test is_legal_move with occupied cell."""
        state = ReversiStateManager.initialize()

        assert ReversiStateManager.is_legal_move(state, 3, 3, "B") is False

    def test_is_legal_move_out_of_bounds(self) -> None:
        """Test is_legal_move with out of bounds positions."""
        state = ReversiStateManager.initialize()

        assert ReversiStateManager.is_legal_move(state, -1, 3, "B") is False
        assert ReversiStateManager.is_legal_move(state, 8, 3, "B") is False
        assert ReversiStateManager.is_legal_move(state, 3, -1, "B") is False
        assert ReversiStateManager.is_legal_move(state, 3, 8, "B") is False


class TestAnalysisManagement:
    """Test cases for analysis management."""

    def test_add_analysis_player1(self) -> None:
        """Test adding analysis for player1."""
        state = ReversiStateManager.initialize()

        analysis = ReversiAnalysis(
            mobility=5,
            frontier_discs=8,
            corner_discs=0,
            stable_discs=2,
            positional_score=10,
            position_evaluation="equal",
            recommended_moves=[Position(row=2, col=3)],
            danger_zones=[],
            strategy="Balanced play",
            reasoning="Good mobility",
        )

        new_state = ReversiStateManager.add_analysis(state, "player1", analysis)

        assert len(new_state.player1_analysis) == 1
        assert new_state.player1_analysis[0] == analysis
        assert len(new_state.player2_analysis) == 0

    def test_add_analysis_player2(self) -> None:
        """Test adding analysis for player2."""
        state = ReversiStateManager.initialize()

        analysis = ReversiAnalysis(
            mobility=3,
            frontier_discs=6,
            corner_discs=1,
            stable_discs=4,
            positional_score=-5,
            position_evaluation="losing",
            recommended_moves=[Position(row=4, col=5)],
            danger_zones=[Position(row=0, col=0)],
            strategy="Defensive play",
            reasoning="Limited options",
        )

        new_state = ReversiStateManager.add_analysis(state, "player2", analysis)

        assert len(new_state.player2_analysis) == 1
        assert new_state.player2_analysis[0] == analysis
        assert len(new_state.player1_analysis) == 0

    def test_get_winner_ongoing_game(self) -> None:
        """Test get_winner for ongoing game."""
        state = ReversiStateManager.initialize()

        winner = ReversiStateManager.get_winner(state)

        assert winner is None

    def test_get_winner_finished_game(self) -> None:
        """Test get_winner for finished game."""
        state = ReversiStateManager.initialize()
        state.game_status = "B_win"
        state.winner = "B"

        winner = ReversiStateManager.get_winner(state)

        assert winner == "B"
