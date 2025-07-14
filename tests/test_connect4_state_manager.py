"""Tests for Connect4 state manager with real component validation.

This module provides comprehensive tests for Connect4 state management including:
    - State initialization and transitions
    - Move validation and application
    - Win condition detection
    - Game flow management
    - Board state integrity

All tests use real components without mocks, following the no-mocks methodology.
"""

from haive.games.connect4.models import Connect4Move
from haive.games.connect4.state import Connect4State
from haive.games.connect4.state_manager import Connect4StateManager


class TestConnect4StateManager:
    """Test suite for Connect4StateManager with real state operations."""

    def test_connect4_state_manager_initialize(self):
        """Test Connect4StateManager initialization creates valid initial state."""
        state = Connect4StateManager.initialize()

        # Check state type
        assert isinstance(state, Connect4State)

        # Check board structure
        assert len(state.board) == 6
        assert all(len(row) == 7 for row in state.board)
        assert all(cell is None for row in state.board for cell in row)

        # Check initial values
        assert state.turn == "red"
        assert state.move_history == []
        assert state.red_analysis == []
        assert state.yellow_analysis == []
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert state.captured is None
        assert state.error_message is None

    def test_connect4_state_manager_get_legal_moves_empty_board(self):
        """Test Connect4StateManager get_legal_moves for empty board."""
        state = Connect4StateManager.initialize()
        legal_moves = Connect4StateManager.get_legal_moves(state)

        # All columns should be legal on empty board
        assert len(legal_moves) == 7
        for i, move in enumerate(legal_moves):
            assert isinstance(move, Connect4Move)
            assert move.column == i

    def test_connect4_state_manager_get_legal_moves_partially_filled(self):
        """Test Connect4StateManager get_legal_moves with partially filled board."""
        state = Connect4StateManager.initialize()

        # Fill column 3 partially (3 pieces)
        state.board[5][3] = "red"
        state.board[4][3] = "yellow"
        state.board[3][3] = "red"

        legal_moves = Connect4StateManager.get_legal_moves(state)

        # All columns should still be legal
        assert len(legal_moves) == 7
        column_numbers = [move.column for move in legal_moves]
        assert set(column_numbers) == {0, 1, 2, 3, 4, 5, 6}

    def test_connect4_state_manager_get_legal_moves_full_column(self):
        """Test Connect4StateManager get_legal_moves with full column."""
        state = Connect4StateManager.initialize()

        # Fill column 3 completely
        for row in range(6):
            state.board[row][3] = "red" if row % 2 == 0 else "yellow"

        legal_moves = Connect4StateManager.get_legal_moves(state)

        # Column 3 should not be legal
        assert len(legal_moves) == 6
        column_numbers = [move.column for move in legal_moves]
        assert 3 not in column_numbers
        assert set(column_numbers) == {0, 1, 2, 4, 5, 6}

    def test_connect4_state_manager_get_legal_moves_multiple_full_columns(self):
        """Test Connect4StateManager get_legal_moves with multiple full columns."""
        state = Connect4StateManager.initialize()

        # Fill columns 2, 3, and 5 completely
        for col in [2, 3, 5]:
            for row in range(6):
                state.board[row][col] = "red" if row % 2 == 0 else "yellow"

        legal_moves = Connect4StateManager.get_legal_moves(state)

        # Only columns 0, 1, 4, 6 should be legal
        assert len(legal_moves) == 4
        column_numbers = [move.column for move in legal_moves]
        assert set(column_numbers) == {0, 1, 4, 6}

    def test_connect4_state_manager_get_legal_moves_board_full(self):
        """Test Connect4StateManager get_legal_moves with completely full board."""
        state = Connect4StateManager.initialize()

        # Fill entire board
        for col in range(7):
            for row in range(6):
                state.board[row][col] = "red" if (row + col) % 2 == 0 else "yellow"

        legal_moves = Connect4StateManager.get_legal_moves(state)

        # No legal moves should be available
        assert len(legal_moves) == 0

    def test_connect4_state_manager_is_valid_move_valid_moves(self):
        """Test Connect4StateManager is_valid_move for valid moves."""
        state = Connect4StateManager.initialize()

        # All columns should be valid initially
        for col in range(7):
            move = Connect4Move(column=col)
            assert Connect4StateManager.is_valid_move(state, move)

    def test_connect4_state_manager_is_valid_move_invalid_column_full(self):
        """Test Connect4StateManager is_valid_move for full column."""
        state = Connect4StateManager.initialize()

        # Fill column 3 completely
        for row in range(6):
            state.board[row][3] = "red" if row % 2 == 0 else "yellow"

        move = Connect4Move(column=3)
        assert not Connect4StateManager.is_valid_move(state, move)

    def test_connect4_state_manager_is_valid_move_invalid_column_out_of_bounds(self):
        """Test Connect4StateManager is_valid_move for out of bounds columns."""
        state = Connect4StateManager.initialize()

        # Negative column
        move_neg = Connect4Move(column=-1)
        assert not Connect4StateManager.is_valid_move(state, move_neg)

        # Column too high
        move_high = Connect4Move(column=7)
        assert not Connect4StateManager.is_valid_move(state, move_high)

    def test_connect4_state_manager_apply_move_empty_column(self):
        """Test Connect4StateManager apply_move to empty column."""
        state = Connect4StateManager.initialize()
        move = Connect4Move(column=3, explanation="Center control")

        new_state = Connect4StateManager.apply_move(state, move)

        # Check piece placement
        assert new_state.board[5][3] == "red"  # Bottom row
        assert all(new_state.board[row][3] is None for row in range(5))

        # Check turn switch
        assert new_state.turn == "yellow"

        # Check move history
        assert len(new_state.move_history) == 1
        assert new_state.move_history[0].column == 3
        assert new_state.move_history[0].explanation == "Center control"

        # Check game status
        assert new_state.game_status == "ongoing"
        assert new_state.winner is None

    def test_connect4_state_manager_apply_move_stacking(self):
        """Test Connect4StateManager apply_move with piece stacking."""
        state = Connect4StateManager.initialize()

        # Place first piece (red)
        move1 = Connect4Move(column=3)
        state = Connect4StateManager.apply_move(state, move1)
        assert state.board[5][3] == "red"
        assert state.turn == "yellow"

        # Place second piece (yellow) in same column
        move2 = Connect4Move(column=3)
        state = Connect4StateManager.apply_move(state, move2)
        assert state.board[5][3] == "red"  # Bottom piece unchanged
        assert state.board[4][3] == "yellow"  # New piece on top
        assert state.turn == "red"

        # Place third piece (red) in same column
        move3 = Connect4Move(column=3)
        state = Connect4StateManager.apply_move(state, move3)
        assert state.board[5][3] == "red"  # Bottom piece unchanged
        assert state.board[4][3] == "yellow"  # Middle piece unchanged
        assert state.board[3][3] == "red"  # New piece on top
        assert state.turn == "yellow"

    def test_connect4_state_manager_apply_move_multiple_columns(self):
        """Test Connect4StateManager apply_move across multiple columns."""
        state = Connect4StateManager.initialize()

        moves = [
            Connect4Move(column=3),  # Red
            Connect4Move(column=4),  # Yellow
            Connect4Move(column=2),  # Red
            Connect4Move(column=5),  # Yellow
        ]

        for move in moves:
            state = Connect4StateManager.apply_move(state, move)

        # Check piece placement
        assert state.board[5][3] == "red"
        assert state.board[5][4] == "yellow"
        assert state.board[5][2] == "red"
        assert state.board[5][5] == "yellow"

        # Check final turn
        assert state.turn == "red"

        # Check move history
        assert len(state.move_history) == 4

    def test_connect4_state_manager_apply_move_invalid_move_full_column(self):
        """Test Connect4StateManager apply_move with invalid move to full column."""
        state = Connect4StateManager.initialize()

        # Fill column 3 completely
        for row in range(6):
            state.board[row][3] = "red" if row % 2 == 0 else "yellow"

        move = Connect4Move(column=3)

        # Apply move should handle invalid move gracefully
        new_state = Connect4StateManager.apply_move(state, move)

        # State should indicate error
        assert new_state.error_message is not None
        assert "full" in new_state.error_message.lower()

        # Board should be unchanged
        assert new_state.board == state.board

        # Turn should be unchanged
        assert new_state.turn == state.turn

    def test_connect4_state_manager_check_win_horizontal(self):
        """Test Connect4StateManager win detection for horizontal wins."""
        state = Connect4StateManager.initialize()

        # Create horizontal win for red in bottom row
        for col in range(4):
            state.board[5][col] = "red"

        # Test win detection
        assert Connect4StateManager._check_win(state, 5, 3)  # Any of the winning pieces
        assert Connect4StateManager._check_win(state, 5, 0)
        assert Connect4StateManager._check_win(state, 5, 1)
        assert Connect4StateManager._check_win(state, 5, 2)

    def test_connect4_state_manager_check_win_vertical(self):
        """Test Connect4StateManager win detection for vertical wins."""
        state = Connect4StateManager.initialize()

        # Create vertical win for yellow in column 3
        for row in range(2, 6):  # Rows 2, 3, 4, 5
            state.board[row][3] = "yellow"

        # Test win detection
        assert Connect4StateManager._check_win(state, 2, 3)
        assert Connect4StateManager._check_win(state, 3, 3)
        assert Connect4StateManager._check_win(state, 4, 3)
        assert Connect4StateManager._check_win(state, 5, 3)

    def test_connect4_state_manager_check_win_diagonal_positive(self):
        """Test Connect4StateManager win detection for positive diagonal wins."""
        state = Connect4StateManager.initialize()

        # Create positive diagonal win (bottom-left to top-right) for red
        positions = [(5, 1), (4, 2), (3, 3), (2, 4)]
        for row, col in positions:
            state.board[row][col] = "red"

        # Test win detection
        for row, col in positions:
            assert Connect4StateManager._check_win(state, row, col)

    def test_connect4_state_manager_check_win_diagonal_negative(self):
        """Test Connect4StateManager win detection for negative diagonal wins."""
        state = Connect4StateManager.initialize()

        # Create negative diagonal win (top-left to bottom-right) for yellow
        positions = [(2, 1), (3, 2), (4, 3), (5, 4)]
        for row, col in positions:
            state.board[row][col] = "yellow"

        # Test win detection
        for row, col in positions:
            assert Connect4StateManager._check_win(state, row, col)

    def test_connect4_state_manager_check_win_no_win(self):
        """Test Connect4StateManager win detection when no win exists."""
        state = Connect4StateManager.initialize()

        # Place scattered pieces with no winning pattern
        positions = [(5, 1), (5, 3), (4, 2), (3, 5), (2, 0)]
        for i, (row, col) in enumerate(positions):
            state.board[row][col] = "red" if i % 2 == 0 else "yellow"

        # Test no false positives
        for row, col in positions:
            assert not Connect4StateManager._check_win(state, row, col)

    def test_connect4_state_manager_check_win_almost_win_horizontal(self):
        """Test Connect4StateManager win detection for almost-wins (3 in a row)."""
        state = Connect4StateManager.initialize()

        # Create 3 in a row horizontally (not a win)
        for col in range(3):
            state.board[5][col] = "red"

        # Should not detect win
        for col in range(3):
            assert not Connect4StateManager._check_win(state, 5, col)

    def test_connect4_state_manager_check_win_five_in_a_row(self):
        """Test Connect4StateManager win detection for more than 4 in a row."""
        state = Connect4StateManager.initialize()

        # Create 5 in a row horizontally
        for col in range(5):
            state.board[5][col] = "red"

        # Should still detect win
        for col in range(5):
            assert Connect4StateManager._check_win(state, 5, col)

    def test_connect4_state_manager_apply_move_with_win_horizontal(self):
        """Test Connect4StateManager apply_move that results in horizontal win."""
        state = Connect4StateManager.initialize()

        # Set up 3 in a row
        state.board[5][0] = "red"
        state.board[5][1] = "red"
        state.board[5][2] = "red"
        state.turn = "red"

        # Complete the win
        winning_move = Connect4Move(column=3)
        new_state = Connect4StateManager.apply_move(state, winning_move)

        # Check win detection
        assert new_state.game_status == "red_win"
        assert new_state.winner == "red"
        assert new_state.board[5][3] == "red"

    def test_connect4_state_manager_apply_move_with_win_vertical(self):
        """Test Connect4StateManager apply_move that results in vertical win."""
        state = Connect4StateManager.initialize()

        # Set up 3 in a column
        state.board[5][3] = "yellow"
        state.board[4][3] = "yellow"
        state.board[3][3] = "yellow"
        state.turn = "yellow"

        # Complete the win
        winning_move = Connect4Move(column=3)
        new_state = Connect4StateManager.apply_move(state, winning_move)

        # Check win detection
        assert new_state.game_status == "yellow_win"
        assert new_state.winner == "yellow"
        assert new_state.board[2][3] == "yellow"

    def test_connect4_state_manager_apply_move_with_draw(self):
        """Test Connect4StateManager apply_move that results in a draw."""
        state = Connect4StateManager.initialize()

        # Fill board almost completely with no wins
        pattern = [
            ["red", "yellow", "red", "yellow", "red", "yellow", "red"],
            ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"],
            ["red", "yellow", "red", "yellow", "red", "yellow", "red"],
            ["yellow", "red", "yellow", "red", "yellow", "red", "yellow"],
            ["red", "yellow", "red", "yellow", "red", "yellow", "red"],
            ["yellow", "red", "yellow", "red", "yellow", "red", None],  # One empty spot
        ]

        for row in range(6):
            for col in range(7):
                state.board[row][col] = pattern[row][col]

        state.turn = "yellow"

        # Fill the last spot
        final_move = Connect4Move(column=6)
        new_state = Connect4StateManager.apply_move(state, final_move)

        # Check draw detection
        assert new_state.game_status == "draw"
        assert new_state.winner is None

    def test_connect4_state_manager_complex_game_scenario(self):
        """Test Connect4StateManager with complex realistic game scenario."""
        state = Connect4StateManager.initialize()

        # Play a realistic game sequence
        moves = [
            Connect4Move(column=3),  # Red: Center
            Connect4Move(column=3),  # Yellow: Stack center
            Connect4Move(column=4),  # Red: Right of center
            Connect4Move(column=2),  # Yellow: Left of center
            Connect4Move(column=5),  # Red: Far right
            Connect4Move(column=4),  # Yellow: Stack right
            Connect4Move(column=1),  # Red: Far left
            Connect4Move(column=4),  # Yellow: Stack right more
        ]

        for move in moves:
            state = Connect4StateManager.apply_move(state, move)

        # Verify board state
        assert state.board[5][3] == "red"  # Bottom center
        assert state.board[4][3] == "yellow"  # Above center
        assert state.board[5][4] == "red"  # Bottom right
        assert state.board[4][4] == "yellow"  # Above right
        assert state.board[3][4] == "yellow"  # Top of right stack
        assert state.board[5][2] == "yellow"  # Bottom left
        assert state.board[5][5] == "red"  # Bottom far right
        assert state.board[5][1] == "red"  # Bottom far left

        # Verify game continues
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert state.turn == "red"

        # Verify move history
        assert len(state.move_history) == 8
        assert all(isinstance(move, Connect4Move) for move in state.move_history)

    def test_connect4_state_manager_edge_case_corner_wins(self):
        """Test Connect4StateManager win detection in board corners."""
        state = Connect4StateManager.initialize()

        # Test corner diagonal win (bottom-left to top-right)
        corner_positions = [(5, 0), (4, 1), (3, 2), (2, 3)]
        for row, col in corner_positions:
            state.board[row][col] = "red"

        # Verify win detection
        for row, col in corner_positions:
            assert Connect4StateManager._check_win(state, row, col)

    def test_connect4_state_manager_state_immutability(self):
        """Test Connect4StateManager preserves original state immutability."""
        original_state = Connect4StateManager.initialize()
        original_board = [row[:] for row in original_state.board]  # Deep copy

        move = Connect4Move(column=3)
        new_state = Connect4StateManager.apply_move(original_state, move)

        # Original state should be unchanged
        assert original_state.board == original_board
        assert original_state.turn == "red"
        assert original_state.move_history == []

        # New state should be different
        assert new_state.board != original_board
        assert new_state.turn == "yellow"
        assert len(new_state.move_history) == 1

    def test_connect4_state_manager_error_handling_invalid_coordinates(self):
        """Test Connect4StateManager error handling for invalid coordinates."""
        state = Connect4StateManager.initialize()

        # Test out-of-bounds moves
        invalid_moves = [
            Connect4Move(column=-1),
            Connect4Move(column=7),
            Connect4Move(column=100),
        ]

        for move in invalid_moves:
            new_state = Connect4StateManager.apply_move(state, move)

            # Should handle gracefully with error message
            assert new_state.error_message is not None
            assert new_state.board == state.board  # Board unchanged
            assert new_state.turn == state.turn  # Turn unchanged
